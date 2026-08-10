#!/usr/bin/env python3
"""Render 6 scene stills for one AAC OE explainer (doctor style)."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"

W, H = 1080, 1350
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
NAVY = (13, 31, 51)
RED = (198, 40, 40)
WHITE = (255, 255, 255)
TEAL = (21, 101, 192)
GREEN = (46, 125, 50)
GOLD = (240, 208, 112)
LIGHT = (245, 248, 251)
MUTED = (58, 88, 112)
PURPLE = (106, 27, 154)
ORANGE = (230, 81, 0)


def font(path: str, size: int):
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


def bg():
    img = Image.new("RGB", (W, H), LIGHT)
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.ellipse((650, -120, 1200, 420), fill=(217, 236, 248, 140))
    od.ellipse((-150, 900, 450, 1450), fill=(232, 245, 233, 120))
    img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((24, 24, W - 24, H - 24), radius=28, outline=(197, 214, 230), width=3)
    return img, d


def paste_doctor(base: Image.Image, name: str, xy, size=420):
    doc = Image.open(ASSETS / name).convert("RGBA")
    # fast near-white key
    arr = doc.getdata()
    doc.putdata(
        [(r, g, b, 0) if r > 245 and g > 245 and b > 245 else (r, g, b, a) for r, g, b, a in arr]
    )
    doc = doc.resize((size, size), Image.Resampling.LANCZOS)
    base.paste(doc, xy, doc)
    return base


def footer(d):
    d.rounded_rectangle((48, H - 130, W - 48, H - 48), radius=16, fill=NAVY)
    d.text((70, H - 108), "AccredReady", fill=GOLD, font=font(FONT_BOLD, 22))
    d.text((70, H - 78), "Quality Today, Accreditation Tomorrow.", fill=(200, 220, 234), font=font(FONT_REG, 16))
    url = "www.accredready.in"
    uw = d.textlength(url, font=font(FONT_BOLD, 18))
    d.text((W - 70 - uw, H - 95), url, fill=(79, 195, 247), font=font(FONT_BOLD, 18))


def render_oe(item: dict, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    short = item["short"]  # AAC 1b
    code = item["code"]  # AAC.1.b
    display = short.replace("AAC ", "AAC ")

    # 01 intro
    img, d = bg()
    d.text((60, 70), "NABH STANDARD", fill=NAVY, font=font(FONT_BOLD, 28))
    # Fit large code
    size = 92 if len(display) <= 6 else 72
    d.text((60, 110), display, fill=RED, font=font(FONT_BOLD, size))
    d.text((60, 230), "One NABH standard", fill=MUTED, font=font(FONT_REG, 28))
    d.text((60, 268), "explained every day", fill=MUTED, font=font(FONT_REG, 28))
    paste_doctor(img, "doctor-wave.png", (520, 320), 480)
    d.rounded_rectangle((60, 520, 520, 700), radius=20, fill=NAVY)
    d.text((90, 555), "Hello! Let's learn", fill=WHITE, font=font(FONT_BOLD, 30))
    d.text((90, 605), f"{code} together.", fill=GOLD, font=font(FONT_BOLD, 28))
    footer(d)
    img.save(out_dir / "01-intro.png")

    # 02 question
    img, d = bg()
    d.text((60, 70), "NABH STANDARD", fill=NAVY, font=font(FONT_BOLD, 24))
    d.text((60, 105), display, fill=RED, font=font(FONT_BOLD, 64 if len(display) > 6 else 72))
    y = 200
    for line in wrap(d, item["headline"], font(FONT_BOLD, 32), W - 120):
        d.text((60, y), line, fill=NAVY, font=font(FONT_BOLD, 32))
        y += 42
        if y > 420:
            break
    box_top = min(y + 20, 460)
    d.rounded_rectangle((60, box_top, W - 60, box_top + 260), radius=18, fill=NAVY)
    ty = box_top + 40
    for line in wrap(d, item["oe_text"], font(FONT_REG, 24), W - 140):
        d.text((90, ty), line, fill=WHITE, font=font(FONT_REG, 24))
        ty += 34
        if ty > box_top + 220:
            break
    paste_doctor(img, "doctor-point.png", (620, 820), 360)
    footer(d)
    img.save(out_dir / "02-question.png")

    # 03 bullets
    img, d = bg()
    d.text((60, 60), f"What {code} requires", fill=TEAL, font=font(FONT_BOLD, 28))
    colors = [TEAL, GREEN, PURPLE]
    y = 120
    for i, req in enumerate(item["requirements"][:3]):
        d.rounded_rectangle((60, y, W - 60, y + 200), radius=18, fill=WHITE, outline=(215, 230, 242), width=2)
        d.ellipse((90, y + 60, 160, y + 130), fill=colors[i])
        d.text((112, y + 75), str(i + 1), fill=WHITE, font=font(FONT_BOLD, 36))
        title = req.get("title") or f"Point {i+1}"
        # derive short title from body
        body = req["body"]
        short_title = title if not title.startswith("Requirement") else (body.split(",")[0][:42])
        d.text((190, y + 45), short_title[:46], fill=colors[i], font=font(FONT_BOLD, 26))
        ty = y + 100
        for line in wrap(d, body, font(FONT_REG, 22), W - 280):
            d.text((190, ty), line, fill=MUTED, font=font(FONT_REG, 22))
            ty += 30
            if ty > y + 175:
                break
        y += 230
    paste_doctor(img, "doctor-point.png", (780, 880), 250)
    footer(d)
    img.save(out_dir / "03-bullets.png")

    # 04 gaps
    img, d = bg()
    d.text((60, 60), "COMMON GAPS HOSPITALS MISS", fill=TEAL, font=font(FONT_BOLD, 26))
    gap_colors = [TEAL, GREEN, PURPLE, ORANGE]
    y = 120
    for i, gap in enumerate(item["gaps"][:4]):
        color = gap_colors[i]
        d.rounded_rectangle((60, y, W - 60, y + 165), radius=16, fill=WHITE, outline=(215, 230, 242), width=2)
        d.rounded_rectangle((60, y, 78, y + 165), radius=8, fill=color)
        d.text((100, y + 35), gap["title"][:36].upper(), fill=color, font=font(FONT_BOLD, 24))
        ty = y + 85
        for line in wrap(d, gap.get("body") or "", font(FONT_REG, 22), W - 160):
            d.text((100, ty), line, fill=MUTED, font=font(FONT_REG, 22))
            ty += 30
        y += 185
    footer(d)
    img.save(out_dir / "04-gaps.png")

    # 05 steps
    img, d = bg()
    d.rounded_rectangle((60, 70, W - 60, 160), radius=16, fill=GREEN)
    d.text((90, 95), "SIMPLE FIRST STEP", fill=WHITE, font=font(FONT_BOLD, 34))
    y = 200
    for i, step in enumerate(item["steps"][:3], 1):
        d.rounded_rectangle((60, y, W - 60, y + 200), radius=18, fill=WHITE, outline=(165, 214, 167), width=3)
        d.ellipse((90, y + 65, 160, y + 135), fill=GREEN)
        d.text((112, y + 80), str(i), fill=WHITE, font=font(FONT_BOLD, 36))
        ty = y + 55
        for line in wrap(d, step, font(FONT_BOLD, 24), W - 280):
            d.text((190, ty), line, fill=(27, 94, 32), font=font(FONT_BOLD, 24))
            ty += 34
            if ty > y + 170:
                break
        y += 230
    paste_doctor(img, "doctor-checklist.png", (700, 880), 300)
    footer(d)
    img.save(out_dir / "05-steps.png")

    # 06 outro
    img, d = bg()
    paste_doctor(img, "doctor-wave.png", (300, 180), 480)
    d.text((W // 2, 700), "AccredReady", fill=NAVY, font=font(FONT_BOLD, 56), anchor="mm")
    d.text((W // 2, 780), "Quality Today, Accreditation Tomorrow.", fill=MUTED, font=font(FONT_REG, 26), anchor="mm")
    d.rounded_rectangle((220, 840, 860, 950), radius=20, fill=TEAL)
    d.text((W // 2, 895), "www.accredready.in", fill=WHITE, font=font(FONT_BOLD, 34), anchor="mm")
    d.text((W // 2, 1020), "#NABH  #NABH6thEdition  #HealthcareQuality", fill=MUTED, font=font(FONT_REG, 20), anchor="mm")
    footer(d)
    img.save(out_dir / "06-outro.png")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--code", required=True, help="e.g. AAC.1.c")
    ap.add_argument("--catalog", default=str(ROOT / "oes_content.json"))
    args = ap.parse_args()
    catalog = {x["code"]: x for x in json.loads(Path(args.catalog).read_text())}
    item = catalog[args.code]
    out = ROOT / "scenes" / item["file_stem"]
    render_oe(item, out)
    print("scenes", out)


if __name__ == "__main__":
    main()
