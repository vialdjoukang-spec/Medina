#!/usr/bin/env python3
"""Contrôle du coordinateur pour une leçon d'un cycle Claude en publication directe (cycles 2 à 30).

  python3 tools/cycle_claude_control.py CODE --entry ENTREE.json \
      --check autorisation CHEMIN "Explication…" … (sept identifiants, pour le relevé de sortie)
      [--swiss-matrix CHEMIN] [--cahier CAHIER.json] [--out DOSSIER]
  python3 tools/cycle_claude_control.py CODE --essai DOSSIER [--cahier …]   # contrôle technique seul, sans reçu

Étapes : (1) la leçon doit être EN_CONTROLE dans organisation/CYCLES_CLAUDE.json, avec revue auteur, registre
des sources et manifeste d'images valides ; (2) le relevé d'entrée (tools/claude_cycle_gate.py --prompts direct,
acteur « Claude — coordinateur ») est vérifié ; (3) aperçu isolé construit depuis le dossier de livraison
(tools/night_preview.py) ; (4) test_v7.py --static sur la copie de l'aperçu ; (5) navigateur à 1440 et 390 px :
quatre onglets, toutes les fenêtres, images chargées, débordement horizontal, erreurs JavaScript ; (6) quatre
captures PNG distinctes (ouverture, fenêtre ouverte, figure, tableau) ; (7) matrice suisse de l'auteur vérifiée
par espace.swiss_context_proof ; (8) relevé de sortie puis reçu control.json, revalidé par la garde.

L'outil n'invente rien : il ne rédige aucune explication (elles viennent de --check), n'écrit pas control.json
si un contrôle échoue et s'arrête en erreur. Revue IA, sans validation médicale humaine.
"""
import argparse
import functools
import hashlib
import http.server
import json
import re
import shutil
import subprocess
import sys
import tempfile
import threading
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import cycle_claude as G  # noqa: E402
import night_cycle as N  # noqa: E402
import tetrade_cycle as C  # noqa: E402
import claude_cycle_gate as GATE  # noqa: E402

RUNTIME = 'claude-code/session_01NNsXRGeno3p5fi2QvuhRCM/coordinateur'
TABS = ('pA', 'pE', 'pS', 'pP')
VIEWPORTS = {'desktop': {'width': 1440, 'height': 1000}, 'mobile': {'width': 390, 'height': 844}}
CAPTURE_KINDS = ('ouverture', 'fenetre', 'figure', 'tableau')


class ControlError(RuntimeError):
    pass


class Disk:
    def read(self, path, required=True):
        p = ROOT / path
        if not p.is_file():
            if required:
                raise C.CycleError('Absent ' + str(path))
            return None
        return p.read_bytes()


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def rel(path):
    return Path(path).resolve().relative_to(ROOT).as_posix()


def lesson(code):
    data = json.loads((ROOT / G.REGISTRY).read_text(encoding='utf-8'))
    cycle = next((c for c in data['cycles'] if c['state'] == 'ACTIF'), None)
    if cycle is None or not G.direct(cycle):
        raise ControlError('Aucun cycle Claude actif en publication directe')
    row = next((r for r in cycle['chapters'] if r['code'] == code), None)
    if row is None or row['status'] != 'EN_CONTROLE':
        raise ControlError(f'{code} : leçon absente du cycle actif ou pas EN_CONTROLE')
    return cycle, row


# --------------------------------------------------------------------------- aperçu et contrôles techniques

def static_check(overlay, code):
    """test_v7.py --static exécuté sur une copie réelle dans l'aperçu isolé."""
    script = overlay / 'test_v7.py'
    if script.is_symlink():
        script.unlink()
    shutil.copy2(ROOT / 'test_v7.py', script)
    run = subprocess.run([sys.executable, str(script), '--static', code], cwd=overlay, capture_output=True, text=True)
    output = run.stdout + run.stderr
    abbreviations = re.findall(r'abréviations non couvertes (.+)', output)
    windows = re.findall(r'fenêtres manquantes (\[.*\])', output)
    return run.returncode, output, abbreviations, windows


@functools.lru_cache(None)
def _server(directory):
    class Quiet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *args):
            pass
    handler = functools.partial(Quiet, directory=directory)
    server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server


WINDOWS_JS = """(tab) => {
  const panel=document.getElementById(tab), missing=[];
  for (const el of panel.querySelectorAll('[data-k]')) {
    el.click();
    const d=document.querySelector('.mc-dlg[open]'), text=(d?.querySelector('.mc-dlg-b')?.innerText||'').trim();
    if(!d||text.length<20||text.includes('Fiche absente')) missing.push(el.dataset.k);
    if(d) d.close();
  }
  return {count: panel.querySelectorAll('[data-k]').length, missing};
}"""

IMAGES_JS = """async (tab) => {
  const imgs=[...document.getElementById(tab).querySelectorAll('img')];
  imgs.forEach(i=>{i.loading='eager'});
  await Promise.all(imgs.map(i=>i.decode().catch(()=>null)));
  return imgs.filter(i=>!(i.complete&&i.naturalWidth>0)).map(i=>i.getAttribute('src'));
}"""


def inspect(html, code, shots):
    from playwright.sync_api import sync_playwright
    server = _server(str(html.parent))
    url = f'http://127.0.0.1:{server.server_address[1]}/{html.name}#/entry/{code}'
    report = {'missing_windows': [], 'javascript_errors': [], 'broken_images': [], 'missing_tabs': [],
              'overflow': [], 'windows_checked': 0, 'captures': []}
    with sync_playwright() as p:
        import os
        exe = os.environ.get('MEDINA_CHROMIUM') or next((x for x in ['/opt/pw-browsers/chromium'] if os.path.exists(x)), None)
        browser = p.chromium.launch(headless=True, args=['--no-sandbox', '--disable-dev-shm-usage'],
                                    **({'executable_path': exe} if exe else {}))
        try:
            for name, viewport in VIEWPORTS.items():
                page = browser.new_page(viewport=viewport, color_scheme='light', reduced_motion='reduce')
                page.set_default_timeout(20000)
                page.on('pageerror', lambda e, n=name: report['javascript_errors'].append(f'{n}: {e}'))
                page.goto(url, wait_until='domcontentloaded', timeout=60000)
                page.wait_for_function('window.MDN_READY===true', timeout=60000)
                course = page.locator(f'.mc[data-code="{code}"]')
                course.wait_for(state='visible')
                if course.evaluate("el=>el.classList.contains('book')"):
                    page.locator('.mc-book').click()
                for tab in TABS:
                    button = page.locator(f'.mc[data-code="{code}"] .mc-tabs button[data-p="{tab}"]')
                    if not button.count():
                        report['missing_tabs'].append(f'{name}: {tab}'); continue
                    button.click()
                    panel = page.locator(f'#{tab}')
                    if not panel.is_visible() or len(panel.inner_text().strip()) < 40:
                        report['missing_tabs'].append(f'{name}: {tab}')
                    report['broken_images'] += [f'{name}: {s}' for s in page.evaluate(IMAGES_JS, tab)]
                    windows = page.evaluate(WINDOWS_JS, tab)
                    report['missing_windows'] += [k for k in windows['missing'] if k not in report['missing_windows']]
                    if name == 'desktop':
                        report['windows_checked'] += windows['count']
                    if page.evaluate('document.documentElement.scrollWidth > innerWidth + 1'):
                        report['overflow'].append(f'{name}: {tab}')
                if name == 'desktop':
                    report['captures'] = capture(page, code, shots)
                page.close()
        finally:
            browser.close()
    return report


def capture(page, code, shots):
    """Quatre captures à quatre endroits distincts du cours, au format bureau."""
    shots.mkdir(parents=True, exist_ok=True)
    out = []

    def shot(kind):
        page.evaluate('new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)))')
        path = shots / f'{code.lower()}-{len(out) + 1}-{kind}.png'
        page.screenshot(path=str(path), full_page=False)
        out.append({'kind': kind, 'path': rel(path), 'sha256': sha(path)})

    def show(selector):
        element = page.locator(f'.mc[data-code="{code}"] .mc-panel {selector}').first
        if not element.count():
            raise ControlError(f'{code} : aucun élément « {selector} » à capturer')
        tab = element.evaluate("el => el.closest('.mc-panel').id")
        page.locator(f'.mc-tabs button[data-p="{tab}"]').click()
        element.scroll_into_view_if_needed()
        return element

    page.locator('.mc-tabs button[data-p="pA"]').click()
    page.evaluate("scrollTo({top:0,behavior:'instant'})")
    shot('ouverture')
    trigger = page.locator('#pA [data-k]').first
    if not trigger.count():
        raise ControlError(f"{code} : aucun mot interactif dans l'onglet Pathologie")
    trigger.scroll_into_view_if_needed(); trigger.click()
    page.locator('.mc-dlg[open]').wait_for(state='visible')
    shot('fenetre')
    page.keyboard.press('Escape')
    image = show('img')
    image.evaluate('i => i.decode().catch(() => null)')
    shot('figure')
    show('table')
    shot('tableau')
    return out


def technical_checks(code, cycle, cahier, files, out):
    sys.path.insert(0, str(ROOT))
    import night_preview
    with tempfile.TemporaryDirectory() as tmp:
        preview = night_preview.build(ROOT, code, Path(tmp), cycle, cahier)
        if preview['source_files'] != files:
            raise ControlError(f'{code} : aperçu construit sur des sources différentes des empreintes du registre')
        overlay = Path(tmp) / 'overlay'
        status, output, abbreviations, static_windows = static_check(overlay, code)
        browser = inspect(Path(preview['html']), code, out)
    technical = {
        'code': code, 'final_files': files, 'checked_at': datetime.now(timezone.utc).isoformat(),
        'preview': {'tool': 'tools/night_preview.py', 'cahier_sha256': preview['cahier_sha256'], 'canonical_injection': False},
        'static': {'tool': 'test_v7.py --static (copie dans l’aperçu)', 'exit': status, 'output': output.strip()[-4000:]},
        'viewports': VIEWPORTS, 'tabs': list(TABS), 'windows_checked': browser['windows_checked'],
        'desktop': not any(x.startswith('desktop') for x in browser['missing_tabs'] + browser['overflow']),
        'mobile': not any(x.startswith('mobile') for x in browser['missing_tabs'] + browser['overflow']),
        'missing_tabs': browser['missing_tabs'], 'missing_windows': sorted(set(browser['missing_windows']) | set(static_windows)),
        'javascript_errors': browser['javascript_errors'], 'uncovered_abbreviations': abbreviations,
        'broken_images': browser['broken_images'], 'horizontal_overflow': bool(browser['overflow']),
        'overflow': browser['overflow'], 'captures': browser['captures'],
        'medical_human_validation': False,
    }
    ok = (status == 0 and technical['desktop'] and technical['mobile'] and not technical['missing_windows'] and
          not technical['javascript_errors'] and not abbreviations and not technical['broken_images'] and
          not technical['horizontal_overflow'] and len(technical['captures']) == G.CAPTURES and
          len({c['sha256'] for c in technical['captures']}) == G.CAPTURES)
    technical['result'] = 'passed' if ok else 'failed'
    return technical


# --------------------------------------------------------------------------- matrice suisse

def swiss_context(row, author, files, explicit):
    from espace import swiss_context_proof, FragmentError
    candidates = []
    if explicit:
        candidates.append(explicit)
    ref = author.get('swiss_context') or {}
    if ref.get('matrix_path'):
        candidates.append(ref['matrix_path'])
    for path in sorted((ROOT / row['source_dir']).rglob('*.json')):
        try:
            data = json.loads(path.read_text(encoding='utf-8'))
        except (ValueError, UnicodeError):
            continue
        if isinstance(data, dict) and data.get('chapter_code') == row['code'] and data.get('scope') == 'chapter' \
                and data.get('source_files') == files:
            candidates.append(rel(path))
    errors = []
    for path in dict.fromkeys(candidates):
        proof = {'verdict': 'conforme', 'matrix_path': path, 'matrix_sha256': sha(ROOT / path)}
        try:
            swiss_context_proof(Disk(), {'swiss_context': proof}, row['fragment_id'], files, scope='chapter', chapter_code=row['code'])
            return proof
        except FragmentError as error:
            errors.append(f'{path} : {error}')
    raise ControlError('Matrice suisse de l’auteur absente ou non conforme' + (' — ' + ' ; '.join(errors) if errors else ''))


# --------------------------------------------------------------------------- reçu

def control(a):
    cycle, row = lesson(a.code)
    disk = Disk()
    files = C.source_files(disk, row, G.SOURCE_ROOTS)
    author = C.review(disk, row, 'author', row['writer'], files, G.author_prompts(row))
    C.source_ledger_proof(disk, row, author, files)
    images = N.image_proof(disk, row)
    entry = json.loads((ROOT / a.entry).read_text(encoding='utf-8'))
    C.prompt_gate(disk, entry, G.COORDINATOR, f'{a.code} contrôle entrée', G.PROMPTS_DIRECT)
    if C.dated(entry['checked_at']) < C.dated(author['exit']['checked_at']):
        raise ControlError('Relevé d’entrée antérieur à la sortie de l’auteur')
    day = C.dated(cycle['started_at']).date().isoformat()
    out = ROOT / (a.out or f"docs/collaboration/reviews/{day}/CYCLE_{cycle['cycle']:02d}_CLAUDE/{a.code}/controle")
    cahier = a.cahier.resolve() if a.cahier else None
    technical = technical_checks(a.code, cycle['cycle'], cahier, files, out / 'captures')
    technical_path = out / 'technique.json'
    technical_path.write_text(json.dumps(technical, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    if technical['result'] != 'passed':
        raise ControlError(f'Contrôle technique en échec ; détail : {rel(technical_path)}')
    swiss = swiss_context(row, author, files, a.swiss_matrix)
    try:
        exit_gate = GATE.make_gate(G.COORDINATOR, a.check, 'direct')
    except ValueError as error:
        raise ControlError(str(error)) from None
    receipt = {'code': a.code, 'actor': G.COORDINATOR, 'runtime_agent_id': RUNTIME, 'medical_human_validation': False,
               'entry': entry, 'exit': exit_gate, 'final_files': files, 'image_files': images, 'blocking_reserves': [],
               'technical_checks': {'path': rel(technical_path), 'sha256': sha(technical_path)},
               'swiss_context': swiss,
               'note': 'Contrôle technique du coordinateur ; publication directe, audit différé après le Cycle 30. '
                       'Revue IA, sans validation médicale humaine.'}
    path = out / 'control.json'
    path.write_text(json.dumps(receipt, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    try:
        checked = dict(row, control={'path': rel(path), 'sha256': sha(path)})
        report = C.review(disk, checked, 'control', G.COORDINATOR, files, G.PROMPTS_DIRECT)
        C.technical_proof(disk, checked, report, files, G.CAPTURES)
        if C.dated(author['exit']['checked_at']) > C.dated(report['entry']['checked_at']) or \
                author['runtime_agent_id'] == report['runtime_agent_id']:
            raise ControlError('Ordre ou indépendance auteur/coordinateur invalide')
    except Exception:
        path.unlink()
        raise
    print(rel(path))
    print(f"Suite : python3 tools/cycle_claude_stage.py stage {a.code} PRET_A_INJECTER --runtime {RUNTIME} --proof control={rel(path)}")


def trial(a):
    """Contrôle technique seul (aucun reçu) sur les sources du dossier de livraison."""
    sys.path.insert(0, str(ROOT))
    out = Path(a.essai).resolve()
    out.mkdir(parents=True, exist_ok=True)
    import night_preview
    with tempfile.TemporaryDirectory() as tmp:
        preview = night_preview.build(ROOT, a.code, Path(tmp), a.cycle, a.cahier.resolve() if a.cahier else None)
        status, output, abbreviations, windows = static_check(Path(tmp) / 'overlay', a.code)
        global rel
        rel = lambda p: str(Path(p).resolve())  # noqa: E731 - captures hors dépôt
        browser = inspect(Path(preview['html']), a.code, out)
    result = dict(browser, static_exit=status, uncovered_abbreviations=abbreviations, static_missing_windows=windows)
    (out / 'essai.json').write_text(json.dumps(result, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k != 'captures'}, ensure_ascii=False)[:2000])


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('code')
    p.add_argument('--entry', help='Relevé d’entrée (claude_cycle_gate.py --prompts direct)')
    p.add_argument('--check', nargs=3, action='append', metavar=('ID', 'CHEMIN', 'EXPLICATION'), default=[])
    p.add_argument('--swiss-matrix')
    p.add_argument('--cahier', type=Path, help='Cahier du cycle (implicite pour le Cycle 2)')
    p.add_argument('--out', help='Dossier de sortie relatif au dépôt')
    p.add_argument('--essai', help='Contrôle technique seul vers ce dossier, sans reçu')
    p.add_argument('--cycle', type=int, default=2, help='Cycle de l’essai')
    a = p.parse_args()
    try:
        if a.essai:
            trial(a)
        else:
            if not a.entry:
                p.error('--entry est requis')
            control(a)
    except (ControlError, C.CycleError, ValueError, RuntimeError) as error:
        print(f'ÉCHEC : {error}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
