import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

chat = client.chats.create(model="gemini-3.6-flash")

print("AI Chatbot ready. Type 'quit' to exit.")
print("-" * 40)

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "quit":
        print("Goodbye!")
        break
    
    response = chat.send_message(user_input)
    
    print(f"AI: {response.text}")
    print("-" * 40)