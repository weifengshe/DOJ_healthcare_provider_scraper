"""OpenAI API configuration."""
from typing import Final

# OpenAI API Configuration
DEFAULT_MODEL: Final[str] = "gpt-4o-mini"
DEFAULT_TEMPERATURE: Final[float] = 0.0
DEFAULT_MAX_TOKENS: Final[int] = 4000

# Common prompt configurations
SUMMARY_MAX_TOKENS: Final[int] = 100
SUMMARY_TEMPERATURE: Final[float] = 0.2