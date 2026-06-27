# Kobestream

Kobestream is an open-source live streaming and sports broadcast stack for camera feeds, scoreboards, AR-style overlays, player stats, and future AI player/ball tracking.

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

## Recommended architecture

```text
Camera / Capture Card
        ↓
OBS Studio
        ↓
Scoreboard + Player Stats Overlay
        ↓
NodeCG / SPX-GC / CasparCG graphics
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

## Update all projects later

```bash
bash scripts/update-submodules.sh
```

## Notes

This repo keeps third-party projects as Git submodules, not copied source code. That keeps each project's license, history, and updates clean.
