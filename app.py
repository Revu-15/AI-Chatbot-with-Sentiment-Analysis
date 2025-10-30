import streamlit as st
from transformers import pipeline

# ✅ Initialize chatbot safely for Python 3.13 + torch 2.6+
chatbot = pipeline(
    "text-generation",
    model="gpt2",
    device_map=None,       # disables meta tensor issue
    torch_dtype="float32"  # fixes dtype compatibility
)

# Streamlit UI
st.title("🤖 AI Conversational Chatbot (Revanth Reddy)")

# Text input
user_input = st.text_input("You:", "")

if user_input:
    with st.spinner("Thinking..."):
        response = chatbot(user_input, max_length=100, num_return_sequences=1)
        st.write("**Bot:**", response[0]['generated_text'])
