"""
Main application window.
"""
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
from ..core.config import APP_NAME, APP_VERSION
from ..utils.debug import debug_print


class MainWindow(QWidget):
    """Main application window."""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        """Initialize the user interface."""
        self.setWindowTitle(f"{APP_NAME} v{APP_VERSION}")
        self.setGeometry(100, 100, 800, 600)
        
        # Create layout
        layout = QVBoxLayout()
        
        # Add title
        title = QLabel(f"Welcome to {APP_NAME}")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold; margin: 20px;")
        layout.addWidget(title)
        
        # Add version info
        version = QLabel(f"Version {APP_VERSION}")
        version.setAlignment(Qt.AlignCenter)
        version.setStyleSheet("font-size: 14px; color: #666; margin-bottom: 20px;")
        layout.addWidget(version)
        
        # Add placeholder button
        button = QPushButton("Start Application")
        button.setStyleSheet("""
            QPushButton {
                background-color: #007acc;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 12px 24px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #005a9e;
            }
        """)
        button.clicked.connect(self.on_start_clicked)
        layout.addWidget(button)
        
        self.setLayout(layout)
        
        debug_print("Main window initialized")
    
    def on_start_clicked(self):
        """Handle start button click."""
        debug_print("Start button clicked - placeholder functionality")
        # TODO: Implement actual application functionality
