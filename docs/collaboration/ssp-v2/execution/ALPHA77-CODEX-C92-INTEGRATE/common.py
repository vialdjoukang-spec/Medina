"""Composition locale C92, sans appel de modèle ni signature automatique."""
from pathlib import Path
import json, html, textwrap, re
OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[4]
BYKEY={s['key']:s for s in json.loads((OUT/'recherche_C92/sources.json').read_text())['sources']}
SECTIONS={};POP={}
def refs(*keys):
 return '<div class="src"><p>Sources : '+' ; '.join(f'<a data-reference-source="1" href="{html.escape(BYKEY[k]["url"],quote=True)}" target="_blank" rel="noopener">[{BYKEY[k]["id"]}] {html.escape(BYKEY[k]["titre"])}</a>' for k in keys)+'.</p></div>'
def table(head,rows):
 return '<table class="t"><thead><tr>'+''.join('<th>'+x+'</th>' for x in head)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+x+'</td>' for x in row)+'</tr>' for row in rows)+'</tbody></table>'
def w(k,label):return f'<button class="w" data-k="c92-{k}">{label}</button>'
def sec(k,title,body,*sources):SECTIONS[str(k)]=f'<section class="ilot" id="c92-{k}"><h2><span class="n">{k}</span> {title}</h2>{body}{refs(*sources)}</section>'
def pop(k,title,body,*sources):
 ident=k if k.startswith('pareto-') else 'c92-'+k
 assert ident not in POP,ident
 POP[ident]=(title,body+refs(*sources))
def key(text):return '<div class="key"><b>À retenir.</b> '+text+'</div>'
def alert(text):return '<div class="alert"><b>Point de décision.</b> '+text+'</div>'
def quiz(question,right,wrong1,wrong2,explanation):
 def expand(s):
  for short,long in [('LAM','leucémie aiguë myéloïde'),('LMC','leucémie myéloïde chronique'),('FI','information professionnelle'),('LLC','leucémie lymphoïde chronique')]:s=re.sub(r'\b'+short+r'\b',long,s)
  return s
 right,wrong1,wrong2=map(expand,[right,wrong1,wrong2])
 return '<div class="quiz ui"><p><b>Cas pédagogique fictif.</b> '+question+'</p><button data-ok="1">'+right+'</button><button data-ok="0">'+wrong1+'</button><button data-ok="0">'+wrong2+'</button><p class="fb" hidden>'+explanation+'</p></div>'
def causal(ident,title,items,caption):
 h=30+130*len(items);svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="580" height="{h}" viewBox="0 0 580 {h}" role="img" aria-label="{html.escape(title,quote=True)}"><title>{html.escape(title)}</title>'
 for i,item in enumerate(items):
  y=15+130*i;lines=textwrap.wrap(item,34);svg+=f'<rect x="10" y="{y}" width="560" height="106" rx="8" fill="white" stroke="#222"/><text x="290" y="{y+51-14*(len(lines)-1)}" text-anchor="middle" font-size="27" fill="#222">'+''.join(f'<tspan x="290" dy="{0 if j==0 else 29}">{html.escape(line)}</tspan>' for j,line in enumerate(lines))+'</text>'
  if i<len(items)-1:svg+=f'<text x="290" y="{y+128}" text-anchor="middle" font-size="25" fill="#222">↓</text>'
 return f'<figure id="{ident}">{svg}</svg><figcaption><b>{title}.</b> {caption} Schéma logique pédagogique ; aucune structure anatomique dessinée.</figcaption></figure>'
IMAGES={
 'marrow':dict(file='normal-marrow-openstax2016.jpg',source='NORMAL-IMAGE',credit='OpenStax, édition 8.25 du 18 mai 2016',license='CC BY 4.0',license_url='https://creativecommons.org/licenses/by/4.0/',title='Le compartiment médullaire normal',alt='Photographie de coupe osseuse montrant espaces médullaires rouges entre les travées',caption='<b>Repère 1, centre rouge :</b> tissu médullaire entre les travées. <b>Repère 2, travées claires :</b> charpente spongieuse. <b>Repère 3, périphérie :</b> limite osseuse de la pièce. <b>Repère 4, barre blanche supérieure :</b> barre originale conservée, sans mesure calculée faute de valeur lisible. Cette vue macroscopique localise un compartiment ; elle ne compte ni blastes ni cellules souches et ne montre aucun génotype.'),
 'auer':dict(file='aml-auer-rods.png',source='AUER-IMAGE',credit='VashiDonsk, téléversement original du 4 mai 2006',license='CC BY-SA 3.0',license_url='https://creativecommons.org/licenses/by-sa/3.0/',title='Un indice de différenciation myéloïde',alt='Aspirat médullaire humain de leucémie aiguë myéloïde avec deux flèches rouges originales vers des corps d’Auer',caption='<b>Repère 1, flèche rouge centrale :</b> inclusion cytoplasmique allongée désignée dans l’original. <b>Repère 2, flèche rouge en haut à droite :</b> second repérage original. <b>Repère 3, grandes cellules violettes :</b> population blastique décrite dans la provenance ; apprécier noyau et cytoplasme avec le laboratoire. <b>Repère 4, ensemble du champ :</b> image sélectionnée, sans décompte représentatif de toute la moelle. Les flèches existaient avant MEDINA. Un corps d’Auer oriente vers une différenciation myéloïde ; cette image ne démontre ni PML::RARA ni un sous-type génétique précis.'),
 'apl':dict(file='apl-hypogranular.jpg',source='APL-IMAGE',credit='Mikael Häggström, 29 novembre 2022',license='CC0 1.0',license_url='https://creativecommons.org/publicdomain/zero/1.0/',title='Une LPA peut être peu granuleuse',alt='Frottis sanguin humain de LPA hypogranulaire montrant deux cellules anormales et des hématies',caption='<b>Repère 1, grande cellule à gauche :</b> noyau irrégulier, avec repli du contour. <b>Repère 2, cellule au centre droit :</b> autre noyau irrégulier et cytoplasme périphérique. <b>Repère 3, cytoplasme bleu :</b> les grosses granulations typiques ne sont pas évidentes dans ce champ. <b>Repère 4, disques rosés autour :</b> hématies servant de contexte visuel, sans étalonnage de taille. La provenance indique une LPA hypogranulaire, coloration de Wright. Aucun corps d’Auer n’est affirmé ici ; la photographie seule ne démontre pas PML::RARA.'),
 'cml':dict(file='cml-left-shift.jpg',source='CML-IMAGE',credit='Paulo Henrique Orlandi Mourao, 9 avril 2009',license='CC BY-SA 3.0',license_url='https://creativecommons.org/licenses/by-sa/3.0/',title='Des maturations différentes dans le même frottis',alt='Frottis humain de LMC riche en éléments granulocytaires de maturations différentes',caption='<b>Repère 1, moitié supérieure :</b> éléments nucléés nombreux, aux formes variées. <b>Repère 2, centre inférieur :</b> cellules à noyau segmenté clairement visibles. <b>Repère 3, grandes cellules moins segmentées :</b> contraste de maturation décrit comme déviation à gauche dans la provenance. <b>Repère 4, fond du champ :</b> hématies plus pâles autour des éléments nucléés. Aucun basophile précis ni pourcentage de blastes n’est assigné à cette seule image. Le diagnostic de LMC exige BCR::ABL1 ; une photographie ne mesure pas non plus la leucocytose absolue.')
}
def original(which,ident):
 x=IMAGES[which];u=BYKEY[x['source']]['url'];share=' La figure et ses annotations françaises sont proposées sous CC BY-SA 3.0.' if 'SA' in x['license'] else ''
 return f'<figure id="{ident}" data-origin="human-original"><img src="assets/img/c92/alpha/codex/{x["file"]}" alt="{html.escape(x["alt"],quote=True)}" loading="lazy"><figcaption><b>{x["title"]}.</b> {x["caption"]} Original : {x["credit"]}, <a href="{u}" target="_blank" rel="noopener">provenance</a>, <a href="{x["license_url"]}" target="_blank" rel="noopener">{x["license"]}</a>. Pixels intacts ; repères français ajoutés à la légende.{share}</figcaption></figure>'
