#!/usr/bin/env python3
"""Zones Compendium pré-marquées d'un cours MEDINA.

Fichier de zones : chapters/<CODE>/<CODE>_compendium.json
{
 "schema_version": 1,
 "code": "J45",
 "zones": [
  {"id": "j45-cz-symbicort", "fichier": "J45_d.html", "texte": "extrait exact du passage marqué",
   "produit": "Symbicort", "sections": ["Posologie"], "statut": "a_lire|lu",
   "consulte_le": "AAAA-MM-JJ", "url": "https://compendium.ch/fr/product/…/mpro"}
 ]
}

Usage :
  python3 tools/compendium_zones.py verifier <CODE>   # chaque zone retrouve son texte, une seule fois ; statut et date cohérents
  python3 tools/compendium_zones.py a_lire  <CODE>    # liste les zones encore à lire, avec la commande de lecture
Code de sortie 1 si une zone est introuvable, ambiguë ou incomplète. Le script ne modifie aucun fichier.
"""
import json, pathlib, sys

RACINE = pathlib.Path(__file__).resolve().parents[1]


def charger(code):
    p = RACINE / "chapters" / code / f"{code}_compendium.json"
    if not p.exists():
        sys.exit(f"Aucun fichier de zones : {p.relative_to(RACINE)}")
    return json.loads(p.read_text(encoding="utf-8"))


def verifier(code):
    d, erreurs = charger(code), []
    for z in d.get("zones", []):
        f = RACINE / "chapters" / code / z["fichier"]
        n = f.read_text(encoding="utf-8").count(z["texte"]) if f.exists() else -1
        if n != 1:
            erreurs.append(f"{z['id']} : texte trouvé {n} fois dans {z['fichier']}")
        if z.get("statut") == "lu" and not (z.get("consulte_le") and z.get("url")):
            erreurs.append(f"{z['id']} : statut « lu » sans date ou sans URL")
        if not z.get("produit") or not z.get("sections"):
            erreurs.append(f"{z['id']} : produit ou sections manquants")
    print(json.dumps({"code": code, "zones": len(d.get("zones", [])), "erreurs": erreurs}, ensure_ascii=False, indent=1))
    return 1 if erreurs else 0


def a_lire(code):
    for z in charger(code).get("zones", []):
        if z.get("statut") != "lu":
            print(f"{z['id']} | {z['produit']} | {', '.join(z['sections'])}")
            print(f"  node tools/compendium_fi.cjs \"{z['produit']}\" {' '.join(z['sections'])}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] not in ("verifier", "a_lire"):
        sys.exit(__doc__)
    sys.exit({"verifier": verifier, "a_lire": a_lire}[sys.argv[1]](sys.argv[2]))
