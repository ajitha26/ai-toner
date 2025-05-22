from app.database import Prompt, SessionLocal

def save_prompt(user_id, query, casual, formal):
    db = SessionLocal()
    prompt = Prompt(user_id=user_id, query=query,
                    casual_response=casual, formal_response=formal)
    db.add(prompt)
    db.commit()
    db.close()

def get_history(user_id):
    db = SessionLocal()
    prompts = db.query(Prompt).filter(Prompt.user_id == user_id).order_by(Prompt.created_at.desc()).all()
    db.close()
    return prompts