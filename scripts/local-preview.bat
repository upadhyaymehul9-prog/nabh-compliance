@echo off
setlocal
title AccredReady local preview

echo.
echo  AccredReady - local preview (healthcare ecosystem branch)
echo  ==========================================================
echo.

where node >nul 2>&1
if errorlevel 1 (
  echo ERROR: Node.js is not installed.
  echo Download from https://nodejs.org/ ^(LTS^), then run this script again.
  pause
  exit /b 1
)

echo Node: 
node -v
echo.

cd /d "%~dp0.."
echo Project folder: %CD%
echo.

git fetch origin 2>nul
git checkout cursor/healthcare-ecosystem-landing-cb2d 2>nul
if errorlevel 1 (
  echo WARNING: Could not checkout branch. Continuing in current branch...
)
git pull origin cursor/healthcare-ecosystem-landing-cb2d 2>nul

echo Installing dependencies...
call npm install
if errorlevel 1 (
  echo ERROR: npm install failed.
  pause
  exit /b 1
)

echo.
echo Starting dev server...
echo When it says "Compiled successfully", open:
echo   http://localhost:3000/healthcare-ecosystem
echo.
echo Press Ctrl+C to stop the server.
echo.

call npm start
