# Roboflow models for Kobestream

Kobestream now supports Roboflow-hosted football models through `services/camera-tracking/roboflow_tracker.py`.

## Included model catalog

The model catalog is stored in:

```text
services/camera-tracking/roboflow_models.json
```

| Key | Roboflow model ID | Purpose |
|---|---|---|
| `football_players` | `football-players-detection-3zvbc/20` | Detect ball, goalkeeper, player and referee |
| `football_ball` | `football-ball-detection-rejhg/4` | Better ball-only detection |
| `football_field` | `football-field-detection-f07vi/17` | Pitch/keypoint calibration |

## Setup

Create a Roboflow account and get an API key, then export it in your terminal:

```bash
export ROBOFLOW_API_KEY=your_key_here
```

Never commit your API key to GitHub.

## Run with webcam

```bash
bash scripts/run-roboflow-tracking.sh 0 football_players 10
```

Arguments:

```text
1 = camera/video source
2 = model key or direct Roboflow model ID
3 = sample every N frames
```

## Run with video file

```bash
bash scripts/run-roboflow-tracking.sh match.mp4 football_players 5
```

## Run ball-only model

```bash
bash scripts/run-roboflow-tracking.sh match.mp4 football_ball 5
```

## Output

The tracker writes live JSON here:

```text
nodecg/bundles/kobestream/shared/ai_stats.json
```

The NodeCG camera overlay reads this file and displays player, ball, referee and goalkeeper counts.

## When to use YOLO local vs Roboflow

| Mode | Best for |
|---|---|
| Local YOLO tracker | Offline use, no API cost, faster if your laptop has GPU |
| Roboflow tracker | Using football-trained hosted models quickly without training locally |

## Next step

For production, train your own model using your league camera angle and uniforms. Use the Roboflow models first to collect test videos and compare accuracy.
