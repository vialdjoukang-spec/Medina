#!/usr/bin/env python3
"""Contrats didactiques des sciences et mesures comparables à la base Git.

Ce contrôle détecte les parties vides, figures inaccessibles et liens de lecture
absents. Il ne constitue pas une validation de l'exactitude médicale.
"""
import argparse
import hashlib
from html.parser import HTMLParser
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link',
        'meta', 'param', 'source', 'track', 'wbr'}
INERT = {'script', 'style', 'template'}


class Node:
    """Small source tree: ordered text, parents and explicit descendant searches."""
    def __init__(self, tag, attrs=(), parent=None):
        self.tag, self.attrib, self.parent = tag, {key: value or '' for key, value in attrs}, parent
        self.content = []

    def get(self, name, default=None):
        return self.attrib.get(name, default)

    def getparent(self):
        return self.parent

    def itertext(self):
        if self.tag in INERT:
            return
        for child in self.content:
            if isinstance(child, str):
                yield child
            else:
                yield from child.itertext()

    def find_all(self, tag=None, attrs=None, class_name=None, direct=False):
        found = []
        for child in self.content:
            if isinstance(child, str) or child.tag in INERT:
                continue
            if ((tag is None or child.tag == tag) and
                    all(key in child.attrib and (value is None or child.get(key) == value)
                        for key, value in (attrs or {}).items()) and
                    (class_name is None or class_name in child.get('class', '').split())):
                found.append(child)
            if not direct:
                found.extend(child.find_all(tag, attrs, class_name))
        return found


class ScienceParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node('document')
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        node = Node(tag, attrs, self.stack[-1])
        self.stack[-1].content.append(node)
        if tag not in VOID:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.stack[-1].content.append(Node(tag, attrs, self.stack[-1]))

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index].tag == tag:
                del self.stack[index:]
                break

    def handle_data(self, data):
        self.stack[-1].content.append(data)


def science(source):
    parser = ScienceParser()
    parser.feed(source)
    parser.close()
    panels = parser.root.find_all(attrs={'id': 'pS'})
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

    if not any(exposed(c) and ' '.join(c.itertext()).strip() for c in figure.find_all('figcaption', direct=True)):
        return False
    for node in figure.find_all('svg', attrs={'role': 'img'}):
        if not exposed(node):
            continue
        if node.get('aria-label', '').strip():
            return True
        labels = node.get('aria-labelledby', '').split()
        if labels and all(len(figure.find_all(attrs={'id': label})) == 1 and
                          ' '.join(figure.find_all(attrs={'id': label})[0].itertext()).strip()
                          for label in labels):
            return True
    return any(exposed(node) and node.get('src', '').strip() and node.get('alt', '').strip()
               for node in figure.find_all('img'))


def words(node):
    # Word boundaries ignore concatenation between adjacent HTML elements.
    return len(re.findall(r"\b[\wÀ-ÿ]+(?:[’'-][\wÀ-ÿ]+)*\b", " ".join(node.itertext())))


def measure(panel):
    return {"words": words(panel), "figures": len(panel.find_all('figure')),
            "disciplines": len(panel.find_all(class_name='sci'))}


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
        tabs = current.find_all('button', attrs={'data-s': None})
        units = current.find_all(class_name='sci')
        if (not units or len({u.get('id') for u in units}) != len(units) or
                len(tabs) != len(units) or not all(u.get('id') for u in units) or
                {u.get('id') for u in units} != {t.get('data-s') for t in tabs}):
            report['errors'].append(f'{code}: navigation des disciplines incomplète')
        for unit in units:
            uid = unit.get('id')
            text = ' '.join(unit.itertext())
            figures = unit.find_all('figure')
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
