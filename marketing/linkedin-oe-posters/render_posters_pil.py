#!/usr/bin/env python3
"""Render all AAC LinkedIn OE posters with Pillow (no Chrome dependency)."""

from __future__ import annotations

import json
import textwrap
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
OES_PATH = ROOT / "aac_oes.json"
W, H = 1080, 1350

FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"

LEVEL_COLORS = {
    "Core": ("#c62828", "#ffebee"),
    "Commitment": ("#1565c0", "#e3f2fd"),
    "Achievement": ("#2e7d32", "#e8f5e9"),
    "Excellence": ("#6a1b9a", "#f3e5f5"),
}
MISTAKE_COLORS = ["#1565c0", "#2e7d32", "#6a1b9a", "#e65100"]


def hex_to_rgb(h: str):
    h = h.lstrip("#")
    return tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines or [""]


def rounded(draw, xy, fill, radius=16):
    draw.rounded_rectangle(xy, radius=radius, fill=fill)


def render(oe: dict, out: Path) -> None:
    img = Image.new("RGB", (W, H), "#f5f8fb")
    d = ImageDraw.Draw(img)

    # soft background washes
    for box, color in [
        ((700, -80, 1200, 420), "#d9ecf8"),
        ((-120, 380, 420, 820), "#e7f5ea"),
    ]:
        overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        od = ImageDraw.Draw(overlay)
        od.ellipse(box, fill=(*hex_to_rgb(color), 110))
        img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
        d = ImageDraw.Draw(img)

    # outer frame
    d.rounded_rectangle((18, 18, W - 18, H - 18), radius=22, outline="#c5d6e6", width=2)

    accent, tint = LEVEL_COLORS[oe["level"]]
    accent_rgb = hex_to_rgb(accent)
    tint_rgb = hex_to_rgb(tint)

    f_label = font(FONT_BOLD, 20)
    f_code = font(FONT_BOLD, 58)
    f_head = font(FONT_SERIF, 30)
    f_body = font(FONT_REG, 20)
    f_small = font(FONT_REG, 18)
    f_tiny = font(FONT_BOLD, 16)
    f_midb = font(FONT_BOLD, 22)
    f_mid = font(FONT_REG, 19)
    f_foot = font(FONT_BOLD, 22)

    y = 48
    d.text((48, y), "NABH STANDARD", fill="#0d1f33", font=f_label)
    # level pill
    pill = oe["level"].upper()
    pw = d.textlength(pill, font=f_tiny) + 28
    rounded(d, (W - 48 - pw, y - 2, W - 48, y + 28), tint_rgb, 20)
    d.text((W - 48 - pw + 14, y + 4), pill, fill=accent_rgb, font=f_tiny)

    y += 28
    d.text((48, y), oe["display"], fill=accent_rgb, font=f_code)
    y += 70

    # headline
    for line in wrap(d, oe["headline"], f_head, W - 100):
        d.text((48, y), line, fill="#0a1828", font=f_head)
        y += 36
    y += 8

    # standard line
    std = f"AAC.{oe['std']} — {oe['standard']}"
    for line in wrap(d, std, f_small, W - 100):
        d.text((48, y), line, fill="#3a5870", font=f_small)
        y += 24
    y += 12

    # OE box
    oe_lines = wrap(d, oe["text"], f_body, W - 140)
    box_h = 28 + 26 + len(oe_lines) * 28 + 18
    rounded(d, (44, y, W - 44, y + box_h), "#0d1f33", 16)
    d.text((64, y + 16), f"OBJECTIVE ELEMENT {oe['code']}", fill="#4fc3f7", font=f_tiny)
    ty = y + 42
    for line in oe_lines:
        d.text((64, ty), line, fill="#eef4f9", font=f_body)
        ty += 28
    y += box_h + 16

    # bullets
    for b in oe["bullets"]:
        d.ellipse((52, y + 8, 62, y + 18), fill="#c62828")
        for i, line in enumerate(wrap(d, b, f_small, W - 130)):
            d.text((72, y), line, fill="#1e3a52", font=f_small)
            y += 24
        y += 4
    y += 6

    d.text((48, y), "COMMON GAPS HOSPITALS MISS", fill="#1565c0", font=f_tiny)
    y += 28

    for i, m in enumerate(oe["mistakes"]):
        color = hex_to_rgb(MISTAKE_COLORS[i % 4])
        block_h = 78
        rounded(d, (44, y, W - 44, y + block_h), "#ffffff", 14)
        d.rounded_rectangle((44, y, W - 44, y + block_h), radius=14, outline="#d7e6f2", width=1)
        rounded(d, (56, y + 20, 90, y + 54), color, 10)
        d.text((67, y + 28), str(i + 1), fill="white", font=f_midb)
        d.text((104, y + 14), m["title"], fill=color, font=f_midb)
        detail_lines = wrap(d, m["detail"], f_mid, W - 170)
        dy = y + 42
        for line in detail_lines[:2]:
            d.text((104, dy), line, fill="#334e68", font=f_mid)
            dy += 22
        y += block_h + 10

    # first step
    y += 4
    rounded(d, (44, y, W - 44, y + 168), "#e8f5e9", 14)
    d.rounded_rectangle((44, y, W - 44, y + 168), radius=14, outline="#a5d6a7", width=2)
    d.text((64, y + 14), "SIMPLE FIRST STEP", fill="#2e7d32", font=f_tiny)
    step_w = (W - 120) // 3
    for i, s in enumerate(oe["steps"]):
        sx = 56 + i * (step_w + 12)
        rounded(d, (sx, y + 42, sx + step_w, y + 150), "#ffffff", 10)
        d.ellipse((sx + 10, y + 52, sx + 34, y + 76), fill="#2e7d32")
        d.text((sx + 17, y + 55), str(i + 1), fill="white", font=f_tiny)
        ty = y + 84
        for line in wrap(d, s, font(FONT_BOLD, 15), step_w - 20)[:4]:
            d.text((sx + 10, ty), line, fill="#1b5e20", font=font(FONT_BOLD, 15))
            ty += 18

    # footer
    fy = H - 118
    rounded(d, (44, fy, W - 44, fy + 70), "#0d1f33", 14)
    d.text((64, fy + 14), "One NABH standard", fill="#9fb6c9", font=f_small)
    d.text((64, fy + 38), "explained every day", fill="#9fb6c9", font=f_small)
    logo = "AccredReady"
    lw = d.textlength(logo, font=f_foot)
    d.text(((W - lw) / 2, fy + 12), logo, fill="#f0d070", font=f_foot)
    tag = "Quality Today, Accreditation Tomorrow."
    tw = d.textlength(tag, font=f_tiny)
    d.text(((W - tw) / 2, fy + 40), tag, fill="#c8dcea", font=f_tiny)
    right = "www.accredready.in"
    rw = d.textlength(right, font=f_small)
    d.text((W - 64 - rw, fy + 14), right, fill="#4fc3f7", font=f_small)
    ed = "HCO 6th Edition"
    ew = d.textlength(ed, font=f_tiny)
    d.text((W - 64 - ew, fy + 40), ed, fill="#9fb6c9", font=f_tiny)

    tags = "#NABH  #HealthcareQuality  #HospitalAccreditation  #NABH6thEdition"
    tw = d.textlength(tags, font=font(FONT_REG, 14))
    d.text(((W - tw) / 2, H - 38), tags, fill="#5b7a94", font=font(FONT_REG, 14))

    img.save(out, "PNG", optimize=True)


def main():
    oes = json.loads(OES_PATH.read_text(encoding="utf-8"))
    for i, oe in enumerate(oes, 1):
        # filename: nabh-aac-1a-linkedin-poster.png (match existing 1a/1b style)
        stem = oe["code"].lower().replace("aac.", "aac-").replace(".", "")
        # AAC.10.a -> aac-10a
        parts = oe["code"].split(".")
        stem = f"aac-{parts[1]}{parts[2]}".lower()
        out = ROOT / f"nabh-{stem}-linkedin-poster.png"
        render(oe, out)
        print(f"[{i}/{len(oes)}] {out.name}", flush=True)
    print("DONE", len(oes))


if __name__ == "__main__":
    main()
