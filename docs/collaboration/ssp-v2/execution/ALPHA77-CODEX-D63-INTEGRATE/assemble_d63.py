#!/usr/bin/env python3
"""Assemblage local ; ne signe ni ne clôture une relecture."""
from pathlib import Path
import re,html,json,hashlib,shutil,subprocess
from bs4 import BeautifulSoup
from PIL import Image
import author_main,author_main2,author_pharma,author_exams,author_popups
from author_sciences import sciences
from common import ROOT,OUT,SECTIONS,POP,BYKEY
base=subprocess.check_output(['git','show','8a512893acbab9caa0dcfdd0e8682a44ea72fda6:chapters/D63/D63_a.html'],cwd=ROOT,text=True)
header=base[:base.index('<section class="ilot"')]
header=re.sub(r'<span class="status">.*?</span>','<span class="status">Adulte, avec limites pédiatriques et grossesse · sources suisses puis européennes et KDIGO 2026 · état au 02.11.2026 · auto-relecture pédagogique distincte d’une validation médicale humaine</span>',header,flags=re.S)
toc='<nav class="toc ui"><b>Plan monographique</b><ol>'
for i in range(15):
 title=BeautifulSoup(SECTIONS[str(i)],'html.parser').h2.get_text(' ',strip=True)
 title=re.sub(r'^'+str(i)+r'\s*','',title)
 toc+=f'<li><a href="#d63-{i}">{html.escape(title)}</a></li>'
toc+='</ol></nav>'
header=re.sub(r'<nav class="toc ui">.*?</nav>',toc,header,flags=re.S)
header=header.replace('data-k="d63-sources"','data-k="d63-sources-guides"').replace('data-k="d63-nosologie"','data-k="d63-cim"')
SECTIONS['6']=SECTIONS['6'].replace('id="d63-6"','id="d63-6" data-semiology-clinical="D63"',1)
pager='<div class="pager ui"><button class="prev">← Partie précédente</button><span></span><button class="next">Partie suivante →</button></div>'
index='<details id="d63-reference-index"><summary>Ouvrir une explication ou une synthèse</summary><ul>'+''.join(f'<li><button class="w" data-k="{ident}">{html.escape(title)}</button></li>' for ident,(title,body) in POP.items())+'</ul></details>'
end='<button class="pareto-btn ui" data-k="pareto-d63-cours">▲ Loi de Pareto — Monographie</button>'+index+'<div class="src"><p>Sources attribuées dans les sections et fiches. <button class="w" data-k="d63-sources-guides">Dates, populations et limites</button>. Les cas et calculs pédagogiques sont fictifs.</p></div>'
files={
'D63_a.html':header+'\n'.join(SECTIONS[str(i)] for i in range(7))+'\n',
'D63_b.html':'\n'.join(SECTIONS[str(i)] for i in range(7,15))+end+'</div>'+pager+'</div>\n',
'D63_c.html':'<div class="panel" id="pE" hidden><div class="chap-body">'+'\n'.join(SECTIONS[f'e-{i}'] for i in range(1,6))+'<button class="pareto-btn ui" data-k="pareto-d63-examens">▲ Loi de Pareto — Examens</button></div>'+pager+'</div>'+sciences()+'\n',
'D63_d.html':'<div class="panel" id="pP" hidden><div class="chap-body">'+'\n'.join(SECTIONS[f'p-{i}'] for i in range(1,6))+'<button class="pareto-btn ui" data-k="pareto-d63-pharma">▲ Loi de Pareto — Pharmacologie</button></div>'+pager+'</div></div></template>\n'}
items=[f'<template data-pop="{ident}" data-title="{html.escape(title,quote=True)}">{body}</template>\n' for ident,(title,body) in POP.items()]
cut=(len(items)+1)//2;files['D63_pop1.html']=''.join(items[:cut]);files['D63_pop2.html']=''.join(items[cut:])

def typography(body):
 parts=re.split(r'(<[^>]+>)',body)
 for i in range(0,len(parts),2):
  t=parts[i]
  terms=['PROFILES','SSP','OMS','KDIGO','ECCO','ESMO','ESC','TSAT','CHr','MICI','MRC','ESA','FI','SSMIG','STAT3','B12','Eprex','IRONMAN','COVID','OAMal','OFS','CIM-10','GM','CRP','HD','G3','G4','G5','D63','Liste','IV','HIF']
  t=re.sub(r'(?<=[a-zàâéèêëîïôöùûüç])(?=(?:'+ '|'.join(terms)+r'))',' ',t)
  t=t.replace('ETTSAT','ET TSAT').replace('protéineC','protéine C').replace('etP','et P').replace('G5D','G5 avec dialyse').replace('UNE perfusion','une seule perfusion').replace('aprèsfer','après fer')
  # Évite que le moteur prenne la conjonction logique pour une abréviation médicale homonyme.
  t=re.sub(r'\bET\b','et',t);t=re.sub(r'\bOU\b','ou',t)
  # Liste fermée de mots/unités ; aucune séparation générale de symboles scientifiques.
  t=re.sub(r'\b(de|du|en|à|les|sous|entre|sur|dès|après|avant|que|édition|figure|puis|dans|repère|Repère|barre)(?=\d)',r'\1 ',t)
  t=re.sub(r'\b(taux|confiance|zone|stade|moins|dépasse|atteint|Enfant|enfant|adulte|supérieur|inférieur|tous|plus|vers|pendant|article|articles)(?=\d)',r'\1 ',t)
  t=re.sub(r'(?<=\d)(?=(?:et|à|an)\b)',' ',t)
  t=re.sub(r'(?<=\d)(?=%)',' ',t)
  t=re.sub(r'(?<=\d)(?=(?:ans|mois|jours|heures|patients|adultes|enfants|points|mai|octobre|cellules|mg|kg|mL|min|minutes|secondes|g/L|g/dL|µg/L|µm|UI/kg|pg)\b)',' ',t)
  t=re.sub(r'\b(CC BY|PROFILES|SSP|OMS|KDIGO|ECCO|ESMO|ESC|MEBEKO|CIM-10-GM|Hb|ferritine|Ferritine|TSAT|CHr|CRP|GM)(?=\d)',r'\1 ',t)
  t=re.sub(r'(?<=[a-zàâéèêëîïôöùûüç])(?=20(?:1[0-9]|2[0-9])\b)',' ',t)
  t=re.sub(r'(?<=[A-Za-zÀ-ÿ0-9])(?=[≤≥])',' ',t);t=re.sub(r'([≤≥])(?=\d)',r'\1 ',t)
  for before,after in {'laMICI':'la MICI','lesMICI':'les MICI','uneMICI':'une MICI','laMRC':'la MRC','uneMRC':'une MRC','laTSAT':'la TSAT','uneHb':'une Hb','l’Hb':'l’Hb','Enoncologie':'En oncologie','sousépoétine':'sous époétine','sousESA':'sous ESA','unESA':'un ESA','lesESA':'les ESA','niESA':'ni ESA','desESA':'des ESA','enMRC':'en MRC','enMICI':'en MICI','l’ESA':'l’ESA','parESA':'par ESA','selonKDIGO':'selon KDIGO','selonECCO':'selon ECCO','selonESMO':'selon ESMO','dansECCO':'dans ECCO','avecHb':'avec Hb','etHb':'et Hb','etTSAT':'et TSAT','etCRP':'et CRP','saCRP':'sa CRP','pourHb':'pour Hb','<b>':'<b>'}.items():t=t.replace(before,after)
  t=t.replace('du18mai','du 18 mai').replace('d’établirD63','d’établir D63')
  for a,b in {'enfolate':'en folate','sousferoral':'sous fer oral','feroral':'fer oral','noncardiaque':'sans maladie cardiaque','Horsdialyse':'Hors dialyse','horsdialyse':'hors dialyse','aprèsérythropoïétine':'après érythropoïétine','sousérythropoïétine':'sous érythropoïétine','sousinflammation':'sous inflammation','souschimiothérapie':'sous chimiothérapie','sousfer':'sous fer','statement5.2':'énoncé 5.2'}.items():t=t.replace(a,b)
  for a,b in {'nondialysée':'non dialysée','nondialysé':'non dialysé','Enhémodialyse':'En hémodialyse','Horshémodialyse':'Hors hémodialyse','Enmaladie':'En maladie','Encas':'En cas','Pourferro':'Pour ferro','parmois':'par mois','sousinhibiteur':'sous inhibiteur','àpartir':'à partir','auplus':'au plus','71a–d OAMal':'71a à 71d de l’OAMal','HIF-prolylhydroxylase':'des prolyl-hydroxylases de HIF'}.items():t=t.replace(a,b)
  parts[i]=t
 return ''.join(parts)

def scope(body):
 mapping={'Hb':'hb','VGM':'vgm','TSAT':'tsat','CHr':'chr','CRP':'crp','ESA':'esa','EPO':'esa','MRC':'mrc','MICI':'mici','HIF-PHI':'hif-phi','IL-6':'il6-stat3','STAT3':'il6-stat3','PROFILES':'profiles','MEBEKO':'profiles','KDIGO':'sources-guides','ECCO':'sources-guides','ESMO':'sources-guides','D63.0':'cim','D63.8':'cim','D63.1':'cim'}
 regex=re.compile(r'(?<![A-Za-zÀ-ÿ0-9])('+ '|'.join(re.escape(k) for k in sorted(mapping,key=len,reverse=True))+r')(?![A-Za-zÀ-ÿ0-9])')
 chunks=re.split(r'(<[^>]+>)',body);protected=[]
 for i,t in enumerate(chunks):
  if i%2:
   m=re.match(r'</?(a|button|svg|script|style)\b',t,re.I)
   if m:
    if t.startswith('</'):
     if protected:protected.pop()
    else:protected.append(m.group(1))
  elif not protected:chunks[i]=regex.sub(lambda m:f'<button class="w" data-k="d63-{mapping[m.group(1)]}">{m.group(1)}</button>',t)
 return ''.join(chunks)
for name,body in files.items():
 body=re.sub(r'<(?=\s*[=\d])','&lt;',body)
 (ROOT/'chapters/D63'/name).write_text(scope(typography(body)))

assets=ROOT/'assets/img/d63/alpha/codex';assets.mkdir(parents=True,exist_ok=True);rows=[]
for name,src,source,credit in [
 ('normal-marrow-openstax2016.jpg',Path('/workspace/Medina-hematologie-C95/assets/img/c95/alpha/codex/normal-marrow-openstax2016.jpg'),'NORMAL-IMAGE','OpenStax, Anatomy and Physiology édition 8.25 du 18 mai 2016, figure 2205 Bone Marrow'),
 ('normal-peripheral-blood.jpg',ROOT/'assets/img/d50/alpha/claude/normal_peripheral_blood_smear_giemsa.jpg','BLOOD-IMAGE','Степанюк Ярослав et Борис Максим, Wikimedia Commons, Кров людини')]:
 dst=assets/name;shutil.copyfile(src,dst)
 with Image.open(dst) as im:width,height=im.size
 rows.append({'file':str(dst.relative_to(ROOT)),'sha256':hashlib.sha256(dst.read_bytes()).hexdigest(),'width':width,'height':height,'source_url':BYKEY[source]['url'],'source_ledger_id':BYKEY[source]['id'],'credit':credit,'license':'CC BY 4.0','license_url':'https://creativecommons.org/licenses/by/4.0/','pixel_modification':False,'annotations':'Four French location-based interpretation markers in figure caption; no synthetic anatomy','original_seen':True,'rendered_final_review_reference':'review-package/self-review.json, recorded only after actual inspection'})
(assets/'provenance.json').write_text(json.dumps({'images':rows,'source_review_date':'2026-11-02','clinical_certification':False},ensure_ascii=False,indent=2)+'\n')
(assets/'ATTRIBUTION.md').write_text('# Originaux D63\n\n'+ '\n\n'.join(f'**{r["file"].split("/")[-1]}** — {r["credit"]}. [Provenance]({r["source_url"]}). [CC BY 4.0]({r["license_url"]}). Pixels inchangés ; quatre repères français de lecture dans la légende. SHA256 `{r["sha256"]}`.' for r in rows)+'\n\nL’image OpenStax relève de la licence du fichier Commons de 2016, pas du manuel actuel. Le frottis était déjà conservé dans D50 avec sa preuve de droits ; sa réutilisation est explicitement attribuée, sans modification de D50. Aucune image normale n’est présentée comme diagnostic d’anémie inflammatoire.\n')
# Corrige seulement les renvois locaux de ce glossaire, sans modifier un glossaire partagé.
glossary=ROOT/'glossary/d63.py';text=subprocess.check_output(['git','show','8a512893acbab9caa0dcfdd0e8682a44ea72fda6:glossary/d63.py'],cwd=ROOT,text=True).replace('d63-nosologie','d63-cim').replace('d63-sources','d63-sources-guides')
for term,full,definition,ref in [
 ('CHr','Contenu en hémoglobine des réticulocytes','Mesure du fer récemment incorporé dans les réticulocytes ; méthode et population accompagnent le seuil.','chr'),
 ('HIF','Facteur induit par l’hypoxie','Voie de réponse cellulaire à l’hypoxie ; un mécanisme ne prouve pas une indication thérapeutique suisse.','hif-phi'),
 ('HIF-PHI','Inhibiteur des prolyl-hydroxylases de HIF','Classe discutée par KDIGO dans l’anémie rénale ; vérifier le produit exact et son autorisation, sans association à un ESA.','hif-phi'),
 ('SSMIG','Société suisse de médecine interne générale','Société à l’origine de la recommandation suisse hospitalière smarter medicine citée.','transfusion'),
 ('COVID','Maladie à coronavirus','Dans IRONMAN, l’analyse liée à la période de pandémie est distincte du résultat principal.','sources-guides'),
 ('HD','Hémodialyse','Modalité de dialyse à distinguer de la dialyse péritonéale pour les critères KDIGO et les doses du produit.','mrc'),
 ('OAMal','Ordonnance sur l’assurance-maladie','Les articles 71a à 71d concernent des conditions particulières de prise en charge, sans garantie individuelle.','sources-guides'),
 ('MEBEKO','Commission des professions médicales','Autorité suisse dont les exigences consultées pour l’examen 2026 renvoient à PROFILES 2017.','profiles')]:
 text+=f'\nif {term!r} not in G:\n    a({term!r}, [({term!r}, {full!r})], {full!r}, {"<p>"+definition+"</p>"!r}, {"d63-"+ref!r})\n'
glossary.write_text(text)
print(json.dumps({'sections':len(SECTIONS),'windows':len(POP),'sciences':6,'originals':len(rows),'status':'assembled_not_validated'}))
