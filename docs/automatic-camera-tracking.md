# Automatic player tracking: YOLO/Roboflow Sports + NodeCG + OBS

Use this mode to detect players and the ball from a webcam, IP camera or video file.

## Start NodeCG

```bash
bash scripts/run-nodecg.sh
```

## Start AI tracking

Webcam:

```bash
bash scripts/run-ai-tracking.sh 0
```

IP camera stream:

```bash
bash scripts/run-ai-tracking.sh "rtsp://camera-ip/stream1"
```

Video file:

```bash
bash scripts/run-ai-tracking.sh match.mp4
```

The tracker writes live data to:

```text
nodecg/bundles/kobestream/shared/ai_stats.json
```

The NodeCG AI overlay reads that file and shows player detections, ball detections, frame number and last update time.

## Important note

This first version detects people/players and sports balls. True player identity, jersey OCR, team separation, heatmaps and tactical stats need a trained football model plus camera calibration.
