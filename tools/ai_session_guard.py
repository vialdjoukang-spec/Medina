#!/usr/bin/env python3
"""Scoped, declarative mission guard and central Git reservation transactions.

Trust config and approvals come from --base, never the candidate tree. The
registry branch must already exist and be protected by the repository owner.
Normal pushes serialize reservations across clones; no local lock is claimed to
coordinate machines. No expiry silently releases a reservation. Actor strings
are provenance declarations, not authenticated identities or medical approval.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

CONFIG = '.medina/ai-session-guard.json'
MISSIONS = '.medina/missions/'
REGISTRY = 'registry.json'
OUTPUTS = 'docs/collaboration/ssp-v2/execution/'
SYSTEMS = {'S08', 'S05', 'S04', 'S06'}
SHA = re.compile(r'[0-9a-f]{40}')
ID = re.compile(r'[A-Za-z0-9][A-Za-z0-9_-]{0,79}')


class GuardError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise GuardError(message)


def git(root, *args, data=None, env=None, optional=False):
    result = subprocess.run(['git', '-C', str(root), *args], input=data,
                            capture_output=True, env=env)
    if result.returncode:
        if optional:
            return None
        raise GuardError(result.stderr.decode(errors='replace').strip() or 'Git failed')
    return result.stdout


def commit(root, revision):
    require(isinstance(revision, str) and SHA.fullmatch(revision), 'Exact 40-character commit SHA required')
    require(git(root, 'cat-file', '-t', revision).strip() == b'commit', 'Commit required')
    return revision


def read(root, revision, path, optional=False):
    return git(root, 'show', f'{revision}:{path}', optional=optional)


def load(raw, label):
    try:
        return json.loads(raw)
    except (ValueError, TypeError, UnicodeDecodeError) as error:
        raise GuardError('Invalid JSON: ' + label) from error


def canonical(value):
    return (json.dumps(value, sort_keys=True, ensure_ascii=False, indent=2) + '\n').encode()


def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()


def path_valid(path):
    return (isinstance(path, str) and path and not path.startswith('/') and
            '\\' not in path and not any(ord(c) < 32 or ord(c) == 127 for c in path) and
            not any(p in {'', '.', '..'} for p in path.split('/')))


def overlaps(a, b):
    return a == b or a.startswith(b + '/') or b.startswith(a + '/')


def config(root, base):
    raw = read(root, base, CONFIG, optional=True)
    if raw is None:
        return None
    cfg = load(raw, CONFIG)
    require(isinstance(cfg, dict) and cfg.get('schema_version') == 1, 'Invalid guard configuration')
    if not cfg.get('enabled', False):
        return None
    mapping = cfg.get('code_systems')
    require(isinstance(mapping, dict) and mapping, 'code_systems mapping required')
    require(all(re.fullmatch(r'[A-Z][0-9]{2}', k) and v in SYSTEMS for k, v in mapping.items()),
            'Guard scope is limited to S08/S05/S04/S06')
    ref = cfg.get('registry_ref', '')
    require(isinstance(ref, str) and ref.startswith('refs/heads/') and
            git(root, 'check-ref-format', ref, optional=True) is not None,
            'Valid dedicated registry branch required')
    require(ref not in {'refs/heads/main', 'refs/heads/master'}, 'Registry must be a dedicated branch')
    shared = cfg.get('shared_paths', ['chapters.json'])
    require(isinstance(shared, list) and all(path_valid(p) for p in shared), 'Invalid shared paths')
    require('chapters.json' in shared, 'chapters.json must be a shared path')
    return cfg


def code_of(path, cfg):
    patterns = (r'chapters/([A-Z][0-9]{2})(?:/|$)',
                r'glossary/([a-z][0-9]{2})\.py$',
                r'assets/img/(?:cycle[0-9]+/)?([a-z][0-9]{2})(?:/|$)')
    for pattern in patterns:
        match = re.match(pattern, path)
        if match and match.group(1).upper() in cfg['code_systems']:
            return match.group(1).upper()
    return None


def is_doc(path):
    return (path.startswith('docs/') and not overlaps(path, OUTPUTS.rstrip('/'))) or path in {'AGENTS.md', 'README.md', 'COORDINATION.md'}


def shared_path(path, cfg):
    return any(overlaps(path, p) for p in cfg.get('shared_paths', ['chapters.json']))


def regular_ancestors(root, revision, path):
    parts = path.split('/')
    for index in range(1, len(parts) + 1):
        entry = git(root, 'ls-tree', revision, '--', '/'.join(parts[:index]))
        require(not entry.startswith((b'120000 ', b'160000 ')), 'Symlink/submodule in source path')


def manifest(root, base, ident, cfg):
    require(isinstance(ident, str) and ID.fullmatch(ident), 'Invalid mission ID')
    value = load(read(root, base, MISSIONS + ident + '.json'), 'mission ' + ident)
    require(isinstance(value, dict) and value.get('schema_version') == 1 and value.get('id') == ident,
            'Invalid mission schema/ID')
    require(value.get('state') == 'active', 'Mission must already be approved active in trusted base')
    for name in ('actor', 'conversation', 'owner', 'assigned_by', 'branch'):
        require(isinstance(value.get(name), str) and value[name].strip() and
                not any(ord(c) < 32 for c in value[name]), 'Missing mission field: ' + name)
    require(git(root, 'check-ref-format', '--branch', value['branch'], optional=True) is not None,
            'Invalid mission branch')
    require(value['branch'] not in {'main', 'master'} and value['branch'] != cfg['registry_ref'][len('refs/heads/'):],
            'Mission requires its own branch, distinct from integration/registry')
    require(value.get('owner') in {'Codex', 'Claude'}, 'Owner must declare Codex/Claude allocation')
    require(value.get('role') in {'author', 'integrator', 'audit'}, 'Invalid mission role')
    require(type(value.get('generation')) is int and value['generation'] > 0, 'Positive generation required')
    commit(root, value.get('base_sha'))
    require(git(root, 'merge-base', '--is-ancestor', value['base_sha'], base, optional=True) is not None,
            'Mission base must be an ancestor of trusted base')
    codes = value.get('codes', [value.get('code')])
    require(isinstance(codes, list) and codes and len(set(codes)) == len(codes) and
            all(isinstance(c, str) and c in cfg['code_systems'] for c in codes), 'Mission codes outside scope')
    require(value['role'] == 'integrator' or len(codes) == 1, 'One course per author/audit mission')
    paths = value.get('paths')
    require(isinstance(paths, list) and paths and all(path_valid(p) for p in paths), 'Mission paths required')
    for path in paths:
        own = value['role'] != 'audit' and code_of(path, cfg) in codes
        output = path == OUTPUTS + ident or path.startswith(OUTPUTS + ident + '/')
        shared = value['role'] == 'integrator' and (shared_path(path, cfg) or path == CONFIG or overlaps(path, MISSIONS.rstrip('/')))
        require(own or shared or output,
                'Mission path outside owned course: ' + path)
        regular_ancestors(root, base, path)
    return value


def approved(root, base, cfg):
    names = git(root, 'ls-tree', '-r', '--name-only', base, '--', MISSIONS).decode().splitlines()
    values = []
    for name in names:
        require(re.fullmatch(re.escape(MISSIONS) + r'[A-Za-z0-9][A-Za-z0-9_-]{0,79}\.json', name),
                'Invalid mission filename')
        raw = load(read(root, base, name), name)
        require(isinstance(raw, dict), 'Mission must be a JSON object')
        if raw.get('state') == 'active':
            values.append(manifest(root, base, Path(name).stem, cfg))
    require(len({m['branch'] for m in values}) == len(values), 'Multiple active missions on one branch')
    require(len({(m['actor'], m['conversation']) for m in values}) == len(values),
            'Multiple active missions for one actor/conversation')
    return values


def registry(root, revision):
    commit(root, revision)
    state = load(read(root, revision, REGISTRY), REGISTRY)
    require(isinstance(state, dict) and state.get('schema_version') == 1 and
            isinstance(state.get('reservations'), list), 'Invalid central registry')
    for item in state['reservations']:
        require(isinstance(item, dict) and ID.fullmatch(item.get('id', '')) and
                item.get('state') in {'active', 'released'} and
                type(item.get('generation')) is int and item['generation'] > 0 and
                isinstance(item.get('codes'), list) and item['codes'] and
                all(isinstance(c, str) and re.fullmatch(r'[A-Z][0-9]{2}', c) for c in item['codes']) and
                isinstance(item.get('paths'), list) and item['paths'] and
                all(path_valid(p) for p in item['paths']) and
                item.get('role') in {'author', 'integrator', 'audit'} and
                isinstance(item.get('manifest_sha256'), str) and
                re.fullmatch(r'[0-9a-f]{64}', item['manifest_sha256']), 'Invalid registry reservation')
    active = [m for m in state['reservations'] if m['state'] == 'active']
    require(len({m['id'] for m in active}) == len(active), 'Duplicate active reservation')
    for index, left in enumerate(active):
        for right in active[index + 1:]:
            require(not collides(left, right), 'Central registry contains conflicting active reservations')
    return state


def course_writer(item):
    # Governance and audit-output missions may mention a course for accounting
    # without taking its source lock or consuming its generation fence.
    mapping = {'code_systems': dict.fromkeys(item['codes'])}
    return item['role'] != 'audit' and any(code_of(p, mapping) or p == 'chapters.json' for p in item['paths'])


def collides(left, right):
    path_collision = any(overlaps(a, b) for a in left['paths'] for b in right['paths'])
    code_collision = (course_writer(left) and course_writer(right) and
                      bool(set(left['codes']) & set(right['codes'])))
    return path_collision or code_collision


def fetch_registry(root, remote, cfg):
    require(isinstance(remote, str) and re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]*', remote),
            'Use a configured Git remote name')
    git(root, 'fetch', '--no-tags', remote, cfg['registry_ref'])
    return git(root, 'rev-parse', 'FETCH_HEAD^{commit}').decode().strip()


def transact(root, remote, cfg, expected, state, message):
    """One normal push. Concurrent sibling commits cannot both be accepted."""
    with tempfile.TemporaryDirectory(prefix='medina-registry-') as directory:
        env = dict(os.environ, GIT_INDEX_FILE=str(Path(directory) / 'index'),
                   GIT_AUTHOR_NAME='MEDINA session registry', GIT_AUTHOR_EMAIL='registry@medina.invalid',
                   GIT_COMMITTER_NAME='MEDINA session registry', GIT_COMMITTER_EMAIL='registry@medina.invalid')
        git(root, 'read-tree', expected, env=env)
        blob = git(root, 'hash-object', '-w', '--stdin', data=canonical(state)).decode().strip()
        git(root, 'update-index', '--add', '--cacheinfo', '100644', blob, REGISTRY, env=env)
        tree = git(root, 'write-tree', env=env).decode().strip()
        new = git(root, 'commit-tree', tree, '-p', expected, data=(message + '\n').encode(), env=env).decode().strip()
        # No force, no force-with-lease, no automatic retry or lost-update overwrite.
        git(root, 'push', remote, new + ':' + cfg['registry_ref'])
        return new


def acquire(root, base, ident, remote='origin', expected_registry=None):
    commit(root, base)
    cfg = config(root, base)
    require(cfg is not None, 'Guard not enabled in trusted base')
    m = manifest(root, base, ident, cfg)
    approved(root, base, cfg)
    parent = fetch_registry(root, remote, cfg)
    require(expected_registry is None or expected_registry == parent, 'Registry advanced; review current reservations')
    state = registry(root, parent)
    codes = m.get('codes', [m.get('code')])
    item = dict(id=m['id'], generation=m['generation'], codes=codes, paths=m['paths'], role=m['role'],
                actor=m['actor'], conversation=m['conversation'], branch=m['branch'],
                manifest_sha256=digest(m), state='active', approved_base_sha=base)
    for previous in state['reservations']:
        require(not (previous['id'] == ident and previous['generation'] >= item['generation']),
                'Stale or already acquired mission generation')
        if course_writer(previous) and course_writer(item) and set(previous['codes']) & set(codes):
            require(item['generation'] > previous['generation'], 'Stale course generation')
        if previous['state'] == 'active':
            require(previous.get('branch') != item['branch'] and
                    (previous.get('actor'), previous.get('conversation')) != (item['actor'], item['conversation']),
                    'Branch or actor/conversation already reserved')
            require(not collides(previous, item), 'Active course/path collision: ' + previous['id'])
    state['reservations'].append(item)
    return transact(root, remote, cfg, parent, state, 'Acquire mission ' + ident)


def release(root, base, ident, generation, reason, remote='origin', expected_registry=None):
    require(isinstance(reason, str) and reason.strip(), 'Explicit release reason required; preserve work before releasing')
    commit(root, base)
    cfg = config(root, base)
    require(cfg is not None, 'Guard not enabled in trusted base')
    parent = fetch_registry(root, remote, cfg)
    require(expected_registry is None or expected_registry == parent, 'Registry advanced; review current reservations')
    state = registry(root, parent)
    matches = [m for m in state['reservations'] if m['id'] == ident and m['generation'] == generation and m['state'] == 'active']
    require(len(matches) == 1, 'Active reservation/generation not found')
    matches[0].update(state='released', release_reason=reason)
    return transact(root, remote, cfg, parent, state, 'Release mission ' + ident)


def changes(root, base, head):
    return [os.fsdecode(p) for p in git(root, 'diff', '--no-renames', '--name-only', '-z', base, head, '--').split(b'\0') if p]


def catalogue_changes(root, base, head, cfg):
    """Compare rows by canonical code; unrelated catalogue rows must survive exactly."""
    def rows(rev):
        raw = read(root, rev, 'chapters.json', optional=True)
        value = [] if raw is None else load(raw, 'chapters.json')
        require(isinstance(value, list) and all(isinstance(x, dict) and isinstance(x.get('code'), str) for x in value),
                'Invalid chapters.json catalogue')
        result = {item['code']: item for item in value}
        require(len(result) == len(value), 'Duplicate catalogue code')
        return result
    before, after = rows(base), rows(head)
    return {code for code in set(before) | set(after) if before.get(code) != after.get(code)}


def check(root, base, head, branch, registry_sha=None, remote='origin', integrated=False):
    commit(root, base)
    commit(root, head)
    cfg = config(root, base)
    if cfg is None:
        return {'guard': 'inactive', 'reason': 'No enabled configuration in trusted base'}
    changed = changes(root, base, head)
    # A replaced parent directory may hide future protected files even when no
    # protected child was tracked yet (notably a newly symlinked glossary).
    source_parents = {'chapters', 'glossary', 'assets', 'assets/img'}
    protected = [p for p in changed if code_of(p, cfg) or p in source_parents or
                 re.fullmatch(r'assets/img/cycle[0-9]+', p)]
    catalog_codes = catalogue_changes(root, base, head, cfg) if 'chapters.json' in changed else set()
    shared = [p for p in changed if shared_path(p, cfg)]
    # Changes limited to older systems and their catalogue do not activate this guard.
    governance = [p for p in changed if p == CONFIG or p.startswith(MISSIONS)]
    outputs = [p for p in changed if overlaps(p, OUTPUTS.rstrip('/'))]
    if not protected and not governance and not outputs and not (catalog_codes & set(cfg['code_systems'])) and not any(p != 'chapters.json' for p in shared):
        return {'guard': 'not-applicable', 'changed_files': changed}
    missions = approved(root, base, cfg)
    current = None
    state = None
    if integrated:
        current = registry_sha or fetch_registry(root, remote, cfg)
        state = registry(root, current)
        # A merge loses the author's branch name. This post-push check detects
        # unallocated changes, but cannot prove that a pull request was used.
        selected = [m for m in missions if any(r['id'] == m['id'] and r['state'] == 'active' and r['generation'] == m['generation'] and r['manifest_sha256'] == digest(m) for r in state['reservations']) and all(is_doc(p) or any(p == q or p.startswith(q + '/') for q in m['paths']) for p in changed)]
    else:
        selected = [m for m in missions if m['branch'] == branch]
    require(len(selected) == 1, 'Exactly one preapproved active mission for candidate branch required')
    m = selected[0]
    require(m['role'] != 'audit' or not (protected or shared or governance), 'Audit role cannot modify protected sources')
    require(MISSIONS + m['id'] + '.json' not in changed, 'Mission cannot change its own approval')
    require(not governance or m['role'] == 'integrator', 'Governance changes require an integrator')
    require(not (governance and (protected or shared)), 'Separate governance changes from source/shared integration')
    require(git(root, 'merge-base', '--is-ancestor', m['base_sha'], head, optional=True) is not None,
            'Candidate does not descend from mission base')
    codes = m.get('codes', [m.get('code')])
    for path in changed:
        require(path_valid(path), 'Invalid candidate path')
        if is_doc(path):
            continue
        require(any(overlaps(path, p) and (path == p or path.startswith(p + '/')) for p in m['paths']),
                'Candidate change outside mission paths: ' + path)
        require(code_of(path, cfg) in codes or (path == OUTPUTS + m['id'] or path.startswith(OUTPUTS + m['id'] + '/')) or
                (m['role'] == 'integrator' and (shared_path(path, cfg) or path in governance)),
                'Candidate change outside owned course: ' + path)
        # Symlinks/submodules can redirect reads outside course scope; reject at every ancestor.
        for revision in (base, head):
            regular_ancestors(root, revision, path)
    require(not shared or m['role'] == 'integrator', 'Shared files require an integrator mission')
    require(catalog_codes <= set(codes), 'Catalogue changed unrelated course/system rows')
    if state is None:
        current = registry_sha or fetch_registry(root, remote, cfg)
        state = registry(root, current)
    reservations = [r for r in state['reservations'] if r['id'] == m['id'] and r['state'] == 'active']
    require(len(reservations) == 1 and reservations[0]['generation'] == m['generation'] and
            reservations[0]['manifest_sha256'] == digest(m), 'Missing/current generation mismatch in central reservation')
    return {'guard': 'passed', 'mission': m['id'], 'generation': m['generation'],
            'registry_sha': current, 'changed_files': changed, 'identity': 'declarative, not authenticated'}


def start(root, base, ident, actor, conversation, remote='origin', registry_sha=None, worktree=None):
    commit(root, base)
    cfg = config(root, base)
    require(cfg is not None, 'Guard not enabled in trusted base')
    m = manifest(root, base, ident, cfg)
    require(m['actor'] == actor and m['conversation'] == conversation, 'Declared session does not match assigned mission')
    workspace = worktree or root
    require(git(workspace, 'symbolic-ref', '--short', 'HEAD', optional=True) == (m['branch'] + '\n').encode(),
            'Start from the mission branch in its own worktree')
    require(git(workspace, 'rev-parse', 'HEAD').decode().strip() == base,
            'Mission worktree must start at the exact trusted base')
    require(not git(workspace, 'status', '--porcelain', '-z'), 'Mission worktree must start clean')
    require(git(workspace, 'rev-parse', '--path-format=absolute', '--git-common-dir').strip() ==
            git(root, 'rev-parse', '--path-format=absolute', '--git-common-dir').strip(),
            'Worktree must belong to the checked repository')
    revision = registry_sha or fetch_registry(root, remote, cfg)
    state = registry(root, revision)
    require(any(r['id'] == ident and r['state'] == 'active' and r['generation'] == m['generation'] and
                r['manifest_sha256'] == digest(m) for r in state['reservations']), 'Mission is not centrally acquired at approved generation')
    return dict(mission=m, registry_sha=revision, identity='declarative, not authenticated')


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', default='.')
    sub = parser.add_subparsers(dest='command', required=True)
    for name in ('acquire', 'release', 'check', 'status', 'start'):
        cmd = sub.add_parser(name)
        cmd.add_argument('--base', required=True, help='Trusted exact commit SHA (never candidate HEAD by assumption)')
        cmd.add_argument('--remote', default='origin')
        if name in {'acquire', 'release', 'start'}:
            cmd.add_argument('mission')
        if name in {'acquire', 'release'}:
            cmd.add_argument('--expected-registry', help='Reject if central registry changed since review')
        if name == 'start':
            cmd.add_argument('--worktree', help='Existing clean worktree on the approved mission branch at --base')
            cmd.add_argument('--actor', required=True)
            cmd.add_argument('--conversation', required=True)
        if name == 'release':
            cmd.add_argument('--generation', required=True, type=int)
            cmd.add_argument('--reason', required=True)
        if name == 'check':
            cmd.add_argument('--integrated', action='store_true', help='Post-push check; cannot prove PR review')
            cmd.add_argument('--head', required=True)
            cmd.add_argument('--branch', required=True)
            cmd.add_argument('--registry-sha', help='Trusted registry snapshot already fetched by controller')
    args = parser.parse_args(argv)
    try:
        if args.command == 'acquire':
            result = {'registry_sha': acquire(args.root, args.base, args.mission, args.remote, args.expected_registry)}
        elif args.command == 'release':
            result = {'registry_sha': release(args.root, args.base, args.mission, args.generation, args.reason,
                                               args.remote, args.expected_registry)}
        elif args.command == 'check':
            result = check(args.root, args.base, args.head, args.branch, args.registry_sha, args.remote, args.integrated)
        elif args.command == 'start':
            result = start(args.root, args.base, args.mission, args.actor, args.conversation, args.remote, worktree=args.worktree)
        else:
            cfg = config(args.root, commit(args.root, args.base))
            require(cfg is not None, 'Guard not enabled in trusted base')
            revision = fetch_registry(args.root, args.remote, cfg)
            result = dict(registry_sha=revision, **registry(args.root, revision))
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (GuardError, OSError) as error:
        print('AI session guard: ' + str(error), file=__import__('sys').stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
