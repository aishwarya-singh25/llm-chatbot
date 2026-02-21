from pydantic import BaseModel
from typing import List


class ChatBotRequest(BaseModel):
    user_message: str
    plan: str
    tool_used: List[str]

