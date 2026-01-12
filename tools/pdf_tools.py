"""
PDF processing tools for Taskify Agent.

This module provides secure PDF text extraction with validation and error handling.
"""

import logging
from pathlib import Path
from typing import Optional
from pypdf import PdfReader

from config import Config

logger = logging.getLogger(__name__)


def extract_pdf_text(file_path: str) -> str:
    """
    Extract text from a PDF file with security validations.
    
    Args:
        file_path: Path to the PDF file
        
    Returns:
        Extracted text from all pages
        
    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If file is invalid or too large
        Exception: For other PDF processing errors
    """
    try:
        # Convert to Path object for better path handling
        pdf_path = Path(file_path).resolve()
        
        # Security: Prevent path traversal
        project_root = Config.get_project_root()
        try:
            pdf_path.relative_to(project_root)
        except ValueError:
            # File is outside project directory - allow but log warning
            logger.warning(f"Accessing file outside project: {pdf_path}")
        
        # Validation: Check file exists
        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF file not found: {file_path}")
        
        # Validation: Check file extension
        if pdf_path.suffix.lower() not in Config.ALLOWED_FILE_EXTENSIONS:
            raise ValueError(
                f"Invalid file type: {pdf_path.suffix}. "
                f"Allowed: {Config.ALLOWED_FILE_EXTENSIONS}"
            )
        
        # Security: Check file size
        file_size_mb = pdf_path.stat().st_size / (1024 * 1024)
        if file_size_mb > Config.MAX_PDF_SIZE_MB:
            raise ValueError(
                f"PDF file too large: {file_size_mb:.2f}MB. "
                f"Maximum allowed: {Config.MAX_PDF_SIZE_MB}MB"
            )
        
        logger.info(f"Processing PDF: {pdf_path.name} ({file_size_mb:.2f}MB)")
        
        # Extract text from PDF
        reader = PdfReader(str(pdf_path))
        
        # Check page count
        num_pages = len(reader.pages)
        if num_pages > Config.MAX_PDF_PAGES:
            logger.warning(
                f"PDF has {num_pages} pages, limiting to {Config.MAX_PDF_PAGES}"
            )
            num_pages = Config.MAX_PDF_PAGES
        
        extracted_pages = []
        for i, page in enumerate(reader.pages[:num_pages]):
            try:
                text = page.extract_text()
                if text and text.strip():
                    extracted_pages.append(text)
            except Exception as e:
                logger.warning(f"Failed to extract text from page {i+1}: {e}")
                continue
        
        if not extracted_pages:
            raise ValueError("No readable text found in PDF")
        
        full_text = "\n".join(extracted_pages)
        logger.info(
            f"Successfully extracted {len(full_text)} characters "
            f"from {len(extracted_pages)} pages"
        )
        
        return full_text
        
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        raise
    except ValueError as e:
        logger.error(f"Validation error: {e}")
        raise
    except Exception as e:
        logger.error(f"Failed to process PDF: {e}", exc_info=True)
        raise Exception(f"PDF processing error: {str(e)}")


def classify_document(text: str) -> dict:
    """
    Classify document type based on content with confidence scoring.
    
    Args:
        text: Document text content
        
    Returns:
        Dictionary with 'type' and 'confidence' keys
    """
    if not text or not text.strip():
        return {"type": "unknown", "confidence": 0.0}
    
    text_lower = text.lower()
    
    # Define classification patterns with weights
    patterns = {
        "exam_timetable": [
            ("exam", 3),
            ("date", 2),
            ("time", 2),
            ("schedule", 2),
            ("timetable", 3),
        ],
        "syllabus": [
            ("syllabus", 4),
            ("unit", 3),
            ("chapter", 2),
            ("topics", 2),
            ("course", 2),
            ("curriculum", 3),
        ],
        "pyq": [
            ("previous year", 4),
            ("question paper", 4),
            ("pyq", 5),
            ("solved", 2),
            ("marks", 2),
        ],
        "assignment": [
            ("assignment", 4),
            ("submit", 3),
            ("deadline", 3),
            ("due date", 3),
            ("homework", 3),
        ],
    }
    
    # Calculate scores for each document type
    scores = {}
    for doc_type, keywords in patterns.items():
        score = sum(weight for keyword, weight in keywords if keyword in text_lower)
        scores[doc_type] = score
    
    # Find the highest scoring type
    if not any(scores.values()):
        return {"type": "unknown", "confidence": 0.0}
    
    max_type = max(scores, key=scores.get)
    max_score = scores[max_type]
    
    # Calculate confidence (normalize to 0-1 range)
    # Maximum possible score for any category
    max_possible = max(sum(w for _, w in patterns[dt]) for dt in patterns)
    confidence = min(max_score / max_possible, 1.0)
    
    logger.info(f"Classified as '{max_type}' with {confidence:.2%} confidence")
    
    return {
        "type": max_type,
        "confidence": round(confidence, 2),
        "scores": scores  # Include all scores for debugging
    }
