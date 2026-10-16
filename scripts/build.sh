#!/usr/bin/env bash
# Builds, tests and packages device-provisioning as a Docker image, then runs it on port 8091.
set -euo pipefail
cd "$(dirname "$0")/.."

echo "==> Build"
pip install -r requirements.txt
echo "==> Unit tests"
python -m pytest -q
echo "==> Docker image"
docker build -t device-provisioning:latest .
echo "==> Run (Ctrl+C to stop)"
docker run --rm -p 8091:8091 device-provisioning:latest
