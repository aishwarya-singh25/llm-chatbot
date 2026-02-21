import os
from dotenv import load_dotenv
from openai import OpenAI

from src.gpt.gpt_config import GPTConfig
from src.gpt.token import get_encoding, total_tokens_used, enforce_token_budget
from src.gpt.prompts import SYSTEM_PROMPT
from common_util.app_constant import APP_CONSTANTS_OBJ as Constant


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY not set in .env")

print("OpenAI API Key loaded successfully!")
client = OpenAI(api_key=OPENAI_API_KEY)
ENCODING = get_encoding()


# import inspect, sys
# print("GPTConfig module:", GPTConfig.__module__)
# print("GPTConfig file:", inspect.getfile(GPTConfig))
# print("GPTConfig attrs:", [a for a in dir(GPTConfig) if not a.startswith('_')])
# print("sys.path (first entries):", sys.path[:6])

## load prompt from src.gpt.prompt.py
system_prompt = SYSTEM_PROMPT if SYSTEM_PROMPT else GPTConfig.SYSTEM_PROMPT

message = [{
    "role": "system", "content": system_prompt
    }]

def main(user_input):
    message.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model=GPTConfig.MODEL,
        messages=message,
        temperature=GPTConfig.TEMPERATURE,
        max_tokens=GPTConfig.MAX_TOKENS
    )

    reply = response.choices[0].message.content
    message.append({"role": "assistant", "content": reply})

    enforce_token_budget(message, budget=GPTConfig.TOKEN_BUDGET)
    return reply

while True:
    user_input = input("You: ")
    if user_input.strip().lower() in ["exit", "quit"]:
        print("Exiting chat.")
        break
    answer=main(user_input)
    print("You: ", user_input)
    print("Assistant:", answer)
    print("Total tokens used in conversation:", total_tokens_used(message))