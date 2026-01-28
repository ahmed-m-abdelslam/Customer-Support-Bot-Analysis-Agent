from pydantic import BaseModel # type: ignore

class AnalyzeRequest(BaseModel):
    data_row: int
