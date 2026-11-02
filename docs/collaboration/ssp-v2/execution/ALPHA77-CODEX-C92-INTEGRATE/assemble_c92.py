#!/usr/bin/env python3
"""Assembler les sources écrites de C92 ; ne signe aucune relecture finale."""
import datetime,hashlib,html,json,re,shutil
from pathlib import Path
from bs4 import BeautifulSoup
from PIL import Image
import author_main,author_main2,author_exams,author_pharma,author_popups
from author_sciences import sciences
from common import ROOT,OUT,SECTIONS,POP,BYKEY,IMAGES

target=ROOT/'chapters/C92';target.mkdir(exist_ok=True)
header='''<template id="ch-C92"><div class="chap">
<div class="chap-head"><div class="code">C92 — Leucémies myéloïdes · LAM, LPA, LMC et entités apparentées · CIM-10-GM 2024 · Sang et organes hématopoïétiques</div>
<h1>Leucémies myéloïdes : de la cellule à la décision</h1><span class="status">Adulte, avec limites pédiatriques et grossesse · sources suisses et européennes datées · état au 02.11.2026 · auto-relecture pédagogique distincte d’une validation médicale humaine</span></div>
<div class="tabs ui" role="tablist"><button role="tab" aria-controls="pA" data-p="pA" aria-selected="true">⚕ Pathologie et prise en charge</button><button role="tab" aria-controls="pE" data-p="pE" aria-selected="false">🔬 Examens complémentaires</button><button role="tab" aria-controls="pS" data-p="pS" aria-selected="false">⚛ Sciences fondamentales spécialisées</button><button role="tab" aria-controls="pP" data-p="pP" aria-selected="false">💊 Pharmacologie</button></div>
<div class="panel" id="pA">'''
toc='<nav class="toc ui"><b>Plan monographique</b><ol>'
for i in range(1,15):
 title=BeautifulSoup(SECTIONS[str(i)],'html.parser').h2.get_text(' ',strip=True)
 title=re.sub(r'^'+str(i)+r'\s*','',title)
 toc+=f'<li><a href="#c92-{i}">{html.escape(title)}</a></li>'
toc+='</ol></nav><div class="chap-body">'
SECTIONS['6']=SECTIONS['6'].replace('id="c92-6"','id="c92-6" data-semiology-clinical="C92"',1)
pager='<div class="pager ui"><button class="prev">← Partie précédente</button><span></span><button class="next">Partie suivante →</button></div>'
index='<details id="c92-reference-index"><summary>Ouvrir une explication ou une synthèse</summary><ul>'+''.join(f'<li><button class="w" data-k="{ident}">{html.escape(title)}</button></li>' for ident,(title,body) in POP.items())+'</ul></details>'
end='<button class="pareto-btn ui" data-k="pareto-c92-cours">▲ Loi de Pareto — Monographie</button>'+index+'<div class="src"><p>Les cas pédagogiques sont fictifs. <button class="w" data-k="c92-sources">Sources, dates et limites</button> ; <button class="w" data-k="c92-profiles">cadre PROFILES et examen fédéral</button>.</p></div>'
files={
'C92_a.html':header+toc+'\n'.join(SECTIONS[str(i)] for i in range(1,8))+'\n',
'C92_b.html':'\n'.join(SECTIONS[str(i)] for i in range(8,15))+end+'</div>'+pager+'</div>\n',
'C92_c.html':'<div class="panel" id="pE" hidden><div class="chap-body">'+'\n'.join(SECTIONS[f'e-{i}'] for i in range(1,6))+'<button class="pareto-btn ui" data-k="pareto-c92-examens">▲ Loi de Pareto — Examens</button></div>'+pager+'</div>'+sciences()+'\n',
'C92_d.html':'<div class="panel" id="pP" hidden><div class="chap-body">'+'\n'.join(SECTIONS[f'p-{i}'] for i in range(1,7))+'<button class="pareto-btn ui" data-k="pareto-c92-pharma">▲ Loi de Pareto — Pharmacologie</button></div>'+pager+'</div></div></template>\n'}
items=[f'<template data-pop="{ident}" data-title="{html.escape(title,quote=True)}">{body}</template>\n' for ident,(title,body) in POP.items()]
cut=(len(items)+1)//2;files['C92_pop1.html']=''.join(items[:cut]);files['C92_pop2.html']=''.join(items[cut:])

# Renvois propres au cours : les définitions globales homonymes ne remplacent pas le contexte.
mapping={'LAM':'classification','LMA':'classification','LPA':'differenciation','LMC':'bcr-abl','BCR::ABL1':'bcr-abl','PML::RARA':'differenciation','MRD':'mrd','MMR':'cml-is','MR4':'cml-is','MR4,5':'cml-is','MR4.5':'cml-is','FLT3':'flt3','ATRA':'differenciation','ATO':'differenciation','TKI':'bcr-abl','ELN':'sources','OMS':'classification','ICC':'classification','OFS':'classification','PROFILES':'profiles','MEBEKO':'profiles','FI':'fi','CYP3A4':'interactions','CYP3A':'interactions','QTcF':'interactions','QTc':'interactions','QT':'interactions'}
regex=re.compile(r'(?<![A-Za-zÀ-ÿ0-9_])('+'|'.join(re.escape(k) for k in sorted(mapping,key=len,reverse=True))+r')(?![A-Za-zÀ-ÿ0-9_])')
def local_refs(body):
 parts=re.split(r'(<[^>]+>)',body);protected=[]
 for i,t in enumerate(parts):
  if i%2:
   m=re.match(r'</?(a|button|svg|script|style)\b',t,re.I)
   if m:
    if t.startswith('</'):
     if protected:protected.pop()
    else:protected.append(m.group(1))
  elif not protected:parts[i]=regex.sub(lambda m:f'<button class="w" data-k="c92-{mapping[m.group(1)]}">{m.group(1)}</button>',t)
 return ''.join(parts)
def spacing(body):
 parts=re.split(r'(<[^>]+>)',body)
 for i in range(0,len(parts),2):
  t=parts[i]
  t=re.sub(r'(?<=\d)(?=(?:ans|mois|jours|heures|mg|kg|mL|min|G/L|g/L|g/dL|mai|novembre|avril)\b)',' ',t)
  t=re.sub(r'\b(de|du|en|à|les|sous|sur|dès|après|avant|édition|repère|Repère|barre)(?=\d)',r'\1 ',t)
  t=re.sub(r'\b(ELN|OMS|ICC|PROFILES|MEBEKO|CIM-10-GM|SSP)(?=\d)',r'\1 ',t)
  t=re.sub(r'(?<=[a-zàâéèêëîïôöùûüç])(?=20(?:1[0-9]|2[0-9])\b)',' ',t)
  t=re.sub(r'(?<=[A-Za-zÀ-ÿ0-9])(?=[≤≥])',' ',t);t=re.sub(r'([≤≥])(?=\d)',r'\1 ',t)
  parts[i]=t
 return ''.join(parts)
for name,body in files.items():
 body=re.sub(r'<(?=\s*[=\d])','&lt;',body)
 (target/name).write_text(local_refs(spacing(body)))

assets=ROOT/'assets/img/c92/alpha/codex';assets.mkdir(parents=True,exist_ok=True);rows=[]
for k,x in IMAGES.items():
 src=(Path('/workspace/Medina-hematologie-D63/assets/img/d63/alpha/codex') if k=='marrow' else Path('/workspace/medina-source-cache/C92'))/x['file']
 dst=assets/x['file'];shutil.copyfile(src,dst)
 with Image.open(dst) as im:width,height=im.size
 rows.append({'file':str(dst.relative_to(ROOT)),'title':x['title'],'sha256':hashlib.sha256(dst.read_bytes()).hexdigest(),'width':width,'height':height,'source_url':BYKEY[x['source']]['url'],'source_ledger_id':BYKEY[x['source']]['id'],'credit':x['credit'],'license':x['license'],'license_url':x['license_url'],'pixel_modification':False,'annotations':'Quatre repères français situés dans la légende ; flèches originales conservées pour Auer, aucune anatomie générée.','original_seen':True,'clinical_certification':False})
(assets/'provenance.json').write_text(json.dumps({'images':rows,'source_review_date':'2026-11-02','review_mode':'self_review; not human clinical validation'},ensure_ascii=False,indent=2)+'\n')
(assets/'ATTRIBUTION.md').write_text('# Originaux C92\n\n'+'\n\n'.join(f'**{r["file"].split("/")[-1]}** — {r["credit"]}. [Provenance]({r["source_url"]}). [{r["license"]}]({r["license_url"]}). Pixels intacts ; quatre repères français dans la légende. SHA256 `{r["sha256"]}`.' for r in rows)+'\n\nLes figures CC BY-SA et leurs annotations sont partagées sous la même licence. L’image OpenStax relève du fichier de 2016, pas du manuel actuel. Les images sélectionnées ne remplacent pas un décompte ni une analyse génétique.\n')

glossary='from cardio_1 import a, G\n# C92 : ajouts conditionnels, aucun terme global existant écrasé.\n'
terms=[('LAM','Leucémie aiguë myéloïde','Entité définie par morphologie et génétique selon une classification datée ; exceptions au seuil de blastes.','classification'),('LPA','Leucémie promyélocytaire aiguë','Leucémie associée à PML::RARA, avec risque de coagulopathie et circuit urgent.','differenciation'),('LMC','Leucémie myéloïde chronique','Néoplasie définie par BCR::ABL1, à caractériser et suivre par méthodes adaptées.','bcr-abl'),('MRD','Maladie résiduelle mesurable','Signal résiduel étudié avec marqueur, méthode et sensibilité connus ; négativité ne signifie pas éradication certaine.','mrd'),('MMR','Réponse moléculaire majeure','En LMC, BCR::ABL1 IS ≤ 0,1 % avec contrôles appropriés.','cml-is'),('TFR','Rémission sans traitement','Arrêt surveillé du TKI chez une personne sélectionnée, avec suivi moléculaire durable.','tfr'),('ATRA','Acide tout-trans rétinoïque','Trétinoïne utilisée notamment dans la LPA ; différenciation et toxicités nécessitent surveillance.','differenciation'),('ATO','Trioxyde d’arsenic','Produit utilisé dans des indications précises de LPA ; surveillance du QT et des électrolytes.','differenciation')]
terms += [
('ABL','Notation ABL du libellé de codage','Abréviation présente dans le libellé historique BCR/ABL de la CIM-10-GM ; le texte biologique moderne précise BCR::ABL1.','bcr-abl'),
('ICD-10-CM','Modification clinique américaine de la CIM-10','Classification américaine distincte de la CIM-10-GM employée dans le projet suisse ; ne pas importer ses caractères de rechute.','classification'),
('ETNK1','Symbole du gène ETNK1','Une mutation peut soutenir le diagnostic de MDS/MPN avec neutrophilie dans le contexte approprié ; elle ne définit pas seule la maladie.','genetique'),
('R132','Position 132 de la protéine IDH1','Notation de la position arginine 132 concernée par les mutations ciblées dans l’indication de Tibsovo.','genetique'),
('TKI','Inhibiteur de tyrosine kinase','Classe de traitements dont cible, site de liaison, indication et interactions doivent être précisés.','bcr-abl'),
('IS','Échelle internationale','International Scale : standardisation de BCR::ABL1 pour les transcrits usuels ; contrôle analytique requis.','cml-is'),
('VashiDonsk','VashiDonsk, auteur du fichier original','Nom du contributeur de la photographie Auer rods sur Wikimedia Commons ; nom propre, pas abréviation médicale.','sources'),
('HMA','Agent hypométhylant','Terme de classe utilisé dans les recommandations ; produit et formulation exacts restent à préciser.','strategie'),
('CR','Rémission complète','Catégorie de réponse définie par morphologie, absence de maladie extramédullaire et récupération hématologique selon critères ELN.','reponse'),
('CRh','Rémission complète avec récupération hématologique partielle','Autres critères de CR, neutrophiles ≥ 0,5 G/L et plaquettes ≥ 50 G/L selon ELN 2022.','reponse'),
('CRi','Rémission complète avec récupération hématologique incomplète','Catégorie distincte de CR ; préciser la classification et ne pas recompter CRh si cette catégorie est employée.','reponse'),
('MR4','Réponse moléculaire de profondeur quatre logs','BCR::ABL1 IS ≤ 0,01 %, sous réserve de contrôles analytiques adaptés.','cml-is'),
('MLL','Munich Leukemia Laboratory','Laboratoire européen cité pour le diagnostic des MDS/MPN avec neutrophilie ; source ne prouve pas une incidence suisse.','sources'),
('BCL-2','Protéine BCL-2','Protéine anti-apoptotique ciblée par le vénétoclax ; expression ne crée pas à elle seule une indication.','strategie'),
('J8','Huitième jour du cycle indiqué','Repère de calendrier, non acronyme médical ; ne pas confondre induction, consolidation et entretien.','fi'),
('J6','Sixième jour du cycle indiqué','Repère de calendrier dont le cycle doit être précisé.','fi'),
('J9','Neuvième jour du cycle indiqué','Repère de calendrier, notamment dans une procédure de contrôle ECG de Xospata.','fi'),
('QTcF','Intervalle QT corrigé selon Fridericia','Paramètre ECG utilisé dans la FI de quizartinib ; seuils d’initiation, suspension et reprise propres au produit.','interactions'),
('CPK','Créatine phosphokinase','Enzyme mesurée notamment dans la surveillance biologique sous giltéritinib.','fi'),
('MEBEKO','Commission des professions médicales','Autorité suisse dont les exigences de l’examen 2026 consultées renvoient au référentiel PROFILES.','profiles')]
for code in ['C92.'+str(n) for n in range(10)]+['C92.00','C92.01','C93.1']:
 terms.append((code,'Code CIM-10-GM '+code,'Code administratif, non acronyme ; voir le tableau des sous-catégories et les limites de la correspondance biologique.','classification'))
for term,full,definition,ref in terms:
 glossary+=f'\nif {term!r} not in G:\n    a({term!r}, [({term!r}, {full!r})], {full!r}, {"<p>"+definition+"</p>"!r}, {"c92-"+ref!r})\n'
(ROOT/'glossary/c92.py').write_text(glossary)

catalog=ROOT/'chapters.json';data=json.loads(catalog.read_text());row={'code':'C92','covers':['C92'],'title':'Leucémies myéloïdes','integrated':True,'owner':'S06','betta':True,'provisional_injection':True,'audit_status':'draft_pending_final_review','added':'2026-11-02'}
old=next((r for r in data if r.get('code')=='C92'),None)
if old:old.update(row)
else:data.append(row)
catalog.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')

config=json.loads((ROOT/'.medina/7-starter-codex.json').read_text());item=next(r for r in config['queue'] if r['code']=='C92');receipt=ROOT/item['production_receipt'];receipt.parent.mkdir(parents=True,exist_ok=True)
sourcepaths=[*sorted(target.glob('*.html')),ROOT/'glossary/c92.py',*sorted(assets.glob('*'))]
payload={'code':'C92','mission':item['missions']['PRODUCE'],'complete':True,'meaning':'Source production assembled in isolated authorized branch; not final review, project closure, human approval or main integration.','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'final_files':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sourcepaths if p.is_file()},'clinical_certification':False,'user_review_pending':True}
receipt.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'sections':len(SECTIONS),'windows':len(POP),'sciences':6,'originals':len(rows),'production_receipt':str(receipt.relative_to(ROOT)),'status':'assembled_not_validated'}))
