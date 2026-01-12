"""
Date and time utilities for Taskify Agent.

This module provides timezone-aware datetime functions for study planning.
"""

import logging
from datetime import datetime, timezone
from typing import Optional

logger = logging.getLogger(__name__)


def get_current_datetime(format_str: Optional[str] = None) -> str:
    """
    Get current UTC datetime with optional custom formatting.
    
    Args:
        format_str: Optional strftime format string. 
                   Defaults to ISO 8601 format.
    
    Returns:
        Formatted datetime string
        
    Examples:
        >>> get_current_datetime()
        '2026-01-12 17:00:00'
        >>> get_current_datetime("%Y-%m-%d")
        '2026-01-12'
    """
    now = datetime.now(timezone.utc)
    
    if format_str is None:
        format_str = "%Y-%m-%d %H:%M:%S"
    
    try:
        formatted = now.strftime(format_str)
        logger.debug(f"Current datetime: {formatted}")
        return formatted
    except Exception as e:
        logger.error(f"Invalid datetime format: {format_str}, error: {e}")
        # Fallback to ISO format
        return now.strftime("%Y-%m-%d %H:%M:%S")


def parse_date(date_str: str) -> Optional[datetime]:
    """
    Parse various date string formats into datetime object.
    
    Args:
        date_str: Date string in various formats
        
    Returns:
        datetime object or None if parsing fails
        
    Examples:
        Supports formats like:
        - "2026-01-15"
        - "15/01/2026"
        - "Jan 15, 2026"
    """
    formats = [
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%m/%d/%Y",
        "%d-%m-%Y",
        "%b %d, %Y",
        "%B %d, %Y",
        "%Y-%m-%d %H:%M:%S",
    ]
    
    for fmt in formats:
        try:
            return datetime.strptime(date_str.strip(), fmt)
        except ValueError:
            continue
    
    logger.warning(f"Could not parse date: {date_str}")
    return None


def calculate_days_until(target_date: str) -> Optional[int]:
    """
    Calculate number of days from now until target date.
    
    Args:
        target_date: Target date string
        
    Returns:
        Number of days (can be negative if date is in past)
        None if date cannot be parsed
    """
    parsed = parse_date(target_date)
    if parsed is None:
        return None
    
    now = datetime.now(timezone.utc).replace(tzinfo=None)
    delta = (parsed - now).days
    
    logger.debug(f"Days until {target_date}: {delta}")
    return delta
