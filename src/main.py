from Agents import ConversationParserAgent , ContextBuilderAgent , IntentDetectionAgent
from crewai import  Crew , Process   # type: ignore
import json


with open("Data/CustomerSupportSample.json", "r", encoding="utf-8") as f:
    data = json.load(f)

Conversation_Parser = ConversationParserAgent()
Context_Builder = ContextBuilderAgent()
Intent_Detection = IntentDetectionAgent()


agent1, task1 = Conversation_Parser.run()
agent2, task2 = Context_Builder.run()
agent3, task3 = Intent_Detection.run()


crew = Crew(
            agents=[agent1,
                    agent2,
                    agent3
                ], 
            tasks=[task1,
                   task2,
                   task3
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
#print(crew_results.raw)
