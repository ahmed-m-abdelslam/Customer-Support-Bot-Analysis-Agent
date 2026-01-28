from pydantic_settings import BaseSettings  # type: ignore

class Settings(BaseSettings):
    
    OPENAI_API_KEY: str
    OPENAI_MODEL: str
    APP_NAME: str 
    APP_VERSION: str 

  
   

    
    class Config:
        env_file = ".env"
        
def get_settings():
    return Settings()