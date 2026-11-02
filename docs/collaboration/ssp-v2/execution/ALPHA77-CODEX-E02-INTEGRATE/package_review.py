"""Assembler les reçus après la relecture effective ; ne certifie pas la médecine."""
from pathlib import Path
import json, hashlib, datetime, shutil, re
R=Path.cwd(); D=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
save=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
now=datetime.datetime.now(datetime.timezone.utc).isoformat(); author='astra_endocrinologie'
stat=json.loads((D/'static-report.json').read_text()); browser=json.loads((D/'browser-report.json').read_text())
assert browser['result']=='passed' and browser['preview_sha256']==sha(D/'E02-apercu-autonome.html')
for n,h in stat['source_sha256'].items(): assert sha(R/n)==h,n
sources=json.loads((D/'source-ledger.json').read_text())['sources']
rows14=[
('Définition',['e02-1'],['S1','S10'],'Le cours distingue le profil infraclinique de son attribution iodée et sépare E02 des autres causes ; une T4 basse ne décide pas seule du code.'),
('Épidémiologie',['e02-2'],['S3','S5','S10'],'Les effectifs, médianes et méthodes suisses sont explicités avant les comparaisons européennes ; aucune prévalence suisse de E02 n’est inventée.'),
('Physiopathologie',['e02-3','e02-s-phys-cours','e02-s-bioch-cours'],['S2','S8','S10'],'La synthèse normale, le rétrocontrôle et les adaptations sont reliés aux mesures ; la carence légère ne suit pas une séquence biologique obligatoire.'),
('Démarche clinique',['e02-0','e02-7'],['S10','S13','S15'],'Le raisonnement part de la population et de son calendrier, confirme le profil puis examine les causes avant une décision nutritionnelle et thérapeutique.'),
('Anamnèse',['e02-5','e02-semio-signs'],['S4','S10','S13'],'Les plaintes sont caractérisées sans score inventé ; alimentation, compléments exacts, médicaments, grossesse et antécédents orientent les hypothèses.'),
('Examen physique',['e02-6','e02-semio-examination'],['S2','S10'],'Observation, palpation et déglutition sont décrites avec grades OMS et limites ; ni goitre ni examen normal ne suffisent à identifier la cause iodée.'),
('Syndromes',['e02-semio-interpretation','e02-e-5'],['S10','S13','S15'],'Les profils infraclinique, manifeste, central et transitoire sont distingués et reliés aux signes peu spécifiques, au contexte et aux interférences.'),
('Diagnostic positif',['e02-7','e02-e-2'],['S10','S13','S15'],'La persistance est confirmée avec normes et délais adaptés ; l’attribution iodée reste argumentée, sans imposer anticorps négatifs ni iodurie isolée.'),
('Explorations',['e02-e-1','e02-e-2','e02-e-3','e02-e-4','e02-e-5'],['S2','S5','S10','S13'],'Biologie, étiologie, marqueurs nutritionnels, indications morphologiques et pièges analytiques sont hiérarchisés sans examens de routine injustifiés.'),
('Arbre et diagnostic différentiel',['e02-7','e02-semio-differentials'],['S10','S13','S15'],'L’arbre tient compte de la grossesse et de l’âge avant les causes transitoires, auto-immunes, médicamenteuses et nutritionnelles et la décision finale.'),
('Prise en charge',['e02-9','e02-p-1','e02-p-2','e02-p-3','e02-p-4','e02-p-5'],['S6','S7','S13','S14','S15','S17'],'Correction des apports et indication hormonale sont séparées ; FI suisse exacte, doses, contre-indications, interactions et divergences européennes sont exposées.'),
('Prévention, suivi, pronostic',['e02-10','e02-11','e02-s-sante-cours'],['S2','S4','S10','S11','S13','S15'],'Le suivi dépend de la population et du traitement ; les taux de progression généraux ne sont pas imputés à E02 et la prévention collective reste distincte.'),
('Points clés',['e02-12','e02-13','e02-e-6'],['S5','S7','S13','S15','S18'],'La synthèse et quatre cas corrigés distinguent seuil, cible, population, cause et bénéfice clinique, avec explication de la décision au patient.'),
('Pièges',['e02-14','e02-semio-limits','e02-p-5'],['S2','S6','S7','S9','S13','S15'],'Les raccourcis de causalité, de grossesse, de supplément et de normalisation biologique sont corrigés ; les cas pédagogiques ne sont pas des sujets officiels.')]
rows20=[
('Question clinique suisse',['e02-0'],['S4','S5','S14']),('Définition et périmètre',['e02-1'],['S1','S10']),('Classifications',['e02-1','e02-e-5'],['S1','S10','S15']),('Épidémiologie CH puis Europe',['e02-2'],['S3','S5','S10']),('Normal et physiopathologie',['e02-3','e02-s-anat-cours','e02-s-histo-cours','e02-s-phys-cours','e02-s-bioch-cours'],['S2','S8']),('Étiologies et risques',['e02-4','e02-7'],['S4','S5','S10']),('Anamnèse',['e02-5'],['S4','S10','S13']),('Examen',['e02-6','e02-semio-examination'],['S2','S10']),('Signaux de gravité',['e02-8','e02-semio-urgency'],['S7','S11','S15']),('Explorations',['e02-e-1','e02-e-2','e02-e-3','e02-e-4','e02-e-5'],['S2','S5','S13']),('Diagnostic différentiel',['e02-7','e02-e-5'],['S10','S13']),('Traitement suisse',['e02-9','e02-p-1','e02-p-2','e02-p-3','e02-p-4','e02-p-5'],['S6','S7','S14','S17']),('Complications et pronostic',['e02-8','e02-10'],['S10','S11','S15','S22']),('Suivi et prévention',['e02-10','e02-s-sante-cours'],['S2','S4','S10','S13']),('Populations particulières',['e02-11','e02-p-3'],['S7','S11','S12','S13','S15']),('Aspects administratifs suisses',['e02-1','e02-9','e02-p-1','e02-p-5'],['S1','S6','S7','S14','S17']),('Critères et alertes',['e02-12','e02-14'],['S10','S13','S15']),('Paramètres décisifs',['e02-12','e02-13','e02-e-2','e02-e-3'],['S2','S5','S13','S15']),('Sous-codes complets',['e02-1','e02-14'],['S1']),('Examen fédéral',['e02-14','e02-e-6'],['S9','S13','S15'])]
monograph=[dict(point=i,label=t,anchor=a[0],additional_anchors=a[1:],sources=ss,coverage_explanation=ex) for i,(t,a,ss,ex) in enumerate(rows14,1)]
matrix20=[dict(point=i,label=t,status='covered',evidence=['review-inputs/E02-source.html#'+x for x in aa],source_ids=ss) for i,(t,aa,ss) in enumerate(rows20,1)]
text='\n'.join((R/n).read_text() for n in stat['source_sha256'])
for row in rows14+rows20:
 for a in row[1]: assert f'id="{a}"' in text,a
(D/'review-inputs').mkdir(exist_ok=True);(D/'review-inputs/E02-source.html').write_text(text)
save(D/'coverage-14-20.json',dict(at=now,review_mode='self_review',monograph14=monograph,medina20=matrix20,limits_are_not_missing_sections=True,clinical_certification=False))
limits=[
'Aucune prévalence contemporaine suisse de E02 ni essai thérapeutique propre à sa cause iodée n’a été retrouvé ; les données de nutrition et d’HIC générale ne les remplacent pas.',
'Plusieurs études sont lues au niveau du résumé seulement. Les recommandations ETA 2013/2014 sont datées et confrontées aux essais ultérieurs, à HAS 2022 et à RCOG 2025, correction 2026 contrôlée.',
'Les divergences HAS/RCOG sur grossesse, anticorps et suivi, ainsi que FI suisse/ETA pour espacement et cibles, sont conservées et contextualisées.',
'Le catalogue OFS local est celui de 2024 ; aucune validation administrative suisse 2026 ou prise en charge financière individuelle n’est certifiée.',
'L’image historique montre une anatomie et une histologie normales ; aucune signature anatomique propre à E02 n’est inventée. Une seule image originale est utilisée dans deux onglets.',
'La figure 2013 a une preuve CC BY 3.0 propre à cette version ; la licence du manuel OpenStax actuel n’est pas extrapolée.',
'Les contrôles de navigateur utilisent une origine interceptée et les octets exacts de la copie autonome ; aucun serveur HTTP réel ni site publié n’est testé.',
'La coque native conserve son bandeau provisoire de contre-audit. Les quatre reçus sont des auto-relectures explicites par intelligence artificielle, sans examen indépendant ni certification humaine.',
'La navigation vers les autres leçons est héritée ; seuls le contenu et les interactions E02 sont revus. Le build signale trois éléments E05 non couverts, hors périmètre et réservation E02.'
]
findings=[dict(id=f'L{i:02}',blocking=False,finding=t) for i,t in enumerate(limits,1)];save(D/'remaining-findings.json',findings)
checks=[
('Profil biologique, attribution iodée et code distingués ; anticorps négatifs non obligatoires et iodurie isolée non diagnostique.',['S1','S2','S10','S13']),
('Enquête suisse : 362 enfants, 513 grossesses et 473 urines distingués ; T4 totale mesurée sur sang séché, pas T4 libre ; 127/97 µg/L et un cas HIC contextualisés.',['S5']),
('Pourcentages d’apport inadéquat estimés selon seuils, groupes et méthode ; association de supplément non interprétée comme preuve de guérison.',['S5']),
('Adaptation iodée possible avec TSH/T4 normales ; aucune séquence Tg puis TSH puis T4 obligatoire.',['S2','S8']),
('Confirmation adulte stable distincte de grossesse et préconception ; seuil diagnostique 4 contextuel distinct de cible 2,5.',['S10','S13','S15']),
('HAS et RCOG comparés sur décision légère, anticorps, TSH/T4, calendrier et post-partum ; hypothyroïdie sévère non différée.',['S7','S13','S15','S16']),
('Histoire naturelle pédiatrique rapportée avec populations et limites ; normes par âge et filière spécialisée sans transposition automatique des doses adultes.',['S7','S11','S12']),
('TRUST : 737 adultes d’au moins 65 ans, TSH moyenne 6,4 ; absence de bénéfice symptomatique non généralisée à toute grossesse ou TSH supérieure à 10.',['S18','S19']),
('Évaluation OFSP : 22 études/28 articles et scénarios économiques distingués de dépenses constatées ou décision individuelle de remboursement.',['S14']),
('FI Euthyrox exacte : autorisation et GTIN séparés, doses, titration, contre-indications cardiaques/surrénaliennes, interactions et fréquences non déterminables.',['S7']),
('FI et ETA : délai calcium/fer distingué ; IPP par pH non résolu automatiquement par simple espacement ; suivi individualisé.',['S7','S10']),
('Elevit Pronatal : composition du produit suisse exact sans iode ; iodure de potassium 65 mg réservé à la radioprotection et jamais utilisé comme complément.',['S6','S17']),
('OMS : doses de programme pour accès insuffisant au sel iodé, pas supplément universel à ajouter au besoin total ; sources OSAV et RCOG contextualisées.',['S2','S4','S15']),
('Fenêtres anti-TPO, HAS, HTA et T4 précisées localement pour éviter les collisions du glossaire partagé ; résumés Pareto harmonisés.',['S8','S13','S14']),
('Figure originale et licence de sa version vérifiées ; annotations HTML sur isthme, région parathyroïdienne et colloïde sans altérer les pixels.',['S8']),
('PROFILES utilisé comme rapprochement pédagogique ; quatre vignettes fictives, aucune question officielle revendiquée.',['S9'])]
common=dict(reviewer=author,author=author,mode='self_review',reviewed_at=now,source_sha256=stat['source_sha256'],review_html_sha256=sha(D/'E02-apercu-autonome.html'),human_validation=False,independent=False,score=None,blocking_findings=0,remaining_limits=findings)
reviews={'medical':dict(**common,kind='medical',scope='Auto-relecture des six HTML, fenêtres, tableaux, résumés, cas et figures, comparés aux passages identifiés dans le ledger.',checks=[dict(finding_and_resolution=t,source_ids=ss,state='checked_by_author') for t,ss in checks]),'language':dict(**common,kind='language',scope='Auto-relecture française de toutes les surfaces E02.',checks=['Causalité, degrés de recommandation et populations explicités.','Erreurs de préposition iodure corrigées et titres Pareto développés.','Code E01.8 distingué de son inclusion ; limite diagnostique et cible différenciées.','Unités, dates, auteurs, références, légendes, fenêtres et résumés harmonisés sans réduction de profondeur.'])}
for kind,w in [('visual_desktop',1440),('visual_mobile',390)]:
 names=[f'{w}-'+x+'.png' for x in ['normal-anatomy','histology','clinical-diagram','e02-s-semio-diagram-0','e02-s-phys-diagram-0','e02-s-phys-diagram-1','e02-s-bioch-diagram-0','e02-s-sante-diagram-0','euthyrox-popup','antitpo-popup','opening','semiology','examinations','font24-pharmacology','book24-pharmacology']]
 if w==390:names.append('390-font24-table-right.png')
 reviews[kind]=dict(**common,kind=kind,scope='Inspection visuelle des captures listées, complétée par les interactions automatisées.',captures={n:sha(D/n) for n in names},checks=['Les deux occurrences de l’original sont décodées après défilement ; trois repères HTML et attributions sont visibles.','Les six schémas logiques sont distincts des images anatomiques ; aucune anatomie générée.','Tableau défilable horizontalement à taille 24, sans débordement global du document.','Six disciplines, neuf sections sémiologiques, 61 fenêtres accessibles, quatre quiz, Navigo, Entrée/Espace et stockage Livre 24 contrôlés.'],browser_report_sha256=sha(D/'browser-report.json'),browser_mode=browser['mode'])
(D/'reviews').mkdir(exist_ok=True)
for k,v in reviews.items():save(D/'reviews'/f'{k}.json',v)
src=R/'assets/img/e02/alpha/codex/e02-thyroide-normale-openstax2013.jpg';(D/'figures').mkdir(exist_ok=True);dst=D/'figures'/src.name;shutil.copyfile(src,dst)
images=[dict(path=str(dst.relative_to(D)),sha256=sha(dst),original_url='https://commons.wikimedia.org/wiki/File:1811_The_Thyroid_Gland.jpg',author='OpenStax College ; micrographie University of Michigan Medical School 2012',license='CC BY 3.0, version Connexions 19 juin 2013 et métadonnées Commons propres à cette image',license_proof='figure-openstax2013-license-metadata.json',annotations='Isthme antérieur, région parathyroïdienne postérieure et colloïde folliculaire ; repères HTML ajoutés, pixels originaux inchangés.',medical_review=dict(mode='self_review',reviewer=author,proof='reviews/medical.json',human_validation=False))]
fi=json.loads((D/'figure-integrity.json').read_text());fi.update(visual_review='Original et deux occurrences rendues inspectés à 1440 et 390 après défilement et décodage ; repères HTML conformes.',reviewed_at=now,proofs=['reviews/visual_desktop.json','reviews/visual_mobile.json']);save(D/'figure-integrity.json',fi)
manifest=dict(schema_version=1,code='E02',lesson='E02',author=author,base_sha=stat['base_sha'],monograph=monograph,matrix20=matrix20,sources=sources,images=images,semiology=dict(section_anchors=['e02-semio-'+x for x in ['normal','signs','mechanisms','examination','interpretation','differentials','urgency','limits','sources']]),blocking_findings=0,remaining_findings=findings,reviews={k:dict(path='reviews/'+k+'.json',reviewer=author,mode='self_review',sha256=sha(D/'reviews'/f'{k}.json')) for k in reviews},source_files_sha256=stat['source_sha256'],preview=dict(path='E02-apercu-autonome.html',sha256=sha(D/'E02-apercu-autonome.html'),browser_report='browser-report.json',native_bundle='E02-apercu-autonome.bundle.json'),clinical_certification=False,publication_to_main=False,tokens_actual=None,cost_actual=None)
save(D/'lesson-manifest.json',manifest)
save(D/'source-binding.json',dict(code='E02',verified_at=now,preview='E02-apercu-autonome.html',preview_sha256=sha(D/'E02-apercu-autonome.html'),final_sources={**stat['source_sha256'],'glossary/e02.py':sha(R/'glossary/e02.py'),**stat['original_images_sha256']},checks=['static-report.json','audit-sciences.json','browser-report.json','coverage-14-20.json','source-ledger.json','lesson-manifest.json','reviews/medical.json','reviews/language.json','reviews/visual_desktop.json','reviews/visual_mobile.json'],clinical_certification=False))
print('E02 : 14 points, 20 rubriques, 24 sources paraphrasées, un original et quatre auto-relectures traçables.')
