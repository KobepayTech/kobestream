#!/bin/bash
set -e

SOURCE="${1:-0}"

bash scripts/setup-submodules.sh

echo "Start NodeCG:"
echo "  bash scripts/run-nodecg.sh"
echo ""
echo "Start camera tracking:"
echo "  bash scripts/run-ai-tracking.sh $SOURCE"
echo ""
echo "Then add OBS browser sources from obs/scene-setup.md"
