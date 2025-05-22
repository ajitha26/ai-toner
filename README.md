# README.md
# AI Tone Switcher Web App

## Overview
A web app that uses prompt engineering to generate responses in casual and formal tones using HuggingFace APIs, stores them in PostgreSQL, and displays via Streamlit UI.

## Tech Stack
- FastAPI
- PostgreSQL
- HuggingFace Transformers
- Streamlit
- SQLAlchemy
- dotenv

## Setup
```bash
git clone <repo_url>
cd project_root
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Make sure PostgreSQL is running and update `.env` accordingly.

## Run Backend
```bash
uvicorn app.main:app --reload
```

## Run Frontend
```bash
streamlit run frontend/streamlit_app.py
```

## Testing
```bash
pytest tests/
```
