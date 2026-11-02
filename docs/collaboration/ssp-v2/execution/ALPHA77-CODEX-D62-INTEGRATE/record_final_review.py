"""Consigner la relecture effective du parent ; jamais appelée par une veille."""
from pathlib import Path
import datetime,hashlib,json,shutil,sys,re
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[4]
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not (OUT/'source-binding.json').exists(),'Reçu existant : aucun renouvellement autorisé'
v=read(OUT/'verification.json');assert v['ok'] and all(c['passed'] for c in v['checks'])
for n,h in v['final_sources'].items():assert sha(ROOT/n)==h,n
assert sha(ROOT/'chapters.json')==v['catalog_sha256'];assert sha(OUT/'D62-apercu-autonome.html')==v['preview_sha256']
visual=read(OUT/'visual-inspection.json');assert visual['actually_seen']
for n,h in visual['sha256'].items():assert sha(OUT/n)==h,'Capture changée depuis inspection : '+n
browser=read(OUT/'browser-report-autonomous.json');assert not browser['errors']
for x in browser['viewports']:assert len(x['windows_checked'])==34 and len(x['quiz_checked'])==4 and len(x['originals_checked'])==3
assert read(OUT/'semiology-final.json')['passed'];now=datetime.datetime.now(datetime.timezone.utc).isoformat()
ledger=read(OUT/'recherche_D62/sources.json');by={s['key']:s for s in ledger['sources']}
mono_specs=[
('Définition','d62-2',['OFS','CIM','WHO'],'La catégorieD62 et ses inclusions/exclusions sont expliquées ; seuil diagnostique, code, source de saignement et choc restent distincts.'),
('Épidémiologie','d62-3',['HUG','TRAUMA'],'La rubrique expose la lacune des données nationalesD62 dans les recherches effectuées ; aucun taux général d’anémie ou de trauma n’est substitué.'),
('Physiopathologie','d62-4',['NORMAL','NORMAL-RBC','TRAUMA'],'Perte de masse et de volume, changements de concentration, transport d’oxygène et récupération médullaire sont expliqués du normal au pathologique.'),
('Démarche clinique','d62-1',['TRAUMA','HUG'],'La source encore active, la perfusion et la tolérance guident les premières décisions ; uneHb initiale normale ne retarde pas l’urgence.'),
('Anamnèse','d62-5',['HUG','TRAUMA','ESGE','PPH-CH'],'Chronologie, sites, médicaments, antécédents, résultats anciens et terrain orientent la perte et la tolérance sans fréquence de signe inventée.'),
('Examen clinique','d62-6',['HUG','TRAUMA','WHO-PPH'],'Les signes sont reliés à leurs mécanismes et limites ; rapport de choc et réévaluation sont contextualisés, avec neuf unités scientifiques dédiées.'),
('Syndromes','d62-3',['TRAUMA','ESGE','PPH-CH'],'Trauma, périopératoire, digestif et obstétrique sont séparés avec perte visible/occulte et phase active/récupération ; pas stadeD62 artificiel.'),
('Diagnostic positif','d62-14',['OFS','CIM','WHO','HUG'],'Association temporelle entre perte et anémie, évolution et causes associées sont documentées ; le diagnostic ne découle pas d’un seul chiffre.'),
('Explorations','d62-e-1',['TRAUMA','HUG','HUG-TRANS'],'Cinq blocs détaillent numération, perfusion/hémostase, localisation, compatibilité et bilan martial, avec indication et limite de chaque examen.'),
('Arbre diagnostique','d62-8',['TRAUMA','HUG','MEDIX'],'L’orientation part de la stabilité et du besoin de contrôle immédiat ; la recherche de source et les alternatives hémolyse/carence/dilution sont explicites.'),
('Prise en charge','d62-10',['TRAUMA','ESGE','WHO-PPH','TXA','PCC'],'L’hémostase spécifique, la transfusion et le traitement martial ont des objectifs distincts ; quatreFI suisses datées et divergences sont exposées.'),
('Prévention et suivi','d62-12',['HUG','MEDIX','FERINJECT','WHO-PPH'],'Suivre la récupération et la récidive, traiter la cause et documenter la carence ; surveillance du fer et délai de réponse séparés des contrôles urgents.'),
('Points clés','d62-14',['WHO','TRAUMA','ESGE','TXA'],'Les chiffres gardent population, unité et but ; seuils diagnostiques, cibles transfusionnelles et horloges thérapeutiques ne sont pas confondus.'),
('Pièges','d62-p-6',['TXA','PCC','FERINJECT','FERROSANOL'],'Produits non interchangeables, calculs reproductibles, contre-indications et concentrations exactes sont expliqués ; quatre cas fictifs évaluent ces décisions.')]
mono=[{'point':i,'title':t,'status':'covered','anchor':a,'sources':[by[k]['id'] for k in keys],'coverage_explanation':c} for i,(t,a,keys,c) in enumerate(mono_specs,1)]
plan=read(OUT/'recherche_D62/plan.json');anchors=['d62-1','d62-2','d62-3','d62-3','d62-s-semio','d62-3','d62-5','d62-6','d62-9','d62-e-1','d62-8','d62-p-1','d62-11','d62-12','d62-13','d62-13','d62-14','d62-14','d62-2','d62-14']
matrix=[]
for i,(r,a) in enumerate(zip(plan['matrix20'],anchors),1):
 matrix.append({'point':i,'title':r['title'],'status':'covered','anchor':a,'sources':r['sources'],'evidence':f'Rubrique traitée dans#{a}, avec références et limites explicitement enseignées ; couverture pédagogique ne signifie pas existence de toutes les données quantitatives.','research_status_preserved':r['status']})
write(OUT/'monograph-14.json',{'code':'D62','points':mono});write(OUT/'matrix-20.json',{'code':'D62','rubrics':matrix,'meaning':'covered signifie rubrique traitée, y compris lacunes déclarées ; pas note médicale20/20.'})
coverage='# Couverture finaleD62\n\nPlan monographique respecté de manière adaptée ; aucun score médical certifié.\n\n| Point | Rubrique | Ancre | Preuve |\n|---|---|---|---|\n'
for r in mono:coverage+=f'| {r["point"]} | {r["title"]} | {r["anchor"]} | {r["coverage_explanation"]} |\n'
coverage+='\n## Matrice20\n\n| Point | Rubrique | Ancre | Limite de recherche conservée |\n|---|---|---|---|\n'
for r in matrix:coverage+=f'| {r["point"]} | {r["title"]} | {r["anchor"]} | {r["research_status_preserved"]} |\n'
(OUT/'coverage-final.md').write_text(coverage)
limits_text=[
'Revue médicale et linguistique ciblée par le même auteur ; aucune validation humaine indépendante, aucune note20/20.',
'Incidence nationaleD62, fréquences de signes et performances isolées non retrouvées ; lacune exposée plutôt que remplacée par des statistiques d’autres populations.',
'Adultes principalement ; pas protocole pédiatrique, de néonatologie ou de traumatisme cérébral complet extrapolé.',
'SGGG2022 etOMS2025 ont des formulations obstétricales distinctes ; aucune adoption suisse fictive du texteOMS.',
'TXA : indication digestiveFI versusESGE, contre-indication rénale sévère versus tableau et allaitement sont explicitement signalés ; pas ordonnance simplifiée.',
'Ferinject : confirmation de carence selonFI et ferritine postpartum inflammatoire doivent être conciliées cliniquement ; besoin total distinct du plafond.',
'Octaplex : pas de dose universelleD62 ; avis spécialisé, héparine et déficitATIII à respecter, données pédiatriques non établies.',
'HUG2022 etSwissmedic2024 restent des références datées ; normes du laboratoire et procédures du centre priment sur une transposition mécanique.',
'Deux originaux photographiques du normal, pas images diagnostiques d’une hémorragie. Repères français en légende, pixels intacts ; cinq schémas logiques non anatomiques.',
'BannièrePROFILES147/165 cohérente avec situations lues ; compteurs globaux du frontend hérité ne certifient pas cette campagne ni sa qualité médicale.',
'Navigation Tab/Entrée vérifiée ; navigation par flèches non prise en charge par moteur hérité. Des barres fixes peuvent recouvrir le bas de longues captures.',
'Livre24 : corps de fenêtre mesuré24.004px et légendes16.944px par taille relative ; police et compteurs hérités non modifiés globalement.',
'Aperçu testé viaHTTP intercepté, aucun déploiement ni fonctionnementfile:// revendiqué ; aucunePR/main, revueVial encore attendue.',
'Délais de conduite/arrêt de travail spécifiquesD62 et garantie de remboursement non établis ; limites administratives déclarées.']
limits=[{'id':f'D62-L{i}','text':t,'blocking':False} for i,t in enumerate(limits_text,1)]
points=[
'OFS D62 sans subdivision, inclusion intra/postopératoire, exclusionP61.3 ; distinctionD50.0 et seuilsOMS diagnostiques120/130, population15–65ans.',
'Hb initiale normale possible ; concentration et masse distinctes, dilution contextualisée, saturation ne remplace pas quantité et circulation.',
'Examen dynamique, anamnèse de source/traitements, réticulocytes non spécifiques, hémolyse et causes mixtes discutées.',
'Trauma : pression80–90 en absence de lésion cérébrale ; cible différente pour traumatisme crânien grave, aucun universalisme.',
'Seuils/cibles digestifs stabilisés70/80 et cibles70–90/≥100 attribuésESGE2026 avec certitude ; choc non résumé au chiffre.',
'TXA :1g10min puis1g8h trauma dans3h ; postpartum1g10min dans3h de naissance, répétition selon30min/24h ; pas indication générale pour tout saignement.',
'FI Leman septembre2026 :100mg/mL,IVexclusive,CI et risques, tableau rénal contradictoire signalé, allaitement et grossesse contextualisés.',
'Ferinject juin2025 :15mg/kg injection versus20perfusion,1000mg par semaine,30min surveillance ; contre-indication reformulée exactement comme absence de carence confirmée.',
'ferro sanol avril2021 : fer élémentaire,100mg/j et phase200sous conditions, plafond5mg/kg/j ; atteinte rénale/hépatique sévère non oubliée.',
'Octaplex novembre2021 : déficit spécifique, individualisation et surveillance ; héparine/TIH/ATIII, aucune routineD62.',
'Transfusion : identité/compatibilité, réaction arrêt/alerte/conservation, hémolyse différée et mécanismesTACO/TRALI ; gravité distincte d’imputabilité.',
'Sciences six disciplines avec neuf unités sémiologiques, trois occurrences de deux originaux et cinq diagrammes ; pas image diagnostiqueD62.',
'Corrections avant liaison : abréviations, unitésmL/g/dL protégées, opérateurs espacés, ancres sémiologie et figure immunohématologie ; tous contrôles relancés.']
pack=OUT/'review-package';pack.mkdir(exist_ok=True)
(pack/'content.html').write_text('\n'.join((ROOT/n).read_text() for n in v['final_sources'] if n.startswith('chapters/D62/') and n.endswith('.html')))
review={'code':'D62','reviewer':'Codex Hématologie','mode':'self_review','reviewed_at':now,'source_snapshot':v['final_sources'],'catalog_sha256':v['catalog_sha256'],'preview_sha256':v['preview_sha256'],'clinical_certification':False,
'medical':{'scope':'Relecture ciblée du contenu rédigé, des décisions et doses ci-dessous ; pas revue humaine exhaustive.','points_checked':points,'blocking_findings':[],'limitations':limits},
'language':{'scope':'Terminologie, unités, calculs, formulations conditionnelles et contre-indications ; corrections relues.','findings_fixed':['mL/g/dL séparés par formatteur : protection des unités avant génération.','Abréviations et fenêtres locales adaptées.','Contre-indicationFerinject reformulée sans ambiguïté.'],'remaining':'Absence absolue d’erreur non garantie.'},
'visual_desktop':{'scope':'1440×900 : accueil, sciences, original/légendes, calculTXA et quiz final ; parcours interactif automatisé distinct.','captures':[n for n in visual['captures'] if '-1440-' in n]},
'visual_mobile':{'scope':'390×844 : original/légendes, diagrammes, calculfer et Livre24 ; taille réelle mesurée.','captures':[n for n in visual['captures'] if '-390-' in n]},
'captures_inspected':visual['captures'],'verification':{'windows_per_viewport':34,'quizzes_per_viewport':4,'science_tabs':6,'semiology_sections':9,'originals':2,'original_occurrences':3,'caption_markers':12,'non_anatomical_causal_diagrams':5,'browser_errors':browser['errors'],'source_binding_preexisting':False}}
write(pack/'self-review.json',review)
images=[]
for x in read(ROOT/'assets/img/d62/alpha/codex/provenance.json')['images']:
 src=ROOT/x['file'];shutil.copyfile(src,pack/src.name);images.append({'path':'review-package/'+src.name,'source_path':x['file'],'title':x['title'],'original_url':x['source_url'],'author':x['credit'],'license':x['license'],'license_url':x['license_url'],'sha256':sha(src),'changes':'Pixels intacts, annotations de légende françaises.','annotations':x['annotations'],'medical_review':'Self_review : originaux réellement vus, légendes finales inspectées ; aucune validation humaine indépendante.'})
sources=[]
for x in ledger['sources']:sources.append({'id':x['id'],'url':x['url'],'publisher':x['editeur'],'title':x['titre'],'read_at':x['date_consultation'],'section':x['section_page'],'passage':x['passage_paraphrase'],'population':x['population'],'limits':x['limites'],'reading_depth':x['niveau_lecture'],'cache_sha256':x['cache_sha256'],'reuse_attributed':x.get('reuse_attributed'),'read_in_this_lesson':x.get('read_in_this_lesson'),'additional_read_reference':'recherche_D62/additional-research.json'})
manifest={'code':'D62','author':'Codex Hématologie','monograph':mono,'matrix20':matrix,'matrix20_reference':'matrix-20.json','sources':sources,'images':images,'semiology':{'section_anchors':['d62-semio-'+x for x in ['normal','signs','mechanisms','examination','interpretation','differentials','urgency','limits','sources']]},'reviews':{k:{'path':'review-package/self-review.json','sha256':sha(pack/'self-review.json'),'reviewer':'Codex Hématologie','mode':'self_review'} for k in ['medical','language','visual_desktop','visual_mobile']},'blocking_findings':[],'limitations':limits,'clinical_certification':False,'closure_status':'ready_for_project_gate_and_user_review'}
write(OUT/'lesson-manifest.json',manifest);write(pack/'lesson-manifest.json',manifest);write(OUT/'images-provenance.json',images)
sys.path.insert(0,'/workspace/Medina-harness/harness');import medina_harness
check=medina_harness.validate_lesson(OUT);assert check['technical_contract_pass'],check
write(OUT/'source-binding.json',{'code':'D62','verified_at':v['finished_at'],'reviewed_at':now,'preview':'D62-apercu-autonome.html','preview_sha256':v['preview_sha256'],'final_sources':v['final_sources'],'checks':['verification.json','browser-report-autonomous.json','sciences-final.json','semiology-final.json','visual-inspection.json','book24-check.json','coverage-final.md','recherche_D62/recherche.md','recherche_D62/additional-research.json'],'clinical_certification':False})
print(json.dumps({'reviewed_at':now,'self_review_recorded':True,'manifest_sha256':sha(OUT/'lesson-manifest.json'),'binding_sha256':sha(OUT/'source-binding.json'),'preview_sha256':v['preview_sha256'],'clinical_certification':False,'completed':False}))
