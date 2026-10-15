#!/usr/bin/env python3
"""Contrats didactiques des sciences et mesures comparables à la base Git.

Ce contrôle détecte les parties vides, figures inaccessibles et liens de lecture
absents. Il ne constitue pas une validation de l'exactitude médicale.
"""
import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path
from lxml import etree, html

ROOT = Path(__file__).resolve().parents[1]
CLASS = "contains(concat(' ',normalize-space(@class),' '),' {} ')"


def science(source):
    try:
        tree = html.fragment_fromstring(source, create_parent=True)
    except etree.ParserError as error:
        raise ValueError('HTML scientifique illisible') from error
    panels = tree.xpath('.//*[@id="pS"]')
    if len(panels) != 1:
        raise ValueError('un unique panneau pS est requis')
    return panels[0]


def git_blob(root, base, path):
    result = subprocess.run(['git', 'show', f'{base}:{path}'], cwd=root,
                            text=True, capture_output=True)
    if result.returncode:
        raise ValueError(f'source de comparaison indisponible : {path} à {base}')
    return result.stdout


def production_proof(root, base, code):
    """Only a production approved in the exact base can explain an absent source."""
    config = json.loads(git_blob(root, base, '.medina/7-starter-codex.json'))
    entries = [item for item in config['queue'] if item.get('code') == code]
    if len(entries) != 1 or entries[0].get('mode') != 'production':
        raise ValueError('aucune nouvelle production approuvée à cette base')
    item = entries[0]
    ident = item['missions']['PRODUCE']
    if not re.fullmatch(r'[A-Za-z0-9_-]+', ident):
        raise ValueError('identifiant de mission invalide')
    mission = json.loads(git_blob(root, base, f'.medina/missions/{ident}.json'))
    if (mission.get('id') != ident or mission.get('state') != 'active' or
            mission.get('role') != 'integrator' or mission.get('codes') != [code] or
            mission.get('actor') != item.get('owner')):
        raise ValueError('mission de production non approuvée')
    receipt_path = Path(item['production_receipt'])
    if receipt_path.is_absolute() or '..' in receipt_path.parts:
        raise ValueError('chemin de reçu invalide')
    receipt = json.loads((root / receipt_path).read_text())
    files = receipt.get('final_files', {})
    required = {f'chapters/{code}/{code}_{part}.html' for part in ('a', 'b', 'c', 'd', 'pop1', 'pop2')}
    required.add(f'glossary/{code.lower()}.py')
    if receipt.get('complete') is not True or receipt.get('mission') != ident or not required <= set(files):
        raise ValueError('reçu de production incomplet ou mission différente')
    for path, digest in files.items():
        if path not in required and not path.startswith(f'assets/img/{code.lower()}/alpha/codex/'):
            raise ValueError('fichier étranger dans le reçu de production')
        if '..' in Path(path).parts or hashlib.sha256((root / path).read_bytes()).hexdigest() != digest:
            raise ValueError('empreinte de production différente des sources actuelles')
    return str(receipt_path)


def accessible_figure(figure):
    def exposed(node):
        # Hidden discipline panels are reachable through tabs; only inspect the figure itself.
        while node is not None:
            style = re.sub(r'\s+', '', node.get('style', '').lower())
            if ('hidden' in node.attrib or node.get('aria-hidden', '').lower() == 'true' or
                    'display:none' in style or 'visibility:hidden' in style):
                return False
            if node is figure:
                return True
            node = node.getparent()
        return False

    if not any(exposed(c) and ' '.join(c.itertext()).strip() for c in figure.xpath('./figcaption')):
        return False
    for node in figure.xpath('.//svg[@role="img"]'):
        if not exposed(node):
            continue
        if node.get('aria-label', '').strip():
            return True
        labels = node.get('aria-labelledby', '').split()
        if labels and all(len(figure.xpath('.//*[@id=$ident]', ident=label)) == 1 and
                          ' '.join(figure.xpath('.//*[@id=$ident]', ident=label)[0].itertext()).strip()
                          for label in labels):
            return True
    return any(exposed(node) and node.get('src', '').strip() and node.get('alt', '').strip()
               for node in figure.xpath('.//img'))


def words(node):
    # Word boundaries ignore concatenation between adjacent HTML elements.
    return len(re.findall(r"\b[\wÀ-ÿ]+(?:[’'-][\wÀ-ÿ]+)*\b", " ".join(node.itertext())))


def measure(panel):
    return {"words": words(panel), "figures": len(panel.xpath('.//figure')),
            "disciplines": len(panel.xpath('.//*[' + CLASS.format('sci') + ']'))}


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--base', required=True, help='SHA Git complet exact de comparaison (40 caractères)')
    parser.add_argument('--out', type=Path)
    parser.add_argument('--codes', nargs='+', help='Limiter le contrôle aux cours indiqués')
    args = parser.parse_args(argv)
    if not re.fullmatch(r'[0-9a-f]{40}', args.base):
        parser.error('--base exige un SHA40 exact, pas une branche ni une abréviation')
    resolved = subprocess.run(['git', 'rev-parse', '--verify', args.base + '^{commit}'],
                              cwd=ROOT, text=True, capture_output=True)
    if resolved.returncode or resolved.stdout.strip() != args.base:
        parser.error('--base doit désigner un commit disponible par son SHA40 exact')
    report = {"base": args.base, "scope": "sciences fondamentales des cours intégrés",
              "courses": {}, "errors": [], "result": "passed"}
    chapters = json.loads((ROOT / 'chapters.json').read_text())
    if args.codes:
        selected = set(args.codes)
        available = {chapter['code'] for chapter in chapters if chapter.get('integrated')}
        if selected - available:
            parser.error('Cours non intégrés : ' + ', '.join(sorted(selected - available)))
        chapters = [chapter for chapter in chapters if chapter['code'] in selected]
    for chapter in chapters:
        if not chapter.get('integrated'):
            continue
        code = chapter['code']
        relative = f'chapters/{code}/{code}_c.html'
        try:
            current = science((ROOT / relative).read_text())
        except (OSError, ValueError) as error:
            report['errors'].append(f'{code}: source actuelle invalide : {error}')
            continue
        proof = None
        baseline_present = True
        before = None
        try:
            previous = git_blob(ROOT, args.base, relative)
        except ValueError:
            baseline_present = False
            try:
                proof = production_proof(ROOT, args.base, code)
                before = {"words": 0, "figures": 0, "disciplines": 0}
            except (OSError, ValueError, KeyError, TypeError) as error:
                report['errors'].append(f'{code}: source de comparaison absente ; preuve de production approuvée requise : {error}')
        else:
            try:
                before = measure(science(previous))
            except ValueError as error:
                report['errors'].append(f'{code}: source de comparaison invalide : {error}')
        details = []
        tabs = current.xpath('.//button[@data-s]')
        units = current.xpath('.//*[' + CLASS.format('sci') + ']')
        if (not units or len({u.get('id') for u in units}) != len(units) or
                len(tabs) != len(units) or not all(u.get('id') for u in units) or
                {u.get('id') for u in units} != {t.get('data-s') for t in tabs}):
            report['errors'].append(f'{code}: navigation des disciplines incomplète')
        for unit in units:
            uid = unit.get('id')
            text = ' '.join(unit.itertext())
            figures = unit.xpath('.//figure')
            if words(unit) < 280:
                report['errors'].append(f'{code}/{uid}: discipline trop brève pour ce contrôle')
            if not figures:
                report['errors'].append(f'{code}/{uid}: aucune figure')
            for figure in figures:
                if not accessible_figure(figure):
                    report['errors'].append(f'{code}/{uid}: figure sans légende ou nom accessible')
            for label in ['Science → clinique.', 'Science → examen.', 'Science → traitement.', 'À retenir.']:
                if label not in text:
                    report['errors'].append(f'{code}/{uid}: lien absent : {label}')
            details.append({"id": uid, "words": words(unit), "figures": len(figures)})
        report['courses'][code] = {"baseline_present": baseline_present,
                                   "production_proof": proof,
                                   "before": before, "after": measure(current), "units": details}
    report['totals'] = {phase: {key: sum(course[phase][key] for course in report['courses'].values() if course[phase] is not None)
                               for key in ['words', 'figures', 'disciplines']}
                        for phase in ['before', 'after']}
    if report['errors']:
        report['result'] = 'failed'
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({"result": report['result'], "courses": len(report['courses']),
                      "totals": report['totals'], "errors": report['errors']}, ensure_ascii=False, indent=2))
    raise SystemExit(bool(report['errors']))


if __name__ == '__main__':
    main()
