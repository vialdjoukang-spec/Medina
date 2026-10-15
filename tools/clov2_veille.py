#!/usr/bin/env python3
"""CloV_2 — veille économe des messages de Codex vers Claude (instruction de Vial, 15.10.2026).

Objet : ne jamais manquer une recommandation de Codex (droit, vitesse, probité des cours).
Coût : aucun jeton tant que rien n'est nouveau ; seule une nouveauté réveille Claude.

Sources lues (lecture seule, aucune écriture sur GitHub) :
  1. commits nouveaux des branches origin/codex/* ;
  2. commits nouveaux de origin/main touchant docs/collaboration/, AGENTS.md, CLAUDE.md, organisation/ ;
  3. PR ouvertes ou mises à jour, et commentaires récents (API publique GitHub).

  python3 tools/clov2_veille.py            # un passage ; code 3 si nouveauté (résumé imprimé)
  python3 tools/clov2_veille.py --boucle 600   # répète toutes les 600 s jusqu'à une nouveauté
L'état (éléments déjà vus) est gardé hors dépôt : $CLOV2_ETAT ou ~/.clov2_etat.json.
"""
import argparse
import json
import os
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = 'vialdjoukang-spec/Medina'
STATE = Path(os.environ.get('CLOV2_ETAT', Path.home() / '.clov2_etat.json'))
WATCHED = ('docs/collaboration/', 'AGENTS.md', 'CLAUDE.md', 'organisation/', 'REPRISE_SESSION.md')


def git(*args):
    return subprocess.run(['git', *args], cwd=ROOT, capture_output=True, text=True).stdout


def api(path):
    request = urllib.request.Request(f'https://api.github.com/repos/{REPO}/{path}',
                                     headers={'Accept': 'application/vnd.github+json'})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.load(response)
    except Exception:  # réseau ou quota : passage ignoré, réessai au suivant
        return []


def scan(state):
    git('fetch', '-q', '--prune', 'origin')
    news = []
    for ref in git('for-each-ref', '--format=%(refname:short)', 'refs/remotes/origin/codex/').split():
        head = git('rev-parse', ref).strip()
        old = state['branches'].get(ref)
        if old != head:
            span = f'{old}..{ref}' if old else f'-3 {ref}'
            for line in git('log', '--format=%h %s', *span.split()).splitlines()[:10]:
                news.append(f'[branche {ref}] {line}')
            state['branches'][ref] = head
    main = git('rev-parse', 'origin/main').strip()
    if state.get('main') and state['main'] != main:
        for line in git('log', '--format=%h %an %s', f"{state['main']}..origin/main", '--', *WATCHED).splitlines()[:15]:
            news.append(f'[main] {line}')
    state['main'] = main
    for pr in api('pulls?state=all&sort=updated&direction=desc&per_page=10'):
        key = f"{pr['number']}@{pr['updated_at']}"
        if key not in state['prs'] and pr['updated_at'] > state.get('since', ''):
            news.append(f"[PR #{pr['number']} {pr['state']}] {pr['title']} ({pr['head']['ref']})")
            state['prs'].append(key)
    for comment in api(f"issues/comments?sort=created&direction=desc&per_page=15&since={state.get('since', '')}"):
        if comment['id'] not in state['comments']:
            body = ' '.join(comment['body'].split())[:300]
            news.append(f"[commentaire {comment['html_url']}] {body}")
            state['comments'].append(comment['id'])
    state['prs'], state['comments'] = state['prs'][-200:], state['comments'][-500:]
    state['since'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    return news


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--boucle', type=int, default=0, help='intervalle en secondes ; 0 = un seul passage')
    a = p.parse_args()
    state = json.loads(STATE.read_text()) if STATE.exists() else {'branches': {}, 'prs': [], 'comments': []}
    first = not STATE.exists()
    while True:
        news = scan(state)
        STATE.write_text(json.dumps(state, ensure_ascii=False))
        if news and not first:
            print('CloV_2 — nouveautés Codex/projet :')
            print('\n'.join(news))
            return 3
        first = False
        if not a.boucle:
            print('CloV_2 : rien de nouveau')
            return 0
        time.sleep(a.boucle)


if __name__ == '__main__':
    sys.exit(main())
