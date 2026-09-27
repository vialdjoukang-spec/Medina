#!/usr/bin/env python3
"""Usage : python3 restore.py MEDINA_SOURCES.json [dossier_cible]"""
import json,os,sys
d=json.load(open(sys.argv[1],encoding='utf-8'));dst=sys.argv[2] if len(sys.argv)>2 else 'medina'
for k,v in d.items():
    p=os.path.join(dst,k);os.makedirs(os.path.dirname(p) or '.',exist_ok=True);open(p,'w',encoding='utf-8').write(v)
print(len(d),'fichiers restaurés dans',dst)
