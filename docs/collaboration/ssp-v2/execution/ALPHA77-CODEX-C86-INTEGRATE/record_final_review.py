#!/usr/bin/env python3
"""Consigner l'auto-relecture effectuée sur les empreintes finales contrôlées.

Exécuter seulement après inspection réelle des captures finales par l'auteur.
Le script ne réalise pas de revue médicale et ne publie ni ne clôture le cours.
"""
from pathlib import Path
import json,hashlib,datetime,shutil,re
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[4]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
verify=json.loads((OUT/'verification.json').read_text())
assert verify.get('ok') and all(c['exit_code']==0 for c in verify['checks'])
for name,expected in verify['final_sources'].items():assert sha(ROOT/name)==expected,name
assert sha(OUT/'C86-apercu-autonome.html')==verify['preview_sha256']
browser=json.loads((OUT/'browser-report-autonomous.json').read_text())
assert not browser['errors']
for v in browser['viewports']:
 assert len(v['windows_checked'])==52 and len(v['quiz_checked'])==5
 assert v['horizontal_overflow']==v['book_overflow']==0
 assert v['book_font']=='24px' and len(v['originals_checked'])==4
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
PACK=OUT/'review-package';PACK.mkdir(exist_ok=True)
content='\n'.join((ROOT/f'chapters/C86/C86_{x}.html').read_text() for x in ('a','b','c','d','pop1','pop2'))
(PACK/'content.html').write_text(content)
limitations=[
 'Incidence suisse contemporaine par sous-code C86 non établie ; proportion suisse secondaire de2021 et cohortes étrangères datées.',
 'Correspondance CIM-10-GM2024 consultée ; aucune certification exhaustive du codage suisse2026.',
 'Limitations LS et remboursement individuels2026 non certifiés ; statut suisse de plusieurs options de rechute et disponibilité crisantaspase à vérifier.',
 'Les trois FI principales et stratégies de sociétés savantes ne constituent pas les protocoles complets de tous les cytotoxiques ni de tous les immunosuppresseurs.',
 'Repères HUG2019 adultes, pas normes nationales universelles ; population pédiatrique et grossesse non extrapolées.',
 'Lectures ciblées et résumé Gayden explicités ; ICC original non relu intégralement ; aucune certification médicale humaine ou audit indépendant prétendu.',
 'Prévisualisation native testée sur origine HTTP interceptée et réseau externe bloqué ; ouverture réelle file:// bloquée par politique administrateur, pas de test file:// revendiqué.',
 'Bandeau historique de publication provisoire et compteurs globaux du moteur conservés ; ils ne représentent pas les clôtures de cette campagne sur branches.'
]
limits=[{'id':f'C86-L{i}','text':t,'blocking':False} for i,t in enumerate(limitations,1)]
images=[]
for name,url,article,author,caption,reading in [
 ('tse2022-figure1-original.jpg','https://media.springernature.com/full/springer-static/image/art%3A10.1186%2Fs13045-022-01293-5/MediaObjects/13045_2022_1293_Fig1_HTML.jpg','https://jhoonline.biomedcentral.com/articles/10.1186/s13045-022-01293-5','Tse et al., Journal of Hematology & Oncology2022','Figure1 : manifestations orbitales/palatines, laryngées et cutanées de cas ENKTL, panneauxA–G.','Lettres et flèches originales comparées au texte éditeur : noir orbite, blanc palais ;D menace laryngée ;E/F foyers cutanés ;C/G évolution illustrative. Aucun résultat individuel garanti.'),
 ('who2022-figure7-original.png','https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41375-022-01620-2/MediaObjects/41375_2022_1620_Fig7_HTML.png','https://www.nature.com/articles/s41375-022-01620-2','Alaggio et al., Leukemia2022','Figure7 : architectures des trois types de lymphomes TFH nodaux, A angio-immunoblastique, B folliculaire avec insertPD1, C sans autre spécification.','Architecture originale A/B/C vérifiée avec légende ; A correspond à C86.5, B/C comparatifs distincts. Ne pas présenter le marquagePD1 comme diagnostic suffisant.')]:
  src=ROOT/'assets/img/c86/alpha/codex'/name;dst=PACK/name;shutil.copyfile(src,dst)
  images.append({'path':'review-package/'+name,'source_path':str(src.relative_to(ROOT)),'original_url':url,'article_url':article,'author':author,'license':'CC BY4.0','license_url':'https://creativecommons.org/licenses/by/4.0/','license_scope':'Licence de l’article et figure sans crédit excluant sa réutilisation, vérifiées sur éditeur.','sha256':sha(src),'caption_original_paraphrase':caption,'changes':'Original bytes unchanged; French explanatory caption linked to original panel letters/arrows.','annotations':'Légende française visible reliant les lettres et flèches originales aux structures, mécanismes et limites cliniques.','medical_review':'Auto-relecture Codex du02.11.2026 : '+reading,'clinical_certification':False})
review={'author':'Codex Hématologie','reviewer':'Codex Hématologie','mode':'self_review','reviewed_at':now,'source_sha256':verify['final_sources'],'preview_sha256':verify['preview_sha256'],'clinical_human_certification':False,
 'medical':{'scope':'Plan monographique complet, vingt rubriques, sources/figures et corrections confrontés aux passages effectivement lus ; auto-relecture, non validation humaine.',
 'findings_fixed':[
 'Sept sous-codes et plusieurs entités ; BPDCN classé dendritique/histiocytaire, pas lymphome NK.',
 'ENKTL : lignée NK typique non obligatoire ; EBER/CD56 ne suffisent pas hors morphologie ; leucémieNK agressive distincte.',
 'Thiopurines : population hommes<35ans, pas risque annuel, pas causalité démontrée du ratio ni arrêt automatique aprèsdeuxans.',
 'RCD-II : symptômes/atrophie après≥12mois et autres causes exclues, seuil cytométrie≥20% contextualisé ; MEITL distinct et risque non transposé à toute maladiecœliaque.',
 'Panniculitelupique, SPTCL, gamma-delta cutané et traitement immunosuppresseur sansHLH explicités ; HAVCR2 noncondition pour agir.',
 'HLH : critères relus et limites adultes ; infection/tumeur, organes et immunomodulation peuvent être traités en parallèle sans attendre cinq critères si gravité.',
 'Clonalité, marqueurs TFH/pDC et architecture intégrés ; mPIT remplace moelle parKi67 ; pas répartitionHSTL totalisant105%.',
 'Greffes : allogreffe premièreligne possible HSTL/BPDCN ; autogreffe EATL sansdonneur ; séries sélectionnées nonrandomisées.',
 'ENKTL : radiothérapie seule possible dans certaines formeslocalisées ; DeVIC necontientpas asparaginase ; dosesLLA Oncaspar séparées des protocolesENKTL.',
 'Adcetris : indication cutanée exacte, G-CSF, bléomycine contre-indiquée, LEMP et adaptations mono/CHP distinctes.',
 'Elzonris : seuil première dose versus surveillance, µg/mg, dénominateurs225/89 et grossesse ; médianeJ6 nonfin du risque.',
 'SuiviPTCL arrêt3/5ans conditionnel à rémissioncontinue asymptomatique ; RCD-II contrôles à considérer avec imagerie si signes ; LyPàvie.',
 'PROFILES2017 et examen2026 distincts dePROFILES2/examen2028 ; SSP159/227 du bandeau relues et cohérentes, autresportesd’entrée explicitées.'
 ],'blocking_findings':[],'limitations':limits},
 'language':{'scope':'Titres, sections, tableaux, fenêtres, quizz et synthèses relus ; correction des absolus, dénominateurs et temporalités sans modifier les termes du moteur.','findings_fixed':['Formulations diagnostiques trop automatiques','Proportion, risque absolu, odds ratio et causalité distingués','Unité/dose/population répétées aux endroits de décision','Suppression des lacunes héritées devenues documentées, conservation des vraies limites'],'remaining':'Aucune garantie d’absence absolue d’erreur ; sources et portée de chaque lecture explicites.'},
 'visual_desktop':{'scope':'1440×900, navigation native, quatreoccurrences d’originaux et légendes, sixsciences, fenêtres, quiz et Livre24.','mode':browser['mode'],'captures':[p for v in browser['viewports'] if v['width']==1440 for p in v['screenshots']],'inspected_by':'Codex, vision des captures finales et comparaison aux originaux, pas validation humaine'},
 'visual_mobile':{'scope':'390×844, lisibilité/retouràlaligne, figures/légendes, navigation et Livre24 ; aucun débordement horizontal constaté.','mode':browser['mode'],'captures':[p for v in browser['viewports'] if v['width']==390 for p in v['screenshots']],'inspected_by':'Codex, vision des captures finales, pas validation humaine'},
 'verification':{'windows_per_viewport':52,'quizzes_per_viewport':5,'science_tabs':6,'semiology_sections':9,'original_images':2,'original_occurrences':4,'non_anatomical_causal_diagrams':2,'browser_errors':browser['errors'],'limits':'Clics quiz sur zone réponse sans sous-bouton d’abréviation ; cliquer une abréviation ouvre sa définition native.'}}
write(PACK/'self-review.json',review)
review['captures_inspected']=[f'captures/C86-{width}-{suffix}.png' for width in (1440,390) for suffix in ('semio','popup','livre24','c86-s-semio-complete','c86-s-histo-complete','c86-s-bio-causal','c86-s-gen-causal')]
review['capture_inspection_scope']='14 captures finales inspectées visuellement ; 28 générées. Les quatre occurrences des deux originaux ont aussi été décodées dans le navigateur. Les captures longues peuvent inclure les barres flottantes natives ; les originaux non modifiés sont conservés séparément.'
write(PACK/'self-review.json',review)
source_data=json.loads((OUT/'recherche_C86/sources.json').read_text())['sources']
sources=[{'id':s['id'],'url':s['url'],'publisher':s['editeur'],'read_at':s['date_consultation'],'section':s['section_page'],'passage':s['passage_paraphrase'],'population':s['population'],'limits':s['limites'],'reading_depth':s['niveau_lecture'],'cache_sha256':s['cache_sha256']} for s in source_data]
manifest={'code':'C86','author':'Codex Hématologie','monograph':json.loads((OUT/'monograph-14.json').read_text())['points'],'sources':sources,'images':images,'semiology':{'section_anchors':['c86-semio-'+k for k in ['normal','signs','mechanisms','examination','interpretation','differentials','urgency','limits','sources']]},'reviews':{k:{'path':'review-package/self-review.json','sha256':sha(PACK/'self-review.json'),'reviewer':'Codex Hématologie','mode':'self_review'} for k in ['medical','language','visual_desktop','visual_mobile']},'blocking_findings':[],'clinical_certification':False,'closure_status':'ready_for_project_completion_gate_and_user_review','matrix20':json.loads((OUT/'matrix-20.json').read_text())['rubrics'],'matrix20_reference':'matrix-20.json','limitations':limits}
write(OUT/'lesson-manifest.json',manifest);write(PACK/'lesson-manifest.json',manifest);write(OUT/'images-provenance.json',images)
binding={'code':'C86','verified_at':verify['finished_at'],'preview':'C86-apercu-autonome.html','preview_sha256':verify['preview_sha256'],'final_sources':verify['final_sources'],'checks':['verification.json','browser-report-autonomous.json','sciences-final.json','recherche_C86/recherche.md'],'clinical_certification':False}
write(OUT/'source-binding.json',binding)
print(json.dumps({'recorded_self_review':True,'manifest_sha256':sha(OUT/'lesson-manifest.json'),'preview_sha256':verify['preview_sha256'],'clinical_certification':False,'completed':False}))
