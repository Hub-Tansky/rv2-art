#!/bin/sh
# Builds rv2-art-<version>.tar.gz from pack/ and prints its SHA-256 (the game pins it in game/src/ArtPack.cpp).
# Reproducible: sorted names, fixed owner and time, gzip without a name or time stamp. Needs GNU tar.
set -eu
version=${1:?usage: tools/build-release.sh <version>}
cd "$(dirname "$0")/.."
python3 tools/check-licence-rows.py pack/main/pack.tsv
out="rv2-art-$version.tar.gz"
cp LICENSE-ART.txt NOTICE.txt TRADEMARKS.md pack/
tar --sort=name --owner=0 --group=0 --numeric-owner --mtime='2026-01-01 00:00Z' \
    -C pack -cf - main LICENSE-ART.txt NOTICE.txt TRADEMARKS.md | gzip -9n > "$out"
rm pack/LICENSE-ART.txt pack/NOTICE.txt pack/TRADEMARKS.md
sha256sum "$out"
