"""Composition locale D62, sans appel de modèle ni reçu clinique automatique."""
from pathlib import Path
import json,html,re,textwrap
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[4]
BYKEY={x['key']:x for x in json.loads((OUT/'recherche_D62/sources.json').read_text())['sources']}
SECTIONS={};POP={}
def refs(*keys):return '<div class="src"><p>Sources : '+' ; '.join(f'<a data-reference-source="1" href="{html.escape(BYKEY[k]["url"],quote=True)}" target="_blank" rel="noopener">[{BYKEY[k]["id"]}] {html.escape(BYKEY[k]["titre"])}</a>' for k in keys)+'.</p></div>'
def table(head,rows):return '<table class="t"><thead><tr>'+''.join('<th>'+x+'</th>' for x in head)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+x+'</td>' for x in row)+'</tr>' for row in rows)+'</tbody></table>'
def w(k,label):return f'<button class="w" data-k="d62-{k}">{label}</button>'
def sec(k,title,body,*sources):SECTIONS[str(k)]=f'<section class="ilot" id="d62-{k}"><h2><span class="n">{k}</span> {title}</h2>{body}{refs(*sources)}</section>'
def pop(k,title,body,*sources):
 ident=k if k.startswith('pareto-') else 'd62-'+k
 assert ident not in POP,ident
 POP[ident]=(title,body+refs(*sources))
def key(s):return '<div class="key"><b>À retenir.</b> '+s+'</div>'
def alert(s):return '<div class="alert"><b>Point de décision.</b> '+s+'</div>'
def quiz(q,right,a,b,explanation):return '<div class="quiz ui"><p><b>Cas pédagogique fictif.</b> '+q+'</p><button data-ok="1">'+right+'</button><button data-ok="0">'+a+'</button><button data-ok="0">'+b+'</button><p class="fb" hidden>'+explanation+'</p></div>'
def causal(ident,title,items,caption):
 h=30+130*len(items);s=f'<svg xmlns="http://www.w3.org/2000/svg" width="580" height="{h}" viewBox="0 0 580 {h}" role="img" aria-label="{html.escape(title,quote=True)}"><title>{html.escape(title)}</title>'
 for i,item in enumerate(items):
  y=15+130*i;lines=textwrap.wrap(item,34);s+=f'<rect x="10" y="{y}" width="560" height="106" rx="8" fill="white" stroke="#222"/><text x="290" y="{y+51-14*(len(lines)-1)}" text-anchor="middle" font-size="27" fill="#222">'+''.join(f'<tspan x="290" dy="{0 if j==0 else 29}">{html.escape(line)}</tspan>' for j,line in enumerate(lines))+'</text>'
  if i<len(items)-1:s+=f'<text x="290" y="{y+128}" text-anchor="middle" font-size="25" fill="#222">↓</text>'
 return f'<figure id="{ident}">{s}</svg><figcaption><b>{title}.</b> {caption} Schéma causal non anatomique ; aucune structure du corps dessinée.</figcaption></figure>'
IMAGES={
 'marrow':dict(file='normal-marrow-openstax2016.jpg',source='NORMAL-IMAGE',credit='OpenStax, édition8.25 du18mai2016',license='CC BY4.0',license_url='https://creativecommons.org/licenses/by/4.0/',title='Le tissu médullaire qui renouvelle le sang',alt='Photographie de coupe osseuse avec travées claires et espaces médullaires rouges',caption='<b>Repère1, centre rouge :</b> tissu médullaire entre les travées. <b>Repère2, travées pâles :</b> charpente de l’os spongieux. <b>Repère3, bord de la pièce :</b> limite osseuse du compartiment. <b>Repère4, barre blanche supérieure :</b> barre originale conservée, sans valeur mesurée faute d’étalonnage lisible. Cette photographie macroscopique localise la moelle ; elle ne montre ni un taux de réticulocytes ni une réponse immédiate à une perte sanguine.'),
 'blood':dict(file='normal-peripheral-blood.jpg',source='BLOOD-IMAGE',credit='Степанюк Ярослав et Борис Максим, photographie diffusée sur Wikimedia Commons',license='CC BY4.0',license_url='https://creativecommons.org/licenses/by/4.0/',title='Un frottis humain : une image n’est pas une concentration',alt='Champ large de frottis humain avec nombreux disques rouges et barre originale100micromètres en haut à gauche',caption='<b>Repère1, disques rouges :</b> hématies réparties sur le champ. <b>Repère2, centre plus clair de nombreux disques :</b> contraste de coloration, sans mesure individuelle. <b>Repère3, régions plus denses :</b> la répartition sur une lame varie ; elle ne donne pas l’hémoglobine du patient. <b>Repère4, haut gauche :</b> échelle originale100µm conservée. Ce faible grossissement ne permet pas d’identifier une réticulocytose ni une carence martiale. Aucun aspect de ce champ ne prouve ou n’exclut une hémorragie aiguë.')}
def original(which,ident):
 x=IMAGES[which]
 return f'<figure id="{ident}" data-origin="human-original"><img src="assets/img/d62/alpha/codex/{x["file"]}" alt="{html.escape(x["alt"],quote=True)}" loading="lazy"><figcaption><b>{x["title"]}.</b> {x["caption"]} Original : {x["credit"]}, <a href="{BYKEY[x["source"]]["url"]}" target="_blank" rel="noopener">provenance</a>, <a href="{x["license_url"]}" target="_blank" rel="noopener">{x["license"]}</a>. Pixels intacts ; repères français situés dans cette légende.</figcaption></figure>'
