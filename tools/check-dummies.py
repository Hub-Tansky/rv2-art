#!/usr/bin/env python3
"""Fails when a weapon model in the pack lacks a dummy the game reads (game/src/Weapon.cpp: flash<n> is where a shot
or throw starts, eject<n> where its shell flies out). A missing flash1 makes the weapon fire nothing: art pack 5's
Hand had none, so grenades and molotovs vanished (2026-11-26). Also fails when a rail weapon's mounting shoe is not at the
ball's side (nearest x 30 to 36 DKO units; the game draws models at 0.005): art pack 9's SMG and ShotGun were exported at
100 units per metre instead of 200, so they sat inside the ball at half size (2026-11-28). Usage: check-dummies.py <pack>/main"""
import os
import struct
import sys

NEED = {
    "Hand": ["flash1"],  # grenade and molotov throws
    "Bazooka": ["flash1"], "SMG": ["flash1", "eject1"], "ShotGun": ["flash1", "eject1"],
    "Sniper": ["flash1", "eject1"], "PhotonRifle": ["flash1"], "FlameThrower": ["flash1"],
    "DualMachineGun": ["flash1", "flash2", "eject1", "eject2"],
    "ChainGun": ["flash1", "flash2", "flash3", "eject1", "eject2", "eject3"],
}
DUMMY_NAME = struct.pack("<hh", 0x0400, 0x0110)  # DUMMY chunk, then its NAME chunk
RAIL = ["Bazooka", "ChainGun", "FlameThrower", "Hand", "Nuclear", "PhotonRifle", "SMG", "ShotGun", "Sniper"]
SHOE_X = (30.0, 36.0)  # BV2 and art packs 5 to 8 put the shoe at x 33 (the ball's radius)
VERTEX_ARRAY = struct.pack("<h", 0x0343)


def nearest_x(data):
    """Smallest vertex x of a one-frame DKO, from each NB_VERTEX count and the VERTEX_ARRAY after it."""
    xs, i = [], 0
    while True:
        i = data.find(struct.pack("<h", 0x0342), i)
        if i < 0:
            return min(xs) if xs else None
        n = struct.unpack_from("<i", data, i + 2)[0]
        if data[i + 6:i + 8] == VERTEX_ARRAY and 0 < n < 10**6:
            xs += struct.unpack_from(f"<{n * 3}f", data, i + 8)[0::3]
        i += 2

main = sys.argv[1]
bad = []
for model, names in NEED.items():
    path = os.path.join(main, "models", model + ".DKO")
    if not os.path.isfile(path):
        continue  # not overridden: the base pack's model is used
    data = open(path, "rb").read()
    bad += [f"{path}: no dummy {n}" for n in names if DUMMY_NAME + n.encode() + b"\0" not in data]
for model in RAIL:
    path = os.path.join(main, "models", model + ".DKO")
    if os.path.isfile(path):
        x = nearest_x(open(path, "rb").read())
        if x is None or not SHOE_X[0] <= x <= SHOE_X[1]:
            bad.append(f"{path}: mounting shoe at x {x}, not on the rail ({SHOE_X[0]} to {SHOE_X[1]}); wrong export scale?")
for line in bad:
    print("FAIL", line)
print("ok: weapon dummies and rail" if not bad else f"{len(bad)} problems")
sys.exit(1 if bad else 0)
