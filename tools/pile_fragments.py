#!/usr/bin/env python3
"""Pile visible des prochains fragments : catégories CIM et leçons, par IA (consigne de Vial du 8 octobre 2026)."""
import html, json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from fragment_surface import frontend_catalog, FRAGMENT_ACCENTS

def build():
    full, owners, courses = frontend_catalog(ROOT)
    names = {f['id']: f for f in json.loads((ROOT / 'organisation/fragments.json').read_text(encoding='utf-8'))}
    plan = json.loads((ROOT / 'organisation/production_plan.json').read_text(encoding='utf-8'))
    federal = json.loads((ROOT / 'organisation/federal_exam.json').read_text(encoding='utf-8'))['fragments']
    alias = {c: course for course in courses.values() for c in course.get('covers', [course['code']])}
    # Cours rédigés hors canonique : remis pour audit croisé, ou en production interne.
    for pattern, state in (('espace_partage/FRAGMENTS_CLAUDE_A_AUDITER_PAR_CODEX/*/sources/chapters_additions.json', 'remis à Codex'),
                           ('espace_partage/FRAGMENTS_CODEX_A_AUDITER_PAR_CLAUDE/*/sources/chapters_additions.json', 'remis à Claude'),
                           ('livraisons/Livraison */*/travail/sources/chapters_additions.json', 'en production')):
        for path in ROOT.glob(pattern):
            for course in json.loads(path.read_text(encoding='utf-8')):
                course = dict(course, state=state, source_fragment_id=owners.get(course['code']))
                for c in course.get('covers', [course['code']]):
                    alias.setdefault(c, course)
    queues = {'Claude': ['S01'] + plan['agents']['Claude']['queue'], 'Codex': plan['agents']['Codex']['queue']}
    out = {'date': '2026-10-08', 'rule': 'Toutes les catégories CIM du fragment reçoivent un cours ; aucune lacune.', 'queues': {}}
    for agent, queue in queues.items():
        items = []
        for rank, fid in enumerate(queue):
            fed = set(federal.get(fid, {}).get('codes', {}))
            blocks = {}
            for e in sorted((e for e in full['entries'] if owners.get(e['code']) == fid), key=lambda e: e['code']):
                course = alias.get(e['code'])
                b = blocks.setdefault(e['block'], {'block': e['block'], 'title': e.get('blockTitle', ''), 'lessons': []})
                b['lessons'].append({'code': e['code'], 'title': e['title'], 'course': course['code'] if course and course['source_fragment_id'] == fid else None,
                                     'course_title': course['title'] if course and course['source_fragment_id'] == fid else None,
                                     'state': (course.get('state') or 'injecté au canonique') if course and course['source_fragment_id'] == fid else None,
                                     'federal': e['code'] in fed or bool(course and course['code'] in fed)})
            cats = sum(len(b['lessons']) for b in blocks.values())
            done = sum(1 for b in blocks.values() for l in b['lessons'] if l['course'])
            items.append({'id': fid, 'label': names[fid]['label'], 'position': 'actif' if rank == 0 else ('suivant' if rank == 1 else 'en file'),
                          'categories': cats, 'covered': done, 'blocks': list(blocks.values())})
        out['queues'][agent] = items
    return out

def page(data):
    h = html.escape
    def frag(f):
        acc = FRAGMENT_ACCENTS.get(f['id'], '#1f3428')
        detail = f['position'] in ('actif', 'suivant')
        rows = ''.join('<section class="blk"><h4>%s · %s</h4><ul>%s</ul></section>' % (h(b['block']), h(b['title']), ''.join(
            '<li class="%s%s"><b>%s</b> %s<span>%s</span></li>' % ('ok' if l['course'] else 'todo', ' fed' if l['federal'] else '', h(l['code']), h(l['title']),
            ('cours %s — %s · %s' % (h(l['course']), h(l['course_title']), h(l['state']))) if l['course'] else 'cours à produire') for l in b['lessons'])) for b in f['blocks'])
        return ('<details class="frag" style="--acc:%s" %s><summary><span class="pos">%s</span><strong>%s</strong><span class="meter">%d / %d catégories couvertes</span></summary>%s</details>'
                % (acc, 'open' if detail else '', h(f['position']), h(f['label']), f['covered'], f['categories'], rows))
    cols = ''.join('<div class="col"><h2>%s</h2>%s</div>' % (h(a), ''.join(frag(f) for f in q)) for a, q in data['queues'].items())
    return ('<!doctype html><html lang="fr-CH"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>Pile des fragments</title><style>:root{color-scheme:light}body{margin:0;background:#fbfaf7;color:#1b1b1b;font:16px/1.5 "Atkinson Hyperlegible Next",Georgia,serif}'
            'main{max-width:1200px;margin:auto;padding:24px 16px}h1{color:#1f3428;margin:0 0 6px}.lead{margin:0 0 18px;color:#333}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%%,520px),1fr));gap:20px}'
            'h2{border-bottom:3px solid #a3241c;padding-bottom:4px}.frag{background:#fff;border:1.5px solid #d9d6cf;border-left:7px solid var(--acc);border-radius:12px;margin:0 0 12px;padding:10px 14px}'
            'summary{cursor:pointer;display:flex;flex-wrap:wrap;gap:8px;align-items:baseline}.pos{background:var(--acc);color:#fff;border-radius:999px;padding:0 9px;font-size:13px;font-weight:700}'
            '.meter{margin-left:auto;font-size:14px;color:#444}h4{margin:12px 0 4px;color:var(--acc)}ul{list-style:none;margin:0;padding:0}li{padding:4px 6px;border-bottom:1px solid #eee;font-size:14px}'
            'li span{display:block;font-size:12.5px;color:#555}li.ok span{color:#1d6b35}li.todo span{color:#a3241c;font-weight:700}li.fed{background:linear-gradient(90deg,#fff3c9,#fff)}li.fed b::after{content:" ★";color:#9a7412}</style></head>'
            '<body><main><h1>Pile des fragments</h1><p class="lead">Fragment actif et fragment suivant de chaque IA, avec toutes leurs catégories CIM et leurs leçons. Règle : <b>%s</b> ★ = chapitre « Isolate Federal – CH Exam ». Date : %s.</p><div class="grid">%s</div></main></body></html>'
            % (h(data['rule']), h(data['date']), cols))

if __name__ == '__main__':
    d = build()
    (ROOT / 'organisation/pile_fragments.json').write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding='utf-8')
    (ROOT / 'organisation/PILE_FRAGMENTS.html').write_text(page(d), encoding='utf-8')
    for a, q in d['queues'].items():
        print(a, ' | '.join('%s %d/%d' % (f['label'], f['covered'], f['categories']) for f in q[:3]))
