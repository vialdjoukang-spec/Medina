#!/usr/bin/env python3
"""Build the five-fragment offline review bundle from repository sources."""
import argparse
import hashlib
import subprocess
import sys
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1]
NAME = 'MEDINA_review_2026-10-07.zip'
FRAGMENTS = (
    'MEDINA_S01_cardiovasculaire.html',
    'MEDINA_S02_respiratoire.html',
    'MEDINA_S07_immunitaire.html',
    'MEDINA_S10_locomoteur.html',
    'MEDINA_T1_agents-therapeutique.html',
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--skip-build', action='store_true', help='Use already-built fragments in dist/fragments.')
    parser.add_argument('--out', type=Path, default=ROOT / 'dist' / 'review' / NAME)
    args = parser.parse_args()
    if not args.skip_build:
        subprocess.run([sys.executable, str(ROOT / 'build_front.py'), '--all-fragments'], cwd=ROOT, check=True)

    template = ROOT / 'deliverables' / 'review-2026-10-07'
    files = [('LIRE_AVANT.txt', template / 'LIRE_AVANT.txt')]
    files.extend((name, ROOT / 'dist' / 'fragments' / name) for name in FRAGMENTS)
    files.append(('index.html', template / 'index.html'))
    for _, file in files:
        if not file.is_file():
            parser.error(f'Fichier absent : {file}. Reconstruire sans --skip-build.')

    out = args.out.resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(out, 'w') as archive:
        for name, file in files:
            info = ZipInfo(name, date_time=(2026, 10, 7, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o644 << 16
            archive.writestr(info, file.read_bytes(), compresslevel=9)
    digest = hashlib.sha256(out.read_bytes()).hexdigest()
    out.with_suffix('.sha256').write_text(f'{digest}  {out.name}\n', encoding='utf-8')
    print(f'{out}\n{out.stat().st_size} octets\nSHA-256 : {digest}')


if __name__ == '__main__':
    main()
