#!/usr/bin/env python3
"""Empreintes du site effectivement construit et de ses sources Git.

Le manifeste atteste une construction technique ; il ne constitue pas une
validation médicale ni une preuve que le déploiement a déjà réussi.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def bounded_deadline(registry, changed, previous_registry=None, catalog=None, previous_catalog=None, transferred=()):
    """La borne concerne les sources injectées, pas les publications ultérieures étrangères.

    Les leçons d'un cycle nocturne transféré à Claude (organisation/CYCLES_CLAUDE.json, transferred_from
    Codex) ne relèvent plus de l'autorisation nocturne : leur injection est contrôlée par la garde des
    cycles Claude (tools/cycle_claude.py) avant publication (autorisation de Vial, 15.10.2026)."""
    if not registry:
        return None
    prior_rows = {r['code']:r for c in (previous_registry or {}).get('cycles', []) for r in c['chapters']}
    prior_catalog = {r['code']:r for r in previous_catalog or []}
    current_catalog = {r['code']:r for r in catalog or []}
    for cycle in registry.get('cycles', []):
        for row in cycle['chapters']:
            code = row['code']
            if code in transferred:
                continue
            if any(p.startswith(f'chapters/{code}/') or p == f'glossary/{code.lower()}.py' or
                   p.startswith(f"assets/img/cycle{cycle['cycle']}/{code.lower()}/") for p in changed):
                return registry['deadline']
            if ('organisation/execution-20261014/cycles.json' in changed and
                    row.get('injection') and row['injection'] != prior_rows.get(code, {}).get('injection')):
                return registry['deadline']
            if ('chapters.json' in changed and current_catalog.get(code, {}).get('integrated') is True and
                    prior_catalog.get(code, {}).get('integrated') is not True):
                return registry['deadline']
    return None


def check_deadline(deadline, now=None):
    if deadline and (now or datetime.now(timezone.utc)) >= datetime.fromisoformat(deadline):
        raise ValueError('Publication nocturne refusée : autorisation expirée à 08 h 00 Europe/Zurich.')


def build(root, site, base=None):
    commit = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=root, text=True).strip()
    if not base or base == '0' * 40:
        base = commit + '^'
    changed = subprocess.check_output(['git', 'diff', '--name-only', '-z', base, commit], cwd=root).decode().split('\0')
    registry_path = root/'organisation/execution-20261014/cycles.json'
    registry = json.loads(registry_path.read_text()) if registry_path.exists() else None
    catalog = json.loads((root/'chapters.json').read_text())
    def previous(path):
        result = subprocess.run(['git','show',base+':'+path],cwd=root,capture_output=True)
        return json.loads(result.stdout) if result.returncode == 0 else None
    claude_path = root/'organisation/CYCLES_CLAUDE.json'
    claude = json.loads(claude_path.read_text()) if claude_path.exists() else {'cycles': []}
    transferred = {r['code'] for c in claude['cycles'] if c.get('transferred_from') == 'Codex' for r in c['chapters']}
    deadline = bounded_deadline(registry, changed, previous('organisation/execution-20261014/cycles.json'),
                                catalog, previous('chapters.json'), transferred)
    check_deadline(deadline)
    courses = {}
    for row in catalog:
        if not row.get('integrated'):
            continue
        code = row['code']
        files = list((root/'chapters'/code).glob('*.html')) + [root/'glossary'/f'{code.lower()}.py']
        courses[code] = {'production_cycle': row.get('production_cycle'),
                         'source_files': {p.relative_to(root).as_posix():sha256(p) for p in files if p.is_file()}}
    output = site/'publication.json'
    files = {p.relative_to(site).as_posix():sha256(p) for p in sorted(site.rglob('*')) if p.is_file() and p != output}
    manifest = {'schema_version':1, 'git_commit':commit,
                'built_at':datetime.now(timezone.utc).isoformat(),
                'scope':'construction technique ; déploiement à vérifier séparément',
                'night_publication_deadline':deadline, 'courses':courses, 'site_files':files}
    output.write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n')
    if os.environ.get('GITHUB_OUTPUT'):
        with open(os.environ['GITHUB_OUTPUT'], 'a') as stream:
            stream.write('night_deadline='+(deadline or '')+'\n')
    print(json.dumps({'manifest':str(output), 'git_commit':commit, 'site_files':len(files), 'night_deadline':deadline}))
    return manifest


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site', type=Path, required=True)
    parser.add_argument('--base', default=os.environ.get('BASE_SHA'))
    args = parser.parse_args()
    build(Path(__file__).resolve().parents[1], args.site.resolve(), args.base)
