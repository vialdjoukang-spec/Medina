#!/usr/bin/env python3
"""Empreintes des sources ; mêmes opérations pour Claude et Codex.

Autorité commune du 15 octobre 2026 ; les registres historiques restent lisibles.
Le registre atteste une décision technique, jamais une validation médicale.

  python3 tools/sceller.py enregistrer --actor Codex
  python3 tools/sceller.py sceller --actor Claude
  python3 tools/sceller.py verifier      # les sources actuelles correspondent au registre

Aucun préfixe de branche ne confère de privilège. Le champ scelle historique
reste documentaire ; les autorisations et veto relèvent de la garde commune.
Pour la publication en l'état, utiliser son reçu de provenance dédié sans
réécrire ce registre historique.
"""

from __future__ import annotations

import hashlib
import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = "organisation/SCELLES.json"
AUTHORITY = "docs/collaboration/LEADERSHIP_CLAUDE_2026-10-08.md#12"
COMMON_AUTHORITY = "docs/collaboration/instructions/PUBLICATION_EN_ETAT_PARITE_2026-10-15.md"


def medical_files(root=ROOT):
    files = [p for base in ("chapters", "glossary") for p in sorted((root / base).rglob("*"))
             if p.is_file() and "__pycache__" not in p.parts]
    files.append(root / "chapters.json")
    return {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest() for p in files}


def write(sealed, actor):
    if actor not in {"Codex", "Claude"}:
        raise ValueError("Acteur Codex ou Claude requis ; ne pas attribuer une opération à l'autre IA.")
    path = ROOT / REGISTRY
    previous = json.loads(path.read_text()) if path.exists() else {}
    data = {
        "autorite": COMMON_AUTHORITY,
        "injecteur": actor,
        "scelle": bool(sealed or previous.get("scelle")),
        "mis_a_jour": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "portee": "Empreintes techniques ; administration commune Codex/Claude, sans validation médicale.",
        "precedent_sha256": hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else None,
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
    """Lit les anciennes preuves sans réintroduire de privilège par IA ou branche."""
    authorised = {}
    if after_registry:
        legacy = after_registry.get("autorite") == AUTHORITY and after_registry.get("injecteur") == "Claude"
        common = after_registry.get("autorite") == COMMON_AUTHORITY and after_registry.get("injecteur") in {"Codex", "Claude"}
        if not (legacy or common):
            raise ValueError("Registre d'empreintes : autorité ou acteur invalide.")
        authorised = dict(after_registry.get("fichiers", {}))
    return authorised


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('action', choices=('enregistrer', 'sceller', 'verifier'))
    parser.add_argument('--actor', choices=('Codex', 'Claude'))
    args = parser.parse_args()
    action = args.action
    if action in {'enregistrer', 'sceller'} and args.actor is None:
        parser.error('--actor Codex|Claude requis pour tracer l’auteur réel de l’opération')
    if action == "enregistrer":
        write(False, args.actor)
    elif action == "sceller":
        write(True, args.actor)
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
