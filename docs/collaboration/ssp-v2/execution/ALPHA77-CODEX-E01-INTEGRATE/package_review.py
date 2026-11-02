from pathlib import Path
import json,hashlib,datetime,shutil,re
R=Path.cwd(); D=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
save=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
now=datetime.datetime.now(datetime.timezone.utc).isoformat();author='astra_endocrinologie'
stat=json.loads((D/'static-report.json').read_text()); browser=json.loads((D/'browser-report.json').read_text())
assert browser['result']=='passed' and browser['preview_sha256']==sha(D/'E01-apercu-autonome.html')
for n,h in stat['source_sha256'].items():assert sha(R/n)==h
raw=json.loads((D/'recherche_E01/sources.json').read_text())['sources']
paraphrases={
'S1':'Le catalogue français distingue goitre diffus, multinodulaire, non précisé et autres affections liées à une carence iodée. Une maladie nodulaire sans cause iodée établie ne suffit pas à affirmer E01.',
'S4':'Le guide distingue besoins nutritionnels, indicateurs collectifs et fonction individuelle. Il décrit la palpation, les grades de goitre, les médianes urinaires et la thyroglobuline ; leurs limites méthodologiques restent essentielles.',
'S5':'Deux populations danoises différant modestement par leur apport iodé présentaient des incidences différentes d’hyperthyroïdie et d’hypothyroïdie. Ces taux historiques ne sont pas des taux suisses contemporains.',
'S6':'La carence peut stimuler une adaptation maintenant l’euthyroïdie ; sa durée et son intensité modifient les troubles observés. L’autonomie nodulaire et la réponse à une surcharge ne sont pas synonymes de TSH constamment élevée.',
'S7':'Les recommandations européennes évaluent le risque avant contraste, réservent la prophylaxie aux situations sélectionnées et adaptent le traitement de la dysfonction à la gravité, à l’âge et aux comorbidités. Elles ne remplacent pas les indications des FI suisses.',
'S8':'La revue historique suisse rapporte une forte endémie ancienne et une régression après prophylaxie iodée, plus incomplète chez l’adulte âgé. Elle ne mesure pas la prévalence actuelle.',
'S9':'L’OSAV présente l’iodation du sel et les sources alimentaires. Le choix du sel iodé ne justifie pas une augmentation de la consommation totale de sel.',
'S10':'L’enquête nationale 2020–2022 décrit les groupes d’enfants et de grossesse ; leurs médianes urinaires sont respectivement 127 et 97 µg/l. Les doses déclarées de suppléments ne constituent pas une prescription universelle.',
'S11':'Le résumé décrit l’hétérogénéité des nodules, des populations clonales et des mutations somatiques dans la pathogenèse du goitre multinodulaire. Il ne permet pas d’inventer une séquence moléculaire unique chez chaque patient.',
'S13':'ETA relie risque échographique, taille et cytologie ; elle précise les exceptions à la ponction, la scintigraphie contextuelle, la surveillance et les options thérapeutiques. Le traitement hormonal suppressif n’est pas recommandé en routine chez le patient euthyroïdien.',
'S14':'La revue des goitres plongeants décrit leur anatomie, leurs symptômes et leur imagerie. Ses chiffres de compression et de malignité proviennent de séries sélectionnées ; ils ne constituent pas des seuils autorisant à différer une urgence.',
'S15':'L’étude suisse observe une amélioration du statut iodé après augmentation de la teneur du sel en 1999. Les comparaisons de 1999 et 2004 sont des données historiques de programme.',
'S16':'Le résumé présente les effets de la carence iodée sur la fonction et le développement ainsi que la prévention par iodation. Il ne fournit pas une estimation actuelle du goitre suisse adulte.',
'S17':'L’étude danoise décrit la structure thyroïdienne en contexte d’apport limite, avec ses propres seuils de volume. L’absence de cancer observée dans un suivi court ne prouve pas un risque individuel nul.',
'S18':'La revue slovène décrit l’évolution des troubles thyroïdiens après modification de l’iodation. La comparaison éclaire une transition de population, sans imposer une conduite suisse individuelle.',
'S20':'La page OSAV aborde la supplémentation pendant l’allaitement et des résultats préliminaires. Le repère de 250 µg/jour concerne l’apport total ; un complément se discute selon la situation.',
'S22':'Une étude transversale danoise trouve une association entre consommation d’alcool et fréquence du goitre. Une association observationnelle ne fonde pas une recommandation préventive d’alcool.',
'S23':'L’enquête polonaise décrit l’hyperthyroïdie après prophylaxie. L’unité de teneur du sel dans le résumé consulté est discordante ; aucune dose corrigée silencieusement n’en est déduite.',
'S24':'L’iodure de potassium axapharm à 65 mg est destiné à la prophylaxie nucléaire sur instruction des autorités. Il ne constitue ni un complément nutritionnel ni un traitement du goitre autonome.',
'S25':'La FI d’Euthyrox décrit les indications suisses, les doses et la titration, les horaires de prise, les contre-indications et les interactions. Son indication de goitre bénin ne rend pas la suppression hormonale recommandée en routine.',
'S26':'LISA compare pendant un an quatre traitements chez des adultes sélectionnés, avec exclusions d’autonomie et de certaines comorbidités. L’association réduit davantage le volume ; cet effet ne démontre pas un bénéfice clinique pour tout goitre.',
'S27':'La revue Cochrane trouve davantage de réduction volumétrique mais davantage d’hypothyroïdie avec préstimulation par rhTSH. La différence de volume est exprimée en points de pourcentage et la qualité de vie reste incertaine.',
'S28':'La revue suisse de 2015 décrit les indications et l’évolution de la chirurgie thyroïdienne. Son nombre annuel d’interventions et sa mortalité très faible sont historiques, sans garantie individuelle actuelle.',
'S29':'La revue médicale suisse relie clinique, TSH, échographie et décision de ponction. Elle apporte un contexte local ; sa filiation aux recommandations alors utilisées est distinguée du cadre ETA retenu pour la conduite actuelle.',
'S30':'Le consensus britannique utilise ses systèmes U et Thy et discute notamment les limites de la cytologie folliculaire et un suivi allégé des lésions bénignes. Ces catégories ne sont pas fusionnées avec EU-TIRADS et Bethesda.',
'S31':'La FI Néo-Mercazole exclut l’hyperthyroïdie induite par l’iode de ses indications et contre-indique le goitre simple ainsi que les signes de compression trachéale. Elle décrit doses, surveillance hématologique, précautions et situations particulières.',
'S32':'I-131 Curium demande une activité individualisée et une évaluation de la fixation et de la rétention. Grossesse, allaitement et difficultés de déglutition comptent dans la décision ; les délais médicamenteux doivent suivre un protocole explicite.',
'S33':'Thyrogen est autorisé dans des situations de cancer thyroïdien après thyroïdectomie. La préstimulation d’un goitre bénin est hors de cette indication suisse et ne reçoit pas une dose extrapolée du protocole oncologique.',
'S34':'La directive OFSP encadre dosimétrie, hospitalisation à partir de 200 MBq d’iode 131, durée minimale et conditions de sortie. Les dérogations nécessitent une autorisation préalable ; le fractionnement pour contourner l’hospitalisation est interdit.',
'S35':'Le répertoire donne des intervalles de fT4 dépendant de l’âge et de la méthode. L’intervalle adulte ne définit pas une cible de grossesse, et le groupe large 0–19 ans ne fournit pas une norme néonatale détaillée.',
'S36':'La classification allemande 2026 précise inclusions et exclusions des affections thyroïdiennes liées à la carence iodée. Elle complète la lecture des codes sans modifier le catalogue français OFS 2024 du dépôt.',
'S37':'Le texte explique la glande normale, le follicule, la thyroglobuline, la synthèse hormonale et le rétrocontrôle. Cette source fondamentale n’est pas une recommandation clinique ; la licence de l’image historique est vérifiée séparément.',
'S38':'La troisième édition de Bethesda définit six catégories et leurs risques dans des nodules opérés. La sélection surestime certains risques ; les résultats de suivi après cytologie bénigne sont distingués des séries chirurgicales.',
'S39':'ETA pédiatrique recommande une évaluation spécialisée, une échographie cervicale et une ponction selon la suspicion. Les seuils adultes ne sont pas transposés ; le suivi bénin et le traitement d’une autonomie sont adaptés à l’enfant.',
'S40':'PROFILES inclut l’examen thyroïdien et les situations de goitre, de tuméfaction cervicale et d’anomalies hormonales. Le rapprochement avec les vignettes du cours est pédagogique, sans reproduction de questions officielles.',
'S41':'Les exigences fédérales de 2026 distinguent évaluation des connaissances et compétences cliniques en référence aux objectifs de formation. Elles ne valident pas les cas fictifs de cette leçon comme sujets officiels.'}
assert set(paraphrases)=={s['id'] for s in raw}
sources=[]
for s in raw:
 p=Path(s['cache_external']);assert p.is_file() and sha(p)==s['sha256'],s['id']
 sources.append(dict(id=s['id'],url=s['url'],publisher=s['editeur'],read_at=s['date_consultation'],section=s['section_page'],passage=paraphrases[s['id']],passage_kind='faithful_paraphrase',population=s['population'],limits=s['limites'],source_content_sha256=s['sha256'],read_level='Résumé uniquement' if 'résumé' in s['section_page'].lower() and 'texte intégral' not in s['section_page'].lower() else 'Passages identifiés, pas affirmation de lecture intégrale de chaque document'))
save(D/'source-ledger.json',{'sources':sources,'full_source_storage':'Cache externe ; aucune source intégrale non libre recopiée dans le livrable.','clinical_certification':False})
rows14=[
('Définition',['e01-1'],['S1','S36'],'Le périmètre et les quatre sous-codes sont explicités ; le goitre structural est distingué de la preuve de sa cause iodée.'),
('Épidémiologie',['e01-2'],['S8','S10','S15','S17'],'Les données suisses précèdent les comparaisons européennes ; les chiffres historiques, les populations et la prévalence adulte inconnue sont distingués.'),
('Physiopathologie',['e01-3','e01-s-physio-cours','e01-s-bioch-cours'],['S4','S6','S11','S37'],'Le normal, la compensation, l’hétérogénéité nodulaire et la surcharge sont expliqués sans trajectoire obligatoire ni TSH constamment élevée.'),
('Démarche clinique',['e01-0','e01-7'],['S7','S13','S29'],'La vignette initiale est résolue par les axes fonction, nodule et compression ; la détresse conduit à l’urgence avant le bilan électif.'),
('Anamnèse',['e01-5','e01-semio-signs'],['S13','S14','S29'],'Chronologie, symptômes compressifs, risques familiaux, irradiation et expositions iodées sont interrogés avec leurs implications pratiques.'),
('Examen clinique',['e01-6','e01-semio-examination'],['S4','S14','S29'],'Inspection, palpation, déglutition, ganglions, respiration et Pemberton sont décrits ; les limites de reproductibilité et de sécurité sont explicites.'),
('Syndromes',['e01-7','e01-semio-interpretation'],['S13','S14'],'Les syndromes morphologique, fonctionnel et compressif sont séparés puis confrontés ; une fonction normale ne rassure pas sur une compression.'),
('Diagnostic positif',['e01-7','e01-e-5'],['S4','S13','S36'],'L’échographie confirme la structure et le contexte étaye la cause ; aucune iodurie isolée ni résidence ancienne ne suffit à affirmer E01.'),
('Explorations',['e01-e-1','e01-e-2','e01-e-3','e01-e-4','e01-e-5'],['S13','S30','S35','S38'],'Les examens sont hiérarchisés et leurs résultats interprétés : biologie, risque échographique, cytologie, scintigraphie et imagerie profonde.'),
('Arbre et diagnostic différentiel',['e01-7','e01-semio-differentials'],['S7','S13','S14'],'L’arbre suit l’urgence, la fonction, la morphologie puis les options ; cancer, Basedow, thyroïdite, autonomie et autres masses sont confrontés.'),
('Prise en charge',['e01-9','e01-p-1','e01-p-2','e01-p-3','e01-p-4'],['S13','S25','S31','S32','S34'],'La décision est hiérarchisée selon symptômes et risque ; FI suisses, divergences, options chirurgicales et mini-invasives, doses et précautions sont exposées.'),
('Prévention, suivi, pronostic',['e01-10','e01-s-sante-cours'],['S9','S13','S20','S30'],'La prévention collective et les décisions individuelles sont séparées ; le calendrier de surveillance suit le risque, les traitements et les symptômes nouveaux.'),
('Points clés',['e01-12','e01-e-6'],['S4','S13','S34','S40','S41'],'Les paramètres décisifs et les cas corrigés synthétisent la conduite ; seuils, normes, cibles et populations ne sont pas confondus.'),
('Pièges',['e01-p-5','e01-semio-limits'],['S7','S13','S24','S25','S31','S32'],'Les erreurs d’iode, de suppression hormonale, de ponction, de causalité et d’interprétation des probabilités sont expliquées avec leurs conséquences.')]
rows20=[
('Question clinique suisse',['e01-0','e01-11'],['S7','S13','S29']),('Définition et périmètre',['e01-1'],['S1','S36']),('Classifications',['e01-1','e01-e-3'],['S4','S13','S14','S38']),('Épidémiologie CH puis Europe',['e01-2'],['S8','S10','S15','S17']),('Normal et physiopathologie',['e01-3','e01-s-anat-cours','e01-s-histo-cours','e01-s-physio-cours','e01-s-bioch-cours'],['S4','S6','S11','S37']),('Étiologies et risques',['e01-4'],['S6','S9','S22']),('Anamnèse',['e01-5'],['S13','S14','S29']),('Examen',['e01-6','e01-semio-examination'],['S4','S14']),('Signaux de gravité',['e01-8','e01-semio-urgency'],['S7','S14']),('Explorations',['e01-e-1','e01-e-2','e01-e-3','e01-e-4','e01-e-5'],['S13','S30','S35','S38']),('Diagnostic différentiel',['e01-7'],['S13','S14','S36']),('Traitement suisse',['e01-9','e01-p-1','e01-p-2','e01-p-3','e01-p-4','e01-p-5'],['S25','S31','S32','S33','S34']),('Complications et pronostic',['e01-8','e01-10'],['S7','S13','S14']),('Suivi et prévention',['e01-10','e01-s-sante-cours'],['S9','S13','S20','S30']),('Populations particulières',['e01-11','e01-p-2','e01-p-3','e01-p-4'],['S20','S25','S31','S32','S39']),('Aspects administratifs suisses',['e01-p-4','e01-p-5'],['S24','S34']),('Critères et alertes',['e01-12','e01-semio-limits'],['S4','S13','S14']),('Paramètres décisifs',['e01-12','e01-e-2','e01-e-3','e01-e-5'],['S10','S13','S26','S27','S35','S38']),('Sous-codes complets',['e01-1'],['S1','S36']),('Examen fédéral',['e01-e-6','e01-12'],['S13','S29','S40','S41'])]
monograph=[dict(point=i,label=t,anchor=a[0],additional_anchors=a[1:],sources=ss,coverage_explanation=ex) for i,(t,a,ss,ex) in enumerate(rows14,1)]
matrix20=[dict(point=i,label=t,status='covered',evidence=['review-inputs/E01-source.html#'+x for x in aa],source_ids=ss) for i,(t,aa,ss) in enumerate(rows20,1)]
(D/'review-inputs').mkdir(exist_ok=True);(D/'review-inputs/E01-source.html').write_text('\n'.join((R/n).read_text() for n in stat['source_sha256']))
save(D/'coverage-14-20.json',{'at':now,'review_mode':'self_review','monograph14':monograph,'medina20':matrix20,'limits_are_not_missing_sections':True,'clinical_certification':False})
limits=[
'La prévalence contemporaine du goitre adulte suisse n’a pas été trouvée ; l’étude nutritionnelle nationale ne la remplace pas.',
'Plusieurs études historiques sont lues au niveau du résumé ; leurs populations, dates et limites restent visibles.',
'La FI suisse du perchlorate n’a pas été identifiée : aucun dosage suisse n’est proposé. La divergence Néo-Mercazole/ETA conduit à un cadre spécialisé documenté.',
'La FI I-131 Curium donne deux et trois jours dans deux passages pour le carbimazole ; le centre doit fixer son protocole explicite.',
'La classification locale reste OFS 2024 ; BfArM 2026 ne constitue pas une validation administrative suisse pour 2026.',
'Les images montrent anatomie normale, compression et hyperplasie ; aucune étiologie iodée ni grade clinique n’est déduit de leur seule apparence.',
'Le navigateur utilise une origine interceptée avec les octets exacts ; aucun serveur HTTP réel ou site publié n’a été testé.',
'La coque native ajoute un bandeau provisoire mentionnant un contre-audit restant ; les quatre reçus présents sont des auto-relectures explicites, sans certification humaine.',
'La copie native conserve la navigation des autres leçons ; les contrôles médicaux et visuels portent exclusivement sur E01.'
]
findings=[dict(id=f'L{i:02}',blocking=False,finding=t) for i,t in enumerate(limits,1)]
save(D/'remaining-findings.json',findings)
checks=[
('Structure, fonction et cause séparées ; aucune iodurie isolée ne prouve la carence chronique.',['S4','S6','S13']),
('Scintigraphie à TSH normale contextuelle ; ponction des nodules hyperfonctionnels uniquement si forte suspicion, y compris dans le cas corrigé.',['S13']),
('Six catégories Bethesda 2023, risque des nodules opérés distingué du suivi bénin ; cytologie folliculaire distincte de l’histologie.',['S30','S38']),
('Calcitonine interprétée selon contexte et méthode ; thyroglobuline non utilisée pour trier le cancer.',['S13']),
('Pemberton inférieur à 5 % est une fréquence, pas une sensibilité ; diamètres trachéaux descriptifs, non seuils d’attente.',['S14']),
('Enquête suisse : effectifs et médianes distincts, apport total de grossesse/allaitement distinct de dose de complément.',['S10','S20']),
('Euthyrox : indication autorisée et recommandation clinique distinguées, doses et titration contextualisées, interactions et grossesse explicites.',['S25','S13']),
('LISA : nombres du résumé et du texte explicitement discordants, exclusions et résultat volumétrique sans bénéfice clinique universel.',['S26']),
('Néo-Mercazole : indication iodée exclue, compression contre-indiquée, doses, durée, hémogramme et signes imposant arrêt vérifiés.',['S31']),
('Iode 131 : dosimétrie, allaitement arrêté huit semaines avant sans reprise pour le même enfant, contraception et radioprotection suisses.',['S32','S34']),
('Thyrogen hors indication bénigne ; différence de volume en points de pourcentage et excès d’hypothyroïdie contextualisés.',['S27','S33']),
('Enfant : seuils adultes non transposés ; suivi et autonomie pédiatriques distincts. Rein, foie et grossesse traités avec les limites des FI.',['S39','S25','S31','S32']),
('Images originales vérifiées avec licences propres à chaque version ; repères HTML sur structures effectivement visibles.',['S37','S14']),
('Thyroperoxydase définie localement pour éviter la collision avec la thrombopoïétine du glossaire partagé.',['S31','S37']),
('Les six surfaces, fenêtres et résumés conservent les nuances de causalité, les populations et les limites après harmonisation.',['S4','S7','S13','S31'])]
common=dict(reviewer=author,author=author,mode='self_review',reviewed_at=now,source_sha256=stat['source_sha256'],review_html_sha256=sha(D/'E01-apercu-autonome.html'),human_validation=False,independent=False,score=None,blocking_findings=0,remaining_limits=findings)
reviews={'medical':dict(**common,kind='medical',scope='Auto-relecture des six HTML, des fenêtres, tableaux, cas, figures et résumés ; comparaison aux passages identifiés du ledger.',checks=[dict(finding_and_resolution=t,source_ids=ss,state='checked_by_author') for t,ss in checks]),'language':dict(**common,kind='language',scope='Auto-relecture française de toutes les surfaces E01.',checks=['Formulations causales et impératives corrigées selon le degré de recommandation.','Phrases nominales historiques développées sans perte des données.','Unités, populations, sources et dates distinguées ; aucune traduction présentée comme officielle.','Intitulés des tableaux, figures, fenêtres et cas harmonisés ; double sens du sigle de la thyroperoxydase évité.'])}
for kind,w in [('visual_desktop',1440),('visual_mobile',390)]:
 names=[f'{w}-normal-anatomy.png',f'{w}-compression-ct.png',f'{w}-histology.png',f'{w}-clinical-diagram.png',f'{w}-e01-s-semio-diagram-0.png',f'{w}-e01-s-physio-diagram-0.png',f'{w}-e01-s-bioch-diagram-0.png',f'{w}-e01-s-sante-diagram-0.png',f'{w}-carbimazole-popup.png',f'{w}-font24-pharmacology.png',f'{w}-book24-pharmacology.png']
 reviews[kind]=dict(**common,kind=kind,scope='Inspection visuelle des captures listées, complétée par les interactions automatisées.',captures={n:sha(D/n) for n in names},checks=['Chaque original est décodé après défilement ; légendes, attribution et repères HTML sont visibles.','Les schémas logiques sont distincts des images anatomiques originales ; leurs polices mobiles ont été agrandies.','Tableaux déroulants horizontalement à taille 24 ; document sans débordement horizontal.','Six disciplines, neuf sections de sémiologie, 55 fenêtres accessibles, quatre quiz, Navigo et touches Entrée/Espace vérifiés.'],browser_report_sha256=sha(D/'browser-report.json'),browser_mode=browser['mode'])
(D/'reviews').mkdir(exist_ok=True)
for k,v in reviews.items():save(D/'reviews'/f'{k}.json',v)
figinfo=[('e01-thyroide-normale-openstax2013.jpg','https://commons.wikimedia.org/wiki/File:1811_The_Thyroid_Gland.jpg','OpenStax College ; micrographie University of Michigan Medical School 2012','CC BY 3.0, version Connexions 19 juin 2013 et métadonnées Commons propres à cette image','Isthme antérieur, parathyroïde postérieure et colloïde folliculaire'),('e01-goitre-compressif-original.jpg','https://commons.wikimedia.org/wiki/File:Goitre_compressif_sur_la_trachée_(sagittal).jpg','Stockholm, 18 août 2016','CC BY-SA 4.0','Masse antérieure et lumière aérienne au voisinage du rétrécissement ; flèche originale conservée'),('e01-goitre-histologie-original.jpg','https://commons.wikimedia.org/wiki/File:Histopathology_of_thyroid_hyperplasia_with_a_nodule.jpg','Mikael Häggström, 16 novembre 2023','CC0','Colloïde et bordure épithéliale ; pas de cause iodée inférée')]
(D/'figures').mkdir(exist_ok=True);images=[]
for name,url,au,lic,ann in figinfo:
 src=R/'assets/img/e01/alpha/codex'/name;dst=D/'figures'/name;shutil.copyfile(src,dst)
 images.append(dict(path=str(dst.relative_to(D)),sha256=sha(dst),original_url=url,author=au,license=lic,annotations=ann+' ; repères HTML ajoutés, pixels originaux inchangés.',medical_review=dict(mode='self_review',reviewer=author,proof='reviews/medical.json',human_validation=False)))
manifest=dict(schema_version=1,code='E01',lesson='E01',author=author,base_sha=stat['base_sha'],monograph=monograph,matrix20=matrix20,sources=sources,images=images,semiology=dict(section_anchors=['e01-semio-'+x for x in ['normal','signs','mechanisms','examination','interpretation','differentials','urgency','limits','sources']]),blocking_findings=0,remaining_findings=findings,reviews={k:dict(path='reviews/'+k+'.json',reviewer=author,mode='self_review',sha256=sha(D/'reviews'/f'{k}.json')) for k in reviews},source_files_sha256=stat['source_sha256'],preview=dict(path='E01-apercu-autonome.html',sha256=sha(D/'E01-apercu-autonome.html'),browser_report='browser-report.json',native_bundle='E01-apercu-autonome.bundle.json'),clinical_certification=False,publication_to_main=False,tokens_actual=None,cost_actual=None)
save(D/'lesson-manifest.json',manifest)
final_sources={**stat['source_sha256'],'glossary/e01.py':sha(R/'glossary/e01.py'),**stat['original_images_sha256']}
save(D/'source-binding.json',dict(code='E01',verified_at=now,preview='E01-apercu-autonome.html',preview_sha256=sha(D/'E01-apercu-autonome.html'),final_sources=final_sources,checks=['static-report.json','audit-sciences.json','browser-report.json','coverage-14-20.json','source-ledger.json','lesson-manifest.json','reviews/medical.json','reviews/language.json','reviews/visual_desktop.json','reviews/visual_mobile.json'],clinical_certification=False))
print('E01 : 14 points, 20 rubriques, 36 sources paraphrasées, 3 originaux et 4 auto-relectures traçables.')
