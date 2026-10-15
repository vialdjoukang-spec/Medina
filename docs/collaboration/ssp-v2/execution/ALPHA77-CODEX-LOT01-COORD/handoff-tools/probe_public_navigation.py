"""Rendu public réel : réserves visibles, six sciences et neuf sections sémiologiques."""
from datetime import datetime, timezone
import json
import os
import shutil
from pathlib import Path
from urllib.parse import urlsplit, unquote
from playwright.sync_api import sync_playwright

work = Path(os.environ.get('MEDINA_PROBE_WORK', '/workspace/work'))
proof = json.loads((work / 'public-site-probe.json').read_text())
assert proof['passed'], 'Vérifier les octets publics avant le rendu'
expected = json.loads((work / 'pages-probe-expectations.json').read_text())
captures = work / 'public-captures'
captures.mkdir(exist_ok=True)
results = []
network_blocked = False
options = dict(headless=True, args=['--no-sandbox'])
chromium_path = os.environ.get('MEDINA_CHROMIUM_PATH') or shutil.which('chromium')
if chromium_path:
    options['executable_path'] = chromium_path
proxy_url = os.environ.get('HTTPS_PROXY') or os.environ.get('HTTP_PROXY')
if proxy_url:
    proxy = urlsplit(proxy_url)
    options['proxy'] = {'server': f'{proxy.scheme}://{proxy.hostname}:{proxy.port or 80}'}
    if proxy.username:
        options['proxy']['username'] = unquote(proxy.username)
    if proxy.password:
        options['proxy']['password'] = unquote(proxy.password)

with sync_playwright() as p:
    browser = p.chromium.launch(**options)
    for width, height in [(1365, 950), (390, 844)]:
        context = browser.new_context(viewport={'width': width, 'height': height}, reduced_motion='reduce')
        for code, course in expected['courses'].items():
            page = context.new_page()
            errors = []
            page.on('pageerror', lambda e: errors.append(str(e)))
            url = course['course_urls'][0]
            row = dict(code=code, viewport=[width, height], url=url, passed=False)
            try:
                response = page.goto(url, wait_until='domcontentloaded', timeout=60000)
                assert response and response.status == 200, 'HTML public non disponible'
                page.wait_for_selector('.mc', timeout=45000)
                assert page.locator('.mc').get_attribute('data-code') == code, 'Mauvais cours rendu'
                page.locator('.mc-tabs [data-p="pA"]').click()
                text = page.locator('.mc').inner_text().replace('\xad', '')
                for notice in course['visible_reservations']:
                    assert notice in text, 'Réserve absente du rendu visible'
                page.locator('.mc-tabs [data-p="pS"]').click()
                tabs = page.locator('.mc .mc-sci-bar [data-s]')
                assert tabs.count() == 6, 'Six sous-onglets scientifiques attendus'
                assert 'Sémiologie fondamentale et analytique' in tabs.first.inner_text()
                first_target = tabs.first.get_attribute('data-s')
                tabs.first.click()
                semio = page.locator(f'.mc [id="{first_target}"]')
                assert semio.is_visible(), 'Sémiologie fondamentale masquée'
                assert semio.locator('h3').first.inner_text() == 'Pour la leçon : quelle est la sémiologie fondamentale et analytique ?', 'Titre sémiologique incorrect'
                assert semio.locator('[data-semiology]').count() == 9, 'Neuf sections sémiologiques attendues'
                page.screenshot(path=str(captures / f'{code}-{width}-semio.png'))
                navigation = []
                for index in range(6):
                    tab = tabs.nth(index)
                    target = tab.get_attribute('data-s')
                    tab.click()
                    assert page.locator(f'.mc [id="{target}"]').is_visible(), f'Sous-onglet inaccessible : {target}'
                    navigation.append(target)
                assert not errors, 'Erreur JavaScript'
                assert page.evaluate('document.documentElement.scrollWidth <= innerWidth + 2'), 'Débordement horizontal du document'
                row.update(passed=True, visible_reservations=True, semio_sections=9, scientific_navigation=navigation,
                           javascript_errors=errors, document_overflow=False)
            except Exception as error:
                row['error'] = str(error)
                if 'Page.goto' in str(error) or 'net::ERR_' in str(error):
                    network_blocked = True
            results.append(row)
            page.close()
            if network_blocked:
                break
        context.close()
        if network_blocked:
            break
    browser.close()

report = dict(at=datetime.now(timezone.utc).isoformat(), git_commit=proof['git_commit'],
              scope='Rendu et navigation des octets publics vérifiés ; aucun nouvel audit médical ni validation humaine',
              medical_human_validation=False, closed_total=0, passed=all(r['passed'] for r in results), results=results)
path = work / 'public-navigation-probe.json'
path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'passed': report['passed'], 'results': len(results), 'failures': [r for r in results if not r['passed']],
                  'report': str(path)}, ensure_ascii=False))
raise SystemExit(0 if report['passed'] else 1)
