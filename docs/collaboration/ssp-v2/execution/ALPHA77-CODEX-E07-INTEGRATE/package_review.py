"""Reçus de relecture effective ; exécuter après inspection visuelle finale."""
from pathlib import Path
import json,hashlib,datetime,shutil,re
R=Path.cwd();D=Path(__file__).resolve().parent;sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();save=lambda n,x:(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
now=datetime.datetime.now(datetime.timezone.utc).isoformat();author='astra_endocrinologie';stat=json.loads((D/'static-report.json').read_text());browser=json.loads((D/'browser-report.json').read_text());assert browser['result']=='passed';assert browser['preview_sha256']==sha(D/'E07-apercu-autonome.html')
for n,h in stat['source_sha256'].items():assert sha(R/n)==h,n
sources=json.loads((D/'source-ledger.json').read_text())['sources']
rows14=[
('Définition',['e07-1'],['S1','S2'],'Cinq raisonnements cliniques sont distingués dans les quatre sous-codes, sans traitement unique de la catégorie.'),
('Épidémiologie',['e07-2'],['S3','S7','S20'],'Dépistage suisse et fréquence institutionnelle sont séparés des populations européennes, séries opératoires et familles sélectionnées.'),
('Physiopathologie',['e07-3','e07-s-physio-cours','e07-s-bioch-cours'],['S3','S6','S16','S17','S42'],'Synthèse, transport lié, action cellulaire, calcitonine et effet de masse relient normalité et perturbation.'),
('Démarche clinique',['e07-0','e07-7'],['S3','S5','S16','S32'],'Le contexte, la gravité et la méthode précèdent le classement, les tests spécialisés et la décision.'),
('Anamnèse',['e07-5','e07-semio-signs'],['S3','S6','S13','S21a'],'Motif, temporalité, symptômes, médicaments, famille, audition et gestes cervicaux orientent les hypothèses.'),
('Examen physique',['e07-6','e07-semio-examination'],['S3','S5','S37'],'Respiration, cou, ganglions, audition et développement sont examinés avec limites de la palpation.'),
('Syndromes',['e07-13','e07-semio-interpretation'],['S3','S6','S16','S17'],'Hypercalcitoninémie, défaut de synthèse, transport, maladie critique et lésion cervicale gardent leurs concordances distinctes.'),
('Diagnostic positif',['e07-7','e07-12'],['S3','S5','S16','S36'],'La confirmation biologique, histologique ou génétique dépend du mécanisme ; ni perchlorate positif ni TSH élevée ne sont universels.'),
('Explorations',['e07-e-1','e07-e-2','e07-e-3','e07-e-4','e07-e-5'],['S3','S5','S8','S32','S33'],'Examens hiérarchisés, normes de laboratoire, performances avec populations, préanalytique et interférences sont explicités.'),
('Arbre et diagnostic différentiel',['e07-7','e07-semio-differentials'],['S5','S6','S16','S36'],'Le schéma calcitonine complète les branches synthèse, transport et maladie critique ; les urgences passent en premier.'),
('Prise en charge',['e07-9','e07-p-1','e07-p-2','e07-p-3','e07-p-4','e07-p-5','e07-p-6'],['S3','S19','S34','S35'],'Objectifs, produit exact, doses, divergence FI/consensus, contre-indications, interactions et calcium hors indication sont reliés au mécanisme.'),
('Prévention, suivi, pronostic',['e07-10','e07-11'],['S3','S4','S16','S19'],'Délais de contrôle, audition, goitre, famille et populations particulières sont couverts sans extrapoler les petites séries.'),
('Points clés',['e07-12','e07-13','e07-e-6'],['S3','S5','S16','S19'],'Synthèse syndromique, paramètres contextualisés, communication au patient et quatre cas corrigés organisent la décision.'),
('Pièges',['e07-14','e07-semio-limits','e07-p-6'],['S5','S8','S16','S19','S37'],'Seuils, unités, causalité, diagnostic concomitant, génétique et nodule nécrotique sont explicitement bornés.')]
rows20=[
('Question clinique suisse',['e07-0'],['S19','S32','S33']),('Définition et périmètre',['e07-1'],['S1','S2']),('Classifications',['e07-1','e07-e-4'],['S1','S2','S3']),('Épidémiologie CH puis Europe',['e07-2'],['S3','S7','S20']),('Normal et mécanismes',['e07-3','e07-s-anat-cours','e07-s-histo-cours','e07-s-physio-cours','e07-s-bioch-cours'],['S3','S6','S16','S42']),('Étiologies et risques',['e07-4','e07-s-gene-cours'],['S3','S6','S16','S41']),('Anamnèse',['e07-5'],['S3','S6','S13']),('Examen',['e07-6','e07-semio-examination'],['S3','S37']),('Signaux de gravité',['e07-8','e07-semio-urgency'],['S21a','S21c','S25','S26']),('Explorations',['e07-e-1','e07-e-2','e07-e-3','e07-e-4','e07-e-5'],['S3','S5','S8','S32','S33']),('Diagnostic différentiel',['e07-7','e07-semio-differentials'],['S6','S16','S36']),('Traitement suisse',['e07-9','e07-p-1','e07-p-2','e07-p-3','e07-p-4','e07-p-5','e07-p-6'],['S3','S19','S34','S35']),('Complications et pronostic',['e07-8','e07-9','e07-10'],['S3','S16','S21c','S38']),('Suivi et prévention',['e07-10'],['S3','S4','S19','S20']),('Populations particulières',['e07-11','e07-p-5','e07-semio-limits'],['S3','S19']),('Aspects administratifs suisses',['e07-1','e07-14','e07-p-5','e07-p-6'],['S1','S19','S34','S35']),('Critères et alertes',['e07-12','e07-14'],['S3','S5','S16']),('Paramètres décisifs',['e07-12','e07-e-2','e07-e-3','e07-p-2'],['S3','S7','S8','S19']),('Sous-codes complets',['e07-1','e07-9'],['S1','S2','S38','S39','S40']),('Examen fédéral',['e07-14','e07-e-6'],['S37'])]
text='\n'.join((R/n).read_text() for n in stat['source_sha256'])
for row in rows14+rows20:
 for a in row[1]:assert f'id="{a}"' in text,a
(D/'review-inputs').mkdir(exist_ok=True);(D/'review-inputs/E07-source.html').write_text(text)
monograph=[dict(point=i,label=t,anchor=a[0],additional_anchors=a[1:],sources=ss,coverage_explanation=ex) for i,(t,a,ss,ex) in enumerate(rows14,1)]
matrix20=[dict(point=i,label=t,status='covered',evidence=['review-inputs/E07-source.html#'+x for x in aa],source_ids=ss) for i,(t,aa,ss) in enumerate(rows20,1)]
save('coverage-14-20.json',dict(at=now,review_mode='self_review',monograph14=monograph,medina20=matrix20,limits_are_not_missing_sections=True,clinical_certification=False))
limits=[
'Pas de recommandation suisse unique E07, de prévalence suisse globale, de score commun ni de seuil opérationnel suisse de rappel néonatal dans les sources lues ; ces absences sont explicitées, pas remplacées par une valeur inventée.',
'Plusieurs formes rares reposent sur des résumés, cas ou petites séries. Les données américaines d’anatomopathologie décrivent des observations ; aucune recommandation américaine directe ne fonde la conduite.',
'La synthèse britannique NEM2 reprend notamment une classification ATA ; elle est attribuée et ne remplace pas une décision de centre expert selon variant et famille.',
'Le calcium B. Braun est un produit allemand importé selon PHEL. Le RCP exact lu date de juillet 2014 ; le test diagnostique est hors indication et le protocole de la série italienne ne se transpose pas automatiquement.',
'Les seuils de calcitonine, performances de procalcitonine, fréquences de TBG et statistiques génétiques restent liés à leur méthode et population ; aucune validation universelle ne leur est attribuée.',
'Le catalogue suisse local est celui de 2024 ; aucune certification du codage ou remboursement individuel 2026. PROFILES 2017 sert de rapprochement pédagogique, sans question officielle ou garantie d’examen.',
'Les deux figures originales montrent une thyroïde normale et un goitre compressif adulte ; elles ne diagnostiquent ni hyperplasie C, ni Pendred, ni obstruction néonatale. La licence OpenStax historique est prouvée pour l’image 2013, indépendamment du manuel actuel.',
'Les tests navigateur emploient une origine HTTPS interceptée et les octets exacts de la copie autonome, avec les autres requêtes bloquées ; aucun serveur HTTP réel ou déploiement main n’est testé.',
'La coque native conserve son statut provisoire et sa navigation héritée. Seul E07 est relu ; trois éléments E05 non couverts signalés au build sont hors périmètre.',
'Relectures médicales, linguistiques et visuelles effectuées par le même auteur IA en mode self_review ; aucune revue indépendante ou certification humaine revendiquée.'
]
findings=[dict(id=f'L{i:02}',blocking=False,finding=t) for i,t in enumerate(limits,1)];save('remaining-findings.json',findings)
checks=[
('Sources CH de produit, laboratoire et dépistage confrontées aux références européennes ; passages publics paraphrasés et résumés identifiés.',['S19','S20','S32','S33','S35']),
('Calcitonine à 40 pg/ml chez la femme : seuil ETA dépassé ; IPP/tabac ne prouvent pas une cause bénigne. Références de laboratoire et seuils opératoires distingués.',['S5','S6','S32','S33']),
('Cochrane : faible VPP contextualisée par prévalence et biais ; pas application à tout niveau de calcitonine.',['S7']),
('Calcium : série 135/47, méthode Immulite 2000, RET exclus ; 9 % de nouvelles bradycardies distincts de 25,4 % après test ; RCP exact et hors indication explicites.',['S8','S34','S35']),
('Procalcitonine : facteurs non infectieux conservés, 396 patients opérés/44 cancers ; 45,9 % de cytologies diagnostiques porte sur 85 patients ponctionnés parmi 104.',['S6','S9','S10','S23']),
('RET identifie une prédisposition, pas une hyperplasie histologique ; âge opératoire attribué au document NHS avec limites.',['S4','S11','S12']),
('Dyshormonogenèse : perchlorate parfois négatif, phénotypes variables, génétique non préalable à la substitution ; dose selon FT4 et contrôle au plus tard une semaine dès 50 µg/j initiaux.',['S3']),
('FI Euthyrox exacte : 0–6 mois 10 µg/kg, non faux intervalle 10–15 ; doses consensus séparées ; contre-indications, interactions, grossesse et fréquences non déterminables vérifiées.',['S19','S3']),
('NTIS : TSH normale ne suffit pas à exclure une hypothyroïdie ; DIO2/DIO3 dépendent des tissus ; reverse-T3 non discriminante isolément ; pas substitution systématique.',['S16','S22']),
('TBG : déficit, faible affinité et excès distingués ; hypothyroïdie coexistante reste à traiter ; fréquences historiques non estimées par quatre cas.',['S17','S18','S36','S41']),
('Hémorragie et infarctus : voies aériennes prioritaires ; observation seulement dans cas stable ; nécrose post-ponction ne prouve pas guérison.',['S21a','S21c','S38','S39','S40']),
('Pendred : phénotype variable, 13/37 sélectionnés non rendement universel ; données de cancer très faibles ; audition et conseil explicités.',['S13','S14','S15','S28','S29','S30']),
('Homonymes TPO/RCP/CMT/AA/T2/TH/IC/IA corrigés localement ; hormones et TBG ont leurs fenêtres contextuelles. Les six sciences et neuf sémiologies relient mécanisme, signe, examen et traitement.',['S3','S16']),
('Deux originaux licenciés inspectés, sans retouche de pixels ; repères anatomiques et cinq schémas logiques relus.',['S3','S6','S16','S42'])]
common=dict(reviewer=author,author=author,mode='self_review',reviewed_at=now,source_sha256=stat['source_sha256'],review_html_sha256=sha(D/'E07-apercu-autonome.html'),human_validation=False,independent=False,score=None,blocking_findings=0,remaining_limits=findings)
reviews={'medical':dict(**common,kind='medical',scope='Auto-relecture de toutes les surfaces E07, sources, tableaux, figures, cas, fenêtres et résumés ; portée de lecture indiquée dans le ledger.',checks=[dict(finding_and_resolution=t,source_ids=ss,state='checked_by_author') for t,ss in checks]),'language':dict(**common,kind='language',scope='Auto-relecture française des six fichiers, textes visibles et fenêtres.',checks=['Raccourcis d’exclusion, causalité et généralisation corrigés.','Cinq groupes cliniques harmonisés, titres diagnostiques et phrases répétitives corrigés.','Population, méthode, unités et degré de preuve conservés dans les synthèses.','Terminologie de transport, précurseurs, TPO et NTIS explicitée sans réduire les sujets existants.'])}
visual=json.loads((D/'visual-inspection.json').read_text());assert visual['preview_sha256']==sha(D/'E07-apercu-autonome.html')
for kind,w in [('visual_desktop',1440),('visual_mobile',390)]:
 names=[n for n in visual['captures'] if n.startswith(str(w)+'-')];assert names
 reviews[kind]=dict(**common,kind=kind,scope='Captures effectivement inspectées par l’auteur, plus interactions automatisées.',captures={n:sha(D/n) for n in names},checks=visual['findings'],browser_report_sha256=sha(D/'browser-report.json'),browser_mode=browser['mode'])
(D/'reviews').mkdir(exist_ok=True)
for k,v in reviews.items():save('reviews/'+k+'.json',v)
(D/'figures').mkdir(exist_ok=True);images=[]
figdefs=[('e07-thyroide-normale-openstax2013.jpg','https://commons.wikimedia.org/wiki/File:1811_The_Thyroid_Gland.jpg','OpenStax College ; micrographie University of Michigan Medical School 2012','CC BY 3.0, version Connexions 2013','figure-openstax2013-license-metadata.json','Isthme, anneaux trachéaux, colloïde et épithélium folliculaire ; quatre repères HTML.'),('e07-goitre-compressif-original.jpg','https://commons.wikimedia.org/wiki/File:Goitre_compressif_sur_la_trach%C3%A9e_(sagittal).jpg','Stockholm, 18 août 2016','CC BY-SA 4.0, y compris annotations proposées','figure-license-metadata.json','Lumière trachéale rétrécie et masse antérieure ; deux repères HTML, flèche rouge originale conservée.')]
for name,url,owner,license,proof,annotations in figdefs:
 src=R/'assets/img/e07/alpha/codex'/name;dst=D/'figures'/name;shutil.copyfile(src,dst)
 images.append(dict(path=str(dst.relative_to(D)),sha256=sha(dst),original_url=url,author=owner,license=license,license_proof=proof,annotations=annotations,medical_review=dict(mode='self_review',reviewer=author,proof='reviews/medical.json',human_validation=False)))
save('figure-integrity.json',dict(at=now,images=images,image_occurrences=3,pixels_edited=False,anatomy_generated=False,logical_schemes=5,visual_review='Trois occurrences décodées après défilement et inspectées à 1440 et 390 ; repères HTML et légendes relus.',proofs=['browser-report.json','visual-inspection.json','reviews/visual_desktop.json','reviews/visual_mobile.json'],clinical_certification=False))
manifest=dict(schema_version=1,code='E07',lesson='E07',author=author,base_sha=stat['base_sha'],monograph=monograph,matrix20=matrix20,sources=sources,images=images,semiology=dict(section_anchors=['e07-semio-'+x for x in ['normal','signs','mechanisms','examination','interpretation','differentials','urgency','limits','sources']]),blocking_findings=0,remaining_findings=findings,reviews={k:dict(path='reviews/'+k+'.json',reviewer=author,mode='self_review',sha256=sha(D/'reviews'/f'{k}.json')) for k in reviews},source_files_sha256=stat['source_sha256'],preview=dict(path='E07-apercu-autonome.html',sha256=sha(D/'E07-apercu-autonome.html'),browser_report='browser-report.json',native_bundle='E07-apercu-autonome.bundle.json'),clinical_certification=False,publication_to_main=False,tokens_actual=None,cost_actual=None)
save('lesson-manifest.json',manifest)
save('source-binding.json',dict(code='E07',verified_at=now,preview='E07-apercu-autonome.html',preview_sha256=sha(D/'E07-apercu-autonome.html'),final_sources={**stat['source_sha256'],'glossary/e07.py':sha(R/'glossary/e07.py'),**stat['original_images_sha256']},checks=['static-report.json','audit-sciences.json','browser-report.json','abbreviation-browser-report.json','glossary-context-report.json','figure-capture-report.json','coverage-14-20.json','source-ledger.json','lesson-manifest.json','reviews/medical.json','reviews/language.json','reviews/visual_desktop.json','reviews/visual_mobile.json'],clinical_certification=False))
print('E07 : 14/20, 42 sources, deux originaux, quatre auto-relectures traçables.')
