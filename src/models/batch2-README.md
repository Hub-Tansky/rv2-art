# Robo Violence 2 · Batch 2 model pack

The catalog contains 20 models and two shared texture entries. Each model folder contains an editable Blender source, GLB, DKO, baked base-colour PNG, and a review image. The review folder has an overhead sheet for the eight primary weapons and a sheet for gear and projectiles.

For a match, use the DKOs and PNGs under `runtime/main/models`. Merge the rows in `runtime/main/pack.tsv` into the destination manifest when combining this overlay with art pack 4. The source catalog has its own provenance manifest. All game textures are PNG.

Mounted models use metres, +Z up and +Y forward, with their origin at the ball’s floor contact. The primary weapons follow the approved Bazooka fit on the +X rail. DualMachineGun has a second mirrored assembly. Thrown objects and debris use their own effect pivots.

## Attachment points

| Model | Muzzles | Ejection points |
| --- | --- | --- |
| Bazooka | `flash1` | `eject1` |
| SMG, ShotGun, Sniper, PhotonRifle, FlameThrower | `flash1` | `eject1` |
| DualMachineGun | `flash1`, `flash2` | `eject1`, `eject2` |
| ChainGun | `flash1`, `flash2`, `flash3` | `eject1`, `eject2` plus `eject3` at the same point as `eject2` |

The ChainGun alias keeps the shell lookup valid when the client indexes ejection points by muzzle number. The other models have no firing or shell markers.

## Animated items

The `.animated.glb` files contain editable clip exports. The DKOs include the sampled motion, and the plain GLBs show the rest pose.

| Model | DKO frames | Motion |
| --- | ---: | --- |
| Knifes | 11 | Retracted to deployed, with the return driven by the game |
| Shield | 21 | Deploys and collapses. The game repeats the sector around the ball |
| ShieldMagnet | 21 | Magnet plates rise and settle |

`Knife.png` is the shared texture for Knifes. `Shieldtga.png` is the shared texture for Shield and the low-profile sensor kept under the Antena asset ID. Hand is a small rail-mounted cradle for thrown items. Gib is fractured metal armour. LifePack has a red cross.

Original models and base colours were made for Robo Violence 2 by Codex in Blender 5.3.0 using its built-in Python API and the project’s rail concepts. The approved Bazooka is included. All 20 models were verified for export and loaded in a local CTF smoke test. That test used an older client and temporary textures in its native format, and exercised ChainGun firing with bots. The supplied runtime uses PNG.
