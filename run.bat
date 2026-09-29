@echo off
title ORIGIN - SIH26091 Unified Server
echo ==========================================================
echo        ORIGIN - Rural Micro-Enterprise Assistant
echo        SIH Problem Statement: SIH26091
echo ==========================================================
echo.
echo [1/2] Setting environment paths...
set "PATH=%~dp0tools\node;C:\Users\np393\AppData\Local\Python\pythoncore-3.14-64\Scripts;%PATH%"

echo [2/2] Launching ORIGIN Full-Stack Server on port 8000...
echo.
echo Application URL: http://127.0.0.1:8000
echo API Swagger Docs: http://127.0.0.1:8000/docs
echo.
echo Press Ctrl+C to terminate the server.
echo.

start http://127.0.0.1:8000
py "%~dp0backend\main.py"
pause

