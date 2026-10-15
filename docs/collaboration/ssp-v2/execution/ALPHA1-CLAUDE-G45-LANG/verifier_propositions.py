#!/usr/bin/env python3
"""Vérification mécanique des propositions LANG de G45 (lecture seule des sources).
Usage : python3 -I docs/collaboration/ssp-v2/execution/ALPHA1-CLAUDE-G45-LANG/verifier_propositions.py   (depuis la racine du worktree)
Contrôles : (1) chaque `ancien` apparaît exactement une fois dans son fichier ;
(2) aucun chevauchement entre deux propositions d'un même fichier ;
(3) l'application simultanée en mémoire laisse inchangée la suite des balises HTML ;
(4) le glossaire modifié reste du Python syntaxiquement valide ;
(5) les ids sont uniques et `fond_inchange` vaut true partout.
Aucune source n'est modifiée."""
import json, re, sys, hashlib, collections
D = 'docs/collaboration/ssp-v2/execution/ALPHA1-CLAUDE-G45-LANG/'
props = json.load(open(D + 'propositions.json', encoding='utf-8'))
res = {'nombre_propositions': len(props), 'ancien_unique': True, 'chevauchements': 0,
       'balises_html_inchangees': True, 'glossaire_syntaxe_valide': None, 'ids_uniques': True,
       'fond_inchange_partout': all(p.get('fond_inchange') is True for p in props), 'details_echecs': []}
if len({p['id'] for p in props}) != len(props): res['ids_uniques'] = False
by = collections.defaultdict(list)
for p in props: by[p['fichier']].append(p)
for f, lst in by.items():
    t = open(f, encoding='utf-8').read()
    spans = []
    for p in lst:
        n = t.count(p['ancien'])
        if n != 1:
            res['ancien_unique'] = False; res['details_echecs'].append((p['id'], 'occurrences=%d' % n)); continue
        i = t.index(p['ancien']); spans.append((i, i + len(p['ancien']), p))
    spans.sort(key=lambda s: s[0])
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]: res['chevauchements'] += 1; res['details_echecs'].append((a[2]['id'], b[2]['id'], 'chevauchement'))
    new = t
    for i, j, p in sorted(spans, key=lambda s: -s[0]): new = new[:i] + p['nouveau'] + new[j:]
    if f.endswith('.html'):
        if re.findall(r'<[^>]+>', t) != re.findall(r'<[^>]+>', new):
            res['balises_html_inchangees'] = False; res['details_echecs'].append((f, 'balises modifiées'))
    elif f.endswith('.py'):
        try: compile(new, f, 'exec'); res['glossaire_syntaxe_valide'] = True
        except SyntaxError as e: res['glossaire_syntaxe_valide'] = False; res['details_echecs'].append((f, str(e)))
res['sha256_propositions'] = hashlib.sha256(open(D + 'propositions.json', 'rb').read()).hexdigest()
print(json.dumps(res, ensure_ascii=False, indent=1))
sys.exit(0 if (res['ancien_unique'] and res['chevauchements'] == 0 and res['balises_html_inchangees'] and res['ids_uniques'] and res['glossaire_syntaxe_valide'] is not False) else 1)
