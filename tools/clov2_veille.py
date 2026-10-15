#!/usr/bin/env python3
"""CloV_2 — veille technique en lecture seule, sans relance implicite de Claude.

Sources indépendantes : branches origin/codex/*, changements documentaires de
main, PR et commentaires d'issues/PR. Chaque source conserve son propre curseur.
Une erreur n'est jamais assimilée à une absence de nouveautés. La pagination est
complète ; le curseur n'avance qu'après lecture complète de sa source.

  python3 tools/clov2_veille.py                 # un passage
  python3 tools/clov2_veille.py --boucle 600    # jusqu'à un signal ou une erreur
  python3 tools/clov2_veille.py --baseline-silencieuse  # première exécution seulement

Codes : 0 = scan complet sans nouveauté ; 3 = nouveautés (signal à un superviseur,
pas un réveil de Claude) ; 2 = scan incomplet/erreur, même si des nouveautés ont
été trouvées ailleurs. Le premier passage signale les éléments présents, sauf
baseline explicitement demandée. L'état est hors dépôt par défaut : $CLOV2_ETAT
ou ~/.clov2_etat.json. Seuls GH_TOKEN/GITHUB_TOKEN sont utilisés pour l'API.

Cette veille observe l'état courant des PR/commentaires, pas tous leurs états
intermédiaires ni les messages supprimés avant consultation.
"""
import argparse
import copy
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
REPO = 'vialdjoukang-spec/Medina'
STATE = Path(os.environ.get('CLOV2_ETAT', Path.home() / '.clov2_etat.json'))
WATCHED = ('docs/collaboration/', 'AGENTS.md', 'CLAUDE.md', 'organisation/', 'REPRISE_SESSION.md')
OVERLAP_SECONDS = 120
PAGE_SIZE = 100


class VeilleError(RuntimeError):
    """Erreur explicite dont le message ne contient ni jeton ni réponse brute."""


@dataclass
class ScanResult:
    news: list
    errors: list


def timestamp(value=None):
    value = value or datetime.now(timezone.utc)
    return value.astimezone(timezone.utc).isoformat(timespec='seconds').replace('+00:00', 'Z')


def parse_timestamp(value):
    try:
        result = datetime.fromisoformat(value.replace('Z', '+00:00'))
        if result.tzinfo is None:
            raise ValueError('timezone missing')
        return result.astimezone(timezone.utc)
    except (AttributeError, TypeError, ValueError) as exc:
        raise VeilleError('Horodatage absent ou invalide dans un état/API') from exc


def lower_bound(source):
    return (timestamp(parse_timestamp(source['since']) - timedelta(seconds=OVERLAP_SECONDS))
            if source.get('since') else None)


def git(*args):
    """Lecture distante uniquement : fetch met à jour le clone, jamais GitHub."""
    try:
        result = subprocess.run(['git', *args], cwd=ROOT, capture_output=True, text=True)
    except OSError as exc:
        raise VeilleError(f'Git {args[0]} indisponible') from exc
    if result.returncode:
        # Les messages git bruts peuvent contenir une URL avec des identifiants.
        raise VeilleError(f'Git {args[0]} a échoué (code {result.returncode})')
    return result.stdout


def api(path):
    headers = {'Accept': 'application/vnd.github+json', 'User-Agent': 'MEDINA-CloV2'}
    token = os.environ.get('GH_TOKEN') or os.environ.get('GITHUB_TOKEN')
    if token:
        headers['Authorization'] = f'Bearer {token}'
    request = urllib.request.Request(f'https://api.github.com/repos/{REPO}/{path}', headers=headers)
    endpoint = path.split('?', 1)[0]
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.load(response)
    except urllib.error.HTTPError as exc:
        raise VeilleError(f'API {endpoint} : HTTP {exc.code} ; curseur conservé') from exc
    except (urllib.error.URLError, OSError, ValueError) as exc:
        raise VeilleError(f'API {endpoint} : réponse indisponible ou JSON invalide ; curseur conservé') from exc


def api_all(path, reader=None):
    """Toutes les pages, y compris l'ultime page vide si nécessaire.

    Le résultat n'est rendu qu'une fois toutes les pages obtenues. Une panne
    tardive ne valide donc ni notifications partielles ni curseur de cette source.
    """
    reader = reader or api
    endpoint, _, query = path.partition('?')
    params = dict(urllib.parse.parse_qsl(query))
    params['per_page'] = PAGE_SIZE
    items = []
    page = 1
    while True:
        params['page'] = page
        batch = reader(f'{endpoint}?{urllib.parse.urlencode(params)}')
        if not isinstance(batch, list):
            raise VeilleError(f'API {endpoint} : une liste paginée était attendue')
        items.extend(batch)
        if len(batch) < PAGE_SIZE:
            return items
        page += 1


def new_state():
    return {'version': 2, 'sources': {
        'codex': {'heads': {}}, 'main': {},
        'prs': {'seen': {}}, 'comments': {'seen': {}},
    }}


def migrate_state(state):
    """Migration de l'ancien since commun, sans remettre les curseurs à zéro."""
    if not isinstance(state, dict):
        raise VeilleError('État de veille invalide : objet JSON attendu')
    if state.get('version') == 2:
        result = copy.deepcopy(state)
        sources = result.get('sources')
        if not isinstance(sources, dict):
            raise VeilleError('État de veille invalide : sources absentes')
        defaults = new_state()['sources']
        for name, default in defaults.items():
            sources.setdefault(name, default)
            if not isinstance(sources[name], dict):
                raise VeilleError(f'État de veille invalide : source {name}')
            if sources[name].get('since'):
                parse_timestamp(sources[name]['since'])
        if not isinstance(sources['codex'].get('heads'), dict):
            raise VeilleError('État de veille invalide : empreintes de branches')
        for name in ('prs', 'comments'):
            if not isinstance(sources[name].get('seen'), dict):
                raise VeilleError(f'État de veille invalide : empreintes {name}')
        return result
    if 'version' in state:
        raise VeilleError('Version d’état inconnue ; aucune remise à zéro automatique')
    result = new_state()
    since = state.get('since')
    if since:
        parse_timestamp(since)
        for source in result['sources'].values():
            source['since'] = since
    branches = state.get('branches', {})
    prs, comments = state.get('prs', []), state.get('comments', [])
    if not isinstance(branches, dict) or not isinstance(prs, list) or not isinstance(comments, list):
        raise VeilleError('Ancien état de veille invalide ; migration interrompue')
    result['sources']['codex']['heads'] = copy.deepcopy(branches)
    if state.get('main'):
        result['sources']['main']['head'] = state['main']
    result['sources']['prs']['legacy_seen'] = [str(value) for value in prs]
    result['sources']['comments']['legacy_seen'] = [str(value) for value in comments]
    return result


def load_state(path):
    if not path.exists():
        return new_state()
    try:
        return migrate_state(json.loads(path.read_text(encoding='utf-8')))
    except (OSError, ValueError) as exc:
        raise VeilleError('État de veille illisible ; fichier conservé sans remise à zéro') from exc


def save_state(path, state):
    """Remplacement atomique, même répertoire et permissions privées."""
    temporary = None
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', dir=path.parent,
                                         prefix=f'.{path.name}.', delete=False) as stream:
            temporary = Path(stream.name)
            json.dump(state, stream, ensure_ascii=False, indent=2)
            stream.write('\n')
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    except OSError as exc:
        raise VeilleError('Écriture atomique de l’état impossible ; ancien fichier conservé') from exc
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def _head(runner, ref):
    value = runner('rev-parse', '--verify', ref).strip()
    if len(value) not in (40, 64) or any(c not in '0123456789abcdefABCDEF' for c in value):
        raise VeilleError(f'Git : empreinte invalide pour {ref}')
    return value


def scan_codex(source, runner):
    heads, news = {}, []
    refs = runner('for-each-ref', '--format=%(refname:short)', 'refs/remotes/origin/codex/').splitlines()
    for ref in refs:
        head = _head(runner, ref)
        heads[ref] = head
        old = source['heads'].get(ref)
        if old == head:
            continue
        # Aucun plafond arbitraire ne jette des recommandations non lues.
        span = [f'{old}..{ref}'] if old else [ref, '--not', 'origin/main']
        lines = runner('log', '--format=%H %s', *span).splitlines()
        news.extend(f'[branche {ref}] {line}' for line in lines)
        if not lines:
            news.append(f'[branche {ref}] tête repérée : {head} (aucun nouveau commit dans l’intervalle lu)')
    source['heads'] = heads
    return news


def scan_main(source, runner):
    head = _head(runner, 'origin/main')
    old = source.get('head')
    news = []
    if old != head:
        span = f'{old}..origin/main' if old else 'origin/main'
        lines = runner('log', '--format=%H %an %s', span, '--', *WATCHED).splitlines()
        news = [f'[main] {line}' for line in lines]
    source['head'] = head
    return news


def _fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def _recent(source, key, at, legacy=None):
    if key in source['seen']:
        return False
    if legacy in source.get('legacy_seen', []) and source.get('since'):
        if parse_timestamp(at) <= parse_timestamp(source['since']):
            source['seen'][key] = at
            return False
    source['seen'][key] = at
    return True


def _within_window(at, lower):
    parsed = parse_timestamp(at)
    return not lower or parsed >= parse_timestamp(lower)


def scan_prs(source, reader):
    lower, news = lower_bound(source), []
    for pr in api_all('pulls?state=all&sort=updated&direction=desc', reader):
        try:
            at, number = pr['updated_at'], pr['number']
            if not _within_window(at, lower):
                continue
            summary = [number, at, pr['state'], pr['title'], pr['head']['ref'],
                       pr['head'].get('sha'), pr.get('draft'), pr.get('body')]
            key = f'pr:{number}:{_fingerprint(summary)}'
            if _recent(source, key, at, f'{number}@{at}'):
                news.append(f"[PR #{number} {pr['state']}] {pr['title']} ({pr['head']['ref']})")
        except (AttributeError, KeyError, TypeError) as exc:
            raise VeilleError('API pulls : objet incomplet ; curseur conservé') from exc
    return news


def scan_comments(source, reader):
    lower, news = lower_bound(source), []
    path = 'issues/comments?sort=updated&direction=asc'
    if lower:
        path += '&' + urllib.parse.urlencode({'since': lower})
    for comment in api_all(path, reader):
        try:
            at = comment.get('updated_at') or comment['created_at']
            if not _within_window(at, lower):
                continue
            key = f"comment:{comment['id']}:{_fingerprint([at, comment['body']])}"
            if _recent(source, key, at, str(comment['id'])):
                # Conserver le correctif Claude ed8b381 : mémoriser l'écho sans
                # le présenter à Claude comme une nouvelle demande Codex.
                # Ce marqueur sert au bruit de veille, jamais à une autorisation.
                if 'Generated by [Claude Code]' in (comment['body'] or ''):
                    continue
                body = ' '.join((comment['body'] or '').split())[:300]
                news.append(f"[commentaire {comment['html_url']}] {body}")
        except (AttributeError, KeyError, TypeError) as exc:
            raise VeilleError('API issues/comments : objet incomplet ; curseur conservé') from exc
    return news


def scan(state, baseline=False, now=None, api_reader=None, git_runner=None):
    """Watermark pris AVANT les lectures ; validation indépendante par source."""
    started = timestamp(now)
    updated = migrate_state(state)
    runner, reader = git_runner or git, api_reader or api
    news, errors = [], []
    git_ready = True
    try:
        # Ne pas dépendre d'un clone initialement limité à une seule branche.
        runner('fetch', '--quiet', 'origin', '+refs/heads/*:refs/remotes/origin/*')
    except VeilleError as exc:
        errors.append(f'branches/main : {exc}')
        git_ready = False
    scans = [('prs', lambda s: scan_prs(s, reader)),
             ('comments', lambda s: scan_comments(s, reader))]
    if git_ready:
        scans[:0] = [('codex', lambda s: scan_codex(s, runner)),
                     ('main', lambda s: scan_main(s, runner))]
    for name, operation in scans:
        candidate = copy.deepcopy(updated['sources'][name])
        try:
            found = operation(candidate)
            candidate['since'] = started
            # Ne conserver que la fenêtre susceptible d'être relue, sans plafond
            # qui ferait perdre des éléments partageant le même horodatage.
            if 'seen' in candidate:
                lower = lower_bound(candidate)
                candidate['seen'] = {key: at for key, at in candidate['seen'].items()
                                     if _within_window(at, lower)}
                candidate.pop('legacy_seen', None)
            updated['sources'][name] = candidate
            if not baseline:
                news.extend(found)
        except VeilleError as exc:
            errors.append(f'{name} : {exc}')
    state.clear()
    state.update(updated)
    return ScanResult(news, errors)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--boucle', type=int, default=0, help='intervalle en secondes ; 0 = un passage')
    parser.add_argument('--baseline-silencieuse', action='store_true',
                        help='initialiser explicitement sans signaler les éléments déjà présents')
    args = parser.parse_args(argv)
    if args.boucle < 0:
        parser.error('--boucle doit être positif ou nul')
    if args.baseline_silencieuse and STATE.exists():
        parser.error('--baseline-silencieuse est réservé à un état inexistant')
    try:
        state = load_state(STATE)
        baseline = args.baseline_silencieuse
        while True:
            result = scan(state, baseline=baseline)
            save_state(STATE, state)
            if result.news:
                print('CloV_2 — nouveautés ; signal au superviseur, aucune relance automatique de Claude :')
                print('\n'.join(result.news))
            if result.errors:
                print('CloV_2 — veille incomplète ; les curseurs des sources en erreur sont conservés :', file=sys.stderr)
                print('\n'.join(result.errors), file=sys.stderr)
                return 2
            if result.news:
                return 3
            if baseline:
                print('CloV_2 : baseline silencieuse explicitement enregistrée')
            elif not args.boucle:
                print('CloV_2 : aucune nouveauté sur les sources intégralement lues')
            baseline = False
            if not args.boucle:
                return 0
            time.sleep(args.boucle)
    except VeilleError as exc:
        print(f'CloV_2 — erreur : {exc}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
