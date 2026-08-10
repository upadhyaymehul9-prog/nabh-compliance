#!/usr/bin/env python3
"""Build AAC OE animated videos for a batch of codes (doctor scenes + VO + BGM)."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
CATALOG = ROOT / "oes_content.json"
BGM = ASSETS / "bgm.mp3"


def run(cmd, **kw):
    subprocess.run(cmd, check=True, **kw)


def speak_script(item: dict) -> str:
    code = item["code"]
    # Spell letters for TTS clarity: AAC.1.c -> A A C one c
    parts = code.split(".")
    std = parts[1]
    letter = parts[2]
    spoken = f"A A C {std} {letter}"
    headline = item["headline"].replace("—", "-")
    oe = item["oe_text"]
    gaps = "; ".join(g["title"] for g in item["gaps"][:4])
    steps = " ".join(f"Step {i}: {s}" for i, s in enumerate(item["steps"][:3], 1))
    return (
        f"Hello quality champions! Today we dive into {spoken}.\n\n"
        f"{headline}\n\n"
        f"Here is the requirement: {oe}\n\n"
        f"Watch for these common gaps: {gaps}.\n\n"
        f"Simple first steps. {steps}\n\n"
        f"You have got this! AccredReady — Quality Today, Accreditation Tomorrow. "
        f"www.accredready.in"
    )


def build_one(item: dict, force: bool = False) -> Path:
    stem = item["file_stem"]
    out_mp4 = ROOT / f"{stem}-animated.mp4"
    if out_mp4.exists() and out_mp4.stat().st_size > 500_000 and not force:
        # Keep user-approved AAC-1a / AAC-1b unless forced
        print(f"SKIP existing {out_mp4.name}")
        return out_mp4

    scenes_dir = ROOT / "scenes" / stem
    run([sys.executable, str(ROOT / "render_oe_scenes.py"), "--code", item["code"]])

    vo_txt = Path(f"/tmp/{stem}-vo.txt")
    vo_mp3 = ASSETS / f"vo-{stem}-enth.mp3"
    mix = ASSETS / f"audio-mix-{stem}.m4a"
    vo_txt.write_text(speak_script(item))
    run(
        [
            "edge-tts",
            "--voice",
            "en-US-GuyNeural",
            "--rate=+18%",
            "--pitch=+4Hz",
            "--file",
            str(vo_txt),
            "--write-media",
            str(vo_mp3),
        ]
    )

    if BGM.exists():
        run(
            [
                "ffmpeg",
                "-y",
                "-i",
                str(vo_mp3),
                "-stream_loop",
                "-1",
                "-i",
                str(BGM),
                "-filter_complex",
                "[1:a]volume=0.10,highpass=f=120,lowpass=f=8000[bg];"
                "[0:a][bg]amix=inputs=2:duration=first:dropout_transition=2[a]",
                "-map",
                "[a]",
                "-c:a",
                "aac",
                "-b:a",
                "192k",
                str(mix),
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    else:
        run(
            ["ffmpeg", "-y", "-i", str(vo_mp3), "-c:a", "aac", "-b:a", "192k", str(mix)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

    dur = float(
        subprocess.check_output(
            [
                "ffprobe",
                "-v",
                "error",
                "-show_entries",
                "format=duration",
                "-of",
                "default=noprint_wrappers=1:nokey=1",
                str(mix),
            ],
            text=True,
        ).strip()
    )

    weights = [5.0, 7.5, 8.0, 8.5, 7.5, 4.0]
    tw = sum(weights)
    durs = [dur * w / tw for w in weights]
    durs[-1] = max(1.0, dur - sum(durs[:-1]))
    scenes = sorted(scenes_dir.glob("*.png"))
    assert len(scenes) == 6, scenes

    tmp = Path(f"/tmp/build_{stem}")
    tmp.mkdir(parents=True, exist_ok=True)
    fps = 30
    concat_lines = []
    for i, (scene, d) in enumerate(zip(scenes, durs), 1):
        clip = tmp / f"c{i}.mp4"
        frames = max(1, int(round(d * fps)))
        vf = (
            f"scale=1200:1500,"
            f"zoompan=z='min(1.0+0.08*on/{frames},1.08)':"
            f"x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
            f"d={frames}:s=1080x1350:fps={fps}"
        )
        run(
            [
                "ffmpeg",
                "-y",
                "-loop",
                "1",
                "-i",
                str(scene),
                "-vf",
                vf,
                "-t",
                f"{d:.3f}",
                "-r",
                str(fps),
                "-c:v",
                "libx264",
                "-pix_fmt",
                "yuv420p",
                "-preset",
                "veryfast",
                "-crf",
                "22",
                str(clip),
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        concat_lines.append(f"file '{clip}'")
    concat = tmp / "concat.txt"
    concat.write_text("\n".join(concat_lines) + "\n")
    silent = tmp / "silent.mp4"
    run(
        ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat), "-c", "copy", str(silent)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    run(
        [
            "ffmpeg",
            "-y",
            "-i",
            str(silent),
            "-i",
            str(mix),
            "-c:v",
            "libx264",
            "-pix_fmt",
            "yuv420p",
            "-preset",
            "veryfast",
            "-crf",
            "22",
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            "-shortest",
            "-movflags",
            "+faststart",
            str(out_mp4),
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    print(f"OK {out_mp4.name} ({dur:.1f}s)")
    return out_mp4


def parse_codes(batch: str) -> list[str]:
    """Accept 'AAC.1.c,AAC.1.d' or range helpers via catalog order."""
    return [c.strip() for c in batch.split(",") if c.strip()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--codes", help="Comma-separated OE codes")
    ap.add_argument("--start", help="Start code inclusive (catalog order)")
    ap.add_argument("--count", type=int, default=10)
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--workers", type=int, default=2)
    args = ap.parse_args()

    catalog = json.loads(CATALOG.read_text())
    by_code = {x["code"]: x for x in catalog}
    order = [x["code"] for x in catalog]

    if args.codes:
        codes = parse_codes(args.codes)
    elif args.start:
        i = order.index(args.start)
        codes = order[i : i + args.count]
    else:
        raise SystemExit("Provide --codes or --start")

    # Always preserve preferred AAC.1.a / AAC.1.b unless --force
    protect = {"AAC.1.a", "AAC.1.b"}
    items = []
    for c in codes:
        if c not in by_code:
            raise SystemExit(f"Unknown code {c}")
        if c in protect and not args.force:
            print(f"KEEP preferred {c}")
            continue
        items.append(by_code[c])

    print(f"Building {len(items)} videos…")
    # Sequential is safer for ffmpeg/edge-tts rate limits; small pool ok
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as ex:
        futs = [ex.submit(build_one, item, args.force) for item in items]
        for f in as_completed(futs):
            f.result()
    print("BATCH DONE", len(items))


if __name__ == "__main__":
    main()
