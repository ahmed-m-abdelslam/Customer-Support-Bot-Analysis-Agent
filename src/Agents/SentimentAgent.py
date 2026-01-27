from Agents.BaseAgent import BaseAgent
from crewai import Agent , Task # type: ignore
from Schema.conversation import SentimentAnalysis

class SentimentAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.llm = self.get_llm(
            llm_name=self.settings.OPENAI_MODEL,
            api_key=self.settings.OPENAI_API_KEY,

        )
    def run(self , task_name):
        agent= Agent(
            name = "Sentiment & Urgency Analyzer",
            role="Sentiment & Urgency Analyzer",
            goal="Detect customer sentiment and urgency level",
            backstory="Behavioral analysis expert for customer interactions",
            llm=self.llm,
            verbose=False
        )
        task = Task(
        description="""
            Analyze customer sentiment and urgency.
            Return JSON:
            {
            "sentiment": "Positive | Neutral | Negative",
            "urgency": "Low | Medium | High"
            }
            """,
        agent=agent,
        output_file="Outputs/sentiment_analysis.json",
        expected_output="A JSON object containing sentiment and urgency labels",
        output_json = SentimentAnalysis,
        context=[task_name]
        )
        return agent , task
