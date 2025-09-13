# PowerShell script to set up GitHub repository
Write-Host "Setting up GitHub repository for EFL Cafe..." -ForegroundColor Green
Write-Host ""

# Check current status
Write-Host "Current git status:" -ForegroundColor Yellow
git status
Write-Host ""

# Check if remote exists
Write-Host "Checking for remote repository..." -ForegroundColor Yellow
$remotes = git remote -v
if ($remotes) {
    Write-Host "Remote repository found:" -ForegroundColor Green
    Write-Host $remotes
} else {
    Write-Host "No remote repository configured." -ForegroundColor Red
    Write-Host ""
    Write-Host "To set up GitHub repository:" -ForegroundColor Yellow
    Write-Host "1. Go to https://github.com and create a new repository" -ForegroundColor White
    Write-Host "2. Name it 'efl-cafe' (or your preferred name)" -ForegroundColor White
    Write-Host "3. Don't initialize with README" -ForegroundColor White
    Write-Host "4. Copy the repository URL" -ForegroundColor White
    Write-Host ""
    Write-Host "Then run these commands:" -ForegroundColor Yellow
    Write-Host "git remote add origin https://github.com/YOUR_USERNAME/efl-cafe.git" -ForegroundColor Cyan
    Write-Host "git push -u origin main" -ForegroundColor Cyan
}

Write-Host ""
Write-Host "Press any key to continue..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
