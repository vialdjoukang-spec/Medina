#!/usr/bin/env python3
"""Relevé d'application du Prompt de vérité (entrée ou sortie) pour les cycles repris par Claude.

Format attendu par tools/tetrade_cycle.py::prompt_gate : empreintes des cinq fichiers du Prompt,
sept contrôles, chacun appuyé sur au moins une preuve du dépôt (chemin + SHA-256 + explication).
L'outil calcule les empreintes ; il ne décide d'aucun verdict : chaque explication est écrite par l'agent.

python3 tools/claude_cycle_gate.py --actor C02-R-NEUR --out chemin/entree.json \
  --check autorisation "docs/collaboration/instructions/CYCLE_02_REPRISE_CLAUDE_VIAL_2026-10-14.md" "Explication…" \
  --check perimetre_provenance CHEMIN "Explication…"   (… sept identifiants, répétables)

--prompts direct : relevé contre PROMPTS_DIRECT (tools/cycle_claude.py), où l'autorité de publication directe
des cycles 2 à 30 remplace celle de la reprise du Cycle 2 ; par défaut « reprise » (chaîne complète).
"""
import argparse, hashlib, json, sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUTHORITY = "docs/collaboration/instructions/CYCLE_02_REPRISE_CLAUDE_VIAL_2026-10-14.md"
PROMPTS = ("PROMPT_MEDINA.md", "PROMPT_TRANSITION.md", "docs/STYLE_REDACTION.md", AUTHORITY,
           "docs/collaboration/instructions/CLARTE_BASES_CALCULS_VIAL_2026-10-11.md")
DIRECT_AUTHORITY = "docs/collaboration/instructions/CYCLES_03_30_PUBLICATION_DIRECTE_VIAL_2026-10-14.md"
PROMPT_SETS = {"reprise": PROMPTS, "direct": tuple(DIRECT_AUTHORITY if p == AUTHORITY else p for p in PROMPTS)}
PROMPT_SETS['novo'] = PROMPT_SETS['direct'] + (
    'docs/collaboration/betta/PROMPT_VERITE.md',
    'docs/collaboration/instructions/NOVO12_EXECUTION_VIAL_2026-10-15.md')
CHECKS = ("autorisation", "perimetre_provenance", "sources_lues", "contexte_suisse", "independance",
          "contrat_cours", "honnetete")


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def make_gate(actor, entries, prompts="reprise"):
    """Relevé conforme au contrat ; ``entries`` : (identifiant, chemin, explication) écrits par l'agent."""
    if prompts not in PROMPT_SETS:
        raise ValueError("jeu de Prompt inconnu : " + str(prompts))
    checks = {}
    for cid, path, why in entries:
        if cid not in CHECKS:
            raise ValueError("identifiant inconnu : " + cid)
        if not (ROOT / path).is_file() or not why.strip():
            raise ValueError(f"preuve absente ou explication vide : {path}")
        checks.setdefault(cid, []).append({"path": path, "sha256": sha(path), "explanation": why.strip()})
    missing = set(CHECKS) - set(checks)
    if missing:
        raise ValueError("contrôles manquants : " + ", ".join(sorted(missing)))
    return {"actor": actor, "verdict": "conforme", "checked_at": datetime.now(timezone.utc).isoformat(),
            "prompt_files": {f: sha(f) for f in PROMPT_SETS[prompts]},
            "checks": [{"id": c, "status": "conforme", "evidence": checks[c]} for c in CHECKS]}


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--actor", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--prompts", choices=sorted(PROMPT_SETS), default="reprise")
    p.add_argument("--check", nargs=3, action="append", metavar=("ID", "CHEMIN", "EXPLICATION"), required=True)
    a = p.parse_args()
    try:
        gate = make_gate(a.actor, a.check, a.prompts)
    except ValueError as error:
        p.error(str(error))
    out = ROOT / a.out
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(gate, ensure_ascii=False, indent=1) + "\n")
    print(out.relative_to(ROOT))


if __name__ == "__main__":
    sys.exit(main())
