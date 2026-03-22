from groq import Groq
from app.config import GROQ_API_KEY, MODEL_NAME

class GroqLLM:
    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)
        self.model = MODEL_NAME

    def generate(self, prompt: str):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are an AI assistant that analyzes student performance data and gives insights."},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content