from Agents.BaseAgent import BaseAgent
from crewai import Agent , Task # type: ignore
from Schema.conversation import FinalResponse

class ResponseAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.llm = self.get_llm(
            llm_name=self.settings.OPENAI_MODEL,
            api_key=self.settings.OPENAI_API_KEY,

        )
    def run(self):
        agent= Agent(
            name = "Response Agent",
            role="Response Generator",
            goal="Generate a polite, helpful final customer response",
            backstory="Customer experience and tone-control expert",
            llm=self.llm,
            verbose=False
        )

        task = Task(
        description="""
            Generate a final customer-facing response.
            - Use friendly Arabic(Egyptian accent) tone
            - Match customer tone
            - Be clear and helpful
            """,
        agent=agent,
        output_file="Outputs/final_response.json",
        expected_output="Final customer response",
        output_json = FinalResponse,
        )
        return agent , task
