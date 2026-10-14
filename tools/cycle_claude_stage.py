#!/usr/bin/env python3
"""Tenue du registre des cycles Claude par le coordinateur (aucune preuve fabriquée).

  python3 tools/cycle_claude_stage.py start 2 --runtime ID [--transferred-from Codex --handover CHEMIN]
  python3 tools/cycle_claude_stage.py stage G45 EN_AUDIT_CROISE --runtime ID [--source-dir DOSSIER]
        [--images CHEMIN] [--proof author=CHEMIN ...]
  python3 tools/cycle_claude_stage.py cross-phase 2 CHEMIN          # clôture initiale des audits croisés
  python3 tools/cycle_claude_stage.py close 2 CHEMIN --runtime ID    # reçu de clôture sans réserve

L'outil met à jour organisation/CYCLES_CLAUDE.json (références {path, sha256} calculées sur les
fichiers existants) et ajoute l'événement au journal append-only. Il ne rédige ni ne juge aucune
revue : la garde tools/cycle_claude.py vérifie ensuite toutes les preuves.
"""
import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import cycle_claude as G  # noqa: E402
import night_cycle as N  # noqa: E402
import tetrade_cycle as C  # noqa: E402


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def ref(path):
    if not (ROOT / path).is_file():
        sys.exit(f'Preuve absente : {path}')
    return {'path': path, 'sha256': sha(path)}


def now():
    return datetime.now(timezone.utc).isoformat()


def load():
    path = ROOT / G.REGISTRY
    if path.exists():
        return json.loads(path.read_text(encoding='utf-8'))
    return {'schema_version': 1, 'authority': G.AUTHORITY, 'authority_sha256': sha(G.AUTHORITY),
            'plan_sha256': sha(G.PLAN), 'coordinator': G.COORDINATOR, 'not_before': G.NOT_BEFORE, 'cycles': []}


def save(data, event):
    (ROOT / G.REGISTRY).write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    with open(ROOT / G.JOURNAL, 'a', encoding='utf-8') as journal:
        journal.write(json.dumps(event, ensure_ascii=False) + '\n')
    print(f"{event['event']} : {G.REGISTRY} et {G.JOURNAL} mis à jour")


class Disk:
    def read(self, path, required=True):
        p = ROOT / path
        if not p.is_file():
            if required:
                raise C.CycleError('Absent ' + path)
            return None
        return p.read_bytes()


def start(a):
    data = load()
    if any(c['state'] == 'ACTIF' for c in data['cycles']):
        sys.exit('Un cycle Claude est déjà actif')
    at = now()
    rows = [dict(code=code, fragment_id=fragment, production_cycle=a.cycle, writer=f'C{a.cycle:02d}-R-{tag}',
                 cross_reviewer=f'C{a.cycle:02d}-R-{N.CROSS[tag]}', counter_reviewer=f'C{a.cycle:02d}-CA-{tag}',
                 status='EN_PRODUCTION', source_dir=None, files={}, images=None, **{k: None for k in G.PROOFS})
            for code, fragment, tag in N.missions(Disk(), a.cycle)]
    data['cycles'].append({'cycle': a.cycle, 'owner': 'Claude', 'state': 'ACTIF', 'started_at': at,
                           'transferred_from': a.transferred_from,
                           'handover': ref(a.handover) if a.handover else None,
                           'cross_phase': None, 'closed_at': None, 'closure': None, 'budget': None, 'chapters': rows})
    save(data, {'at': at, 'event': 'cycle_started', 'cycle': a.cycle, 'coordinator_runtime': a.runtime})


def active(data):
    cycles = [c for c in data['cycles'] if c['state'] == 'ACTIF']
    if not cycles:
        sys.exit('Aucun cycle Claude actif')
    return cycles[0]


def stage(a):
    data = load()
    cycle = active(data)
    row = next((r for r in cycle['chapters'] if r['code'] == a.code), None)
    if row is None:
        sys.exit(f'{a.code} absent du cycle actif')
    if a.status not in C.STATES or C.STATES.index(a.status) < C.STATES.index(row['status']):
        sys.exit('Statut inconnu ou régression')
    locked = C.STATES.index(row['status']) >= C.STATES.index('INJECTE')
    for item in a.proof or []:
        key, _, path = item.partition('=')
        if key not in G.PROOFS or not path:
            sys.exit(f'Preuve invalide : {item}')
        if locked and key != 'publication':
            sys.exit('Cours injecté : seules les preuves de publication peuvent être ajoutées')
        row[key] = ref(path)
    if a.source_dir:
        if locked:
            sys.exit('Cours injecté : dossier source immuable')
        row['source_dir'] = a.source_dir
    if not locked and row['source_dir']:
        base = ROOT / row['source_dir']
        files = sorted(p for p in (base / 'chapters' / row['code']).rglob('*') if p.is_file())
        glossary = base / 'glossary' / (row['code'].lower() + '.py')
        if glossary.is_file():
            files.append(glossary)
        row['files'] = {str(p.relative_to(base)): hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    if a.images:
        row['images'] = ref(a.images)
    elif row['images'] and not locked:
        row['images'] = ref(row['images']['path'])
    row['status'] = a.status
    save(data, {'at': now(), 'event': 'stage_recorded', 'cycle': cycle['cycle'], 'code': row['code'],
                'status': row['status'], 'proofs': {k: row[k] for k in G.PROOFS}, 'runtime_agent_id': a.runtime})


def cross_phase(a):
    data = load()
    cycle = active(data)
    if cycle['cycle'] != a.cycle or cycle.get('cross_phase'):
        sys.exit('Cycle inactif ou clôture croisée déjà archivée')
    cycle['cross_phase'] = ref(a.path)
    save(data, {'at': now(), 'event': 'cross_phase_archived', 'cycle': a.cycle, 'cross_phase': cycle['cross_phase']})


def close(a):
    data = load()
    cycle = active(data)
    if cycle['cycle'] != a.cycle or any(r['status'] != 'PUBLIE_VERIFIE' for r in cycle['chapters']):
        sys.exit('Clôture prématurée')
    at = now()
    cycle.update(state='CLOTURE', closed_at=at, closure=ref(a.path))
    save(data, {'at': at, 'event': 'cycle_closed', 'cycle': a.cycle, 'closure': cycle['closure'],
                'coordinator_runtime': a.runtime})


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest='action', required=True)
    s = sub.add_parser('start'); s.add_argument('cycle', type=int); s.add_argument('--runtime', required=True)
    s.add_argument('--transferred-from', choices=['Codex']); s.add_argument('--handover')
    s.set_defaults(run=start)
    s = sub.add_parser('stage'); s.add_argument('code'); s.add_argument('status'); s.add_argument('--runtime', required=True)
    s.add_argument('--source-dir'); s.add_argument('--images'); s.add_argument('--proof', action='append')
    s.set_defaults(run=stage)
    s = sub.add_parser('cross-phase'); s.add_argument('cycle', type=int); s.add_argument('path'); s.set_defaults(run=cross_phase)
    s = sub.add_parser('close'); s.add_argument('cycle', type=int); s.add_argument('path'); s.add_argument('--runtime', required=True)
    s.set_defaults(run=close)
    a = p.parse_args()
    if a.action == 'start' and bool(a.transferred_from) != bool(a.handover):
        p.error('--transferred-from et --handover vont ensemble')
    a.run(a)


if __name__ == '__main__':
    main()
