#!/usr/bin/env python3
"""Extension Novo Tétrade ; l'outil historique figé dans les preuves reste intact."""
import argparse
import json
try:
    from tools import claude_cycle_gate as legacy
except ModuleNotFoundError:
    import claude_cycle_gate as legacy

EXTRA_PROMPTS = ('docs/collaboration/betta/PROMPT_VERITE.md',
                 'docs/collaboration/instructions/NOVO12_EXECUTION_VIAL_2026-10-15.md')


def make_gate(actor, entries):
    # Les explications viennent de l'agent ; aucune lecture n'est présumée réelle.
    result = legacy.make_gate(actor, entries, 'direct')
    result['prompt_files'].update({path: legacy.sha(path) for path in EXTRA_PROMPTS})
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--actor', required=True)
    parser.add_argument('--out', required=True)
    parser.add_argument('--prompts', choices=['novo'], default='novo')
    parser.add_argument('--check', nargs=3, action='append', required=True,
                        metavar=('ID', 'CHEMIN', 'EXPLICATION'))
    args = parser.parse_args()
    try:
        gate = make_gate(args.actor, args.check)
    except (ValueError, OSError) as error:
        parser.error(str(error))
    out = legacy.ROOT / args.out
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(out.relative_to(legacy.ROOT))


if __name__ == '__main__':
    main()
