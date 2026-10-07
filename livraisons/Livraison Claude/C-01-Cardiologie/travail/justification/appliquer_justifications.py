#!/usr/bin/env python3
"""Applique une passe de justification systématique à un cours MEDINA.

Usage : python3 appliquer_justifications.py <CODE> <dossier_resultats> [--ecrire]

<dossier_resultats> contient, pour le cours :
  edits/<F>.json      compléments proposés [{id, old, new, source}] ;
  verdicts/<F>.json   verdicts du vérificateur [{id, decision, new_final, old_reel?, fichier_reel?}] ;
  jobs/<cle>[__Pn].json  fenêtre : {cle, titre, action, fichier_cible, ancres:[{file, id, old, label}]} ;
  out/<cle>[__Pn].html   template complet (creer) ou rubriques à ajouter (completer) ;
  out/<cle>[__Pn].json   {ancres_retirees:[{id}], label_modifies:[{id, label}]}.
La base est la copie livrée par Claude si elle existe, sinon la source canonique.
Ordre : compléments du texte, mots verts, fenêtres, puis nettoyage des rubriques Source.
Sans --ecrire, rien n'est écrit et le bilan est affiché.
"""
import json
import pathlib
import re
import sys

ICI = pathlib.Path(__file__).resolve().parent
LIVR = ICI.parents[1]
DEPOT = LIVR.parents[2]

NOM = r"(?:Mc|Mac|de |van der |van |Van )?[A-ZÀ-Ý][a-zà-ÿ’'\-]+(?:[ -][A-ZÀ-Ý][a-zà-ÿ’'\-]+)?"
AUTEUR = NOM + r" [A-Z]{1,3}(?![\w])"
LISTE = re.compile(rf"({NOM}) [A-Z]{{1,3}}(?:, {AUTEUR})+(?:,? et al\.?| et coll\.?)?")
SEUL = re.compile(rf"({NOM}) [A-Z]{{1,3}}(?![\w’'])(?=[ ,.;:)])")


def nettoyer_sources(texte):
    """Retire les initiales d'auteurs, que l'audit des sigles refuse."""
    def corrige(m):
        p = LISTE.sub(lambda x: x.group(1) + " et al.", m.group(2))
        p = SEUL.sub(lambda x: x.group(1), p)
        p = p.replace("et al. et al.", "et al.").replace("et al.,  et al.", "et al.")
        return m.group(1) + p + m.group(3)
    texte = re.sub(r'(<div class="lab">Sources?(?: complémentaires?)?</div><p>)(.*?)(</p>)', corrige, texte, flags=re.S)
    return texte.replace("et al..", "et al.").replace("et coll..", "et coll.")


def dans_balise(texte, pos):
    if texte.rfind("<", 0, pos) > texte.rfind(">", 0, pos):
        return True
    ouvert = texte.rfind("<button", 0, pos)
    return ouvert != -1 and texte.find("</button>", ouvert) > pos


def main():
    code, res = sys.argv[1], pathlib.Path(sys.argv[2])
    ecrire = "--ecrire" in sys.argv
    copies = LIVR / "sources" / "chapters" / code
    canon = DEPOT / "chapters" / code
    noms = sorted(p.stem for p in canon.glob("*.html"))

    def lire(n):
        c = copies / f"{n}.html"
        return (c if c.exists() else canon / f"{n}.html").read_text(encoding="utf-8")

    textes = {n: lire(n) for n in noms}
    bilan = {"textes_appliques": 0, "textes_rejetes": 0, "textes_echecs": [], "ancres": 0,
             "ancres_retirees": 0, "ancres_echecs": [], "fenetres_creees": [], "fenetres_completees": [],
             "fenetres_echecs": []}

    for n in noms:
        prop = res / "edits" / f"{n}.json"
        if not prop.exists():
            continue
        initial = {x["id"]: x for x in json.loads(prop.read_text())}
        verd = res / "verdicts" / f"{n}.json"
        verdicts = json.loads(verd.read_text()) if verd.exists() else []
        if not verdicts:
            bilan["textes_echecs"].append((n, "aucun verdict : non appliqué"))
        for v in verdicts:
            x = initial.get(v["id"])
            if x is None or v["decision"] == "rejeter":
                bilan["textes_rejetes"] += 1
                continue
            g = re.match(rf"{code}_[\w]+", v.get("fichier_reel") or n).group(0)
            old, new = v.get("old_reel") or x["old"], v.get("new_final") or x["new"]
            if textes[g].count(old) != 1:
                bilan["textes_echecs"].append((v["id"], "old absent ou multiple"))
                continue
            textes[g] = textes[g].replace(old, new, 1)
            bilan["textes_appliques"] += 1

    completions = {}
    for job in sorted((res / "jobs").glob("*.json")):
        w = json.loads(job.read_text())
        cle, tag = w["cle"], job.stem
        html_f, meta_f = res / "out" / f"{tag}.html", res / "out" / f"{tag}.json"
        if not html_f.exists():
            bilan["fenetres_echecs"].append(tag + " : HTML absent")
            continue
        meta = json.loads(meta_f.read_text()) if meta_f.exists() else {}
        if meta.get("fusionnee_dans"):
            bilan["fenetres_echecs"].append(tag + " fusionnée dans " + meta["fusionnee_dans"])
        retirees = {a["id"] for a in meta.get("ancres_retirees", [])}
        labels = {a["id"]: a["label"] for a in meta.get("label_modifies", [])}
        cible_cle = meta.get("fusionnee_dans") or cle
        for a in w["ancres"]:
            if a["id"] in retirees:
                bilan["ancres_retirees"] += 1
                continue
            label = labels.get(a["id"], a["label"])
            f = re.match(rf"{code}_[\w]+", a["file"]).group(0)
            t = textes[f]
            debut = t.find(a["old"])
            if debut != -1:
                pos = t.find(label, debut, debut + len(a["old"]))
            else:
                occ = [m.start() for m in re.finditer(re.escape(label), t)]
                pos = occ[0] if len(occ) == 1 else -1
            if not label or pos == -1 or dans_balise(t, pos):
                bilan["ancres_echecs"].append((a["id"], cle, label))
                continue
            textes[f] = t[:pos] + f'<button class="w" data-k="{cible_cle}">{label}</button>' + t[pos + len(label):]
            bilan["ancres"] += 1
        if meta.get("fusionnee_dans"):
            continue
        html = html_f.read_text(encoding="utf-8").strip()
        if w["action"] == "creer":
            cible = re.match(rf"{code}_[\w]+", w["fichier_cible"]).group(0)
            if any(f'data-pop="{cle}"' in t for t in textes.values()):
                bilan["fenetres_echecs"].append(cle + " : clé déjà présente")
                continue
            textes[cible] = textes[cible].rstrip() + "\n" + html + "\n"
            bilan["fenetres_creees"].append(cle)
        else:
            completions.setdefault(cle, []).append(html)

    for cle, morceaux in completions.items():
        for n, t in textes.items():
            m = re.search(rf'<template data-pop="{re.escape(cle)}"[^>]*>.*?(</template>)', t, re.S)
            if m:
                textes[n] = t[:m.start(1)].rstrip() + "\n" + "\n".join(morceaux) + "\n" + t[m.start(1):]
                bilan["fenetres_completees"].append(cle)
                break
        else:
            bilan["fenetres_echecs"].append(cle + " : fenêtre à compléter introuvable")

    textes = {n: nettoyer_sources(t) for n, t in textes.items()}
    if ecrire:
        copies.mkdir(parents=True, exist_ok=True)
        for n, t in textes.items():
            if t != lire(n) or (copies / f"{n}.html").exists():
                (copies / f"{n}.html").write_text(t, encoding="utf-8")
    resume = {k: (len(v) if isinstance(v, list) and k.startswith("fenetres_c") else v) for k, v in bilan.items()}
    print(json.dumps(resume, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
