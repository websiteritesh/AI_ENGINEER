# AI Engineer Portfolio

A collection of AI projects built with Python and Google Gemini API.

## Projects in this repository

### 1. Email Classifier (first_ai.py)
AI that reads any email and returns structured JSON with:
- Category (Support, Sales, Billing, Spam, Other)
- Urgency level (High, Medium, Low)
- One line summary

Tools: Python, Google Gemini API

### 2. Conversation Chatbot (chatbot.py)
AI chatbot that remembers the full conversation history.
User can have a multi-turn conversation — AI remembers 
everything said earlier in the session.

Tools: Python, Google Gemini API

## How to run
1. Add your Google API key to .env file
2. For email classifier: python first_ai.py
3. For chatbot: python chatbot.py

## Tools used
- Python 3.13
- Google Gemini API (gemini-3.6-flash)
- python-dotenv