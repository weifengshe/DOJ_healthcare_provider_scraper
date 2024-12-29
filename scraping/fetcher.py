import requests
from typing import Optional
# website url = "https://www.justice.gov/news/press-releases"
def fetch_page(url: str) -> Optional[str]:
    """Fetch HTML content from the given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error fetching page: {str(e)}")
        return None