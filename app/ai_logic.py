import requests
from app.config import HUGGINGFACE_API_KEY
import re

import re

def clean_llm_output(text):
    pattern = re.compile(
        r"(Explain the following in a fun and casual way within 100 words\.?\s*"
        r"Do not start with any headings, emojis, or introductions\.?\s*Go directly to the explanation and complete within 100 words in full sentences:?\s*)"
        r"|"
        r"(Provide a formal and concise explanation of the following topic within 100 words\.?\s*"
        r"Do not include introductions or headings\.?\s*Go directly to the explanation and complete within 100 words in full sentences:?\s*)",
        re.IGNORECASE
    )
    return pattern.sub("", text).strip()


API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3"
headers = {
    "Authorization": f"Bearer {HUGGINGFACE_API_KEY}"
}

def query_model(prompt: str):
    payload = {
        "inputs": prompt,
        "parameters": {
        "max_new_tokens": 120
        }
    }
    #headers = {"Content-Type": "application/json"}

    response = requests.post(API_URL, json=payload, headers=headers)
    
    print("🟡 Raw response text:", response.text)  # Add this line
    print("🟡 Status code:", response.status_code)

    try:
        result = response.json()
        print("🟢 Parsed JSON:", result)
        return result[0]["generated_text"]  # This is the risky part
    except Exception as e:
        print("❌ Error decoding model response:", str(e))
        return "⚠️ Model failed to respond properly"


def generate_responses(user_query):
    casual_prompt = (
        "Explain the following in a fun and casual way within 100 words. "
        "Do not start with any headings, emojis, or introductions. Go directly to the explanation and complete within 100 words in full sentences:"
        f"{user_query}"
    )

    formal_prompt = (
        "Provide a formal and concise explanation of the following topic within 100 words."
        "Do not include introductions or headings. Go directly to the explanation and complete within 100 words in full sentences:"
        f"{user_query}"
    )
    raw_response = query_model(casual_prompt)
    pattern= re.compile(
        r"(Explain the following in a fun and casual way within 100 words\.?\s*"
        r"Do not start with any headings, emojis, or introductions\.?\s*Go directly to the explanation and complete within 100 words in full sentences:?\s*)"
        r"|"
        r"(Provide a formal and concise explanation of the following topic within 100 words\.?\s*"
        r"Do not include introductions or headings\.?\s*Go directly to the explanation and complete within 100 words in full sentences:?\s*)"
        rf"{user_query}",
        re.IGNORECASE
    )
    casual_response=pattern.sub("", raw_response).strip()
    

    raw_response = query_model(formal_prompt)
    pattern= re.compile(
        r"(Explain the following in a fun and casual way within 100 words\.?\s*"
        r"Do not start with any headings, emojis, or introductions\.?\s*Go directly to the explanation and complete within 100 words in full sentences:?\s*)"
        r"|"
        r"(Provide a formal and concise explanation of the following topic within 100 words\.?\s*"
        r"Do not include introductions or headings\.?\s*Go directly to the explanation and complete within 100 words in full sentences:?\s*)"
        rf"{user_query}",
        re.IGNORECASE
    )
    formal_response=pattern.sub("", raw_response).strip()
    

    return casual_response, formal_response