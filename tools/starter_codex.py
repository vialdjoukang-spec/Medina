#!/usr/bin/env python3
"""Independent, fail-closed Codex campaign controller. Python stdlib only."""
import argparse
import copy
import hashlib
from html.parser import HTMLParser
import json
import os
from pathlib import Path, PurePosixPath
import re
import signal
import socket
import subprocess
import tempfile
import time
import urllib.request
import urllib.parse
import uuid

REF = 'refs/heads/medina/7-starter-codex'
FIRST = ['I63', 'G01', 'E10', 'E05', 'N17', 'D69', 'D64']
SHA = re.compile(r'[0-9a-f]{40}')
DIGEST = re.compile(r'[0-9a-f]{64}')
PAGES_ORIGIN = 'https://vialdjoukang-spec.github.io/Medina/'
PAGES_WORKFLOW = 368800567
PAGES_REPOSITORY = 'vialdjoukang-spec/Medina'
FRAGMENT_SLUGS = {'S08': 'nerveux', 'S05': 'endocrinien-metabolique', 'S04': 'renal-voies-urinaires', 'S06': 'hematopoietique-lymphatique'}


class Blocked(RuntimeError):
    pass


def need(ok, message):
    if not ok:
        raise Blocked(message)


def command(args, cwd, data=None, env=None, timeout=120):
    result = subprocess.run(args, cwd=cwd, input=data, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, env=env, timeout=timeout)
    # Never echo raw child output: authentication diagnostics can contain secrets.
    need(result.returncode == 0, 'Command failed: ' + ' '.join(args[:3]))
    return result.stdout


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':')).encode()


def safe_path(path):
    need(isinstance(path, str) and path and '\\' not in path, 'Invalid path')
    p = PurePosixPath(path)
    need(not p.is_absolute() and '..' not in p.parts and '.git' not in p.parts,
         'Unsafe repository path')
    need('claude' not in path.lower(), 'Claude paths are outside this engine')
    return path


def validate_config(cfg):
    need(cfg.get('schema_version') == 1, 'Unsupported config')
    queue = cfg.get('queue', [])
    need(len(queue) == 77 and len({q['code'] for q in queue}) == 77, 'Exactly 77 unique lessons required')
    need([q['code'] for q in queue[:7]] == FIRST, 'Must adopt existing first seven')
    need(sum(q.get('mode') == 'existing' for q in queue) == 52 and
         sum(q.get('mode') == 'production' for q in queue) == 25, 'Expected 52 existing plus 25 new')
    for item in queue:
        need(item.get('owner') == 'Codex', 'Only Codex allocation allowed')
        need(re.fullmatch(r'[A-Z][0-9]{2}', item['code']), 'Invalid lesson code')
        safe_path(item['closure_path'])
        for role in ('MED', 'LANG', 'INTEGRATE'):
            ident = item['missions'][role]
            need(re.fullmatch(r'[A-Za-z0-9_-]{1,80}', ident) and 'CLAUDE' not in ident.upper(), 'Invalid owned mission')
        if item['mode'] == 'production':
            need('PRODUCE' in item['missions'], 'Production mission required')
            safe_path(item['production_receipt'])
    need(cfg.get('worker_backend', 'codex_cli') in ('codex_cli', 'native_handoff'), 'Unknown worker backend')
    need(len(cfg.get('batches', [])) == 11, 'Eleven batches of seven required')
    need(60 <= cfg.get('poll_seconds', 90) <= 120, 'Poll interval must be 60–120 seconds')
    need(60 <= cfg.get('worker_timeout_seconds', 3600) <= 14400, 'Bounded worker runtime required')
    return cfg


class HTMLTree(HTMLParser):
    def __init__(self, raw):
        super().__init__(convert_charrefs=True)
        self.nodes = []
        self.stack = []
        self.feed(raw.decode('utf-8'))

    def handle_starttag(self, tag, attrs):
        node = {'tag': tag, 'attrs': dict(attrs), 'parents': list(self.stack), 'text': [], 'prose': []}
        self.nodes.append(node)
        if tag not in {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}:
            self.stack.append(node)

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index]['tag'] == tag:
                del self.stack[index:]
                break

    def handle_data(self, data):
        for index, node in enumerate(self.stack):
            node['text'].append(data)
            if not any(parent['tag'] in {'h1','h2','h3','h4','h5','h6','button','script','style','nav'} for parent in self.stack[index:]):
                node['prose'].append(data)

    @staticmethod
    def text(node):
        return ' '.join(' '.join(node['text']).split())


class Repository:
    def __init__(self, root, remote='origin'):
        self.root = Path(root).resolve()
        self.remote = remote
        self.public_cache = {}

    def git(self, *args, **kwargs):
        return command(['git', *args], self.root, **kwargs)

    def refresh(self):
        self.git('fetch', '--quiet', self.remote, 'refs/heads/main')
        self.main = self.git('rev-parse', 'FETCH_HEAD').decode().strip()
        self.public_cache = {}
        return self.main

    def read(self, revision, path):
        return self.git('show', revision + ':' + safe_path(path))

    def json(self, revision, path):
        return json.loads(self.read(revision, path))

    def state(self):
        lines = self.git('ls-remote', '--heads', self.remote, REF).decode().splitlines()
        if not lines:
            return None, {'schema_version': 1, 'closed': [], 'batch': 0, 'phase': 'IDLE', 'workers': []}
        revision = lines[0].split()[0]
        self.git('fetch', '--quiet', self.remote, REF)
        return revision, self.json(revision, 'state.json')

    def cas(self, expected, state):
        """A commit parented by exactly expected; normal push rejects competing writer."""
        fd, index = tempfile.mkstemp(prefix='starter-index-')
        os.close(fd)
        os.unlink(index)
        env = dict(os.environ, GIT_INDEX_FILE=index,
                   GIT_AUTHOR_NAME='7 Starter Codex', GIT_AUTHOR_EMAIL='starter-codex@localhost',
                   GIT_COMMITTER_NAME='7 Starter Codex', GIT_COMMITTER_EMAIL='starter-codex@localhost')
        try:
            self.git('read-tree', '--empty', env=env)
            blob = self.git('hash-object', '-w', '--stdin', data=canonical(state)).decode().strip()
            self.git('update-index', '--add', '--cacheinfo', '100644,' + blob + ',state.json', env=env)
            tree = self.git('write-tree', env=env).decode().strip()
            args = ['commit-tree', tree]
            if expected:
                args += ['-p', expected]
            revision = self.git(*args, data=('7 Starter Codex transaction ' + uuid.uuid4().hex + '\n').encode(), env=env).decode().strip()
            # No force, no leases that can replace history. Branch creation also races safely.
            self.git('push', '--quiet', self.remote, revision + ':' + REF)
            return revision
        finally:
            Path(index).unlink(missing_ok=True)

    def checked_blob(self, revision, evidence):
        raw = self.read(revision, evidence['path'])
        need(DIGEST.fullmatch(evidence['sha256']) and hashlib.sha256(raw).hexdigest() == evidence['sha256'], 'Evidence digest mismatch')
        return raw

    def merged_pr(self, integration):
        need(SHA.fullmatch(integration.get('merge_sha', '')), 'Missing merge SHA')
        need(type(integration.get('pr')) is int and integration['pr'] > 0, 'Missing merged PR')
        pr = json.loads(command(['gh', 'pr', 'view', str(integration['pr']), '--json',
                                  'state,baseRefName,mergeCommit,statusCheckRollup'], self.root))
        need(pr['state'] == 'MERGED' and pr['baseRefName'] == 'main' and
             pr['mergeCommit']['oid'] == integration['merge_sha'], 'PR is not merged into main')
        checks = pr.get('statusCheckRollup', [])
        need(checks and all((c.get('conclusion') in ('SUCCESS', 'NEUTRAL', 'SKIPPED') and c.get('status') == 'COMPLETED') or c.get('state') == 'SUCCESS' for c in checks), 'CI is not successfully complete')
        self.git('merge-base', '--is-ancestor', integration['merge_sha'], self.main)

    def public_blob(self, url):
        if url not in self.public_cache:
            need(url.startswith(PAGES_ORIGIN), 'Public URL outside trusted Pages origin')
            req = urllib.request.Request(url, headers={'User-Agent': 'Medina-7-Starter-Codex/1', 'Cache-Control': 'no-cache'})
            with urllib.request.urlopen(req, timeout=30) as response:
                need(response.status == 200 and response.geturl() == url, 'Public probe unavailable or redirected')
                body = response.read(64 * 1024 * 1024 + 1)
            need(len(body) <= 64 * 1024 * 1024, 'Public response exceeds bounded size')
            self.public_cache[url] = body
        return self.public_cache[url]

    def live_publication(self, item, publication, files, probes):
        actual = json.loads(self.public_blob(PAGES_ORIGIN + 'publication.json'))
        deployed = actual.get('git_commit', '')
        need(actual.get('schema_version') == 1 and SHA.fullmatch(deployed), 'Actual Pages publication manifest invalid')
        self.git('merge-base', '--is-ancestor', publication['main_sha'], deployed)
        self.git('merge-base', '--is-ancestor', deployed, self.main)
        core = {f'chapters/{item["code"]}/{item["code"]}_{part}.html' for part in ('a','b','c','d','pop1','pop2')} | {f'glossary/{item["code"].lower()}.py'}
        course = actual.get('courses', {}).get(item['code'])
        need(isinstance(course, dict) and all(course.get('source_files', {}).get(path) == files[path] for path in core),
             'Actual deployed manifest does not contain exact final lesson sources')
        site_files = actual.get('site_files', {})
        for path, digest in files.items():
            self.checked_blob(deployed, {'path': path, 'sha256': digest})
            if path not in core:
                need(site_files.get(path) == digest, 'Own asset missing or stale in actual deployed site')
        expected_pages = {PAGES_ORIGIN + 'MEDINA.html'}
        fragment = item.get('fragment')
        if fragment in FRAGMENT_SLUGS:
            expected_pages.add(PAGES_ORIGIN + 'fragments/MEDINA_' + fragment + '_' + FRAGMENT_SLUGS[fragment] + '.html')
        for probe in probes:
            # The recorded digest is dated evidence. Other lessons may legitimately rebuild this shared page.
            need(probe['url'] in expected_pages and DIGEST.fullmatch(probe['sha256']), 'Probe outside actual MEDINA lesson surface')
            relative = probe['url'][len(PAGES_ORIGIN):]
            current_digest = site_files.get(relative, '')
            need(DIGEST.fullmatch(current_digest), 'Current page absent from actual publication manifest')
            body = self.public_blob(probe['url'])
            need(hashlib.sha256(body).hexdigest() == current_digest, 'Current public page differs from actual deployed manifest')
            pattern = rb'<template\b[^>]*\bid\s*=\s*["\']ch-' + item['code'].encode() + rb'["\']'
            need(re.search(pattern, body, re.I), 'Current public page does not contain the actual lesson template')

    def semiology(self, item, proof, files, output_prefix, expected_sources=None):
        reference = proof['requirement_evidence']['semiology']
        need(reference['path'].startswith(output_prefix), 'Semiology proof outside integration mission')
        evidence = json.loads(self.checked_blob(self.main, reference))
        code = item['code']
        tab = code.lower() + '-s-semio'
        source_path = f'chapters/{code}/{code}_c.html'
        need(evidence.get('kind') == 'SEMIO' and evidence.get('requirement') == 'fundamental_analytical_semiology' and evidence.get('actor') == 'Codex' and
             evidence.get('code') == code and evidence.get('status') == 'closed' and evidence.get('unresolved_blockers') == [] and
             evidence.get('reviewed_files_sha256') == files and evidence.get('tab_id') == tab and
             evidence.get('source_path') == source_path and evidence.get('evidence') and
             evidence.get('medical_human_validation') is False and
             evidence.get('source_files_sha256') == (expected_sources or {}) and
             isinstance(evidence.get('findings'), list) and isinstance(evidence.get('evidence'), list) and
             all(f.get('status') in ('resolved','non_blocking') and f.get('evidence') for f in evidence['findings']),
             'Semiology final audit missing/stale')
        tree = HTMLTree(self.read(self.main, source_path))
        in_ps = lambda node: any(p['attrs'].get('id') == 'pS' for p in node['parents'])
        buttons = [node for node in tree.nodes if node['tag'] == 'button' and in_ps(node) and 'data-s' in node['attrs']]
        need(len(buttons) >= 6 and buttons[0]['attrs'].get('data-s') == tab and
             tree.text(buttons[0]) == 'Sémiologie fondamentale et analytique' and
             buttons[0]['attrs'].get('role') == 'tab' and buttons[0]['attrs'].get('aria-controls') == tab and
             buttons[0]['attrs'].get('aria-selected') == 'true' and
             buttons[0]['attrs'].get('id') == code.lower() + '-tab-semio', 'Semiology must be the first selected local science tab')
        panels = [node for node in tree.nodes if node['tag'] == 'div' and node['attrs'].get('id') == tab and
                  'sci' in node['attrs'].get('class', '').split() and in_ps(node) and
                  node['attrs'].get('aria-labelledby') == code.lower() + '-tab-semio']
        need(len(panels) == 1, 'Semiology panel must be inside fundamental pS')
        panel = panels[0]
        need('hidden' not in panel['attrs'] and panel['attrs'].get('aria-hidden') != 'true', 'Initial semiology panel must be visible')
        all_units = [node for node in tree.nodes if panel in node['parents'] and 'ilot' in node['attrs'].get('class', '').split()]
        need(all_units, 'Semiology first science unit absent')
        first_titles = [node for node in tree.nodes if node['tag'] == 'h3' and all_units[0] in node['parents']]
        need(first_titles and tree.text(first_titles[0]) == 'Pour la leçon : quelle est la sémiologie fondamentale et analytique ?', 'Incorrect first semiology unit title')
        required = {'normal','signs','mechanisms','examination','interpretation','differentials','urgency','limits','sources'}
        sections = [node for node in tree.nodes if panel in node['parents'] and node['attrs'].get('data-semiology') in required and
                    'ilot' in node['attrs'].get('class', '').split() and
                    any(child['tag'] == 'h3' and node in child['parents'] and tree.text(child) for child in tree.nodes)]
        need({node['attrs']['data-semiology'] for node in sections if ''.join(node['prose']).strip()} == required, 'Semiology sections missing or empty')
        sources = [node for node in sections if node['attrs']['data-semiology'] == 'sources']
        need(any(node['tag'] == 'a' and node['attrs'].get('href', '').startswith('https://') and
                 any(source in node['parents'] for source in sources) for node in tree.nodes), 'Semiology sources need real linked references')
        clinical = HTMLTree(self.read(self.main, f'chapters/{code}/{code}_a.html') + self.read(self.main, f'chapters/{code}/{code}_b.html'))
        need(any(node['attrs'].get('data-semiology-clinical') == code and ''.join(node['prose']).strip() and
                 any(parent['attrs'].get('id') == 'pA' for parent in node['parents']) for node in clinical.nodes), 'Clinical semiology absent from pathology pA')

    def pages_run(self, publication):
        run_id = publication.get('run_id')
        need(type(run_id) is int and run_id > 0, 'Successful Pages workflow run required')
        value = json.loads(command(['gh', 'api', 'repos/' + PAGES_REPOSITORY + '/actions/runs/' + str(run_id)], self.root))
        need(value.get('workflow_id') == PAGES_WORKFLOW and value.get('path') == '.github/workflows/pages.yml' and
             value.get('repository', {}).get('full_name') == PAGES_REPOSITORY and
             value.get('head_repository', {}).get('full_name') == PAGES_REPOSITORY and
             value.get('head_sha') == publication['main_sha'] and value.get('head_branch') == 'main' and
             value.get('status') == 'completed' and value.get('conclusion') == 'success',
             'Pages deployment run is not successful for exact published main SHA')

    def closure(self, item):
        proof = self.json(self.main, item['closure_path'])
        need(proof.get('schema_version') == 1 and proof.get('code') == item['code'] and
             proof.get('owner') == 'Codex' and proof.get('complete') is True and
             type(proof.get('blocking_reserves')) is int and proof['blocking_reserves'] == 0,
             'Lesson remains open')
        files = proof.get('final_files')
        code = item['code']
        core = {f'chapters/{code}/{code}_{part}.html' for part in ('a', 'b', 'c', 'd', 'pop1', 'pop2')} | {f'glossary/{code.lower()}.py'}
        need(isinstance(files, dict) and core <= set(files), 'All seven owned source files required')
        need(all(path in core or path.startswith(f'assets/img/{code.lower()}/alpha/codex/') for path in files), 'Unrelated lesson/source in closure')
        need(proof.get('medical_human_validation') is False, 'AI closure must not claim human validation')
        source_mission = self.mission(item['missions']['INTEGRATE'], [code], 'integrator')
        need(source_mission['codes'] == [code], 'One-code source mission required')
        output_prefix = 'docs/collaboration/ssp-v2/execution/' + source_mission['id'] + '/'
        need(item['closure_path'].startswith(output_prefix), 'Closure outside own integration output')
        alpha_ref = proof['alpha_receipt']
        need(re.fullmatch(r'organisation/alpha-publications/Codex/' + code + r'/[0-9]{4}\.json', alpha_ref['path']), 'Wrong Alpha receipt path')
        need(any(alpha_ref['path'] == p or alpha_ref['path'].startswith(p + '/') for p in source_mission['paths']), 'Alpha receipt outside approved mission')
        alpha = json.loads(self.checked_blob(self.main, alpha_ref))
        need(alpha.get('schema_version') == 1 and alpha.get('actor') == 'Codex' and alpha.get('code') == code and
             alpha.get('phase') == 'completed' and alpha.get('mission') == source_mission['id'] and
             alpha.get('medical_human_validation') is False, 'Alpha receipt is not a completed owned publication')
        need({path: ref['sha256'] for path, ref in alpha['files'].items()} == files, 'Alpha receipt final hashes differ')
        need(SHA.fullmatch(alpha.get('source_commit', '')), 'Alpha source commit required')
        self.git('merge-base', '--is-ancestor', alpha['source_commit'], self.main)
        expected_sources = {path: alpha['files'][path]['previous_sha256'] for path in core if alpha['files'][path]['previous_sha256'] is not None}
        for path, digest in files.items():
            self.checked_blob(self.main, {'path': path, 'sha256': digest})
        for role in ('MED', 'LANG'):
            report = proof['reports'][role]
            need(report['path'].startswith(output_prefix) and alpha['audits'][role] == {'path': report['path'], 'sha256': report['sha256']}, 'Final report outside Alpha mission or different from Alpha receipt')
            report_raw = self.checked_blob(self.main, report)
            need(self.read(alpha['source_commit'], report['path']) == report_raw, 'Report differs from source commit')
            actual = json.loads(report_raw)
            need(actual.get('actor') == 'Codex' and actual.get('code') == code and actual.get('kind') == role and
                 actual.get('status') == 'closed' and actual.get('medical_human_validation') is False and
                 actual.get('reviewed_files_sha256') == files and actual.get('source_files_sha256') == expected_sources and
                 actual.get('requirements_reviewed', {}).get('fundamental_analytical_semiology') is True and actual.get('unresolved_blockers') == [] and
                 isinstance(actual.get('findings'), list) and isinstance(actual.get('evidence'), list) and actual['evidence'],
                 'Actual audit JSON is unclosed, stale or unsupported')
            need(all(f.get('status') in ('resolved', 'non_blocking') and f.get('evidence') for f in actual['findings']), 'Actual audit findings remain open')
            need(report.get('mission') == item['missions'][role] and report.get('final_files') == files,
                 'Report does not cover final sources')
        figure = proof['figure_validation']
        need(figure['path'].startswith(output_prefix), 'Figures proof outside owned output')
        figure_actual = json.loads(self.checked_blob(self.main, figure))
        need(figure_actual.get('actor') == 'Codex' and figure_actual.get('code') == code and
             figure_actual.get('status') == 'passed' and figure_actual.get('complete') is True and
             figure_actual.get('pending') == [] and figure_actual.get('reviewed_files_sha256') == files and
             figure_actual.get('medical_human_validation') is False and figure_actual.get('evidence'), 'Actual figure proof is stale or unsupported')
        need(figure.get('status') == 'passed' and figure.get('final_files') == files, 'Figure validation missing/stale')
        need(alpha['audits'].get('SEMIO') == proof['requirement_evidence']['semiology'], 'Semiology attestation differs from completed Alpha receipt')
        self.semiology(item, proof, files, output_prefix, expected_sources)
        self.merged_pr(proof['integration'])
        publication = proof['publication']
        need(SHA.fullmatch(publication.get('main_sha', '')), 'Publication main SHA required')
        self.pages_run(publication)
        self.git('merge-base', '--is-ancestor', proof['integration']['merge_sha'], publication['main_sha'])
        self.git('merge-base', '--is-ancestor', publication['main_sha'], self.main)
        manifest_raw = self.checked_blob(self.main, {'path': publication['manifest_path'], 'sha256': publication['manifest_sha256']})
        manifest = json.loads(manifest_raw)
        need(manifest.get('main_sha') == publication['main_sha'] and manifest.get('final_files') == files,
             'Publication manifest does not bind final files')
        for path, digest in files.items():
            self.checked_blob(publication['main_sha'], {'path': path, 'sha256': digest})
        probes = publication.get('probes', [])
        need(probes and manifest.get('probes') == probes, 'Public probes must be bound to manifest')
        self.live_publication(item, publication, files, probes)
        if item['mode'] == 'production':
            production = self.json(self.main, item['production_receipt'])
            need(production.get('complete') is True and production.get('mission') == item['missions']['PRODUCE'] and
                 production.get('final_files') == files, 'New lesson must be produced before audit/closure')
        return proof

    def mission(self, ident, codes, role=None):
        mission = self.json(self.main, '.medina/missions/' + ident + '.json')
        need(mission.get('state') == 'active' and mission.get('owner') == 'Codex' and
             mission.get('actor') == 'Codex' and set(mission.get('codes', [])) <= set(codes), 'Mission not approved for owned batch')
        need(mission.get('codes') and mission.get('id') == ident, 'Mission identity mismatch')
        if role:
            need(mission['role'] == role, 'Invalid mission role')
        for path in mission['paths']:
            safe_path(path)
        return mission

    def prepare(self, mission, directory):
        self.git('merge-base', '--is-ancestor', mission['base_sha'], self.main)
        base = self.main
        guard = str(self.root / 'tools/ai_session_guard.py')
        command(['python3', guard, '--root', str(self.root), 'acquire', mission['id'], '--base', self.main, '--remote', self.remote], self.root)
        self.git('worktree', 'add', '-b', mission['branch'], str(directory), base)
        command(['python3', guard, '--root', str(self.root), 'start', mission['id'], '--base', base,
                 '--actor', mission['actor'], '--conversation', mission['conversation'],
                 '--remote', self.remote, '--worktree', str(directory)], self.root)


def prompt_for(batch, config, index, coordinator):
    return '''Execute only the following preapproved Codex batch. Read AGENTS.md, docs/collaboration/instructions/SEMIOLOGIE_FONDAMENTALE_ANALYTIQUE_2026-10-15.yaml and current SSP V2 guards from the exact approved main base of this worktree. Cardiologie is a frontend reference in read-only mode; do not edit its content or shared engine without a separate mission.
You are the bounded coordinator, not governance: never approve missions or overwrite main.
Acquire every mission with ai_session_guard.py, create its exclusive worktree at exact base, and start it before writes.
Source corrections MUST use the matching per-code INTEGRATE mission, never coordinator paths or audit paths.
For this adopted first batch, existing MED/LANG work is already delivered: adopt and inspect it, do not redispatch the same unchanged audits.
New semiology requirement applies to all seven now: put its local data-s tab FIRST in pS, aria-selected=true, panel initially visible; first ilot h3 EXACTLY "Pour la leçon : quelle est la sémiologie fondamentale et analytique ?". Run existing tests/audit_sciences.py for changed courses; preserve its existing >=280 words, accessible sourced figure and four science-to-clinic/exam/treatment/key-point callouts, without inventing new word thresholds or medical claims.
Then integrate the substantive sourced fundamental/analytical panel and clinical pathology signs, then obtain actual updated final audit attestations for that changed content.
For subsequent batches, only launch missing work: new lessons require PRODUCE complete before MED/LANG;
MED uses GPT6.1 high, LANG GPT6.1 medium and preserves medical content. Own at most these seven assignments.
Reuse existing reports, branches and sessions; uncertain state means stop for reconciliation, never duplicate an AI launch.
Resolve all blocking reserves, validate figures and final-source report hashes, merge through PR with CI, publish and probe public content.
Write truthful closure receipts following docs/collaboration/instructions/7_STARTER_CODEX.md.
Closure requires all seven core source files, completed Alpha receipt and actual final audit/figure JSON; never wrappers asserting completion.
For a clean incomplete CLI turn only, write explicit continuation.json with exact session ID, remaining_codes and next resume_number, per that contract.
For native handoff, attach-native with request nonce before work and complete-native only after seven real closures; never attach a second agent.
A report or process success is NEVER closure. Preserve history and all Claude work.
No external messages. No bypass/force flags. Stop after this batch or on a blocker.
Coordinator manifest: %s
Batch index: %s (first batch is adoption only)
Assignments: %s
Config contract: %s
''' % (json.dumps(coordinator), index, json.dumps(batch), json.dumps({'schema_version': 1, 'closure_contract': '7_STARTER_CODEX.md'}))


class Engine:
    def __init__(self, repo, cfg, runtime):
        self.repo, self.cfg = repo, validate_config(cfg)
        self.runtime = Path(runtime).resolve()
        self.runtime.mkdir(parents=True, exist_ok=True)
        self.identity = socket.gethostname() + ':' + str(os.getpid()) + ':' + uuid.uuid4().hex

    def transition(self, revision, state, **values):
        state.update(values)
        state['updated_at'] = int(time.time())
        committed = self.repo.cas(revision, state)
        self.write_control(state)
        return committed

    def write_control(self, state):
        """Local shared stop switch derived only from a committed campaign state."""
        control = self.runtime / 'control.json'
        value = {'schema_version': 1, 'config_sha256': state.get('config_sha256'),
                 'phase': state['phase'], 'image_execution_enabled': state.get('image_execution_enabled', state['phase'] != 'STOPPED'),
                 'campaign_execution_enabled': state.get('campaign_execution_enabled', state['phase'] != 'STOPPED')}
        if control.exists():
            prior = json.loads(control.read_bytes())
            if prior.get('image_execution_enabled') is False and prior.get('config_sha256') == value['config_sha256']:
                value['image_execution_enabled'] = False
                value['campaign_execution_enabled'] = False
        fd, temporary = tempfile.mkstemp(prefix='.control-', dir=self.runtime)
        try:
            with os.fdopen(fd, 'wb') as stream:
                stream.write(canonical(value))
                stream.flush()
                os.fsync(stream.fileno())
            os.replace(temporary, control)
        finally:
            Path(temporary).unlink(missing_ok=True)

    def tick(self):
        self.repo.refresh()
        revision, state = self.repo.state()
        config_digest = hashlib.sha256(canonical(self.cfg)).hexdigest()
        need(state.get('config_sha256', config_digest) == config_digest, 'Campaign config changed; reconcile explicitly')
        state['config_sha256'] = config_digest
        if revision is not None:
            self.write_control(state)
        if state['phase'] in ('NATIVE_REQUESTED', 'NATIVE_RUNNING'):
            return state
        if state['phase'] in ('STOPPED', 'BLOCKED', 'NEEDS_RECONCILIATION', 'SPAWN_INTENT', 'RUNNING'):
            # Intent survives crashes; no timeout lease or automatic takeover can replay an ambiguous spawn.
            return state
        closed = []
        for item in self.cfg['queue']:
            try:
                self.repo.closure(item)
            except (Blocked, KeyError, ValueError, OSError, subprocess.TimeoutExpired):
                break
            closed.append(item['code'])
        need(set(state['closed']) <= set(closed), 'Previously closed proof regressed; reconciliation required')
        state['closed'] = closed
        if len(closed) == 77:
            receipts = self.cfg.get('image_tasks_done', [])
            for receipt in receipts:
                value = json.loads(self.repo.checked_blob(self.repo.main, receipt))
                need(value.get('complete') is True and value.get('owner') == 'Codex', 'Image work remains open')
            # The independent finder reads this flag from the campaign branch; history/images/tools remain intact.
            self.transition(revision, state, phase='STOPPED', campaign_execution_enabled=False,
                            image_execution_enabled=False, terminal_reason='77 lessons and image tasks complete')
            return state
        index = len(closed) // 7
        if len(closed) % 7:
            # Continue existing batch, never begin the next before its seven are closed.
            index = state.get('batch', index)
        batch = self.cfg['queue'][index * 7:(index + 1) * 7]
        coordinator = self.repo.mission(self.cfg['batches'][index]['coordinator_mission'], [i['code'] for i in batch], 'integrator')
        for item in batch:
            for role, ident in item['missions'].items():
                manifest = self.repo.mission(ident, [item['code']], 'audit' if role in ('MED', 'LANG') else 'integrator')
                if role in ('MED', 'LANG'):
                    need(manifest.get('requested_model') in ('GPT6.1', 'gpt-6.1') and
                         manifest.get('requested_effort') == ('high' if role == 'MED' else 'medium'),
                         'Audit model/effort does not match mandate')
        state.update(batch=index, owner=self.identity, campaign_execution_enabled=True, image_execution_enabled=True,
                     resume_count=0, resume_thread=None)
        # Durable, globally exclusive claim BEFORE guard/worktree/Popen side effects.
        revision = self.transition(revision, state, phase='SPAWN_INTENT', main_sha=self.repo.main)
        directory = self.runtime / ('batch-%02d-%s' % (index, uuid.uuid4().hex[:10]))
        try:
            self.repo.prepare(coordinator, directory)
            revision = self.transition(revision, state, phase='RUNNING', worktree=str(directory))
            prompt = prompt_for(batch, self.cfg, index, coordinator)
            prompt += '\nEvery Image_Codex_Finder call MUST pass --campaign-state ' + str(self.runtime / 'control.json') + '. All local copies share this control file; independent machines are not globally stopped by this local file.\n'
            if self.cfg.get('worker_backend', 'codex_cli') == 'native_handoff':
                request_id = uuid.uuid4().hex
                self.transition(revision, state, phase='NATIVE_REQUESTED', request_id=request_id,
                                prompt_sha256=hashlib.sha256(prompt.encode()).hexdigest(), handoff={
                    'request_id': request_id, 'coordinator_mission': coordinator['id'],
                    'worktree': str(directory), 'prompt': prompt, 'dispatch_status': 'pending_native_attach',
                    'required_model': 'gpt-6.1', 'required_effort': 'high'})
                return state
            return self.worker(revision, state, directory, prompt)
        except Exception as error:
            # No raw diagnostics or automated replay. A human examines mission/worktree/session evidence.
            self.transition(revision, state, phase='NEEDS_RECONCILIATION', reason=type(error).__name__)
            return state

    def native(self, action, request_id, agent_id):
        self.repo.refresh()
        revision, state = self.repo.state()
        need(state.get('config_sha256') == hashlib.sha256(canonical(self.cfg)).hexdigest(), 'Campaign config changed during native handoff')
        need(self.cfg.get('worker_backend') == 'native_handoff', 'Not a native campaign')
        need(request_id and agent_id and state.get('request_id') == request_id, 'Native request nonce mismatch')
        if action == 'attach-native':
            need(state['phase'] == 'NATIVE_REQUESTED', 'Native request already attached or inactive')
            self.transition(revision, state, phase='NATIVE_RUNNING', native_agent_id=agent_id,
                            native_attached_at=int(time.time()))
        else:
            need(state['phase'] == 'NATIVE_RUNNING' and state.get('native_agent_id') == agent_id,
                 'Native completion requires the attached agent')
            batch = self.cfg['queue'][state['batch'] * 7:(state['batch'] + 1) * 7]
            for item in batch:
                self.repo.closure(item)
            # Revalidate all earlier closures too; no regression hidden by native completion.
            prefix = self.cfg['queue'][:(state['batch'] + 1) * 7]
            for item in prefix:
                self.repo.closure(item)
            self.transition(revision, state, phase='IDLE', closed=[i['code'] for i in prefix],
                            native_completed_at=int(time.time()), reason='Native batch verified complete')
        return state

    def continuation(self, state, directory, record):
        """Only a successful known thread may request up to three explicit same-thread resumes."""
        if record.get('returncode') != 0 or not record.get('thread_id') or state.get('resume_count', 0) >= 3:
            return None
        ident = self.cfg['batches'][state['batch']]['coordinator_mission']
        path = Path(directory) / ('docs/collaboration/ssp-v2/execution/' + ident + '/continuation.json')
        try:
            need(path.resolve().is_relative_to(Path(directory).resolve()), 'Continuation path escapes worktree')
            raw = path.read_bytes()
            receipt = json.loads(raw)
            need(receipt.get('schema_version') == 1 and receipt.get('status') == 'resumable' and
                 receipt.get('thread_id') == record['thread_id'] and receipt.get('coordinator_mission') == ident and
                 receipt.get('batch') == state['batch'] and receipt.get('turn_complete') is True and
                 receipt.get('resume_number') == state.get('resume_count', 0) + 1, 'Invalid continuation identity')
            remaining = []
            for item in self.cfg['queue'][state['batch'] * 7:(state['batch'] + 1) * 7]:
                try:
                    self.repo.closure(item)
                except (Blocked, KeyError, ValueError, OSError, subprocess.TimeoutExpired):
                    remaining.append(item['code'])
            need(remaining and receipt.get('remaining_codes') == remaining and receipt.get('reason'), 'Continuation remaining work mismatch')
            return {'sha256': hashlib.sha256(raw).hexdigest(),
                    'prompt': 'Continue this SAME session and existing mission worktrees only. Do not create duplicate AI sessions. '
                              'Finish the still-open owned lessons, or report blockers: ' + ','.join(remaining)}
        except (Blocked, KeyError, ValueError, OSError):
            return None

    def worker(self, revision, state, directory, prompt):
        argv = [self.cfg.get('codex_binary', '/opt/codex/bin/codex'), '-a', 'never', 'exec']
        if state.get('resume_thread'):
            argv += ['resume']
        argv += ['--json', '-m', 'gpt-6.1', '-c', 'model_reasoning_effort="high"']
        if state.get('resume_thread'):
            argv += [state['resume_thread']]
        argv += ['-']
        log = self.runtime / ('batch-%02d-%s.events.jsonl' % (state['batch'], uuid.uuid4().hex[:12]))
        # Redirect JSON events to disk and parse only thread IDs; no potentially sensitive child text printed.
        with log.open('ab', buffering=0) as output:
            process = subprocess.Popen(argv, cwd=directory, stdin=subprocess.PIPE, stdout=output,
                                       stderr=subprocess.DEVNULL, start_new_session=True)
            record = {'pid': process.pid, 'host': socket.gethostname(), 'started_at': int(time.time()),
                      'event_log': str(log), 'owner': self.identity}
            state['workers'].append(record)
            revision = self.transition(revision, state, phase='RUNNING')
            process.stdin.write(prompt.encode())
            process.stdin.close()
            deadline = time.monotonic() + self.cfg.get('worker_timeout_seconds', 3600)
            event_offset = 0
            while process.poll() is None:
                if time.monotonic() >= deadline or log.stat().st_size > 32 * 1024 * 1024:
                    # Only the process group created by this live controller is signalled.
                    os.killpg(process.pid, signal.SIGTERM)
                    try:
                        process.wait(timeout=10)
                    except subprocess.TimeoutExpired:
                        os.killpg(process.pid, signal.SIGKILL)
                        process.wait(timeout=10)
                    break
                with log.open('rb') as events:
                    events.seek(event_offset)
                    while True:
                        line = events.readline()
                        if not line or not line.endswith(b'\n'):
                            break
                        event_offset = events.tell()
                        try:
                            event = json.loads(line)
                            if event.get('type') == 'thread.started' and not record.get('thread_id'):
                                record['thread_id'] = event['thread_id']
                                revision = self.transition(revision, state, phase='RUNNING')
                        except (ValueError, KeyError):
                            pass
                time.sleep(1)
            with log.open('rb') as events:
                for line in events:
                    try:
                        event = json.loads(line)
                        if event.get('type') == 'thread.started':
                            record['thread_id'] = event['thread_id']
                    except (ValueError, KeyError):
                        pass
            record['returncode'] = process.poll()
        with log.open('rb') as events:
            for line in events:
                try:
                    event = json.loads(line)
                    if event.get('type') == 'error' and any(word in str(event.get('message', '')).lower() for word in
                            ('authentication', 'unauthorized', 'login required', 'invalid api key', 'not authenticated', 'token could not be refreshed', 'logged out')):
                        self.transition(revision, state, phase='BLOCKED', reason='Codex authentication unavailable')
                        return state
                except ValueError:
                    pass
        # Reconcile actual main proofs, never the child's exit status alone.
        self.repo.refresh()
        try:
            for item in self.cfg['queue'][state['batch'] * 7:(state['batch'] + 1) * 7]:
                self.repo.closure(item)
        except (Blocked, KeyError, ValueError, OSError, subprocess.TimeoutExpired):
            continuation = self.continuation(state, directory, record)
            if continuation:
                state['resume_count'] = state.get('resume_count', 0) + 1
                state['resume_thread'] = record['thread_id']
                state['continuation_sha256'] = continuation['sha256']
                revision = self.transition(revision, state, phase='SPAWN_INTENT', reason='Explicit bounded same-thread continuation')
                return self.worker(revision, state, directory, continuation['prompt'])
            self.transition(revision, state, phase='NEEDS_RECONCILIATION', reason='Worker stopped without seven valid closure proofs')
        else:
            self.transition(revision, state, phase='IDLE', reason='Seven closures verified; next tick revalidates')
        return state


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', default='.')
    parser.add_argument('--remote', default='origin')
    parser.add_argument('--config', default='.medina/7-starter-codex.json')
    parser.add_argument('--runtime', default='/workspace/scratch/7-starter-codex-runtime')
    parser.add_argument('action', choices=('run', 'tick', 'status', 'verify', 'attach-native', 'complete-native'))
    parser.add_argument('--request-id')
    parser.add_argument('--agent-id')
    args = parser.parse_args(argv)
    repo = Repository(args.root, args.remote)
    try:
        repo.refresh()
        if args.action == 'status':
            _, state = repo.state()
            print(json.dumps(state, indent=2))
            return 0
        # Configuration MUST come from main, never from an unmerged candidate worktree.
        cfg = repo.json(repo.main, args.config)
        engine = Engine(repo, cfg, args.runtime)
        if args.action in ('attach-native', 'complete-native'):
            state = engine.native(args.action, args.request_id, args.agent_id)
            print(json.dumps({'phase': state['phase'], 'batch': state['batch']}))
            return 0
        if args.action == 'verify':
            closed = []
            for item in cfg['queue']:
                try:
                    repo.closure(item)
                    closed.append(item['code'])
                except (Blocked, KeyError, ValueError, OSError, subprocess.TimeoutExpired):
                    break
            print(json.dumps({'phase': 'PROOF_ONLY', 'closed': closed, 'next_batch': len(closed) // 7}))
            return 0
        while True:
            state = engine.tick()
            print(json.dumps({'phase': state['phase'], 'closed': len(state['closed']), 'batch': state['batch']}), flush=True)
            if args.action == 'tick' or state['phase'] in ('STOPPED', 'BLOCKED', 'NEEDS_RECONCILIATION'):
                break
            time.sleep(cfg.get('poll_seconds', 90))
        return 0
    except (Blocked, KeyError, ValueError, OSError, subprocess.TimeoutExpired) as error:
        print(json.dumps({'phase': 'BLOCKED', 'reason': type(error).__name__}), flush=True)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
