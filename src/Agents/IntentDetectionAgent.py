from Agents.BaseAgent import BaseAgent
from crewai import Agent , Task # type: ignore
from Schema.conversation import IntentDetection

class IntentDetectionAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.llm = self.get_llm(
            llm_name=self.settings.OPENAI_MODEL,
            api_key=self.settings.OPENAI_API_KEY,

        )
    def run(self, task_name):
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
        output_file="Outputs/intent_detection.json",
        expected_output="Single intent label",
        output_json = IntentDetection,
        context=[task_name]
        )
        return agent , task
