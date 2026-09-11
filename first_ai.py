import os
from google import genai
from dotenv import load_dotenv
import json
import time

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def classify_email(email_text):
    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=f"""You are an email classifier.
Read this email and return ONLY a JSON object like this:
{{"category": "Support or Sales or Billing or Spam or Other",
  "urgency": "High or Medium or Low",
  "summary": "one sentence max 10 words"}}

Return ONLY the JSON. No explanation. No extra text.

Email: {email_text}"""
        )
        result = json.loads(response.text)
        return result
    except Exception as e:
        return {"error": str(e)}

emails = [
    "Hi I ordered last week and still have not received my package. I need it urgently for tomorrow.",
    "I want to know your pricing plans for the enterprise package.",
    "Congratulations you won a prize click this link now!!!",
    "My invoice shows wrong amount please fix it before end of month."
]

for i, email in enumerate(emails, 1):
    print(f"\nEmail {i}:")
    time.sleep(2)
    result = classify_email(email)
    if "error" in result:
        print("Error:", result["error"])
    else:
        print("Category:", result["category"])
        print("Urgency:", result["urgency"])
        print("Summary:", result["summary"])