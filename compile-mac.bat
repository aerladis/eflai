@echo off
echo Building EFL-Cafe for macOS...
echo.
echo This script will compile the application for macOS using PyInstaller.
echo Note: You need to have the macOS dependencies installed.
echo.
echo Prerequisites:
echo 1. Python with PyInstaller installed
echo 2. macOS-compatible Tesseract (will be handled by the app)
echo 3. All Python dependencies installed
echo.
echo Starting compilation...
echo.

pyinstaller --clean --noconfirm EFL-Cafe-Mac.spec

echo.
echo Build complete!
echo.
echo The macOS executable should be in the 'dist' folder.
echo.
echo IMPORTANT NOTES FOR macOS DEPLOYMENT:
echo 1. The app expects Tesseract to be installed via Homebrew: brew install tesseract
echo 2. For language support: brew install tesseract-lang
echo 3. You may need to code sign the app for distribution
echo 4. Consider creating a .dmg installer for easy distribution
echo.
pause
