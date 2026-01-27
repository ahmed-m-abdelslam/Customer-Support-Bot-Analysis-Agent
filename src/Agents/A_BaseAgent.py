from Helpers.config import get_settings
from crewai import  LLM  # type: ignore
from pathlib import Path 

class BaseAgent:
    def __init__(self):
        self.settings = get_settings()

    @staticmethod
    def get_llm(llm_name: str ,
            temperature: float = 0 ,
            base_url: str = "" ,
            api_key: str = "",
            max_tokens : int = 1000
            ) -> LLM:

        llm = LLM(model = llm_name,
                   temperature = temperature, 
                   base_url = base_url, 
                   api_key = api_key, 
                   max_tokens = max_tokens
                   )
  
        return llm
    
    def data_path(self) -> Path:
        
        base_dir = Path(__file__).resolve().parents[1]  # src
        data_dir = base_dir / "Outputs"
        
        data_dir.mkdir(parents=True, exist_ok=True)

        return data_dir  