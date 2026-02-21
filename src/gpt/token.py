import tiktoken

def count_tokens(text: str) -> int:
    encoding = tiktoken.get_encoding("cl100k_base")
    return len(encoding.encode(text))

def total_tokens_used(messages: list) -> int:
    try:
        count = sum(count_tokens(msg["content"]) for msg in messages)
        return count
    except Exception as e:
        return 0

def enforce_token_budget(messages: list, budget: int = 10) -> None:
    try:
        while total_tokens_used(messages) > budget:
            if len(messages) <= 2:
                break
            messages.pop(1)
    except Exception as e:
        print(f"Error enforcing token budget: {e}")
