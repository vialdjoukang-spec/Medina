#!/usr/bin/env python3
"""7_Starter_Claude — moteur propre à Claude (et à lui seul) qui enchaîne les lots d'audits agressifs MEDINA.

Exigences de prévention des conflits (contrat SSP V2) :
- un lot ne démarre que lorsque le précédent est RÉELLEMENT clos : rapports fusionnés dans main ET
  réservations libérées au registre distant (medina/session-registry) ;
- aucune auto-approbation : le moteur ne crée ni ne modifie aucun manifeste ; il constate la présence
  des missions approuvées dans main et, sinon, émet l'APPEL de relance destiné à la gouvernance ;
- lecture seule : il n'écrit ni dans le dépôt, ni dans le registre ; Claude exécute acquire/start/agents ;
- arrêt à 77 leçons, premier lot inclus (ordre de Vial) : il désactive alors les exécuteurs d'images de la
  campagne (courtier local) et se détruit, sans toucher aux images publiées ni aux preuves.

Usage : seven_starter.py status | watch [--every 120] | destroy
"""
import csv, json, os, re, shutil, signal, subprocess, sys, time
from pathlib import Path

REPO = Path('/home/user/Medina')
HERE = Path(__file__).resolve().parent
STATE = HERE / 'etat.json'
PLAN = 'docs/collaboration/ssp-v2/2026-10-15/attributions-audit.csv'
ROUNDS = [7, 7, 7, 7, 7, 7, 10]          # tour1.json : round_sizes_per_owner
TARGET = 77                              # Vial : 77 leçons au total, premier lot inclus
TOUR1 = ['I61', 'G45', 'E11', 'E12', 'N18', 'D50', 'C77']
GREEN, EMPTY = '🟩', '⬜'


def git(*a):
    return subprocess.run(['git', '-C', str(REPO), *a], capture_output=True, text=True).stdout


def fetch():
    git('fetch', '-q', 'origin', 'main', 'medina/session-registry')


def catalogue():
    rows = list(csv.DictReader(git('show', f'origin/main:{PLAN}').splitlines()))
    codes = [r['code'] for r in rows if r['owner'] == 'Claude']
    rest = [c for c in codes if c not in TOUR1]
    tours, i = [TOUR1], 0
    for n in ROUNDS[1:]:
        tours.append(rest[i:i + n]); i += n
    return [t for t in tours if t], len(codes)


def manifests():
    out = {}
    for path in git('ls-tree', '--name-only', 'origin/main', '.medina/missions/').split():
        try:
            m = json.loads(git('show', f'origin/main:{path}'))
        except json.JSONDecodeError:
            continue
        if m.get('actor') == 'Claude' and m.get('role') == 'audit':
            for c in m.get('codes', []):
                out.setdefault(c, []).append(m)
    return out


def reservations():
    try:
        r = subprocess.run([sys.executable, str(REPO / 'tools/ai_session_guard.py'), 'status', '--base',
                            git('rev-parse', 'origin/main').strip()], capture_output=True, text=True, cwd=REPO)
        return {x['id']: x['state'] for x in json.loads(r.stdout)['reservations']}
    except Exception:
        return None


def report_merged(mid):
    return bool(git('ls-tree', '--name-only', 'origin/main', f'docs/collaboration/ssp-v2/execution/{mid}/rapport.json').strip())


def published(code):
    files = git('ls-tree', '-r', '--name-only', 'origin/main', f'organisation/alpha-publications/Claude/{code}/').split()
    for f in files:
        if f.endswith('.json'):
            try:
                r = json.loads(git('show', f'origin/main:{f}'))
            except json.JSONDecodeError:
                continue
            if r.get('phase') == 'completed' and 'SEMIO' in (r.get('audits') or {}):
                return six_subtabs(code)
    return False


def six_subtabs(code):
    # AGENTS.md : la Sémiologie est le 6e sous-onglet, après cinq disciplines ; absence = MAJEUR bloquant la clôture.
    try:
        src = git('show', f'origin/main:chapters/{code}/{code}_c.html')
    except Exception:
        return False
    tabs = set(re.findall(r'data-s="([^"]+)"', src))
    return len(tabs) >= 6 and f'{code.lower()}-s-semio' in tabs


def lesson_state(code, mans, res):
    ms = [m for m in mans.get(code, []) if m.get('audit_type') in ('medical', 'linguistic', 'langue', 'language') or m['id'].endswith(('-MED', '-LANG'))]
    if len(ms) < 2:
        return 'NON_APPROUVEE'
    ids = [m['id'] for m in ms]
    if res is None:
        return 'REGISTRE_ILLISIBLE'
    audits_ok = all(report_merged(i) for i in ids) and all(res.get(i) == 'released' for i in ids)
    # Règle commune (AGENTS.md, MOTEURS_INDEPENDANTS) : les rapports seuls ne clôturent pas une leçon.
    # Clôture = reçu de publication Alpha dans main (phase completed, audits.SEMIO) pour ce code.
    if audits_ok and published(code):
        return 'CLOSE'
    if audits_ok:
        return 'AUDITEE_NON_PUBLIEE'
    if any(res.get(i) == 'active' for i in ids):
        return 'EN_COURS'
    return 'APPROUVEE_NON_ACQUISE'


def evaluate():
    fetch()
    tours, catalog_size = catalogue()
    mans, res = manifests(), reservations()
    state = []
    for n, codes in enumerate(tours, 1):
        state.append({'tour': n, 'lecons': {c: lesson_state(c, mans, res) for c in codes}})
    closed = sum(v == 'CLOSE' for t in state for v in t['lecons'].values())
    current = next((t for t in state if any(v != 'CLOSE' for v in t['lecons'].values())), None)
    return {'tours': state, 'closes': closed, 'catalogue_audit_claude': catalog_size, 'cible_vial': TARGET,
            'tour_courant': current['tour'] if current else None, 'courant': current}


def save(e, d):
    try:
        STATE.write_text(json.dumps({'maj': time.strftime('%H:%M'), 'jauge': gauge(e), 'decision': d,
                                     'closes': e['closes'], 'tour': e['tour_courant']}, ensure_ascii=False))
    except OSError:
        pass


def gauge(e):
    w = 20
    p = round(w * e['closes'] / TARGET)
    bar = GREEN * p + EMPTY * (w - p)
    t = e['courant']
    det = ' '.join(f"{c}:{s[:4]}" for c, s in t['lecons'].items()) if t else 'catalogue clos'
    return f"7_STARTER {bar} {e['closes']}/{TARGET} leçons closes · tour {e['tour_courant']} · {det}"


def decision(e):
    t = e['courant']
    if e['closes'] >= TARGET:
        return 'FIN_77'
    if t is None:
        return 'CATALOGUE_EPUISE'
    states = set(t['lecons'].values())
    if 'NON_APPROUVEE' in states:
        return 'APPEL_GOUVERNANCE'     # lot précédent clos, missions du lot suivant absentes de main
    if 'AUDITEE_NON_PUBLIEE' in states and states <= {'AUDITEE_NON_PUBLIEE', 'CLOSE'}:
        return 'INTEGRATION_EN_COURS'  # images, corrections, sémiologie, publication Alpha
    if 'APPROUVEE_NON_ACQUISE' in states:
        return 'LANCER_LOT'            # Claude : acquire → worktree → start → 2 agents par leçon
    return 'ATTENDRE'


def call_message(e):
    t = e['courant']
    return (f"[7_STARTER_CLAUDE → GOUVERNANCE] Lot {t['tour'] - 1} clos (rapports fusionnés, réservations libérées). "
            f"Appel de relance : approuver dans main les missions ALPHA-CLAUDE MED et LANG du lot {t['tour']} : "
            + ', '.join(t['lecons']) + ". Aucune auto-approbation ; démarrage dès leur présence dans main.")


def destroy():
    # Désactive les exécuteurs d'images de la campagne (courtier local) ; images publiées et preuves conservées.
    out = subprocess.run(['pgrep', '-f', 'image_codex_finder.py.*serve'], capture_output=True, text=True).stdout.split()
    for pid in out:
        try:
            os.kill(int(pid), signal.SIGTERM)
        except ProcessLookupError:
            pass
    shutil.rmtree(HERE, ignore_errors=True)
    print(f'7_STARTER DÉTRUIT — courtiers images arrêtés : {len(out)} ; images publiées et preuves conservées')


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'status'
    if cmd == 'destroy':
        return destroy()
    if cmd == 'status':
        e = evaluate()
        save(e, decision(e))
        print(gauge(e)); print('DÉCISION', decision(e))
        if decision(e) == 'APPEL_GOUVERNANCE':
            print(call_message(e))
        return
    every = int(sys.argv[sys.argv.index('--every') + 1]) if '--every' in sys.argv else 120
    last = None
    while True:
        try:
            e = evaluate(); d = decision(e); save(e, d); line = gauge(e) + ' · ' + d
            if line != last:
                print(line, flush=True)
                if d == 'APPEL_GOUVERNANCE':
                    print('APPEL ' + call_message(e), flush=True)
                last = line
            if d in ('FIN_77', 'CATALOGUE_EPUISE'):
                print(f'7_STARTER {d} : {e["closes"]} leçons closes ; catalogue Claude = {e["catalogue_audit_claude"]}', flush=True)
                if d == 'FIN_77':
                    destroy()
                return
        except Exception as exc:  # une erreur de lecture n'est jamais un succès silencieux
            print(f'7_STARTER ERREUR {type(exc).__name__}: {exc}', flush=True)
        time.sleep(every)


if __name__ == '__main__':
    main()
