@echo off
echo Building EFL-Cafe with NO console flashes...
echo.
echo This will create a clean GUI application without any console windows.
echo.
pyinstaller --clean --noconfirm EFL-Cafe-Fixed.spec
echo.
echo Build complete! 
echo.
echo The executable will run without any console window flashes.
echo To enable debug mode, create a DEBUG.txt file next to the .exe
echo.
pause

