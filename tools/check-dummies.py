#!/usr/bin/env python3
"""Fails when a weapon model in the pack lacks a dummy the game reads (game/src/Weapon.cpp: flash<n> is where a shot
or throw starts, eject<n> where its shell flies out). A missing flash1 makes the weapon fire nothing: art pack 5's
Hand had none, so grenades and molotovs vanished (2026-11-26). Usage: check-dummies.py <pack>/main"""
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

main = sys.argv[1]
bad = []
for model, names in NEED.items():
    path = os.path.join(main, "models", model + ".DKO")
    if not os.path.isfile(path):
        continue  # not overridden: the base pack's model is used
    data = open(path, "rb").read()
    bad += [f"{path}: no dummy {n}" for n in names if DUMMY_NAME + n.encode() + b"\0" not in data]
for line in bad:
    print("FAIL", line)
print("ok: weapon dummies" if not bad else f"{len(bad)} missing dummies")
sys.exit(1 if bad else 0)
