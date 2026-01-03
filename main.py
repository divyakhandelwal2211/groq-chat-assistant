# main.py

import streamlit as st
from datetime import datetime
from dotenv import load_dotenv
import os

from chat import get_groq_response
from session_utils import (
    load_chat_titles,
    load_chat_session,
    save_chat_session,
    generate_new_title,
)

# Load API key from environment
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("❌ GROQ_API_KEY not found in .env file.")
    st.stop()

# Streamlit Page Setup
st.set_page_config(page_title="Groq Chatbot", page_icon="🤖")
# st.title("💬 Chatbot using LLaMA3 on Groq")
st.title("💬 Chatbot using Groq")

# Load chat titles in sidebar
with st.sidebar:
    st.header("💬 Chat Sessions")
    session_titles = load_chat_titles()
    selected_title = st.selectbox("Choose a session", ["New Chat"] + session_titles)

# Mode dropdown
mode = st.selectbox("Choose Chat Mode", ["Default", "ML Tutor", "Python Helper"])

# Prompt based on mode
if mode == "ML Tutor":
    system_prompt = "You are an expert Machine Learning tutor who explains concepts in detail with examples."
elif mode == "Python Helper":
    system_prompt = "You are a Python programming expert who helps with code and explains step by step."
else:
    system_prompt = "You are a helpful assistant."

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": system_prompt}]
    st.session_state.chat_title = None

# If a session is selected (not new), load its content
if selected_title != "New Chat" and st.session_state.get("chat_title") != selected_title:
    st.session_state.messages = load_chat_session(selected_title)
    st.session_state.chat_title = selected_title

# Chat input from user
user_input = st.chat_input("Type your message here...")

if user_input:
    # First time in new chat
    if selected_title == "New Chat" and not st.session_state.get("chat_title"):
        generated_title = generate_new_title(user_input)
        st.session_state.chat_title = generated_title
        st.session_state.messages = [{"role": "system", "content": system_prompt}]
    else:
        generated_title = st.session_state.chat_title

    # Append user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get Groq response
    with st.spinner("Thinking..."):
        reply = get_groq_response(GROQ_API_KEY, st.session_state.messages)
        st.session_state.messages.append({"role": "assistant", "content": reply})

    # Save chat
    save_chat_session(st.session_state.chat_title, st.session_state.messages)

# Render chat messages (skip system prompt)
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
