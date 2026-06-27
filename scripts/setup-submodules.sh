#!/bin/bash
set -e

mkdir -p vendor

git submodule add https://github.com/obsproject/obs-studio.git vendor/obs-studio || true
git submodule add https://github.com/mmlTools/fly-scoreboard.git vendor/fly-scoreboard || true
git submodule add https://github.com/nodecg/nodecg.git vendor/nodecg || true
git submodule add https://github.com/JimThatcher/sport-streamer.git vendor/sport-streamer || true
git submodule add https://github.com/CasparCG/server.git vendor/casparcg-server || true
git submodule add https://github.com/TuomoKu/SPX-GC.git vendor/spx-gc || true
git submodule add https://github.com/roboflow/sports.git vendor/roboflow-sports || true

git submodule update --init --recursive

echo "Kobestream submodules are ready. Commit and push with:"
echo "git add . && git commit -m 'Add broadcast stack submodules' && git push"
