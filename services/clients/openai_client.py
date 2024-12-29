"""OpenAI API client singleton."""
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def get_openai_client() -> OpenAI:
    """Get OpenAI client instance."""
    return OpenAI(api_key=os.getenv('OPENAI_API_KEY'))