#!/usr/bin/env python3
"""Injection canonique des leçons Betta à l'état LIVRE (instruction de Vial, 15 octobre 2026).

Pour chaque leçon LIVRE (ou les codes donnés) : copie chapters/<CODE>/ et glossary/<code>.py
vers la racine, état INJECTE + empreintes « canonical » dans organisation/betta_status.json,
ligne chapters.json (audit différé non effectué), empreinte de chapters.json dans
nosology/integrity.json. La garde tools/betta_cycle.py vérifie ensuite chaque empreinte.
Ne touche aucun fichier de la chaîne des cycles 1–30 (CYCLES_CLAUDE.json, travail/, cycle_claude).
Usage : python3 tools/betta_injecter.py [--novo] [CODE ...]   (--novo : Projet Novo_12)
"""
import hashlib, json, shutil, sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WAVE = {"S08": 6, "S05": 4, "S04": 3, "S06": 8}


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def charger(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def ecrire(rel, data, compact=False, nl=True):
    texte = json.dumps(data, ensure_ascii=False, separators=(",", ":")) if compact else json.dumps(data, ensure_ascii=False, indent=2)
    (ROOT / rel).write_text(texte + ("\n" if nl else ""), encoding="utf-8")


def main(cibles, novo=False):
    plan_rel, status_rel, flag = (("organisation/progression/plan-novo12.json", "organisation/novo12_status.json", "novo12") if novo
                                  else ("organisation/progression/plan-betta-cycles.json", "organisation/betta_status.json", "betta"))
    plan = charger(plan_rel)
    status = charger(status_rel)
    rows = charger("chapters.json")
    lecons = {l["code"]: (c["number"], l) for c in plan["cycles"] for a in c["agents"] for l in a["lessons"]}
    existants, faits = {r["code"] for r in rows}, []
    for n, cyc in status["cycles"].items():
        for code, st in cyc["lessons"].items():
            if not isinstance(st, dict) or st.get("state") != "LIVRE" or (cibles and code not in cibles):
                continue
            src = ROOT / st["dir"]
            dst_ch, gl = ROOT / "chapters" / code, src / "glossary" / f"{code.lower()}.py"
            if dst_ch.exists() or code in existants:
                sys.exit(f"{code} : déjà présent dans chapters/ ou chapters.json — arrêt")
            shutil.copytree(src / "chapters" / code, dst_ch)
            shutil.copy2(gl, ROOT / "glossary" / gl.name)
            canon = {str(p.relative_to(ROOT)): sha(p) for p in sorted(dst_ch.rglob("*")) if p.is_file()}
            canon[f"glossary/{gl.name}"] = sha(ROOT / "glossary" / gl.name)
            st.update(state="INJECTE", canonical=canon)
            cycle, l = lecons[code]
            assert cycle == int(n), f"{code} : cycle incohérent"
            rows.append({"code": code, "covers": [code], "title": l["title"], "integrated": True,
                         "owner": l["fragment"], "wave": WAVE.get(l["fragment"]), "production_cycle": cycle,
                         flag: True, "provisional_injection": True,
                         "audit_status": "audit_differe_non_effectue", "added": date.today().isoformat()})
            faits.append(code)
        if all(isinstance(v, dict) and v.get("state") == "INJECTE" for v in cyc["lessons"].values()):
            cyc["state"] = "INJECTE"
    ecrire(status_rel, status, nl=False)
    ecrire("chapters.json", rows)
    integ = charger("nosology/integrity.json")
    integ["chapters.json"] = sha(ROOT / "chapters.json")
    ecrire("nosology/integrity.json", integ, compact=True)
    print(f"{len(faits)} leçons injectées : {' '.join(faits)}")


if __name__ == "__main__":
    main(set(a for a in sys.argv[1:] if a != "--novo"), novo="--novo" in sys.argv)
