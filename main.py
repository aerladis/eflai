#!/usr/bin/env python3
"""
EFL Cafe - Main Entry Point

English as a Foreign Language Question Generator
A PyQt5 application for generating educational questions with AI integration.
"""

import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Set up DPI awareness before importing PyQt
from efl_cafe.utils.dpi import setup_dpi_environment
setup_dpi_environment()

# Import PyQt after DPI setup
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

# Import application components
from efl_cafe.gui.main_window import MainWindow
from efl_cafe.core.config import APP_NAME, APP_VERSION
from efl_cafe.utils.debug import debug_print


def main():
    """Main application entry point."""
    debug_print(f"Starting {APP_NAME} v{APP_VERSION}")
    
    # Create QApplication
    app = QApplication(sys.argv)
    app.setApplicationName(APP_NAME)
    app.setApplicationVersion(APP_VERSION)
    app.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    app.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    
    # Create and show main window
    window = MainWindow()
    window.show()
    
    # Start event loop
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
