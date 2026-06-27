# Camera tracking service

This service reads a webcam, IP camera stream or video file. It uses YOLO to count players and sports balls, then writes live JSON for the Kobestream NodeCG overlay.

## Install

```bash
cd services/camera-tracking
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python tracker.py 0
```

The output file is:

```text
nodecg/bundles/kobestream/shared/ai_stats.json
```

## Next improvements

- Use a football-trained Roboflow or YOLO model.
- Add tracking IDs.
- Add team-color classification.
- Add jersey-number OCR.
- Add pitch calibration for speed, distance and heatmaps.
