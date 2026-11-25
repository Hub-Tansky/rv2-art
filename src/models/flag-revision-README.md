# Robo Violence 2 · CTF flag readability revision

This update contains `BlueFlag` and `RedFlag`. Each model uses 1,440 triangles and the same origin, 1.008 m pole height, and front edge along +X in Blender. The cloth extends about 0.68 m from the pole origin in frame 1. The sleeve stays upright while the free cloth rolls up to approximately 58° from vertical, with a small variation through the loop. The red texture has brighter chromatic midtones for contrast against the floor.

Each model folder contains the editable `.blend`, frame-1 static `.glb`, animated `.animated.glb`, base-colour PNGs, and a 7 m Blender comparison. Each animated export contains a single one-second loop with ten distinct poses and an end key that closes the loop. The static GLBs passed `gltf-to-dko.py`.

The geometry and animation were revised in Blender 5.3.0 with its built-in Python API. The provenance manifest identifies the project art licence and the supplied P3 cloth textures.

The original and revised static models were drawn in matching local CTF matches. The in-game comparison uses screenshot crops enlarged 4×. The installed test client uses uncompressed TGA, so the test copies used a lossless conversion of the supplied PNGs. The shipped GLBs embed PNG.
