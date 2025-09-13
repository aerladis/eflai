# GitHub Setup Instructions

Follow these steps to set up automatic macOS compilation using GitHub Actions:

## 1. Initialize Git Repository

If you haven't already, initialize a git repository in your project:

```bash
git init
git add .
git commit -m "Initial commit with macOS build automation"
```

## 2. Create GitHub Repository

1. Go to [GitHub.com](https://github.com) and create a new repository
2. Name it `efl-cafe` (or your preferred name)
3. Don't initialize with README (since we already have one)

## 3. Connect Local Repository to GitHub

```bash
git remote add origin https://github.com/YOUR_USERNAME/efl-cafe.git
git branch -M main
git push -u origin main
```

## 4. Verify GitHub Actions

1. Go to your repository on GitHub
2. Click on the "Actions" tab
3. You should see the "Build macOS Application" workflow
4. The workflow will run automatically on every push

## 5. Download Build Artifacts

After a successful build:

1. Go to the "Actions" tab
2. Click on the latest successful workflow run
3. Scroll down to "Artifacts"
4. Download `efl-cafe-macos` to get your compiled application

## 6. Create Releases (Optional)

To create downloadable releases:

1. Create a git tag: `git tag v1.0.0`
2. Push the tag: `git push origin v1.0.0`
3. GitHub Actions will automatically create a release with the DMG file

## Troubleshooting

### Build Fails
- Check the Actions tab for error logs
- Ensure all required files are committed
- Verify the macOS spec file is correct

### Missing Dependencies
- The workflow installs all required dependencies automatically
- Check the "Install Python dependencies" step in the logs

### Tesseract Issues
- The workflow installs Tesseract via Homebrew
- Check the "Install system dependencies" step for any errors

## Files Added for GitHub Actions

- `.github/workflows/build-macos.yml` - Main workflow file
- `requirements.txt` - Python dependencies
- `README.md` - Project documentation
- `setup-github.md` - This setup guide

The workflow will automatically:
- Install system dependencies (Tesseract, etc.)
- Install Python dependencies
- Build the application using PyInstaller
- Create a DMG installer
- Upload build artifacts
- Create releases when you push tags
