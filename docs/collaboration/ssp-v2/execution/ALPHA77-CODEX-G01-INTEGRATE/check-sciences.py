"""Contrôle local : mêmes assertions que audit_sciences, BASE changée explicitement.
Le test partagé original échoue car G01 est absent de sa base historique.
"""
from pathlib import Path
import importlib.util,json,subprocess,hashlib
ROOT=Path(__file__).resolve().parents[5]
spec=importlib.util.spec_from_file_location('science_gate',ROOT/'tests/audit_sciences.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
mod.BASE='3131a5cbf6cc003ead358e25152073959c53c4d9'
if __name__=='__main__':mod.main()
