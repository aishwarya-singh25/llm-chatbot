import tiktoken

def get_encoding() -> tiktoken.Encoding:
    return tiktoken.get_encoding("cl100k_base")

def count_tokens(text: str) -> int:
    return len(get_encoding().encode(text))

def total_tokens_used(messages: list) -> int:
    try:
        return sum(count_tokens(msg["content"]) for msg in messages)
    except Exception as e:
        print(f"Error counting tokens: {e}")
        return 0

def enforce_token_budget(messages: list, budget: int = 10) -> None:
    try:
        while total_tokens_used(messages) > budget:
            if len(messages) <= 2:
                break
            messages.pop(1)
    except Exception as e:
        print(f"Error enforcing token budget: {e}")
