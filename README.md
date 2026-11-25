# es-theme-arcade-town

A cozy 16-bit pixel-art RPG town frontend theme for **ArkOS / EmulationStation** (designed for 640×480 4:3 handhelds).

## Features
- **Peaberry Base** pixel typography & warm cream/navy/coral retro palette
- **Dynamic Theme Configuration** (`Start → UI Settings → Theme Configuration`):
  - **System View Layout:** RPG Split Directory (default) or Town Street (3 Shops)
  - **Left Console List Style:** Coral RPG Bar (default), 2×4 Original Console Logo Grid, or Classic RPG Menu List
- **Status Bar:** Live clock + crisp pixel-grid SVG Wi-Fi & Battery icons
- **Audio:** Custom 16-bit RPG UI sound effects + CC0 8-bit chiptune BGM
- **Splash & Boot Logo:** Matching ES loading splash (`<view name="splash">`) + minimal iconic `extras/arkos-boot/logo.bmp`

## Local Preview (Batocera EmulationStation)

```bash
./run_es_preview.sh
```

## Installing to R36S (ArkOS)

1. Copy `theme.xml`, `systems/`, `_inc/`, and `art/shops/*.png` to `EASYROMS/themes/es-theme-arcade-town/`.
2. *(Optional)* Back up `BOOT/logo.bmp` and copy `extras/arkos-boot/logo.bmp` to `BOOT/logo.bmp`.
3. In ArkOS, select **es-theme-arcade-town** under **Start → UI Settings → Theme Set**.
