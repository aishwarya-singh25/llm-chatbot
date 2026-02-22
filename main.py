import os
import json
import logging as log
from dotenv import load_dotenv
from openai import OpenAI

from common_util.app_constant import Constants
from common_util.gpt_config import GPTConfig
from src.gpt.tools import get_recipe_data
from src.gpt.tools import tools
from src.gpt.token import GPT_TOKENIZER_OBJ


load_dotenv()
log.basicConfig(level=log.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY not set in .env")

log.info(f"OpenAI API Key for {Constants.APP_NAME} loaded successfully!")
client = OpenAI(api_key=OPENAI_API_KEY)

message = [{
    "role": "system", "content": GPTConfig.SYSTEM_PROMPT
    }]

def chat(user_input):
    message.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model=GPTConfig.MODEL,
        messages=message,
        tools=tools,
        temperature=GPTConfig.TEMPERATURE,
        max_tokens=GPTConfig.MAX_TOKENS
    )
    assistant_message = response.choices[0].message

    # Check if the model has made any tool calls
    if assistant_message.tool_calls:
        message.append(assistant_message)

        tool_calls = assistant_message.tool_calls[0]
        function_name = tool_calls.function.name
        arguments = json.loads(tool_calls.function.arguments)

        print(f"Model requested: {function_name} with arguments {arguments}")
        result = get_recipe_data(arguments["recipe_name"])
        
        message.append({
            "role": "tool",
            "tool_call_id": tool_calls.id,
            "content": json.dumps(result)
        })

        finally_response = client.chat.completions.create(
            model=GPTConfig.MODEL,
            messages=message,
            tools=tools,
            temperature=GPTConfig.TEMPERATURE,
            max_tokens=GPTConfig.MAX_TOKENS
        )
    
    else:
        finally_response = response

    reply = finally_response.choices[0].message.content
    message.append({"role": "assistant", "content": reply})

    GPT_TOKENIZER_OBJ.enforce_token_budget(message, budget=GPTConfig.TOKEN_BUDGET)
    return reply

while True:
    user_input = input("You: ")
    if user_input.strip().lower() in ["exit", "quit"]:
        print("Exiting chat.")
        break
    answer=chat(user_input)
    print("You: ", user_input)
    print("Assistant:", answer)
    print("Total tokens used in conversation:", GPT_TOKENIZER_OBJ.total_tokens_used(message))