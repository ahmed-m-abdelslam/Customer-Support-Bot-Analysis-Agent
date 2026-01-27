from openai import OpenAI # type: ignore
from .A_BaseAgent import BaseAgent
client = OpenAI()

class IntentDetectionAgent(BaseAgent):
    def run(self, context_summary: str):
        prompt = f"""
        You are a customer support analyst.
        Classify the main intent of this conversation into one of:
        Order Issue, Pickup, Return, Payment, Complaint, General Inquiry

        Conversation:
        {context_summary}

        Return only the intent label.
        """

        response = client.chat.completions.create(
            model=self.settings.OPENAI_MODEL,
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content.strip()
