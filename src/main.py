from fastapi import FastAPI # type: ignore
from Routes import agents , base
import os
from fastapi.middleware.cors import CORSMiddleware # type: ignore
from Helpers.config import get_settings

app = FastAPI()
os.environ["OPENAI_API_KEY"] = get_settings().OPENAI_API_KEY
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # أثناء التطوير
    allow_credentials=True,
    allow_methods=["*"],      # يسمح بـ OPTIONS
    allow_headers=["*"],
)
app.include_router(base.base_router)
app.include_router(agents.agent_router)