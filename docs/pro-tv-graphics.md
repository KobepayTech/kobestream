# Professional TV graphics: OBS Studio + NodeCG

Use this mode for TV-style graphics: lower thirds, scoreboard, player cards and live stats panels.

## Start NodeCG

```bash
bash scripts/run-nodecg.sh
```

Open the NodeCG dashboard:

```text
http://localhost:9090
```

## OBS browser sources

Add these as OBS Browser Sources:

| Graphic | URL | Size |
|---|---|---|
| Scoreboard | `http://localhost:9090/bundles/kobestream/graphics/scoreboard.html` | 1920x1080 |
| Player stats | `http://localhost:9090/bundles/kobestream/graphics/player-stats.html` | 1920x1080 |
| Lower third | `http://localhost:9090/bundles/kobestream/graphics/lower-third.html` | 1920x1080 |
| AI tracking | `http://localhost:9090/bundles/kobestream/graphics/ai-tracking.html` | 1920x1080 |

## Control panel

The Kobestream NodeCG panel controls:

- Team names
- Scores
- Timer
- Player number and name
- Goals and assists
- Yellow and red cards
- Lower-third title and subtitle
