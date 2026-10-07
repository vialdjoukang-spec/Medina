#!/usr/bin/env python3
"""Contrats didactiques des sciences et mesures comparables à la base Git.

Ce contrôle détecte les parties vides, figures inaccessibles et liens de lecture
absents. Il ne constitue pas une validation de l'exactitude médicale.
"""
import argparse
import json
import re
import subprocess
from pathlib import Path
from lxml import html

ROOT = Path(__file__).resolve().parents[1]
BASE = "c50a28a23d7e2a2e0cf8ac36842b567de419daf4"
CLASS = "contains(concat(' ',normalize-space(@class),' '),' {} ')"


def science(source):
    tree = html.fragment_fromstring(source, create_parent=True)
    return tree.xpath('.//*[@id="pS"]')[0]


def words(node):
    # Word boundaries ignore concatenation between adjacent HTML elements.
    return len(re.findall(r"\b[\wÀ-ÿ]+(?:[’'-][\wÀ-ÿ]+)*\b", " ".join(node.itertext())))


def measure(panel):
    return {"words": words(panel), "figures": len(panel.xpath('.//figure')),
            "disciplines": len(panel.xpath('.//*[' + CLASS.format('sci') + ']'))}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path)
    args = parser.parse_args()
    report = {"base": BASE, "scope": "sciences fondamentales des cours intégrés",
              "courses": {}, "errors": [], "result": "passed"}
    chapters = json.loads((ROOT / 'chapters.json').read_text())
    for chapter in chapters:
        if not chapter.get('integrated'):
            continue
        code = chapter['code']
        relative = f'chapters/{code}/{code}_c.html'
        current = science((ROOT / relative).read_text())
        old = science(subprocess.check_output(['git', 'show', f'{BASE}:{relative}'], cwd=ROOT, text=True))
        details = []
        tabs = current.xpath('.//button[@data-s]')
        units = current.xpath('.//*[' + CLASS.format('sci') + ']')
        if {u.get('id') for u in units} != {t.get('data-s') for t in tabs}:
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
                if not figure.xpath('./figcaption') or not figure.xpath('.//svg[@role="img"][@aria-label]'):
                    report['errors'].append(f'{code}/{uid}: figure sans légende ou nom accessible')
            for label in ['Science → clinique.', 'Science → examen.', 'Science → traitement.', 'À retenir.']:
                if label not in text:
                    report['errors'].append(f'{code}/{uid}: lien absent : {label}')
            details.append({"id": uid, "words": words(unit), "figures": len(figures)})
        report['courses'][code] = {"before": measure(old), "after": measure(current), "units": details}
    report['totals'] = {phase: {key: sum(course[phase][key] for course in report['courses'].values())
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
