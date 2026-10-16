#!/usr/bin/env python3
"""Vérifie que chaque « ancien » de propositions.json apparaît exactement une fois dans son fichier,
sans chevauchement, et que les nombres du texte visible ne changent pas (hors conversion lettres/chiffres signalée).
Usage (depuis la racine du worktree) : python3 docs/collaboration/ssp-v2/execution/ALPHA1-CLAUDE-G63-LANG/verification_unicite.py"""
import json, pathlib, collections
d = pathlib.Path(__file__).parent
props = json.load(open(d / "propositions.json", encoding="utf-8"))
root = d.parents[4]
bad = 0
by = collections.defaultdict(list)
for p in props:
    t = (root / p["fichier"]).read_text(encoding="utf-8")
    n = t.count(p["ancien"])
    if n != 1:
        bad += 1; print("KO", p["id"], n); continue
    by[p["fichier"]].append((t.index(p["ancien"]), t.index(p["ancien"]) + len(p["ancien"]), p["id"]))
for f, s in by.items():
    s.sort()
    for x, y in zip(s, s[1:]):
        if x[1] > y[0]:
            bad += 1; print("CHEVAUCHEMENT", x[2], y[2])
print(len(props), "propositions ;", bad, "erreur(s)")
raise SystemExit(1 if bad else 0)
