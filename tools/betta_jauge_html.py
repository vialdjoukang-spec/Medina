#!/usr/bin/env python3
"""Jauge Betta survolable : un carreau par cycle, 8 leçons par fragment au survol.

Écrit organisation/progression/jauge_betta.html (instantané embarqué + rafraîchissement
direct depuis GitHub quand la page est servie hors bac à sable). Coût en jetons : nul.
Usage : python3 tools/betta_jauge_html.py [--branche <branche>] [--fragment <fichier artifact>]
"""
import json, sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "organisation/progression/jauge_betta.html"
TEMPLATE = ROOT / "tools/betta_jauge_template.html"


def etat(v):
    return v.get("state") if isinstance(v, dict) else v


def donnees():
    plan = json.loads((ROOT / "organisation/progression/plan-betta-cycles.json").read_text())
    status = json.loads((ROOT / "organisation/betta_status.json").read_text())["cycles"]
    livr = {p.name for p in ROOT.glob("livraisons/Livraison Claude/*/betta/CYCLE_*")}
    cycles = []
    for c in plan["cycles"]:
        n, lecons = c["number"], []
        for a in c["agents"]:
            for l in a["lessons"]:
                st = etat(status[str(n)]["lessons"].get(l["code"], "A_FAIRE"))
                if st == "A_FAIRE" and f"CYCLE_{n}_{l['code']}" in livr:
                    st = "EN_COURS"
                lecons.append({"code": l["code"], "titre": l["title"], "frag": a["label"], "etat": st})
        if status[str(n)].get("state") != "TRANSFERE_NOVO12":
            cycles.append({"n": n, "nom": c["name"], "lecons": lecons})
    novo_p, novo_s = ROOT / "organisation/progression/plan-novo12.json", ROOT / "organisation/novo12_status.json"
    if novo_p.exists() and novo_s.exists():
        plan, st = json.loads(novo_p.read_text()), json.loads(novo_s.read_text())["cycles"]
        livr = {p.name for p in ROOT.glob("livraisons/Livraison Claude/*/novo12/CYCLE_*")}
        for c in plan["cycles"]:
            n, lecons = c["number"], []
            for a in c["agents"]:
                for l in a["lessons"]:
                    e = etat(st[str(n)]["lessons"].get(l["code"], "A_FAIRE"))
                    if e == "A_FAIRE" and f"CYCLE_{n}_{l['code']}" in livr:
                        e = "EN_COURS"
                    lecons.append({"code": l["code"], "titre": l["title"], "frag": a["label"], "etat": e})
            cycles.append({"n": n, "nom": "Novo_12 · " + c["name"], "lecons": lecons})
    return cycles


def main():
    branche = sys.argv[sys.argv.index("--branche") + 1] if "--branche" in sys.argv else "claude/bold-edison-glmbv7"
    data = {"maj": datetime.now(timezone.utc).strftime("%d.%m.%Y %H:%M UTC"), "branche": branche, "cycles": donnees()}
    html = TEMPLATE.read_text().replace("/*DATA*/null", json.dumps(data, ensure_ascii=False))
    OUT.write_text('<!doctype html>\n<html lang="fr"><head><meta charset="utf-8">'
                   '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
                   '<style>body{margin:0}[hidden]{display:none!important}</style></head><body>\n' + html + "\n</body></html>\n")
    if "--fragment" in sys.argv:  # version sans squelette pour l'Artifact claude.ai
        Path(sys.argv[sys.argv.index("--fragment") + 1]).write_text(html)
    fait = sum(l["etat"] in ("LIVRE", "INJECTE") for c in data["cycles"] for l in c["lecons"])
    print(f"{OUT.relative_to(ROOT)} · {fait}/{sum(len(c['lecons']) for c in data['cycles'])} leçons")


if __name__ == "__main__":
    main()
