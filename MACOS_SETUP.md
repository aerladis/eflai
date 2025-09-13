# macOS Compilation Guide for EFL-Cafe

This guide explains how to compile the EFL-Cafe application for macOS on Windows.

## Prerequisites

### 1. Python Environment
- Python 3.8+ installed
- All required Python packages installed:
  ```bash
  pip install PyQt5 google-generativeai python-docx Pillow pytesseract PyMuPDF reportlab
  ```

### 2. PyInstaller
```bash
pip install pyinstaller
```

### 3. macOS Dependencies (for target system)
The compiled app will need these installed on the target macOS system:
- **Tesseract OCR**: `brew install tesseract`
- **Tesseract Language Data**: `brew install tesseract-lang`

## Compilation Process

### Step 1: Use the macOS-compatible script
The main script `3_mac.py` has been modified to:
- Use macOS-compatible Tesseract paths
- Remove Windows-specific dependencies
- Handle cross-platform OCR functionality

### Step 2: Run the build script
```bash
compile-mac.bat
```

This will:
- Use the `EFL-Cafe-Mac.spec` configuration
- Create a macOS-compatible executable
- Bundle all necessary dependencies

### Step 3: Test the build
The compiled app will be in the `dist` folder. Test it on a macOS system.

## Key Differences from Windows Version

### Tesseract Configuration
- **Windows**: Uses bundled `.exe` and `.dll` files
- **macOS**: Expects system-installed Tesseract via Homebrew

### File Paths
- **Windows**: `C:\Program Files\Tesseract-OCR\tesseract.exe`
- **macOS**: `/usr/local/bin/tesseract` or `/opt/homebrew/bin/tesseract`

### Dependencies
- **Removed**: `win32com.client`, `docx2pdf` (Windows-specific)
- **Kept**: All cross-platform libraries

## Deployment Considerations

### Code Signing
For distribution outside the App Store, you'll need to code sign the app:
1. Get a Developer ID from Apple
2. Update the `codesign_identity` in the spec file
3. Sign the executable: `codesign --force --deep --sign "Developer ID" EFL-Cafe`

### Creating a DMG
For easy distribution, create a DMG installer:
1. Create a folder with the app and any required files
2. Use Disk Utility or a tool like `create-dmg`
3. Include installation instructions for Tesseract

### App Store Distribution
For App Store distribution:
1. Create an entitlements file
2. Use proper code signing
3. Follow Apple's sandboxing requirements

## Troubleshooting

### Tesseract Not Found
- Ensure Tesseract is installed: `brew install tesseract`
- Check if it's in PATH: `which tesseract`
- Install language data: `brew install tesseract-lang`

### Missing Dependencies
- Ensure all Python packages are installed
- Check PyInstaller logs for missing modules
- Update the `hiddenimports` list in the spec file if needed

### Performance Issues
- The app may run slower in a virtual machine
- Consider using a real macOS system for testing
- Optimize the spec file by excluding unused modules

## Files Modified for macOS

1. **`3_mac.py`**: Main application with macOS-compatible paths
2. **`EFL-Cafe-Mac.spec`**: PyInstaller configuration for macOS
3. **`compile-mac.bat`**: Build script for Windows
4. **`MACOS_SETUP.md`**: This setup guide

## Next Steps

1. Run the compilation
2. Test on a macOS system
3. Create a DMG installer if needed
4. Set up code signing for distribution
