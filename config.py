"""
Configuration management for Taskify Agent.

This module handles environment variables, API keys, and application settings
with proper validation and security measures.
"""

import os
import logging
from typing import Optional
from pathlib import Path


class Config:
    """Application configuration with environment variable support."""
    
    # API Configuration
    GOOGLE_API_KEY: Optional[str] = os.getenv("GOOGLE_API_KEY")
    AGENT_MODEL: str = os.getenv("AGENT_MODEL", "gemini-2.0-flash-exp")
    
    # File Processing Limits
    MAX_PDF_SIZE_MB: int = int(os.getenv("MAX_PDF_SIZE_MB", "10"))
    MAX_PDF_PAGES: int = int(os.getenv("MAX_PDF_PAGES", "100"))
    
    # Logging Configuration
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    LOG_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    # Security Settings
    ALLOWED_FILE_EXTENSIONS: tuple = (".pdf",)
    ENABLE_DEBUG: bool = os.getenv("ENABLE_DEBUG", "false").lower() == "true"
    
    @classmethod
    def validate(cls) -> bool:
        """
        Validate configuration settings.
        
        Returns:
            bool: True if configuration is valid
            
        Raises:
            ValueError: If critical configuration is missing or invalid
        """
        if not cls.GOOGLE_API_KEY:
            raise ValueError(
                "GOOGLE_API_KEY environment variable is required. "
                "Please set it in your .env file or environment."
            )
        
        if len(cls.GOOGLE_API_KEY) < 20:
            raise ValueError("GOOGLE_API_KEY appears to be invalid (too short)")
        
        if cls.MAX_PDF_SIZE_MB <= 0 or cls.MAX_PDF_SIZE_MB > 100:
            raise ValueError("MAX_PDF_SIZE_MB must be between 1 and 100")
        
        return True
    
    @classmethod
    def setup_logging(cls) -> None:
        """Configure application logging."""
        logging.basicConfig(
            level=getattr(logging, cls.LOG_LEVEL.upper(), logging.INFO),
            format=cls.LOG_FORMAT,
            handlers=[
                logging.StreamHandler(),
            ]
        )
        
        # Mask API key in logs
        if cls.GOOGLE_API_KEY:
            logging.getLogger().addFilter(
                lambda record: cls._mask_sensitive_data(record)
            )
    
    @staticmethod
    def _mask_sensitive_data(record: logging.LogRecord) -> bool:
        """Mask sensitive data in log records."""
        if hasattr(record, 'msg'):
            msg = str(record.msg)
            # Mask API keys (simple pattern matching)
            if 'api_key' in msg.lower() or 'google_api_key' in msg.lower():
                record.msg = msg.replace(Config.GOOGLE_API_KEY or "", "***MASKED***")
        return True
    
    @classmethod
    def get_project_root(cls) -> Path:
        """Get the project root directory."""
        return Path(__file__).parent.absolute()


# Initialize logging on module import
Config.setup_logging()
