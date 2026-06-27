# Manual player stats: OBS Studio + Fly Scoreboard

Use this mode when a human operator enters match events live.

## Workflow

1. Open OBS Studio.
2. Add your camera or capture card.
3. Open Fly Scoreboard from `vendor/fly-scoreboard`.
4. Configure teams, timer, score, goals, assists, yellow cards and red cards.
5. Add the Fly Scoreboard output as an OBS browser/source overlay.
6. Stream to YouTube, Facebook, TikTok, Instagram through RTMP or a restream server.

## Operator checklist

| Match event | Operator action |
|---|---|
| Goal | Increase team score and player goals |
| Assist | Update player assists |
| Yellow card | Update player yellow cards |
| Red card | Update player red cards |
| Half time | Pause timer and show half-time graphic |
| Full time | Stop timer and show full-time graphic |

Recommended OBS layer order:

```text
Top:    Player stats popup
        Scoreboard
Bottom: Camera feed
```
