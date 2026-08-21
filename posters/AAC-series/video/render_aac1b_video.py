#!/usr/bin/env python3
"""Render AAC.1.b animated explainer scenes with cartoon doctor character."""

from __future__ import annotations

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
OUT = ROOT / "scenes-1b"
OUT.mkdir(parents=True, exist_ok=True)

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


def paste_doctor(base: Image.Image, path: Path, xy, size=420):
    doc = Image.open(path).convert("RGBA")
    datas = doc.getdata()
    new = []
    for r, g, b, a in datas:
        if r > 245 and g > 245 and b > 245:
            new.append((r, g, b, 0))
        else:
            new.append((r, g, b, a))
    doc.putdata(new)
    doc = doc.resize((size, size), Image.Resampling.LANCZOS)
    base.paste(doc, xy, doc)
    return base


def footer(d, img):
    d.rounded_rectangle((48, H - 130, W - 48, H - 48), radius=16, fill=NAVY)
    f = font(FONT_BOLD, 22)
    d.text((70, H - 108), "AccredReady", fill=GOLD, font=f)
    d.text((70, H - 78), "Quality Today, Accreditation Tomorrow.", fill=(200, 220, 234), font=font(FONT_REG, 16))
    url = "www.accredready.in"
    uw = d.textlength(url, font=font(FONT_BOLD, 18))
    d.text((W - 70 - uw, H - 95), url, fill=(79, 195, 247), font=font(FONT_BOLD, 18))


def scene_intro():
    img, d = bg()
    d.text((60, 70), "NABH STANDARD", fill=NAVY, font=font(FONT_BOLD, 28))
    d.text((60, 110), "AAC 1b", fill=RED, font=font(FONT_BOLD, 92))
    d.text((60, 230), "One NABH standard", fill=MUTED, font=font(FONT_REG, 28))
    d.text((60, 268), "explained every day", fill=MUTED, font=font(FONT_REG, 28))
    paste_doctor(img, ASSETS / "doctor-wave.png", (520, 320), 480)
    d.rounded_rectangle((60, 520, 520, 700), radius=20, fill=NAVY)
    d.text((90, 555), "Hello! Let's learn", fill=WHITE, font=font(FONT_BOLD, 30))
    d.text((90, 605), "AAC.1.b together.", fill=GOLD, font=font(FONT_BOLD, 30))
    footer(d, img)
    img.save(OUT / "01-intro.png")


def scene_question():
    img, d = bg()
    d.text((60, 70), "NABH STANDARD", fill=NAVY, font=font(FONT_BOLD, 24))
    d.text((60, 105), "AAC 1b", fill=RED, font=font(FONT_BOLD, 72))
    y = 210
    for line in wrap(
        d,
        "Does Every Specialty Have Real Staff Cover — OP, IP, Daycare and Emergency?",
        font(FONT_BOLD, 34),
        W - 120,
    ):
        d.text((60, y), line, fill=NAVY, font=font(FONT_BOLD, 34))
        y += 46
    d.rounded_rectangle((60, y + 24, W - 60, y + 280), radius=18, fill=NAVY)
    oe = (
        "Each defined healthcare service should have diagnostic and treatment "
        "services with suitably qualified personnel who provide out-patient, "
        "in-patient, daycare and emergency cover."
    )
    ty = y + 50
    for line in wrap(d, oe, font(FONT_REG, 24), W - 140):
        d.text((90, ty), line, fill=WHITE, font=font(FONT_REG, 24))
        ty += 34
    paste_doctor(img, ASSETS / "doctor-point.png", (620, 820), 380)
    footer(d, img)
    img.save(OUT / "02-question.png")


def scene_bullets():
    img, d = bg()
    d.text((60, 60), "What AAC.1.b requires", fill=TEAL, font=font(FONT_BOLD, 28))
    bullets = [
        ("1", "Diagnostics + treatment", "Each defined clinical service has diagnostic and treatment support."),
        ("2", "Full pathway cover", "Qualified staff cover OP, IP, daycare and emergency — not OPD alone."),
        ("3", "Emergency consultants", "Named consultants provide emergency cover for their service."),
    ]
    y = 120
    colors = [TEAL, GREEN, (106, 27, 154)]
    for i, (num, title, body) in enumerate(bullets):
        d.rounded_rectangle((60, y, W - 60, y + 200), radius=18, fill=WHITE, outline=(215, 230, 242), width=2)
        d.ellipse((90, y + 60, 160, y + 130), fill=colors[i])
        d.text((112, y + 75), num, fill=WHITE, font=font(FONT_BOLD, 36))
        d.text((190, y + 45), title, fill=colors[i], font=font(FONT_BOLD, 28))
        ty = y + 100
        for line in wrap(d, body, font(FONT_REG, 24), W - 280):
            d.text((190, ty), line, fill=MUTED, font=font(FONT_REG, 24))
            ty += 32
        y += 230
    paste_doctor(img, ASSETS / "doctor-point.png", (780, 880), 260)
    footer(d, img)
    img.save(OUT / "03-bullets.png")


def scene_gaps():
    img, d = bg()
    d.text((60, 60), "COMMON GAPS HOSPITALS MISS", fill=TEAL, font=font(FONT_BOLD, 26))
    gaps = [
        ((21, 101, 192), "SPECIALTY ON PAPER ONLY", "Service named without qualified consultants and nursing cover."),
        ((46, 125, 50), "NO FULL CARE PATH", "OPD exists, but IP, daycare or emergency cover is missing."),
        ((106, 27, 154), "WEAK DIAGNOSTIC BACKING", "Diagnostics and treatment infrastructure do not match the service."),
        ((230, 81, 0), "EMERGENCY COVER MISSING", "Registration and casualty do not know who to call."),
    ]
    y = 120
    for color, title, body in gaps:
        d.rounded_rectangle((60, y, W - 60, y + 165), radius=16, fill=WHITE, outline=(215, 230, 242), width=2)
        d.rounded_rectangle((60, y, 78, y + 165), radius=8, fill=color)
        d.text((100, y + 35), title, fill=color, font=font(FONT_BOLD, 26))
        ty = y + 85
        for line in wrap(d, body, font(FONT_REG, 22), W - 160):
            d.text((100, ty), line, fill=MUTED, font=font(FONT_REG, 22))
            ty += 30
        y += 185
    footer(d, img)
    img.save(OUT / "04-gaps.png")


def scene_steps():
    img, d = bg()
    d.rounded_rectangle((60, 70, W - 60, 160), radius=16, fill=GREEN)
    d.text((90, 95), "SIMPLE FIRST STEP", fill=WHITE, font=font(FONT_BOLD, 34))
    steps = [
        "List every defined clinical service from your scope document.",
        "For each service, name OP, IP, daycare and emergency cover holders.",
        "Close gaps before assessment — staff first, then infrastructure.",
    ]
    y = 200
    for i, s in enumerate(steps, 1):
        d.rounded_rectangle((60, y, W - 60, y + 200), radius=18, fill=WHITE, outline=(165, 214, 167), width=3)
        d.ellipse((90, y + 65, 160, y + 135), fill=GREEN)
        d.text((112, y + 80), str(i), fill=WHITE, font=font(FONT_BOLD, 36))
        ty = y + 55
        for line in wrap(d, s, font(FONT_BOLD, 26), W - 280):
            d.text((190, ty), line, fill=(27, 94, 32), font=font(FONT_BOLD, 26))
            ty += 36
        y += 230
    paste_doctor(img, ASSETS / "doctor-checklist.png", (700, 880), 320)
    footer(d, img)
    img.save(OUT / "05-steps.png")


def scene_outro():
    img, d = bg()
    paste_doctor(img, ASSETS / "doctor-wave.png", (300, 180), 480)
    d.text((W // 2, 700), "AccredReady", fill=NAVY, font=font(FONT_BOLD, 56), anchor="mm")
    d.text((W // 2, 780), "Quality Today, Accreditation Tomorrow.", fill=MUTED, font=font(FONT_REG, 26), anchor="mm")
    d.rounded_rectangle((220, 840, 860, 950), radius=20, fill=TEAL)
    d.text((W // 2, 895), "www.accredready.in", fill=WHITE, font=font(FONT_BOLD, 34), anchor="mm")
    d.text((W // 2, 1020), "#NABH  #NABH6thEdition  #HealthcareQuality", fill=MUTED, font=font(FONT_REG, 20), anchor="mm")
    footer(d, img)
    img.save(OUT / "06-outro.png")


def main():
    scene_intro()
    scene_question()
    scene_bullets()
    scene_gaps()
    scene_steps()
    scene_outro()
    print("scenes ready in", OUT)


if __name__ == "__main__":
    main()
