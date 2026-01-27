from Agents.A_BaseAgent import BaseAgent
from crewai import Agent , Task , LLM # type: ignore

class ConversationParserAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.llm = self.get_llm(
            llm_name=self.settings.OPENAI_MODEL,
            api_key=self.settings.OPENAI_API_KEY,

        )

    def run(self):
        agent = Agent(
            name="Conversation Parser",
            role="Conversation Parser Agent",
            goal="Convert raw customer support chat into structured conversation turns",
            backstory="Expert in text parsing and conversation normalization",
            llm=self.llm,
            verbose=False,
        )

        task =Task(
            description="""
                Parse the raw conversation text into structured turns.
                Each turn must include:
                - speaker (User or Agent)
                - message
                - position
                """,
            agent= agent,
            expected_output="List of structured conversation turns"
        )

        return agent , task


