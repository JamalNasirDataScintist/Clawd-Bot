# Clawd Bot

A minimal Streamlit chatbot powered by the Groq API (openai/gpt-oss-20b). Type a message and get a reply in a chat-style UI.

## Features

- Streamlit chat interface
- Fast inference through Groq
- API key loaded from .env, never hardcoded

## Setup

```bash
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and add your key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

## Run

```bash
streamlit run app.py
```

## Tech stack

Python, Streamlit, Groq
