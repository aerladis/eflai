@echo off
echo ========================================
echo EFL Cafe - Push to GitHub
echo ========================================
echo.

echo Step 1: Adding all files...
git add .
if %errorlevel% neq 0 (
    echo Error adding files!
    pause
    exit /b 1
)

echo Step 2: Committing changes...
git commit -m "Add project structure test and GitHub setup scripts"
if %errorlevel% neq 0 (
    echo Error committing!
    pause
    exit /b 1
)

echo Step 3: Checking for remote repository...
git remote -v >nul 2>&1
if %errorlevel% neq 0 (
    echo No remote repository found!
    echo.
    echo Please create a GitHub repository first:
    echo 1. Go to https://github.com
    echo 2. Click "New repository"
    echo 3. Name it "efl-cafe"
    echo 4. Don't initialize with README
    echo 5. Copy the repository URL
    echo.
    echo Then run:
    echo git remote add origin YOUR_REPOSITORY_URL
    echo git push -u origin main
    pause
    exit /b 1
)

echo Step 4: Pushing to GitHub...
git push -u origin main
if %errorlevel% neq 0 (
    echo Error pushing to GitHub!
    echo Make sure you have the correct remote URL and permissions.
    pause
    exit /b 1
)

echo.
echo ========================================
echo SUCCESS! Your code has been pushed to GitHub.
echo ========================================
echo.
echo Next steps:
echo 1. Go to your GitHub repository
echo 2. Check the Actions tab for automatic builds
echo 3. Download the macOS build artifacts when ready
echo.
pause
