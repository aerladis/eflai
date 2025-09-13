@echo off
echo Setting up GitHub repository for EFL Cafe...
echo.

echo Step 1: Check if we have a remote repository
git remote -v
echo.

echo Step 2: If no remote exists, you need to:
echo 1. Go to https://github.com and create a new repository
echo 2. Name it "efl-cafe" (or your preferred name)
echo 3. Don't initialize with README
echo 4. Copy the repository URL
echo.

echo Step 3: Add the remote repository
echo Run this command with your actual GitHub username:
echo git remote add origin https://github.com/YOUR_USERNAME/efl-cafe.git
echo.

echo Step 4: Push to GitHub
echo git push -u origin main
echo.

echo Step 5: Verify GitHub Actions
echo Go to your repository on GitHub and check the Actions tab
echo.

pause
