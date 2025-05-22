from pydantic import BaseModel

class PromptRequest(BaseModel):
    user_id: str
    query: str

class PromptResponse(BaseModel):
    casual_response: str
    formal_response: str