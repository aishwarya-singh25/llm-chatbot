""" A file containing gpt configuration. """

class GPTConfig:
    GPT_ENDPOINT = "https://api.openai.com/v1/chat/completions"
    DEFAULT_BASE_URL = "https://api.together.xyz/v1"
    MODEL = "gpt-3.5-turbo"
    DEFAULT_MODEL = "meta-llama/Meta-Llama-3-8B-Instruct-Lite" # Link to models: https://api.together.ai/models
    TEMPERATURE = 0.7
    SYSTEM_PROMPT = "Use the tools provided to answer the user's question."
    USER_PROMPT = "Hi"
    MAX_TOKENS = 50
    TOKEN_BUDGET = 100

GPT_CONFIG_OBJ = GPTConfig()