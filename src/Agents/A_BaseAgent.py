from Helpers.config import get_settings
class BaseAgent:
    def __init__(self):
        self.settings = get_settings()
        
    @staticmethod
    def llm(llm_name: str ,
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