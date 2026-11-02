#!/usr/bin/env python3
"""MEDINA: gates, leases, evidence, exact cache and truthful observability.

No model calls, no automatic clinical approval, no main writes or PR creation.
All state mutations serialize locally. Remote missions remain the authoritative
cross-machine reservation service (tools/ai_session_guard.py).
"""
from __future__ import annotations
import argparse
import contextlib
import datetime as dt
import fcntl
import hashlib
import html
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import time
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
DEFAULT_ROOT = HERE.parent
STAGES = ['preparation', 'recherche', 'redaction', 'images', 'verification', 'revue_requise', 'termine']
MONOGRAPH = ['Définition', 'Épidémiologie', 'Physiopathologie', 'Démarche clinique',
             'Anamnèse', 'Examen clinique', 'Syndromes', 'Diagnostic positif',
             'Explorations', 'Arbre diagnostique', 'Prise en charge', 'Prévention et suivi',
             'Points clés', 'Pièges']

def now():
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds')

def age(value):
    return (dt.datetime.now(dt.timezone.utc) - dt.datetime.fromisoformat(value)).total_seconds()

def digest(data):
    return hashlib.sha256(data).hexdigest()

def load(path, default=None):
    try:
        return json.loads(Path(path).read_text())
    except FileNotFoundError:
        if default is not None:
            return default
        raise

def atomic(path, data):
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    if not isinstance(data, str):
        data = json.dumps(data, ensure_ascii=False, indent=2) + '\n'
    fd, tmp = tempfile.mkstemp(prefix='.' + path.name, dir=path.parent)
    try:
        with os.fdopen(fd, 'w') as stream:
            stream.write(data); stream.flush(); os.fsync(stream.fileno())
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp): os.unlink(tmp)

def inside(root, relative):
    root = Path(root).resolve(); p = (root / relative).resolve()
    if not p.is_relative_to(root): raise ValueError('Chemin hors périmètre')
    return p

def git(root, *args):
    return subprocess.check_output(['git', '-C', str(root), *args], text=True, timeout=30).strip()

def verify_binding(worktree, code, folder):
    """Check a recorded verification against current bytes; never renew it."""
    folder=Path(folder);binding=load(folder/'source-binding.json')
    required={f'chapters/{code}/{code}_{x}.html' for x in ('a','b','c','d','pop1','pop2')}
    required.add('glossary/'+code.lower()+'.py')
    if binding.get('code')!=code or not required<=set(binding.get('final_sources',{})):
        raise ValueError('Liaison aux sept sources finales incomplète')
    if not binding.get('verified_at') or not binding.get('checks'):
        raise ValueError('Vérification finale non documentée')
    for name,expected in binding['final_sources'].items():
        if not (name in required or name.startswith('assets/img/'+code.lower()+'/alpha/codex/')):
            raise ValueError('Source liée hors leçon')
        p=inside(worktree,name)
        if not p.is_file() or digest(p.read_bytes())!=expected:
            raise ValueError('Source modifiée depuis vérification: '+name)
    preview=inside(folder,binding.get('preview','missing'))
    if not preview.is_file() or digest(preview.read_bytes())!=binding.get('preview_sha256'):
        raise ValueError('Aperçu modifié depuis vérification')
    return binding

def code_hash():
    paths = sorted([*HERE.glob('*.py'), *HERE.glob('tests/*.py'), HERE/'dashboard-template.html', HERE/'catalog.json'])
    return digest(b''.join(str(p.relative_to(HERE)).encode()+b'\0'+p.read_bytes() for p in paths if p.exists()))

class Harness:
    def __init__(self, root=DEFAULT_ROOT):
        self.root = Path(root).resolve(); self.home = self.root / 'harness'
        self.runtime = self.home / 'runtime'; self.runtime.mkdir(parents=True, exist_ok=True)
        self.config = load(self.home / 'config.json')

    @contextlib.contextmanager
    def transaction(self):
        with (self.runtime / '.lock').open('a+') as lock:
            fcntl.flock(lock, fcntl.LOCK_EX)
            state = load(self.runtime / 'state.json', {'schema': 1, 'created_at': now(), 'agents': {}, 'events': [], 'cache': {'hits': 0, 'misses': 0, 'bytes_avoided': 0}})
            yield state
            atomic(self.runtime / 'state.json', state)

    def event(self, state, action, **fields):
        event = {'at': now(), 'action': action, **fields}
        state['events'] = (state.get('events', []) + [event])[-200:]
        with (self.runtime / 'events.jsonl').open('a') as f:
            f.write(json.dumps(event, ensure_ascii=False) + '\n')

    def readiness(self):
        problems = []
        test = load(self.runtime / 'tests.json', {})
        monitor = load(self.runtime / 'watch.json', {})
        if test.get('ok') is not True or test.get('code_sha256') != code_hash():
            problems.append('Tests absents, échoués ou périmés après modification du harness')
        if monitor.get('ok') is not True or not monitor.get('observed_at') or not 0 <= age(monitor['observed_at']) <= 900:
            problems.append('Veille sans observation saine de moins de 15 minutes')
        roster = self.config.get('agents', [])
        if len(roster) != 4 or len({a['specialty'] for a in roster}) != 4:
            problems.append('Quatre affectations exclusives requises')
        if sum(a.get('model') == 'gpt-6-astra' and a.get('reasoning') == 'high' for a in roster) != 3:
            problems.append('Trois agents Astra high requis')
        prompt = load(self.home / 'prompt-lock.json', {})
        for entry in prompt.get('files', []):
            p = inside(self.root, entry['path'])
            if not p.exists() or digest(p.read_bytes()) != entry['sha256']:
                problems.append('Prompt modifié ou absent: ' + entry['path'])
        if not prompt.get('files'): problems.append('Prompt non identifié')
        if not (self.home / 'REPARTITION.md').exists(): problems.append('Répartition .md absente')
        if not (self.home / 'dashboard.html').exists(): problems.append('Plan HTML absent')
        return {'allowed': not problems, 'problems': problems, 'checked_at': now(), 'scope': 'Autorise la recherche/rédaction réservée, jamais la publication ni la clôture médicale.'}

    def claim(self, agent, code, worktree, receipt):
        gate = self.readiness()
        if not gate['allowed']: raise ValueError('; '.join(gate['problems']))
        spec = next(a for a in self.config['agents'] if a['id'] == agent)
        if code not in spec['queue']: raise ValueError('Leçon hors attribution')
        proof = load(receipt)
        # ai_session_guard start is the proof, not a user editable boolean.
        if not re.fullmatch('[0-9a-f]{40}', proof.get('registry_sha', '')) or proof.get('mission', {}).get('codes') != [code]:
            raise ValueError('Reçu start de mission réel attendu')
        mission = proof['mission']
        if git(worktree, 'branch', '--show-current') != mission['branch']:
            raise ValueError('Branche différente du reçu de mission')
        if not Path(worktree).is_dir(): raise ValueError('Worktree absent')
        with self.transaction() as state:
            for other, a in state['agents'].items():
                if a.get('lesson') == code and other != agent: raise ValueError('Leçon déjà réservée')
                if other == agent and a.get('lesson') not in (None, code) and a.get('stage') != 'termine':
                    raise ValueError('Une seule leçon active par agent')
                if other != agent and a.get('worktree') == str(Path(worktree).resolve()):
                    raise ValueError('Worktree déjà affecté')
            state['agents'][agent] = {'lesson': code, 'worktree': str(Path(worktree).resolve()), 'stage': 'recherche',
                'branch': mission['branch'], 'allowed_paths': mission.get('paths', []),
                'started_at': now(), 'activity_at': now(), 'message': 'Mission réservée; recherche autorisée',
                'tokens_input': None, 'tokens_output': None, 'cost_usd': None, 'usage_source': 'non exposé par interface native',
                'medical_score': None, 'medical_review': 'non effectuée', 'completed_sections': 0,
                'receipt_sha256': digest(Path(receipt).read_bytes())}
            self.event(state, 'claim', agent=agent, code=code)
        self.report()
        return {'claimed': code, 'agent': agent}

    def progress(self, agent, stage, message, completed_sections=None):
        if stage not in STAGES: raise ValueError('Étape inconnue')
        if stage == 'termine': raise ValueError('Clôture réservée à la validation complète; progress ne peut clôturer')
        if stage != 'preparation' and not self.readiness()['allowed']:
            raise ValueError('Harness non prêt; progression de production bloquée')
        with self.transaction() as state:
            a = state['agents'].setdefault(agent, {'started_at': now(), 'tokens_input': None, 'tokens_output': None, 'cost_usd': None})
            if agent not in {x['id'] for x in self.config['agents']}: raise ValueError('Agent inconnu')
            if stage != 'preparation' and not a.get('lesson'): raise ValueError('Mission non acquise')
            a.update(stage=stage, message=message, activity_at=now())
            if completed_sections is not None:
                if not 0 <= completed_sections <= 14: raise ValueError('Sections hors limites')
                a['completed_sections'] = completed_sections
            self.event(state, 'progress', agent=agent, stage=stage, message=message)
        self.report()
        return {'updated': agent, 'at': now()}

    def complete(self, agent, folder):
        """Record attributed project completion, never a clinical certification."""
        if not self.readiness()['allowed']:raise ValueError('Harness non prêt')
        folder=Path(folder).resolve();manifest=load(folder/'lesson-manifest.json')
        result=validate_lesson(folder)
        if not result['technical_contract_pass']:raise ValueError('; '.join(result['errors']))
        rows=manifest.get('matrix20',[])
        if (len(rows)!=20 or {r.get('point') for r in rows}!=set(range(1,21))
                or any(r.get('status')!='covered' or not r.get('evidence') for r in rows)):
            raise ValueError('Matrice20 incomplète ou réserves ouvertes')
        with self.transaction() as state:
            a=state['agents'][agent];code=a['lesson']
            if a.get('stage')=='termine':raise ValueError('Achèvement déjà enregistré')
            if manifest.get('code')!=code:raise ValueError('Manifeste différent de la mission')
            if not folder.is_relative_to(Path(a['worktree']).resolve()):raise ValueError('Dossier hors worktree')
            if git(a['worktree'],'branch','--show-current')!=a['branch']:raise ValueError('Branche différente')
            binding=verify_binding(a['worktree'],code,folder)
            record={'agent':agent,'code':code,'at':now(),'branch':a['branch'],'worktree':a['worktree'],'folder':str(folder),'manifest_sha256':digest((folder/'lesson-manifest.json').read_bytes()),
                    'source_binding_sha256':digest((folder/'source-binding.json').read_bytes()),'review_modes':result['review_modes'],
                    'clinical_certification':False,'publication_allowed':False,'preview_sha256':binding['preview_sha256']}
            a.update(stage='termine',completed_sections=14,activity_at=now(),message='Achèvement de projet documenté; présentation à Vial avant toute PR main.')
            state.setdefault('completed_lessons',[]).append(record)
            self.event(state,'complete',agent=agent,code=code)
        atomic(folder/'harness-completion.json',record);self.report();return record

    def extract(self, path, first, last, repeat=False, worktree=None):
        scope = self.root
        if worktree:
            scope = Path(worktree).resolve()
            state = load(self.runtime / 'state.json', {'agents': {}})
            if str(scope) not in {a.get('worktree') for a in state['agents'].values()}:
                raise ValueError('Worktree non réservé par ce harness')
        p = inside(scope, path)
        if not 1 <= first <= last or last - first >= 200: raise ValueError('Lecture bornée à 200 lignes')
        raw = p.read_bytes()
        if len(raw) > 16 * 1024 * 1024: raise ValueError('Fichier >16 Mio; extraction dédiée nécessaire')
        text = raw.decode('utf-8'); lines = text.splitlines()
        excerpt = '\n'.join(lines[first-1:last])
        if len(excerpt.encode()) > 24000: raise ValueError('Passage >24 Ko; réduire la fenêtre')
        key = digest(raw + f'{p}:{first}:{last}'.encode())
        cache = self.runtime / 'cache' / (key + '.json'); hit = cache.exists()
        payload = {'path': path, 'scope': str(scope), 'sha256': digest(raw), 'first': first, 'last': min(last, len(lines)), 'excerpt': excerpt}
        if not hit: atomic(cache, payload)
        with self.transaction() as state:
            state['cache']['hits' if hit else 'misses'] += 1
            avoided = len(raw) if hit and not repeat else max(0, len(raw)-len(excerpt.encode()))
            state['cache']['bytes_avoided'] += avoided
            self.event(state, 'extract', path=path, cache_hit=hit, bytes_input=len(raw), bytes_output=0 if hit and not repeat else len(excerpt.encode()), bytes_avoided=avoided)
        if hit and not repeat: payload.pop('excerpt')
        return {**payload, 'cache_hit': hit, 'cache_path': str(cache), 'savings_kind': 'octets évités; ne constitue pas une mesure de tokens facturés'}

    def watch(self):
        findings = []
        state = load(self.runtime / 'state.json', {'agents': {}})
        for agent, a in state['agents'].items():
            if a.get('activity_at') and age(a['activity_at']) > 1200 and a.get('stage') != 'termine':
                findings.append({'agent': agent, 'level': 'warning', 'reason': 'Aucune activité déclarée depuis plus de 20 min; agent non supposé actif'})
            if a.get('worktree') and not Path(a['worktree']).is_dir():
                findings.append({'agent': agent, 'level': 'error', 'reason': 'Worktree disparu'})
            elif a.get('worktree') and a.get('allowed_paths'):
                try:
                    if git(a['worktree'], 'branch', '--show-current') != a['branch']:
                        findings.append({'agent': agent, 'level': 'error', 'reason': 'Branche différente de la réservation'})
                    files = set(git(a['worktree'], 'diff', '--name-only', self.config['base_sha']).splitlines())
                    files.update(git(a['worktree'], 'ls-files', '--others', '--exclude-standard').splitlines())
                    forbidden=[p for p in files if not any(p==prefix or p.startswith(prefix+'/') for prefix in a['allowed_paths'])]
                    if forbidden: findings.append({'agent':agent,'level':'error','reason':'Écritures hors périmètre','paths':forbidden})
                    folder=Path(a['worktree'])/'docs/collaboration/ssp-v2/execution'/('ALPHA77-CODEX-'+a['lesson']+'-INTEGRATE')
                    if (folder/'source-binding.json').exists():
                        try:verify_binding(a['worktree'],a['lesson'],folder)
                        except (ValueError,OSError) as exc:
                            findings.append({'agent':agent,'level':'warning','reason':'Preuves/aperçu périmés; nouvelle vérification requise avant clôture: '+str(exc)})
                except subprocess.SubprocessError as exc:
                    findings.append({'agent':agent,'level':'error','reason':'Contrôle Git indisponible: '+str(exc)})
        for spec in self.config['agents']:
            p = self.home / 'agents' / spec['specialty'] / 'progress.json'
            if p.exists():
                try:
                    value = load(p)
                    if value.get('agent') != spec['id']: raise ValueError('agent mismatch')
                except (ValueError, OSError) as exc:
                    findings.append({'agent': spec['id'], 'level': 'error', 'reason': 'Progression illisible: '+str(exc)})
        result = {'observed_at': now(), 'ok': not any(x['level'] == 'error' for x in findings), 'findings': findings,
                  'interval_seconds': 600, 'observer_pid': os.getpid(), 'agent_activity_refreshed': False,
                  'limits': 'Observation logicielle seulement; aucun réveil de modèle, aucune validation médicale.'}
        atomic(self.runtime / 'watch.json', result)
        self.report()
        with self.transaction() as s: self.event(s, 'watch', ok=result['ok'], findings=len(findings))
        return result

    def report(self):
        state = load(self.runtime / 'state.json', {'agents': {}, 'events': [], 'cache': {}})
        watch = load(self.runtime / 'watch.json', {})
        result = {'generated_at': now(), 'timezone': 'Europe/Zurich', 'deadline': self.config['deadline'],
                  'base_sha': self.config['base_sha'], 'gate': self.readiness(), 'watch': watch,
                  'tests': load(self.runtime / 'tests.json', {}), 'agents': [], 'events': state.get('events', []),
                  'cache': state.get('cache', {}), 'monitor': load(self.home / 'monitor.json', {}),
                  'prompt': load(self.home / 'prompt-lock.json', {}),
                  'plan': load(self.home / 'plan.json', {}),
                  'deliverables': load(self.home / 'deliverables.json', {}),
                  'completed_lessons':state.get('completed_lessons',[])}
        for spec in self.config['agents']:
            a = {**spec, **state.get('agents', {}).get(spec['id'], {})}
            a['brief'] = load(self.home / 'agents' / spec['specialty'] / 'brief.json', {})
            a['activity_age_seconds'] = round(age(a['activity_at'])) if a.get('activity_at') else None
            a['activity_fresh'] = a['activity_age_seconds'] is not None and 0 <= a['activity_age_seconds'] <= 1200
            a['sections_per_hour'] = round(a.get('completed_sections', 0) / max(age(a.get('started_at', now()))/3600, 0.001), 2)
            a['throughput_limit'] = 'Sections déclarées par auteur, non leçons validées'
            result['agents'].append(a)
        atomic(self.home / 'status.json', result)
        render(result, self.home / 'dashboard.html')
        # Snapshot frozen only at/after 08:00 Zurich; no future timestamp invented.
        if dt.datetime.now(dt.timezone.utc) >= dt.datetime.fromisoformat(self.config['deadline']):
            target = self.home / 'rapport-08h00.html'
            if not target.exists(): render({**result,'report_frozen_at':now()},target)
        return result

def validate_lesson(folder):
    folder = Path(folder); manifest = load(folder/'lesson-manifest.json'); errors = []
    sources = {s['id']: s for s in manifest.get('sources', [])}
    content = '\n'.join(p.read_text() for p in folder.rglob('*.html'))
    for number in range(1, 15):
        rows = [x for x in manifest.get('monograph', []) if x.get('point') == number]
        if len(rows) != 1: errors.append(f'Point monographique {number} absent ou dupliqué'); continue
        row = rows[0]
        if not row.get('anchor') or not re.search(r'id=[\"\']'+re.escape(row['anchor'])+r'[\"\']', content):
            errors.append(f'Ancre non résolue point {number}')
        if not row.get('sources') or any(s not in sources for s in row['sources']): errors.append(f'Preuves absentes point {number}')
        if len(row.get('coverage_explanation', '')) < 80: errors.append(f'Couverture à expliciter point {number}')
    for source in sources.values():
        if not all(source.get(k) for k in ['url','publisher','read_at','section','passage','population','limits']):
            errors.append('Métadonnées source incomplètes: '+source.get('id','?'))
    if not manifest.get('images'): errors.append('Images annotées absentes')
    for fig in manifest.get('images', []):
        if not all(fig.get(k) for k in ['original_url','license','author','annotations','medical_review']): errors.append('Figure non traçable/annotée/revue')
        p = inside(folder, fig.get('path','missing'))
        if not p.is_file() or digest(p.read_bytes()) != fig.get('sha256'): errors.append('Figure absente/empreinte incorrecte')
    semio = manifest.get('semiology', {})
    if not isinstance(semio, dict) or len(set(semio.get('section_anchors', []))) < 9:
        errors.append('Sémiologie: neuf sections documentées requises')
    elif any(not re.search(r'id=[\"\']'+re.escape(anchor)+r'[\"\']', content) for anchor in semio['section_anchors']):
        errors.append('Sémiologie: ancres absentes')
    if manifest.get('blocking_findings', 1): errors.append('Réserves bloquantes non levées')
    # Current SSP V2 permits attributed self-review. Never call it independent.
    for kind in ('medical', 'language', 'visual_desktop', 'visual_mobile'):
        review = manifest.get('reviews', {}).get(kind, {})
        if not review.get('path') or not review.get('reviewer'):
            errors.append('Revue distincte absente: '+kind); continue
        mode=review.get('mode','independent')
        if mode not in ('self_review','independent'):
            errors.append('Mode de revue inconnu: '+kind); continue
        if review.get('reviewer') == manifest.get('author') and mode != 'self_review':
            errors.append('Revue distincte absente; auto-relecture à déclarer explicitement: '+kind); continue
        p = inside(folder, review['path'])
        if not p.is_file() or digest(p.read_bytes()) != review.get('sha256'): errors.append('Preuve de revue absente: '+kind)
    return {'technical_contract_pass': not errors, 'errors': errors, 'clinical_certification': False,
            'publication_allowed': False,
            'review_modes': {k:v.get('mode','independent') for k,v in manifest.get('reviews',{}).items()},
            'reason': 'Une vérification de fichiers ou auto-relecture ne certifie pas la médecine; présentation utilisateur requise avant PR main.'}

def render(data, path):
    template = (HERE/'dashboard-template.html').read_text()
    payload = json.dumps(data, ensure_ascii=False).replace('<','\\u003c').replace('&','\\u0026')
    atomic(path, template.replace('__DATA__', payload))

def main():
    p=argparse.ArgumentParser(); p.add_argument('--root',type=Path,default=DEFAULT_ROOT)
    sub=p.add_subparsers(dest='cmd',required=True)
    for x in ('gate','report','watch','self-test'): sub.add_parser(x)
    d=sub.add_parser('daemon'); d.add_argument('--interval',type=int,default=600)
    x=sub.add_parser('extract'); x.add_argument('path'); x.add_argument('--first',type=int,required=True); x.add_argument('--last',type=int,required=True); x.add_argument('--repeat',action='store_true'); x.add_argument('--worktree',type=Path)
    x=sub.add_parser('claim'); x.add_argument('agent'); x.add_argument('code'); x.add_argument('worktree'); x.add_argument('receipt')
    x=sub.add_parser('progress'); x.add_argument('agent'); x.add_argument('stage'); x.add_argument('message'); x.add_argument('--sections',type=int)
    x=sub.add_parser('validate'); x.add_argument('folder')
    x=sub.add_parser('complete'); x.add_argument('agent'); x.add_argument('folder')
    a=p.parse_args(); h=Harness(a.root)
    if a.cmd=='gate': out=h.readiness()
    elif a.cmd=='report': out=h.report(); out={'report':str(h.home/'dashboard.html'),'generated_at':out['generated_at']}
    elif a.cmd=='watch': out=h.watch()
    elif a.cmd=='extract': out=h.extract(a.path,a.first,a.last,a.repeat,a.worktree)
    elif a.cmd=='claim': out=h.claim(a.agent,a.code,a.worktree,a.receipt)
    elif a.cmd=='progress': out=h.progress(a.agent,a.stage,a.message,a.sections)
    elif a.cmd=='validate': out=validate_lesson(a.folder)
    elif a.cmd=='complete': out=h.complete(a.agent,a.folder)
    elif a.cmd=='self-test':
        r=subprocess.run([sys.executable,'-m','unittest','discover','-s',str(HERE/'tests'),'-v'],capture_output=True,text=True,timeout=120)
        (h.runtime/'tests.log').write_text(r.stdout+r.stderr)
        out={'ok':r.returncode==0,'code_sha256':code_hash(),'at':now(),'returncode':r.returncode,'log':'runtime/tests.log'}
        atomic(h.runtime/'tests.json',out)
    elif a.cmd=='daemon':
        if a.interval != 600: raise ValueError('Cadence obligatoire:600s')
        with (h.runtime/'.daemon.lock').open('a+') as lock:
            try: fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
            except BlockingIOError: raise ValueError('Veille déjà active')
            while True:
                begin=time.monotonic()
                try: print(json.dumps(h.watch(),ensure_ascii=False),flush=True)
                except Exception as exc:
                    atomic(h.runtime/'watch.json',{'ok':False,'observed_at':now(),'error':str(exc)})
                    print(json.dumps({'error':str(exc),'at':now()}),flush=True)
                time.sleep(max(1,a.interval-(time.monotonic()-begin)))
        return
    print(json.dumps(out,ensure_ascii=False,indent=2))
    if a.cmd=='gate' and not out['allowed']: sys.exit(2)
    if a.cmd=='self-test' and not out['ok']: sys.exit(2)
    if a.cmd=='validate' and not out['technical_contract_pass']: sys.exit(2)

if __name__=='__main__':
    try: main()
    except (ValueError, KeyError, OSError, subprocess.SubprocessError) as e:
        print(json.dumps({'error':str(e)},ensure_ascii=False));sys.exit(2)
