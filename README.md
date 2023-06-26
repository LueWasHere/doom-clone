# doom-clone

## Overview

I try to clone doom from the ground up. Not particularly following how DOOM itself was programmed, just trying to make something that mimics it

## Needed features

* 3D rendering engine.
* 3D camera workings.
* Player controls.
* Rendering of textures.
* Rendering of 2D objects in a 3D space.
* File system for storing map data.

## Wanted features

* Some sort of scripting language (Pretty much just making this into a fully-fledged game engine at this point)
* 3D models for enemies (Very basic, like PS1 level graphics) and also for things like the health packs to add more atmosphere (This could also be used to add more 3D objects into the scenery E.X: Pipes on the walls, volumetric walls, etc)
* More depth in maps, one version of the original map but along with a version that can have things like rooms on top of rooms
* Map editor
* Model editor (if 3D models are implemented)
* Ability to use not only a custom file system but also read the .wad files of the OG DOOMs

## Journal

*10:28PM 6/22/2023 (June 22nd 2023):* Development begins.

*10:39PM 6/22/2023 (June 22nd 2023):* A basic framework of different files is created, pretty much just everything I thought is necessary to start on. First commit starts now.

*10:43PM 6/22/2023 (June 22nd 2023):* I fix spelling error as to not look like an idiot.

*11:01PM 6/22/2023 (June 22nd 2023):* Begun to had utils that will be useful in the future like a rotate function. Also laid ground work in doom.py.

*2:43PM 6/23/2023 (June 23rd 2023):* Removed "rotate_around_point" because I thought it would be useless; But mostly because I gave up.

*2:58PM 6/23/2023 (June 23rd 2023):* Committing after having a crazy idea with making the scripting language I plan to implement more low level. I had the idea to have 1 master node that reads a compiled byte code version of the script (inspiration from Java) and continuously updates two sub nodes (threads) through an input buffer, the master node will then take from an output buffer on both of these and do various things with them. The more important of the two is the world node (See rendering.world.World) which houses continuous updating for player position, entity list (not just the enemy ais but also things like health backs or secrets), ai activity, and the world geometry. Having all these things contained in the node allows for the scripting language to interface with them through the proxy of the master node. I might scrap this approach, mostly 'cus I'm not sure how efficient it will be in terms of speed, but for now I think it's a pretty good and interesting way to do it.

*1:19PM 6/26/2023 (June 26th 2023):* Yeah, Imma just commit this before I forget for the 3rd time in a row...
