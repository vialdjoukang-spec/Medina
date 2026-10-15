#!/usr/bin/env python3
"""Projet Novo_12 (Vial, 15 octobre 2026) : cycles de 12 leçons, 4 fragments × 3 leçons.

Reprend le reliquat Betta non injecté (cycles 42–47, sauf C72 qui reste au cycle 41),
puis toutes les leçons fédérales (étoile SSP/PROFILES) non programmées des autres
fragments, dans l'ordre de production. Exclut tout code des cycles 1–30 (tétrade),
tout code injecté (chapters.json) et tout code déjà couvert.
Usage : python3 tools/build_novo12_plan.py [--pdf]
"""
import html, json, subprocess, sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "organisation/progression/plan-novo12"
FIRST = 42
PAR_FRAGMENT, FRAGMENTS_PAR_CYCLE = 3, 4


def charger(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def build():
    ordre = charger("organisation/fragments.json")
    ordre = ordre if isinstance(ordre, list) else ordre.get("fragments", list(ordre.values()))
    labels = {f["id"]: f["label"] for f in ordre}
    tet = charger("organisation/plan_tetrade_30_cycles.json")
    tetrade = {ch[0] for s in tet["systems"] for ch in s["chapters"]}
    rows = charger("chapters.json")
    pris = {r["code"] for r in rows} | {c for r in rows for c in r.get("covers", [])}
    betta = charger("organisation/progression/plan-betta-cycles.json")
    status = charger("organisation/betta_status.json")["cycles"]
    etat = lambda n, c: (lambda v: v.get("state") if isinstance(v, dict) else v)(status[str(n)]["lessons"].get(c))
    file = {fid: [] for fid in labels}
    deja = set()
    for c in betta["cycles"]:  # reliquat Betta : leçons encore A_FAIRE
        for a in c["agents"]:
            for l in a["lessons"]:
                deja.add(l["code"])
                if etat(c["number"], l["code"]) == "A_FAIRE":
                    file[l["fragment"]].append({"code": l["code"], "title": l["title"], "block": l["block"], "origine": f"Betta C{c['number']}"})
    for fid in labels:
        try:
            lessons = charger(f"nosology/fragments/{fid}.json")["lessons"]
        except FileNotFoundError:
            continue
        for l in lessons:
            code = l["code"]
            if ("." in code or not l.get("gold_star", {}).get("enabled") or l.get("state") == "filled"
                    or code in tetrade | pris | deja):
                continue
            file[fid].append({"code": code, "title": l["title"], "block": l.get("block", ""), "origine": "fédéral non programmé"})
    queue = ["S08", "S05"] + [fid for fid in labels if fid not in ("S08", "S05")]
    queue = [fid for fid in queue if file[fid]]
    cycles, n = [], FIRST
    while any(file[f] for f in queue):
        agents = []
        cible = PAR_FRAGMENT * FRAGMENTS_PAR_CYCLE
        while (len(agents) < FRAGMENTS_PAR_CYCLE or sum(len(a["lessons"]) for a in agents) < cible) and any(file[f] for f in queue):
            utilises = {a["fragment"] for a in agents}
            libres = [f for f in queue if file[f] and f not in utilises] or [f for f in queue if file[f]]
            fid = libres[0]
            reste = cible - sum(len(a["lessons"]) for a in agents)
            pris3 = [file[fid].pop(0) for _ in range(min(PAR_FRAGMENT, len(file[fid]), reste))]
            agents.append({"id": f"N{n}-A{len(agents) + 1}-{fid}", "fragment": fid, "label": labels[fid],
                           "research_model": "Opus 5.5", "writing_model": "Sonnet 5.5",
                           "lessons": [dict(l, order=j, fragment=fid, label=labels[fid]) for j, l in enumerate(pris3, 1)]})
        noms = []
        for a in agents:
            court = "-".join(a["label"].split("-")[:2])
            if court not in noms:
                noms.append(court)
        cycles.append({"number": n, "name": " · ".join(noms), "agents": agents,
                       "lessons": sum(len(a["lessons"]) for a in agents)})
        n += 1
    return {"id": "novo12", "date": date.today().isoformat(), "first": FIRST, "last": n - 1,
            "rule": "12 leçons par cycle : 4 fragments × 3 leçons ; une seule poussée et un seul déploiement par cycle ; prompt de vérité en entrée ; audit différé, jamais déclaré réalisé.",
            "total_lessons": sum(c["lessons"] for c in cycles), "cycles": cycles}


def page(plan):
    e = html.escape
    lignes = "".join(
        f"<section><h2>Cycle {c['number']} <small>{c['lessons']} leçons</small></h2><div class='g'>" +
        "".join(f"<div class='a'><h3>{e(a['label'])}</h3><ol>" +
                "".join(f"<li><b>{e(l['code'])}</b> {e(l['title'])}<i>{e(l['origine'])}</i></li>" for l in a["lessons"]) +
                "</ol></div>" for a in c["agents"]) + "</div></section>" for c in plan["cycles"])
    return f"""<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>Projet Novo_12</title><style>
@page{{size:A4;margin:14mm}} body{{font:10pt/1.4 "Atkinson Hyperlegible Next","Atkinson Hyperlegible",Georgia,serif;color:#17231c}}
h1{{color:#1f3428;margin:0 0 4px}} .lead{{color:#5b6a60;margin:0 0 14px}} section{{break-inside:avoid;margin:0 0 10px;border-top:2px solid #1f3428;padding-top:4px}}
h2{{font-size:12pt;margin:0 0 4px;color:#1f3428}} h2 small{{color:#5b6a60;font-weight:400}} .g{{display:grid;grid-template-columns:repeat(4,1fr);gap:6px}}
.a{{background:#f3f5f2;border-radius:6px;padding:5px 7px}} h3{{font-size:9pt;margin:0 0 3px}} ol{{margin:0;padding-left:14px}} li{{font-size:8.5pt;margin:0 0 2px}}
li i{{display:block;color:#5b6a60;font-size:7.5pt}} table{{border-collapse:collapse;margin:0 0 14px}} td,th{{border:1px solid #c9d2cb;padding:3px 6px;font-size:9pt}}
</style></head><body><h1>Projet Novo_12</h1><p class="lead">MEDINA · réorganisation du {plan['date']} · cycles {plan['first']} à {plan['last']} · {plan['total_lessons']} leçons</p>
<table><tr><th>Règle</th><td>{e(plan['rule'])}</td></tr><tr><th>Agents</th><td>4 agents par cycle, un fragment chacun, 3 leçons l'une après l'autre : recherche Opus 5.5 → porte de vérité (betta_verite.py) → rédaction Sonnet 5.5.</td></tr>
<tr><th>Publication</th><td>Injection directe des 12 leçons, une PR, une fusion, un seul déploiement GitHub Pages par cycle.</td></tr>
<tr><th>Exclusions</th><td>Codes des cycles 1–30 (chaîne tétrade), leçons déjà injectées, C72 (complétée dans Betta C41).</td></tr></table>
{lignes}</body></html>"""


def main():
    plan = build()
    OUT.with_suffix(".json").write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT.with_suffix(".html").write_text(page(plan), encoding="utf-8")
    if "--pdf" in sys.argv:  # Chromium préinstallé, sans module Python
        chrome = next(Path("/opt/pw-browsers").glob("chromium-*/chrome-linux*/chrome"))
        subprocess.run([str(chrome), "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                        f"--print-to-pdf={OUT.with_suffix('.pdf')}", OUT.with_suffix(".html").as_uri()],
                       check=True, capture_output=True, timeout=180)
    print(f"Novo_12 : cycles {plan['first']}–{plan['last']}, {plan['total_lessons']} leçons")


if __name__ == "__main__":
    main()
