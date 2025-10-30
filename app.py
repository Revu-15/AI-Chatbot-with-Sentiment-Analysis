import streamlit as st
from transformers import pipeline

# Title
st.title("🤖 AI ChatGPT-Like Chatbot")

# Load models
sentiment_analyzer = pipeline("sentiment-analysis")
chatbot = pipeline("text-generation", model="gpt2")

# User input
user_input = st.text_input("You:", "")

# Generate response
if st.button("Send") and user_input:
    sentiment = sentiment_analyzer(user_input)[0]['label']
    response = chatbot(f"{user_input}. Sentiment: {sentiment}. Response:",
                       max_length=80,
                       num_return_sequences=1,
                       do_sample=True,
                       temperature=0.7)[0]['generated_text']
    st.write("**AI:**", response)
