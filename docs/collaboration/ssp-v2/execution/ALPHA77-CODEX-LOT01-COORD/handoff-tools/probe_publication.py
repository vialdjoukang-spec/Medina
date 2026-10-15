"""Vérifie la publication réelle à partir des reçus attendus, sans audit médical."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import urllib.request
from urllib.parse import urljoin, urlsplit

WORK = Path(os.environ.get('MEDINA_PROBE_WORK', '/workspace/work'))
REPO = Path(os.environ.get('MEDINA_PROBE_REPO', '/workspace/Medina'))
EXPECTED = json.loads((WORK / 'pages-probe-expectations.json').read_text())
BASE = EXPECTED['site_base_url']
OUT = WORK / 'public-site-probe.json'
SITE = WORK / 'public-site'
SITE.mkdir(exist_ok=True)

def fetch(url):
    assert url.startswith(BASE), url
    request = urllib.request.Request(url, headers={'User-Agent': 'Medina-publication-proof/1.0'})
    with urllib.request.urlopen(request, timeout=45) as response:
        return response.read(), dict(response.headers), response.geturl()

def digest(raw):
    return hashlib.sha256(raw).hexdigest()

report = {'at': datetime.now(timezone.utc).isoformat(), 'scope': 'HTTP et intégrité de publication ; aucun audit médical nouveau',
          'medical_human_validation': False, 'closed_total': 0, 'checks': [], 'files': []}

def check(label, result):
    report['checks'].append({'check': label, 'passed': bool(result)})

def save():
    report['passed'] = all(row['passed'] for row in report['checks'])
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'passed': report['passed'], 'git_commit': report.get('git_commit'),
                      'checks': len(report['checks']), 'verified_http_files': len(report['files']),
                      'failed': [r['check'] for r in report['checks'] if not r['passed']], 'report': str(OUT)}, ensure_ascii=False))

raw, headers, final_url = fetch(EXPECTED['publication_manifest_url'])
manifest = json.loads(raw)
report.update(git_commit=manifest.get('git_commit'), built_at=manifest.get('built_at'),
              manifest_sha256=digest(raw), manifest_url=final_url)
(SITE / 'publication.json').write_bytes(raw)
for code, expected in EXPECTED['courses'].items():
    alpha = manifest.get('alpha_publications', {}).get(code, {})
    check(code + ': reçu Alpha exact', alpha.get('receipt_sha256') == expected['receipt_sha256'])
    check(code + ': acteur et statut provisoire', alpha.get('actor') == 'Codex' and alpha.get('phase') == 'provisional')
    check(code + ': commit source exact', alpha.get('source_commit') == expected['source_commit'])
    check(code + ': sorties exactes', alpha.get('files') == expected['expected_alpha_files'])
    source = manifest.get('courses', {}).get(code, {}).get('source_files', {})
    check(code + ': sept sources finales exactes', source == expected['expected_source_files'])
    proof = subprocess.run(['git', 'merge-base', '--is-ancestor', expected['source_commit'], str(manifest.get('git_commit'))],
                           cwd=REPO, capture_output=True)
    check(code + ': provenance dans historique publié', proof.returncode == 0)
if not all(row['passed'] for row in report['checks']):
    report['state'] = 'public_manifest_does_not_yet_match_expected_candidates'
    save()
    raise SystemExit(1)

targets = {}
for code, expected in EXPECTED['courses'].items():
    for path in expected['html_document_paths']:
        targets[urljoin(BASE, path)] = {'path': path, 'sha256': manifest.get('site_files', {}).get(path), 'kind': 'built_html'}
    for asset in expected['assets']:
        for url in asset['urls']:
            path = urlsplit(url).path.removeprefix(urlsplit(BASE).path)
            targets[url] = {'path': path, 'sha256': asset['sha256'], 'kind': 'source_asset'}
            check(path + ': asset lié au manifeste', manifest.get('site_files', {}).get(path) == asset['sha256'])

def probe(item):
    url, expected = item
    try:
        body, headers, final_url = fetch(url)
        actual = digest(body)
        path = SITE / expected['path']
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(body)
        return {'url': final_url, 'path': expected['path'], 'kind': expected['kind'], 'bytes': len(body),
                'sha256': actual, 'expected_sha256': expected['sha256'], 'passed': actual == expected['sha256']}
    except Exception as error:
        return {'url': url, 'path': expected['path'], 'passed': False, 'error': str(error)}

with ThreadPoolExecutor(max_workers=2) as pool:
    report['files'] = list(pool.map(probe, targets.items()))
for row in report['files']:
    check(row['path'] + ': octets HTTP exacts', row['passed'])
report['state'] = 'verified_public_bytes' if all(r['passed'] for r in report['checks']) else 'public_bytes_mismatch'
save()
raise SystemExit(0 if report['passed'] else 1)
