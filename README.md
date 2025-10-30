# 🤖 AI Conversational Chatbot with Sentiment Analysis

**🔗 Live Demo:** [https://ai-chatbot-with-sentiment-analysis-revanthreddy15.streamlit.app/](https://ai-chatbot-with-sentiment-analysis-revanthreddy15.streamlit.app/)

---

## 📘 Overview
This project is an **AI-powered conversational chatbot** built using **Python, NLP, and Machine Learning**.  
It allows users to chat interactively while performing **real-time sentiment analysis** (Positive / Negative / Neutral) for each user message.  

The chatbot uses:
- **GPT-2** for generating intelligent, human-like responses  
- **DistilBERT** for sentiment analysis  
- **Streamlit** for the interactive web interface  

---

## ✨ Features
- 💬 Interactive chatbot powered by GPT-2  
- 🔍 Real-time sentiment analysis using DistilBERT  
- 🌐 Simple Streamlit UI for web deployment  
- ⚡ Lightweight and fast — works on CPU  
- 📦 Easy to deploy on Streamlit Cloud  

---

## 🧠 Tech Stack
| Component | Technology |
|------------|-------------|
| **Frontend** | Streamlit |
| **Backend / Logic** | Python |
| **NLP Models** | GPT-2, DistilBERT |
| **Libraries** | Transformers, Torch, Streamlit |
| **Deployment** | Streamlit Cloud |

---

## ⚙️ Installation & Setup

To run this project locally, follow these steps:


# 1️⃣ Clone your GitHub repository
git clone https://github.com/<your-username>/AI-Chatbot-with-Sentiment.git

# 2️⃣ Move into the project folder
cd AI-Chatbot-with-Sentiment

# 3️⃣ Create a virtual environment
python -m venv venv

# 4️⃣ Activate it
venv\Scripts\activate   # (for Windows)
# or, if you're using Linux/Mac:
# source venv/bin/activate

# 5️⃣ Install all dependencies
pip install -r requirements.txt

# 6️⃣ Run the chatbot
streamlit run app.py

