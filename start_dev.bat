@echo off
title ORIGIN Development Mode (Vite + FastAPI)
echo ==========================================================
echo        ORIGIN - Development Environment
echo ==========================================================
echo.
set "PATH=%~dp0tools\node;C:\Users\np393\AppData\Local\Python\pythoncore-3.14-64\Scripts;%PATH%"

echo Starting FastAPI Backend in background...
start "ORIGIN Backend" cmd /k "py "%~dp0backend\main.py""

timeout /t 2 >nul

echo Starting Vite Frontend with Hot-Reload...
start http://localhost:5173
cd "%~dp0frontend"
npm run dev

