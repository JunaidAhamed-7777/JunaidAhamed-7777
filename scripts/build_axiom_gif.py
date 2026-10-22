"""Encode the selected-work GIF from Axiom's original gameplay recording.

Requires ffmpeg on PATH. Pass a checkout of axiom-steal-the-laws:
    python scripts/build_axiom_gif.py /path/to/axiom-steal-the-laws

Source: JunaidAhamed-7777/axiom-steal-the-laws at
b46dc36d6b8eec511253e2011026b0a128469442,
Evidence/Demo/AXIOM_final_native_live_demo.mp4.
This is actual Unreal gameplay with scripted player actions, not a human
playthrough. Its on-screen disclosure and original frame timing are retained.
"""

import argparse
import hashlib
from pathlib import Path
import subprocess

SOURCE_HASH = "4ebf26f6e2d4126ecf051c96d5b2bcd9d1026fa94bf816c9d34f3fa37dde75dd"
FIT = "scale=720:405:flags=lanczos,pad=720:420:0:7:color=0x101210"
OUT = Path(__file__).resolve().parents[1] / "assets"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_repo", type=Path)
    args = parser.parse_args()
    source = args.source_repo / "Evidence/Demo/AXIOM_final_native_live_demo.mp4"
    if hashlib.sha256(source.read_bytes()).hexdigest() != SOURCE_HASH:
        parser.error("Source recording differs from the verified original.")
    common = ["ffmpeg", "-nostdin", "-hide_banner", "-loglevel", "error"]
    subprocess.run(common + [
        "-i", str(source), "-filter_complex",
        f"[0:v]trim=start=43.4:end=50.4,setpts=PTS-STARTPTS,{FIT},split[a][b];"
        "[a]palettegen=stats_mode=diff[p];[b][p]paletteuse=dither=sierra2_4a:diff_mode=rectangle",
        "-fps_mode", "vfr", "-loop", "0", "-an", "-y", str(OUT / "project-axiom.gif"),
    ], check=True)
    subprocess.run(common + [
        "-ss", "47.0", "-i", str(source), "-frames:v", "1", "-vf", FIT,
        "-y", str(OUT / "project-axiom-static.png"),
    ], check=True)


if __name__ == "__main__":
    main()
