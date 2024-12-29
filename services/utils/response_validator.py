"""Validation utilities for OpenAI API responses."""
from typing import Dict, List, Union
import json

def validate_provider_response(content: str) -> Dict[str, Union[str, List[Dict[str, str]]]]:
    """Validate and process provider analysis response."""
    try:
        providers = json.loads(content.strip())
        
        if not isinstance(providers, list):
            return {"message": "Invalid response format", "providers": []}
            
        valid_providers = []
        for provider in providers:
            if isinstance(provider, dict) and 'name' in provider and 'title' in provider:
                valid_provider = {
                    'name': str(provider['name']),
                    'title': str(provider['title'])
                }
                if 'facility' in provider:
                    valid_provider['facility'] = str(provider['facility'])
                valid_providers.append(valid_provider)
        
        return {
            "message": "Healthcare providers found" if valid_providers else "No providers found",
            "providers": valid_providers
        }
        
    except json.JSONDecodeError as e:
        return {"message": "Invalid JSON response", "providers": []}