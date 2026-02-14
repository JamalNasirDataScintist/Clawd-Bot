import streamlit as st 
from anthropic import Anthropic 
from dotenv import load_dotenv
import os


load_dotenv()

API_KEY=os.getenv("ANTHROPIC_API_KEY")
client = Anthropic(api_key=API_KEY)

st.set_page_config(page_title="Anthropic Clawd SMIT", page_icon=":robot:")

st.title("SMIT ClawdBot AI")



if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Always define user_input
user_input = st.chat_input("Say something")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    with st.chat_message("user"):
        st.markdown(user_input)
        
        
    with st.chat_message("assistant"):
        with st.spinner("our clawd is thinking..."):
            response=client.messages.create(
                model="glm-4.5",
                max_tokens=1024,
                messages=[
                    {"role": "user", "content": user_input}
                ]
            )
            
            bot_reply=response.content[0].text
            st.markdown(bot_reply)

    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
            
           