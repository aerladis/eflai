# PowerShell script to add GitHub remote and push
Write-Host "========================================" -ForegroundColor Green
Write-Host "EFL Cafe - Add GitHub Remote" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""

# Check current status
Write-Host "Current git status:" -ForegroundColor Yellow
git status
Write-Host ""

# Check for existing remotes
Write-Host "Checking for existing remotes..." -ForegroundColor Yellow
$remotes = git remote -v
if ($remotes) {
    Write-Host "Existing remotes found:" -ForegroundColor Green
    Write-Host $remotes
    Write-Host ""
    Write-Host "Do you want to add a new remote? (y/n)" -ForegroundColor Yellow
    $response = Read-Host
    if ($response -ne "y" -and $response -ne "Y") {
        Write-Host "Exiting..." -ForegroundColor Red
        exit
    }
}

Write-Host ""
Write-Host "Please provide your GitHub repository URL:" -ForegroundColor Yellow
Write-Host "Example: https://github.com/YOUR_USERNAME/efl-cafe.git" -ForegroundColor Cyan
Write-Host ""
$repoUrl = Read-Host "Repository URL"

if (-not $repoUrl) {
    Write-Host "No URL provided. Exiting..." -ForegroundColor Red
    exit
}

# Add remote
Write-Host ""
Write-Host "Adding remote repository..." -ForegroundColor Yellow
git remote add origin $repoUrl

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Remote added successfully!" -ForegroundColor Green
} else {
    Write-Host "❌ Error adding remote. It might already exist." -ForegroundColor Red
    Write-Host "Trying to set URL instead..." -ForegroundColor Yellow
    git remote set-url origin $repoUrl
}

# Push to GitHub
Write-Host ""
Write-Host "Pushing to GitHub..." -ForegroundColor Yellow
git push -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "🎉 SUCCESS! Your code has been pushed to GitHub!" -ForegroundColor Green
    Write-Host ""
    Write-Host "Next steps:" -ForegroundColor Yellow
    Write-Host "1. Go to your GitHub repository" -ForegroundColor White
    Write-Host "2. Check the Actions tab for automatic builds" -ForegroundColor White
    Write-Host "3. Download the macOS build artifacts when ready" -ForegroundColor White
} else {
    Write-Host ""
    Write-Host "❌ Error pushing to GitHub!" -ForegroundColor Red
    Write-Host "Please check:" -ForegroundColor Yellow
    Write-Host "- Your repository URL is correct" -ForegroundColor White
    Write-Host "- You have access to the repository" -ForegroundColor White
    Write-Host "- Your GitHub credentials are set up" -ForegroundColor White
}

Write-Host ""
Write-Host "Press any key to continue..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
