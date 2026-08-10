#!/usr/bin/env python3
"""Build AAC.1.a video from the static LinkedIn poster + VO/BGM mix (no character animation)."""

from __future__ import annotations

import subprocess
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
POSTER = ROOT.parent / "AAC-1a.png"
AUDIO = ROOT / "assets" / "audio-mix.m4a"
STILL = Path("/tmp/aac1a-still.png")
OUT = ROOT / "AAC-1a-animated.mp4"
TARGET = (1080, 1350)


def fit_cover(src: Path, dst: Path, size=(1080, 1350)) -> None:
    im = Image.open(src).convert("RGB")
    tw, th = size
    w, h = im.size
    scale = max(tw / w, th / h)
    nw, nh = int(w * scale), int(h * scale)
    im = im.resize((nw, nh), Image.Resampling.LANCZOS)
    left = (nw - tw) // 2
    top = (nh - th) // 2
    im.crop((left, top, left + tw, top + th)).save(dst, quality=95)


def main() -> None:
    fit_cover(POSTER, STILL, TARGET)
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-loop",
            "1",
            "-i",
            str(STILL),
            "-i",
            str(AUDIO),
            "-c:v",
            "libx264",
            "-tune",
            "stillimage",
            "-pix_fmt",
            "yuv420p",
            "-preset",
            "medium",
            "-crf",
            "18",
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            "-shortest",
            "-movflags",
            "+faststart",
            str(OUT),
        ],
        check=True,
    )
    print("wrote", OUT)


if __name__ == "__main__":
    main()
