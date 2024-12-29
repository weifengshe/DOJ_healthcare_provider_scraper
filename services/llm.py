
from typing import Dict, List, Optional, Union
from .clients.openai_client import get_openai_client
from .config.openai_config import (
    DEFAULT_MODEL,
    DEFAULT_TEMPERATURE,
    DEFAULT_MAX_TOKENS,
    SUMMARY_MAX_TOKENS,
    SUMMARY_TEMPERATURE
)
from .prompts import HEALTHCARE_PROVIDER_SYSTEM_PROMPT
import json

client = get_openai_client()

def summarize_content(text: str) -> Optional[str]:
    """Generate a one-sentence summary of the article content."""
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes text in one concise sentence."},
                {"role": "user", "content": f"Summarize this in one sentence: {text}"}
            ],
            max_tokens=100,
            temperature=0.5
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error in LLM summarization: {str(e)}")
        return None

# def analyze_healthcare_providers(text: str) -> Dict[str, Union[str, List[Dict[str, str]]]]:
#     """Extract healthcare provider information from the article."""
#     try:
#         response = client.chat.completions.create(
#             model="gpt-4o-mini",
#             messages=[
#                 {"role": "system", "content": HEALTHCARE_PROVIDER_SYSTEM_PROMPT},
#                 {"role": "user", "content": text}
#             ],
#             max_tokens=1000,
#             temperature=0.3
#         )
#         try:
#             # Use json.loads instead of eval for safer parsing
#             content = response.choices[0].message.content.strip()
#             providers = json.loads(content)
            
#             # Ensure we have a list
#             if not isinstance(providers, list):
#                 return {"message": "Invalid response format", "providers": []}
                
#             # Validate each provider entry
#             valid_providers = []
#             for provider in providers:
#                 if isinstance(provider, dict) and 'name' in provider and 'title' in provider:
#                     valid_provider = {
#                         'name': str(provider['name']),
#                         'title': str(provider['title'])
#                     }
#                     # Only add facility if it exists
#                     if 'facility' in provider:
#                         valid_provider['facility'] = str(provider['facility'])
#                     valid_providers.append(valid_provider)
            
#             return {
#                 "message": "Healthcare providers found" if valid_providers else "No providers found",
#                 "providers": valid_providers
#             }
        
#         # try:
#         #     providers = eval(response.choices[0].message.content)
#         #     # Ensure we have a list of dictionaries
#         #     if not isinstance(providers, list):
#         #         return {"message": "No provider found", "providers": []}
                
#         #     # Filter out any invalid entries
#         #     valid_providers = [p for p in providers if isinstance(p, dict) and p.get('name') and p.get('title')]
            
#         #     if not valid_providers:
#         #         return {"message": "No provider found", "providers": []}
            
#         #     return {
#         #         "message": "Healthcare provider found",
#         #         "providers": valid_providers
#         #     }
            
#         except Exception as parse_error:
#             print(f"Error parsing provider response: {parse_error}")
#             return {"message": "No provider found", "providers": []}
            
#     except Exception as e:
#         print(f"Error in healthcare provider analysis: {str(e)}")
#         return {"message": "No provider found", "providers": []}

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
        
        try:
            content = response.choices[0].message.content.strip()
            providers = json.loads(content)
            
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
            
        except json.JSONDecodeError as json_error:
            # print(f"Error parsing JSON response: {json_error}")
            # print(f"Raw response: {response.choices[0].message.content}")
            return {"message": "Invalid JSON response", "providers": []}
            
    except Exception as e:
        print(f"Error in healthcare provider analysis: {str(e)}")
        return {"message": "Error processing providers", "providers": []}