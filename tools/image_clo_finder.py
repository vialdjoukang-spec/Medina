#!/usr/bin/env python3
"""Image_Clo_finder — couche Claude au-dessus d'Image_Codex_Finder (même moteur, même cache, même budget).

Pourquoi une couche et non un second moteur : deux moteurs aux états séparés ne partagent ni quotas
ni verrous, et multiplient les requêtes vers les sites sources. Toutes les copies Claude (sous-agents,
processus parallèles) passent donc par la base SQLite partagée d'Image_Codex_Finder, et de préférence
par son courtier local unique (`serve`). Aucune image n'est générée, téléchargée ni importée.

Commandes :
  inventory <CODE>        inventaire hors ligne des figures d'une leçon (chapters/<CODE>/*.html)
  candidates "<requête>"  candidats Commons ou Europe PMC via le courtier (ou --direct sur le cache partagé),
                          sans les rejets IA/licence, avec une attribution proposée
  status                  délais d'attente, échecs et budget du jour par fournisseur (base partagée)
  selftest                contrôles hors réseau (transport factice)

Règle de Vial (15.10.2026) : une anatomie dessinée par IA n'est pas recevable. Ce moteur aide à trouver
des originaux existants ; il ne certifie ni l'origine humaine, ni la licence, ni l'exactitude anatomique.
Toute sortie garde publication_ready=false : ouvrir la page et l'original, vérifier visuellement.
"""
import argparse, json, os, re, sqlite3, sys, tempfile, datetime as dt
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import image_codex_finder as icf  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SHARED_CACHE = os.path.expanduser('~/.cache/image_codex_finder/shared.sqlite3')
CLAUDE_DAILY_BUDGET = 60  # ne peut que réduire le seuil partagé (politique min) : sobriété accrue
DRAWING_TAGS = {'path', 'ellipse', 'circle', 'polygon', 'polyline'}


class _Figures(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.items, self.stack, self.caption, self.in_caption = [], [], [], False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'figure':
            self.stack.append({'balise': 'figure', 'id': a.get('id'), 'images': [], 'svg': None})
            self.caption = []
        elif tag == 'figcaption':
            self.in_caption = True
        elif tag == 'img':
            img = {'src': a.get('src', '')[:300], 'alt': a.get('alt', '')[:300], 'id': a.get('id')}
            if self.stack:
                self.stack[-1]['images'].append(img)
            else:
                self.items.append({'balise': 'img', **img})
        elif tag == 'svg':
            svg = {'id': a.get('id'), 'aria': a.get('aria-label') or a.get('role'), 'formes': 0, 'textes': 0}
            if self.stack and self.stack[-1]['svg'] is None:
                self.stack[-1]['svg'] = svg
            else:
                svg['balise'] = 'svg'  # même objet : les compteurs suivants restent visibles dans l'inventaire
                self.items.append(svg)
            self._svg = svg
        elif tag in DRAWING_TAGS and getattr(self, '_svg', None) is not None:
            self._svg['formes'] += 1
        elif tag == 'text' and getattr(self, '_svg', None) is not None:
            self._svg['textes'] += 1

    def handle_endtag(self, tag):
        if tag == 'figcaption':
            self.in_caption = False
        elif tag == 'svg':
            self._svg = None
        elif tag == 'figure' and self.stack:
            fig = self.stack.pop()
            fig['legende'] = ' '.join(''.join(self.caption).split())[:400]
            self.items.append(fig)

    def handle_data(self, data):
        if self.in_caption:
            self.caption.append(data)


def inventory(code, root=ROOT):
    """Inventaire hors ligne. Toute figure vectorielle est à examiner visuellement : seul l'auditeur classe
    ANATOMIQUE_IA / SCHEMA_NON_ANATOMIQUE / IMAGE_SOURCEE ; toute image raster garde sa provenance à vérifier."""
    out = []
    for f in sorted((Path(root) / 'chapters' / code).glob(f'{code}_*.html')):
        p = _Figures()
        p.feed(f.read_text(encoding='utf-8'))
        for i, it in enumerate(p.items, 1):
            svg = it.get('svg') if it['balise'] == 'figure' else (it if it['balise'] == 'svg' else None)
            it['fichier'], it['rang'] = f.name, i
            # Aucun seuil automatique : le nombre de formes ne distingue pas une anatomie dessinée d'un schéma.
            it['indice'] = 'vectoriel_a_examiner_visuellement' if svg or not it.get('images') and it['balise'] != 'img' \
                else 'image_raster_provenance_a_verifier'
            out.append(it)
    return out


def attribution(r):
    who = r.get('author') or 'Auteur à confirmer'
    lic = r.get('license') or 'licence à confirmer'
    return f"{who}, « {r.get('title') or 'sans titre'} », {lic} ({r.get('license_url') or 'URL de licence à confirmer'}), via {r.get('source_page')}"


def finder(cache=SHARED_CACHE, http=icf.transport):
    return icf.Finder(cache, http=http, daily_budget=CLAUDE_DAILY_BUDGET)


def candidates(query, provider='commons', limit=6, broker=None, direct=False, cache=SHARED_CACHE):
    if broker:
        data = icf.broker_search(broker, query, provider, limit)
    elif direct:
        data = finder(cache).search(query, provider, limit)
    else:
        raise icf.FinderError('Choisir --broker http://127.0.0.1:8765 (recommandé) ou --direct (cache partagé)')
    kept = [dict(r, attribution_proposee=attribution(r)) for r in data.get('results', [])
            if not str(r.get('status', '')).startswith('REJECTED')]
    return dict(data, results=kept, rejets_ecartes=len(data.get('results', [])) - len(kept),
                rappel='Candidats seulement : contrôle visuel médical, origine et droits propres à la figure avant usage.')


def status(cache=SHARED_CACHE):
    if not Path(cache).exists():
        return {'cache': cache, 'etat': 'absent'}
    c = sqlite3.connect(cache, timeout=15)
    day = dt.datetime.now(dt.timezone.utc).date().isoformat()
    now = dt.datetime.now(dt.timezone.utc).timestamp()
    rows = c.execute('SELECT name,cooldown,failures FROM provider').fetchall()
    used = dict(c.execute('SELECT provider,used FROM budget WHERE day=?', (day,)).fetchall())
    budget = c.execute("SELECT value FROM policy WHERE k='daily_budget'").fetchone()
    return {'cache': cache, 'budget_journalier': budget[0] if budget else None, 'fournisseurs': [
        {'nom': n, 'echecs': f, 'utilise_aujourdhui': used.get(n, 0),
         'attente_restante_s': max(0, round(cd - now))} for n, cd, f in rows]}


def selftest():
    class R:  # transport factice : aucune requête réseau
        def __init__(self, status, body, headers=None):
            self.status, self.body, self.headers = status, body, headers or {'Content-Type': 'application/json'}
    page = {'title': 'File:Gray516.png', 'imageinfo': [{'mime': 'image/png', 'url': 'https://upload.wikimedia.org/x.png',
            'descriptionurl': 'https://commons.wikimedia.org/wiki/File:Gray516.png', 'extmetadata': {
                'Artist': {'value': 'Henry Vandyke Carter'}, 'LicenseShortName': {'value': 'Public domain'},
                'LicenseUrl': {'value': ''}, 'Source': {'value': "Gray's Anatomy (1918)"}}}]}
    ai = {'title': 'File:Brain AI.png', 'imageinfo': [{'mime': 'image/png', 'url': 'https://u/x2.png',
          'descriptionurl': 'https://commons.wikimedia.org/wiki/File:Brain_AI.png', 'extmetadata': {
              'Artist': {'value': 'x'}, 'LicenseShortName': {'value': 'CC0'}, 'Source': {'value': 'AI-generated with Midjourney'},
              'ImageDescription': {'value': 'AI-generated image'}}}]}
    calls = []
    def http(url, extra_headers=None):
        calls.append(url)
        return R(200, json.dumps({'query': {'pages': {'1': page, '2': ai}}}).encode())
    with tempfile.TemporaryDirectory() as d:
        cache = os.path.join(d, 'c.sqlite3')
        f = finder(cache, http)
        res = f.search('circle of Willis', 'commons', 4)
        kept = [r for r in res['results'] if not r['status'].startswith('REJECTED')]
        assert len(kept) == 1 and kept[0]['author'] == 'Henry Vandyke Carter', kept
        f.search('circle of Willis', 'commons', 4)
        assert len(calls) == 1, 'le cache doit éviter un second appel'
        assert all(not r['publication_ready'] for r in res['results'])
        st = status(cache)
        assert st['budget_journalier'] <= CLAUDE_DAILY_BUDGET and st['fournisseurs'][0]['utilise_aujourdhui'] == 1
        lesson = Path(d) / 'chapters' / 'T00'
        lesson.mkdir(parents=True)
        (lesson / 'T00_c.html').write_text('<figure id="f1"><svg>' + '<path d="M0 0"/>' * 9 +
                                          '</svg><figcaption>Rein dessiné</figcaption></figure>'
                                          '<svg id="s2"><circle/><circle/><text>x</text></svg>'
                                          '<figure><img src="a.jpg" alt="IRM"><figcaption>IRM réelle</figcaption></figure>',
                                          encoding='utf-8')
        inv = inventory('T00', d)
        assert [i['indice'] for i in inv] == ['vectoriel_a_examiner_visuellement', 'vectoriel_a_examiner_visuellement',
                                              'image_raster_provenance_a_verifier'], inv
        assert (inv[0]['svg']['formes'], inv[1]['formes'], inv[1]['textes']) == (9, 2, 1), inv
    return 'selftest OK : rejet IA, cache sans second appel, budget partagé, inventaire hors ligne'


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--cache', default=SHARED_CACHE)
    sp = ap.add_subparsers(dest='cmd', required=True)
    i = sp.add_parser('inventory'); i.add_argument('code')
    c = sp.add_parser('candidates'); c.add_argument('query')
    c.add_argument('--provider', choices=list(icf.ENDPOINTS), default='commons')
    c.add_argument('--limit', type=int, default=6)
    m = c.add_mutually_exclusive_group(); m.add_argument('--broker'); m.add_argument('--direct', action='store_true')
    sp.add_parser('status'); sp.add_parser('selftest')
    a = ap.parse_args()
    try:
        if a.cmd == 'inventory':
            out = inventory(a.code.upper())
        elif a.cmd == 'candidates':
            out = candidates(a.query, a.provider, a.limit, a.broker, a.direct, a.cache)
        elif a.cmd == 'status':
            out = status(a.cache)
        else:
            print(selftest()); return 0
    except icf.FinderError as e:
        print(json.dumps({'erreur': str(e), 'consigne': 'aucun nouvel essai en boucle ; autre source ou lacune déclarée'},
                         ensure_ascii=False)); return 2
    print(json.dumps(out, ensure_ascii=False, indent=1)); return 0


if __name__ == '__main__':
    sys.exit(main())
