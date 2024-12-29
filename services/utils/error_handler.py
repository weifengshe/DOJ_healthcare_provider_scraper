"""Error handling utilities for OpenAI API calls."""
from typing import Dict, List, Union
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def handle_openai_error(error: Exception, operation: str) -> Union[str, Dict[str, Union[str, List]]]:
    """Handle OpenAI API errors with appropriate responses."""
    error_msg = str(error)
    logger.error(f"Error in {operation}: {error_msg}")
    
    if operation == "summarization":
        return "Summary not available"
    
    return {
        "message": f"Error processing {operation}",
        "providers": []
    }