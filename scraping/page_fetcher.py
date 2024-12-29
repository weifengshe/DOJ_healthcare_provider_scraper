"""Module for fetching pages from DOJ website."""
from typing import Optional, List
import asyncio
from aiohttp import ClientSession, ClientTimeout
import logging

logger = logging.getLogger(__name__)

async def fetch_pages(urls: List[str]) -> List[Optional[str]]:
    """Fetch multiple pages concurrently."""
    timeout = ClientTimeout(total=30)
    async with ClientSession(timeout=timeout) as session:
        tasks = [fetch_single_page(session, url) for url in urls]
        return await asyncio.gather(*tasks)

async def fetch_single_page(session: ClientSession, url: str) -> Optional[str]:
    """Fetch a single page."""
    try:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.text()
            logger.error(f"Failed to fetch {url}, status: {response.status}")
            return None
    except Exception as e:
        logger.error(f"Error fetching {url}: {str(e)}")
        return None