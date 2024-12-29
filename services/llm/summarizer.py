"""Text summarization service."""
from typing import Optional
from ..clients.openai_client import get_openai_client
from ..config.openai_config import DEFAULT_MODEL, SUMMARY_MAX_TOKENS, SUMMARY_TEMPERATURE
from ..utils.error_handler import handle_openai_error

client = get_openai_client()

def summarize_content(text: str) -> str:
    """Generate a one-sentence summary of the article content."""
    try:
        response = client.chat.completions.create(
            model=DEFAULT_MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes text in one concise sentence."},
                {"role": "user", "content": f"Summarize this in one sentence: {text}"}
            ],
            max_tokens=SUMMARY_MAX_TOKENS,
            temperature=SUMMARY_TEMPERATURE
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return handle_openai_error(e, "summarization")