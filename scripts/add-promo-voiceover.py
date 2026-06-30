#!/usr/bin/env python3
"""Generate Edge TTS voiceover synced to SRT and mux into promo MP4."""

from __future__ import annotations

import asyncio
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

import edge_tts

ROOT = Path(__file__).resolve().parent.parent
SRT = ROOT / "marketing/video/accredready-promo.srt"
OUT_DIR = ROOT / "marketing/video/output"
VOICE = "en-IN-NeerjaNeural"
VIDEO_DURATION = 37.0


@dataclass
class Cue:
    index: int
    start: float
    end: float
    text: str


def parse_srt(path: Path) -> list[Cue]:
    raw = path.read_text(encoding="utf-8").strip()
    blocks = re.split(r"\n\s*\n", raw)
    cues: list[Cue] = []
    for block in blocks:
        lines = block.strip().splitlines()
        if len(lines) < 3:
            continue
        idx = int(lines[0])
        start_s, end_s = [p.strip() for p in lines[1].split("-->")]
        text = " ".join(line.strip() for line in lines[2:])
        cues.append(Cue(idx, srt_time(start_s), srt_time(end_s), text))
    return cues


def srt_time(value: str) -> float:
    h, m, rest = value.split(":")
    s, ms = rest.split(",")
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000.0


async def synthesize(text: str, out_path: Path) -> None:
    communicate = edge_tts.Communicate(text, VOICE, rate="-5%")
    await communicate.save(str(out_path))


def run(cmd: list[str]) -> None:
    print("+", " ".join(cmd))
    subprocess.run(cmd, check=True)


def fit_segment(src: Path, dst: Path, max_duration: float) -> None:
    probe = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(src),
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    duration = float(probe.stdout.strip())
    if duration <= max_duration or max_duration <= 0:
        shutil.copy(src, dst)
        return
    speed = min(duration / max_duration, 1.35)
    run(
        [
            "ffmpeg",
            "-y",
            "-i",
            str(src),
            "-filter:a",
            f"atempo={speed:.4f}",
            str(dst),
        ]
    )


def build_audio(cues: list[Cue], work: Path) -> Path:
    fitted: list[Path] = []
    for cue in cues:
        raw = work / f"seg-{cue.index:02d}-raw.mp3"
        fit = work / f"seg-{cue.index:02d}.mp3"
        asyncio.run(synthesize(cue.text, raw))
        slot = max(cue.end - cue.start, 0.5)
        fit_segment(raw, fit, slot)
        fitted.append(fit)

    inputs: list[str] = [
        "-f",
        "lavfi",
        "-i",
        f"anullsrc=r=44100:cl=mono,atrim=0:{VIDEO_DURATION}",
    ]
    filter_parts: list[str] = []
    mix_inputs: list[str] = ["[0:a]"]

    for i, (cue, seg) in enumerate(zip(cues, fitted), start=1):
        inputs.extend(["-i", str(seg)])
        delay_ms = int(cue.start * 1000)
        label = f"a{i}"
        filter_parts.append(f"[{i}:a]adelay={delay_ms}|{delay_ms}[{label}]")
        mix_inputs.append(f"[{label}]")

    mixed = work / "voiceover.m4a"
    n = len(cues) + 1
    filter_complex = (
        ";".join(filter_parts)
        + ";"
        + "".join(mix_inputs)
        + f"amix=inputs={n}:duration=first:dropout_transition=0,volume=1.2[aout]"
    )
    run(
        [
            "ffmpeg",
            "-y",
            *inputs,
            "-filter_complex",
            filter_complex,
            "-map",
            "[aout]",
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            str(mixed),
        ]
    )
    return mixed


def mux_video(video_in: Path, audio: Path, video_out: Path) -> None:
    run(
        [
            "ffmpeg",
            "-y",
            "-i",
            str(video_in),
            "-i",
            str(audio),
            "-map",
            "0:v:0",
            "-map",
            "1:a:0",
            "-c:v",
            "copy",
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            "-shortest",
            "-movflags",
            "+faststart",
            str(video_out),
        ]
    )


def main() -> int:
    if shutil.which("ffmpeg") is None:
        print("ffmpeg is required", file=sys.stderr)
        return 1
    if not SRT.exists():
        print(f"Missing SRT: {SRT}", file=sys.stderr)
        return 1

    cues = parse_srt(SRT)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="promo-voice-") as tmp:
        work = Path(tmp)
        audio = build_audio(cues, work)

        pairs = [
            (
                OUT_DIR / "accredready-promo-1080p.mp4",
                OUT_DIR / "accredready-promo-1080p-voiced.mp4",
            ),
            (
                OUT_DIR / "accredready-promo-vertical.mp4",
                OUT_DIR / "accredready-promo-vertical-voiced.mp4",
            ),
        ]
        for src, dst in pairs:
            if not src.exists():
                print(f"Skip missing video: {src}")
                continue
            mux_video(src, audio, dst)
            print(f"✓ {dst}")

        public = ROOT / "public"
        public.mkdir(exist_ok=True)
        for _, dst in pairs:
            if dst.exists():
                shutil.copy(dst, public / dst.name.replace("-voiced", "-with-voice"))

    print("\nDone.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
