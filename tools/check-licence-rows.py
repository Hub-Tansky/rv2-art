#!/usr/bin/env python3
"""Every row of the art pack manifest carries the art licence, an author and a tool, and its file exists."""
import os
import sys

manifest = sys.argv[1]
root = os.path.dirname(manifest)
bad = 0
for n, line in enumerate(open(manifest, encoding="utf-8"), 1):
    cols = line.rstrip("\n").split("\t")
    if n == 1 or line.startswith("#"):
        continue
    if len(cols) < 8 or cols[6] != "LicenseRef-RV2-Art" or not cols[4] or not cols[5] or not os.path.isfile(os.path.join(root, cols[1])):
        print(f"{manifest}:{n}: bad row: {line.strip()}")
        bad += 1
sys.exit(1 if bad else 0)
