from fastapi import FastAPI # type: ignore
from Routes import agents , base
import os
from Helpers.config import get_settings

app = FastAPI()
os.environ["OPENAI_API_KEY"] = get_settings().OPENAI_API_KEY

app.include_router(base.base_router)
app.include_router(agents.agent_router)