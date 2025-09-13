"""
Debug utilities and configuration.
"""
import os
import sys


# Debug mode detection
DEBUG_MODE = False
if getattr(sys, 'frozen', False):
    # Running as compiled executable
    exe_dir = os.path.dirname(sys.executable)
    debug_file = os.path.join(exe_dir, "DEBUG.txt")
    DEBUG_MODE = os.path.exists(debug_file)
else:
    # Running as Python script
    DEBUG_MODE = True

# Redirect stdout and stderr to prevent console flashes in compiled exe
if getattr(sys, 'frozen', False) and not DEBUG_MODE:
    # Redirect stdout and stderr to null to prevent console window
    import os
    devnull = open(os.devnull, 'w')
    sys.stdout = devnull
    sys.stderr = devnull


def debug_print(message):
    """Print debug messages only in debug mode to avoid console flashes."""
    if DEBUG_MODE:
        print(message)


def debug_print(*a):
    """Print debug messages with multiple arguments."""
    if DEBUG_MODE:
        print(*a)


def debug_mode_info():
    """Get debug mode information."""
    return {
        'debug_mode': DEBUG_MODE,
        'frozen': getattr(sys, 'frozen', False),
        'executable': sys.executable if getattr(sys, 'frozen', False) else None
    }


def setup_debug_folder():
    """Set up debug folder for logging."""
    if not DEBUG_MODE:
        return
    
    debug_folder = os.path.join(os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else os.getcwd(), "DEBUG")
    if not os.path.exists(debug_folder):
        os.makedirs(debug_folder)
    return debug_folder
