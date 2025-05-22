from fastapi import FastAPI, Depends
from app.models import PromptRequest, PromptResponse
from app.crud import save_prompt, get_history
from app.ai_logic import generate_responses
from app.database import Base, engine, get_db
from fastapi.middleware.cors import CORSMiddleware
from typing import List

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate", response_model=PromptResponse)
def generate(prompt_request: PromptRequest):
   
    casual, formal = generate_responses(prompt_request.query)
    print("CASUAL",casual)
    save_prompt(prompt_request.user_id, prompt_request.query, casual, formal)
    return {"casual_response": casual, "formal_response": formal}

@app.get("/history")
def history(user_id: str):
    prompts = get_history(user_id)
    return [
        {
            "query": p.query,
            "casual_response": p.casual_response,
            "formal_response": p.formal_response,
            "created_at": p.created_at
        } for p in prompts
    ]

