# BSPprotect
Strips the entity lump from BSPs. This allows you to have a server running the real BSP, but serve the stripped down version to clients. 
Attempting to run the stripped down BSP on a server will cause a crash

Python script by GAMMACASE.

## Creating the protected BSP
### You trust the EXE
- Download latest exe from [releases](https://github.com/dysphie/bsp-protect/releases)
- Drag and drop your `.bsp` into `bspprotect.exe`. A new BSP with the suffix `.noents` will be created
- Copy this file to your download server and remove the `.noents` suffix

### You don't trust the EXE
- Install [Python](https://www.python.org/downloads)
- Run `bspprotect.py <bsp filename>`


