from pydantic import BaseModel # type: ignore
from typing import List

class Turn(BaseModel):
    speaker: str
    message: str
    position: int


class ConversationContext(BaseModel):
    user_messages: List[str]
    agent_messages: List[str]
    summary: str
    stats: dict
