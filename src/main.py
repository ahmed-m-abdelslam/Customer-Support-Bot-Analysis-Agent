from Agents import ConversationParserAgent , ContextBuilderAgent , IntentDetectionAgent , SentimentAgent , DecisionAgent , ResponseAgent
from crewai import  Crew , Process   # type: ignore
import json
import os
from Helpers.config import get_settings

os.environ["OPENAI_API_KEY"] = get_settings().OPENAI_API_KEY


with open("Data/CustomerSupportSample.json", "r", encoding="utf-8") as f:
    data = json.load(f)

Conversation_Parser = ConversationParserAgent()
Context_Builder = ContextBuilderAgent()
Intent_Detection = IntentDetectionAgent()
Sentiment_Analyzer = SentimentAgent()
Decision_Maker = DecisionAgent()
Response_Generator = ResponseAgent()

agent1, task1 = Conversation_Parser.run()
agent2, task2 = Context_Builder.run()
agent3, task3 = Intent_Detection.run(task_name=task2)
agent4, task4 = Sentiment_Analyzer.run(task_name=task2)
agent5, task5 = Decision_Maker.run(task1_name=task3, task2_name=task4)
agent6, task6 = Response_Generator.run()

crew = Crew(
            agents=[agent1,
                    agent2,
                    agent3,
                    agent4,
                    agent5,
                    agent6
                ], 
            tasks=[task1,
                   task2,
                   task3,
                   task4,
                   task5,
                   task6
            ],
            process = Process.sequential,
            tracing=True
            )

conversation= data[0]["conversation"]
        
crew_results = crew.kickoff(
                 inputs={
                    "conversation": conversation,
            }
        )
