"""Intitulés clairs des catégories et des chapitres (exigence de Vial du 8 octobre 2026).

Les mots « autre », « sans précision », « non classé ailleurs » et « non précisé » n'apparaissent
dans aucun intitulé affiché. Les noms sont d'abord repris de `organisation/libelles_clairs.json`
quand ils y sont écrits à la main, puis nettoyés par des règles générales. Les codes CIM-10-GM
eux-mêmes ne changent pas : seul l'intitulé lisible est reformulé.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INTERDITS = re.compile(r"\bautres?\b|sans précision|non class[ée]e?s? ailleurs|non précis", re.I)

_TABLE = None

# Retraits et remplacements appliqués dans l'ordre.
_REGLES = (
    (r",?\s*non class[ée]e?s?\s+ailleurs\b", ""),
    (r",?\s*sans précision\b", ""),
    (r",?\s*non précis[ée]e?s?\b", ""),
    (r"\bd[’']autres\s+", "d’"),
    (r"\bà\s+d[’']autres\s+", "à "),
    (r"\bdes\s+autres\s+", "des "),
    (r"\bet\s+autres\b", "et apparentés"),
    (r"^Autres?\s+", ""),
    (r"\s*,\s*autres?\b", ""),
    (r"\bautres?\s+", ""),
    (r"\s{2,}", " "),
    (r"\s+([,;:])", r"\1"),
    (r"[\s,;:]+$", ""),
)


def table():
    global _TABLE
    if _TABLE is None:
        _TABLE = json.loads((ROOT / "organisation/libelles_clairs.json").read_text(encoding="utf-8"))
    return _TABLE


def nettoyer(texte):
    """Applique les règles générales, puis remet une majuscule initiale."""
    for motif, remplacement in _REGLES:
        texte = re.sub(motif, remplacement, texte, flags=re.I)
    texte = texte.strip(" ,;:")
    return texte[:1].upper() + texte[1:] if texte else texte


def bloc(code, titre):
    """Intitulé lisible d'une catégorie CIM (bloc), en une ligne."""
    return table()["blocks"].get(code) or nettoyer(titre)


def chapitre(code, titre):
    """Intitulé lisible d'un chapitre ou d'une catégorie rattachée."""
    return table()["codes"].get(code) or nettoyer(titre)
