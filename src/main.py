from Agents.A_ConversationParserAgent import ConversationParserAgent
from crewai import  Crew , Process   # type: ignore
import json


with open("Data/CustomerSupportSample.json", "r", encoding="utf-8") as f:
    data = json.load(f)

Conversation_Parser = ConversationParserAgent()

agent1, task1 = Conversation_Parser.run()



crew = Crew(
            agents=[agent1,
     
                ], 
            tasks=[task1,
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
