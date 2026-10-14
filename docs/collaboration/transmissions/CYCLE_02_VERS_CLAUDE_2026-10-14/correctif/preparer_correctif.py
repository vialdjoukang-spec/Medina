#!/usr/bin/env python3
"""Prépare deux corrections G45 sans écrire dans le dépôt.

Le programme contrôle les empreintes Git des fichiers complets, puis produit
une proposition séparée, un diff et un reçu. Il ne lève aucune réserve,
ne modifie aucun registre du dépôt et ne publie rien.
Python 3.10+ ; bibliothèque standard uniquement.
"""
from __future__ import annotations

import argparse
import difflib
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import shutil
import sys
import tempfile
from datetime import datetime, timezone
from typing import Any

BASE = ('livraisons/Livraison Codex/N-05-Neurologie/travail/'
        'CYCLE_02_G45/chapters/G45/')
ALLOWED_PATHS = frozenset({BASE + 'G45_pop2.html', BASE + 'G45_d.html'})


class Refusal(ValueError):
    """Une précondition non satisfaite empêche toute préparation."""


def git_blob_sha1(data: bytes) -> str:
    prefix = b'blob ' + str(len(data)).encode('ascii') + b'\x00'
    return hashlib.sha1(prefix + data).hexdigest()


def unique_index(text: str, token: str, context: str) -> int:
    if not token or text.count(token) != 1:
        raise Refusal(f'{context}: une occurrence unique est requise.')
    return text.index(token)


def transform(text: str, operations: list[dict[str, str]]) -> str:
    """Insère uniquement dans les fenêtres/sections explicitement identifiées."""
    current = text
    for op in operations:
        for field in ('scope_start', 'scope_end', 'before', 'marker', 'html'):
            if not isinstance(op.get(field), str) or not op[field]:
                raise Refusal(f'Opération incomplète : {field}')
        marker = f'data-c02-correction="{op["marker"]}"'
        if marker in current:
            raise Refusal(f'Correctif déjà présent : {op["marker"]}')
        if marker not in op['html']:
            raise Refusal('Le contenu proposé ne porte pas son marqueur.')
        start = unique_index(current, op['scope_start'], 'Début de périmètre')
        end = current.find(op['scope_end'], start + len(op['scope_start']))
        if end < 0:
            raise Refusal('Fin de périmètre introuvable.')
        scope = current[start:end]
        offset = unique_index(scope, op['before'], 'Ancre dans le périmètre')
        index = start + offset
        current = current[:index] + op['html'] + current[index:]
        if current.count(marker) != 1:
            raise Refusal('Le marqueur du correctif n’est pas unique.')
    return current


def checked_path(root: Path, relative: str) -> Path:
    rel = PurePosixPath(relative)
    if relative not in ALLOWED_PATHS or rel.is_absolute() or '..' in rel.parts:
        raise Refusal(f'Chemin hors du périmètre autorisé : {relative}')
    target = root.joinpath(*rel.parts)
    if target.resolve() != target:
        raise Refusal(f'Lien symbolique interdit dans le chemin : {relative}')
    if not target.is_file():
        raise Refusal(f'Fichier absent : {relative}')
    return target


def prepare_changes(root: Path, spec: dict[str, Any]) -> list[dict[str, Any]]:
    files = spec.get('files')
    if not isinstance(files, list) or len(files) != len(ALLOWED_PATHS):
        raise Refusal('Les deux fichiers G45 attendus doivent être présents.')
    paths = [f.get('path') for f in files]
    if len(paths) != len(set(paths)) or set(paths) != ALLOWED_PATHS:
        raise Refusal('Périmètre de fichiers incorrect ou dupliqué.')
    changes: list[dict[str, Any]] = []
    # Tous les fichiers sont vérifiés avant la création de la sortie.
    for entry in files:
        path = checked_path(root, entry['path'])
        original = path.read_bytes()
        expected = entry.get('expected_git_blob_sha1', '')
        if not re.fullmatch('[0-9a-f]{40}', expected):
            raise Refusal('Empreinte attendue invalide.')
        found = git_blob_sha1(original)
        if found != expected:
            raise Refusal(
                f'{entry["path"]}: version différente. '
                f'Attendue {expected}, observée {found}. '
                'Une nouvelle comparaison humaine/IA est requise ; aucun forçage prévu.'
            )
        try:
            old_text = original.decode('utf-8')
        except UnicodeDecodeError as exc:
            raise Refusal('Fichier non UTF-8.') from exc
        new_text = transform(old_text, entry.get('operations', []))
        if new_text == old_text:
            raise Refusal('Aucune modification proposée.')
        changed = new_text.encode('utf-8')
        changes.append({
            'path': entry['path'], 'before_bytes': original, 'after_bytes': changed,
            'before_git_blob_sha1': found,
            'before_sha256': hashlib.sha256(original).hexdigest(),
            'after_sha256': hashlib.sha256(changed).hexdigest(),
            'markers': [x['marker'] for x in entry['operations']],
        })
    return changes


def diff_text(changes: list[dict[str, Any]]) -> str:
    result: list[str] = []
    for change in changes:
        lines = difflib.unified_diff(
            change['before_bytes'].decode('utf-8').splitlines(keepends=True),
            change['after_bytes'].decode('utf-8').splitlines(keepends=True),
            fromfile='a/' + change['path'], tofile='b/' + change['path'],
        )
        for line in lines:
            if line.endswith('\n'):
                result.append(line)
            else:
                result.append(line + '\n\\ No newline at end of file\n')
    return ''.join(result)


def build_proposal(repo: Path, output: Path, spec: dict[str, Any]) -> Path:
    root = repo.expanduser().resolve()
    destination = output.expanduser().resolve()
    if not root.is_dir():
        raise Refusal('Le répertoire du dépôt est absent.')
    if destination == root or root in destination.parents:
        raise Refusal('La sortie doit être située EN DEHORS du dépôt.')
    if destination.exists():
        raise Refusal('La sortie existe déjà ; aucun écrasement autorisé.')
    if not destination.parent.is_dir():
        raise Refusal('Le répertoire parent de sortie doit déjà exister.')
    changes = prepare_changes(root, spec)
    stage = Path(tempfile.mkdtemp(prefix='.medina-c02-', dir=destination.parent))
    try:
        for change in changes:
            candidate = stage / 'proposition' / change['path']
            candidate.parent.mkdir(parents=True, exist_ok=True)
            candidate.write_bytes(change['after_bytes'])
        (stage / 'cycle2-g45-partiel.patch').write_text(diff_text(changes), encoding='utf-8')
        receipt = {
            'created_at': datetime.now(timezone.utc).isoformat(),
            'status': 'PROPOSITION GENEREE HORS DEPOT — NON APPLIQUEE',
            'source_head_observed_when_spec_was_prepared': spec.get('head_observed'),
            'input_check': 'Empreintes Git des deux fichiers complets concordantes.',
            'repository_modified': False, 'source_ledger_updated': False,
            'cross_pass2_performed': False, 'counter_audit_performed': False,
            'human_medical_validation': False, 'reserves_lifted': [],
            'publication_performed': False,
            'files': [{k: v for k, v in c.items() if not k.endswith('_bytes')} for c in changes],
            'required_next_steps': spec.get('suite_obligatoire', []),
        }
        (stage / 'recu_proposition.json').write_text(
            json.dumps(receipt, ensure_ascii=False, indent=2) + '\n', encoding='utf-8'
        )
        # Vérification finale : le programme ne s’autorise pas à travailler sur
        # une entrée modifiée concurremment entre lecture et préparation.
        for change in changes:
            if (root / change['path']).read_bytes() != change['before_bytes']:
                raise Refusal('Un fichier source a changé pendant la préparation.')
        if destination.exists():
            raise Refusal('La destination a été créée concurremment.')
        stage.rename(destination)
    except Exception:
        shutil.rmtree(stage, ignore_errors=True)
        raise
    return destination


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, required=True, help='Copie locale de Medina')
    parser.add_argument('--out', type=Path, required=True, help='Nouveau dossier hors dépôt')
    args = parser.parse_args()
    spec_path = Path(__file__).with_name('corrections_G45.json')
    try:
        spec = json.loads(spec_path.read_text(encoding='utf-8'))
        destination = build_proposal(args.repo, args.out, spec)
    except (Refusal, OSError, ValueError) as exc:
        print(f'PREPARATION REFUSEE : {exc}', file=sys.stderr)
        return 2
    print(f'Proposition et diff créés : {destination}')
    print('Aucun fichier du dépôt modifié ; aucune réserve levée ; aucune publication.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
