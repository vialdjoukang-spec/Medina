#!/usr/bin/env python3
"""Assembler la rédaction relue ; jamais une validation médicale automatique."""
from pathlib import Path
import subprocess,re,html
ROOT=Path(__file__).resolve().parents[5]
import author_popups2,author_main2,author_exams,author_pharma,author_summaries
from author_main import SECTIONS
from author_sciences import sciences
from author_popups import POP,refs
chapter=ROOT/'chapters/C86'
def base(name):return subprocess.check_output(['git','show','8a512893acbab9caa0dcfdd0e8682a44ea72fda6:chapters/C86/'+name],cwd=ROOT,text=True)
old=base('C86_a.html')
header=old[:old.index('<section class="ilot"')]
header=re.sub(r'<span class="status">.*?</span>','<span class="status">Adulte · sept sous-codes, plusieurs entités · sources suisses puis européennes, classifications OMS et revues ciblées · état au 02.11.2026 · relecture par intelligence artificielle, distincte d’une validation médicale humaine</span>',header,flags=re.S)
pager='<div class="pager ui"><button class="prev">← Partie précédente</button><span></span><button class="next">Partie suivante →</button></div>'
(chapter/'C86_a.html').write_text(header+'\n'.join(SECTIONS[str(i)] for i in range(7))+'\n')
index='<details id="c86-reference-index"><summary>Ouvrir une fiche explicative ou une synthèse</summary><ul>'+''.join(f'<li><button class="w" data-k="{ident}">{html.escape(title)}</button></li>' for ident,(title,body) in POP.items())+'</ul></details>'
end=index+'<div class="src"><p>Les références sont liées aux sections et aux fenêtres. Les résultats de séries sont rattachés à leur population. Les limites restantes et les lectures ciblées figurent dans la fenêtre <button class="w" data-k="c86-lacunes">Sources et limites</button>. Aucune validation médicale humaine n’est revendiquée.</p></div>'
(chapter/'C86_b.html').write_text('\n'.join(SECTIONS[str(i)] for i in range(7,13))+end+'</div>'+pager+'</div>\n')
(chapter/'C86_c.html').write_text('<div class="panel" id="pE" hidden><div class="chap-body">'+'\n'.join(SECTIONS[f'e-{i}'] for i in range(1,6))+'</div>'+pager+'</div>'+sciences()+'\n')
(chapter/'C86_d.html').write_text('<div class="panel" id="pP" hidden><div class="chap-body">'+'\n'.join(SECTIONS[f'p-{i}'] for i in range(1,5))+'</div>'+pager+'</div></div></template>\n')
items=[]
for ident,(title,body) in POP.items():items.append(f'<template data-pop="{ident}" data-title="{html.escape(title,quote=True)}">{body}</template>\n')
cut=(len(items)+1)//2
(chapter/'C86_pop1.html').write_text(''.join(items[:cut]))
(chapter/'C86_pop2.html').write_text(''.join(items[cut:]))
print(f'Assemblage C86 : {len(SECTIONS)} sections principales ; {len(items)} fenêtres ; six sciences. Contrôles encore requis.')
