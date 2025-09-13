"""
Application configuration and constants.
"""
import os
import sys
from ..utils import debug


# App Info & Config
APP_NAME = "EFL Cafe Wizard"
APP_VERSION = "0.23 BETA"  # updated for beta release
UPDATE_IN_PROGRESS = False  # Global flag to prevent multiple update dialogs

# Dependencies
OCR_AVAILABLE = False
GOOGLE_AI_AVAILABLE = False

# Initialize dependencies
def _check_dependencies():
    """Check for available dependencies."""
    global OCR_AVAILABLE, GOOGLE_AI_AVAILABLE
    
    # OCR imports
    try:
        from PIL import Image, ImageOps
        import pytesseract
        import fitz  # PyMuPDF
        OCR_AVAILABLE = True
    except ImportError as e:
        OCR_AVAILABLE = False
        debug.debug_print(f"OCR dependencies not available: {e}")

    # Google AI imports
    try:
        import google.generativeai as genai
        GOOGLE_AI_AVAILABLE = True
        debug.debug_print(f"Google AI library loaded successfully")
    except ImportError as e:
        GOOGLE_AI_AVAILABLE = False
        debug.debug_print(f"Google AI library not available: {e}")


# Initialize dependencies on import
_check_dependencies()
