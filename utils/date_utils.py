"""Utility functions for date operations."""
from datetime import datetime, timedelta

def get_monday_of_last_week() -> str:
    """Get Monday's date of last week in yyyy-mm-dd format."""
    today = datetime.now()
    last_monday = today - timedelta(days=today.weekday() + 7)
    return last_monday.strftime('%Y-%m-%d')

def get_sunday_of_last_week() -> str:
    """Get Sunday's date of last week in yyyy-mm-dd format."""
    today = datetime.now()
    last_sunday = today - timedelta(days=today.weekday() + 1)
    return last_sunday.strftime('%Y-%m-%d')