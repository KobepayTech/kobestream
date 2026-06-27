#!/bin/bash
set -e

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
NODECG_DIR="$ROOT_DIR/vendor/nodecg"
BUNDLE_SRC="$ROOT_DIR/nodecg/bundles/kobestream"
BUNDLE_DST="$NODECG_DIR/bundles/kobestream"

if [ ! -d "$NODECG_DIR" ]; then
  echo "NodeCG submodule not found. Run: bash scripts/setup-submodules.sh"
  exit 1
fi

mkdir -p "$NODECG_DIR/bundles"
cp -R "$BUNDLE_SRC" "$BUNDLE_DST"

cd "$NODECG_DIR"
if [ ! -d node_modules ]; then
  npm install
fi

npm start -- --port 9090
