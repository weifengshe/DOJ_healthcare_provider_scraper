"""Healthcare provider analysis service."""
from typing import Dict, List, Union
import json
from ..clients.openai_client import get_openai_client
from ..config.openai_config import DEFAULT_MODEL, DEFAULT_MAX_TOKENS, DEFAULT_TEMPERATURE
from ..utils.error_handler import handle_openai_error
from ..utils.response_validator import validate_provider_response
from ..prompts import HEALTHCARE_PROVIDER_SYSTEM_PROMPT

client = get_openai_client()

def analyze_healthcare_providers(text: str) -> Dict[str, Union[str, List[Dict[str, str]]]]:
    """Extract healthcare provider information from the article."""
    try:
        response = client.chat.completions.create(
            model=DEFAULT_MODEL,
            messages=[
                {"role": "system", "content": HEALTHCARE_PROVIDER_SYSTEM_PROMPT},
                {"role": "user", "content": text}
            ],
            max_tokens=DEFAULT_MAX_TOKENS,
            temperature=DEFAULT_TEMPERATURE
        )
        
        return validate_provider_response(response.choices[0].message.content)
    except Exception as e:
        return handle_openai_error(e, "provider analysis")