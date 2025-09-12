from google import genai
from django.conf import settings

def generate_text(prompt: str) -> str:
    # model = genai.GenerativeModel("gemini-1.5-flash")
    # response = model.generate_content(prompt)
    client = genai.Client(api_key=settings.GEMINI_APY_KEY)
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )
    return response.text