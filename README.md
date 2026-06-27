# Kobestream

Kobestream is an open-source live streaming and sports broadcast stack for camera feeds, scoreboards, AR-style overlays, player stats, and AI player/ball tracking.

## What it supports

1. **Manual player stats**: OBS Studio + Fly Scoreboard
2. **Professional TV graphics**: OBS Studio + NodeCG
3. **Automatic tracking**: Local YOLO or Roboflow football models + NodeCG + OBS

## Included open-source projects

| Folder | Project | Use |
|---|---|---|
| `vendor/obs-studio` | OBS Studio | Main live streaming, recording and scene mixing |
| `vendor/fly-scoreboard` | Fly Scoreboard | Scoreboard, timer, match stats and OBS overlays |
| `vendor/nodecg` | NodeCG | Professional broadcast graphics framework |
| `vendor/sport-streamer` | Sport Streamer | Sports scoreboard, player highlights and ads |
| `vendor/casparcg-server` | CasparCG Server | Professional graphics/video playout server |
| `vendor/spx-gc` | SPX-GC | Graphics controller for OBS, CasparCG and vMix |
| `vendor/roboflow-sports` | Roboflow Sports | Sports computer vision and tracking tools |

## Roboflow model support

Roboflow model catalog:

```text
services/camera-tracking/roboflow_models.json
```

Included model keys:

| Key | Purpose |
|---|---|
| `football_players` | Detect ball, goalkeeper, player and referee |
| `football_ball` | Better ball-only detection |
| `football_field` | Pitch/keypoint calibration |

Run Roboflow tracking:

```bash
export ROBOFLOW_API_KEY=your_key_here
bash scripts/run-roboflow-tracking.sh 0 football_players 10
```

Read the guide:

```text
docs/roboflow-models.md
```

## Recommended architecture

```text
Camera / Capture Card / IP camera / Video file
        ↓
OBS Studio
        ↓
Scoreboard + Player Stats Overlay
        ↓
NodeCG / SPX-GC / CasparCG graphics
        ↓
Local YOLO or Roboflow detector writes ai_stats.json
        ↓
YouTube / TikTok / Instagram / Facebook / RTMP server
```

## Clone with all projects

```bash
git clone --recursive https://github.com/KobepayTech/kobestream.git
cd kobestream
```

If you already cloned it:

```bash
git submodule update --init --recursive
```

## Setup

```bash
bash scripts/setup-submodules.sh
```

## Run NodeCG graphics

```bash
bash scripts/run-nodecg.sh
```

## Run local YOLO tracking

```bash
bash scripts/run-ai-tracking.sh 0
```

## Run Roboflow tracking

```bash
export ROBOFLOW_API_KEY=your_key_here
bash scripts/run-roboflow-tracking.sh 0 football_players 10
```

## Update all projects later

```bash
bash scripts/update-submodules.sh
```

## Notes

This repo keeps third-party projects as Git submodules, not copied source code. That keeps each project's license, history, and updates clean. Never commit API keys to GitHub.
