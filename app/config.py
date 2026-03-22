import os 
from dotenv import load_dotenv

# Load environment variables from .env file 

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")

# if __name__  == "__main__":
#     print("API",  GROQ_API_KEY)
#     print("Model",  MODEL_NAME)



