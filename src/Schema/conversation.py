from pydantic import BaseModel , Field # type: ignore
from typing import List


class Turn(BaseModel):
    speaker: str = Field(..., description="Speaker of the turn, either 'User' or 'Agent'")
    message: str = Field(..., description="Content of the message")
    position: int = Field(..., description="Position of the turn in the conversation")

class AllTurns(BaseModel):
    turns: List[Turn]

class Statistics(BaseModel):
    repetition: str
    length: int

class ConversationContext(BaseModel):
    user_messages: List[str] = Field(..., description="List of messages from the user")
    agent_messages: List[str] = Field(..., description="List of messages from the agent")
    summary: str = Field(..., description="Summary of the conversation")
    stats: Statistics = Field(..., description="Statistics related to the conversation")

class SentimentAnalysis(BaseModel):
    sentiment: str = Field(..., description="Sentiment of the customer: Positive, Neutral, Negative")
    urgency: str = Field(..., description="Urgency level of the customer: Low, Medium, High")

class IntentDetection(BaseModel):
    intent: str = Field(..., description="Main customer intent: Order Issue, Pickup, Return, Payment, Complaint, General Inquiry")

class DecisionOutcome(BaseModel):
    action: str = Field(..., description="Decided action: Answer Directly, Ask Clarification, Call Tool, Escalate to Human")

class FinalResponse(BaseModel):
    response: str = Field(..., description="Final response to the customer")