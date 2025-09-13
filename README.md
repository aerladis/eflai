# EFL-Cafe

An English as a Foreign Language (EFL) application built with PyQt5 and Python.

## Features

- Document processing and analysis
- OCR capabilities using Tesseract
- Google AI integration
- Cross-platform support (Windows, macOS)

## Building for macOS

This repository includes GitHub Actions automation to build the application for macOS.

### Automatic Builds

The application is automatically built for macOS using GitHub Actions when:

- Code is pushed to the `main` or `master` branch
- A pull request is created
- The workflow is manually triggered

### Build Artifacts

After a successful build, you can download:

- `EFL-Cafe` - The compiled macOS executable
- `EFL-Cafe-macOS.dmg` - A DMG installer package
- `requirements.txt` - Python dependencies

### Local Development

To build locally on macOS:

1. Install dependencies:
   ```bash
   brew install tesseract tesseract-lang poppler
   pip install -r requirements.txt
   ```

2. Build the application:
   ```bash
   pyinstaller --clean EFL-Cafe-Mac.spec
   ```

### Requirements

- Python 3.9+
- macOS 10.14+
- Tesseract OCR (installed via Homebrew)
- All Python dependencies listed in `requirements.txt`

## File Structure

- `3_mac.py` - Main application (macOS-compatible version)
- `EFL-Cafe-Mac.spec` - PyInstaller configuration for macOS
- `.github/workflows/build-macos.yml` - GitHub Actions workflow
- `requirements.txt` - Python dependencies

## License

[Add your license information here]
