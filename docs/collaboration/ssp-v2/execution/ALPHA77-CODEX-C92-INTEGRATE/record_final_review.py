#!/usr/bin/env python3
"""Consignation manuelle d'une relecture réelle. Jamais exécutée par la veille."""
from pathlib import Path
import datetime,hashlib,json,shutil,sys
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[4]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not (OUT/'source-binding.json').exists(),'Un reçu existant ne doit jamais être renouvelé automatiquement'
v=read(OUT/'verification.json');assert v['ok'] and all(x['passed'] for x in v['checks'])
for name,digest in v['final_sources'].items():assert sha(ROOT/name)==digest,name
assert sha(ROOT/'chapters.json')==v['catalog_sha256']
assert sha(OUT/'C92-apercu-autonome.html')==v['preview_sha256']
visual=read(OUT/'visual-inspection.json');assert visual['actually_inspected'] and visual['preview_sha256']==v['preview_sha256'] and len(visual['captures'])>=20
for name,digest in visual['captures'].items():assert sha(OUT/name)==digest,name
browser=read(OUT/'browser-report-autonomous.json');assert not browser['errors']
for x in browser['viewports']:
 assert len(x['windows_checked'])==42 and len(x['quiz_checked'])==8 and len(x['originals_checked'])==6
 assert x['horizontal_overflow']==x['book_overflow']==x['unsafe_shared_abbreviations']==0 and x['book_font']=='24px'
 assert x['keyboard_after_tab']=='c92-tab-anat'
semio=read(OUT/'semiology-final.json');assert semio['passed'] and not semio['findings']
now=datetime.datetime.now(datetime.timezone.utc).isoformat();pack=OUT/'review-package';pack.mkdir(exist_ok=True)
(pack/'content.html').write_text('\n'.join((ROOT/f'chapters/C92/C92_{x}.html').read_text() for x in ['a','b','c','d','pop1','pop2']))
limits_text=[
'41 entrées documentaires, dont 15 FI suisses : lectures ciblées, résumé institutionnel du sarcome ORL et réutilisations attribuées. Aucune lecture intégrale générale des documents revendiquée.',
'Porte recherche réelle avant rédaction : 38 entrées. Trois FI ajoutées après cette porte pour la pharmacologie ; reçu initial conservé, aucun effet rétroactif.',
'Pas d’incidence suisse actuelle propre à chaque sous-type C92 établie ; statistiques C91–C95 et cohortes européennes non transformées en taux suisse spécifique.',
'OMS 2022, ICC, ELN 2022 intensif et ELN 2024 moins intensif ont des portées différentes ; terminologie CIM et ancien libellé AML-MRC de FI non assimilés automatiquement aux entités modernes.',
'LPA : usage européen récent ATO de première ligne haut risque distinct de la FI suisse Trisenox non haut risque ; divergence de suspension ATO/ATRA lors de différenciation explicitée.',
'Vanflyta : entretien après allogreffe exclu de l’indication suisse consultée ; colonnes de réduction pour interaction et toxicité distinctes.',
'Vyxeos : unité de bilirubine incohérente dans extraction française, aucun seuil numérique recopié ni corrigé de mémoire. Schéma liposomal non interchangeable avec molécules libres.',
'Daunoblastin : exemples posologiques de FI ne hiérarchisent pas tous les protocoles actuels ; formulations de contre-indications et précautions parfois divergentes, vérification spécialisée requise.',
'Vidaza : tableau extrait de cytopénies présente une incohérence de libellé ; aucun algorithme certain reconstruit à partir de cette extraction.',
'Quatre originaux, six occurrences et vingt-quatre repères de légende ; pas de génotype, incidence ou décompte représentatif déduit d’un champ. Agrandissement utile pour les détails cytologiques fins.',
'Moteur hérité : navigation par flèches absente ; Tab puis Entrée testés. Barres fixes pouvant recouvrir temporairement une zone lors du défilement ou sur une capture longue.',
'Bandeau hérité PROFILES SSP159/227 non certifié comme cartographie officielle. Texte clinique renvoyant aux situations du référentiel réellement lues ; compteurs globaux de l’interface distincts de cette campagne.',
'Essais du moteur natif sur origine HTTP interceptée, requêtes externes bloquées ; aucun déploiement ni fonctionnement file:// affirmé.',
'Quatre catégories de revue attribuées au même parent en self_review ; aucune revue médicale humaine indépendante. Matrices14/20 et compteurs ne sont pas un score de qualité médicale.',
'CIM-10-GM 2024 OFS : sous-codes et rémission relus. Aucune certification exhaustive de facturation2026 ni garantie de remboursement individuel ; revue Vial attendue avant toute PR/main.'
]
limits=[{'id':f'C92-L{i}','text':t,'blocking':False} for i,t in enumerate(limits_text,1)]
points=[
'Périmètre OFS C92.0 à C92.9 et caractères0/1 ; C92.5 aiguë distinct de C93.1 chronique, pas de suffixe de rechute américain.',
'OMS/ICC : seuils de blastes contextualisés, exceptions BCR::ABL1/CEBPA/AML-MR et corrélation morphologique ; dysplasie seule insuffisante pour AML-MR.',
'ELN intensif versus moins intensif : populations et limites distinctes ; MRD négative ne prouve pas éradication et mutations DTA interprétées séparément.',
'LPA : ATRA dès suspicion et support coagulation ; forme hypogranulaire possible, Auer non spécifique de PML::RARA ; pas de leucaphérèse routinière.',
'Trisenox : première ligne non haut risque≤10G/L,0,15mg/kg/j, différences induction/consolidation/rechute, K/Mg et QT ; divergence avec recommandations conservée.',
'Vénétoclax : escalade100/200/400 HMA versus600 LDAC, WBC<25 avant début, lyse et CYP3A ; règles LLC non importées en LAM.',
'Tibsovo : IDH1R132,500mg à jeun et250 si inhibiteur pertinent ; CI et QT propres à la FI, différenciation surveillée.',
'FLT3 : midostaurine50mg2x/j J8–21, quizartinib ITD phases distinctes et pas entretien postallogreffe, giltéritinib rechute120mg ; surveillances propres aux produits.',
'Cytarabine/daunorubicine libres versus Vyxeos : formulation et calendrier distincts, exemples de FI et adaptations non érigés en protocole universel.',
'LMC : BCR::ABL1 et transcrit, jalons IS datés, cinétique/observance avant changement, profondeur et durée de réponse avant TFR surveillée.',
'Scemblix : FI septembre2026,80mg/j ou40mg2x/j, T315I200mg2x/j, jeûne et interactions non assimilés aux autres TKI ; imatinib avec repas et doses propres.',
'MDS/MPN neutrophilique et sarcome : diagnostic/exclusions, données rares et allogreffe ou traitement systémique contextualisés, pas stratégie LMC par défaut.',
'Images : pixels et flèches originales intacts, licences et repères de légende vérifiés ; schémas causaux sans anatomie synthétique.',
'Lacune des sous-codes repérée et corrigée avant liaison finale ; définitions et quiz corrigés après contrôles, puis ensemble des vérifications repassé.'
]
review={'code':'C92','reviewer':'Codex Hématologie','mode':'self_review','reviewed_at':now,'source_snapshot':v['final_sources'],'catalog_sha256':v['catalog_sha256'],'preview_sha256':v['preview_sha256'],'clinical_certification':False,
'medical':{'scope':'Relecture ciblée des décisions, critères, doses, limites et sous-codes du contenu rédigé ; ne vaut pas revue humaine indépendante exhaustive.','points_checked':points,'blocking_findings':[],'limitations':limits},
'language':{'scope':'Auto-relecture ciblée de la terminologie, des unités, des formulations conditionnelles et des explications de quiz.','findings_fixed':['Abréviations non couvertes ajoutées avec définition adaptée, y compris noms propres identifiés comme tels.','Réponses aux quiz développées pour éviter certains renvois globaux ; termes sensibles liés aux fenêtres C92.','Recommandation, indication suisse, codage et remboursement explicitement séparés.'],'remaining':'Absence absolue d’erreur non garantie ; revue utilisateur attendue.'},
'visual_desktop':{'scope':'1440×900 : six occurrences originales, légendes, sciences, navigation et Livre24.','captures':[n for n in visual['captures'] if '-1440-' in n],'mode':browser['mode']},
'visual_mobile':{'scope':'390×844 : légendes, cinq diagrammes, dialogues, Livre24 et tableau OFS.','captures':[n for n in visual['captures'] if '-390-' in n],'mode':browser['mode']},
'captures_inspected':visual['captures'],'verification':{'windows_per_viewport':42,'quizzes_per_viewport':8,'science_tabs':6,'semiology_sections':9,'originals':4,'original_occurrences':6,'caption_markers':24,'non_anatomical_causal_diagrams':5,'keyboard':'Tab and Enter passed; inherited arrow navigation unsupported','browser_errors':browser['errors']}}
write(pack/'self-review.json',review)
images=[]
for row in read(ROOT/'assets/img/c92/alpha/codex/provenance.json')['images']:
 src=ROOT/row['file'];shutil.copyfile(src,pack/src.name)
 images.append({'path':'review-package/'+src.name,'source_path':row['file'],'title':row['title'],'original_url':row['source_url'],'author':row['credit'],'license':row['license'],'license_url':row['license_url'],'sha256':sha(src),'changes':'Pixels intacts, repères français dans les légendes.','annotations':row['annotations'],'medical_review':'Self_review parent : originaux et occurrences rendues réellement inspectés ; aucune validation humaine indépendante. Voir visual-inspection.json et ses empreintes.'})
sources=[]
for s in read(OUT/'recherche_C92/sources.json')['sources']:
 sources.append({'id':s['id'],'url':s['url'],'publisher':s['editeur'],'title':s['titre'],'read_at':s['date_consultation'],'section':s['section_page'],'passage':s['passage_paraphrase'],'population':s['population'],'limits':s['limites'],'reading_depth':s['niveau_lecture'],'cache_sha256':s['cache_sha256'],'reuse_attributed':s.get('reuse_attributed'),'read_in_current_session':s.get('read_in_current_session')})
manifest={'code':'C92','author':'Codex Hématologie','monograph':read(OUT/'monograph-14.json')['points'],'matrix20':read(OUT/'matrix-20.json')['rubrics'],'matrix20_reference':'matrix-20.json','sources':sources,'images':images,'semiology':{'section_anchors':['c92-semio-'+s for s in ['normal','signs','mechanisms','examination','interpretation','differentials','urgency','limits','sources']]},'reviews':{k:{'path':'review-package/self-review.json','sha256':sha(pack/'self-review.json'),'reviewer':'Codex Hématologie','mode':'self_review'} for k in ['medical','language','visual_desktop','visual_mobile']},'blocking_findings':[],'limitations':limits,'clinical_certification':False,'closure_status':'ready_for_project_gate_and_user_review'}
write(OUT/'lesson-manifest.json',manifest);write(pack/'lesson-manifest.json',manifest);write(OUT/'images-provenance.json',images)
sys.path.insert(0,'/workspace/Medina-harness/harness');import medina_harness
result=medina_harness.validate_lesson(OUT);assert result['technical_contract_pass'],result
write(OUT/'source-binding.json',{'code':'C92','verified_at':v['finished_at'],'reviewed_at':now,'preview':'C92-apercu-autonome.html','preview_sha256':v['preview_sha256'],'final_sources':v['final_sources'],'checks':['verification.json','browser-report-autonomous.json','sciences-final.json','semiology-final.json','visual-inspection.json','coverage-final.md','recherche_C92/recherche.md'],'clinical_certification':False})
print(json.dumps({'self_review_recorded':True,'manifest_sha256':sha(OUT/'lesson-manifest.json'),'binding_sha256':sha(OUT/'source-binding.json'),'preview_sha256':v['preview_sha256'],'clinical_certification':False,'completed':False}))
