# session_utils.py

import os
import json
from datetime import datetime

SESSIONS_DIR = "chat_sessions"
os.makedirs(SESSIONS_DIR, exist_ok=True)

# Return saved chat titles (list of filenames without .json)
def load_chat_titles():
    return [f[:-5] for f in os.listdir(SESSIONS_DIR) if f.endswith(".json")]

# Load session messages
def load_chat_session(title):
    try:
        with open(os.path.join(SESSIONS_DIR, f"{title}.json"), "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return [{"role": "system", "content": "You are a helpful assistant."}]

# Save session messages
def save_chat_session(title, messages):
    with open(os.path.join(SESSIONS_DIR, f"{title}.json"), "w") as f:
        json.dump(messages, f, indent=2)

# Generate a chat title using timestamp and first message
def generate_new_title(user_input):
    prefix = user_input.strip().split(" ")[0:4]  # First few words
    short_title = "_".join(prefix).strip().replace(" ", "_")
    return f"{short_title}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
