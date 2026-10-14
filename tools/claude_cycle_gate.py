#!/usr/bin/env python3
"""Relevé d'application du Prompt de vérité (entrée ou sortie) pour les cycles repris par Claude.

Format attendu par tools/tetrade_cycle.py::prompt_gate : empreintes des cinq fichiers du Prompt,
sept contrôles, chacun appuyé sur au moins une preuve du dépôt (chemin + SHA-256 + explication).
L'outil calcule les empreintes ; il ne décide d'aucun verdict : chaque explication est écrite par l'agent.

python3 tools/claude_cycle_gate.py --actor C02-R-NEUR --out chemin/entree.json \
  --check autorisation "docs/collaboration/instructions/CYCLE_02_REPRISE_CLAUDE_VIAL_2026-10-14.md" "Explication…" \
  --check perimetre_provenance CHEMIN "Explication…"   (… sept identifiants, répétables)
"""
import argparse, hashlib, json, sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUTHORITY = "docs/collaboration/instructions/CYCLE_02_REPRISE_CLAUDE_VIAL_2026-10-14.md"
PROMPTS = ("PROMPT_MEDINA.md", "PROMPT_TRANSITION.md", "docs/STYLE_REDACTION.md", AUTHORITY,
           "docs/collaboration/instructions/CLARTE_BASES_CALCULS_VIAL_2026-10-11.md")
CHECKS = ("autorisation", "perimetre_provenance", "sources_lues", "contexte_suisse", "independance",
          "contrat_cours", "honnetete")


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--actor", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--check", nargs=3, action="append", metavar=("ID", "CHEMIN", "EXPLICATION"), required=True)
    a = p.parse_args()
    checks = {}
    for cid, path, why in a.check:
        if cid not in CHECKS:
            p.error("identifiant inconnu : " + cid)
        if not (ROOT / path).is_file() or not why.strip():
            p.error(f"preuve absente ou explication vide : {path}")
        checks.setdefault(cid, []).append({"path": path, "sha256": sha(path), "explanation": why.strip()})
    missing = set(CHECKS) - set(checks)
    if missing:
        p.error("contrôles manquants : " + ", ".join(sorted(missing)))
    gate = {"actor": a.actor, "verdict": "conforme", "checked_at": datetime.now(timezone.utc).isoformat(),
            "prompt_files": {f: sha(f) for f in PROMPTS},
            "checks": [{"id": c, "status": "conforme", "evidence": checks[c]} for c in CHECKS]}
    out = ROOT / a.out
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(gate, ensure_ascii=False, indent=1) + "\n")
    print(out.relative_to(ROOT))


if __name__ == "__main__":
    sys.exit(main())
