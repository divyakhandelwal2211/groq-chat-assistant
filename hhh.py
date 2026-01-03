import requests
from dotenv import load_dotenv
import os

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")# Replace with your actual key

# print("KEY VALUE:", GROQ_API_KEY)
# print("KEY LENGTH:", len(GROQ_API_KEY) if GROQ_API_KEY else "None")


headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "llama-3.3-70b-versatile",
    "messages": [
        {"role": "system", "content": "You are a professional proofreader. Correct the grammar of the sentence."},
        {"role": "user", "content": "He don't like apples."}
    ]
}

response = requests.post(
    "https://api.groq.com/openai/v1/chat/completions",
    headers=headers,
    json=data
)


if response.status_code == 200:
    print(response.json()["choices"][0]["message"]["content"])
else:
    print("Error:", response.text)