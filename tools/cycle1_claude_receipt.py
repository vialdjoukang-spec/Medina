#!/usr/bin/env python3
"""Tracer les corrections Claude ; utiliser un vrai rapport technique déjà produit.

python3 tools/cycle1_claude_receipt.py --checks RAPPORT.json --reason "Correction expliquée"
N'effectue ni audit ni tests et ne fabrique jamais un résultat favorable.
"""
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECEIPT = "organisation/CYCLE_01_REPRISE_CLAUDE_2026-10-13.json"

def digest(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--checks", required=True)
    p.add_argument("--reason", required=True)
    args = p.parse_args()
    checks = Path(args.checks)
    if checks.is_absolute() or ".." in checks.parts or not args.reason.strip():
        p.error("Rapport relatif au dépôt et motif non vide requis")
    data = json.loads((ROOT / RECEIPT).read_text())
    files = {path: digest(path) for path in data["files"]}
    technical = json.loads((ROOT / checks).read_text())
    if technical.get("files") != files or technical.get("result") != "passed":
        p.error("Le rapport doit vérifier réellement les empreintes courantes avec succès")
    changed = {path: {"before": data["files"][path], "after": sha, "reason": args.reason}
               for path, sha in files.items() if data["files"][path] != sha}
    if changed:
        name = datetime.now(timezone.utc).strftime("corrections_Claude_%Y%m%dT%H%M%S%fZ.json")
        path = "docs/collaboration/reviews/2026-10-13/CYCLE_01/" + name
        (ROOT / path).write_text(json.dumps({"actor": "Claude", "files": changed}, ensure_ascii=False, indent=2)+"\n")
        data["change_report"] = {"path": path, "sha256": digest(path)}
    data["files"] = files
    data["technical_checks"] = {"path": str(checks), "sha256": digest(checks)}
    (ROOT / RECEIPT).write_text(json.dumps(data, ensure_ascii=False, indent=2)+"\n")
    state_path = ROOT / "organisation/tetrade_cycle_status.json"
    state = json.loads(state_path.read_text())
    state["publication_exception"] = {"path": RECEIPT, "sha256": digest(RECEIPT)}
    state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2)+"\n")
    print(f"{len(changed)} corrections tracées ; aucune qualification d'audit modifiée.")

if __name__ == "__main__":
    main()
