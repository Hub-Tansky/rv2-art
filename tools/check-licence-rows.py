#!/usr/bin/env python3
"""Every row of the art pack manifest carries the art licence, an author and a tool, and its file exists. A font may
instead be under the SIL Open Font License 1.1 (OFL-1.1), with OFL.txt beside it (Teko, game ROBO-265)."""
import os
import sys

manifest = sys.argv[1]
root = os.path.dirname(manifest)
bad = 0
for n, line in enumerate(open(manifest, encoding="utf-8"), 1):
    cols = line.rstrip("\n").split("\t")
    if n == 1 or line.startswith("#"):
        continue
    ofl = len(cols) >= 8 and cols[6] == "OFL-1.1" and cols[2] == "font" and os.path.isfile(os.path.join(root, os.path.dirname(cols[1]), "OFL.txt"))
    if len(cols) < 8 or (cols[6] != "LicenseRef-RV2-Art" and not ofl) or not cols[4] or not cols[5] or not os.path.isfile(os.path.join(root, cols[1])):
        print(f"{manifest}:{n}: bad row: {line.strip()}")
        bad += 1
sys.exit(1 if bad else 0)
