#!/usr/bin/env python3
"""AAC.1.a explainer with walking doctor + amplitude lip-sync."""

from __future__ import annotations

import math
import wave
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
FRAMES = Path("/tmp/aac1a_lip_frames")
FRAMES.mkdir(parents=True, exist_ok=True)

W, H = 1080, 1350
FPS = 24  # slightly lower for render speed
DUR = 40.0  # matches VO roughly
N = int(DUR * FPS)

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


def font(path, size):
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


def knock_white(im: Image.Image) -> Image.Image:
    im = im.convert("RGBA")
    px = im.load()
    w, h = im.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if r > 242 and g > 242 and b > 242:
                px[x, y] = (r, g, b, 0)
    return im


def load_doc(name, size):
    im = knock_white(Image.open(ASSETS / name))
    return im.resize((size, size), Image.Resampling.LANCZOS)


def load_rms(wav_path: str, n_frames: int, fps: int) -> np.ndarray:
    with wave.open(wav_path, "rb") as wf:
        sr = wf.getframerate()
        n = wf.getnframes()
        data = np.frombuffer(wf.readframes(n), dtype=np.int16).astype(np.float32)
    # frame windows
    samples_per = max(1, int(sr / fps))
    rms = []
    for i in range(n_frames):
        a = i * samples_per
        b = min(len(data), a + samples_per)
        chunk = data[a:b]
        if len(chunk) == 0:
            rms.append(0.0)
        else:
            rms.append(float(np.sqrt(np.mean(chunk * chunk))))
    rms = np.array(rms)
    if rms.max() > 0:
        rms = rms / rms.max()
    # smooth
    k = 3
    pad = np.pad(rms, (k, k), mode="edge")
    rms = np.convolve(pad, np.ones(2 * k + 1) / (2 * k + 1), mode="valid")
    return rms[:n_frames]


def base_bg():
    img = Image.new("RGB", (W, H), LIGHT)
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.ellipse((650, -120, 1200, 420), fill=(217, 236, 248, 140))
    od.ellipse((-150, 900, 450, 1450), fill=(232, 245, 233, 120))
    img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((24, 24, W - 24, H - 24), radius=28, outline=(197, 214, 230), width=3)
    return img, d


def draw_footer(d):
    d.rounded_rectangle((48, H - 120, W - 48, H - 44), radius=16, fill=NAVY)
    d.text((70, H - 100), "AccredReady", fill=GOLD, font=font(FONT_BOLD, 22))
    d.text((70, H - 72), "Quality Today, Accreditation Tomorrow.", fill=(200, 220, 234), font=font(FONT_REG, 15))
    url = "www.accredready.in"
    uw = d.textlength(url, font=font(FONT_BOLD, 18))
    d.text((W - 70 - uw, H - 88), url, fill=(79, 195, 247), font=font(FONT_BOLD, 18))


def draw_speech_bubble(d, text, tip_x, tip_y, max_w=420):
    """Rounded bubble pointing roughly toward tip_x, tip_y (doctor mouth)."""
    fnt = font(FONT_BOLD, 22)
    lines = wrap(d, text, fnt, max_w - 40)
    line_h = 30
    bh = 28 + len(lines) * line_h
    bw = max(int(d.textlength(line, font=fnt)) for line in lines) + 48
    bw = max(bw, 200)
    bx = max(40, min(tip_x - bw // 2, W - bw - 40))
    by = max(40, tip_y - bh - 36)
    d.rounded_rectangle((bx, by, bx + bw, by + bh), radius=18, fill=WHITE, outline=NAVY, width=3)
    # tail
    d.polygon(
        [(tip_x - 14, by + bh - 2), (tip_x + 14, by + bh - 2), (tip_x, by + bh + 22)],
        fill=WHITE,
        outline=NAVY,
    )
    # redraw fill over outline seam
    d.polygon(
        [(tip_x - 12, by + bh - 4), (tip_x + 12, by + bh - 4), (tip_x, by + bh + 18)],
        fill=WHITE,
    )
    ty = by + 14
    for line in lines:
        d.text((bx + 24, ty), line, fill=NAVY, font=fnt)
        ty += line_h


def scene_content(t: float, d, img):
    """Draw text content based on time (seconds)."""
    if t < 5.5:
        d.text((60, 70), "NABH STANDARD", fill=NAVY, font=font(FONT_BOLD, 28))
        d.text((60, 110), "AAC 1a", fill=RED, font=font(FONT_BOLD, 90))
        d.text((60, 230), "One NABH standard", fill=MUTED, font=font(FONT_REG, 28))
        d.text((60, 270), "explained every day", fill=MUTED, font=font(FONT_REG, 28))
        d.rounded_rectangle((60, 360, 560, 520), radius=18, fill=NAVY)
        d.text((90, 400), "Look — here comes", fill=WHITE, font=font(FONT_BOLD, 28))
        d.text((90, 445), "our quality doctor!", fill=GOLD, font=font(FONT_BOLD, 28))
    elif t < 12.5:
        d.text((60, 70), "NABH STANDARD", fill=NAVY, font=font(FONT_BOLD, 24))
        d.text((60, 105), "AAC 1a", fill=RED, font=font(FONT_BOLD, 70))
        y = 200
        for line in wrap(d, "Are Your Services Defined by Community Need?", font(FONT_BOLD, 34), W - 140):
            d.text((60, y), line, fill=NAVY, font=font(FONT_BOLD, 34))
            y += 46
        d.rounded_rectangle((60, y + 20, W - 60, y + 210), radius=18, fill=NAVY)
        oe = "Healthcare services being provided are defined and are in consonance with the needs of the community."
        ty = y + 50
        for line in wrap(d, oe, font(FONT_REG, 24), W - 140):
            d.text((90, ty), line, fill=WHITE, font=font(FONT_REG, 24))
            ty += 34
    elif t < 22:
        d.text((60, 60), "What AAC.1.a requires", fill=TEAL, font=font(FONT_BOLD, 28))
        bullets = [
            (TEAL, "1", "Services are formally defined"),
            (GREEN, "2", "Aligned to community needs"),
            ((106, 27, 154), "3", "Needs guide new planning"),
        ]
        y = 130
        for color, num, title in bullets:
            d.rounded_rectangle((60, y, 700, y + 140), radius=16, fill=WHITE, outline=(215, 230, 242), width=2)
            d.ellipse((90, y + 35, 155, y + 100), fill=color)
            d.text((112, y + 50), num, fill=WHITE, font=font(FONT_BOLD, 32))
            d.text((180, y + 55), title, fill=color, font=font(FONT_BOLD, 26))
            y += 165
    elif t < 30:
        d.text((60, 60), "COMMON GAPS", fill=TEAL, font=font(FONT_BOLD, 28))
        gaps = [
            ((21, 101, 192), "NO WRITTEN LIST"),
            ((46, 125, 50), "NO COMMUNITY INPUT"),
            ((106, 27, 154), "GUESSWORK PLANNING"),
            ((230, 81, 0), "STAFF DON'T KNOW"),
        ]
        y = 120
        for color, title in gaps:
            d.rounded_rectangle((60, y, 700, y + 115), radius=14, fill=WHITE, outline=(215, 230, 242), width=2)
            d.rounded_rectangle((60, y, 78, y + 115), radius=6, fill=color)
            d.text((100, y + 40), title, fill=color, font=font(FONT_BOLD, 26))
            y += 135
    elif t < 36:
        d.rounded_rectangle((60, 70, W - 60, 150), radius=16, fill=GREEN)
        d.text((90, 92), "SIMPLE FIRST STEP", fill=WHITE, font=font(FONT_BOLD, 32))
        steps = [
            "Write an approved service list",
            "Attach community feedback",
            "Brief your teams this week",
        ]
        y = 190
        for i, s in enumerate(steps, 1):
            d.rounded_rectangle((60, y, 700, y + 130), radius=16, fill=WHITE, outline=(165, 214, 167), width=3)
            d.ellipse((90, y + 30, 155, y + 95), fill=GREEN)
            d.text((112, y + 45), str(i), fill=WHITE, font=font(FONT_BOLD, 32))
            d.text((180, y + 50), s, fill=(27, 94, 32), font=font(FONT_BOLD, 24))
            y += 150
    else:
        d.text((W // 2, 180), "AccredReady", fill=NAVY, font=font(FONT_BOLD, 56), anchor="mm")
        d.text((W // 2, 260), "Quality Today, Accreditation Tomorrow.", fill=MUTED, font=font(FONT_REG, 24), anchor="mm")
        d.rounded_rectangle((240, 320, 840, 420), radius=20, fill=TEAL)
        d.text((W // 2, 370), "www.accredready.in", fill=WHITE, font=font(FONT_BOLD, 32), anchor="mm")


def main():
    print("Loading sprites…")
    walk_a = load_doc("doctor-walk-a.png", 460)
    walk_b = load_doc("doctor-walk-b.png", 460)
    talk_c = load_doc("doctor-talk-closed.png", 480)
    talk_o = load_doc("doctor-talk-open.png", 480)

    print("Analyzing audio for lip-sync…")
    rms = load_rms("/tmp/vo.wav", N, FPS)
    # mouth open threshold
    thr = max(0.12, float(np.percentile(rms, 45)))

    print(f"Rendering {N} frames @ {FPS}fps…")
    for i in range(N):
        t = i / FPS
        img, d = base_bg()
        scene_content(t, d, img)
        draw_footer(d)
        frame = img.convert("RGBA")

        draw = ImageDraw.Draw(frame)

        if t < 5.5:
            # Walking in from left → settle
            progress = min(1.0, t / 4.5)
            ease = 1 - (1 - progress) ** 2
            x = int(-220 + ease * 740)  # ends near x=520
            y = 720
            bob = int(abs(math.sin(t * math.pi * 6)) * 10)
            sprite = walk_a if (i // 4) % 2 == 0 else walk_b
            frame.paste(sprite, (x, y + bob), sprite)
            if t > 1.0:
                bubble = "Coming to explain AAC.1.a!" if t < 3.2 else "Let's make services match need!"
                draw_speech_bubble(draw, bubble, x + 230, y + bob + 80)
        else:
            # Talking doctor on right with lip-sync
            x, y = 600, 690
            bob = int(4 * math.sin(t * 3))
            open_mouth = bool(rms[i] > thr)
            # hold mouth open briefly for readability
            if i > 0 and rms[i - 1] > thr:
                open_mouth = open_mouth or rms[i] > thr * 0.65
            sprite = talk_o if open_mouth else talk_c
            if open_mouth:
                s = 500
                sp = sprite.resize((s, s), Image.Resampling.LANCZOS)
                frame.paste(sp, (x - 10, y + bob - 10), sp)
            else:
                frame.paste(sprite, (x, y + bob), sprite)

            bubble = None
            if 5.5 <= t < 12.5:
                bubble = "Services must match community need!"
            elif 12.5 <= t < 22:
                bubble = "Three must-do checks!"
            elif 22 <= t < 30:
                bubble = "Watch these common gaps…"
            elif 30 <= t < 36:
                bubble = "Start with one service list!"
            elif 36 <= t < 39:
                bubble = "You've got this — let's go!"
            if bubble:
                draw_speech_bubble(draw, bubble, x + 160, y + bob + 90)

        frame.convert("RGB").save(FRAMES / f"f{i:05d}.png")
        if i % 48 == 0:
            print(f"  {i}/{N} ({100*i/N:.0f}%)")

    print("DONE frames", N)


if __name__ == "__main__":
    main()
