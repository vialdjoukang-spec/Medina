#!/usr/bin/env python3
"""Empaquette toutes les sources MEDINA dans MEDINA_SOURCES.json (restauration : restore.py)."""
import json,glob,os
ROOT=os.path.dirname(os.path.abspath(__file__));os.chdir(ROOT)
pats=['*.py','*.md','chapters.json','engine/*','shell/*.html','shell/*.py','modules/*.py','modules/ecg.json','glossary/*.py','chapters/*/*.html']
files=sorted({f for p in pats for f in glob.glob(p)})
out=os.environ.get('MEDINA_OUT','/mnt/user-data/outputs' if os.path.isdir('/mnt/user-data') else ROOT+'/dist');os.makedirs(out,exist_ok=True)
json.dump({f:open(f,encoding='utf-8').read() for f in files},open(out+'/MEDINA_SOURCES.json','w'),ensure_ascii=False)
print(len(files),'fichiers',os.path.getsize(out+'/MEDINA_SOURCES.json'),'octets')
