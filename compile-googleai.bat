@echo off
echo Compiling EFL Cafe with Google AI support...
pyinstaller --clean --noconfirm --collect-all google.generativeai --collect-all google.protobuf --collect-all google.auth --collect-all google.api_core --collect-all google.oauth2 --onefile --windowed --name "EFL-Cafe" --icon="app.ico" --add-data "B2 templateee.docx;." --add-data "prompts.ini;." --add-data "app.ico;." --add-data "Tesseract-OCR;Tesseract-OCR" --hidden-import "google.generativeai" --hidden-import "docx" --hidden-import "PIL.Image" --hidden-import "PIL.ImageOps" --hidden-import "pytesseract" --hidden-import "fitz" --hidden-import "urllib.request" --hidden-import "urllib.error" --hidden-import "json" --hidden-import "ssl" --exclude-module "tkinter" --exclude-module "matplotlib" --exclude-module "numpy" --exclude-module "scipy" --exclude-module "pandas" --exclude-module "jupyter" --exclude-module "IPython" --optimize 2 --console 3.py
echo.
echo Compilation complete! Check dist\EFL-Cafe.exe
pause

