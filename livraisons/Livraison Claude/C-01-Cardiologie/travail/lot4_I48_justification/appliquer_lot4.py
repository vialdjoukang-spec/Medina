#!/usr/bin/env python3
"""Applique le lot 4 (justification d'I48) aux copies livrées par Claude.

Usage : python3 appliquer_lot4.py <dossier_resultats> [--ecrire]

<dossier_resultats> contient :
  jobs/<cle>.json        plan de chaque fenêtre (clé, action, fichier cible, ancres) ;
  out/<cle>.html, .json  fenêtre vérifiée (template complet ou rubriques à ajouter) ;
  inline_out/<F>.json    verdicts sur les compléments intégrés au texte ;
  inline/<F>.json        propositions initiales (old, new).
Sans --ecrire, le script n'écrit rien et affiche le bilan.
Ordre : compléments du texte, puis mots verts, puis fenêtres.
"""
import json
import pathlib
import re
import sys

ICI = pathlib.Path(__file__).resolve().parent
LIVR = ICI.parents[1]
COPIES = LIVR / "sources" / "chapters" / "I48"
DEPOT = LIVR.parents[2]
FICHIERS = ["I48_a", "I48_b", "I48_c", "I48_d", "I48_pop1", "I48_pop2", "I48_pop3", "I48_pop4"]


def lire(nom):
    copie = COPIES / f"{nom}.html"
    return (copie if copie.exists() else DEPOT / "chapters" / "I48" / f"{nom}.html").read_text(encoding="utf-8")


def dans_balise(texte, pos):
    """Vrai si pos se trouve dans une balise ou dans un bouton existant."""
    if texte.rfind("<", 0, pos) > texte.rfind(">", 0, pos):
        return True
    ouvert = texte.rfind('<button', 0, pos)
    return ouvert != -1 and texte.find("</button>", ouvert) > pos


def main():
    res = pathlib.Path(sys.argv[1])
    ecrire = "--ecrire" in sys.argv
    textes = {f: lire(f) for f in FICHIERS}
    bilan = {"inline_appliques": 0, "inline_rejetes": 0, "inline_echecs": [],
             "ancres": 0, "ancres_retirees": 0, "ancres_echecs": [],
             "fenetres_creees": [], "fenetres_completees": [], "fenetres_absentes": []}

    # 1. Compléments intégrés au texte.
    for f in FICHIERS:
        prop = res / "inline" / f"{f}.json"
        verd = res / "inline_out" / f"{f}.json"
        if not prop.exists():
            continue
        initial = {x["id"]: x for x in json.loads(prop.read_text())["inline"]}
        for v in json.loads(verd.read_text()) if verd.exists() else []:
            x = initial.get(v["id"])
            if x is None or v["decision"] == "rejeter":
                bilan["inline_rejetes"] += 1
                continue
            old = v.get("old_reel") or x["old"]
            new = v.get("new_final") or x["new"]
            g = v.get("fichier_reel") or f
            if textes[g].count(old) != 1:
                bilan["inline_echecs"].append((v["id"], "old absent ou multiple"))
                continue
            textes[g] = textes[g].replace(old, new, 1)
            bilan["inline_appliques"] += 1

    # 2. Mots verts et 3. fenêtres.
    for job in sorted((res / "jobs").glob("*.json")):
        w = json.loads(job.read_text())
        cle = w["cle"]
        html_f, meta_f = res / "out" / f"{cle}.html", res / "out" / f"{cle}.json"
        if not html_f.exists():
            bilan["fenetres_absentes"].append(cle)
            continue
        meta = json.loads(meta_f.read_text()) if meta_f.exists() else {}
        retirees = {a["id"] for a in meta.get("ancres_retirees", [])}
        labels = {a["id"]: a["label"] for a in meta.get("label_modifies", [])}
        for a in w["ancres"]:
            if a["id"] in retirees:
                bilan["ancres_retirees"] += 1
                continue
            label = labels.get(a["id"], a["label"])
            t = textes[a["file"]]
            debut = t.find(a["old"])
            if debut != -1:
                pos = t.find(label, debut, debut + len(a["old"]))
            else:
                occ = [m.start() for m in re.finditer(re.escape(label), t)]
                pos = occ[0] if len(occ) == 1 else -1
            if not label or pos == -1 or dans_balise(t, pos):
                bilan["ancres_echecs"].append((a["id"], cle, label))
                continue
            bouton = f'<button class="w" data-k="{cle}">{label}</button>'
            textes[a["file"]] = t[:pos] + bouton + t[pos + len(label):]
            bilan["ancres"] += 1
        html = html_f.read_text(encoding="utf-8").strip()
        cible = w.get("fichier_reel") or w["fichier_cible"]
        t = textes[cible]
        if w["action"] == "creer":
            if f'data-pop="{cle}"' in t:
                bilan["fenetres_absentes"].append(cle + " (déjà présente)")
                continue
            textes[cible] = t.rstrip() + "\n" + html + "\n"
            bilan["fenetres_creees"].append(cle)
        else:
            m = re.search(rf'<template data-pop="{re.escape(cle)}"[^>]*>.*?(</template>)', t, re.S)
            if not m:
                bilan["fenetres_absentes"].append(cle + " (cible introuvable)")
                continue
            textes[cible] = t[:m.start(1)].rstrip() + "\n" + html + "\n" + t[m.start(1):]
            bilan["fenetres_completees"].append(cle)

    if ecrire:
        for f, t in textes.items():
            if t != lire(f):
                (COPIES / f"{f}.html").write_text(t, encoding="utf-8")
    print(json.dumps(bilan, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
