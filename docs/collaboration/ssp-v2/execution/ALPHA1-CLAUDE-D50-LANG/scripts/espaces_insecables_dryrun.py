#!/usr/bin/env python3
"""Compte (lecture seule) les endroits des nœuds texte HTML où la typographie française
standard demande une espace insécable : avant ; : ! ? et », après «, avant % et avant les
unités (g/L, mg, µg, pg, fl, mmol, µmol, mL, dL, kg, min...). N'écrit rien.
Usage : python3 espaces_insecables_dryrun.py <racine_du_worktree>"""
import re,sys,os,glob,json
root=sys.argv[1] if len(sys.argv)>1 else '.'
pat={
 'avant_; : ! ? »':r'(?<=\S) (?=[;:!?»])',
 'apres_«':r'(?<=«) (?=\S)',
 'avant_%':r'(?<=\d) (?=%)',
 'avant_unite':r'(?<=\d) (?=(?:g/L|g/dL|mg|µg|pg|fl|mmol|µmol|mL|dL|kg|min|mm|cm|h)\b)',
}
tot={}
for f in sorted(glob.glob(os.path.join(root,'chapters/D50/*.html'))):
    t=open(f,encoding='utf-8').read()
    t=re.sub(r'<svg.*?</svg>','',t,flags=re.S)
    c={k:0 for k in pat}
    for m in re.finditer(r'>([^<>]+)<',t):
        for k,p in pat.items(): c[k]+=len(re.findall(p,m.group(1)))
    tot[os.path.basename(f)]=c
print(json.dumps(tot,ensure_ascii=False,indent=1))
