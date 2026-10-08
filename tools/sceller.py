#!/usr/bin/env python3
"""Registre d'injection directe et scellement des cours par Claude.

Autorité : section 12 de docs/collaboration/LEADERSHIP_CLAUDE_2026-10-08.md
(consigne directe de Vial, 8 octobre 2026) : les cours de Claude et les cours
Codex corrigés par Claude sont injectés directement par Claude, sans audit Codex.

  python3 tools/sceller.py enregistrer   # empreintes des sources médicales actuelles
  python3 tools/sceller.py sceller       # idem, et scelle : modification réservée aux branches claude/*
  python3 tools/sceller.py verifier      # les sources actuelles correspondent au registre

La garde (tools/espace.py garde) autorise une source médicale modifiée lorsque
son empreinte figure dans ce registre ; une fois le registre scellé, toute
modification d'une source scellée ou du registre hors d'une branche claude/*
est refusée. Le registre atteste une décision d'injection, pas une validation
médicale.
"""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = "organisation/SCELLES.json"
AUTHORITY = "docs/collaboration/LEADERSHIP_CLAUDE_2026-10-08.md#12"


def medical_files(root=ROOT):
    files = [p for base in ("chapters", "glossary") for p in sorted((root / base).rglob("*"))
             if p.is_file() and "__pycache__" not in p.parts]
    files.append(root / "chapters.json")
    return {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest() for p in files}


def write(sealed):
    path = ROOT / REGISTRY
    previous = json.loads(path.read_text()) if path.exists() else {}
    data = {
        "autorite": AUTHORITY,
        "injecteur": "Claude",
        "scelle": bool(sealed or previous.get("scelle")),
        "mis_a_jour": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "portee": "Sources médicales canoniques injectées par Claude ; décision d'injection, non validation médicale.",
        "fichiers": medical_files(),
    }
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{len(data['fichiers'])} fichiers enregistrés ; scellé : {data['scelle']}")


def current_branch():
    for key in ("GITHUB_HEAD_REF", "GITHUB_REF_NAME"):
        if os.environ.get(key):
            return os.environ[key]
    try:
        return subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return ""


def guard(before_registry, after_registry, changed_medical, read_after):
    """Return {path: digest} authorised by the registry; raise ValueError on a seal breach."""
    authorised = {}
    if after_registry:
        if after_registry.get("autorite") != AUTHORITY or after_registry.get("injecteur") != "Claude":
            raise ValueError("Registre d'injection Claude invalide.")
        authorised = dict(after_registry.get("fichiers", {}))
    if before_registry and before_registry.get("scelle"):
        sealed = before_registry.get("fichiers", {})
        touched = [p for p in changed_medical if p in sealed]
        registry_changed = before_registry != after_registry
        if (touched or registry_changed) and not current_branch().startswith("claude/"):
            raise ValueError("Cours scellés par Claude : modification réservée à Claude "
                             f"(branche claude/*). Fichiers : {touched[:10]}")
    return authorised


def main():
    action = sys.argv[1] if len(sys.argv) > 1 else ""
    if action == "enregistrer":
        write(False)
    elif action == "sceller":
        write(True)
    elif action == "verifier":
        data = json.loads((ROOT / REGISTRY).read_text())
        diff = [p for p, d in medical_files().items() if data["fichiers"].get(p) != d]
        print("Conforme" if not diff else f"{len(diff)} écarts : {diff[:20]}")
        return 1 if diff else 0
    else:
        print(__doc__)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
