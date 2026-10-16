#!/usr/bin/env python3
"""Inventaire exhaustif des valeurs numériques de la leçon G99 (EXIGENCE_CALCULS § 1).

Lit les 7 fichiers figés (lecture seule), extrait chaque nombre du texte visible, des attributs
aria-label et data-title, et du glossaire, avec l'identifiant HTML le plus proche (ancre), l'unité
détectée et le contexte. Écrit calculs/inventaire.json à côté de ce script.

Usage : python3 calculs/inventaire.py <racine du worktree>
"""
import html
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

FICHIERS = [
    "chapters/G99/G99_a.html", "chapters/G99/G99_b.html", "chapters/G99/G99_c.html",
    "chapters/G99/G99_d.html", "chapters/G99/G99_pop1.html", "chapters/G99/G99_pop2.html",
    "glossary/g99.py",
]

NOMBRE = re.compile(r"(?<![\w.,])(\d{1,3}(?:[   ]\d{3})+|\d+)(?:,(\d+))?")
UNITES = [
    ("pour 100 000 par an", r"\s*(?:à\s*\d+\s*)?(?:cas\s*)?pour\s*100\s*000"),
    ("sur 10 000", r"\s*sur\s*10\s*000"),
    ("pour 10 000", r"\s*pour\s*10\s*000"),
    ("%", r"\s*%"),
    ("mL", r"\s*mL\b"),
    ("µg", r"\s*µg"),
    ("mg/kg", r"\s*mg/kg"),
    ("mg", r"\s*mg\b"),
    ("heures", r"\s*(?:heures?|h)\b"),
    ("minutes", r"\s*min(?:utes?)?\b"),
    ("jours", r"\s*jours?\b"),
    ("mois", r"\s*mois\b"),
    ("ans", r"\s*ans\b"),
    ("patients", r"\s*(?:patients?|adultes|malades|cas|syndromes|hommes|femmes|personnes|lombalgiques)\b"),
    ("études", r"\s*(?:études|articles|recommandations|documents|vignettes|définitions|manifestations|variables|types|formes|stades|catégories|paliers)\b"),
]
LETTRES = re.compile(r"\b(?:[Uu]ne?|[Dd]eux|[Tt]rois|[Qq]uatre|[Cc]inq|[Ss]ix|[Ss]ept|[Hh]uit|[Nn]euf|[Dd]ix|[Tt]reize|[Qq]uinze|[Vv]ingt)\s+"
                     r"(?:pour cent|patients?|études|cas|mois|ans|heures?|semaines?|jours?|malades?|quart|tiers|paliers|"
                     r"premiers mois|recommandations|sur (?:trois|cinq|deux|dix)|minutes?|grandes|signes)\b|\bdans l’heure\b|\bla moitié\b")
CODE_CIM = re.compile(r"[A-Z]\d{2}(?:\.\d{1,2}-?)?$")


class Lecteur(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.pile = []  # (balise, ancre)
        self.morceaux = []  # (ancre, texte, nature)
        self.dans_n = 0

    def _ancre(self):
        for _, a in reversed(self.pile):
            if a:
                return a
        return "(racine)"

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        a = d.get("id") or d.get("data-pop") or (("data-k=" + d["data-k"]) if tag == "button" and "data-k" in d else None)
        if tag in ("br", "path", "rect", "circle", "img"):
            if "aria-label" in d:
                self.morceaux.append((self._ancre(), d["aria-label"], "aria"))
            return
        self.pile.append((tag, a))
        for k in ("aria-label", "data-title"):
            if k in d:
                self.morceaux.append((a or self._ancre(), d[k], k))
        if tag == "span" and d.get("class") == "n":
            self.dans_n += 1

    def handle_endtag(self, tag):
        for i in range(len(self.pile) - 1, -1, -1):
            if self.pile[i][0] == tag:
                if tag == "span" and self.dans_n:
                    self.dans_n -= 1
                del self.pile[i:]
                break

    def handle_data(self, data):
        if data.strip():
            self.morceaux.append((self._ancre(), data, "numerotation" if self.dans_n else "texte"))


def unite(apres):
    for nom, motif in UNITES:
        if re.match(motif, apres):
            return nom
    return ""


def nature(valeur, avant, apres, origine, u):
    if origine == "numerotation":
        return "numerotation"
    if re.match(r"\s*(?:janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre)\b", apres):
        return "date"
    if re.search(r"(?:fictif|N-|Cas)\s*$", avant) or re.search(r"N-$", avant):
        return "numerotation"
    if re.search(r"[A-Z]$", avant) or re.match(r"\.\d", apres) or CODE_CIM.search((avant[-1:] + valeur)):
        return "code_CIM"
    if re.search(r"(?:\b[GNMIE]\d{0,2}|G8|G9|G5|CIM-|ICD-|G )$", avant):
        return "code_CIM"
    if re.search(r"(?:Sections?|Betta|Cycle Betta|sections?)\s+(?:\d+\s+(?:à|et)\s+)?$", avant):
        return "numerotation"
    if re.search(r"(?:[Rr]acines sacrées|racines)\s+(?:\d+\s+à\s+)?$", avant):
        return "rang"
    v = valeur.replace(" ", "").replace(" ", "").replace(" ", "")
    if re.fullmatch(r"(19|20)\d{2}", v) and not u:
        return "annee_reference"
    if re.search(r"(Figure|Cas|section|sections|îlot|Type|type|e-|p-|onglet|Partie)\s*$", avant):
        return "numerotation"
    if re.search(r"\d+e\b", valeur + apres[:1]):
        return "rang"
    return "valeur"


def extraire(racine):
    sortie = []
    n = 0
    for f in FICHIERS:
        p = racine / f
        texte = p.read_text(encoding="utf-8")
        if f.endswith(".py"):
            morceaux = [("glossary/g99.py:l%d" % (i + 1), html.unescape(l), "glossaire") for i, l in enumerate(texte.splitlines())]
        else:
            lec = Lecteur()
            lec.feed(texte)
            morceaux = lec.morceaux
        for ancre, t, origine in morceaux:
            for m in NOMBRE.finditer(t):
                val = m.group(1) + ("," + m.group(2) if m.group(2) else "")
                avant, apres = t[max(0, m.start() - 40):m.start()], t[m.end():m.end() + 40]
                # Rangs ordinaux : « 2e lombaire », « 1re sacrée »
                if re.match(r"(?:e|re|er)\b", apres):
                    nat = "rang"
                    u = ""
                else:
                    u = unite(apres)
                    nat = nature(val, avant, apres, origine, u)
                n += 1
                sortie.append({
                    "id": "I%04d" % n,
                    "fichier": f,
                    "ancre": ancre,
                    "valeur": val,
                    "unite": u,
                    "nature": nat,
                    "origine": origine,
                    "contexte": re.sub(r"\s+", " ", (t[max(0, m.start() - 90):m.end() + 90])).strip(),
                    "position": len(re.sub(r"\s+", " ", t[max(0, m.start() - 90):m.start()]).lstrip()),
                })
            for m in LETTRES.finditer(t):
                n += 1
                sortie.append({
                    "id": "I%04d" % n,
                    "fichier": f,
                    "ancre": ancre,
                    "valeur": m.group(0),
                    "unite": "en lettres",
                    "nature": "valeur_en_lettres",
                    "origine": origine,
                    "contexte": re.sub(r"\s+", " ", (t[max(0, m.start() - 90):m.end() + 90])).strip(),
                    "position": len(re.sub(r"\s+", " ", t[max(0, m.start() - 90):m.start()]).lstrip()),
                })
    return sortie


def main():
    racine = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    inv = extraire(racine)
    par_nature = {}
    for e in inv:
        par_nature[e["nature"]] = par_nature.get(e["nature"], 0) + 1
    doc = {
        "mission": "ALPHA1-CLAUDE-G99-MED",
        "methode": "calculs/inventaire.py : analyse HTML (texte visible, aria-label, data-title) et lignes du glossaire ; "
                   "regex des nombres entiers et décimaux à virgule ; unité détectée sur les 40 caractères suivants ; "
                   "nature : valeur, rang (2e, 1re), code_CIM, numerotation, annee_reference ; position = rang du premier caractère de la valeur dans le contexte.",
        "total": len(inv),
        "par_nature": par_nature,
        "occurrences": inv,
    }
    out = Path(__file__).resolve().parent / "inventaire.json"
    out.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("inventaire :", len(inv), "occurrences", par_nature)


if __name__ == "__main__":
    main()
