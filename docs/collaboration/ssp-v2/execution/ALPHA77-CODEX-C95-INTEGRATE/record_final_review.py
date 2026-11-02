#!/usr/bin/env python3
"""Consigner une relecture réellement faite ; jamais appelé par la veille.

Exécuter manuellement après inspection des captures finales énumérées dans
visual-inspection.json. Ce script vérifie les octets, mais ne relit pas la médecine.
"""
from pathlib import Path
import json,hashlib,datetime,shutil,re
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[4]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
verify=read(OUT/'verification.json');assert verify.get('ok') and all(c['exit_code']==0 for c in verify['checks'])
for name,expected in verify['final_sources'].items():assert sha(ROOT/name)==expected,name
assert sha(OUT/'C95-apercu-autonome.html')==verify['preview_sha256']
visual=read(OUT/'visual-inspection.json');assert visual['preview_sha256']==verify['preview_sha256'] and visual['actually_inspected'] and len(visual['captures'])>=10
for name,expected in visual['captures'].items():assert sha(OUT/name)==expected,name
browser=read(OUT/'browser-report-autonomous.json');assert not browser['errors']
for v in browser['viewports']:
 assert len(v['windows_checked'])==52 and len(v['quiz_checked'])==5
 assert v['horizontal_overflow']==v['book_overflow']==v['unsafe_shared_abbreviations']==0
 assert v['book_font']=='24px' and len(v['originals_checked'])==7
now=datetime.datetime.now(datetime.timezone.utc).isoformat();PACK=OUT/'review-package';PACK.mkdir(exist_ok=True)
content='\n'.join((ROOT/f'chapters/C95/C95_{x}.html').read_text() for x in ('a','b','c','d','pop1','pop2'));(PACK/'content.html').write_text(content)
texts=[
 'Incidence suisse propre à C95/LALA/LAPM non établie ; données OFS2013–2017 agrégées C91–C95 et registres étrangers restent datés et contextualisés.',
 'CIM-10-GM2024 lue ; aucune certification exhaustive de facturation2026, ni prix ou remboursement individuel LS/OAMal établi.',
 'EBMT2026 : résumé public seulement lu, pas texte intégral ; cohortes de greffe sélectionnées non randomisées avec horizons distincts.',
 'Corpus32entrées avec passages ciblés et réutilisations attribuées ; toutes les références ne sont pas des lectures intégrales nouvelles. Les revues ne remplacent pas les classifications originales pour les points non relus.',
 'Sept fiches suisses lues aux rubriques déclarées ; quatre produits détaillés en fenêtres. Ce cours ne contient pas les protocoles prescripteurs complets de tous les cytotoxiques, immunothérapies ou greffes.',
 'LAPM/LAI rares : recommandations et séries conditionnelles, aucune indication suisse nommée LAPM inventée ; soins de support lus selon leur libellé, sans qualifier automatiquement tous les usages hors indication.',
 'Repères biologiques HUG2019 adultes, pas normes suisses universelles2026, pédiatriques, de grossesse ou seuils transfusionnels.',
 'OpenStax utilisé pour faits biologiques normaux paraphrasés ; seule photographie édition2016 explicitement CC BY4.0 reproduite. Revue de cytométrie utilisée pour diagnostic/figures, pas fondement américain de conduite thérapeutique.',
 'Essai sur origine HTTP interceptée, sans déploiement ni accès file:// revendiqué ; ouverture file:// interdite par politique administrateur.',
 'Sur mobile, diagrammes de cytométrie denses : utiliser zoom/ordinateur pour axes fins ; légendes françaises explicites. Barres flottantes Plan/pagination héritées peuvent masquer temporairement une portion lors du défilement ; moteur partagé non modifié.',
 'Bandeau et compteurs globaux hérités ne mesurent pas cette campagne. Auto-relectures attribuées au parent Codex, sans audit indépendant ni certification médicale humaine.'
]
limits=[{'id':f'C95-L{i}','text':t,'blocking':False} for i,t in enumerate(texts,1)]
images=[]
for row in read(ROOT/'assets/img/c95/alpha/codex/provenance.json')['images']:
 src=ROOT/row['file'];name=src.name;shutil.copyfile(src,PACK/name)
 images.append({'path':'review-package/'+name,'source_path':row['file'],'original_url':row['source_url'],'author':row['credit'],'license':row['license'],'license_url':row['license_url'],'license_scope':'Licence de figure contrôlée sur source : Commons édition2016 ou article Cancers2025 ; aucune exclusion relevée pour les figures3/6/14.','sha256':sha(src),'changes':'Pixels originaux inchangés ; légendes françaises explicatives ajoutées au cours.','annotations':'Moelle : tissu/limite de la photographie ; cytométrie : couleurs, panneaux, contrôles et intensité relative, différence faible MPO et profil LAI.','medical_review':'Auto-relecture Codex : originaux réellement vus, figure3 B/myéloïde, figure6 faibleMPO LLA-B, figure14 LAI/CD34/CD117 et TdT non obligatoire ; légendes et limites confrontées aux passages effectivement lus.','clinical_certification':False})
review={'author':'Codex Hématologie','reviewer':'Codex Hématologie','mode':'self_review','reviewed_at':now,'model':'Modèle de la session parent ; aucun changement Sol du parent prétendu.','source_sha256':verify['final_sources'],'preview_sha256':verify['preview_sha256'],'clinical_human_certification':False,
 'medical':{'scope':'Relecture des14points,20rubriques, sixsciences, fenêtres et cas avec confrontation aux passages réellement lus ; revue de l’auteur, pas avis indépendant.',
 'findings_fixed':[
 'Dossier incomplet distinct de lignée ambiguë démontrée ; sous-codes chroniques/autres non décrits comme nécessairement provisoires ; caractère0 inclut rémissionpartielle/inconnue, pas caractère2.',
 'Seuil20% LALA distinct des exceptions génétiques LMA et du cadre25% LLA/LBL ; urgence ATRA non retardée par seuil arbitraire.',
 'CD19 fort/faible, combinaisons et exclusion CD79a en contexteT ; CD3epsilon/non-zêta, MPOrelative et alternative monocytaire ; positivité associée isolée insuffisante.',
 'OMS/ICC non fusionnées : intensités, populationmineure5%, RUNX1 et hiérarchies ; divergence d’une cellule de tableau Fuda conservée explicitement.',
 'Deux populations phénotypiques ne prouvent pas deux clones ; hématogones exclus ; LAI suppose panel large et TdT non obligatoirement positive.',
 'LMCblastique, LMAgénétique, anomalies liées à myélodysplasie et fusions de kinase contextualisées ; aucun testFGFR1 obligatoire universel.',
 'Registre américain et cohortes pédiatriques/adultes gardent dénominateurs, horizons et sélection ; EVOLVE70cas ayant déjà changé de lignée, pas incidence chez tous les traités.',
 'Induction typeLLA souvent favorisée pour LAPM, pas touteLAI ; MRDpositive et greffe non décisions automatiques ; iBFM<18ans, algorithme5% non universel.',
 'EBMT2017/2026 : horizons3/2ans et absence de bras randomisé ; résumé2026 limité ; aucun gain causal14,4points annoncé.',
 'Leucostase possible sous100G/L ; ATRA sur suspicionLAP, pas touteC95 ; source neutropénie2016 ne fixe pas antibiotique2026.',
 'Glivec LLA600mg/j adulte, pédiatrie340mg/m²max600, adaptations rein/foie et interactions contextualisées ; indicationsLLA non assimilées automatiquement LAPM.',
 'Iclusig suisse : T315I ou autresITKc-abl inappropriés ; pas condition résistance/intolérance importée ;45mgLLA, réduction45→15 propre àLMCchronique, foie30 et rein≥50 contextualisés.',
 'Fasturtec0,20mg/kg/jIV30min jusqu’à7jours, G6PD/hémolyse et méthémoglobine ; urateprérefroidi/glace4°C/<4h, surveillanceK/phosphate indépendante.',
 'LitalirFIaoût2026 :40–50mg/kginitial puis10–20entretien dans indicationschroniques, pas transposition acute ; renal/foie/contraception/mesurecontinueglucose explicités.',
 'Vesanoid dose parsurface et contexteLAP ; Blincyto populations/indications et MRD≥0,1 ; Venclyxto interactionsCYP3A propres àLLC versusLMA et millepertuis.',
 'RC morphologique, récupération, MRD et guérison séparées ; calendrierLLA aprèsmaintenance non transposé àtouteLALA/postgreffe.',
 'PROFILES2017 SSP2/4/6/16/21/25/88/159/227 et examen2026 vérifiés ; transition2028 conservée.',
 'Définitions partagées horscontexte (ICC,MPO,CD3,CD79a,CD117,BCR::ABL1,KMT2A,G6PD) dirigées vers fenêtres locales ; IA/PCR/ICANS/TNM explicités ; MPO des réponsesquiz développé pour éviter la cibleANCA.'
 ],'blocking_findings':[],'limitations':limits},
 'language':{'scope':'Texte clinique, scientifique, pharmacologique, fenêtres et cinqcas relus ; unités, temporalités, dénominateurs, titres et formulations absolues corrigés.','findings_fixed':['Intensité versus proportion de cellules distinguées','Recommandation, indication et remboursement séparés','Ponatinib : libellé suisse conservé sans ajout étranger','Espacements des dates/unités/seuils et développement des sigles ambigus'],'remaining':'Aucune garantie absolue d’absence d’erreur ; auto-relecture sans validation humaine.'},
 'visual_desktop':{'scope':'1440×900, originaux/annotations, sixsciences, fenêtres, quiz et Livre24 ; références de capture réellement inspectées ci-dessous.','mode':browser['mode'],'inspected_by':'Codex parent, vision des captures finales','captures':[name for name in visual['captures'] if '-1440-' in name]},
 'visual_mobile':{'scope':'390×844, originaux et légendes, navigation, fenêtres et Livre24 ; limites de densité et barres flottantes conservées.','mode':browser['mode'],'inspected_by':'Codex parent, vision des captures finales','captures':[name for name in visual['captures'] if '-390-' in name]},
 'captures_inspected':visual['captures'],'capture_inspection_scope':visual['scope'],
 'verification':{'windows_per_viewport':52,'dialog_overflow_checked':True,'quizzes_per_viewport':5,'science_tabs':6,'semiology_sections':9,'original_images':4,'original_occurrences':7,'non_anatomical_causal_diagrams':4,'browser_errors':browser['errors'],'limits':'Clics quiz sur zone réponse hors sous-bouton d’abréviation ; abréviation native conserve son propre clic.'}}
write(PACK/'self-review.json',review)
sources=[{'id':s['id'],'url':s['url'],'publisher':s['editeur'],'title':s['titre'],'read_at':s['date_consultation'],'section':s['section_page'],'passage':s['passage_paraphrase'],'population':s['population'],'limits':s['limites'],'reading_depth':s['niveau_lecture'],'cache_sha256':s['cache_sha256'],'reuse_attributed':s.get('reuse_attributed'),'read_in_current_session':s.get('read_in_current_session')} for s in read(OUT/'recherche_C95/sources.json')['sources']]
manifest={'code':'C95','author':'Codex Hématologie','monograph':read(OUT/'monograph-14.json')['points'],'matrix20':read(OUT/'matrix-20.json')['rubrics'],'matrix20_reference':'matrix-20.json','sources':sources,'images':images,'semiology':{'section_anchors':['c95-semio-'+s for s in ['normal','mecanisme','symptomes','signes','syndromes','examens','interpretation','gravite','synthese']]},'reviews':{kind:{'path':'review-package/self-review.json','sha256':sha(PACK/'self-review.json'),'reviewer':'Codex Hématologie','mode':'self_review'} for kind in ['medical','language','visual_desktop','visual_mobile']},'blocking_findings':[],'limitations':limits,'clinical_certification':False,'closure_status':'ready_for_project_completion_gate_and_user_review'}
write(OUT/'lesson-manifest.json',manifest);write(PACK/'lesson-manifest.json',manifest);write(OUT/'images-provenance.json',images)
write(OUT/'source-binding.json',{'code':'C95','verified_at':verify['finished_at'],'preview':'C95-apercu-autonome.html','preview_sha256':verify['preview_sha256'],'final_sources':verify['final_sources'],'checks':['verification.json','browser-report-autonomous.json','sciences-final.json','visual-inspection.json','coverage-final.md','recherche_C95/recherche.md'],'clinical_certification':False})
finding=read(OUT/'render-finding-before-final.json');finding['closed']=True;finding['resolved_at']=now;finding['final_preview_sha256']=verify['preview_sha256'];finding['resolution']='Duplication de figure retirée du dialogue ; original annoté conservé en Histologie ; débordement des52fenêtres contrôlé à1440/390.';write(OUT/'render-finding-before-final.json',finding)
print(json.dumps({'recorded_self_review':True,'manifest_sha256':sha(OUT/'lesson-manifest.json'),'preview_sha256':verify['preview_sha256'],'clinical_certification':False,'completed':False}))
