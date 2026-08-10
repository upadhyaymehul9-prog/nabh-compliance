#!/usr/bin/env bash
# Build AAC.1.b animated explainer (same style as preferred AAC.1.a cut).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
ASSETS="$ROOT/assets"
SCENES="$ROOT/scenes-1b"
TMP=/tmp/aac1b_build
mkdir -p "$TMP"

python3 "$ROOT/render_aac1b_video.py"

VO_SCRIPT="$TMP/vo.txt"
cat > "$VO_SCRIPT" <<'EOF'
Hello quality champions! Today we dive into A A C one b — staff cover for every specialty!

Does every specialty have real cover for O P, I P, daycare, and emergency?

A A C one b requires diagnostic and treatment services for each defined clinical service, with suitably qualified personnel covering out-patient, in-patient, daycare and emergency — plus consultants on emergency cover.

Common gaps: specialty on paper only, no full care path, weak diagnostics, and missing emergency call lists!

Simple first step: list every clinical service, name cover holders for each pathway, then close gaps — staff first, then infrastructure!

You have got this! AccredReady — Quality Today, Accreditation Tomorrow. www.accredready.in
EOF

echo "Generating enthusiastic VO…"
edge-tts --voice en-US-GuyNeural --rate=+18% --pitch=+4Hz \
  --file "$VO_SCRIPT" --write-media "$ASSETS/vo-aac1b-enth.mp3"

# Mix BGM under VO (reuse 1a bgm if present)
BGM="$ASSETS/bgm.mp3"
if [[ ! -f "$BGM" ]]; then
  echo "Missing bgm.mp3 — using VO only"
  cp "$ASSETS/vo-aac1b-enth.mp3" "$ASSETS/audio-mix-1b.m4a"
else
  ffmpeg -y -i "$ASSETS/vo-aac1b-enth.mp3" -stream_loop -1 -i "$BGM" \
    -filter_complex "[1:a]volume=0.12[bg];[0:a][bg]amix=inputs=2:duration=first:dropout_transition=2[a]" \
    -map "[a]" -c:a aac -b:a 192k "$ASSETS/audio-mix-1b.m4a"
fi

DUR=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$ASSETS/audio-mix-1b.m4a")
echo "Audio duration: $DUR"

# Scene durations (seconds) — match narrative beats; scale to audio length
# weights: intro, question, bullets, gaps, steps, outro
python3 - <<PY
from pathlib import Path
import subprocess
dur = float("$DUR")
weights = [5.0, 7.5, 8.0, 8.5, 7.5, 4.0]
total_w = sum(weights)
durs = [dur * w / total_w for w in weights]
# ensure last scene absorbs rounding
s = sum(durs[:-1])
durs[-1] = max(1.0, dur - s)
scenes = sorted(Path("$SCENES").glob("*.png"))
assert len(scenes) == 6, scenes
fps = 30
concat = Path("$TMP/concat.txt")
lines = []
for i, (scene, d) in enumerate(zip(scenes, durs), 1):
    out = Path("$TMP") / f"c{i}.mp4"
    # gentle Ken Burns zoom (same feel as AAC.1.a)
    frames = max(1, int(round(d * fps)))
    z_end = 1.08
    # zoompan: z increases slowly; keep centered
    vf = (
        f"scale=1200:1500,"
        f"zoompan=z='min(1.0+0.08*on/{frames},1.08)':"
        f"x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
        f"d={frames}:s=1080x1350:fps={fps}"
    )
    subprocess.run([
        "ffmpeg", "-y", "-loop", "1", "-i", str(scene),
        "-vf", vf, "-t", f"{d:.3f}", "-r", str(fps),
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "veryfast", "-crf", "20",
        str(out),
    ], check=True)
    lines.append(f"file '{out}'")
concat.write_text("\n".join(lines) + "\n")
print("clips ready", durs)
PY

ffmpeg -y -f concat -safe 0 -i "$TMP/concat.txt" -c copy "$TMP/video_silent.mp4"
ffmpeg -y -i "$TMP/video_silent.mp4" -i "$ASSETS/audio-mix-1b.m4a" \
  -c:v libx264 -pix_fmt yuv420p -preset medium -crf 20 \
  -c:a aac -b:a 192k -shortest -movflags +faststart \
  "$ROOT/AAC-1b-animated.mp4"

ls -lh "$ROOT/AAC-1b-animated.mp4"
ffprobe -v error -show_entries format=duration,size -show_entries stream=codec_type,width,height,r_frame_rate -of default=noprint_wrappers=1 "$ROOT/AAC-1b-animated.mp4"
echo "DONE"
