from Agents.A_BaseAgent import BaseAgent
from crewai import Agent , Task # type: ignore
from Schema.conversation import AllTurns

class ContextBuilderAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.llm = self.get_llm(
            llm_name=self.settings.OPENAI_MODEL,
            api_key=self.settings.OPENAI_API_KEY,

        )

    def run(self):
        agent = Agent(
            name="Context Builder",
            role="Context Builder Agent",
            goal="Build context from structured conversation turns for customer support analysis",
            backstory="Specialist in summarization and conversation analytics",
            llm=self.llm,
            verbose=False,
        )

        task =Task(
            description="""
                Using the parsed conversation turns:
                - Extract user messages
                - Extract agent messages
                - Generate a short summary
                - Compute interaction statistics (repetition, length)
                """,
            
            expected_output="Conversation context object with summary and statistics",
            output_file= "Outputs/context_summary.json",
            agent= agent,
        )

        return agent , task