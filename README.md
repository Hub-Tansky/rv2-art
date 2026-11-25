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
