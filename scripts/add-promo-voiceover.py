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
PUBLIC = ROOT / "public"
VOICE = "en-IN-NeerjaNeural"
VIDEO_DURATION = 37.0
GAP_BETWEEN_CUES = 0.12  # seconds — prevents back-to-back overlap


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


def max_segment_duration(cues: list[Cue], index: int) -> float:
    cue = cues[index]
    if index + 1 < len(cues):
        return max(cues[index + 1].start - cue.start - GAP_BETWEEN_CUES, 0.4)
    return max(VIDEO_DURATION - cue.start - 0.2, 0.4)


async def synthesize_all(cues: list[Cue], work: Path) -> None:
    async def one(cue: Cue) -> None:
        out = work / f"seg-{cue.index:02d}-raw.mp3"
        communicate = edge_tts.Communicate(cue.text, VOICE, rate="-5%")
        await communicate.save(str(out))

    await asyncio.gather(*(one(c) for c in cues))


def run(cmd: list[str]) -> None:
    print("+", " ".join(cmd))
    subprocess.run(cmd, check=True)


def probe_duration(path: Path) -> float:
    probe = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(path),
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    return float(probe.stdout.strip())


def atempo_chain(speed: float) -> str:
    """Build ffmpeg atempo chain (each factor must stay within 0.5–2.0)."""
    filters: list[str] = []
    remaining = speed
    while remaining > 1.01:
        step = min(remaining, 2.0)
        filters.append(f"atempo={step:.4f}")
        remaining /= step
    while remaining < 0.99:
        step = max(remaining, 0.5)
        filters.append(f"atempo={step:.4f}")
        remaining /= step
    return ",".join(filters) if filters else "anull"


def fit_segment(src: Path, dst: Path, max_duration: float) -> None:
    duration = probe_duration(src)
    filters: list[str] = []
    if duration > max_duration:
        filters.append(atempo_chain(duration / max_duration))
    filters.append(f"atrim=0:{max_duration:.3f}")
    filters.append("asetpts=PTS-STARTPTS")
    run(
        [
            "ffmpeg",
            "-y",
            "-i",
            str(src),
            "-af",
            ",".join(filters),
            str(dst),
        ]
    )


def build_audio(cues: list[Cue], work: Path) -> Path:
    asyncio.run(synthesize_all(cues, work))

    fitted: list[Path] = []
    for i, cue in enumerate(cues):
        raw = work / f"seg-{cue.index:02d}-raw.mp3"
        fit = work / f"seg-{cue.index:02d}.mp3"
        allowed = max_segment_duration(cues, i)
        fit_segment(raw, fit, allowed)
        fitted.append(fit)
        dur = probe_duration(fit)
        print(f"  cue {cue.index}: start={cue.start:.2f}s max={allowed:.2f}s actual={dur:.2f}s")

    inputs: list[str] = []
    filter_parts: list[str] = []
    mix_labels: list[str] = []

    for i, (cue, seg) in enumerate(zip(cues, fitted)):
        inputs.extend(["-i", str(seg)])
        delay_ms = int(cue.start * 1000)
        label = f"v{i}"
        # Segment already trimmed — delay places it; no overlap possible
        filter_parts.append(f"[{i}:a]adelay={delay_ms}|{delay_ms}[{label}]")
        mix_labels.append(f"[{label}]")

    mixed = work / "voiceover.m4a"
    n = len(cues)
    filter_complex = (
        ";".join(filter_parts)
        + ";"
        + "".join(mix_labels)
        + f"amix=inputs={n}:duration=longest:dropout_transition=0:normalize=0,"
        f"atrim=0:{VIDEO_DURATION},asetpts=PTS-STARTPTS,"
        f"loudnorm=I=-14:TP=-1.5:LRA=11[aout]"
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
            "-ar",
            "44100",
            str(mixed),
        ]
    )

    saved = OUT_DIR / "accredready-promo-voiceover.m4a"
    shutil.copy(mixed, saved)
    print(f"✓ {saved}")
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
            "-ar",
            "44100",
            "-shortest",
            "-movflags",
            "+faststart",
            str(video_out),
        ]
    )


def ensure_silent_backups() -> None:
    """Keep one silent copy — never overwrite from a voiced file."""
    PUBLIC.mkdir(exist_ok=True)
    silent_h = PUBLIC / "accredready-promo-silent.mp4"
    silent_v = PUBLIC / "accredready-promo-vertical-silent.mp4"
    src_h = OUT_DIR / "accredready-promo-1080p.mp4"
    src_v = OUT_DIR / "accredready-promo-vertical.mp4"
    if not silent_h.exists() and src_h.exists():
        shutil.copy(src_h, silent_h)
    if not silent_v.exists() and src_v.exists():
        shutil.copy(src_v, silent_v)


def publish_voiced_videos(voiced: dict[str, Path]) -> None:
    PUBLIC.mkdir(exist_ok=True)
    ensure_silent_backups()

    shutil.copy(voiced["horizontal"], PUBLIC / "accredready-promo.mp4")
    shutil.copy(voiced["vertical"], PUBLIC / "accredready-promo-vertical.mp4")
    shutil.copy(voiced["horizontal"], PUBLIC / "accredready-promo-1080p-with-voice.mp4")
    shutil.copy(voiced["vertical"], PUBLIC / "accredready-promo-vertical-with-voice.mp4")


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

        sources = {
            "horizontal": OUT_DIR / "accredready-promo-1080p.mp4",
            "vertical": OUT_DIR / "accredready-promo-vertical.mp4",
        }
        outputs = {
            "horizontal": OUT_DIR / "accredready-promo-1080p-voiced.mp4",
            "vertical": OUT_DIR / "accredready-promo-vertical-voiced.mp4",
        }

        voiced: dict[str, Path] = {}
        for key, src in sources.items():
            if not src.exists():
                print(f"Skip missing video: {src}")
                continue
            dst = outputs[key]
            mux_video(src, audio, dst)
            voiced[key] = dst
            print(f"✓ {dst}")

        if voiced:
            publish_voiced_videos(voiced)
            print("✓ public/accredready-promo.mp4 now includes voiceover")

    print("\nDone.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
