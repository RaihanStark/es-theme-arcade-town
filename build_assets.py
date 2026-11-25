#!/usr/bin/env python3
"""
Generate pixel-perfect UI frames, RPG dialogue boxes, portraits, and icons
for es-theme-arcade-town (native 640x480 R36S resolution).
Also post-processes any generated *_raw.png shop illustrations into crisp
640x320 transparent/matched pixel-art shop cards.
"""
import os
from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).parent
FRAMES = ROOT / "_inc" / "frames"
PORTRAITS = ROOT / "_inc" / "portraits"
ICONS = ROOT / "_inc" / "icons"
SHOPS = ROOT / "art" / "shops"

for d in (FRAMES, PORTRAITS, ICONS, SHOPS):
    d.mkdir(parents=True, exist_ok=True)

# Exact PortMaster Patching Shop inspired palette
BG_CREAM = (236, 232, 225, 255)       # #ECE8E1
NAVY = (30, 36, 72, 255)              # #1E2448
BLUE = (29, 75, 143, 255)             # #1D4B8F
TEAL = (0, 151, 167, 255)             # #0097A7
CYAN = (92, 214, 230, 255)            # #5CD6E6
CORAL = (232, 111, 122, 255)          # #E86F7A
PINK = (242, 159, 163, 255)           # #F29FA3
GOLD = (217, 155, 56, 255)            # #D99B38
PAPER = (234, 231, 240, 255)          # #EAE7F0
LAVENDER = (183, 181, 216, 255)       # #B7B5D8
SHADOW = (214, 209, 200, 255)         # #D6D1C8
WHITE = (250, 248, 245, 255)


def draw_rpg_box(draw: ImageDraw.ImageDraw, x0: int, y0: int, x1: int, y1: int, fill=PAPER):
    """Draw a crisp double-bordered RPG dialogue/menu box matching the Patching Shop aesthetic."""
    # Soft drop shadow
    draw.rectangle([x0 + 4, y0 + 4, x1 + 4, y1 + 4], fill=SHADOW)
    # Outer navy border (2px)
    draw.rectangle([x0, y0, x1, y1], fill=NAVY)
    # Lavender bevel (2px)
    draw.rectangle([x0 + 2, y0 + 2, x1 - 2, y1 - 2], fill=LAVENDER)
    # Inner navy hairline (2px)
    draw.rectangle([x0 + 5, y0 + 5, x1 - 5, y1 - 5], fill=NAVY)
    # Interior fill
    draw.rectangle([x0 + 7, y0 + 7, x1 - 7, y1 - 7], fill=fill)


def build_system_bg():
    # 1) Split RPG Directory background (multi-system list on left + full-height shop showcase on right)
    img = Image.new("RGBA", (640, 480), BG_CREAM)
    d = ImageDraw.Draw(img)

    # Top compact status header bar
    d.rectangle([0, 0, 640, 36], fill=PAPER)
    d.rectangle([0, 34, 640, 36], fill=NAVY)
    d.rectangle([0, 36, 640, 39], fill=LAVENDER)
    for idx, col in enumerate([CORAL, GOLD, TEAL, BLUE]):
        cx = 562 + idx * 16
        d.rectangle([cx, 12, cx + 10, 22], fill=NAVY)
        d.rectangle([cx + 2, 14, cx + 8, 20], fill=col)

    # Left: Vertical System Directory RPG box (x=18..228, y=46..438 — leaves clean 42px bottom strip for footer!)
    draw_rpg_box(d, 18, 46, 228, 438, fill=PAPER)

    # Right: Single Full-Height Shop Showcase Window (x=242..622, y=46..438)
    draw_rpg_box(d, 242, 46, 622, 438, fill=BG_CREAM)

    # Composite static pixel-art town backdrop inside the showcase (x=249..615, y=53..392)
    backdrop_path = ROOT / "art" / "town_backdrop_raw.jpg"
    if backdrop_path.exists():
        bd = Image.open(backdrop_path).convert("RGBA")
        bd = bd.resize((366, 339), Image.Resampling.LANCZOS)
        img.paste(bd, (249, 53))
        d = ImageDraw.Draw(img)
    else:
        d.rectangle([258, 376, 606, 378], fill=NAVY)
        d.rectangle([264, 379, 600, 383], fill=SHADOW)

    # Subtle footer bar inside bottom of showcase (y=392..431)
    d.rectangle([249, 392, 615, 431], fill=PAPER)
    d.rectangle([249, 392, 615, 394], fill=NAVY)
    d.rectangle([249, 394, 615, 396], fill=LAVENDER)

    img.save(FRAMES / "bg_system_split.png")

    # 2) Town Street background (3 shops side-by-side + bottom RPG dialogue box)
    img2 = Image.new("RGBA", (640, 480), BG_CREAM)
    d2 = ImageDraw.Draw(img2)

    # Top header bar
    d2.rectangle([0, 0, 640, 34], fill=PAPER)
    d2.rectangle([0, 32, 640, 34], fill=NAVY)
    d2.rectangle([0, 34, 640, 37], fill=LAVENDER)

    # Continuous cobblestone/ground street strip
    d2.rectangle([0, 322, 640, 325], fill=NAVY)
    d2.rectangle([0, 325, 640, 338], fill=(224, 219, 210, 255))
    for x in range(12, 640, 28):
        d2.rectangle([x, 329, x + 14, 331], fill=SHADOW)

    # Nameplate tab
    nx0, ny0, nx1, ny1 = 22, 330, 178, 360
    d2.rectangle([nx0, ny0, nx1, ny1], fill=NAVY)
    d2.rectangle([nx0 + 2, ny0 + 2, nx1 - 2, ny1 - 2], fill=LAVENDER)
    d2.rectangle([nx0 + 4, ny0 + 4, nx1 - 4, ny1 - 4], fill=NAVY)
    d2.rectangle([nx0 + 6, ny0 + 6, nx1 - 6, ny1 - 6], fill=PAPER)

    # Main bottom RPG dialogue box
    draw_rpg_box(d2, 22, 358, 618, 464, fill=PAPER)

    # Portrait inset
    px0, py0, px1, py1 = 36, 374, 100, 448
    d2.rectangle([px0, py0, px1, py1], fill=NAVY)
    d2.rectangle([px0 + 2, py0 + 2, px1 - 2, py1 - 2], fill=BLUE)
    d2.rectangle([px0 + 4, py0 + 4, px1 - 4, py1 - 4], fill=NAVY)

    tx, ty = 596, 444
    for i in range(5):
        d2.line([(tx - 4 + i, ty + i), (tx + 4 - i, ty + i)], fill=CORAL)

    img2.save(FRAMES / "bg_system_street.png")
    # Keep bg_system.png as default alias to split
    img.save(FRAMES / "bg_system.png")


def build_gamelist_bg():
    img = Image.new("RGBA", (640, 480), BG_CREAM)
    d = ImageDraw.Draw(img)

    # Top header banner bar
    d.rectangle([0, 0, 640, 38], fill=PAPER)
    d.rectangle([0, 36, 640, 38], fill=NAVY)
    d.rectangle([0, 38, 640, 41], fill=LAVENDER)
    # Decorative colored pixel dots on top-right
    for idx, col in enumerate([CORAL, GOLD, TEAL, BLUE]):
        cx = 562 + idx * 16
        d.rectangle([cx, 13, cx + 10, 23], fill=NAVY)
        d.rectangle([cx + 2, 15, cx + 8, 21], fill=col)

    # Left gamelist RPG box (leaves clean bottom strip for footer)
    draw_rpg_box(d, 18, 46, 326, 326, fill=PAPER)

    # Right artwork / video showcase RPG box
    draw_rpg_box(d, 338, 46, 622, 326, fill=PAPER)
    # Inner screen recess for screenshot/boxart
    d.rectangle([352, 60, 608, 272], fill=NAVY)
    d.rectangle([354, 62, 606, 270], fill=(38, 45, 86, 255))
    # Little console LED dot below screen
    d.rectangle([354, 282, 362, 290], fill=NAVY)
    d.rectangle([356, 284, 360, 288], fill=CORAL)
    d.rectangle([368, 282, 376, 290], fill=NAVY)
    d.rectangle([370, 284, 374, 288], fill=CYAN)

    # Bottom RPG description dialogue box (y=338..438)
    draw_rpg_box(d, 18, 338, 622, 438, fill=PAPER)

    img.save(FRAMES / "bg_gamelist.png")


def build_selector_and_menu():
    # Selector bar for gamelist
    sel = Image.new("RGBA", (290, 30), (0, 0, 0, 0))
    d = ImageDraw.Draw(sel)
    d.rectangle([0, 0, 289, 29], fill=NAVY)
    d.rectangle([2, 2, 287, 27], fill=CORAL)
    d.rectangle([2, 2, 287, 5], fill=PINK)
    # Pixel cursor arrow on left
    for i in range(5):
        d.line([(8 + i, 10 + i), (8 + i, 19 - i)], fill=WHITE)
    sel.save(FRAMES / "selector.png")

    # Pure flat solid paper 9-patch for ES MenuComponent (no border/padding lines)
    m9 = Image.new("RGBA", (48, 48), PAPER)
    m9.save(FRAMES / "menu_frame_9patch.png")

    # Solid cream fullscreen backdrop behind ES menus (via fadePath)
    fade = Image.new("RGBA", (64, 64), BG_CREAM)
    fade.save(FRAMES / "menu_fade.png")

    # Fullscreen 640x480 RPG Menu background (used by HTML preview)
    mf = Image.new("RGBA", (640, 480), BG_CREAM)
    dmf = ImageDraw.Draw(mf)
    dmf.rectangle([0, 0, 640, 38], fill=PAPER)
    dmf.rectangle([0, 36, 640, 38], fill=NAVY)
    dmf.rectangle([0, 38, 640, 41], fill=LAVENDER)
    for idx, col in enumerate([CORAL, GOLD, TEAL, BLUE]):
        cx = 562 + idx * 16
        dmf.rectangle([cx, 13, cx + 10, 23], fill=NAVY)
        dmf.rectangle([cx + 2, 15, cx + 8, 21], fill=col)
    draw_rpg_box(dmf, 18, 52, 622, 462, fill=PAPER)
    dmf.rectangle([25, 422, 615, 424], fill=LAVENDER)
    mf.save(FRAMES / "menu_fullscreen.png")
    m9.save(FRAMES / "menu_bg.png")


def draw_pixel_portrait(name: str, body_col, accent_col, screen_col, motif: str):
    """Draw a charming 16x16 pixel-art shopkeeper/console portrait, upscaled 4x to 64x64."""
    im = Image.new("RGBA", (16, 16), BLUE)
    p = im.load()

    def rect(x0, y0, x1, y1, c):
        for y in range(y0, y1 + 1):
            for x in range(x0, x1 + 1):
                if 0 <= x < 16 and 0 <= y < 16:
                    p[x, y] = c

    # Subtle checkerboard background
    for y in range(16):
        for x in range(16):
            p[x, y] = (34, 52, 102, 255) if (x + y) % 2 == 0 else (28, 44, 88, 255)

    # Robot / console mascot head
    rect(3, 2, 12, 11, NAVY)
    rect(4, 3, 11, 10, body_col)
    # Screen face
    rect(5, 4, 10, 8, NAVY)
    rect(5, 4, 10, 7, screen_col)
    # Cute pixel eyes
    p[6, 5] = NAVY
    p[9, 5] = NAVY
    p[6, 6] = NAVY
    p[9, 6] = NAVY
    # Smile / blush
    p[5, 7] = accent_col
    p[10, 7] = accent_col
    # Antenna / hat motif
    if motif == "antenna":
        p[7, 1] = NAVY; p[8, 1] = accent_col
    elif motif == "crown":
        p[5, 1] = GOLD; p[8, 1] = GOLD; p[10, 1] = GOLD
    elif motif == "ears":
        p[3, 1] = accent_col; p[12, 1] = accent_col
    # Shoulders
    rect(2, 12, 13, 15, NAVY)
    rect(3, 13, 12, 15, accent_col)
    rect(6, 13, 9, 15, WHITE)

    im = im.resize((64, 64), Image.Resampling.NEAREST)
    im.save(PORTRAITS / f"{name}.png")


def build_portraits():
    specs = {
        "ports":   (TEAL,   CORAL, CYAN,  "antenna"),
        "gba":     (BLUE,   PINK,  CYAN,  "ears"),
        "snes":    (LAVENDER, CORAL, WHITE, "crown"),
        "psx":     (PAPER,  TEAL,  CYAN,  "antenna"),
        "n64":     (GOLD,   BLUE,  WHITE, "crown"),
        "gb":      (PAPER,  GOLD,  (155, 188, 15, 255), "ears"),
        "pico-8":  (CORAL,  GOLD,  CYAN,  "antenna"),
        "j2me":    (CYAN,   BLUE,  WHITE, "ears"),
        "pymo":    (PINK,   CORAL, WHITE, "crown"),
        "options": (GOLD,   TEAL,  WHITE, "antenna"),
        "default": (TEAL,   GOLD,  CYAN,  "antenna"),
    }
    for name, (b, a, s, m) in specs.items():
        draw_pixel_portrait(name, b, a, s, m)


def process_raw_shops():
    """Flood-fill remove outer cream background from *_raw.{png,jpg} and sit flush on 560x310."""
    from collections import deque

    for raw in list(SHOPS.glob("*_raw.png")) + list(SHOPS.glob("*_raw.jpg")):
        sys_name = raw.stem.replace("_raw", "")
        out_path = SHOPS / f"{sys_name}.png"
        im = Image.open(raw).convert("RGBA")
        w, h = im.size
        px = im.load()

        # Sample average corner color
        corners = [px[2, 2], px[w - 3, 2], px[2, h - 3], px[w - 3, h - 3]]
        bg_r = sum(c[0] for c in corners) // 4
        bg_g = sum(c[1] for c in corners) // 4
        bg_b = sum(c[2] for c in corners) // 4

        def is_bg(r, g, b):
            return abs(r - bg_r) < 32 and abs(g - bg_g) < 32 and abs(b - bg_b) < 32

        # Corner flood-fill so interior cream details stay intact!
        visited = bytearray(w * h)
        q = deque()
        for sx, sy in [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1)]:
            q.append((sx, sy))
            visited[sy * w + sx] = 1

        while q:
            x, y = q.popleft()
            r, g, b, a = px[x, y]
            if is_bg(r, g, b):
                px[x, y] = (0, 0, 0, 0)
                for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    if 0 <= nx < w and 0 <= ny < h:
                        idx = ny * w + nx
                        if not visited[idx]:
                            visited[idx] = 1
                            q.append((nx, ny))

        # Tight crop to non-transparent pixels
        bbox = im.getbbox()
        if bbox:
            im = im.crop(bbox)

        # Fit cleanly inside 320x310 preserving aspect ratio (tightly cropped — no wasted side padding!)
        im.thumbnail((320, 310), Image.Resampling.LANCZOS)
        nw, nh = im.size
        im.save(out_path)
        print(f"Processed {out_path.name} ({nw}x{nh})")


if __name__ == "__main__":
    build_system_bg()
    build_gamelist_bg()
    build_selector_and_menu()
    build_portraits()
    process_raw_shops()
    print("All UI assets generated successfully!")
