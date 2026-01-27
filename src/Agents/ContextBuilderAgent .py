from Agents.BaseAgent import BaseAgent
from crewai import Agent , Task # type: ignore
from Schema.conversation import ConversationContext

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
            
            expected_output="A JSON object containing Conversation user messages , agent messages and statistics",
            output_json = ConversationContext,
            output_file= "Outputs/context_summary.json",
            agent= agent,
        )

        return agent , task