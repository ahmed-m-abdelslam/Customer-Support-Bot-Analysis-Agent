from Agents.BaseAgent import BaseAgent
from crewai import Agent , Task # type: ignore
from Schema.conversation import AllTurns

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
                conversation = {conversation}
                Parse the raw conversation text into structured turns.
                Each turn must include:
                - Speaker (User or Agent)
                - Message
                - Position
                
                """,
            
            expected_output="A JSON object containing list of structured conversation turns",
            output_json = AllTurns,
            output_file= "Outputs/parsed_conversation.json",
            agent= agent,
        )

        return agent , task


