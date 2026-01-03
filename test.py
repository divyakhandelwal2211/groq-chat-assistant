import streamlit as st
import requests
import os
import json
from dotenv import load_dotenv

st.set_page_config(page_title="Chatbot with Groq", page_icon="🤖")

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

if not GROQ_API_KEY:
    st.error("❌ GROQ_API_KEY not found.")
    st.stop()

# Constants
API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL_NAME = "llama3-8b-8192"
HISTORY_FILE = "all_chats.json"

# Load all chat sessions from file
def load_all_chats():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return {}

# Save all chats to file
def save_all_chats(chat_data):
    with open(HISTORY_FILE, "w") as f:
        json.dump(chat_data, f, indent=2)

# Load all chats into session state
if "all_chats" not in st.session_state:
    st.session_state.all_chats = load_all_chats()

# Set current chat title
if "chat_title" not in st.session_state:
    st.session_state.chat_title = None

# Sidebar: list previous chat titles
with st.sidebar:
    st.title("📚 Saved Chats")

    chat_titles = list(st.session_state.all_chats.keys())
    selected_title = st.radio("Select a chat", ["➕ New Chat"] + chat_titles)

    if selected_title == "➕ New Chat":
        st.session_state.chat_title = None
        st.session_state.messages = []
    else:
        st.session_state.chat_title = selected_title
        st.session_state.messages = st.session_state.all_chats[selected_title]

# Set system prompt based on mode
mode = st.selectbox("Chat Mode", ["Default", "ML Tutor", "Python Helper"])
if mode == "ML Tutor":
    system_prompt = "You are an expert ML tutor who explains concepts with examples."
elif mode == "Python Helper":
    system_prompt = "You are a Python expert who helps debug and explain code."
else:
    system_prompt = "You are a helpful assistant."

# Ensure system message is always first
if not st.session_state.messages:
    st.session_state.messages.append({"role": "system", "content": system_prompt})

# Main title
st.title("💬 Chatbot with Groq")

# Chat input
user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL_NAME,
        "messages": st.session_state.messages
    }

    with st.spinner("Thinking..."):
        try:
            response = requests.post(API_URL, headers=headers, json=payload)
            response.raise_for_status()
            reply = response.json()["choices"][0]["message"]["content"]
            st.session_state.messages.append({"role": "assistant", "content": reply})

            # Generate title if it's a new chat
            if not st.session_state.chat_title:
                title_prompt = [
                    {"role": "system", "content": "Generate a short title for the following conversation."},
                    *st.session_state.messages[:6]
                ]
                title_payload = {
                    "model": MODEL_NAME,
                    "messages": title_prompt
                }
                title_resp = requests.post(API_URL, headers=headers, json=title_payload)
                title_resp.raise_for_status()
                chat_title = title_resp.json()["choices"][0]["message"]["content"].strip()

                # Store new chat
                st.session_state.chat_title = chat_title
                st.session_state.all_chats[chat_title] = st.session_state.messages

            else:
                # Update existing chat
                st.session_state.all_chats[st.session_state.chat_title] = st.session_state.messages

            # Save all chats
            save_all_chats(st.session_state.all_chats)

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            st.session_state.messages.append({"role": "assistant", "content": "Sorry, an error occurred."})

# Display chat in main area
for msg in st.session_state.messages[1:]:  # skip system message
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
