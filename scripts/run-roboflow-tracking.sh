#!/bin/bash
set -e

SOURCE="${1:-0}"
MODEL_KEY="${2:-football_players}"
SAMPLE_EVERY="${3:-10}"
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SERVICE_DIR="$ROOT_DIR/services/camera-tracking"

if [ -z "$ROBOFLOW_API_KEY" ]; then
  echo "Missing ROBOFLOW_API_KEY. Export it first:"
  echo "export ROBOFLOW_API_KEY=your_key_here"
  exit 1
fi

cd "$SERVICE_DIR"

if [ ! -d .venv ]; then
  python3 -m venv .venv
fi

source .venv/bin/activate
pip install -r requirements.txt
python roboflow_tracker.py "$SOURCE" "$MODEL_KEY" "$SAMPLE_EVERY"
