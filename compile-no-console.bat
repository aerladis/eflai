@echo off
echo Building EFL-Cafe without console window...
pyinstaller --clean --noconfirm EFL-Cafe-Fixed.spec
echo Build complete! Check the dist folder for EFL-Cafe.exe
pause

