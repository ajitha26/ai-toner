import requests

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3"
headers = {
    "Authorization": "Bearer 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"
}

data = {
    "inputs": "What's the weather like in Paris?"
}

response = requests.post(API_URL, headers=headers, json=data)
print(response.json())
