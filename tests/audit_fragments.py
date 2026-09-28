#!/usr/bin/env python3
"""Audit bloquant des fragments et de la reproductibilité du build MEDINA."""
import base64
import gzip
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FRAGMENT_DIR = Path(os.environ.get("MEDINA_FRAGMENTS", ROOT / "dist/fragments"))


def expanded_html(path):
    source = path.read_text(encoding="utf-8")
    packed = re.search(r'<script id="mdn-pack"[^>]*>([^<]+)</script>', source)
    if packed:
        source += gzip.decompress(base64.b64decode(packed.group(1))).decode("utf-8")
    return source


def expected_chapters(fragment, chapters, entries, explicit):
    attached = set(fragment["rattachements"])
    systems = {entry["code"]: entry.get("system") for entry in entries}
    return {chapter["code"] for chapter in chapters if chapter.get("integrated") and
            (chapter["code"] in attached or
             (chapter["code"] not in explicit and systems.get(chapter["code"]) in attached))}


def check_javascript(path, source):
    scripts = re.findall(r'<script(?P<attrs>[^>]*)>(?P<body>[\s\S]*?)</script>', source, re.I)
    for number, match in enumerate(scripts, 1):
        attrs, body = match
        kind = re.search(r'\btype=["\']([^"\']+)', attrs, re.I)
        if kind and kind.group(1).lower() not in ("text/javascript", "application/javascript", "module"):
            continue
        with tempfile.NamedTemporaryFile("w", suffix=".js", encoding="utf-8", dir=ROOT) as js:
            js.write(body)
            js.flush()
            result = subprocess.run(["node", "--check", js.name], capture_output=True, text=True)
        if result.returncode:
            raise AssertionError(f"JavaScript invalide dans {path.name}, bloc {number}:\n{result.stderr}")


def reproducibility():
    hashes = []
    with tempfile.TemporaryDirectory(prefix=".audit-build-", dir=ROOT) as temporary:
        for run in ("a", "b"):
            output = Path(temporary) / run
            env = os.environ.copy()
            env["MEDINA_ROOT"] = str(ROOT)
            env["MEDINA_OUT"] = str(output)
            subprocess.run([sys.executable, str(ROOT / "build_front.py")], check=True, env=env,
                           stdout=subprocess.DEVNULL)
            hashes.append(hashlib.sha256((output / "MEDINA.html").read_bytes()).hexdigest())
    if hashes[0] != hashes[1]:
        raise AssertionError(f"build non reproductible : {hashes[0]} != {hashes[1]}")


def main():
    fragments = json.loads((ROOT / "fragments.json").read_text(encoding="utf-8"))
    required_ids = {f"S{number:02d}" for number in range(1, 17)} - {"S09"}
    required_ids |= {f"T{number}" for number in range(1, 8)}
    manifest_ids = {fragment["id"] for fragment in fragments}
    if manifest_ids != required_ids:
        missing = ", ".join(sorted(required_ids - manifest_ids)) or "aucun"
        extra = ", ".join(sorted(manifest_ids - required_ids)) or "aucun"
        raise SystemExit(f"fragments.json incomplet (manquants : {missing} ; inattendus : {extra})")
    chapters = json.loads((ROOT / "chapters.json").read_text(encoding="utf-8"))
    shell = (ROOT / "shell/medina_front.html").read_text(encoding="utf-8")
    payload = re.search(r'<script id="medora-data" type="application/json">(.*?)</script>', shell, re.S)
    entries = json.loads(payload.group(1))["entries"]
    explicit = {code: fragment["id"] for fragment in fragments for code in fragment["rattachements"]
                if re.fullmatch(r"[A-Z][0-9]{2}", code)}

    errors = []
    for fragment in fragments:
        path = FRAGMENT_DIR / f"MEDINA_{fragment['id']}_{fragment['slug']}.html"
        if not path.is_file():
            errors.append(f"fragment manquant : {path}")
            continue
        source = expanded_html(path)
        present = set(re.findall(r'id=["\']ch-([^"\']+)["\']', source))
        foreign = present - expected_chapters(fragment, chapters, entries, explicit)
        if foreign:
            errors.append(f"{fragment['id']} contient des chapitres étrangers : {', '.join(sorted(foreign))}")
        try:
            check_javascript(path, source)
        except AssertionError as error:
            errors.append(str(error))
    if errors:
        raise SystemExit("\n".join(errors))
    reproducibility()
    print(f"audit réussi : {len(fragments)} fragments, JavaScript valide, build reproductible")


if __name__ == "__main__":
    main()
