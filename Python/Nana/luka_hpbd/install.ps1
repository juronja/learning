# Set error action preference to stop script on error
$ErrorActionPreference = "Stop"

# --- Configuration ---
$pythonScriptUrl = "https://raw.githubusercontent.com/juronja/Nana/refs/heads/main/luka_hpbd/hpbd.py"
$pythonScriptName = "hpbd.py"
$downloadPath = Join-Path $env:UserProfile "Downloads"

# --- Function to display messages ---
function Show-Message {
    param (
        [string]$Message,
        [string]$Color = "Green"
    )
    Write-Host ""
    Write-Host -ForegroundColor $Color $Message
    Write-Host ""
    Start-Sleep -Seconds 1
}

Show-Message "Hello Luka! This script will install Python and download a Happy Birthday script to your downloads folder.`nAfter that you just have to run the script."
Show-Message "Press Enter to begin the installation and download process. Have fun! =^.^="
Read-Host | Out-Null # Read-Host without storing input, just waits for Enter

# --- 1. Check if winget is available ---
Show-Message "Checking for Windows Package Manager (winget)..."
try {
    winget --version | Out-Null
    Show-Message "winget found!"
}
catch {
    Show-Message "winget not found or not in PATH. Please ensure Windows is up to date or install winget from the Microsoft Store.", "Red"
    Show-Message "You might need to manually install Python from python.org if winget isn't available.", "Red"
    Exit 1
}

# --- 2. Install Python using winget ---
Show-Message "Attempting to install Python via winget..."
try {
    # Using --scope user to try and install without needing elevated admin if possible
    # Some packages might still require elevation depending on their installer
    winget install -e --id Python.Python.3.13
    Show-Message "Python installed successfully!"
}
catch {
    Show-Message "Failed to install Python via winget. This might require administrator privileges or a different installation method. Error: $($_.Exception.Message)", "Red"
    Show-Message "Please try running this script as an administrator, or manually install Python from python.org as described in the previous instructions.", "Red"
    Exit 1
}

# --- 3. Download the Python script ---
Show-Message "Downloading the birthday script from GitHub..."
try {
    $destinationFile = Join-Path $downloadPath $pythonScriptName
    Invoke-WebRequest -Uri $pythonScriptUrl -OutFile $destinationFile
    Show-Message "Script downloaded to: $destinationFile"
}
catch {
    Show-Message "Failed to download the script from GitHub. Check the URL and your internet connection. Error: $($_.Exception.Message)", "Red"
    Exit 1
}

# --- 4. Provide instructions to run the script ---
Show-Message "Setup Complete!" -Color "Yellow"
Show-Message "Here's how to run the birthday script:"

Show-Message "1. Open the Terminal (you can search for 'terminal' in the Windows search bar)."

Show-Message "2. Navigate to your Downloads folder by typing:"
Write-Host "   cd $downloadPath" -ForegroundColor "Cyan"
Write-Host "   Then press Enter."

Show-Message "3. Run the script by typing:"
Write-Host "   python $pythonScriptName" -ForegroundColor "Cyan"
Write-Host "   Then press Enter."

Start-Sleep -Seconds 5