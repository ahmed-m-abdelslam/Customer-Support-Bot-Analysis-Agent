from Agents import ConversationParserAgent , ContextBuilderAgent
from crewai import  Crew , Process   # type: ignore
import json


with open("Data/CustomerSupportSample.json", "r", encoding="utf-8") as f:
    data = json.load(f)

Conversation_Parser = ConversationParserAgent()
Context_Builder = ContextBuilderAgent()


agent1, task1 = Conversation_Parser.run()
agent2, task2 = Context_Builder.run()



crew = Crew(
            agents=[agent1,
                    agent2
                ], 
            tasks=[task1,
                   task2
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
