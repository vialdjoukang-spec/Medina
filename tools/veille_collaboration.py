#!/usr/bin/env python3
"""Veille des contributions de l'autre agent MEDINA.

Usage : python3 tools/veille_collaboration.py --agent Claude|Codex [--state FICHIER] [--attendre SECONDES]

Récupère toutes les branches distantes, compare leurs têtes à l'état enregistré et signale les
branches de l'autre agent (préfixe claude/ ou codex/), ainsi que main, dont la tête a changé.
Pour chacune, liste les fichiers modifiés depuis la tête précédente et les classe : livraisons,
reçus, chapitres, consignes, autres. Sans changement, rien n'est écrit sur la sortie.
Avec --attendre, la commande boucle jusqu'au premier changement, puis s'arrête avec le code 10 :
une session peut la lancer en arrière-plan et être réveillée dès qu'une contribution arrive.
Le script ne fusionne, n'injecte et ne publie rien.
"""
import argparse
import json
import pathlib
import subprocess
import sys
import time

RACINE = pathlib.Path(__file__).resolve().parents[1]


def git(*args):
    return subprocess.run(["git", *args], cwd=RACINE, capture_output=True, text=True, check=False).stdout


def tetes():
    sortie = git("for-each-ref", "--format=%(refname:short) %(objectname)", "refs/remotes/origin")
    return dict(l.split() for l in sortie.splitlines() if l and not l.startswith("origin/HEAD"))


def classe(chemin):
    for prefixe, nom in (("livraisons/", "livraison"), ("docs/collaboration/receipts/", "reçu"),
                         ("chapters/", "chapitre"), ("docs/collaboration/", "consigne"),
                         ("organisation/", "organisation"), ("glossary/", "glossaire")):
        if chemin.startswith(prefixe):
            return nom
    return "autre"


def examiner(agent, etat):
    git("fetch", "-q", "--prune", "origin")
    autre = "codex/" if agent == "Claude" else "claude/"
    nouveau, changements = tetes(), []
    for ref, sha in sorted(nouveau.items()):
        nom = ref.removeprefix("origin/")
        if not (nom.startswith(autre) or nom == "main" or nom.startswith("codex/sciences-cs-fragments")):
            continue
        ancien = etat.get(ref)
        if ancien == sha:
            continue
        fichiers = git("diff", "--name-only", f"{ancien}..{sha}").split() if ancien else []
        groupes = {}
        for f in fichiers:
            groupes.setdefault(classe(f), []).append(f)
        changements.append({"branche": nom, "avant": ancien, "apres": sha,
                            "commits": git("log", "--oneline", f"{ancien}..{sha}").splitlines()[:30] if ancien else [],
                            "fichiers": {k: v[:200] for k, v in groupes.items()}})
    return nouveau, changements


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--agent", required=True, choices=["Claude", "Codex"])
    p.add_argument("--state", default=str(RACINE / ".git" / "veille_collaboration.json"))
    p.add_argument("--attendre", type=int, default=0)
    a = p.parse_args()
    etat_f = pathlib.Path(a.state)
    etat = json.loads(etat_f.read_text()) if etat_f.exists() else {}
    premier = not etat
    while True:
        nouveau, changements = examiner(a.agent, etat)
        etat_f.write_text(json.dumps(nouveau, indent=1))
        if premier:
            print(json.dumps({"initialisation": len(nouveau)}, ensure_ascii=False))
            premier, etat = False, nouveau
            if not a.attendre:
                return 0
        elif changements:
            print(json.dumps(changements, ensure_ascii=False, indent=1))
            return 10
        if not a.attendre:
            return 0
        etat = nouveau
        time.sleep(a.attendre)


if __name__ == "__main__":
    sys.exit(main())
