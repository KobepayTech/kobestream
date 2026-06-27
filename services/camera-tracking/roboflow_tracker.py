import json
import os
import sys
import time
from pathlib import Path

import cv2
from inference_sdk import InferenceHTTPClient

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "nodecg" / "bundles" / "kobestream" / "shared" / "ai_stats.json"
MODEL_CONFIG = Path(__file__).resolve().parent / "roboflow_models.json"


def parse_source(raw):
    try:
        return int(raw)
    except ValueError:
        return raw


def load_model_id(model_key):
    config = json.loads(MODEL_CONFIG.read_text(encoding="utf-8"))
    models = config["models"]
    key = model_key or config.get("default_model", "football_players")
    if key in models:
        return models[key]["model_id"]
    return key


def save_stats(frame_id, predictions, model_id):
    players = 0
    balls = 0
    referees = 0
    goalkeepers = 0

    for item in predictions:
        label = str(item.get("class", "")).lower()
        if label == "player":
            players += 1
        elif label == "ball":
            balls += 1
        elif label == "referee":
            referees += 1
        elif label == "goalkeeper":
            goalkeepers += 1

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps({
        "frame": frame_id,
        "model": model_id,
        "players_detected": players,
        "ball_detected": balls,
        "referees_detected": referees,
        "goalkeepers_detected": goalkeepers,
        "detections": predictions,
        "updated_at": time.strftime("%Y-%m-%d %H:%M:%S")
    }, indent=2), encoding="utf-8")


def main():
    api_key = os.environ.get("ROBOFLOW_API_KEY")
    if not api_key:
        raise RuntimeError("Set ROBOFLOW_API_KEY before running this tracker.")

    source = parse_source(sys.argv[1] if len(sys.argv) > 1 else "0")
    model_key = sys.argv[2] if len(sys.argv) > 2 else "football_players"
    sample_every = int(sys.argv[3]) if len(sys.argv) > 3 else 10
    model_id = load_model_id(model_key)

    client = InferenceHTTPClient(api_url="https://detect.roboflow.com", api_key=api_key)
    cap = cv2.VideoCapture(source)
    frame_id = 0

    print("Starting Roboflow tracker")
    print("source:", source)
    print("model:", model_id)

    while True:
        ok, frame = cap.read()
        if not ok:
            time.sleep(0.5)
            continue

        frame_id += 1
        if frame_id % sample_every != 0:
            continue

        result = client.infer(frame, model_id=model_id)
        predictions = result.get("predictions", [])
        save_stats(frame_id, predictions, model_id)
        print("frame", frame_id, "detections", len(predictions))


if __name__ == "__main__":
    main()
