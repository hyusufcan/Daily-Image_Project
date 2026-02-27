@echo off
REM The Daily Antiquarian - Quick Start Batch File
REM Windows PowerShell/Command Prompt için

title The Daily Antiquarian - Local Dev Server

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║          🏛️  The Daily Antiquarian - Dev Server              ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

REM Check if requirements are installed
python -m pip show requests >nul 2>&1
if errorlevel 1 (
    echo ⚠️  Installing dependencies...
    python -m pip install -r requirements.txt
) else (
    echo ✅ Dependencies already installed
)

echo.
echo 🚀 Starting development server...
echo.
echo 📍 Website:  http://localhost:8000/public/
echo 📝 Files:    %cd%
echo.
echo Press CTRL+C to stop the server.
echo.

python -m http.server 8000 --directory public

pause
