#!/usr/bin/env python3
"""Consigner manuellement une relecture réelle après vision des captures finales.
Jamais exécuté par le watcher ; aucune lecture médicale n'est simulée par ce script.
"""
from pathlib import Path
import json,hashlib,datetime,shutil,sys
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[4]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
verify=read(OUT/'verification.json');assert verify.get('ok') and all(x['exit_code']==0 for x in verify['checks'])
for name,value in verify['final_sources'].items():assert sha(ROOT/name)==value,name
assert sha(OUT/'D63-apercu-autonome.html')==verify['preview_sha256']
visual=read(OUT/'visual-inspection.json');assert visual['actually_inspected'] and visual['preview_sha256']==verify['preview_sha256'] and len(visual['captures'])>=12
for name,value in visual['captures'].items():assert sha(OUT/name)==value,name
browser=read(OUT/'browser-report-autonomous.json');assert not browser['errors']
for v in browser['viewports']:
 assert len(v['windows_checked'])==39 and len(v['quiz_checked'])==8 and len(v['originals_checked'])==4
 assert v['horizontal_overflow']==v['book_overflow']==v['unsafe_shared_abbreviations']==0 and v['book_font']=='24px'
 assert v['keyboard_after_tab']=='d63-tab-anat'
sys.path.insert(0,'/workspace/Medina-harness/harness');import medina_harness
semio=medina_harness.inspect_semiology(ROOT,'D63');assert not semio['findings'];write(OUT/'semiology-final.json',semio)
now=datetime.datetime.now(datetime.timezone.utc).isoformat();PACK=OUT/'review-package';PACK.mkdir(exist_ok=True)
(PACK/'content.html').write_text('\n'.join((ROOT/f'chapters/D63/D63_{x}.html').read_text() for x in ['a','b','c','d','pop1','pop2']))
texts=[
 'Aucune incidence suisse contemporaine propre à D63 établie ; cohortes hétérogènes et ancienne série de 1997 citée indirectement ne deviennent pas une probabilité individuelle actuelle.',
 'Corpus de 26 entrées : passages ciblés, trois FI suisses et réutilisations attribuées. Les reçus précisent leur profondeur ; aucune lecture intégrale nouvelle de toutes les sources revendiquée.',
 'Versions FI retrouvées : ferro sanol avril 2021, Eprex août 2021, Ferinject juin 2025. Recommandation et indication suisse sont distinctes ; aucun protocole prescripteur universel ou statut suisse HIF-PHI inventé.',
 'Eprex : ambiguïté des conditions oncologiques de réponse à quatre semaines reliées par ou conservée ; cas discordant à clarifier avec prescripteur/protocole, aucun algorithme certain reconstruit.',
 'Différences ECCO TSAT 16/20 %, CHr ECCO 29 versus ESMO 28 pg, ferritine medix/Delphi et cible Eprex/KDIGO explicites. Leurs populations, méthodes et objectifs ne sont pas fusionnés.',
 'Tableau graphique des classes ESC 2023 non lu ; seules les recommandations textuelles et résultats IRONMAN effectivement consultés sont utilisés. Aucun bénéfice de mortalité inventé.',
 'Repères HUG 2019 adultes datés ; OMS 2024 ne couvre pas par ce tableau tous les moins de six mois ou plus de 65 ans. Les seuils diagnostiques ne sont pas des ordres de transfusion.',
 'Deux images humaines normales, quatre occurrences et seize repères de légende. La photographie macroscopique ne montre pas les lignées ; le frottis à champ large ne permet pas un comptage réticulocytaire ni un diagnostic de D63. Grossissement/zoom utile pour détails fins, surtout mobile.',
 'Moteur hérité : les flèches ne déplacent pas les sous-onglets. Navigation Tab puis Entrée et états ARIA testés ; barres flottantes Plan/pagination peuvent recouvrir temporairement une zone lors du défilement. Aucun moteur partagé modifié.',
 'Essai du vrai moteur sur origine HTTP interceptée et sans requêtes externes ; aucun déploiement ni essai file:// revendiqué. Les compteurs et bandeaux globaux hérités ne mesurent pas cette campagne.',
 'Couverture 14/20 et auto-relectures attribuées au parent Codex ; aucune revue indépendante ou validation médicale humaine. Publication sur branche et attente de revue Vial seulement, aucune PR/main.',
 'CIM-10-GM 2024 du projet : D63.0* et D63.8* vérifiés dans les données OFS ; aucune certification exhaustive de facturation 2026, aucun prix ni remboursement individuel présumé.'
]
limits=[{'id':f'D63-L{i}','text':t,'blocking':False} for i,t in enumerate(texts,1)]
images=[]
for row in read(ROOT/'assets/img/d63/alpha/codex/provenance.json')['images']:
 src=ROOT/row['file'];shutil.copyfile(src,PACK/src.name)
 images.append({'path':'review-package/'+src.name,'source_path':row['file'],'original_url':row['source_url'],'author':row['credit'],'license':row['license'],'license_url':row['license_url'],'license_scope':'Licence propre au fichier Commons OpenStax 2016 ou au frottis humain Commons déjà documenté dans D50 ; pas de copie des figures du manuel OpenStax actuel.','sha256':sha(src),'changes':'Pixels intacts ; annotations françaises dans les légendes.','annotations':'Quatre repères de position et d’interprétation par occurrence : tissu/travées/limite/barre ou hématies/contraste/répartition/barre, avec limites diagnostiques.','medical_review':'Auto-relecture parent Codex : originaux et quatre occurrences rendues effectivement vus, normales et non présentées comme pathologie. Captures finales et empreintes dans visual-inspection.json.'})
review={'code':'D63','reviewer':'Codex Hématologie','mode':'self_review','reviewed_at':now,'source_snapshot':verify['final_sources'],'preview_sha256':verify['preview_sha256'],'clinical_certification':False,
 'medical':{'scope':'Monographie, examens, six sciences, trois FI, trente fenêtres et neuf synthèses ; relecture de mécanismes, seuils, calculs, populations et limites après rédaction.','points_checked':[
 'WHO 2024 : seuils sexe/âge/trimestre ; diagnostic, sévérité, objectif ESA et transfusion distingués.',
 'Ferritine/TSAT : réserve versus disponibilité, carence mixte ; CHr 28/29 et sTfR non universels.',
 'KDIGO : HD ferritine ≤500 et TSAT ≤30 ; ND/PD <100 et <40 ou 100–<300 et <25 ; suspendre routine si >700 ou TSAT ≥40 ; infection systémique et réévaluation.',
 'ESA : cible adulte KDIGO <11,5 g/dL, FI Eprex 10–12 distincte ; dose initiale 50 UI/kg trois fois par semaine et calcul 3500 UI à 70 kg.',
 'Ferinject : g/dL dans Ganzoni ; 1508 mg puis arrondi1600 contre tableau2000 à70 kg/Hb9 ; injection15, perfusion20 mg/kg et1000 max, semaine1000, HD200/j ; exemple45 kg donne900 mg.',
 'ferro sanol : âge ET poids,100/200 mg et5 mg/kg/j ; contre-indication rénale/hépatique sévère, interactions et prise sans mâcher.',
 'Eprex : contre-indication autonome des antécédents thromboemboliques conservée après hypothèse initiale réfutée ; intention curative, HTA non contrôlée et PRCA ; conditions discordantes de réponse non réinventées.',
 'Transfusion : repères suisses70/80 chez patients stables définis ; hémorragie/ACS distincts ; une unité/réévaluation, allo-immunisation sans retard d’urgence.',
 'ESC : symptômes/qualité de vie/hospitalisations séparés de mortalité ; IRONMAN RR0,82 IC0,66–1,02 P0,070 et analyse COVID distincte.',
 'Sources suisses d’abord, recommandations de population ensuite ; OpenStax pour physiologie normale paraphrasée et image2016CCBY, aucune anatomie générée.',
 'Structure native : six onglets, premier h3 exact, neuf marqueurs nommés, sources directes et marqueur clinique contenant une prose.'
 ],'blocking_findings':[],'limitations':limits},
 'language':{'scope':'Relecture clinique et linguistique des six fragments et fenêtres, unités, temporalités, formulations conditionnelles et codes.','findings_fixed':['Mots et dates collés corrigés par liste fermée, pas de séparation générale des symboles scientifiques','Définitions Hb/MRC/TSAT/ESA/MICI/EPO et mots logiques et/ou rendus localement sans faux renvoi ET','Réponses quiz développées pour éviter les sous-cibles de glossaire','Prescription, recommandation et couverture distinguées ; exemples fictifs explicites'],'remaining':'Auto-relecture sans garantie absolue d’absence d’erreur.'},
 'visual_desktop':{'scope':'1440×900 : images originales, annotations, sciences, dialogues, navigation et mode Livre24.','captures':[n for n in visual['captures'] if '-1440-' in n],'mode':browser['mode']},
 'visual_mobile':{'scope':'390×844 : images et légendes, cinq diagrammes causaux lisibles, dialogues, navigation et mode Livre24.','captures':[n for n in visual['captures'] if '-390-' in n],'mode':browser['mode']},
 'captures_inspected':visual['captures'],'verification':{'windows_per_viewport':39,'quizzes_per_viewport':8,'science_tabs':6,'semiology_sections':9,'originals':2,'original_occurrences':4,'non_anatomical_causal_diagrams':5,'keyboard':'Tab + Enter works; arrow keys unsupported by inherited engine','browser_errors':browser['errors']}}
write(PACK/'self-review.json',review)
ledger=read(OUT/'recherche_D63/sources.json')['sources']
sources=[{'id':s['id'],'url':s['url'],'publisher':s['editeur'],'title':s['titre'],'read_at':s['date_consultation'],'section':s['section_page'],'passage':s['passage_paraphrase'],'population':s['population'],'limits':s['limites'],'reading_depth':s['niveau_lecture'],'cache_sha256':s['cache_sha256'],'reuse_attributed':s.get('reuse_attributed'),'read_in_current_session':s.get('read_in_current_session')} for s in ledger]
manifest={'code':'D63','author':'Codex Hématologie','monograph':read(OUT/'monograph-14.json')['points'],'matrix20':read(OUT/'matrix-20.json')['rubrics'],'matrix20_reference':'matrix-20.json','sources':sources,'images':images,'semiology':{'section_anchors':['d63-semio-'+s for s in ['normal','signs','mechanisms','examination','interpretation','differentials','urgency','limits','sources']]},'reviews':{k:{'path':'review-package/self-review.json','sha256':sha(PACK/'self-review.json'),'reviewer':'Codex Hématologie','mode':'self_review'} for k in ['medical','language','visual_desktop','visual_mobile']},'blocking_findings':[],'limitations':limits,'clinical_certification':False,'closure_status':'ready_for_project_gate_and_user_review'}
write(OUT/'lesson-manifest.json',manifest);write(PACK/'lesson-manifest.json',manifest);write(OUT/'images-provenance.json',images)
assert not (OUT/'source-binding.json').exists(),'No automatic renewal of an existing source binding'
write(OUT/'source-binding.json',{'code':'D63','verified_at':verify['finished_at'],'reviewed_at':now,'preview':'D63-apercu-autonome.html','preview_sha256':verify['preview_sha256'],'final_sources':verify['final_sources'],'checks':['verification.json','browser-report-autonomous.json','sciences-final.json','semiology-final.json','visual-inspection.json','coverage-final.md','recherche_D63/recherche.md'],'clinical_certification':False})
print(json.dumps({'self_review_recorded':True,'manifest_sha256':sha(OUT/'lesson-manifest.json'),'binding_sha256':sha(OUT/'source-binding.json'),'preview_sha256':verify['preview_sha256'],'clinical_certification':False,'completed':False}))
