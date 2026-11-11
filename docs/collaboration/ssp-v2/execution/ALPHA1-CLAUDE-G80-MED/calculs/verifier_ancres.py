#!/usr/bin/env python3
"""Vérifie que chaque bloc « ancien » des propositions figure exactement une fois dans le fichier source visé.
Usage : python3 calculs/verifier_ancres.py <racine_du_worktree>  ; sortie : calculs/ancres.json"""
import json, re, sys
from pathlib import Path
ICI = Path(__file__).parent
racine = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
res = []
for p in sorted((ICI.parent / "propositions").glob("*.html")):
    s = p.read_text(encoding="utf-8")
    for m in re.finditer(r"<!-- *\d+\. *((?:chapters|glossary)/[^,\s]+)[^>]*-->\s*<!-- ancien -->\n(.*?)\n<!-- nouveau -->", s, re.S):
        cible, ancien = m.group(1), m.group(2)
        n = (racine / cible).read_text(encoding="utf-8").count(ancien)
        res.append({"proposition": p.name, "fichier": cible, "ancien": ancien[:120], "occurrences": n, "ok": n == 1})
(ICI / "ancres.json").write_text(json.dumps({"total": len(res), "ok": sum(r["ok"] for r in res), "blocs": res}, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(res), "blocs ;", sum(r["ok"] for r in res), "uniques")
for r in res:
    if not r["ok"]:
        print("ECHEC", r)
