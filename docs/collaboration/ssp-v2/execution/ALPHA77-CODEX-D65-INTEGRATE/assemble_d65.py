"""Assembler D65 dans le périmètre réservé ; aucune clôture ni relecture automatique."""
from pathlib import Path
import json,hashlib,datetime,html,re,shutil
from bs4 import BeautifulSoup
from PIL import Image
import author_main,author_main2,author_exams,author_pharma,author_popups
from author_sciences import sciences
from common import ROOT,OUT,SECTIONS,POP,BYKEY,IMAGES
assert json.loads((OUT/'research-entry.json').read_text())['passed']
target=ROOT/'chapters/D65';target.mkdir(exist_ok=True)
header='''<template id="ch-D65"><div class="chap"><div class="chap-head"><div class="code">D65 — Coagulation intravasculaire disséminée [syndrome de défibrination] · CIM-10-GM2024 · Sang et organes hématopoïétiques</div><h1>Coagulation intravasculaire disséminée : relier cause, consommation et organes</h1><span class="status">Adulte ; contextes septique, traumatique, obstétrical et hématologique distingués · Sources au02.11.2026 · Auto-relecture pédagogique distincte d’une validation médicale humaine</span></div><div class="tabs ui" role="tablist"><button role="tab" aria-controls="pA" data-p="pA" aria-selected="true">⚕ Pathologie et prise en charge</button><button role="tab" aria-controls="pE" data-p="pE" aria-selected="false">🔬 Examens complémentaires</button><button role="tab" aria-controls="pS" data-p="pS" aria-selected="false">⚛ Sciences fondamentales spécialisées</button><button role="tab" aria-controls="pP" data-p="pP" aria-selected="false">💊 Pharmacologie</button></div><div class="panel" id="pA">'''
toc='<nav class="toc ui"><b>Plan monographique</b><ol>'
for i in range(1,15):
 t=BeautifulSoup(SECTIONS[str(i)],'html.parser').h2.get_text(' ',strip=True);t=re.sub(r'^'+str(i)+r'\s*','',t);toc+=f'<li><a href="#d65-{i}">{html.escape(t)}</a></li>'
toc+='</ol></nav><div class="chap-body">';SECTIONS['6']=SECTIONS['6'].replace('id="d65-6"','id="d65-6" data-semiology-clinical="D65"',1)
pager='<div class="pager ui"><button class="prev">← Partie précédente</button><span></span><button class="next">Partie suivante →</button></div>'
index='<details id="d65-reference-index"><summary>Ouvrir une explication ou une synthèse</summary><ul>'+''.join(f'<li><button class="w" data-k="{k}">{html.escape(t)}</button></li>' for k,(t,b) in POP.items())+'</ul></details>'
end='<button class="pareto-btn ui" data-k="pareto-d65-cours">▲ Loi de Pareto — Monographie</button>'+index+'<div class="src"><p>Cas pédagogiques fictifs. <button class="w" data-k="d65-sources">Sources, dates et limites</button> ; <button class="w" data-k="d65-profiles">cadre de l’examen fédéral</button>.</p></div>'
files={'D65_a.html':header+toc+'\n'.join(SECTIONS[str(i)] for i in range(1,8)),
'D65_b.html':'\n'.join(SECTIONS[str(i)] for i in range(8,15))+end+'</div>'+pager+'</div>',
'D65_c.html':'<div class="panel" id="pE" hidden><div class="chap-body">'+'\n'.join(SECTIONS['e-'+str(i)] for i in range(1,4))+'<button class="pareto-btn ui" data-k="pareto-d65-examens">▲ Loi de Pareto — Examens</button></div>'+pager+'</div>'+sciences(),
'D65_d.html':'<div class="panel" id="pP" hidden><div class="chap-body">'+'\n'.join(SECTIONS['p-'+str(i)] for i in range(1,7))+'<button class="pareto-btn ui" data-k="pareto-d65-pharma">▲ Loi de Pareto — Pharmacologie</button></div>'+pager+'</div></div></template>'}
items=[f'<template data-pop="{k}" data-title="{html.escape(t,quote=True)}">{b}</template>' for k,(t,b) in POP.items()];half=(len(items)+1)//2;files['D65_pop1.html']='\n'.join(items[:half]);files['D65_pop2.html']='\n'.join(items[half:])
mapping={'CIVD': 'classification', 'ISTH': 'sources', 'SIC': 'sic', 'SOFA': 'sofa', 'PT': 'pt-inr', 'INR': 'pt-inr', 'aPTT': 'pt-inr', 'TXA': 'txa', 'HNF': 'heparine', 'HBPM': 'heparine', 'TIH': 'tih', 'ATIII': 'antithrombine', 'TFPI': 'tfpi', 'NETs': 'net', 'APL': 'apl', 'PTT': 'differentiel', 'FEU': 'ddimeres', 'DDU': 'ddimeres', 'VTE': 'anticoagulation', 'TACO': 'taco-trali', 'TRALI': 'taco-trali', 'FI': 'fi', 'OFS': 'classification', 'SSC': 'sources', 'ESICM': 'sources', 'SCCM': 'sources', 'PROFILES': 'profiles', 'MEBEKO': 'profiles', 'IV': 'fi', 'UI': 'fi'}
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
   t=t.replace('PROFILES2','PROFILES 2').replace('ISBN978','ISBN 978').replace('BY4.0','BY 4.0').replace('CCBY','CC BY')
   t=re.sub(r'\b(PT|INR|TXA|CIVD|SSP|DOI)(?=\d)',r'\1 ',t)
   t=re.sub(r'(?<=[a-zà-ÿ])(?=[A-ZÀ-ÖØ-Þ0-9])',' ',t)
   t=re.sub(r'(?<!S)(?<=\d)(?=[A-Za-zÀ-ÿ])',' ',t)
   t=t.replace('S2 k','S2k')
   t=re.sub(r'\b(PT|INR|TXA|CIVD|SSP|DOI)(?=\d)',r'\1 ',t)
   t=re.sub(r'(?<=[A-Z])(?=20\d\d\b)',' ',t)
   t=re.sub(r'\s*([×÷=])\s*',r' \1 ',t).replace('À1','À 1')
   for original,token in preserved.items():t=t.replace(token,original)
   t=re.sub(r'(?<!\d)([:;!?])(?=\S)',r'\1 ',t)
   t=re.sub(r'(?<=[A-Za-zÀ-ÿ]),(?=\S)',', ',t)
   t=re.sub(r',(?=[A-Za-zÀ-ÿ])',', ',t)
   parts[i]=pattern.sub(lambda m:f'<button class="w" data-k="d65-{mapping[m.group(1)]}">{m.group(1)}</button>',t) if not protect else t
 return ''.join(parts)
for name,body in files.items():
 result=transform(body)
 assert not re.search(r'\b(?:m|d)\s+L\b',result),name
 (target/name).write_text(result+'\n')
assets=ROOT/'assets/img/d65/alpha/codex';assets.mkdir(parents=True,exist_ok=True);rows=[]
for k,x in IMAGES.items():
 p=assets/x['file'];shutil.copyfile(Path(x['cache']),p)
 with Image.open(p) as im:width,height=im.size
 rows.append({'file':str(p.relative_to(ROOT)),'title':x['title'],'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'width':width,'height':height,'source_url':BYKEY[x['source']]['url'],'source_ledger_id':BYKEY[x['source']]['id'],'credit':x['credit'],'license':x['license'],'license_url':x['license_url'],'pixel_modification':False,'annotations':'Quatre repères français dans le bloc de légende adjacent à chaque image ; statut clinique individuel non établi.','original_seen':True,'clinical_certification':False})
(assets/'provenance.json').write_text(json.dumps({'images':rows,'source_review_date':'2026-11-02','review_mode':'self_review, aucune validation médicale humaine'},ensure_ascii=False,indent=2)+'\n')
(assets/'ATTRIBUTION.md').write_text('# Originaux D65\n\n'+'\n\n'.join(f'**{x["file"].split("/")[-1]}** — {x["credit"]}. [Provenance]({x["source_url"]}). [{x["license"]}]({x["license_url"]}). Pixels intacts, quatre repères français dans le bloc adjacent. SHA256 `{x["sha256"]}`.' for x in rows)+'\n\nDeux originaux du normal : microscopie électronique Wellcome et frottis sanguin. Aucune image ne prouve une CIVD ni ne mesure une concentration sanguine.\n')
terms=[('CIVD', 'Coagulation intravasculaire disséminée', 'Syndrome acquis secondaire, avec activation diffuse, fibrinolyse dérégulée et atteinte endothéliale.', 'classification'), ('ISTH', 'International Society on Thrombosis and Haemostasis', 'Société internationale ; définition et score2025 attribués dans le cours.', 'sources'), ('SIC', 'Coagulopathie induite par le sepsis', 'Sepsis-induced coagulopathy ; total et condition plaquettes+INR nécessaires.', 'sic'), ('SOFA', 'Sequential Organ Failure Assessment', 'Évaluation des organes ; quatre domaines retenus pour la composante SIC.', 'sofa'), ('PT', 'Temps de prothrombine', 'Le score manifeste utilise son allongement en secondes.', 'pt-inr'), ('INR', 'International Normalized Ratio', 'Rapport normalisé ; ne remplace pas directement un temps en secondes.', 'pt-inr'), ('aPTT', 'Temps de thromboplastine partielle activée', 'Examen complémentaire, hors score ISTH manifeste présenté.', 'pt-inr'), ('HNF', 'Héparine non fractionnée', 'Anticoagulant aux indications et restrictions propres.', 'heparine'), ('HBPM', 'Héparine de bas poids moléculaire', 'Classe distincte du produit HNF détaillé dans le cours.', 'heparine'), ('TIH', 'Thrombopénie induite par l’héparine', 'Complication nécessitant une démarche propre.', 'tih'), ('TXA', 'Acide tranexamique', 'Antifibrinolytique ; exception spécialisée dans une minorité de CIVD.', 'txa'), ('TFPI', 'Inhibiteur de la voie du facteur tissulaire', 'Frein physiologique de la coagulation.', 'tfpi'), ('NETs', 'Réseaux extracellulaires des neutrophiles', 'Structures impliquées dans les interactions immunité-coagulation.', 'net'), ('FEU', 'Fibrinogen equivalent units', 'Unités de D-dimères à garder cohérentes avec la méthode.', 'ddimeres'), ('DDU', 'D-dimer units', 'Expression de D-dimères distincte des FEU.', 'ddimeres'), ('APL', 'Leucémie aiguë promyélocytaire', 'Acute promyelocytic leukemia ; contexte hématologique spécifique.', 'apl'), ('ATIII', 'Antithrombine III', 'Protéine anticoagulante, indication de concentré non déduite de sa seule baisse.', 'antithrombine'), ('TACO', 'Surcharge circulatoire associée à la transfusion', 'Mécanisme distinct du TRALI.', 'taco-trali'), ('TRALI', 'Atteinte pulmonaire aiguë associée à la transfusion', 'Classification et enquête contextuelles.', 'taco-trali'), ('MEBEKO', 'Commission des professions médicales', 'Cadre suisse de formation et d’examen.', 'profiles'), ('SSC', 'Abréviation à contextualiser', 'Comité scientifique de l’ISTH ou Surviving Sepsis Campaign selon le titre de source.', 'sources'), ('ESICM', 'European Society of Intensive Care Medicine', 'Société européenne partenaire des recommandations sepsis2026.', 'sources'), ('SCCM', 'Society of Critical Care Medicine', 'Partenaire des recommandations internationales conjointes sepsis2026.', 'sources'), ('OAMal', 'Ordonnance sur l’assurance-maladie', 'Cadre suisse, sans garantie individuelle de remboursement.', 'sources'), ('D65', 'Code CIM-10-GM D65', 'Classification et limites expliquées dans la leçon.', 'classification'), ('D65.0', 'Code CIM-10-GM D65.0', 'Classification et limites expliquées dans la leçon.', 'classification'), ('D65.1', 'Code CIM-10-GM D65.1', 'Classification et limites expliquées dans la leçon.', 'classification'), ('D65.2', 'Code CIM-10-GM D65.2', 'Classification et limites expliquées dans la leçon.', 'classification'), ('D65.9', 'Code CIM-10-GM D65.9', 'Classification et limites expliquées dans la leçon.', 'classification'), ('P60', 'Code CIM-10-GM P60', 'Classification et limites expliquées dans la leçon.', 'classification')]
terms += [('XIII', 'Treize, facteur de coagulation', 'Le facteur XIII activé stabilise la fibrine.', 'coagulation'), ('CSV', 'Comma-separated values', 'Format de données tabulaires du référentiel OFS cité.', 'sources'), ('XML', 'Extensible Markup Language', 'Format structuré de texte ou de classification ; ne constitue pas une recommandation clinique.', 'sources'), ('FPV', 'Forfaitpauschalenvereinbarung', 'Cadre allemand de facturation mentionné dans la source de classification, non transposé à la Suisse.', 'classification'), ('CAHT', 'Groupe CAHT', 'Société ayant rendu disponible une copie publique de la communication primaire ISTH2025 ; accès distinct de l’auteur du texte.', 'sources'), ('SHA', 'Empreinte cryptographique', 'Élément de provenance des fichiers, sans valeur de certification médicale.', 'sources'), ('DOI', 'Digital Object Identifier', 'Identifiant bibliographique stable d’une publication.', 'sources'), ('APC', 'Protéine C activée', 'Protéine physiologique ; ancien médicament recombinant retiré, pas traitement actuel proposé.', 'coagulation'), ('AT', 'Antithrombine', 'Frein physiologique de la coagulation.', 'antithrombine'), ('TM', 'Thrombomoduline', 'Composant de régulation endothéliale ; mention de recherche, sans routine thérapeutique suisse déduite.', 'coagulation'), ('CI', 'Contre-indication', 'Situation où le produit ne doit pas être utilisé selon sa fiche.', 'fi'), ('PPH', 'Hémorragie du post-partum', 'Postpartum haemorrhage ; contexte distinct d’une CIVD générale.', 'causes'), ('ATO', 'Trioxyde d’arsenic', 'Abréviation apparaissant dans le périmètre de la source APL antérieure ; aucune posologie proposée dans ce cours.', 'apl'), ('DGGG', 'Société allemande de gynécologie et d’obstétrique', 'Partenaire de la directive péripartale citée.', 'sources'), ('OEGGG', 'Société autrichienne de gynécologie et d’obstétrique', 'Partenaire de la directive péripartale citée.', 'sources'), ('SGGG', 'Société suisse de gynécologie et d’obstétrique', 'Partenaire suisse de la directive péripartale citée.', 'sources'), ('RAI', 'Recherche d’anticorps irréguliers', 'Examen immunohématologique intégré à la sécurité transfusionnelle selon procédure locale.', 'transfusion'), ('O2', 'Oxygène', 'Notation moléculaire dans une référence, sans dose d’oxygène déduite.', 'sources'), ('01-A01', 'Fragment d’identifiant de document', 'Référence administrative Swissmedic, pas paramètre clinique.', 'sources'), ('NC', 'Non commercial', 'Mention de licence d’une source textuelle ; droits des images vérifiés séparément.', 'sources'), ('SEM', 'Microscopie électronique à balayage', 'Scanning electron microscopy ; technique de l’original Wellcome.', 'sources')]
g='from cardio_1 import a, G\n# Définitions D65 conditionnelles ; aucun terme global existant écrasé.\n'
for t,full,body,ref in terms:g+=f'\nif {t!r} not in G:\n    a({t!r}, [({t!r}, {full!r})], {full!r}, {"<p>"+body+"</p>"!r}, {"d65-"+ref!r})\n'
(ROOT/'glossary/d65.py').write_text(g)
p=ROOT/'chapters.json';catalog=json.loads(p.read_text());row={'code':'D65','covers':['D65','D65.0','D65.1','D65.2','D65.9'],'title':'Coagulation intravasculaire disséminée [syndrome de défibrination]','integrated':True,'owner':'S06','betta':True,'provisional_injection':True,'audit_status':'draft_pending_final_review','added':'2026-11-02'}
old=next((x for x in catalog if x.get('code')=='D65'),None)
if old:old.update(row)
else:catalog.append(row)
p.write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+'\n')
config=json.loads((ROOT/'.medina/7-starter-codex.json').read_text());item=next(x for x in config['queue'] if x['code']=='D65');receipt=ROOT/item['production_receipt'];receipt.parent.mkdir(parents=True,exist_ok=True)
paths=[*sorted(target.glob('*.html')),ROOT/'glossary/d65.py',*sorted(assets.glob('*'))]
receipt.write_text(json.dumps({'code':'D65','mission':item['missions']['PRODUCE'],'complete':True,'meaning':'Sources assemblées dans branche réservée ; aucune clôture clinique, validation humaine ou intégration main.','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'final_files':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths if p.is_file()},'clinical_certification':False,'user_review_pending':True},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'sections':len(SECTIONS),'windows':len(POP),'sciences':6,'originals':len(rows),'status':'assembled_not_validated'}))
