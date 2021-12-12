# BSPprotect
Strips entity lump from BSPs so maps can only be played in a specific server. Attempting to run the downloaded BSP anywhere else will cause a crash.

Python script by GAMMACASE

## Usage

### Option A:
- Download latest exe from [releases](https://github.com/dysphie/bsp-protect/releases)
- Drag and drop your `.bsp` into `bspprotect.exe`. A new BSP with the suffix `.noents` will be created
- Copy this file to your download server and remove the `.noents` suffix

### Option B:
- Install [Python](https://www.python.org/downloads)
- Run `bspprotect.py <bsp filename>`
