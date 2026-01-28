from fastapi import  APIRouter  , Request # type: ignore
from Agents import ConversationParserAgent , ContextBuilderAgent , IntentDetectionAgent , SentimentAgent , DecisionAgent , ResponseAgent
from crewai import  Crew , Process   # type: ignore
from Helpers.data_loader import load_data





agent_router = APIRouter(
    prefix="/api/v1/agent",
    tags=["api_v1","agent"]
)

@agent_router.post("/index/data")
async def process_conversation( request: Request, payload: dict ):
    
    data = load_data()

    conversation= data[payload["data_row"]]["conversation"]
        
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
                tracing=False
                )
            
    crew_results = crew.kickoff(
                    inputs={
                        "conversation": conversation,
                }
            )

    return {"result": crew_results.raw}