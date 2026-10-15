#!/usr/bin/env python3
"""Jauge verte permanente des cycles Betta (ligne d'état Claude Code, coût nul en jetons)."""
import json, os, sys
from pathlib import Path
root = Path(os.environ.get("CLAUDE_PROJECT_DIR") or Path(__file__).resolve().parents[1])
try:
    sys.stdin.read() if not sys.stdin.isatty() else None
    c = json.loads((root / "organisation/betta_status.json").read_text())["cycles"]
except Exception:
    print("MEDINA Betta · jauge indisponible"); sys.exit()
done = [n for n, v in c.items() if v["state"] in ("LIVRE", "INJECTE")]
cur = next((n for n, v in c.items() if v["state"] not in ("LIVRE", "INJECTE")), None)
les = sum(s in ("LIVRE", "INJECTE") or isinstance(s, dict) for v in c.values() for s in v["lessons"].values())
tot = sum(len(v["lessons"]) for v in c.values())
bar = "".join("✅" if v["state"] in ("LIVRE", "INJECTE") else ("🟩" if n == cur else "⬜") for n, v in c.items())
G, R = "\033[1;32m", "\033[0m"
print(f"{G}MEDINA Betta {len(done)}/{len(c)} cycles · {les}/{tot} leçons{R} {bar}" + (f" {G}▶ C{cur}{R}" if cur else f" {G}TERMINÉ{R}"))
