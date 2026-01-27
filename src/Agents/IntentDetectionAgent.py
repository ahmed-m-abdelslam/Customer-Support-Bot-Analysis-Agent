from Agents.BaseAgent import BaseAgent
from crewai import Agent , Task # type: ignore

class IntentDetectionAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.llm = self.get_llm(
            llm_name=self.settings.OPENAI_MODEL,
            api_key=self.settings.OPENAI_API_KEY,

        )
    def run(self):
        agent= Agent(
            name = "Intent Detection Agent",
            role="Intent Detection Analyst",
            goal="Identify the main customer intent from the conversation",
            backstory="Customer support NLP expert trained on real chat logs",
            llm=self.llm,
            verbose=False
        )
        task = Task(
        description="""
            Identify the main customer intent.
            Choose ONE label only:
            Order Issue, Pickup, Return, Payment, Complaint, General Inquiry
            """,
        agent=agent,
        output_file="Outputs/intent_detection.txt",
        expected_output="Single intent label"
            )
        return agent , task
