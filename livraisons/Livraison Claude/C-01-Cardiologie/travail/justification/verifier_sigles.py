#!/usr/bin/env python3
"""Contrôle les sigles d'un fragment HTML comme le fait test_v7.py.

Usage : python3 verifier_sigles.py <CODE> <fichier.html> [...]
Variable MEDINA_GLOSSAIRE_EXTRA : fichiers de glossaire provisoires (séparés par « : »),
au format de glossary/<code>.py, pris en compte en plus du glossaire du dépôt.
Affiche {} si tous les sigles sont couverts, sinon les sigles refusés.
"""
import importlib.util
import os
import pathlib
import sys

DEPOT = pathlib.Path(__file__).resolve().parents[5]
sys.path.insert(0, str(DEPOT))
import build_medina as B  # noqa: E402

for i, chemin in enumerate(filter(None, os.environ.get("MEDINA_GLOSSAIRE_EXTRA", "").split(":"))):
    spec = importlib.util.spec_from_file_location(f"glossaire_extra_{i}", chemin)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    B.G.update(module.G)

code = sys.argv[1]
src = "".join(pathlib.Path(p).read_text(encoding="utf-8") for p in sys.argv[2:])
print(B.audit(B.wrap_html(B.pareto_ratios(B.transform(src))), code))
