from pathlib import Path
import json,hashlib,datetime,shutil,subprocess
ROOT=Path(__file__).resolve().parents[5];OUT=Path(__file__).resolve().parent
CACHE=Path('/tmp/medina-n04-source-cache');NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
LEGACY='livraisons/Livraison Claude/N-07-Néphrologie/travail/CYCLE_03_N04/preuves/dossier_sources.json'
old=json.loads((ROOT/LEGACY).read_text());sources=[]
PARA=json.loads((OUT/'paraphrases.json').read_text())
for x in json.loads((OUT/'passages-lus.json').read_text())['passages']:
    sources.append(dict(x,id=x['id'],publisher=x['editeur'],read_at=x['date_consultation'],section=x['section_page'],limits=x['limites'],reading_scope='current author: selected passage actually read'))

def current(key,needle,length,section,population,limits,after=None,ident=None):
    text=(CACHE/(key+'.txt')).read_text();offset=text.find(needle,text.find(after) if after else 0);assert offset>=0,(key,needle)
    if key.startswith('FI_'):
        ref=old['swissmedic_fi'][key[3:]];url=ref['url'];publisher='Information professionnelle suisse du produit, diffusée via AmiKo/oddb';title=ref['product'];version=ref['update']
    else:
        ref=old['sources'][key];url=ref['url'];publisher=ref['organization'];title=ref['title'];version=ref['version_date']
    row={'id':ident or 'R-'+key,'url':url,'publisher':publisher,'title':title,'version':version,'read_at':'2026-11-02','section':section,'passage':PARA[ident or 'R-'+key], 'passage_format':'paraphrase; exact excerpt remains in external source cache', 'working_excerpt_sha256':hashlib.sha256(text[offset:offset+length].encode()).hexdigest(),'population':population,'limits':limits,'reading_scope':'current author: selected passage actually displayed and read; not complete-document certification','offset_char':offset,'raw_sha256':hashlib.sha256((CACHE/(key+'.raw')).read_bytes()).hexdigest(),'text_sha256':hashlib.sha256(text.encode()).hexdigest()}
    if key.startswith('FI_'):row.update(gtin=ref['gtin'],authorization=ref['auth'],product=ref['product'])
    sources.append(row)

current('OGN_FSGS','Genetische Abklärung',6200,'Exploration génétique','FSGS adulte et formes congénitales distinguées','Consensus autrichien 2023 ; variants incertains et limites histologiques, sans prétendre veille exhaustive 2024–2026.',after='Genetische Abklärung\n\nSeit',ident='R-GENETICS')
current('OGN_MN','Die MN ist eine Immunkomplex',2400,'Introduction, autoantigènes et morphologie','Néphropathie membraneuse','Les fréquences sont celles du consensus2023 ; pas de preuve individuelle par image.',ident='R-IMMUNO')
current('OGN_FSGS','Parietale Epithelzellen',1100,'Physiopathologie, précurseurs podocytaires','Podocytopathies','Réserve limitée de précurseurs, pas capacité illimitée de régénération.',ident='R-PODOCYTES')
current('OGN_GEN','Prophylaktische Antikoagulation\n',3300,'Prophylaxie anticoagulante','Adulte néphrotique','Consensus sans essais contrôlés ; choix bénéfice/risque et doses non uniformisés.',ident='R-ANTICOAG')
current('KDIGO21','Full anticoagulation',1100,'Point1.7.1 ; figure11 pageS36 vue dans le PDF','Syndrome néphrotique adulte','La figure11 distingue événements avérés et prophylaxie à envisager ; ne remplace pas FI suisse.',ident='R-KDIGO-ANTICOAG')

fi_specs=[
('prednisone','Posologie/Mode',2900,'Posologie générale','Adultes ; ne pas confondre avec protocole néphrotique spécifique'),
('spiricort','Pour le traitement à dose élevée',950,'Posologie, fortes doses et durée','Plage générale adulte, distincte des protocoles prolongés spécialisés'),
('solumedrol','La durée d’administration',1000,'Administration et traitement intermittent','Voie intraveineuse ; vitesse de perfusion'),
('lasix_po','Posologie/Mode',1800,'Posologie orale','Adultes et enfants distingués'),
('lasix_iv','Posologie/Mode',1300,'Posologie intraveineuse','Maximum exceptionnel en fonction rénale fortement diminuée'),
('torem',"Traitement d'œdèmes lors de syndrome néphrotique",1100,'Posologie syndrome néphrotique','Adultes et enfants de plus de12ans selonFI'),
('aldactone','Syndrome néphrotiqueNormalement',750,'Posologie néphrotique et œdème pédiatrique','Adulte et enfant distingués'),
('zestril','Indications/Possibilités',1850,'Indications et hypertension','Pas d’indication antiprotéinurique non diabétique explicite'),
('cosaar','Néphropathie chez les diabétiques',900,'Indication diabétique','Ne pas extrapoler cette autorisation au syndrome non diabétique'),
('sortis',"La dose quotidienne de 10 mg d'atorvastatine",600,'Interaction ciclosporine','Dose maximale sous ciclosporine'),
('clexane','Un ajustement posologique est nécessaire',1550,'Insuffisance rénale sévère, doses thérapeutiques et prophylactiques','Clairance de créatinine en mL/min ; distinguer prévention et traitement'),
('marcoumar',"En fonction de l'indication",1000,'Cibles INR','Indications thromboemboliques et limites de prophylaxie néphrotique'),
('sintrom',"Traitement d'entretien et contrôles",1100,'Entretien, INR et dose','Adaptation individuelle, pas dose fixe universelle'),
('eliquis','Indications/Possibilités',1950,'Indications et posologie','Absence de prophylaxie néphrotique dans les indications listées'),
('mabthera','Polyarthrite rhumatoïde (PR)',1500,'Indications auto-immunes et administration','Indications spécifiques ; syndrome néphrotique non listé'),
('endoxan','Administration orale',700,'Posologie orale, dragées50mg','FI comporte oral et IV ; plage générale non protocole néphrotique'),
('sandimmun','Syndrome néphrotiquePour',2200,'Posologie néphrotique et fonction rénale','Dose initiale2,5mg/kg/j si créatinine anormale ; indication spécialisée'),
('prograf','Indications/Possibilités',650,'Indications transplantation','Usage néphrotique hors indication'),
('cellcept','Indications/Possibilités',450,'Indications transplantation','Usage néphrotique hors indication'),
('bactrim','Prophylaxie d’une pneumonie',1400,'Pneumocystose et adaptation rénale','Prévention adulte/adolescent ; demi-dose15–30mL/min, ne pas utiliser<15'),
('albunorm','Indications/Possibilités',1300,'Indication et dosage selon volume circulant','La seule hypoalbuminémie ne détermine pas la posologie'),
('forxiga','Les données concernant les patients présentant une polykystose',600,'Précautions en néphropathie','Non recommandé sous immunosuppresseurs faute de données suffisantes')]
for key,needle,n,section,pop in fi_specs:
    # Normalize the single typographic apostrophe for the exact cached Solu-Medrol text.
    if key=='solumedrol':needle="La durée d'administration"
    current('FI_'+key,needle,n,section,pop,'Lecture ciblée des passages indiqués ; les autres rubriques héritées ne sont pas présentées comme une certification intégrale actuelle.')
current('FI_sortis',"Sortis n'est pas autorisé",280,'Population pédiatrique','Enfants et adolescents','Produit exact : ne pas généraliser la recommandation de classe dès8ans.',ident='R-SORTIS-PEDIATRIE')

sources.append({'id':'R-CIM','url':old['sources']['CIM']['url'],'publisher':'Office fédéral de la statistique','read_at':'2026-11-02','section':'N04, blocN00–N08 et modificateur communS14N00_4','passage':PARA['R-CIM'], 'passage_format':'paraphrase; exact XML retained in external source cache','population':'Nomenclature suisse CIM-10-GM2024','limits':'Édition2024 explicitement indiquée ; pas d’affirmation sur une édition ultérieure. Table après conclusion clinique.','reading_scope':'current author: exact XML rubrics displayed and read','raw_sha256':hashlib.sha256((CACHE/'CIM.raw').read_bytes()).hexdigest()})
current_count=len(sources)
for claim in old['claims']:
    sources.append({'id':'H-'+claim['id'],'title':claim['source_title'],'version':claim['version_date'],'url':claim['source_url'],'publisher':old['sources'].get(claim['source_key'],{}).get('organization','Information professionnelle suisse via AmiKo/oddb'),'read_at':claim['accessed_on'],'section':claim['section'],'passage':claim['claim'], 'passage_format':'inherited author claim paraphrase; exact source excerpt is not recopied and remains at inherited_evidence under the original claim id','population':claim['population'],'limits':claim['limits']+' Héritage Claude Cycle3 : attribution conservée, pas une relecture externe intégrale attribuée à Astra le2novembre.','reading_scope':'inherited documented passage from Claude Cycle3, retained with original date and attribution','claim':claim['claim'],'inherited_location':claim['location'],'inherited_evidence':LEGACY,'source_sha256':claim.get('download_sha256')})
ledger={'code':'N04','author':'astra_nephrologie','recorded_at':NOW,'medical_human_validation':False,'current_selected_passages':current_count,'inherited_claim_records':len(old['claims']),'swiss_fi_products_with_current_targeted_reading':len(fi_specs),'sources':sources,'limitations':['La présence d’un document téléchargé n’est pas une preuve de lecture.','Les passages hérités restent attribués à Claude et datés2026-10-14.','Deux récupérations EuropePMC ont échoué (AGRAWAL18,KERLIN12) ; preuves héritées conservées, aucune relecture externe actuelle revendiquée.','Les22FI ont une lecture ciblée, non une certification de toutes les rubriques et interactions.','Résumé RMS seulement ; pas d’accès prétendu au texte intégral.']}
(OUT/'source-ledger.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')

mapping=[
(1,'Définition','n04-a02',['S6','S7'],'Définitions adulte/enfant, protéinurie de rang néphrotique et syndrome complet ; unités, méthodes et différences de population explicites.'),
(2,'Épidémiologie','n04-a03',['H-EPI-1','H-EPI-2','H-EPI-3','H-EPI-4','H-EPI-5','H-EPI-6'],'Incidences internationales et européennes, dénominateurs par forme et âge ; absence de donnée suisse dans les sources consultées explicitement maintenue.'),
(3,'Physiopathologie','n04-a04',['S4','S10','R-PODOCYTES','R-IMMUNO'],'Organisation normale, perte protéique, œdème, sodium et complications ; six disciplines approfondissent séparément les mécanismes et leurs limites.'),
(4,'Démarche clinique','n04-a07',['S1','S2','S5'],'Les vignettes et la démarche relient confirmation syndromique, gravité et recherche étiologique ; aucune histologie n’est déduite du seul œdème.'),
(5,'Anamnèse','n04-a06',['S5','S8'],'Chronologie, expositions, médicaments, causes secondaires, histoire familiale et manifestations extrarénales ; distinction adulte/enfant conservée.'),
(6,'Examen clinique','n04-semio-examination',['S8','S9'],'Examen initial, volume circulant, œdèmes, pression, infection et manifestations extrarénales ; limites de chaque signe et contexte pédiatrique explicités.'),
(7,'Syndromes','n04-a02',['S6','S7','H-DEF-4'],'Différenciation du syndrome néphrotique complet, de la protéinurie néphrotique isolée et des tableaux mixtes, sans confondre morphologie et cause.'),
(8,'Diagnostic positif','n04-a12',['S6','S7','S5'],'Critères formels regroupés, méthodes et unités visibles ; conditions de l’absence de biopsie en membraneuse précisées dans toutes les surfaces corrigées.'),
(9,'Explorations','n04-e01',['S6','H-DX-1','H-DX-5','H-DX-6'],'Quantification urinaire, albuminémie, sédiment, bilan immunologique et biopsie ; choix de prélèvement, critères de recours et limites d’interprétation.'),
(10,'Arbre diagnostique (différentiels)','n04-a07',['S5','H-DX-10','H-DX-11','H-DX-12'],'Arbre clinique adulte/enfant hérité conservé, diagnostics différentiels et examens discriminants ; liens à la sémiologie et aux limites des marqueurs.'),
(11,'PEC','n04-a09',['R-FI_sandimmun','R-FI_clexane','R-FI_spiricort','R-FI_endoxan','R-ANTICOAG','H-TX-1','H-TX-8'],'Traitement de soutien et étiologique détaillé ; produits suisses exacts, statut hors indication, distinction prévention/traitement et adaptations rénales corrigées.'),
(12,'Prévention/suivi/pronostic','n04-a11',['H-SUP-12','H-SUP-13','H-SUP-14','H-EPI-6','R-FI_forxiga'],'Suivi clinique et immunologique, prévention infectieuse suisse, situations particulières, pronostic et toxicités ; héritage daté clairement distingué de la relecture actuelle.'),
(13,'Points clés','n04-a12',['S6','S7','R-FI_sandimmun','H-DEF-1'],'Synthèse et paramètres clés, retour aux deux patients, fenêtres Pareto et questions existantes conservées ; critères et doses restent attachés à leurs sources.'),
(14,'Pièges','n04-semio-limits',['S3','S5','S9','R-SORTIS-PEDIATRIE','R-FI_clexane'],'Pièges répartis dans le cours et regroupés dans les limites de sémiologie : œdème/volémie, histologie prématurée, unités, clairance/DFGe et autorisation pédiatrique.')]
monograph=[dict(point=n,title=t,anchor=a,sources=s,coverage_explanation=e) for n,t,a,s,e in mapping]
(OUT/'plan-14.json').write_text(json.dumps(monograph,ensure_ascii=False,indent=2)+'\n')
names=['Question clinique et enjeu pour l’examen fédéral','Définition et périmètre CIM-10-GM','Classifications et stades','Épidémiologie suisse puis européenne','Normal → pathologique','Étiologies et facteurs de risque','Anamnèse et symptômes','Examen clinique','Drapeaux rouges et urgences','Examens complémentaires','Diagnostic différentiel','Prise en charge suisse','Complications et pronostic','Suivi, prévention, dépistage','Situations particulières','Spécificités suisses','Critères formels du diagnostic','Paramètres clés chiffrés','Sous-codes CIM-10-GM couverts','Points d’examen fédéral']
anchors=['n04-a01','n04-a02','n04-a05','n04-a03','n04-a04','n04-a05','n04-a06','n04-semio-examination','n04-a08','n04-e01','n04-a07','n04-a09','n04-a08','n04-a11','n04-a11','n04-p01','n04-a12','n04-a12','n04-annexe-cim','n04-a12']
matrix=[{'rubric':i+1,'title':t,'anchor':anchors[i],'content_present':True,'current_verification':'targeted current reading plus attributed inherited evidence; no independent medical certification','limits':'Incidence suisse non trouvée ; données internationales/européennes explicitement étiquetées.' if i==3 else 'Voir source-ledger pour distinction entre passages actuels et hérités.'} for i,t in enumerate(names)]
(OUT/'matrice-20.json').write_text(json.dumps(matrix,ensure_ascii=False,indent=2)+'\n')

figs=json.loads((OUT/'figures-rights.json').read_text())['figures'];(OUT/'images').mkdir(exist_ok=True)
for f in figs:
    target=OUT/'images'/Path(f['path']).name;shutil.copyfile(ROOT/f['path'],target)
    f['path']=str(target.relative_to(OUT));f['annotations']='Numbered overlay markers in lesson HTML; original pixels unchanged; descriptive caption and limits; same license as original.'
    f['medical_review']='Author viewed original and checked description against source; independent medical review pending, not certification.'
content='\n'.join((ROOT/f'chapters/N04/N04_{part}.html').read_text() for part in ['a','b','c','d','pop1','pop2'])
(OUT/'monographie-source.html').write_text(content)
manifest={'code':'N04','author':'astra_nephrologie','recorded_at':NOW,'branch':'codex/alpha77/n04-integrate-g1','base':'8a512893acbab9caa0dcfdd0e8682a44ea72fda6','monograph':monograph,'medina_rubrics':matrix,'sources':sources,'images':figs,'semiology':{'section_anchors':['n04-semio-'+x for x in ['normal','signs','mechanisms','examination','interpretation','differentials','urgency','limits','sources']]},'reviews':{},'blocking_findings':['Independent medical, language and desktop/mobile visual reviews not yet performed; author checks are not distinct reviews.'],'medical_human_validation':False,'tokens_actual':None,'cost_actual':None,'scientific_subtabs':6,'canonical_files':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((ROOT/'chapters/N04').glob('*.html'))},'source_glossary_sha256':hashlib.sha256((ROOT/'glossary/n04.py').read_bytes()).hexdigest()}
(OUT/'lesson-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('Evidence:',current_count,'current selected passages;',len(old['claims']),'attributed inherited claims;',len(fi_specs),'Swiss product FIs; 14 points;20rubrics.')
