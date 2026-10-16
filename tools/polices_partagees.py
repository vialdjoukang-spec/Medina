#!/usr/bin/env python3
"""Polices des pages construites : incorporées (défaut) ou fichiers communs.

Par défaut, chaque page reste autonome : les WOFF2 sont incorporés en ``data:`` (ouverture
hors ligne d'un fichier isolé). Avec ``MEDINA_POLICES_PARTAGEES=1``, les pages pointent vers
un dossier commun ``polices/`` à la racine du site (``../polices/`` depuis ``fragments/``) :
le navigateur télécharge et met en cache les six polices une seule fois pour les 24 pages.
Ce mode suppose que le dossier ``polices/`` soit publié à côté des pages. Le workflow Pages
(chemin partagé, mission d'intégration requise) devrait alors exporter la variable pour les
deux constructions et ajouter, dans « Assembler le site » :
    cp -R dist/polices _site/polices
build_index.py, exécuté dans _site, copie lui-même les polices à côté de index.html.
"""
from __future__ import annotations

import base64
import os
import shutil
from pathlib import Path

DOSSIER = 'polices'
POLICES = (
    'shell/fonts/ahn-400.woff2', 'shell/fonts/ahn-400i.woff2',
    'shell/fonts/ahn-600.woff2', 'shell/fonts/ahn-700.woff2',
    'assets/fonts/AnthropicSerif-Roman-Web.woff2', 'assets/fonts/AnthropicSerif-Italic-Web.woff2',
)


def partagees() -> bool:
    return os.environ.get('MEDINA_POLICES_PARTAGEES', '0') == '1'


def url_police(root, relatif: str, profondeur: int = 0) -> str:
    """URL CSS de la police ``relatif`` (chemin depuis la racine du dépôt).

    ``profondeur`` : nombre de dossiers entre la page et la racine du site (1 pour fragments/).
    """
    if relatif not in POLICES:
        raise ValueError('police inconnue : ' + relatif)
    if partagees():
        return '../' * profondeur + DOSSIER + '/' + Path(relatif).name
    return 'data:font/woff2;base64,' + base64.b64encode((Path(root) / relatif).read_bytes()).decode('ascii')


def copier(root, site) -> Path | None:
    """Copie les polices communes dans ``<site>/polices`` (mode partagé uniquement)."""
    if not partagees():
        return None
    dossier = Path(site) / DOSSIER
    dossier.mkdir(parents=True, exist_ok=True)
    for relatif in POLICES:
        shutil.copyfile(Path(root) / relatif, dossier / Path(relatif).name)
    return dossier
