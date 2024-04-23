import requests

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"
headers = {"Authorization": "Bearer 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"}

def summarize_text(text):
    payload = {
    "inputs": text,
    "parameters": {"candidate_labels": ["refund", "legal", "faq"]},
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
