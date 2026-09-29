# ORIGIN - SIH26091 PowerShell Launcher
Write-Host "==========================================================" -ForegroundColor Green
Write-Host "       ORIGIN - Rural Micro-Enterprise Assistant" -ForegroundColor Cyan
Write-Host "       SIH Problem Statement: SIH26091" -ForegroundColor Yellow
Write-Host "==========================================================" -ForegroundColor Green
Write-Host ""

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$env:PATH = "$ScriptDir\tools\node;C:\Users\np393\AppData\Local\Python\pythoncore-3.14-64\Scripts;$env:PATH"

Write-Host "[1/2] Starting ORIGIN Unified Server (FastAPI + React UI)..." -ForegroundColor Green
Write-Host "Web Application: http://127.0.0.1:8000" -ForegroundColor White
Write-Host "Interactive Docs: http://127.0.0.1:8000/docs" -ForegroundColor White
Write-Host ""
Write-Host "Opening browser..." -ForegroundColor Gray

Start-Process "http://127.0.0.1:8000"

py "$ScriptDir\backend\main.py"

