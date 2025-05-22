import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
