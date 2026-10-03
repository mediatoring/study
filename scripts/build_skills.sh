#!/usr/bin/env bash
# Sestaví ZIP každého skillu ze složky skills/ do dist/.
# Výsledné ZIPy se nahrávají jako assety do GitHub Release s tagem skills-v1.
set -euo pipefail
cd "$(dirname "$0")/.."
rm -rf dist && mkdir dist
for dir in skills/*/; do
  name=$(basename "$dir")
  (cd skills && zip -qr "../dist/$name.zip" "$name")
  echo "dist/$name.zip"
done
