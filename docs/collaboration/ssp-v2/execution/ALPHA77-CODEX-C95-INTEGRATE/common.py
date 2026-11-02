"""Composants éditoriaux C95 ; aucun appel de modèle ou service externe."""
from pathlib import Path
import json,html
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[4]
SOURCES=json.loads((OUT/'recherche_C95/sources.json').read_text())['sources']
BYKEY={s['key']:s for s in SOURCES}
SECTIONS={};POP={}
def refs(*keys):
 return '<div class="src"><p>Sources : '+ ' ; '.join(f'<a data-reference-source="1" href="{html.escape(BYKEY[k]["url"],quote=True)}" target="_blank" rel="noopener">[{BYKEY[k]["id"]}] {html.escape(BYKEY[k]["titre"])}</a>' for k in keys)+'.</p></div>'
def table(head,rows):
 return '<table class="t"><thead><tr>'+''.join('<th>'+x+'</th>' for x in head)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+x+'</td>' for x in row)+'</tr>' for row in rows)+'</tbody></table>'
def w(key,label):return f'<button class="w" data-k="c95-{key}">{label}</button>'
def sec(key,title,body,*keys):
 SECTIONS[str(key)]=f'<section class="ilot" id="c95-{key}"><h2><span class="n">{key}</span> {title}</h2>{body}{refs(*keys)}</section>'
def pop(key,title,body,*keys):POP['c95-'+key]=(title,body+refs(*keys))
def original(which,ident):
 data={
 'marrow':('normal-marrow-openstax2016.jpg','Photographie originale d’une coupe osseuse avec tissu spongieux et moelle rouge',854,791,'Os spongieux et moelle : situer la production sanguine','<b>Au centre :</b> les espaces entre les travées sont occupés par la moelle, visible ici en rouge. <b>À la périphérie :</b> le tissu osseux délimite la pièce. Cette photographie macroscopique montre un site de tissu médullaire ; elle ne permet ni de compter les blastes ni d’attribuer leur lignée. La barre blanche est conservée mais aucune mesure n’en est déduite, sa valeur n’étant pas donnée sur ce fichier.','OpenStax, Anatomy and Physiology, édition8.25 du18mai2016, fichier2205 Bone Marrow','https://commons.wikimedia.org/wiki/File:2205_Bone_Marrow.jpg'),
 'mpal':('flow-g003.png','Cytométrie originale : blastes B myéloïdes en rouge, cellules B matures en bleu et neutrophiles en vert',0,0,'Une population remplit les critères B et myéloïdes','<b>Rouge :</b> population blastique biphénotypique ; les panneaux montrent notamment CD19, CD10, CD22 et CD79a. <b>Bleu :</b> cellules B matures servant de comparaison. <b>Vert :</b> neutrophiles. <b>Panneau de droite :</b> une partie du nuage rouge dépasse le repère de MPO du laboratoire ; ce cas publié satisfait les critères B/myéloïdes et porte une fusion P2RY8::CRLF2. Le trait rose matérialise une intensité, pas50 % de cellules positives. Les axes/logarithmes et contrôles restent ceux de l’original ; on ne recalcule pas le seuil à partir des pixels.','Fuda et Chen, Cancers2025;17:871, figure3','https://doi.org/10.3390/cancers17050871'),
 'dim':('flow-g006.png','Cytométrie originale d’une LLA B à expression faible de MPO, sous le repère de lignée myéloïde',0,0,'Une MPO faible n’établit pas une LAPM','<b>Rouge :</b> lymphoblastes B ; <b>bleu :</b> cellules B matures ; <b>vert :</b> neutrophiles. <b>À droite :</b> le nuage blastique reste sous le repère rose de MPO. Les autres panneaux ne montrent pas une différenciation monocytaire coordonnée. Les auteurs classent ce cas en LLA-B avec expression aberrante faible de MPO. La présence d’un signal n’est donc pas synonyme de seconde lignée. Cette illustration ne mesure ni sensibilité ni spécificité dans une population.','Fuda et Chen, Cancers2025;17:871, figure6','https://doi.org/10.3390/cancers17050871'),
 'aul':('flow-g014.png','Cytométrie originale d’une leucémie aiguë indifférenciée, blastes CD34 CD117 sans marqueurs définissant une lignée',0,0,'LAI : un panel étendu, pas un marqueur manquant','<b>Rouge :</b> blastes CD34+ exprimant CD117, sans MPO, CD3 ou combinaison B définissante. <b>Vert :</b> neutrophiles ; <b>bleu :</b> cellules B ; <b>rose :</b> monocytes. Les panneaux documentent aussi l’absence de profils monocytaires, mégacaryocytaires et érythroïdes ; d’autres marqueurs négatifs figurent dans la légende de l’article. TdT n’est pas fortement exprimée dans ce cas : son absence n’exclut donc pas la LAI. La conclusion suppose la confrontation avec génétique et contexte.','Fuda et Chen, Cancers2025;17:871, figure14','https://doi.org/10.3390/cancers17050871')}
 file,alt,width,height,title,caption,credit,url=data[which]
 dims=f' width="{width}" height="{height}"' if width else ''
 return f'<figure id="{ident}" data-origin="human-original"><img src="assets/img/c95/alpha/codex/{file}" alt="{alt}" loading="lazy"{dims}><figcaption><b>{title}.</b> {caption} Original : {credit}, <a href="{url}" target="_blank" rel="noopener">source</a>, <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener">CC BY4.0</a>. Pixels et repères d’origine conservés ; légende française explicative ajoutée.</figcaption></figure>'
def causal(ident,title,items,caption):
 # Diagramme textuel causal, aucune anatomie ou cellule inventée.
 h=90+75*len(items)
 text='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 '+str(h)+'" role="img" aria-label="'+html.escape(title,quote=True)+'"><title>'+html.escape(title)+'</title>'
 for i,item in enumerate(items):
  y=20+75*i;text+=f'<rect x="20" y="{y}" width="640" height="54" rx="8" fill="#fff7ed" stroke="#92400e"/><text x="340" y="{y+33}" text-anchor="middle" font-size="18" fill="#17365d">{html.escape(item)}</text>'
  if i<len(items)-1:text+=f'<text x="340" y="{y+72}" text-anchor="middle" font-size="21" fill="#92400e">↓</text>'
 return f'<figure id="{ident}">{text}</svg><figcaption><b>{title}.</b> {caption} Diagramme causal pédagogique non anatomique ; les sources de la section en précisent les limites.</figcaption></figure>'
