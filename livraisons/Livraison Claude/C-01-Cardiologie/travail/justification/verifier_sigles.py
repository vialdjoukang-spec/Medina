#!/usr/bin/env python3
"""Contrôle les sigles d'un fragment HTML comme le fait test_v7.py.

Usage : python3 verifier_sigles.py <CODE> <fichier.html> [...]
Affiche {} si tous les sigles sont couverts par le glossaire, sinon les sigles refusés.
"""
import pathlib
import sys

DEPOT = pathlib.Path(__file__).resolve().parents[5]
sys.path.insert(0, str(DEPOT))
import build_medina as B  # noqa: E402

code = sys.argv[1]
src = "".join(pathlib.Path(p).read_text(encoding="utf-8") for p in sys.argv[2:])
print(B.audit(B.wrap_html(B.pareto_ratios(B.transform(src))), code))
