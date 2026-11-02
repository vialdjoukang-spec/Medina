"""Composition locale D63 : aucune génération distante et aucun reçu automatique."""
from pathlib import Path
import json,html,textwrap
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[4]
BYKEY={s['key']:s for s in json.loads((OUT/'recherche_D63/sources.json').read_text())['sources']}
SECTIONS={};POP={}
def refs(*keys):
 return '<div class="src"><p>Sources : '+' ; '.join(f'<a data-reference-source="1" href="{html.escape(BYKEY[k]["url"],quote=True)}" target="_blank" rel="noopener">[{BYKEY[k]["id"]}] {html.escape(BYKEY[k]["titre"])}</a>' for k in keys)+'.</p></div>'
def table(head,rows):
 return '<table class="t"><thead><tr>'+''.join('<th>'+x+'</th>' for x in head)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+x+'</td>' for x in row)+'</tr>' for row in rows)+'</tbody></table>'
def w(k,label):return f'<button class="w" data-k="d63-{k}">{label}</button>'
def sec(k,title,body,*sources):SECTIONS[str(k)]=f'<section class="ilot" id="d63-{k}"><h2><span class="n">{k}</span> {title}</h2>{body}{refs(*sources)}</section>'
def pop(k,title,body,*sources):POP['d63-'+k]=(title,body+refs(*sources))
def key(t):return '<div class="key"><b>À retenir.</b> '+t+'</div>'
def quiz(question,right,wrong1,wrong2,explanation):return '<div class="quiz ui"><p><b>Cas pédagogique fictif.</b> '+question+'</p><button data-ok="1">'+right+'</button><button data-ok="0">'+wrong1+'</button><button data-ok="0">'+wrong2+'</button><p class="fb" hidden>'+explanation+'</p></div>'
def causal(ident,title,items,caption):
 h=30+130*len(items);svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="580" height="{h}" viewBox="0 0 580 {h}" role="img" aria-label="{html.escape(title,quote=True)}"><title>{html.escape(title)}</title>'
 for i,item in enumerate(items):
  y=15+130*i;lines=textwrap.wrap(item,34);svg+=f'<rect x="10" y="{y}" width="560" height="106" rx="8" fill="white" stroke="#222"/><text x="290" y="{y+51-14*(len(lines)-1)}" text-anchor="middle" font-size="27" fill="#222">'+''.join(f'<tspan x="290" dy="{0 if j==0 else 29}">{html.escape(line)}</tspan>' for j,line in enumerate(lines))+'</text>'
  if i<len(items)-1:svg+=f'<text x="290" y="{y+128}" text-anchor="middle" font-size="25" fill="#222">↓</text>'
 return f'<figure id="{ident}">{svg}</svg><figcaption><b>{title}.</b> {caption} Schéma causal pédagogique, sans représentation anatomique synthétique.</figcaption></figure>'
def original(which,ident):
 if which=='marrow':
  file='normal-marrow-openstax2016.jpg';alt='Coupe osseuse originale montrant tissu spongieux et moelle rouge';title='Le compartiment où se fabrique le sang';credit='OpenStax, édition8.25 du18mai2016';url=BYKEY['NORMAL-IMAGE']['url']
  caption='<b>Repère1, centre rouge :</b> tissu médullaire entre les travées. <b>Repère2, travées claires :</b> architecture spongieuse qui délimite les espaces. <b>Repère3, bord périphérique :</b> limite osseuse de la pièce. <b>Repère4, barre blanche supérieure :</b> barre conservée, sans mesure calculée car sa valeur manque dans ce fichier. Cette coupe macroscopique ne montre pas une lignée cellulaire, ne mesure pas le fer et ne diagnostique pas une anémie inflammatoire.'
 else:
  file='normal-peripheral-blood.jpg';alt='Frottis sanguin humain original, champ large et barre100micromètres';title='Les hématies observées dans le sang circulant';credit='Степанюк Ярослав et Борис Максим, Wikimedia Commons';url=BYKEY['BLOOD-IMAGE']['url']
  caption='<b>Repère1, éléments rosés très nombreux :</b> hématies du champ. <b>Repère2, centre plus clair de nombreuses hématies :</b> contraste de coloration visible, sans mesure quantitative d’hypochromie. <b>Repère3, répartition dans le champ :</b> les cellules sont observées sur un frottis, non dans une circulation vivante. <b>Repère4, angle supérieur gauche :</b> barre100µm originale. Ce faible grossissement ne permet ni de compter les réticulocytes, ni de doser le fer, ni d’établirD63. Une coloration et une analyse adaptées répondent à ces autres questions.'
 return f'<figure id="{ident}" data-origin="human-original"><img src="assets/img/d63/alpha/codex/{file}" alt="{alt}" loading="lazy"><figcaption><b>{title}.</b> {caption} Original : {credit}, <a href="{url}" target="_blank" rel="noopener">provenance</a>, <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener">CC BY4.0</a>. Pixels intacts ; annotations françaises de lecture ajoutées à la légende.</figcaption></figure>'
