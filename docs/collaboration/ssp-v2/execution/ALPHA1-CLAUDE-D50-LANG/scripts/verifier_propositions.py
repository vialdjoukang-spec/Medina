#!/usr/bin/env python3
"""Vérifie mécaniquement propositions.json contre les sources (lecture seule).
Usage : python3 verifier_propositions.py <racine_du_worktree>
Contrôles : (1) chaque `ancien` apparaît exactement une fois dans son fichier ;
(2) aucun chevauchement entre deux `ancien` d'un même fichier ;
(3) après application simulée en mémoire : seules des balises <i> sont ajoutées,
    le glossaire reste compilable. Aucun fichier source n'est modifié."""
import json,sys,os,re,collections
root=sys.argv[1] if len(sys.argv)>1 else '.'
base=os.path.join(root,'docs/collaboration/ssp-v2/execution/ALPHA1-CLAUDE-D50-LANG')
P=json.load(open(os.path.join(base,'propositions.json'),encoding='utf-8'))
props=[p for p in P if p.get('nouveau') is not None]
res={'nombre_propositions':len(props),'ancien_unique':0,'ancien_non_unique':[],'chevauchements':[],'balises_modifiees':[],'glossaire_compile':None}
txt={}
byf=collections.defaultdict(list)
for p in props:
    f=p['fichier']; txt.setdefault(f,open(os.path.join(root,f),encoding='utf-8').read())
    c=txt[f].count(p['ancien'])
    if c==1: res['ancien_unique']+=1; byf[f].append((txt[f].index(p['ancien']),p))
    else: res['ancien_non_unique'].append({'id':p['id'],'occurrences':c})
for f,l in byf.items():
    l.sort(key=lambda x:x[0])
    for (a,pa),(b,pb) in zip(l,l[1:]):
        if a+len(pa['ancien'])>b: res['chevauchements'].append([pa['id'],pb['id']])
    t=txt[f]
    for pos,p in sorted(l,key=lambda x:-x[0]): t=t[:pos]+p['nouveau']+t[pos+len(p['ancien']):]
    tag=lambda s:collections.Counter(re.findall(r'</?([a-zA-Z0-9]+)',s))
    d=tag(t)-tag(txt[f]); e=tag(txt[f])-tag(t)
    if set(d)-{'i'} or e: res['balises_modifiees'].append({'fichier':f,'ajoutees':dict(d),'retirees':dict(e)})
    if f.endswith('.py'):
        try: compile(t,f,'exec'); res['glossaire_compile']=True
        except SyntaxError as ex: res['glossaire_compile']=str(ex)
res['conforme']=(res['ancien_unique']==len(props) and not res['chevauchements'] and not res['balises_modifiees'] and res['glossaire_compile'] is True)
print(json.dumps(res,ensure_ascii=False,indent=1))
