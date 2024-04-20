# ArcadeM3U
This Python script can be used to display Arcade/Neo Geo roms with proper names in MinUI. The script is utilizing the way m3u files work in MinUI and will create a proper folder structure and m3u files based on the zip rom files. You only need to provide the path to your Arcade/Neo Geo rom files and a dat file, e.g. a MAME dat file (https://www.progettosnaps.net/dats/MAME/) or one of the dats provided by Libretro (https://git.libretro.com/libretro/FBNeo/-/tree/master/dats)

Usage:
```python .\arcadem3u.py <path to roms> <path to dat file>```

Example:
```python .\arcadem3u.py "d:\roms\neogeo" "d:\dats\neogeo.dat"```

Before you run the script make sure to create a backup of your roms in case you are not satisfied with the result or something unexpected happens.

Before and after

![Alt text](./1_before.jpg?raw=true "Before")
![Alt text](./2_after.jpg?raw=true "After")
