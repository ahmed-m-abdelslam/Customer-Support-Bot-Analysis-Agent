from Agents.BaseAgent import BaseAgent
from crewai import Agent , Task # type: ignore
from Schema.conversation import DecisionOutcome

class DecisionAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.llm = self.get_llm(
            llm_name=self.settings.OPENAI_MODEL,
            api_key=self.settings.OPENAI_API_KEY,

        )
    def run(self, task1_name, task2_name):
        agent= Agent(
            name = "Decision Agent",
            role="Decision Analyst",
            goal="Decide the next best action to handle the customer case",
            backstory="Expert in customer support decision making",
            llm=self.llm,
            verbose=False
        )
        task = Task(
        description="""
            Based on intent, sentiment, and urgency:
            Choose ONE action:
            - Answer Directly
            - Ask Clarification
            - Escalate to Human
            """,
        agent=agent,
        output_file="Outputs/decision_outcome.json",
        expected_output="Single action label",
        output_json = DecisionOutcome,
        context=[task1_name , task2_name]
        )
        return agent , task
