#!/usr/bin/env python3
"""
Simple icon test to verify the app.ico file is valid
"""

import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

def test_icon_file():
    app = QApplication(sys.argv)
    
    # Test loading the icon file
    icon_path = "app.ico"
    print(f"Testing icon file: {icon_path}")
    print(f"File exists: {os.path.exists(icon_path)}")
    
    if os.path.exists(icon_path):
        icon = QIcon(icon_path)
        print(f"Icon loaded: {not icon.isNull()}")
        print(f"Icon sizes available: {icon.availableSizes()}")
        print(f"Icon cache key: {icon.cacheKey()}")
        
        # Test if icon can be painted
        from PyQt5.QtGui import QPainter
        from PyQt5.QtCore import QSize
        pixmap = icon.pixmap(QSize(32, 32))
        print(f"Pixmap created: {not pixmap.isNull()}")
        print(f"Pixmap size: {pixmap.size()}")
    else:
        print("Icon file not found!")
        return False
    
    # Create a simple window to test
    window = QMainWindow()
    window.setWindowTitle("Icon Test")
    window.setWindowIcon(icon)
    window.setGeometry(100, 100, 300, 200)
    
    label = QLabel("Icon Test\nCheck taskbar for icon", window)
    label.setAlignment(Qt.AlignCenter)
    window.setCentralWidget(label)
    
    window.show()
    
    print("Window created. Check if icon appears in taskbar.")
    print("Press Ctrl+C to exit.")
    
    try:
        sys.exit(app.exec_())
    except KeyboardInterrupt:
        print("\nTest completed.")

if __name__ == "__main__":
    test_icon_file()

