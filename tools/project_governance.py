"""Veto commun du projet : journal déclaratif, contrôles locaux et CI."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
from datetime import datetime, timezone
from uuid import uuid4

ROOT = Path(__file__).resolve().parents[1]
JOURNAL = 'organisation/governance_events.jsonl'
ACTORS = {'Codex', 'Claude', 'Vial'}


class GovernanceError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise GovernanceError(message)


def events(raw):
    try:
        data = [json.loads(line) for line in (raw or b'').splitlines() if line.strip()]
    except (ValueError, TypeError) as error:
        raise GovernanceError('Journal de gouvernance illisible') from error
    active, identifiers = {}, set()
    for row in data:
        ident, actor = row.get('id'), row.get('actor')
        require(isinstance(ident, str) and ident and ident not in identifiers, 'Identifiant de gouvernance absent ou dupliqué')
        identifiers.add(ident)
        require(actor in ACTORS and isinstance(row.get('reason'), str) and row['reason'].strip(), 'Auteur ou motif de gouvernance absent')
        try:
            require(datetime.fromisoformat(row['at']).utcoffset() is not None, 'Date de gouvernance sans fuseau')
        except (ValueError, TypeError, KeyError) as error:
            raise GovernanceError('Date de gouvernance invalide') from error
        if row.get('event') == 'veto':
            scope = row.get('scope')
            require(isinstance(scope, str) and scope and '\\' not in scope and
                    (scope == '*' or (not scope.startswith('/') and all(p not in {'', '.', '..'} for p in scope.rstrip('/').split('/')))) and
                    not any(c in scope for c in '\n\r\x00'), 'Périmètre de veto invalide')
            require(row.get('operations') in (['change'], ['publish'], ['change', 'publish']), 'Opérations de veto invalides')
            active[ident] = row
        elif row.get('event') == 'release':
            target = row.get('veto_id')
            require(target in active, 'Veto absent ou déjà levé')
            require(actor == active[target]['actor'] or actor == 'Vial', 'Une IA ne peut lever le veto de l’autre')
            if actor == 'Vial':
                require(isinstance(row.get('authority'), dict) and row['authority'].get('path') and
                        isinstance(row['authority'].get('sha256'), str) and len(row['authority']['sha256']) == 64,
                        'Levée humaine : instruction de provenance requise')
            del active[target]
        else:
            raise GovernanceError('Événement de gouvernance inconnu')
    return data, active


def matches(scope, path):
    return scope == '*' or path == scope.rstrip('/') or path.startswith(scope.rstrip('/') + '/')


def check(before, after, operation='change'):
    old_raw, new_raw = before.read(JOURNAL, required=False), after.read(JOURNAL, required=False)
    require(not old_raw or (new_raw is not None and new_raw.startswith(old_raw)), 'Journal de gouvernance : historique réécrit ou supprimé')
    _, old_active = events(old_raw)
    data, active = events(new_raw)
    for row in data:
        if row.get('event') == 'release' and row['actor'] == 'Vial':
            ref = row['authority']
            require(hashlib.sha256(after.read(ref['path'])).hexdigest() == ref['sha256'], 'Instruction humaine différente de son empreinte')
    changed = {p for p in before.entries.keys() | after.entries.keys() if before.entries.get(p) != after.entries.get(p)}
    # Le journal doit rester modifiable pour poser ou lever un veto global.
    changed.discard(JOURNAL)
    for ident, veto in active.items():
        if operation in veto['operations'] and (operation == 'publish' or any(matches(veto['scope'], p) for p in changed)):
            raise GovernanceError(f"Veto {ident} ({veto['actor']}) : {veto['reason']}")
    # Un veto actif dans la base reste applicable aux changements qui le lèvent :
    # séparer la levée et l'opération rend la décision consultable avant son effet.
    for ident, veto in old_active.items():
        if ident not in active and changed and operation in veto['operations'] and any(matches(veto['scope'], p) for p in changed):
            raise GovernanceError('Lever le veto dans un commit distinct avant l’opération : ' + ident)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    checker = sub.add_parser('check')
    checker.add_argument('--revision', default='HEAD')
    checker.add_argument('--operation', choices=('change', 'publish'), default='publish')
    for name in ('veto', 'release'):
        cmd = sub.add_parser(name)
        cmd.add_argument('--actor', choices=sorted(ACTORS), required=True)
        cmd.add_argument('--reason', required=True)
        if name == 'veto':
            cmd.add_argument('--scope', default='*')
            cmd.add_argument('--operations', nargs='+', choices=('change', 'publish'), default=['change', 'publish'])
        else:
            cmd.add_argument('--veto-id', required=True)
            cmd.add_argument('--authority')
    args = parser.parse_args()
    try:
        if args.command == 'check':
            try:
                from tools.espace import GitTree
            except ModuleNotFoundError:
                from espace import GitTree
            tree = GitTree(ROOT, args.revision)
            check(tree, tree, args.operation)
            print('Gouvernance : aucun veto applicable à ' + args.operation)
            return 0
        path = ROOT / JOURNAL
        raw = path.read_bytes() if path.exists() else b''
        row = dict(id=uuid4().hex, actor=args.actor, event=args.command, reason=args.reason,
                   at=datetime.now(timezone.utc).isoformat())
        if args.command == 'veto':
            row.update(scope=args.scope, operations=sorted(set(args.operations), key=('change', 'publish').index))
        else:
            row['veto_id'] = args.veto_id
            if args.actor == 'Vial':
                require(args.authority is not None, '--authority requis pour une instruction humaine')
                ref = Path(args.authority)
                require(not ref.is_absolute() and '..' not in ref.parts, 'Instruction dans le dépôt requise')
                row['authority'] = {'path': ref.as_posix(), 'sha256': hashlib.sha256((ROOT / ref).read_bytes()).hexdigest()}
        candidate = raw + (json.dumps(row, ensure_ascii=False) + '\n').encode()
        events(candidate)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(candidate)
        print(row['id'])
        return 0
    except (GovernanceError, OSError, ValueError) as error:
        print('REFUS gouvernance : ' + str(error), file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
