import tiktoken
from src.gpt.gpt_config import GPTConfig

class ChatGPTTokenizer:
    def __init__(self):
        self.encoding = tiktoken.get_encoding("cl100k_base")
        self.token_budget = GPTConfig.TOKEN_BUDGET

    
    def count_tokens(self, text: str) -> int:
        encoding = self.encoding
        return len(encoding.encode(text))

    def total_tokens_used(self, messages: list) -> int:
        try:
            count = sum(self.count_tokens(msg["content"]) for msg in messages)
            return count
        except Exception as e:
            return 0

    def enforce_token_budget(self, messages: list, budget: int = 10) -> None:
        try:
            while self.total_tokens_used(messages) > budget:
                if len(messages) <= 2:
                    break
                messages.pop(1)
        except Exception as e:
            print(f"Error enforcing token budget: {e}")

GPT_TOKENIZER_OBJ = ChatGPTTokenizer()