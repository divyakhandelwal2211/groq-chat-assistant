import requests

API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL_NAME = "llama-3.3-70b-versatile"


def get_groq_response(api_key, messages):
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    payload = {"model": MODEL_NAME, "messages": messages, "temperature": 0.7}

    try:
        response = requests.post(API_URL, headers=headers, json=payload)

        # 🔍 DEBUG: agar error aaye to actual response dikhe
        if response.status_code != 200:
            return f"❌ Groq API Error {response.status_code}: {response.text}"

        data = response.json()

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        return f"❌ Error calling Groq API: {str(e)}"
