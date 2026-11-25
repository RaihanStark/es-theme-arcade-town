# Arcade Town — Art Style Guide & Reusable AI Prompts

Use this guide and prompt templates whenever generating new system shops, town backdrops, or pixel-art props for **es-theme-arcade-town** so every asset stays 100% visually consistent.

---

## 1. Core Color Palette

| Role | Hex | Usage |
| :--- | :--- | :--- |
| **Background / Sky Cream** | `#ECE8E1` | Flat solid background for shop sprites & sky canvas |
| **Deep Navy Ink (Outlines)** | `#1E2448` | Crisp 1–2px pixel outlines, text, borders, curb line |
| **Cobalt Blue** | `#1D4B8F` | Roof tiles, secondary walls, portrait backdrop |
| **Teal** | `#0097A7` | Trim, shutters, neighbor buildings, accents |
| **Cyan** | `#5CD6E6` | Glowing signs, CRT/handheld screens, highlights |
| **Coral Pink** | `#E86F7A` | Awnings, pillars, active menu selector, signage |
| **Soft Pink** | `#F29FA3` | Highlights on coral elements, blush, bunting |
| **Warm Gold** | `#D99B38` | Doors, frames, lamp glow, lettering, coins |
| **Paper / Dialogue Fill** | `#EAE7F0` | RPG panels, top header bar, shop walls |
| **Lavender Bevel** | `#B7B5D8` | Inner RPG frame bevel, clouds, soft sky accents |

**Font:** `PeaberryBase.ttf` (located in `_inc/fonts/PeaberryBase.ttf`)

---

## 2. Master Shop Sprite Prompt Template

Copy and fill in `[SYSTEM_LABEL]` and `[THEME_PROPS]`:

```text
Generate a crisp, charming 16-bit pixel-art illustration of a cozy retro "[SYSTEM_LABEL]" video game shop building.
Style requirements:
- Clean, crisp pixel art with deep navy outlines (#1E2448)
- Limited retro-pastel palette: cobalt blue (#1D4B8F), teal (#0097A7), cyan (#5CD6E6), coral pink (#E86F7A), warm gold (#D99B38), cream (#F5EFE6)
- Flat solid warm off-white background (#ECE8E1) with NO gradients, NO drop shadows on the background, NO ground shadow, NO UI boxes, NO text box at the bottom
- A cute two-story indie pixel-art game shop storefront featuring: [THEME_PROPS]
- Centered composition with generous margin of solid #ECE8E1 background around all four sides of the building, 4:3 or 1:1 aspect ratio
```

---

## 3. Ready-to-Use Prompts for Remaining Systems

### Nintendo 64 (`art/shops/n64_raw.png`)
```text
Generate a crisp, charming 16-bit pixel-art illustration of a cozy retro "N64" Nintendo 64 game shop building.
Style requirements:
- Clean, crisp pixel art with deep navy outlines (#1E2448)
- Limited retro-pastel palette: cobalt blue (#1D4B8F), teal (#0097A7), cyan (#5CD6E6), coral pink (#E86F7A), warm gold (#D99B38), cream (#F5EFE6)
- Flat solid warm off-white background (#ECE8E1) with NO gradients, NO shadows on the background, NO UI boxes, NO text box at the bottom
- A cute two-story indie pixel-art game shop storefront with a colorful 3D pixel cube "N64" rooftop sign, striped coral-and-cream awning, giant pixel trident controller sign hanging on the side, cartridge displays in the glowing window, and tiny potted plants by the door
- Centered composition with generous margin of solid #ECE8E1 background around the building, 4:3 aspect ratio
```

### Game Boy (`art/shops/gb_raw.png`)
```text
Generate a crisp, charming 16-bit pixel-art illustration of a cozy retro "GB" original Game Boy pocket shop building.
Style requirements:
- Clean, crisp pixel art with deep navy outlines (#1E2448)
- Limited retro-pastel palette: cobalt blue (#1D4B8F), teal (#0097A7), cyan (#5CD6E6), coral pink (#E86F7A), warm gold (#D99B38), cream (#F5EFE6), with subtle olive-green Game Boy screen glow
- Flat solid warm off-white background (#ECE8E1) with NO gradients, NO shadows on the background, NO UI boxes, NO text box at the bottom
- A cute compact two-story indie pixel-art shop shaped like a classic dot-matrix Game Boy with a glowing olive-tinted upper display window, burgundy/coral A & B round awning badges, hanging cartridge stand outside, and a cozy shopkeeper waving inside
- Centered composition with generous margin of solid #ECE8E1 background around the building, 4:3 aspect ratio
```

### PICO-8 (`art/shops/pico-8_raw.png`)
```text
Generate a crisp, charming 16-bit pixel-art illustration of a cozy indie "PICO-8" fantasy console micro-shop kiosk.
Style requirements:
- Clean, crisp pixel art with deep navy outlines (#1E2448)
- Limited retro-pastel palette: cobalt blue (#1D4B8F), teal (#0097A7), cyan (#5CD6E6), coral pink (#E86F7A), warm gold (#D99B38), cream (#F5EFE6)
- Flat solid warm off-white background (#ECE8E1) with NO gradients, NO shadows on the background, NO UI boxes, NO text box at the bottom
- A tiny whimsical indie pixel-art game stand with a rainbow-pixel "PICO-8" rooftop marquee, tiny pastel cartridge rack out front, colorful bunting flags, a glowing miniature monitor on the counter, and a cute pixel cat sitting on the roof
- Centered composition with generous margin of solid #ECE8E1 background around the building, 4:3 aspect ratio
```

### J2ME / Java Mobile (`art/shops/j2me_raw.png`)
```text
Generate a crisp, charming 16-bit pixel-art illustration of a cozy retro "J2ME" classic flip-phone mobile game shop building.
Style requirements:
- Clean, crisp pixel art with deep navy outlines (#1E2448)
- Limited retro-pastel palette: cobalt blue (#1D4B8F), teal (#0097A7), cyan (#5CD6E6), coral pink (#E86F7A), warm gold (#D99B38), cream (#F5EFE6)
- Flat solid warm off-white background (#ECE8E1) with NO gradients, NO shadows on the background, NO UI boxes, NO text box at the bottom
- A cute two-story indie pixel-art corner shop with a retro pixel keypad phone rooftop sign, tiny steaming coffee-cup pixel badge hanging on the side, striped teal awning, and glowing pixel phone displays in the window
- Centered composition with generous margin of solid #ECE8E1 background around the building, 4:3 aspect ratio
```

### PyMO / Visual Novels (`art/shops/pymo_raw.png`)
```text
Generate a crisp, charming 16-bit pixel-art illustration of a cozy "PYMO" visual novel bookshop & reading cafe.
Style requirements:
- Clean, crisp pixel art with deep navy outlines (#1E2448)
- Limited retro-pastel palette: cobalt blue (#1D4B8F), teal (#0097A7), cyan (#5CD6E6), coral pink (#E86F7A), warm gold (#D99B38), cream (#F5EFE6)
- Flat solid warm off-white background (#ECE8E1) with NO gradients, NO shadows on the background, NO UI boxes, NO text box at the bottom
- A charming two-story pixel-art indie bookshop storefront with an open-book pixel rooftop sign, flower boxes on the upper windows, striped coral awning, wooden bookshelf stand outside the door, and warm golden reading lamps glowing inside
- Centered composition with generous margin of solid #ECE8E1 background around the building, 4:3 aspect ratio
```

### ArkOS Options / Workshop (`art/shops/retropie_raw.png`)
```text
Generate a crisp, charming 16-bit pixel-art illustration of a cozy retro "TOOLS" handheld repair workshop building.
Style requirements:
- Clean, crisp pixel art with deep navy outlines (#1E2448)
- Limited retro-pastel palette: cobalt blue (#1D4B8F), teal (#0097A7), cyan (#5CD6E6), coral pink (#E86F7A), warm gold (#D99B38), cream (#F5EFE6)
- Flat solid warm off-white background (#ECE8E1) with NO gradients, NO shadows on the background, NO UI boxes, NO text box at the bottom
- A cute two-story pixel-art repair workshop with a crossed-wrench and gear rooftop sign, Wi-Fi antenna tower on the roof, tool pegboard visible through the window, and a tiny retro console workbench out front
- Centered composition with generous margin of solid #ECE8E1 background around the building, 4:3 aspect ratio
```

---

## 4. Town Street Backdrop Prompt (Used for `art/town_backdrop_raw.jpg`)

```text
Generate a cozy, crisp 16-bit pixel-art static town street background scene (NO main foreground building in the center—leave the center open so a foreground shop sprite can be placed on top of the sidewalk!).
Style requirements:
- Match the PortMaster Patching Shop pixel-art aesthetic: deep navy outlines (#1E2448), soft warm cream/off-white sky (#ECE8E1), muted pastel cobalt blue (#1D4B8F), teal (#0097A7), soft lavender (#B7B5D8), coral pink (#E86F7A), warm gold (#D99B38)
- Top 60%: airy warm cream sky (#ECE8E1) with a few tiny crisp pixel clouds, distant faint pastel pixel rooftops/water-tower/trees along the far horizon, and a thin powerline or tiny bunting string near the top corners
- Left & right edges: cozy pixel-art streetlamp, tiny potted trees/bushes, and peeking edges of neighboring pastel shops
- Bottom 15%: a flat, horizontal pixel-art sidewalk / cobblestone ground strip running edge-to-edge so a foreground pixel-art shop building can stand cleanly on it
- Aspect ratio: square / 1:1 (will fit inside a 366x356 panel)
- NO text, NO UI boxes, NO characters in the center.
```

---

## 5. Adding New Generated Art to the Theme

1. Save any newly generated shop image into `art/shops/<system>_raw.jpg` (or `.png`), e.g. `art/shops/n64_raw.png`.
2. Run the asset processor:
   ```bash
   python3 build_assets.py
   ```
   It automatically flood-fill removes the `#ECE8E1` background from the corners (keeping interior cream details intact), crops tightly, and outputs `art/shops/<system>.png`.
3. Update `preview.html` (if previewing) to point that system's `shop:` field to `/art/shops/<system>.png`. EmulationStation (`_layout_split.xml`) picks up `./art/shops/${system.theme}.png` automatically!
