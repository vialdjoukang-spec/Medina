#!/usr/bin/env python3
"""Porte de vérité Betta : contrôle d'un dossier de recherche avant rédaction.

Usage : python3 tools/betta_verite.py "<dossier CYCLE_<n>_<CODE>>" [...]
Vérifie, selon docs/collaboration/betta/PROMPT_VERITE.md : matrice de complétude
complète (20 rubriques, statut ✔/∅/LACUNE), références [Sx] toutes présentes dans
sources.json, champs de traçabilité, au moins une source suisse, aucune
recommandation américaine utilisée comme fondement sans être signalée.
"""
import json, re, sys
from pathlib import Path

RUBRIQUES = 20
CHAMPS = ("id", "url", "titre", "editeur", "version_annee", "date_consultation", "section_page")
SUISSE = re.compile(r"\.ch\b|swissmedic|compendium|pharmavista|smf|revue médicale suisse|ofsp|bag\b|suva|swissnoso", re.I)
USA = re.compile(r"acc\.org|heart\.org|idsociety|uspreventiveservices|aafp\.org|acog\.org|ada\.org/|diabetesjournals", re.I)


def controler(dossier):
    d = Path(dossier)
    code = d.name.split("_")[-1]
    try:
        texte = (d / "recherche.md").read_text(encoding="utf-8")
        sources = json.loads((d / "sources.json").read_text(encoding="utf-8"))["sources"]
    except (OSError, ValueError, KeyError) as e:
        return [f"dossier illisible : {e}"]
    return controler_contenu(texte, sources, code)


def controler_contenu(texte, sources, code):
    """Contrôle pur réutilisable par les gardes Git, sans attestation de lecture."""
    err = []
    if not isinstance(sources, list) or not all(isinstance(s, dict) for s in sources):
        return ["sources : liste d'objets requise"]
    bloc = re.search(r"^## Matrice de complétude\s*$(.*?)(?=^## |\Z)", texte, re.M | re.S)
    if not bloc:
        err.append("section « ## Matrice de complétude » absente")
    else:
        lignes = [l for l in bloc.group(1).splitlines() if l.startswith("|") and not re.match(r"\|\s*[-:]", l)]
        lignes = [l for l in lignes if not re.search(r"\|\s*rubrique\s*\|", l, re.I)]
        if len(lignes) < RUBRIQUES:
            err.append(f"matrice : {len(lignes)}/{RUBRIQUES} rubriques")
        for l in lignes:
            cases = [c.strip() for c in l.strip("|").split("|")]
            if len(cases) < 3 or not re.match(r"^(✔|∅|LACUNE)", cases[1]):
                err.append(f"matrice : statut invalide → {l[:70]}")
            elif cases[1].startswith("✔") and not re.search(r"S\d+", cases[2]):
                err.append(f"matrice : rubrique couverte sans source → {cases[0][:50]}")
    ids = {s.get("id") for s in sources}
    for s in sources:
        manque = [c for c in CHAMPS if not s.get(c)]
        if manque:
            err.append(f"{s.get('id', '?')} : champs manquants {manque}")
    cites = set(re.findall(r"\[(S\d+)\]", texte)) | {m for g in re.findall(r"\[((?:S\d+[ ,;]*)+)\]", texte) for m in re.findall(r"S\d+", g)}
    if cites - ids:
        err.append(f"références absentes de sources.json : {sorted(cites - ids)}")
    if not any(SUISSE.search(f"{s.get('url', '')} {s.get('editeur', '')} {s.get('titre', '')}") for s in sources):
        err.append("aucune source suisse")
    for s in sources:
        if USA.search(s.get("url", "")) and "américain" not in (s.get("limites") or "").lower():
            err.append(f"{s['id']} : source américaine non signalée dans « limites »")
    if not re.search(re.escape(code) + r"\.\d", texte) and not re.search(r"sans subdivision|pas de sous-code", texte, re.I):
        err.append(f"aucun sous-code {code}.x cité ni absence de subdivision déclarée")
    return err


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    echec = False
    for dossier in sys.argv[1:]:
        err = controler(dossier)
        echec |= bool(err)
        print(f"{'VÉRITÉ OK' if not err else 'VÉRITÉ ÉCHEC'} · {Path(dossier).name}")
        for e in err:
            print("  -", e)
    sys.exit(1 if echec else 0)
