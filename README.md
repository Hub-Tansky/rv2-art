# Robo Violence 2 art pack

The art of [Robo Violence 2](https://github.com/Hub-Tansky/RoboViolence2): textures, skins, models and fonts that
the game downloads on first run and stacks over its free placeholder pack (ADR 0069, ADR ROBO-260).

**This is not free software.** The game is GPL-3.0-or-later; this pack is a separate work under
[LICENSE-ART.txt](LICENSE-ART.txt) (`LicenseRef-RV2-Art`). See [NOTICE.txt](NOTICE.txt) and
[TRADEMARKS.md](TRADEMARKS.md). The game runs without it.

## Layout

- `pack/main/pack.tsv`: one row per file (id, file, type, format, author, tool, licence, source), checked by the
  game repo's `tools/check-pack.py --base content/base-pack.tsv`.
- `pack/main/textures/...`: files at the same ids as the base pack.
- `pack/main/skins/<name>.png` (512x256 RGB, equirectangular) and `<name>_mask.png` (white where team colour goes):
  full-colour ball skins, new ids `skins/<name>` and `skins/<name>_mask` (game ADR ROBO-258). `skin10` is face 08,
  the default skin.
- `pack/main/models/<name>.DKO` with their PNG textures beside them: CTF flags (10 frames, a 1 s loop) and flag pods,
  converted with the game repo's `tools/gltf-to-dko.py` (ADR ROBO-247). Batch 2 adds the 14 weapon models plus
  Hand, Rocket, Douille, Gib, LifePack and Antena, exported straight from Blender. The DKO loads its texture by file
  name from its own folder, so the batch 2 texture rows use `<name>-texture` ids that override nothing.
- `pack/main/fonts/Teko-Medium.ttf` at id `fonts/babo`: the game font, baked at load (game ADR 0067, ROBO-265).
  Teko is under the SIL Open Font License 1.1 (`fonts/OFL.txt`), not the art licence.
- `src/textures/batch3/`: HUD icon masters, contact sheets and the delivered rows; `delivered/` keeps glowTrail and Smoke2 as
  delivered, before they were turned to run along the trail (the game maps a trail's V along it).
- `src/models/<name>/`: Blender sources, glTF exports and top-down comparisons of those models. Not in the release.
  `src/models/batch2-README.md` lists the weapon attachment dummies (`flash<n>`, `eject<n>`) and animated frames.

## Release

1. `tools/build-release.sh <n>` builds `rv2-art-<n>.tar.gz` (reproducible) and prints its SHA-256.
2. `gh release create rv2-art-<n> rv2-art-<n>.tar.gz --repo Hub-Tansky/rv2-art --title "Art pack <n>"`
3. In the game repo, pin version, URL and SHA-256 in `game/src/ArtPack.cpp`.

Never delete or replace a published release: installed games keep using its URL and hash.

## Releases

| Version | Content |
|---|---|
| 1 | Four map looks (floor, floor dirt, wall), sky, crosshairs, menu cursor, HUD flags, minimap dots, halo, shadow, splash |
| 2 | Pack 1 plus 17 full-colour ball skins with team masks (faces 01-03, 05-07, 08 as `skin10`, 09, 14-16, 18, 20-23, 25) |
| 3 | Pack 2 plus CTF models: BlueFlag, RedFlag (animated), BlueFlagPod, RedFlagPod |
| 4 | Pack 3 plus the game font: Teko SemiBold (OFL-1.1) replaces `babo.tga` |
| 5 | Pack 4 plus batch 2: all 14 weapon models (Knifes, Shield and ShieldMagnet animated), Hand, Rocket, Douille, Gib, LifePack, Antena |
| 6 | Pack 5 with fixes from the owner's playtest: Hand gets the `flash1` dummy that grenade and molotov throws start from (without it the throw did nothing), and the font is Teko Medium (500), slimmer than SemiBold |
| 7 | Pack 6 plus batch 3 combat effects: 10 hit splatters (white, tinted by the game), drip, explosion and bomb marks, smoke, glows, muzzle flash, hit vignette and 3 HUD icons; Knifes is now a ring of 8 blades, and Hand is re-exported with its `flash1` from source |
| 8 | Pack 7 with a black ball shadow: `BaboShadow` was white, and the game draws the player shadow untinted, so balls had a white glow under them |
| 9 | Pack 8 with round fixes 1: Pineapple grenade with a matching HUD icon, Break Action shotgun, Caged Ceramic SMG (85% of the old size), Honed Steel menu cursor, and the ten blood splats at 70% radius (`blood05` is now a pooled shape; the game tints them red again) |
| 10 | Pack 9 with SMG, ShotGun and Grenade at the right size: their DKOs had been exported at 100 units per metre instead of 200, so the guns sat half size inside the ball; `check-dummies.py` now checks the rail position |
| 11 | Pack 10 with round fixes 2: Twin Red Shells shotgun ammo icon (`CartridgeIcon`), Olive Wrap Molotov icon, Lighter Brass casing texture (`Douille.png`; the casing mesh is unchanged) |
