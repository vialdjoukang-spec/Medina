#!/usr/bin/env python3
"""Automate front_poids : poids et vitesse de l'Atlas MEDINA construit.

Usage :
    MEDINA_OUT=/chemin python3 build_front.py && python3 build_front.py --all-fragments
    python3 tools/front_poids.py --out /chemin [--budget budget.json] [--json rapport.json]

L'outil ne modifie rien dans le dossier mesuré. Il produit :
  * le poids de chaque page HTML, décomposé en HTML, CSS, JS, données incorporées,
    polices et images (brut, gzip, brotli si le module ``brotli`` est installé) ;
  * les dix plus gros fichiers et les doublons (même empreinte sous plusieurs noms,
    y compris les ressources incorporées en base64 répétées d'une page à l'autre) ;
  * le CSS et le JS chargés mais inutilisés (couverture Chromium par CDP) ;
  * le premier rendu (FCP), l'interactivité (TTI approché) et l'état « prêt »,
    en file:// et via ``python3 -m http.server``, avec limitation CPU et réseau CDP ;
  * l'audit du chargement des polices (font-display, préchargement).

Code retour : 0 conforme, 1 budget dépassé ou métrique du budget non mesurée, 2 erreur d'utilisation.
Chromium : celui de Playwright sous /opt/pw-browsers (ou MEDINA_CHROMIUM) ;
l'outil n'exécute jamais ``playwright install``.
"""
from __future__ import annotations

import argparse
import base64
import contextlib
import datetime as _dt
import gzip
import hashlib
import json
import os
import re
import socket
import subprocess
import sys
import time
from pathlib import Path

try:  # optionnel : le résumé indique « n/d » sans lui
    import brotli as _brotli  # type: ignore
except Exception:  # pragma: no cover - dépend de l'environnement
    _brotli = None

VERSION = 1
CATEGORIES = ('html', 'css', 'js', 'donnees', 'polices', 'images', 'autres')
TEXT_CATEGORIES = {'html', 'css', 'js', 'donnees'}
TEXT_EXTENSIONS = {'.svg'}  # images textuelles, compressées par le serveur


def compressible(chemin: str, taille: int = 0) -> bool:
    cat = categorie_fichier(chemin)
    return (cat in TEXT_CATEGORIES or Path(chemin).suffix.lower() in TEXT_EXTENSIONS
            or (cat == 'autres' and taille < 1 << 20))
EXTENSIONS = {
    '.html': 'html', '.htm': 'html',
    '.css': 'css',
    '.js': 'js', '.mjs': 'js', '.cjs': 'js',
    '.json': 'donnees', '.jsonl': 'donnees', '.txt': 'donnees', '.xml': 'donnees', '.webmanifest': 'donnees',
    '.woff2': 'polices', '.woff': 'polices', '.ttf': 'polices', '.otf': 'polices', '.eot': 'polices',
    '.png': 'images', '.jpg': 'images', '.jpeg': 'images', '.gif': 'images', '.webp': 'images',
    '.avif': 'images', '.svg': 'images', '.ico': 'images',
}
# Types de <script> qui ne s'exécutent pas : ce sont des données incorporées.
DATA_SCRIPT_TYPES = ('application/json', 'application/ld+json', 'application/octet-stream',
                     'text/template', 'text/plain', 'importmap')

# Profil « mobile moyen » (référence Lighthouse mobile) : CPU ×4, 150 ms RTT,
# 1,6 Mbit/s descendant et 750 kbit/s montant, multipliés par 0,9 comme Lighthouse.
PROFIL_MOBILE = {
    'cpu': 4,
    'latence_ms': 150,
    'descendant_octets_s': int(1.6 * 1024 * 1024 / 8 * 0.9),
    'montant_octets_s': int(750 * 1024 / 8 * 0.9),
    'viewport': {'width': 412, 'height': 823},
    'echelle': 1.75,
}
SCENARIOS = {
    # nom : (transport, limitation CPU, limitation réseau)
    'file-brut': ('file', False, False),
    'file-mobile': ('file', True, False),   # le réseau ne s'applique pas à file://
    'http-brut': ('http', False, False),
    'http-mobile': ('http', True, True),
}
PAGES_DEFAUT = [
    # nom, chemin relatif (#route), condition « prêt », couverture mesurée
    ('accueil', 'index.html', "document.readyState==='complete'", True),
    ('atlas', 'MEDINA.html#/home', 'window.MDN_READY===true', False),
    ('lecon', 'fragments/MEDINA_S08_nerveux.html#/entry/I63', "!!document.querySelector('.mc')", True),
]


# ---------------------------------------------------------------- compression

def taille_gzip(data: bytes, niveau: int = 6) -> int:
    return len(gzip.compress(data, niveau, mtime=0))


def taille_brotli(data: bytes, qualite: int = 9) -> int | None:
    if _brotli is None:
        return None
    return len(_brotli.compress(data, quality=qualite))


def mesures(data: bytes, compresser: bool = True, gzip_niveau: int = 6, brotli_qualite: int = 9) -> dict:
    """Poids brut et compressé d'un contenu. Sans compression : gzip/brotli = brut."""
    brut = len(data)
    if not compresser or not data:
        return {'brut': brut, 'gzip': brut, 'brotli': brut if _brotli else None}
    return {'brut': brut, 'gzip': taille_gzip(data, gzip_niveau), 'brotli': taille_brotli(data, brotli_qualite)}


def additionner(*items: dict) -> dict:
    total = {'brut': 0, 'gzip': 0, 'brotli': 0}
    for item in items:
        for cle in total:
            if total[cle] is None:
                continue
            valeur = item.get(cle)
            total[cle] = None if valeur is None else total[cle] + valeur
    return total


# ---------------------------------------------------------------- classification

def categorie_fichier(chemin: str) -> str:
    return EXTENSIONS.get(Path(chemin).suffix.lower(), 'autres')


def categorie_data_uri(mime: str) -> str:
    mime = mime.lower()
    if mime.startswith('font/') or 'font' in mime or mime.endswith('woff2') or mime.endswith('woff'):
        return 'polices'
    if mime.startswith('image/'):
        return 'images'
    return 'donnees'


DATA_URI = re.compile(r'data:([a-zA-Z0-9.+/-]+)((?:;[a-zA-Z0-9=._-]+)*),([A-Za-z0-9+/=%._~-]+)')
BLOC = re.compile(r'<(script|style|template)\b([^>]*)>(.*?)</\1\s*>', re.S | re.I)
ATTR_TYPE = re.compile(r'\btype\s*=\s*["\']?([^"\'\s>]+)', re.I)


def extraire_data_uris(texte: str):
    """Retire les URI data: d'un texte. Renvoie (reste, [(catégorie, mime, uri, octets décodés)])."""
    trouves = []

    def garder(m):
        mime, params, charge = m.group(1), m.group(2), m.group(3)
        try:
            decode = base64.b64decode(charge, validate=False) if 'base64' in params else charge.encode()
        except Exception:
            decode = charge.encode()
        trouves.append((categorie_data_uri(mime), mime, m.group(0), decode))
        return ''

    return DATA_URI.sub(garder, texte), trouves


def type_script(attributs: str) -> str:
    m = ATTR_TYPE.search(attributs)
    return (m.group(1).lower() if m else 'text/javascript')


def decomposer_html(texte: str) -> dict:
    """Répartit une page autonome en catégories (textes UTF-8 tels que transférés).

    Renvoie {catégorie: [morceaux str]} et la liste des ressources incorporées
    (data: URI) sous la clé ``_incorporees`` : [(catégorie, mime, octets décodés)].
    """
    parts = {c: [] for c in CATEGORIES}
    incorporees = []
    reste = []
    position = 0
    for m in BLOC.finditer(texte):
        reste.append(texte[position:m.start()])
        balise, attributs, contenu = m.group(1).lower(), m.group(2), m.group(3)
        ouverture = texte[m.start():m.start(3)]
        fermeture = texte[m.end(3):m.end()]
        reste.append(ouverture + fermeture)
        if balise == 'style':
            categorie = 'css'
        elif balise == 'template':
            categorie = 'html'
        else:
            t = type_script(attributs)
            categorie = 'donnees' if t in DATA_SCRIPT_TYPES or t.endswith('+json') or t.endswith('/json') else 'js'
        contenu_net, trouves = extraire_data_uris(contenu)
        parts[categorie].append(contenu_net)
        for cat, mime, uri, decode in trouves:
            parts[cat].append(uri)
            incorporees.append((cat, mime, decode))
        position = m.end()
    reste.append(texte[position:])
    html_net, trouves = extraire_data_uris(''.join(reste))
    parts['html'].append(html_net)
    for cat, mime, uri, decode in trouves:
        parts[cat].append(uri)
        incorporees.append((cat, mime, decode))
    parts['_incorporees'] = incorporees
    return parts


REF_EXTERNE = re.compile(r'''<(?:img|link|script|source|video|audio)\b[^>]*?\b(?:src|href)\s*=\s*["']([^"'#?]+)''', re.I)


def references_locales(texte: str, page: Path, racine: Path) -> list[Path]:
    """Fichiers locaux référencés statiquement par la page (img, link, script…)."""
    vus = []
    for ref in REF_EXTERNE.findall(texte):
        if ref.startswith(('data:', 'http:', 'https:', '//', 'mailto:', 'javascript:', '$')) or '${' in ref:
            continue
        cible = (page.parent / ref).resolve()
        try:
            cible.relative_to(racine.resolve())
        except ValueError:
            continue
        if cible.is_file() and cible not in vus:
            vus.append(cible)
    return vus


# ---------------------------------------------------------------- inventaire

def empreinte(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def plus_gros(fichiers: list[dict], n: int = 10) -> list[dict]:
    return sorted(fichiers, key=lambda f: (-f['brut'], f['chemin']))[:n]


def doublons(entrees: list[tuple[str, str, int]]) -> list[dict]:
    """entrees : (nom, sha256, taille). Groupes d'au moins deux noms, triés par octets redondants."""
    groupes: dict[str, dict] = {}
    for nom, sha, taille in entrees:
        g = groupes.setdefault(sha, {'sha256': sha, 'taille': taille, 'chemins': []})
        if nom not in g['chemins']:
            g['chemins'].append(nom)
    resultat = []
    for g in groupes.values():
        if len(g['chemins']) > 1:
            g['chemins'].sort()
            g['copies'] = len(g['chemins'])
            g['octets_redondants'] = g['taille'] * (g['copies'] - 1)
            resultat.append(g)
    return sorted(resultat, key=lambda g: (-g['octets_redondants'], g['sha256']))


def inventaire(out: Path, gzip_niveau: int = 6, brotli_qualite: int = 9, journal=print) -> dict:
    out = out.resolve()
    fichiers, pages, incorporees = [], {}, []
    par_categorie = {c: {'brut': 0, 'gzip': 0, 'brotli': 0 if _brotli else None, 'fichiers': 0} for c in CATEGORIES}
    for chemin in sorted(p for p in out.rglob('*') if p.is_file()):
        rel = chemin.relative_to(out).as_posix()
        data = chemin.read_bytes()
        cat = categorie_fichier(rel)
        m = mesures(data, compressible(rel, len(data)), gzip_niveau, brotli_qualite)
        fichier = {'chemin': rel, 'categorie': cat, 'sha256': empreinte(data), **m}
        fichiers.append(fichier)
        agg = par_categorie[cat]
        agg['fichiers'] += 1
        for cle in ('brut', 'gzip', 'brotli'):
            if agg[cle] is not None and m[cle] is not None:
                agg[cle] += m[cle]
            else:
                agg[cle] = None
        if cat == 'html':
            journal(f'  page {rel} ({m["brut"] / 1e6:.1f} Mo)')
            texte = data.decode('utf-8', errors='replace')
            parts = decomposer_html(texte)
            cats = {}
            for c in CATEGORIES:
                contenu = ''.join(parts[c]).encode('utf-8')
                if not contenu:
                    continue
                # Les URI base64 de polices/images restent compressibles (~25 %) : on mesure.
                cats[c] = mesures(contenu, True, gzip_niveau, brotli_qualite)
            externes = []
            for ref in references_locales(texte, chemin, out):
                d = ref.read_bytes()
                c = categorie_fichier(ref.name)
                externes.append({'chemin': ref.relative_to(out).as_posix(), 'categorie': c,
                                 **mesures(d, compressible(ref.name, len(d)), gzip_niveau, brotli_qualite)})
            pages[rel] = {
                'total': {'brut': m['brut'], 'gzip': m['gzip'], 'brotli': m['brotli']},
                'categories': cats,
                'incorporees': len(parts['_incorporees']),
                'ressources_externes': externes,
                'avec_ressources': additionner(m, *externes),
                'polices': audit_polices(texte),
            }
            for c, mime, decode in parts['_incorporees']:
                if len(decode) >= 1024:
                    incorporees.append((f'{rel} [{mime}]', empreinte(decode), len(decode)))
    total = additionner(*fichiers)
    return {
        'site': {'fichiers': len(fichiers), 'total': total, 'par_categorie': par_categorie},
        'pages': pages,
        'plus_gros_fichiers': [{k: f[k] for k in ('chemin', 'categorie', 'brut', 'gzip', 'brotli')}
                               for f in plus_gros(fichiers)],
        'doublons': {
            'fichiers': doublons([(f['chemin'], f['sha256'], f['brut']) for f in fichiers]),
            'incorporees': regrouper_incorporees(incorporees),
        },
    }


def regrouper_incorporees(entrees: list[tuple[str, str, int]]) -> list[dict]:
    """Ressources base64 identiques répétées : une page qui l'incorpore plusieurs fois compte aussi."""
    groupes: dict[str, dict] = {}
    for nom, sha, taille in entrees:
        g = groupes.setdefault(sha, {'sha256': sha, 'taille': taille, 'occurrences': 0, 'pages': []})
        g['occurrences'] += 1
        page = nom.split(' [', 1)[0]
        if page not in g['pages']:
            g['pages'].append(page)
    res = []
    for g in groupes.values():
        if g['occurrences'] > 1:
            g['octets_redondants'] = g['taille'] * (g['occurrences'] - 1)
            g['nb_pages'] = len(g['pages'])
            g['pages'] = sorted(g['pages'])[:5] + (['…'] if len(g['pages']) > 5 else [])
            res.append(g)
    return sorted(res, key=lambda g: (-g['octets_redondants'], g['sha256']))


# ---------------------------------------------------------------- polices

FONT_FACE = re.compile(r'@font-face\s*\{(.*?)\}', re.S | re.I)
PRELOAD = re.compile(r'<link\b[^>]*\brel\s*=\s*["\']?preload[^>]*>', re.I)


def audit_polices(texte: str) -> dict:
    faces = []
    for m in FONT_FACE.finditer(texte):
        bloc = m.group(1)
        famille = re.search(r'font-family\s*:\s*([^;]+)', bloc, re.I)
        style = re.search(r'font-style\s*:\s*([^;]+)', bloc, re.I)
        display = re.search(r'font-display\s*:\s*([^;]+)', bloc, re.I)
        incorporee = re.search(r'url\(\s*["\']?data:[^;,]+;base64,([A-Za-z0-9+/=]+)', bloc)
        url = re.search(r'url\(\s*["\']?(?!data:)([^"\')]+)', bloc)
        faces.append({
            'famille': famille.group(1).strip().strip('"\'') if famille else None,
            'style': style.group(1).strip() if style else 'normal',
            'font_display': display.group(1).strip() if display else None,
            'source': 'incorporee' if incorporee else (url.group(1).strip() if url else None),
            'octets': len(base64.b64decode(incorporee.group(1))) if incorporee else None,
        })
    prechargements = [p for p in PRELOAD.findall(texte) if re.search(r'\bas\s*=\s*["\']?font', p, re.I)]
    sans_display = [f for f in faces if not f['font_display']]
    return {
        'font_face': faces,
        'prechargements': prechargements,
        'alertes': ([f"{len(sans_display)} @font-face sans font-display"] if sans_display else [])
        + (["polices externes sans <link rel=preload as=font>"]
           if any(f['source'] not in (None, 'incorporee') for f in faces) and not prechargements else []),
    }


# ---------------------------------------------------------------- couverture

def fusionner_intervalles(intervalles) -> list[tuple[int, int]]:
    res = []
    for debut, fin in sorted((a, b) for a, b in intervalles if b > a):
        if res and debut <= res[-1][1]:
            res[-1] = (res[-1][0], max(res[-1][1], fin))
        else:
            res.append((debut, fin))
    return res


def octets_couverts(intervalles) -> int:
    return sum(b - a for a, b in fusionner_intervalles(intervalles))


def intervalles_js_utilises(fonctions: list[dict]) -> list[tuple[int, int]]:
    """Couverture V8 détaillée (blocs imbriqués) → intervalles disjoints exécutés.

    Même algorithme que la couverture de Puppeteer : le bloc le plus interne gagne.
    """
    points = []
    for fn in fonctions:
        for r in fn.get('ranges', []):
            points.append((r['startOffset'], 0, r))
            points.append((r['endOffset'], 1, r))

    def cle(p):
        offset, kind, r = p
        longueur = r['endOffset'] - r['startOffset']
        # À offset égal : fermeture avant ouverture ; ouvertures du plus long au plus court.
        return (offset, -kind, -longueur if kind == 0 else longueur)

    points.sort(key=cle)
    pile, res, dernier = [], [], 0
    for offset, kind, r in points:
        if pile and dernier < offset and pile[-1] > 0:
            if res and res[-1][1] == dernier:
                res[-1] = (res[-1][0], offset)
            else:
                res.append((dernier, offset))
        dernier = offset
        if kind == 0:
            pile.append(r['count'])
        else:
            pile.pop()
    return res


def plages_font_face(texte: str) -> list[tuple[int, int]]:
    """Plages [début, fin) des règles @font-face d'une feuille (offsets en caractères)."""
    return [(m.start(), m.end()) for m in FONT_FACE.finditer(texte)]


def couverture_css(longueur: int, utilises, exclues) -> tuple[int, int, int]:
    """(total hors @font-face, utilisé hors @font-face, octets @font-face).

    Les @font-face ne sont jamais « utilisées » au sens de CSS.ruleUsage : leur charge
    (souvent des polices base64) est mesurée à part avec document.fonts.
    """
    exclues = fusionner_intervalles(exclues)
    exclu = sum(b - a for a, b in exclues)
    morceaux = []
    for a, b in fusionner_intervalles(utilises):
        for x, y in exclues:
            if y <= a or x >= b:
                continue
            if x > a:
                morceaux.append((a, x))
            a = max(a, y)
            if a >= b:
                break
        if a < b:
            morceaux.append((a, b))
    return max(0, longueur - exclu), octets_couverts(morceaux), exclu


def bilan_couverture(elements: list[dict]) -> dict:
    """elements : [{'nom','total','utilise'}] → totaux et 10 plus gros gaspillages."""
    total = sum(e['total'] for e in elements)
    utilise = sum(min(e['utilise'], e['total']) for e in elements)
    inutilise = total - utilise
    detail = sorted(({**e, 'inutilise': e['total'] - min(e['utilise'], e['total'])} for e in elements),
                    key=lambda e: -e['inutilise'])
    return {
        'total': total, 'utilise': utilise, 'inutilise': inutilise,
        'pct_inutilise': round(100 * inutilise / total, 1) if total else 0.0,
        'elements': len(elements), 'principaux': detail[:10],
    }


# ---------------------------------------------------------------- temps

def calculer_tti(fcp: float | None, taches: list[tuple[float, float]], dcl: float | None,
                 fenetre: float = 5000) -> float | None:
    """Time to Interactive approché (méthode Lighthouse simplifiée, sans réseau).

    Fin de la dernière tâche longue (> 50 ms) qui précède la première fenêtre calme
    de ``fenetre`` ms après le FCP ; au moins le DOMContentLoaded.
    """
    if fcp is None:
        return None
    curseur = fcp
    for debut, duree in sorted(taches):
        fin = debut + duree
        if fin <= curseur:
            continue
        if debut - curseur >= fenetre:
            break
        curseur = max(curseur, fin)
    return max(curseur, dcl or 0.0)


# ---------------------------------------------------------------- budget

def lire_metrique(rapport: dict, chemin: str):
    """Chemin pointé « a.b.c » ; les clés peuvent contenir des points si entourées de [ ]."""
    noeud = rapport
    for cle in re.findall(r'\[([^\]]+)\]|([^.\[\]]+)', chemin):
        cle = cle[0] or cle[1]
        if isinstance(noeud, dict) and cle in noeud:
            noeud = noeud[cle]
        else:
            return None
    return noeud if isinstance(noeud, (int, float)) and not isinstance(noeud, bool) else None


def verifier_budget(rapport: dict, budget: dict) -> dict:
    """budget : {"max": {"chemin.metrique": limite}}. Une métrique absente est signalée, non bloquante."""
    depassements, absentes, verifies = [], [], 0
    for chemin, limite in sorted(budget.get('max', {}).items()):
        valeur = lire_metrique(rapport, chemin)
        if valeur is None:
            absentes.append(chemin)
            continue
        verifies += 1
        if valeur > limite:
            depassements.append({'metrique': chemin, 'valeur': valeur, 'limite': limite,
                                 'exces_pct': round(100 * (valeur - limite) / limite, 1) if limite else None})
    return {'verifies': verifies, 'depassements': depassements, 'non_mesurees': absentes}


def arrondir_haut(valeur: float, pas: float) -> float:
    return float(int(-(-valeur // pas)) * pas)


def proposer_budget(rapport: dict, marge: float = 0.10, marge_temps: float = 0.25) -> dict:
    """Budget de non-régression : mesure actuelle + marge, arrondie (100 ko / 100 ms).

    Les temps varient davantage d'une machine à l'autre : marge propre (25 % par défaut).
    """
    limites = {}

    def poser(chemin, pas):
        v = lire_metrique(rapport, chemin)
        if v is not None:
            m = marge_temps if chemin.startswith('temps.') else marge
            limites[chemin] = arrondir_haut(v * (1 + m), pas)
            if pas >= 1:
                limites[chemin] = int(limites[chemin])

    poser('site.total.brut', 1e6)
    poser('site.total.gzip', 1e6)
    for page in rapport.get('pages', {}):
        poser(f'pages.[{page}].total.brut', 1e5)
        poser(f'pages.[{page}].total.gzip', 1e5)
    for nom, cov in rapport.get('couverture', {}).items():
        poser(f'couverture.{nom}.js.inutilise', 1e4)
        poser(f'couverture.{nom}.css.inutilise', 1e4)
    for nom, scen in rapport.get('temps', {}).items():
        for s in scen:
            for m in ('fcp_ms', 'tti_ms', 'pret_ms'):
                poser(f'temps.{nom}.{s}.{m}', 100)
    return {'description': f'Non-régression : mesure du {rapport.get("date", "?")} + {round(marge * 100)} % (poids),'
                           f' + {round(marge_temps * 100)} % (temps)',
            'max': limites}


# ---------------------------------------------------------------- navigateur

def chromium_executable() -> str | None:
    env = os.environ.get('MEDINA_CHROMIUM')
    if env and os.path.exists(env):
        return env
    base = Path(os.environ.get('PLAYWRIGHT_BROWSERS_PATH', '/opt/pw-browsers'))
    for motif in ('chromium-*/chrome-linux*/chrome', 'chromium/chrome-linux*/chrome', 'chromium'):
        for p in sorted(base.glob(motif), reverse=True):
            if p.is_file() and os.access(p, os.X_OK):
                return str(p)
    return None


@contextlib.contextmanager
def serveur_http(racine: Path):
    with socket.socket() as s:
        s.bind(('127.0.0.1', 0))
        port = s.getsockname()[1]
    proc = subprocess.Popen([sys.executable, '-m', 'http.server', str(port), '--bind', '127.0.0.1',
                             '--directory', str(racine)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        for _ in range(100):
            with contextlib.suppress(OSError), socket.create_connection(('127.0.0.1', port), 0.2):
                break
            time.sleep(0.1)
        yield f'http://127.0.0.1:{port}'
    finally:
        proc.terminate()
        with contextlib.suppress(Exception):
            proc.wait(5)


OBSERVATEUR = """(() => {
  window.__fp = {taches: []};
  try { new PerformanceObserver(l => { for (const e of l.getEntries())
    window.__fp.taches.push([e.startTime, e.duration]); })
    .observe({type: 'longtask', buffered: true}); } catch (e) {}
})();"""

LECTURE = """() => {
  const paint = performance.getEntriesByType('paint');
  const fcp = paint.find(p => p.name === 'first-contentful-paint');
  const nav = performance.getEntriesByType('navigation')[0] || {};
  return {fcp: fcp ? fcp.startTime : null, dcl: nav.domContentLoadedEventEnd || null,
          load: nav.loadEventEnd || null, taches: (window.__fp || {}).taches || [],
          tas: performance.memory ? performance.memory.usedJSHeapSize : null};
}"""


def _contexte(navigateur, mobile: bool):
    if mobile:
        return navigateur.new_context(viewport=PROFIL_MOBILE['viewport'], device_scale_factor=PROFIL_MOBILE['echelle'],
                                      is_mobile=True, has_touch=True)
    return navigateur.new_context(viewport={'width': 1300, 'height': 900})


def _attendre(page, condition: str, debut: float, delai_s: float) -> float | None:
    while time.monotonic() - debut < delai_s:
        with contextlib.suppress(Exception):
            if page.evaluate(f'() => {{ try {{ return !!({condition}); }} catch (e) {{ return false; }} }}'):
                return page.evaluate('() => performance.now()')
        time.sleep(0.05)
    return None


def mesurer_temps(navigateur, url: str, condition: str, scenario: str, delai_s: float,
                  fenetre_ms: float = 5000) -> dict:
    transport, cpu, reseau = SCENARIOS[scenario]
    ctx = _contexte(navigateur, cpu)
    page = ctx.new_page()
    cdp = ctx.new_cdp_session(page)
    try:
        cdp.send('Network.enable')
        cdp.send('Network.setCacheDisabled', {'cacheDisabled': True})
        if reseau:
            cdp.send('Network.emulateNetworkConditions', {
                'offline': False, 'latency': PROFIL_MOBILE['latence_ms'],
                'downloadThroughput': PROFIL_MOBILE['descendant_octets_s'],
                'uploadThroughput': PROFIL_MOBILE['montant_octets_s']})
        if cpu:
            cdp.send('Emulation.setCPUThrottlingRate', {'rate': PROFIL_MOBILE['cpu']})
        page.add_init_script(OBSERVATEUR)
        erreurs = []
        page.on('pageerror', lambda e: erreurs.append(str(e)[:200]))
        debut = time.monotonic()
        page.goto(url, wait_until='commit', timeout=delai_s * 1000)
        pret = _attendre(page, condition, debut, delai_s)
        # Fenêtre calme : on observe jusqu'à `fenetre_ms` sans tâche longue (ou délai).
        while time.monotonic() - debut < delai_s:
            lu = page.evaluate(LECTURE)
            fin = max([a + b for a, b in lu['taches']] or [0])
            if lu['fcp'] is not None and page.evaluate('() => performance.now()') - max(fin, lu['fcp']) >= fenetre_ms:
                break
            time.sleep(0.25)
        lu = page.evaluate(LECTURE)
        taches = [tuple(t) for t in lu['taches']]
        return {
            'url': url.split('://', 1)[0] + '://…/' + url.rsplit('/', 1)[-1],
            'fcp_ms': _r(lu['fcp']), 'dcl_ms': _r(lu['dcl']), 'load_ms': _r(lu['load']),
            'tti_ms': _r(calculer_tti(lu['fcp'], taches, lu['dcl'], fenetre_ms)),
            'pret_ms': _r(pret), 'taches_longues': len(taches),
            'blocage_total_ms': _r(sum(max(0.0, d - 50) for _, d in taches)),
            'tache_max_ms': _r(max([d for _, d in taches] or [0])),
            'tas_js_octets': lu['tas'], 'delai_depasse': pret is None,
            'erreurs': erreurs[:3],
        }
    finally:
        ctx.close()


def _r(v):
    return None if v is None else round(float(v))


def mesurer_couverture(navigateur, url: str, condition: str, delai_s: float) -> dict:
    ctx = _contexte(navigateur, False)
    page = ctx.new_page()
    cdp = ctx.new_cdp_session(page)
    feuilles, scripts = {}, {}
    cdp.on('CSS.styleSheetAdded', lambda e: feuilles.__setitem__(e['header']['styleSheetId'], e['header']))
    cdp.on('Debugger.scriptParsed', lambda e: scripts.__setitem__(e['scriptId'], e))
    try:
        cdp.send('Profiler.enable')
        cdp.send('Debugger.enable')
        cdp.send('Profiler.startPreciseCoverage', {'callCount': False, 'detailed': True})
        cdp.send('DOM.enable')
        cdp.send('CSS.enable')
        cdp.send('CSS.startRuleUsageTracking')
        debut = time.monotonic()
        page.goto(url, wait_until='commit', timeout=delai_s * 1000)
        _attendre(page, condition, debut, delai_s)
        page.wait_for_timeout(1500)
        regles = cdp.send('CSS.stopRuleUsageTracking')['ruleUsage']
        couverture = cdp.send('Profiler.takePreciseCoverage')['result']
        # CSS : octets des règles utilisées par feuille.
        utilises: dict[str, list] = {}
        for r in regles:
            if r['used']:
                utilises.setdefault(r['styleSheetId'], []).append((int(r['startOffset']), int(r['endOffset'])))
        css, octets_polices = [], 0
        for sid, h in feuilles.items():
            longueur = int(h.get('length') or 0)
            if not longueur:
                continue
            texte = ''
            with contextlib.suppress(Exception):
                texte = cdp.send('CSS.getStyleSheetText', {'styleSheetId': sid})['text']
            total, utilise, faces = couverture_css(longueur, utilises.get(sid, []), plages_font_face(texte))
            octets_polices += faces
            if not total:
                continue
            nom = (h.get('sourceURL') or '').split('#', 1)[0]
            nom = ('inline:' if h.get('isInline') else '') + (nom.rsplit('/', 1)[-1] or '?') + f'@{h.get("startLine", 0)}'
            css.append({'nom': nom, 'total': total, 'utilise': utilise})
        polices = page.evaluate("""() => [...document.fonts].map(f => ({famille: f.family.replace(/["']/g, ''),
            style: f.style, poids: f.weight, statut: f.status}))""")
        # JS : blocs exécutés par script (scripts inline, modules, eval exclus).
        js = []
        for entree in couverture:
            info = scripts.get(entree['scriptId'], {})
            url_s = entree.get('url') or info.get('url') or ''
            if not url_s or url_s.startswith(('chrome', 'devtools', 'extensions::')) or '__playwright' in url_s:
                continue
            total = int(info.get('length') or (info.get('endOffset') or 0))
            if not total:
                with contextlib.suppress(Exception):
                    total = len(cdp.send('Debugger.getScriptSource', {'scriptId': entree['scriptId']})['scriptSource'])
            if total < 200:
                continue
            nom = url_s.split('#', 1)[0].rsplit('/', 1)[-1] + f'@{info.get("startLine", 0)}'
            js.append({'nom': nom, 'total': total, 'utilise': octets_couverts(intervalles_js_utilises(entree['functions']))})
        chargees = [f for f in polices if f['statut'] == 'loaded']
        return {'css': bilan_couverture(css), 'js': bilan_couverture(js),
                'polices': {'octets_font_face_css': octets_polices, 'faces': len(polices),
                            'chargees': len(chargees), 'non_utilisees': [f for f in polices if f['statut'] != 'loaded']}}
    finally:
        ctx.close()


def mesures_navigateur(out: Path, pages: list, scenarios: list[str], delai_s: float, journal=print) -> tuple[dict, dict]:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        journal('Playwright absent : mesures navigateur omises.')
        return {}, {}
    exe = chromium_executable()
    couverture, temps = {}, {}
    with sync_playwright() as p, serveur_http(out) as base_http:
        navigateur = p.chromium.launch(**({'executable_path': exe} if exe else {}),
                                       args=['--enable-precise-memory-info'])
        try:
            for nom, chemin, condition, cov in pages:
                fichier = (out / chemin.split('#', 1)[0])
                if not fichier.is_file():
                    journal(f'  {nom} : {chemin} absent, ignoré')
                    continue
                url_file = fichier.resolve().as_uri() + ('#' + chemin.split('#', 1)[1] if '#' in chemin else '')
                if cov:
                    journal(f'  couverture {nom}')
                    couverture[nom] = {'page': chemin, **mesurer_couverture(navigateur, url_file, condition, delai_s)}
                for s in scenarios:
                    journal(f'  temps {nom} [{s}]')
                    url = url_file if SCENARIOS[s][0] == 'file' else f'{base_http}/{chemin}'
                    temps.setdefault(nom, {})[s] = mesurer_temps(navigateur, url, condition, s, delai_s)
        finally:
            navigateur.close()
    return couverture, temps


# ---------------------------------------------------------------- sortie

def ko(v) -> str:
    if v is None:
        return 'n/d'
    return f'{v / 1e6:.2f} Mo' if v >= 1e6 else f'{v / 1e3:.0f} ko'


def ms(v) -> str:
    return 'n/d' if v is None else (f'{v / 1000:.1f} s' if v >= 1000 else f'{v:.0f} ms')


def resume(r: dict) -> str:
    lignes = [f"front_poids — {r['dossier']} — {r['date']}"]
    t = r['site']['total']
    lignes.append(f"Site : {r['site']['fichiers']} fichiers, {ko(t['brut'])} brut, {ko(t['gzip'])} gzip, {ko(t['brotli'])} brotli")
    lignes.append('Pages (brut / gzip) — répartition brute :')
    for nom, p in sorted(r['pages'].items(), key=lambda x: -x[1]['total']['brut'])[:8]:
        rep = ', '.join(f"{c} {ko(v['brut'])}" for c, v in sorted(p['categories'].items(), key=lambda x: -x[1]['brut']))
        lignes.append(f"  {nom}: {ko(p['total']['brut'])} / {ko(p['total']['gzip'])} — {rep}")
    lignes.append('Dix plus gros fichiers :')
    lignes += [f"  {ko(f['brut']):>10}  {f['chemin']}" for f in r['plus_gros_fichiers']]
    df, di = r['doublons']['fichiers'], r['doublons']['incorporees']
    lignes.append(f"Doublons de fichiers : {len(df)} groupes, {ko(sum(g['octets_redondants'] for g in df))} redondants")
    lignes.append(f"Ressources incorporées répétées : {len(di)} groupes, {ko(sum(g['octets_redondants'] for g in di))} redondants")
    for nom, c in r.get('couverture', {}).items():
        lignes.append(f"Couverture {nom} : CSS {c['css']['pct_inutilise']} % inutilisé ({ko(c['css']['inutilise'])}/{ko(c['css']['total'])}"
                      f" hors @font-face), JS {c['js']['pct_inutilise']} % inutilisé ({ko(c['js']['inutilise'])}/{ko(c['js']['total'])}),"
                      f" polices {c['polices']['chargees']}/{c['polices']['faces']} faces chargées ({ko(c['polices']['octets_font_face_css'])} de @font-face)")
    for nom, sc in r.get('temps', {}).items():
        for s, v in sc.items():
            lignes.append(f"Temps {nom} [{s}] : FCP {ms(v['fcp_ms'])}, TTI {ms(v['tti_ms'])}, prêt {ms(v['pret_ms'])},"
                          f" blocage {ms(v['blocage_total_ms'])}{' (DÉLAI DÉPASSÉ)' if v['delai_depasse'] else ''}")
    b = r.get('budget')
    if b:
        lignes.append(f"Budget : {b['verifies']} métriques vérifiées, {len(b['depassements'])} dépassements")
        lignes += [f"  DÉPASSÉ {d['metrique']} = {d['valeur']} > {d['limite']}" for d in b['depassements']]
        lignes += [f"  NON MESURÉE {m}" for m in b['non_mesurees']]
    return '\n'.join(lignes)


def analyser_pages(specs: list[str] | None) -> list:
    if not specs:
        return PAGES_DEFAUT
    pages = []
    for spec in specs:
        # nom=chemin[#route][|condition JS][|couverture]
        nom, _, reste = spec.partition('=')
        morceaux = reste.split('|')
        pages.append((nom, morceaux[0], morceaux[1] if len(morceaux) > 1 and morceaux[1] else "document.readyState==='complete'",
                      len(morceaux) > 2 and morceaux[2] in ('1', 'oui', 'couverture')))
    return pages


def principal(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--out', required=True, help='dossier construit (MEDINA_OUT, éventuellement assemblé comme _site)')
    ap.add_argument('--budget', help='budget JSON {"max": {"chemin.metrique": limite}}')
    ap.add_argument('--json', help='rapport JSON (défaut : <out>/../front_poids.json)')
    ap.add_argument('--proposer-budget', help='écrit un budget de non-régression (mesure + marge) dans ce fichier')
    ap.add_argument('--marge', type=float, default=0.10, help='marge du budget proposé pour les poids')
    ap.add_argument('--marge-temps', type=float, default=0.25, help='marge du budget proposé pour les temps')
    ap.add_argument('--page', action='append', help='nom=chemin[#route]|condition JS|couverture (répétable)')
    ap.add_argument('--scenarios', default='file-brut,file-mobile,http-mobile',
                    help='parmi ' + ','.join(SCENARIOS))
    ap.add_argument('--tolerer-non-mesurees', action='store_true',
                    help='ne pas échouer quand une métrique du budget est absente du rapport')
    ap.add_argument('--sans-navigateur', action='store_true', help='poids seulement')
    ap.add_argument('--delai', type=float, default=900, help='délai maximal par mesure (s)')
    ap.add_argument('--gzip-niveau', type=int, default=6)
    ap.add_argument('--brotli-qualite', type=int, default=9)
    a = ap.parse_args(argv)
    out = Path(a.out)
    if not out.is_dir():
        ap.error(f'{out} n’est pas un dossier')
    scenarios = [s for s in a.scenarios.split(',') if s]
    inconnus = [s for s in scenarios if s not in SCENARIOS]
    if inconnus:
        ap.error('scénarios inconnus : ' + ', '.join(inconnus))
    journal = lambda m: print(m, file=sys.stderr, flush=True)
    journal('Inventaire des poids…')
    rapport = {'outil': 'front_poids', 'version': VERSION,
               'date': _dt.datetime.now().astimezone().isoformat(timespec='seconds'),
               'dossier': str(out.resolve()),
               'compression': {'gzip_niveau': a.gzip_niveau, 'brotli_qualite': a.brotli_qualite if _brotli else None},
               'profil_mobile': PROFIL_MOBILE}
    rapport.update(inventaire(out, a.gzip_niveau, a.brotli_qualite, journal))
    if not a.sans_navigateur:
        journal('Mesures Chromium…')
        rapport['couverture'], rapport['temps'] = mesures_navigateur(out, analyser_pages(a.page), scenarios, a.delai, journal)
    code = 0
    if a.budget:
        rapport['budget'] = verifier_budget(rapport, json.loads(Path(a.budget).read_text(encoding='utf-8')))
        rapport['budget']['fichier'] = a.budget
        b = rapport['budget']
        # Une métrique demandée mais non mesurée ne doit pas laisser passer la CI.
        code = 1 if b['depassements'] or (b['non_mesurees'] and not a.tolerer_non_mesurees) else 0
    if a.proposer_budget:
        Path(a.proposer_budget).write_text(json.dumps(proposer_budget(rapport, a.marge, a.marge_temps), ensure_ascii=False, indent=2) + '\n',
                                           encoding='utf-8')
    cible = Path(a.json) if a.json else out.resolve().parent / 'front_poids.json'
    cible.write_text(json.dumps(rapport, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(resume(rapport))
    print(f'Rapport JSON : {cible}')
    return code


if __name__ == '__main__':
    sys.exit(principal())
