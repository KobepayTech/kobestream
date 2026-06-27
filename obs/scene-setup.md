# OBS scene setup

Create a scene called `Kobestream Match`.

## Sources

1. Camera or capture card
2. Scoreboard browser source
3. Player stats browser source
4. Lower-third browser source
5. AI tracking browser source

## Browser source settings

- Width: `1920`
- Height: `1080`
- FPS: `30`
- Shutdown source when not visible: enabled
- Refresh browser when scene becomes active: enabled

## Kobestream NodeCG URLs

| Source name | URL |
|---|---|
| `KS Scoreboard` | `http://localhost:9090/bundles/kobestream/graphics/scoreboard.html` |
| `KS Player Stats` | `http://localhost:9090/bundles/kobestream/graphics/player-stats.html` |
| `KS Lower Third` | `http://localhost:9090/bundles/kobestream/graphics/lower-third.html` |
| `KS AI Tracking` | `http://localhost:9090/bundles/kobestream/graphics/ai-tracking.html` |
