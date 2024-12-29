"""Module for handling asynchronous operations."""
import asyncio
from typing import List, Dict, Any, Callable
from functools import partial

async def run_in_threadpool(func: Callable, *args, **kwargs) -> Any:
    """Run a blocking function in a thread pool."""
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, partial(func, *args, **kwargs))

async def process_concurrently(items: List[Any], processor: Callable) -> List[Any]:
    """Process multiple items concurrently using asyncio."""
    return await asyncio.gather(*[processor(item) for item in items])