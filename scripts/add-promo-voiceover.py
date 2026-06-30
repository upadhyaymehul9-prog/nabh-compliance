#!/usr/bin/env python3
"""Generate Edge TTS voiceover for promo MP4 — one continuous read, uniform pace."""

from __future__ import annotations

import asyncio
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import edge_tts

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "marketing/video/output"
PUBLIC = ROOT / "public"
VOICE = "en-IN-NeerjaNeural"
VIDEO_DURATION = 37.0
LEAD_IN = 0.3
TARGET_SPEECH = VIDEO_DURATION - LEAD_IN - 0.15  # room before end card

# Trimmed for 37s at a calm, consistent pace (+8–10% TTS, minimal compression)
FULL_SCRIPT = (
    "AccredReady — NABH compliance for Indian hospitals and healthcare organisations. "
    "Most teams still use Excel and consultants charging fifty thousand to two lakh rupees. "
    "One platform to score objective elements, rank gaps, log CAPA, and track KPIs, audits, and drills. "
    "Your readiness dashboard shows where you stand before the assessor arrives. "
    "HCO Full, SHCO Full, ELC, and ECO — every major NABH programme, one subscription. "
    "Four hundred ninety-nine rupees a month. Start your free trial at accredready.in — no credit card required."
)


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


async def synthesize(text: str, rate: str, out: Path) -> None:
    communicate = edge_tts.Communicate(text, VOICE, rate=rate)
    await communicate.save(str(out))


def make_silence(path: Path, duration: float) -> None:
    run(
        [
            "ffmpeg",
            "-y",
            "-f",
            "lavfi",
            "-i",
            "anullsrc=r=44100:cl=mono",
            "-t",
            f"{duration:.3f}",
            "-c:a",
            "libmp3lame",
            str(path),
        ]
    )


def build_audio(work: Path) -> Path:
    """One voice, one speed: TTS rate + single atempo pass to fit the video."""
    # Pick the slowest TTS rate that fits with minimal atempo (calmer delivery)
    rates = ["+0%", "+5%", "+8%", "+10%", "+12%", "+15%"]
    raw = work / "narration-raw.mp3"
    best_rate = rates[-1]

    for rate in rates:
        asyncio.run(synthesize(FULL_SCRIPT, rate, raw))
        duration = probe_duration(raw)
        tempo_needed = duration / TARGET_SPEECH
        print(f"  TTS rate {rate}: {duration:.1f}s → tempo {tempo_needed:.3f}x to fit {TARGET_SPEECH:.1f}s")
        if tempo_needed <= 1.12:
            best_rate = rate
            break
        best_rate = rate

    duration = probe_duration(raw)
    tempo = duration / TARGET_SPEECH
    tempo = min(max(tempo, 1.0), 1.12)

    fitted = work / "narration-fit.mp3"
    run(
        [
            "ffmpeg",
            "-y",
            "-i",
            str(raw),
            "-af",
            f"{atempo_chain(tempo)},loudnorm=I=-14:TP=-1.5:LRA=11",
            str(fitted),
        ]
    )
    speech_dur = probe_duration(fitted)
    print(f"  final: rate={best_rate}, tempo={tempo:.3f}x, speech={speech_dur:.1f}s")

    lead = work / "lead.mp3"
    make_silence(lead, LEAD_IN)

    concat_list = work / "concat.txt"
    concat_list.write_text(f"file '{lead}'\nfile '{fitted}'\n", encoding="utf-8")

    mixed = work / "voiceover.m4a"
    run(
        [
            "ffmpeg",
            "-y",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(concat_list),
            "-af",
            f"apad=pad_dur={VIDEO_DURATION},atrim=0:{VIDEO_DURATION}",
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
    print(f"✓ {saved} ({probe_duration(saved):.1f}s)")
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

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="promo-voice-") as tmp:
        work = Path(tmp)
        audio = build_audio(work)

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
            print("✓ public/accredready-promo.mp4 updated")

    print("\nDone.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
