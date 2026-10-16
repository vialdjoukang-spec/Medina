#!/usr/bin/env python3
"""Vérifie que chaque « ancien » de propositions.json apparaît exactement une fois dans son fichier.
Usage (depuis la racine du worktree) : python3 docs/collaboration/ssp-v2/execution/ALPHA1-CLAUDE-E12-LANG/verification_unicite.py"""
import json, pathlib
d = pathlib.Path(__file__).parent
props = json.load(open(d / "propositions.json", encoding="utf-8"))
root = d.parents[4]
bad = 0
for p in props:
    n = (root / p["fichier"]).read_text(encoding="utf-8").count(p["ancien"])
    if n != 1:
        bad += 1
        print("KO", p["id"], n)
print(len(props), "propositions ;", bad, "erreur(s)")
raise SystemExit(1 if bad else 0)
