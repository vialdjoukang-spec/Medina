"""Assembler D62 dans le périmètre réservé ; aucune clôture ni relecture automatique."""
from pathlib import Path
import json,hashlib,datetime,html,re,shutil
from bs4 import BeautifulSoup
from PIL import Image
import author_main,author_main2,author_exams,author_pharma,author_popups
from author_sciences import sciences
from common import ROOT,OUT,SECTIONS,POP,BYKEY,IMAGES
assert json.loads((OUT/'research-entry.json').read_text())['passed']
target=ROOT/'chapters/D62';target.mkdir(exist_ok=True)
header='''<template id="ch-D62"><div class="chap"><div class="chap-head"><div class="code">D62 — Anémie posthémorragique aiguë · CIM-10-GM2024 · Sang et organes hématopoïétiques</div><h1>Après une perte de sang : reconnaître l’urgence et comprendre l’anémie</h1><span class="status">Adulte ; contextes traumatique, digestif, opératoire et obstétrical distingués · Sources au02.11.2026 · Auto-relecture pédagogique distincte d’une validation médicale humaine</span></div><div class="tabs ui" role="tablist"><button role="tab" aria-controls="pA" data-p="pA" aria-selected="true">⚕ Pathologie et prise en charge</button><button role="tab" aria-controls="pE" data-p="pE" aria-selected="false">🔬 Examens complémentaires</button><button role="tab" aria-controls="pS" data-p="pS" aria-selected="false">⚛ Sciences fondamentales spécialisées</button><button role="tab" aria-controls="pP" data-p="pP" aria-selected="false">💊 Pharmacologie</button></div><div class="panel" id="pA">'''
toc='<nav class="toc ui"><b>Plan monographique</b><ol>'
for i in range(1,15):
 t=BeautifulSoup(SECTIONS[str(i)],'html.parser').h2.get_text(' ',strip=True);t=re.sub(r'^'+str(i)+r'\s*','',t);toc+=f'<li><a href="#d62-{i}">{html.escape(t)}</a></li>'
toc+='</ol></nav><div class="chap-body">';SECTIONS['6']=SECTIONS['6'].replace('id="d62-6"','id="d62-6" data-semiology-clinical="D62"',1)
pager='<div class="pager ui"><button class="prev">← Partie précédente</button><span></span><button class="next">Partie suivante →</button></div>'
index='<details id="d62-reference-index"><summary>Ouvrir une explication ou une synthèse</summary><ul>'+''.join(f'<li><button class="w" data-k="{k}">{html.escape(t)}</button></li>' for k,(t,b) in POP.items())+'</ul></details>'
end='<button class="pareto-btn ui" data-k="pareto-d62-cours">▲ Loi de Pareto — Monographie</button>'+index+'<div class="src"><p>Cas pédagogiques fictifs. <button class="w" data-k="d62-sources">Sources, dates et limites</button> ; <button class="w" data-k="d62-profiles">cadre de l’examen fédéral</button>.</p></div>'
files={'D62_a.html':header+toc+'\n'.join(SECTIONS[str(i)] for i in range(1,8)),
'D62_b.html':'\n'.join(SECTIONS[str(i)] for i in range(8,15))+end+'</div>'+pager+'</div>',
'D62_c.html':'<div class="panel" id="pE" hidden><div class="chap-body">'+'\n'.join(SECTIONS['e-'+str(i)] for i in range(1,6))+'<button class="pareto-btn ui" data-k="pareto-d62-examens">▲ Loi de Pareto — Examens</button></div>'+pager+'</div>'+sciences(),
'D62_d.html':'<div class="panel" id="pP" hidden><div class="chap-body">'+'\n'.join(SECTIONS['p-'+str(i)] for i in range(1,7))+'<button class="pareto-btn ui" data-k="pareto-d62-pharma">▲ Loi de Pareto — Pharmacologie</button></div>'+pager+'</div></div></template>'}
items=[f'<template data-pop="{k}" data-title="{html.escape(t,quote=True)}">{b}</template>' for k,(t,b) in POP.items()];half=(len(items)+1)//2;files['D62_pop1.html']='\n'.join(items[:half]);files['D62_pop2.html']='\n'.join(items[half:])
mapping={'Hb':'concentration','VGM':'indices','MCV':'indices','MCH':'indices','MCHC':'indices','TXA':'txa','PCC':'pcc','RAI':'compatibilite','TACO':'taco-trali','TRALI':'taco-trali','FI':'fi','OMS':'sources','OFS':'classification','ESGE':'sources','SGGG':'sources','DGGG':'sources','OEGGG':'sources','PROFILES':'profiles','MEBEKO':'profiles','IV':'fi'}
pattern=re.compile(r'(?<![A-Za-zÀ-ÿ0-9_])('+'|'.join(map(re.escape,sorted(mapping,key=len,reverse=True)))+r')(?![A-Za-zÀ-ÿ0-9_])')
def transform(body):
 parts=re.split(r'(<[^>]+>)',body);protect=[]
 for i,t in enumerate(parts):
  if i%2:
   m=re.match(r'</?(a|button|svg|script|style)\b',t,re.I)
   if m:
    if t.startswith('</'):
     if protect:protect.pop()
    else:protect.append(m.group(1).lower())
  elif not any(x in protect for x in ['svg','script','style']):
   preserved={'mL':'MLUNITPLACEHOLDER','dL':'DLUNITPLACEHOLDER','NaCl':'NACLPLACEHOLDER','OpenStax':'OPENSTAXPLACEHOLDER','AmiKo':'AMIKOPLACEHOLDER'}
   for original,token in preserved.items():t=t.replace(original,token)
   t=t.replace('PROFILES2','PROFILES 2').replace('ISBN978','ISBN 978').replace('BY4.0','BY 4.0')
   t=re.sub(r'(?<=[a-zà-ÿ])(?=[A-ZÀ-ÖØ-Þ0-9])',' ',t)
   t=re.sub(r'(?<!S)(?<=\d)(?=[A-Za-zÀ-ÿ])',' ',t)
   t=t.replace('S2 k','S2k')
   t=re.sub(r'(?<=[A-Z])(?=20\d\d\b)',' ',t)
   t=re.sub(r'\s*([×÷=])\s*',r' \1 ',t).replace('À1','À 1')
   for original,token in preserved.items():t=t.replace(token,original)
   parts[i]=pattern.sub(lambda m:f'<button class="w" data-k="d62-{mapping[m.group(1)]}">{m.group(1)}</button>',t) if not protect else t
 return ''.join(parts)
for name,body in files.items():
 result=transform(body)
 assert not re.search(r'\b(?:m|d)\s+L\b',result),name
 (target/name).write_text(result+'\n')
assets=ROOT/'assets/img/d62/alpha/codex';assets.mkdir(parents=True,exist_ok=True);rows=[]
for k,x in IMAGES.items():
 p=assets/x['file'];shutil.copyfile(Path('/workspace/Medina-hematologie-D63/assets/img/d63/alpha/codex')/x['file'],p)
 with Image.open(p) as im:width,height=im.size
 rows.append({'file':str(p.relative_to(ROOT)),'title':x['title'],'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'width':width,'height':height,'source_url':BYKEY[x['source']]['url'],'source_ledger_id':BYKEY[x['source']]['id'],'credit':x['credit'],'license':x['license'],'license_url':x['license_url'],'pixel_modification':False,'annotations':'Quatre repères français dans chaque légende ; image du normal, pas diagnosticD62.','original_seen':True,'clinical_certification':False})
(assets/'provenance.json').write_text(json.dumps({'images':rows,'source_review_date':'2026-11-02','review_mode':'self_review, aucune validation médicale humaine'},ensure_ascii=False,indent=2)+'\n')
(assets/'ATTRIBUTION.md').write_text('# Originaux D62\n\n'+'\n\n'.join(f'**{x["file"].split("/")[-1]}** — {x["credit"]}. [Provenance]({x["source_url"]}). [{x["license"]}]({x["license_url"]}). Pixels intacts, quatre repères français dans la légende. SHA256 `{x["sha256"]}`.' for x in rows)+'\n\nImage OpenStax de2016, pas licence du manuel actuel. Aucune image ne mesure l’hémoglobine ni ne prouve une hémorragie.\n')
terms=[('TXA','Acide tranexamique','Antifibrinolytique dont indication, délai et contre-indications dépendent du contexte.','txa'),('PCC','Concentré de complexe prothrombinique','En anglais prothrombin complex concentrate ; apport de facteurs précis, non de globules rouges.','pcc'),('RAI','Recherche d’anticorps irréguliers','Examen immunohématologique intégré à la sécurité transfusionnelle selon procédure locale.','compatibilite'),('TACO','Surcharge circulatoire associée à la transfusion','En anglais transfusion associated circulatory overload ; mécanisme de surcharge à distinguer duTRALI.','taco-trali'),('TRALI','Atteinte pulmonaire aiguë associée à la transfusion','En anglais transfusion related acute lung injury ; définition datée et diagnostic contextualisé.','taco-trali'),('ESGE','Société européenne d’endoscopie gastro-intestinale','European Society of Gastrointestinal Endoscopy ; directive2026 utilisée pour le saignement haut non variqueux.','sources'),('SGGG','Société suisse de gynécologie et d’obstétrique','Participe à la directive péripartale2022 avec les sociétés allemande et autrichienne.','sources'),('DGGG','Société allemande de gynécologie et d’obstétrique','Partenaire de la directive péripartale2022.','sources'),('OEGGG','Société autrichienne de gynécologie et d’obstétrique','Partenaire de la directive péripartale2022.','sources'),('MCV','Volume globulaire moyen','Mean corpuscular volume ; taille moyenne des hématies.','indices'),('MCH','Teneur corpusculaire moyenne en hémoglobine','Mean corpuscular hemoglobin ; quantité moyenne par hématie.','indices'),('MCHC','Concentration corpusculaire moyenne en hémoglobine','Mean corpuscular hemoglobin concentration ; rapportée au volume érythrocytaire.','indices'),('ATIII','AntithrombineIII','Protéine de régulation de la coagulation ; absence dansOctaplex et restrictions spécifiques de saFI.','pcc'),('MEBEKO','Commission des professions médicales','Autorité suisse ; exigences de l’examen2026 distinguées dePROFILES2.','profiles')]
terms += [('SMPR','Service de médecine de premier recours','ServiceHUG auteur de la stratégie sur les anémies.','sources'),('S2k','Niveau S2k de directive AWMF','Directive fondée sur un consensus structuré ; ne se confond pas avec un niveauS3.','sources'),('CI','Contre-indication','Situation où le produit ne doit pas être utilisé selon saFI.','fi'),('PPH','Hémorragie du post-partum','Postpartum haemorrhage dans les textes internationaux.','postpartum'),('O2','Oxygène','Notation moléculaire ; quantité de transporteurs et saturation ne sont pas identiques.','oxygene'),('01-A01','Fragment d’identifiant documentaire','Partie de la référence administrativeSwissmedic, pas paramètre clinique.','sources'),('NC','Non commercial','Clause de licence d’une source textuelle ; les photographies reprises ont leurs droits propres.','sources'),('ISBN','Numéro international normalisé du livre','Identifiant bibliographique, non acronyme clinique.','sources'),('OAMal','Ordonnance sur l’assurance-maladie','Cadre suisse ; aucune garantie individuelle de remboursement donnée par le cours.','sources')]
for code in ['D62','D50.0','P61.3']:terms.append((code,'Code CIM-10-GM '+code,'Code de classification, pas acronyme clinique ; portée et exclusions expliquées dans la leçon.','classification'))
g='from cardio_1 import a, G\n# Définitions D62 conditionnelles ; aucun terme global existant écrasé.\n'
for t,full,body,ref in terms:g+=f'\nif {t!r} not in G:\n    a({t!r}, [({t!r}, {full!r})], {full!r}, {"<p>"+body+"</p>"!r}, {"d62-"+ref!r})\n'
(ROOT/'glossary/d62.py').write_text(g)
p=ROOT/'chapters.json';catalog=json.loads(p.read_text());row={'code':'D62','covers':['D62'],'title':'Anémie posthémorragique aiguë','integrated':True,'owner':'S06','betta':True,'provisional_injection':True,'audit_status':'draft_pending_final_review','added':'2026-11-02'}
old=next((x for x in catalog if x.get('code')=='D62'),None)
if old:old.update(row)
else:catalog.append(row)
p.write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+'\n')
config=json.loads((ROOT/'.medina/7-starter-codex.json').read_text());item=next(x for x in config['queue'] if x['code']=='D62');receipt=ROOT/item['production_receipt'];receipt.parent.mkdir(parents=True,exist_ok=True)
paths=[*sorted(target.glob('*.html')),ROOT/'glossary/d62.py',*sorted(assets.glob('*'))]
receipt.write_text(json.dumps({'code':'D62','mission':item['missions']['PRODUCE'],'complete':True,'meaning':'Sources assemblées dans branche réservée ; aucune clôture clinique, validation humaine ou intégration main.','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'final_files':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths if p.is_file()},'clinical_certification':False,'user_review_pending':True},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'sections':len(SECTIONS),'windows':len(POP),'sciences':6,'originals':len(rows),'status':'assembled_not_validated'}))
