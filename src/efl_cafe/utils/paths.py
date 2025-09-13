"""
Path utilities and resource management.
"""
import os
import sys


def _resource_path(rel: str) -> str:
    """Get absolute path to resource, works for dev and for PyInstaller."""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, rel)


def _get_prompts_path():
    """Get the path to the prompts.ini file."""
    if getattr(sys, 'frozen', False):
        # Running as compiled executable
        exe_dir = os.path.dirname(sys.executable)
        prompts_path = os.path.join(exe_dir, "prompts.ini")
        if os.path.exists(prompts_path):
            return prompts_path
        # Fallback to resource path
        return _resource_path("prompts.ini")
    else:
        # Running as Python script
        return os.path.join(os.path.dirname(__file__), "..", "..", "..", "prompts.ini")
