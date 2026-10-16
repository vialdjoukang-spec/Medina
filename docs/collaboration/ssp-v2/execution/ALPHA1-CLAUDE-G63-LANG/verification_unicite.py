#!/usr/bin/env python3
"""Vérifie, pour propositions.json : (1) chaque « ancien » apparaît exactement une fois dans son fichier ;
(2) aucun chevauchement ; (3) comparaison des valeurs numériques entre « ancien » et « nouveau » (même multiset
de nombres écrits en chiffres, balises exclues) : les écarts sont listés. Un écart n'est toléré que s'il est justifié
(ici : conversion « deux à trois » en « 2 à 3 », G63-LANG-d-05).
Usage (depuis la racine du worktree) : python3 docs/collaboration/ssp-v2/execution/ALPHA1-CLAUDE-G63-LANG/verification_unicite.py"""
import json, pathlib, collections, re
d = pathlib.Path(__file__).parent
props = json.load(open(d / "propositions.json", encoding="utf-8"))
root = d.parents[4]
bad = 0
by = collections.defaultdict(list)
nums = lambda s: collections.Counter(re.findall(r"\d+(?:[.,]\d+)?", re.sub(r"<[^>]+>", " ", s)))
ecarts = []
for p in props:
    t = (root / p["fichier"]).read_text(encoding="utf-8")
    n = t.count(p["ancien"])
    if n != 1:
        bad += 1; print("KO", p["id"], n); continue
    i = t.index(p["ancien"])
    by[p["fichier"]].append((i, i + len(p["ancien"]), p["id"]))
    a, b = nums(p["ancien"]), nums(p["nouveau"])
    if a != b:
        ecarts.append((p["id"], dict(a - b), dict(b - a)))
for f, s in by.items():
    s.sort()
    for x, y in zip(s, s[1:]):
        if x[1] > y[0]:
            bad += 1; print("CHEVAUCHEMENT", x[2], y[2])
for e in ecarts:
    print("ECART NOMBRES", e[0], "retirés:", e[1], "ajoutés:", e[2])
print(len(props), "propositions ;", bad, "erreur(s) ;", len(ecarts), "écart(s) numérique(s)")
raise SystemExit(1 if bad else 0)
