import json
import sys
import time
from pathlib import Path

import cv2
from ultralytics import YOLO

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "nodecg" / "bundles" / "kobestream" / "shared" / "ai_stats.json"


def parse_source(raw):
    try:
        return int(raw)
    except ValueError:
        return raw


def save_stats(frame_id, players, balls):
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps({
        "frame": frame_id,
        "players_detected": players,
        "ball_detected": balls,
        "updated_at": time.strftime("%Y-%m-%d %H:%M:%S")
    }, indent=2), encoding="utf-8")


def main():
    source = parse_source(sys.argv[1] if len(sys.argv) > 1 else "0")
    model_name = sys.argv[2] if len(sys.argv) > 2 else "yolov8n.pt"
    model = YOLO(model_name)
    cap = cv2.VideoCapture(source)
    frame_id = 0

    while True:
        ok, frame = cap.read()
        if not ok:
            time.sleep(0.5)
            continue

        frame_id += 1
        result = model(frame, verbose=False)[0]
        players = 0
        balls = 0

        for box in result.boxes:
            cls = int(box.cls[0])
            if cls == 0:
                players += 1
            elif cls == 32:
                balls += 1

        save_stats(frame_id, players, balls)
        if frame_id % 30 == 0:
            print("frame", frame_id, "players", players, "ball", balls)


if __name__ == "__main__":
    main()
