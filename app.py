import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Get Groq API key
api_key = os.getenv("GROQ_API_KEY")

# Create Groq client
client = Groq(api_key=api_key)

# Streamlit page
st.title("🤖 JM's Bot")

# Chat input
user_message = st.chat_input("Type your message...")

if user_message:

    # Show user message
    with st.chat_message("user"):
        st.write(user_message)

    # Get response from Groq
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": user_message
            }
        ]
    )

    answer = response.choices[0].message.content

    # Show bot response
    with st.chat_message("assistant"):
        st.write(answer)