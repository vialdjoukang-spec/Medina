#!/usr/bin/env python3
"""Assemble only real, hash-verified Chromium captures; no simulated UI."""
import argparse
import hashlib
import json
from pathlib import Path
from PIL import Image


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", type=Path, default=Path("docs/collaboration/reviews/2026-10-08/C01_PROVISOIRE/reserves"))
    args = parser.parse_args()
    report = json.loads((args.directory / "i51_reservations_results.json").read_text(encoding="utf-8"))
    if report.get("result") != "passed":
        raise SystemExit("Real browser reservations check must pass before animation.")
    captures = {item["file"]: item for item in report["captures"]}
    names = ["i51-1440-i51-reserve-choc.png", "i51-1440-i51-reserve-aod.png", "i51-1440-i51-reserve-levo.png", "i51-1440-explication.png"]
    frames = []
    for name in names:
        file = args.directory / name
        if hashlib.sha256(file.read_bytes()).hexdigest() != captures[name]["sha256"]:
            raise SystemExit("Screenshot hash changed: " + name)
        with Image.open(file) as source:
            if source.size != (1440, 900):
                raise SystemExit("Unexpected capture dimensions: " + name)
            frames.append(source.convert("RGB"))
    target = args.directory / "I51_navigation_enregistree_2026-10-08.gif"
    frames[0].save(target, save_all=True, append_images=frames[1:], duration=[4000] * len(frames), loop=0, disposal=2)
    print(json.dumps({"animation": str(target), "frames": len(frames), "source": "Real recorded browser clicks; not a live stream", "sha256": hashlib.sha256(target.read_bytes()).hexdigest()}))


if __name__ == "__main__":
    main()
