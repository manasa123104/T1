# Builds, tests and packages device-provisioning as a Docker image, then runs it on port 8091 (Windows PowerShell).
$ErrorActionPreference = "Stop"
Set-Location (Join-Path $PSScriptRoot "..")

Write-Host "==> Build"
pip install -r requirements.txt
Write-Host "==> Unit tests"
python -m pytest -q
Write-Host "==> Docker image"
docker build -t device-provisioning:latest .
Write-Host "==> Run (Ctrl+C to stop)"
docker run --rm -p 8091:8091 device-provisioning:latest
