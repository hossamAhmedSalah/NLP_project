import requests

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": "Bearer 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"}

def summarize_text(text):
    payload = {
    "inputs": text,
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()[0]
