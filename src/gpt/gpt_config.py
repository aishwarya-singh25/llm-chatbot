""" A file containing gpt configuration. """

class GPTConfig:
    GPT_ENDPOINT = "https://api.openai.com/v1/chat/completions"
    MODEL = "gpt-3.5-turbo"
    TEMPERATURE = 0.7
    SYSTEM_PROMPT = "Greet user Good Morning."
    USER_PROMPT = "Please plan my day!"
    MAX_TOKENS = 20
    TOKEN_BUDGET = 10

GPT_CONFIG_OBJ = GPTConfig()