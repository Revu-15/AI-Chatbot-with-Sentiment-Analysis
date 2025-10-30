import torch
from transformers import pipeline
import streamlit as st

# ✅ Fix for PyTorch + Transformers compatibility
torch.set_default_dtype(torch.float32)
torch.set_default_device("cpu")

# Load Sentiment Model
@st.cache_resource
def load_sentiment_analyzer():
    return pipeline(
        "sentiment-analysis",
        model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
        device_map=None,
        torch_dtype=torch.float32,
    )

# Load GPT-2 Chatbot Model
@st.cache_resource
def load_chatbot():
    return pipeline(
        "text-generation",
        model="gpt2",
        device_map=None,
        torch_dtype=torch.float32,
        max_new_tokens=150,
        temperature=0.7,
    )

# Initialize models
sentiment_analyzer = load_sentiment_analyzer()
chatbot = load_chatbot()

# Streamlit UI
st.set_page_config(page_title="AI Chatbot by Revanth", page_icon="🤖", layout="centered")
st.title("🤖 AI Chatbot with Sentiment Analysis")
st.markdown("Built by **Polamreddy Revanth Reddy** using Python, ML, and HuggingFace Transformers.")

user_input = st.text_area("💬 Type your message here:", height=150)

if st.button("Generate Response"):
    if user_input.strip() == "":
        st.warning("Please type a message before generating a response.")
    else:
        with st.spinner("Analyzing..."):
            # Analyze sentiment
            sentiment = sentiment_analyzer(user_input)[0]
            # Generate chatbot reply
            response = chatbot(user_input, max_length=150, num_return_sequences=1)[0]["generated_text"]

        st.subheader("🗣️ Chatbot Response:")
        st.write(response)

        st.subheader("💡 Sentiment Analysis:")
        st.write(f"**Label:** {sentiment['label']}  |  **Confidence:** {sentiment['score']:.2f}")

st.markdown("---")
st.caption("Made with ❤️ using Python, Streamlit, and Transformers.")
