# 🤖 Groq Streamlit Chatbot

An AI-powered chatbot built using **Groq LLM** and **Streamlit**, featuring multiple chat modes, chat history persistence, and secure API key management.  
The application is deployed on **Streamlit Cloud** and the source code is maintained on **GitHub**.

---

## 🚀 Live Demo
🔗 https://groq-chat-assistant.streamlit.app

---

## 📌 Features
- 💬 Interactive AI chatbot powered by **Groq LLM**
- 🧠 Multiple chat modes:
  - Default Assistant  
  - ML Tutor  
  - Python Helper
- 📚 Persistent chat history (saved locally)
- 🔐 Secure API key handling using environment variables
- ⚡ Fast and responsive UI using Streamlit
- ☁️ Deployed on Streamlit Cloud

---

## 🛠️ Tech Stack
- **Python**
- **Streamlit**
- **Groq API**
- **Requests**
- **python-dotenv**
- **Git & GitHub**

---

## 📂 Project Structure
Groq_Chat_App/
│
├── main.py # Streamlit app entry point
├── chat.py # Groq API interaction logic
├── session_utils.py # Session & chat history handling
├── requirements.txt # Project dependencies
├── README.md # Project documentation
├── .gitignore # Ignored files & folders
└── venv/ # Virtual environment (local only)

---

## ⚙️ How to Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/divyakhandelwal2211/groq-chat-assistant.git
cd groq-chat-assistant
2️⃣ Create & activate virtual environment
bash
Copy code
python -m venv venv
venv\Scripts\activate
3️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Set environment variable
Create a .env file in the project root:

env

GROQ_API_KEY=your_groq_api_key_here
5️⃣ Run the app

streamlit run main.py
🔐 Security Notes
API keys are never hardcoded

.env, venv, .vscode, and __pycache__ are excluded using .gitignore

Streamlit Secrets are used for deployment

🌐 Deployment
The application is deployed using Streamlit Cloud and connected directly to the GitHub repository.

💡 Future Enhancements
Gemini-based chatbot version

Database-backed chat history

Authentication system

UI/UX improvements

👩‍💻 Author
Divya Khandelwal
Final-year B.Tech student | Aspiring Data & AI Professional

⭐ Acknowledgements
Groq for providing fast LLM inference

Streamlit for seamless app deployment

## 🚀 Live Demo
🔗 https://groq-chat-assistant.streamlit.app