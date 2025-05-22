from sqlalchemy import create_engine, Column, String, Text, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid
from app.config import DATABASE_URL
from datetime import datetime

Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Prompt(Base):
    __tablename__ = "prompts"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String)
    query = Column(Text)
    casual_response = Column(Text)
    formal_response = Column(Text)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)