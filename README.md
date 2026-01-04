# 🤖 Groq Chat App (LLaMA 3 Powered)

An AI-powered chatbot built using **Streamlit** and **Groq’s LLaMA 3 model**, supporting multiple chat sessions, role-based chat modes, and persistent chat history.

---

## 🚀 Features

- 💬 Chatbot powered by **LLaMA 3 (70B)** on Groq
- 🧠 Multiple chat modes:
  - Default Assistant
  - ML Tutor
  - Python Helper
- 📁 Persistent chat sessions (saved as JSON)
- 🔄 Resume previous conversations from sidebar
- ⚡ Fast inference using Groq API
- 🔐 Secure API key handling using `.env`

---

## 🏗️ Project Structure

├── main.py # Streamlit UI and app logic
├── chat.py # Groq API interaction
├── session_utils.py # Chat save/load utilities
├── test.py # API testing script
├── hhh.py # Experimental API practice script
├── chat_sessions/ # Stored chat history (JSON files)
├── .env # Environment variables (not uploaded)
└── README.md

yaml
Copy code

---

## 🧠 How the App Works

1. User enters a message in the Streamlit UI  
2. `main.py` handles UI and session state  
3. Messages are sent to Groq via `chat.py`  
4. Groq’s LLaMA model generates a response  
5. Chat history is saved using `session_utils.py`  
6. User can resume chats from the sidebar  

---

## 🔑 API Setup (Groq)

1. Create an account at **https://console.groq.com**
2. Generate an API key
3. Create a `.env` file in the project root:

GROQ_API_KEY=your_api_key_here

yaml
Copy code

⚠️ Never commit `.env` to GitHub

---

## ▶️ How to Run the App

### 1️⃣ Install dependencies
```bash
pip install streamlit requests python-dotenv
2️⃣ Run the chatbot
bash
Copy code
streamlit run main.py
The app will open at:

arduino
Copy code
http://localhost:8501
🧪 Running Test Scripts
Run API test script
bash
Copy code
python test.py
Run experimental script
bash
Copy code
python hhh.py
These scripts are standalone and not part of the main app flow.

🧩 Chat Modes Explained
Default → General-purpose assistant

ML Tutor → Explains Machine Learning concepts with examples

Python Helper → Debugging and step-by-step Python explanations

📦 Technologies Used
Python

Streamlit

Groq API

LLaMA 3

Requests

JSON

python-dotenv

🎯 Learning Outcomes
API integration with Large Language Models (LLMs)

Secure credential management using environment variables

Streamlit session state handling

Modular project architecture

Persistent data storage using JSON

📌 Notes
test.py and hhh.py were used during development for testing and experimentation

Core application files:

main.py

chat.py

session_utils.py

👩‍💻 Author
Divya Khandelwal
Final Year B.Tech Student
AI & Data Analytics Enthusiast


## 🚀 Live Demo
🔗 https://groq-chat-assistant.streamlit.app