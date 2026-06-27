#!/bin/bash
set -e

SOURCE="${1:-0}"
MODEL="${2:-yolov8n.pt}"
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SERVICE_DIR="$ROOT_DIR/services/camera-tracking"

cd "$SERVICE_DIR"

if [ ! -d .venv ]; then
  python3 -m venv .venv
fi

source .venv/bin/activate
pip install -r requirements.txt
python tracker.py "$SOURCE" "$MODEL"
