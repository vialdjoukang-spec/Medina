"""Composition locale D65, sans appel de modèle ni reçu clinique automatique."""
from pathlib import Path
import json,html,re,textwrap
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[4]
BYKEY={x['key']:x for x in json.loads((OUT/'recherche_D65/sources.json').read_text())['sources']}
SECTIONS={};POP={}
def refs(*keys):return '<div class="src"><p>Sources : '+' ; '.join(f'<a data-reference-source="1" href="{html.escape(BYKEY[k]["url"],quote=True)}" target="_blank" rel="noopener">[{BYKEY[k]["id"]}] {html.escape(BYKEY[k]["titre"])}</a>' for k in keys)+'.</p></div>'
def table(head,rows):return '<table class="t"><thead><tr>'+''.join('<th>'+x+'</th>' for x in head)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+x+'</td>' for x in row)+'</tr>' for row in rows)+'</tbody></table>'
def w(k,label):return f'<button class="w" data-k="d65-{k}">{label}</button>'
def sec(k,title,body,*sources):SECTIONS[str(k)]=f'<section class="ilot" id="d65-{k}"><h2><span class="n">{k}</span> {title}</h2>{body}{refs(*sources)}</section>'
def pop(k,title,body,*sources):
 ident=k if k.startswith('pareto-') else 'd65-'+k
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
 'sem':dict(file='platelets-rbc-wellcome.jpg',cache='/workspace/medina-source-cache/D65/platelets-rbc-wellcome.jpg',source='SEM-IMAGE',credit='David Gregory et Debbie Marshall / Wellcome Collection',license='CC BY 4.0',license_url='https://creativecommons.org/licenses/by/4.0/',title='Une hématie et des plaquettes en microscopie électronique',alt='Micrographie électronique en noir et blanc montrant un disque érythrocytaire concave et un groupe de plaquettes avec une échelle originale de dix micromètres',caption='<b>Repère 1, disque inférieur gauche :</b> hématie dont la concavité se voit sur cette préparation. <b>Repère 2, amas central et droit :</b> éléments plaquettaires de formes irrégulières. <b>Repère 3, contours des plaquettes :</b> reliefs et prolongements visibles ; leur aspect ne quantifie pas une activation chez un patient. <b>Repère 4, barre inférieure :</b> échelle originale de 10 µm. Il s’agit d’une image de structures sanguines, sans diagnostic de CIVD ni mesure de coagulation. Le statut clinique du sujet n’est pas établi par cette notice.'),
 'blood':dict(file='normal-peripheral-blood.jpg',cache='/workspace/Medina-hematologie-D62/assets/img/d62/alpha/codex/normal-peripheral-blood.jpg',source='BLOOD-IMAGE',credit='Степанюк Ярослав et Борис Максим, Wikimedia Commons',license='CC BY 4.0',license_url='https://creativecommons.org/licenses/by/4.0/',title='Le frottis sanguin humain : voir sans surinterpréter',alt='Champ large de frottis sanguin humain avec disques rouges et barre originale de cent micromètres',caption='<b>Repère 1, disques rouges :</b> hématies réparties sur la lame. <b>Repère 2, centres plus clairs :</b> contraste visible de nombreuses cellules, sans mesure individuelle. <b>Repère 3, zones denses et espacées :</b> distribution variable sur la préparation ; elle ne donne pas la numération du patient. <b>Repère 4, haut gauche :</b> barre originale de 100 µm. Ce faible grossissement ne permet pas de certifier une absence de schizocytes. Cette image illustrative ne prouve ni n’exclut une CIVD. Le statut clinique du sujet n’est pas établi par cette notice.')}
def original(which,ident):
 x=IMAGES[which]
 return f'<figure id="{ident}" data-origin="human-original"><img src="assets/img/d65/alpha/codex/{x["file"]}" alt="{html.escape(x["alt"],quote=True)}" loading="lazy"><figcaption><b>{x["title"]}.</b> Crédit : {x["credit"]}. <a href="{BYKEY[x["source"]]["url"]}" target="_blank" rel="noopener">Provenance originale</a> ; <a href="{x["license_url"]}" target="_blank" rel="noopener">{x["license"]}</a>. Pixels intacts. <a href="#{ident}-annotations">Lire les quatre repères français ci-dessous</a>.</figcaption></figure><div class="key" id="{ident}-annotations" role="note"><p><b>Lecture annotée de l’original.</b> {x["caption"]}</p></div>'
