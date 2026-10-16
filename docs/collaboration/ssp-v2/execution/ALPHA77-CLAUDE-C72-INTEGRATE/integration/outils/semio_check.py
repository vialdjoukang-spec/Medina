"""Rejoue la partie structurelle de starter_codex.semiology sur les fichiers finaux."""
import sys, json, importlib.util
root, code = sys.argv[1], sys.argv[2]
spec = importlib.util.spec_from_file_location('sc', root + '/tools/starter_codex.py'); sc = importlib.util.module_from_spec(spec); spec.loader.exec_module(sc)
HTMLTree = sc.HTMLTree
res = []
def need(c, m): res.append({'controle': m, 'resultat': bool(c)})
tab = code.lower() + '-s-semio'
rd = lambda p: open(f'{root}/chapters/{code}/{p}', 'rb').read()
tree = HTMLTree(rd(f'{code}_c.html'))
in_ps = lambda node: any(p['attrs'].get('id') == 'pS' for p in node['parents'])
buttons = [n for n in tree.nodes if n['tag'] == 'button' and in_ps(n) and 'data-s' in n['attrs']]
need(len(buttons) >= 6 and buttons[0]['attrs'].get('data-s') == tab and tree.text(buttons[0]) == 'Sémiologie fondamentale et analytique' and
     buttons[0]['attrs'].get('role') == 'tab' and buttons[0]['attrs'].get('aria-controls') == tab and buttons[0]['attrs'].get('aria-selected') == 'true' and
     buttons[0]['attrs'].get('id') == code.lower() + '-tab-semio', 'Semiology must be the first selected local science tab (>= 6 data-s)')
need(all(b['attrs'].get('aria-selected') == 'false' for b in buttons[1:]), 'Autres boutons aria-selected=false')
panels = [n for n in tree.nodes if n['tag'] == 'div' and n['attrs'].get('id') == tab and 'sci' in n['attrs'].get('class', '').split() and in_ps(n) and n['attrs'].get('aria-labelledby') == code.lower() + '-tab-semio']
need(len(panels) == 1, 'Semiology panel must be inside fundamental pS')
panel = panels[0]
need('hidden' not in panel['attrs'] and panel['attrs'].get('aria-hidden') != 'true', 'Initial semiology panel must be visible')
units = [n for n in tree.nodes if panel in n['parents'] and 'ilot' in n['attrs'].get('class', '').split()]
need(units, 'Semiology first science unit absent')
first = [n for n in tree.nodes if n['tag'] == 'h3' and units and units[0] in n['parents']]
need(first and tree.text(first[0]) == 'Pour la leçon : quelle est la sémiologie fondamentale et analytique ?', 'Incorrect first semiology unit title')
req = ['normal','signs','mechanisms','examination','interpretation','differentials','urgency','limits','sources']
secs = [n for n in tree.nodes if panel in n['parents'] and n['attrs'].get('data-semiology') in req and 'ilot' in n['attrs'].get('class', '').split() and any(c['tag'] == 'h3' and n in c['parents'] and tree.text(c) for c in tree.nodes)]
need({n['attrs']['data-semiology'] for n in secs if ''.join(n['prose']).strip()} == set(req), 'Semiology sections missing or empty')
need([n['attrs']['data-semiology'] for n in secs] == req, 'Ordre des neuf sections')
need(not any(n['tag'] == 'h2' for n in tree.nodes if panel in n['parents']), 'Aucun h2 dans le panneau')
src = [n for n in secs if n['attrs']['data-semiology'] == 'sources']
need(any(n['tag'] == 'a' and n['attrs'].get('href', '').startswith('https://') and any(s in n['parents'] for s in src) for n in tree.nodes), 'Semiology sources need real linked references')
clin = HTMLTree(rd(f'{code}_a.html') + rd(f'{code}_b.html'))
need(any(n['attrs'].get('data-semiology-clinical') == code and ''.join(n['prose']).strip() and any(p['attrs'].get('id') == 'pA' for p in n['parents']) for n in clin.nodes), 'Clinical semiology absent from pathology pA')
pareto = [n for n in tree.nodes if n['attrs'].get('data-k','').startswith('pareto') and panel in n['parents']]
need(not pareto, 'Aucun Pareto dans le panneau data-semiology')
print(json.dumps({'resultat': 'passed' if all(r['resultat'] for r in res) else 'failed', 'controles': res}, ensure_ascii=False, indent=1))
