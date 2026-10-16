#!/usr/bin/env python3
"""Images des gabarits de cours : dédoublonnage et WebP sans perte, à la construction.

Les cours (chapters/, en lecture seule) incorporent leurs figures en URI ``data:image/...``.
Une même figure figure souvent dans le cours et dans ses fenêtres ; gzip ne la
dédoublonne pas (fenêtre de 32 ko). ``extraire`` remplace chaque URI par un jeton
``@mdn-img-N@`` et renvoie la table des images uniques ; le chargeur de build_front.py
restitue les URI avant d'insérer les gabarits, si bien que le HTML final est celui
d'origine, à l'encodage d'image près.

WebP : uniquement GIF fixes et PNG sans profil colorimétrique, encodés sans perte et
retenus seulement si le décodage redonne exactement les mêmes pixels RGBA et si le
gain dépasse ``GAIN_MIN``. Sans Pillow (ou sans WebP), les images restent d'origine.
Un cache disque (``MEDINA_CACHE_WEBP``) évite de réencoder entre les fragments.
"""
from __future__ import annotations

import base64
import hashlib
import io
import os
import re
import tempfile
from pathlib import Path

JETON = '@mdn-img-%d@'
JETON_RE = re.compile(r'@mdn-img-\d+@')
URI_IMAGE = re.compile(r'data:image/(gif|png|jpeg|webp);base64,([A-Za-z0-9+/]+={0,2})')
TAILLE_MIN = 1024          # caractères base64 : les petites icônes restent en place
GAIN_MIN = 0.05            # WebP retenu seulement s'il gagne au moins 5 %
PARAMETRES_WEBP = {'lossless': True, 'quality': 75, 'method': 4, 'exact': True}
VERSION_CACHE = 'v1-q75-m4-exact'


def _pillow():
    try:
        from PIL import Image, ImageChops, features
    except Exception:
        return None
    try:
        if not features.check('webp'):
            return None
    except Exception:
        return None
    return Image, ImageChops


def _dossier_cache() -> Path | None:
    valeur = os.environ.get('MEDINA_CACHE_WEBP')
    if valeur == '0':
        return None
    dossier = Path(valeur) if valeur else Path(tempfile.gettempdir()) / 'medina-cache-webp'
    try:
        dossier.mkdir(parents=True, exist_ok=True)
    except OSError:
        return None
    return dossier


def webp_identique(donnees: bytes, genre: str, pil=None) -> bytes | None:
    """WebP sans perte aux pixels identiques, ou None si non applicable ou sans gain."""
    if genre not in ('gif', 'png'):
        return None  # JPEG : un réencodage sans perte grossit ; WebP : déjà fait
    pil = pil or _pillow()
    if pil is None:
        return None
    Image, ImageChops = pil
    try:
        image = Image.open(io.BytesIO(donnees))
        if getattr(image, 'n_frames', 1) > 1 or getattr(image, 'is_animated', False):
            return None  # animation : hors périmètre
        # Profil ICC, gamma ou chromaticités : le navigateur les applique au PNG, pas au WebP.
        if any(cle in image.info for cle in ('icc_profile', 'gamma', 'chromaticity', 'cHRM', 'iCCP')):
            return None
        if image.mode not in ('1', 'L', 'LA', 'P', 'PA', 'RGB', 'RGBA'):
            return None  # 16 bits ou modes exotiques : pas de conversion sûre
        image.load()
        rgba = image.convert('RGBA')
        sortie = io.BytesIO()
        rgba.save(sortie, 'WEBP', **PARAMETRES_WEBP)
        webp = sortie.getvalue()
        if len(webp) > len(donnees) * (1 - GAIN_MIN):
            return None
        retour = Image.open(io.BytesIO(webp))
        retour.load()
        if retour.size != rgba.size or ImageChops.difference(rgba, retour.convert('RGBA')).getbbox() is not None:
            return None
        return webp
    except Exception:
        return None


def optimiser_uri(genre: str, charge: str, pil=None, cache: Path | None = None) -> str:
    """URI data: optimisée (WebP sans perte) ou URI d'origine."""
    origine = 'data:image/%s;base64,%s' % (genre, charge)
    if genre not in ('gif', 'png'):
        return origine
    empreinte = hashlib.sha256((VERSION_CACHE + genre + charge).encode('ascii')).hexdigest()
    fichier = cache / (empreinte + '.txt') if cache else None
    if fichier and fichier.is_file():
        try:
            valeur = fichier.read_text(encoding='ascii').strip()
            return origine if valeur == '=' else 'data:image/webp;base64,' + valeur
        except OSError:
            pass
    webp = webp_identique(base64.b64decode(charge), genre, pil)
    if fichier and (pil is not None):
        try:
            fichier.write_text(base64.b64encode(webp).decode('ascii') if webp else '=', encoding='ascii')
        except OSError:
            pass
    return 'data:image/webp;base64,' + base64.b64encode(webp).decode('ascii') if webp else origine


def extraire(texte: str, webp: bool = True):
    """Retire les URI d'image du texte des gabarits.

    Renvoie (texte avec jetons, [URI uniques], statistiques). Le texte restitué par
    ``restituer`` est identique à l'entrée lorsque ``webp`` est faux.
    """
    if JETON_RE.search(texte):
        raise ValueError('jeton @mdn-img-N@ déjà présent dans les gabarits')
    pil = _pillow() if webp else None
    cache = _dossier_cache() if pil else None
    index: dict[str, int] = {}
    images: list[str] = []
    stats = {'occurrences': 0, 'uniques': 0, 'octets_origine': 0, 'octets_table': 0, 'webp': 0}

    def remplacer(m):
        if len(m.group(2)) < TAILLE_MIN:
            return m.group(0)
        stats['occurrences'] += 1
        cle = m.group(0)
        if cle not in index:
            index[cle] = len(images)
            uri = optimiser_uri(m.group(1), m.group(2), pil, cache) if pil else cle
            if uri != cle:
                stats['webp'] += 1
            images.append(uri)
            stats['octets_table'] += len(uri)
        stats['octets_origine'] += len(cle)
        return JETON % index[cle]

    resultat = URI_IMAGE.sub(remplacer, texte)
    stats['uniques'] = len(images)
    return resultat, images, stats


def restituer(texte: str, images: list[str]) -> str:
    """Équivalent Python du chargeur JavaScript (contrôles et outils)."""
    return re.sub(r'@mdn-img-(\d+)@', lambda m: images[int(m.group(1))], texte)
