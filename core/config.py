from dotenv import load_dotenv
import os
load_dotenv()
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "groq")

GROQ_API_KEY=os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL")
