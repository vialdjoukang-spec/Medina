#!/usr/bin/env python3
"""Workspaces de conversation locaux, sans push ni modification des gardes.

begin rafraîchit origin/main avant de créer une branche auteur. Un audit consulte
le commit propre d'une mission auteur, dans un worktree détaché. Les identités et
la lecture seule sont des contrats contrôlés par status/close, pas un sandbox OS.
Les baux expirés restent réservés : close --abandon --reason documente une levée
explicite, conserve branche et worktree et ne garantit pas l'arrêt de l'auteur.

Le verrou fcntl et les baux ne coordonnent que les worktrees du même .git commun.
Pour plusieurs clones/machines : attribution serveur des chemins via PR/registre
transactionnel, checks obligatoires et file de fusion GitHub ; ce CLI ne remplace
pas ces protections. Les droits GitHub et les veto du projet restent applicables.

Exemple : begin --actor Codex --conversation conv-12 --code I63
 --path chapters/I63 --path glossary/i63.py --worktree /tmp/medina-conv-12
"""
from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
import fcntl
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import uuid


class WorkspaceError(ValueError):
    pass


def git(root, *args):
    result = subprocess.run(['git', '-C', str(root), *args], capture_output=True, text=True)
    if result.returncode:
        raise WorkspaceError(result.stderr.strip() or 'Échec Git')
    return result.stdout.strip()


def now():
    return datetime.now(timezone.utc)


def state_directory(root):
    return Path(git(root, 'rev-parse', '--path-format=absolute', '--git-common-dir')) / 'medina-conversations'


@contextmanager
def locked(root):
    state = state_directory(root)
    state.mkdir(parents=True, exist_ok=True)
    with (state / 'allocation.lock').open('a') as handle:
        fcntl.flock(handle, fcntl.LOCK_EX)
        yield state


def records(state):
    return [json.loads(p.read_text()) for p in sorted(state.glob('*.json'))]


def save(state, mission):
    target = state / (mission['id'] + '.json')
    temporary = state / (mission['id'] + '.tmp')
    with temporary.open('w') as handle:
        json.dump(mission, handle, ensure_ascii=False, indent=2)
        handle.write('\n')
        handle.flush()
        os.fsync(handle.fileno())
    temporary.replace(target)


def overlaps(left, right):
    return left == right or left.startswith(right + '/') or right.startswith(left + '/')


def allowed_paths(code, paths):
    if not paths:
        raise WorkspaceError('Au moins un chemin de mission requis')
    clean = []
    for path in paths:
        if (not isinstance(path, str) or not path or '\\' in path or
                any(c in path for c in '\n\r\x00') or path.startswith('/') or
                any(part in {'', '.', '..'} for part in path.split('/'))):
            raise WorkspaceError('Chemin relatif invalide')
        parts = PurePosixPath(path).parts
        own = (overlaps(path, 'chapters/' + code) and path.startswith('chapters/' + code))
        own = own or path == 'glossary/' + code.lower() + '.py'
        own = own or (len(parts) >= 3 and parts[:2] == ('assets', 'img') and
                      (parts[2] == code.lower() or
                       (len(parts) >= 4 and re.fullmatch(r'cycle[0-9]+', parts[2]) and parts[3] == code.lower())))
        if not own:
            raise WorkspaceError('Chemin global ou extérieur au cours : ' + path)
        clean.append(path)
    return sorted(set(clean))


def no_symlink_ancestors(root, revision, paths):
    for path in paths:
        parts = PurePosixPath(path).parts
        for index in range(1, len(parts) + 1):
            value = '/'.join(parts[:index])
            entry = git(root, 'ls-tree', revision, '--', value)
            if entry.startswith('120000 '):
                raise WorkspaceError('Lien symbolique interdit dans le périmètre : ' + value)


def changed_files(mission):
    root = Path(mission['worktree'])
    # -z préserve les noms comprenant des espaces ; ni quoting Git ni parsing shell.
    commands = [('diff', '--name-only', '-z', mission['base_sha'], '--'),
                ('ls-files', '--others', '--exclude-standard', '-z')]
    paths = set()
    for command in commands:
        result = subprocess.run(['git', '-C', str(root), *command], capture_output=True)
        if result.returncode:
            raise WorkspaceError('Worktree indisponible : ' + str(root))
        paths.update(os.fsdecode(p) for p in result.stdout.split(b'\0') if p)
    return sorted(paths)


def inspect(mission):
    report = dict(mission)
    report['expired'] = now() >= datetime.fromisoformat(mission['expires_at'])
    try:
        changes = changed_files(mission)
    except WorkspaceError as error:
        report.update(worktree_error=str(error), changed_files=None, unauthorized_files=None)
        return report
    report['changed_files'] = changes
    report['unauthorized_files'] = changes if mission['role'] == 'audit' else [
        path for path in changes if not any(path == p or path.startswith(p + '/') for p in mission['files'])]
    return report


def begin(root, *, actor, conversation, code, worktree, files=(), role='author',
          author_mission=None, ttl_hours=24):
    if actor not in {'Codex', 'Claude'} or role not in {'author', 'audit'}:
        raise WorkspaceError('IA ou rôle invalide')
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]{0,79}', conversation):
        raise WorkspaceError('Identifiant de conversation invalide')
    if not re.fullmatch(r'[A-Z][0-9]{2}', code) or not 0 < ttl_hours <= 168:
        raise WorkspaceError('Code ou TTL invalide (maximum 168 heures)')
    destination = Path(worktree).absolute()
    with locked(root) as state:
        if destination.exists() or destination.is_symlink():
            raise WorkspaceError('Le worktree doit avoir un nouveau chemin')
        repositories = [Path(field[9:]).resolve() for field in
                        git(root, 'worktree', 'list', '--porcelain', '-z').split('\0')
                        if field.startswith('worktree ')]
        for forbidden in [*repositories, state.resolve()]:
            if destination.resolve() == forbidden or forbidden in destination.resolve().parents:
                raise WorkspaceError('Worktree imbriqué dans le dépôt ou registre interdit')
        existing = records(state)
        if any(m['state'] == 'active' and m['conversation'] == conversation for m in existing):
            raise WorkspaceError('Conversation déjà active')
        author = None
        if role == 'author':
            if author_mission:
                raise WorkspaceError('Une mission auteur ne reprend pas une mission audit')
            paths = allowed_paths(code, files)
            for mission in existing:
                if mission['state'] == 'active' and mission['role'] == 'author' and any(
                        overlaps(a, b) for a in paths for b in mission['files']):
                    raise WorkspaceError('Bail actif ou expiré à libérer explicitement : ' + mission['id'])
            # Rafraîchir seulement la référence distante ; aucun checkout/reset du tronc.
            git(root, 'fetch', 'origin', '+refs/heads/main:refs/remotes/origin/main')
            base = git(root, 'rev-parse', 'refs/remotes/origin/main^{commit}')
        else:
            author = next((m for m in existing if m['id'] == author_mission), None)
            if not author or author['role'] != 'author' or author['code'] != code:
                raise WorkspaceError('Mission auteur du même cours requise')
            if author['actor'] == actor or author['conversation'] == conversation:
                raise WorkspaceError('Audit indépendant : autre IA et autre conversation requises')
            if author['state'] == 'closed':
                base = author['final_sha']
            elif author['state'] == 'active':
                if git(author['worktree'], 'status', '--porcelain'):
                    raise WorkspaceError('Audit : committer les modifications auteur avant photographie')
                if inspect(author)['unauthorized_files']:
                    raise WorkspaceError('Mission auteur hors périmètre')
                base = git(author['worktree'], 'rev-parse', 'HEAD^{commit}')
            else:
                raise WorkspaceError('Mission abandonnée : aucune remise finale attestée')
            paths = author['files']
            if files and sorted(files) != paths:
                raise WorkspaceError('Audit : périmètre auteur exact requis')
        no_symlink_ancestors(root, base, paths)
        ident = uuid.uuid4().hex
        branch = actor.lower() + '/conversations/' + conversation + '-' + code + '-' + ident[:8]
        command = ['worktree', 'add']
        command += ['-b', branch] if role == 'author' else ['--detach']
        mission = dict(schema_version=1, id=ident, actor=actor, conversation=conversation,
                       code=code, role=role, base_sha=base, files=paths, worktree=str(destination),
                       branch=branch if role == 'author' else None, state='active',
                       author_mission=author_mission, created_at=now().isoformat(),
                       expires_at=(now() + timedelta(hours=ttl_hours)).isoformat(),
                       coordination='local au .git commun ; identité déclarative',
                       provisioned=False,
                       access='read_only_contract' if role == 'audit' else 'scoped_author_contract')
        # La réservation précède l'écriture du worktree : même une interruption
        # laisse un bail visible, jamais une création orpheline autorisant un rival.
        save(state, mission)
        try:
            git(root, *command, str(destination), base)
        except WorkspaceError as error:
            raise WorkspaceError('Création interrompue ; bail conservé ' + ident + ' : ' + str(error)) from error
        mission['provisioned'] = True
        save(state, mission)
        return mission


def status(root):
    with locked(root) as state:
        return [inspect(m) for m in records(state)]


def close(root, ident, *, abandon=False, reason=None):
    with locked(root) as state:
        mission = next((m for m in records(state) if m['id'] == ident), None)
        if not mission or mission['state'] != 'active':
            raise WorkspaceError('Mission active introuvable')
        if abandon and (not reason or not reason.strip()):
            raise WorkspaceError('Abandon : motif explicite requis')
        if not abandon:
            report = inspect(mission)
            if report.get('worktree_error'):
                raise WorkspaceError('Worktree indisponible ; abandon motivé requis')
            if report['unauthorized_files']:
                raise WorkspaceError('Modifications hors contrat ; conserver et examiner avant clôture')
            if git(mission['worktree'], 'status', '--porcelain'):
                raise WorkspaceError('Committer ou conserver explicitement par abandon les modifications')
            mission['final_sha'] = git(mission['worktree'], 'rev-parse', 'HEAD^{commit}')
        mission.update(state='abandoned' if abandon else 'closed', closed_at=now().isoformat(),
                       close_reason=reason, worktree_preserved=True)
        save(state, mission)
        return mission


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--repo', type=Path, default=Path.cwd())
    sub = parser.add_subparsers(dest='command', required=True)
    start = sub.add_parser('begin')
    start.add_argument('--actor', choices=['Codex', 'Claude'], required=True)
    start.add_argument('--conversation', required=True)
    start.add_argument('--code', required=True)
    start.add_argument('--worktree', type=Path, required=True)
    start.add_argument('--path', dest='files', action='append', default=[])
    start.add_argument('--role', choices=['author', 'audit'], default='author')
    start.add_argument('--author-mission')
    start.add_argument('--ttl-hours', type=float, default=24)
    sub.add_parser('status')
    finish = sub.add_parser('close')
    finish.add_argument('ident')
    finish.add_argument('--abandon', action='store_true')
    finish.add_argument('--reason')
    args = vars(parser.parse_args(argv))
    root, command = args.pop('repo'), args.pop('command')
    try:
        result = begin(root, **args) if command == 'begin' else close(root, **args) if command == 'close' else status(root)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (WorkspaceError, OSError, ValueError) as error:
        parser.exit(1, str(error) + '\n')


if __name__ == '__main__':
    raise SystemExit(main())
