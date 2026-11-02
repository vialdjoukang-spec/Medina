#!/usr/bin/env python3
"""Consigner la couverture relue par l'auteur ; ne produit aucune validation médicale."""
from pathlib import Path
import json,datetime
from common import BYKEY
OUT=Path(__file__).resolve().parent
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
MONO=[
('Définition','c95-1',['WHO','ALAL','CIM','OFS-CIM'],'LALA, LAPM biphénotypique/bilinéale, LAI et catégorie biologique résiduelle sont séparées du dossier incomplet ; sous-codes et caractère de rémission expliqués.'),
('Épidémiologie','c95-2',['OFS-CANCER','AML','ALL','KARASEK'],'Données suisses C91–C95 datées, comparateurs européens LMA/LLA et rareté LALA gardent leur population ; incidence suisse propre à C95 non inventée.'),
('Physiopathologie','c95-3',['NORMAL','WHO','ALAL','KARASEK'],'Six sciences relient production normale, fonctions sanguines, anomalie génétique, plasticité de lignée, symptômes et interprétation ; deux populations ne prouvent pas deux clones.'),
('Démarche clinique','c95-7',['AML','ALL','WHO','FLOW'],'Stabilité et urgences, prélèvements adaptés, populations et critères, génétique/contextes puis conclusion intégrée constituent une progression argumentée.'),
('Anamnèse','c95-5',['AML','ALL','RMS-NF','ALAL'],'Chronologie, tolérance, saignements, fièvre, symptômes neurologiques, traitements/expositions et contexte social sont reliés aux hypothèses et à la gravité.'),
('Examen clinique','c95-6',['AML','ALL','RMS-NF'],'Fonctions vitales, peau/muqueuses, ganglions/organes et neurologie sont décrits ; absence de signes et leucocytes élevés ne garantissent pas une situation rassurante.'),
('Syndromes','c95-9',['AML','APL','FASTURTEC','RMS-NF'],'Insuffisance médullaire, infiltration, leucostase, infection, hémorragie et lyse sont distinguées avec actions parallèles ; aucun seuil leucocytaire ne remplace la clinique.'),
('Diagnostic positif','c95-1',['WHO','FLOW','ALAL'],'Seuil global LALA, critères OMS de lignées avec intensité relative/contrôles, alternatives monocytaires et différences ICC sont exposés sans tableau fusionné.'),
('Explorations','c95-e-1',['AML','ALL','FLOW','FASTURTEC'],'Chaque examen répond à une question ; prélèvements, panels, génétique, bilan métabolique, MRD et préanalytique sont reliés à leurs limites et aux décisions.'),
('Arbre diagnostique','c95-arbre-final',['WHO','FLOW','ALAL','AML'],'Arbre causal non anatomique, séquence en quatre temps et tableau différentiel explicitent urgence, classification et réponse ; les cinq cas vérifient les bifurcations.'),
('Prise en charge','c95-10',['ALAL','IBFM','EBMT17','EBMT26','GLIVEC','ICLUSIG'],'Orientation type LLA pour de nombreuses LAPM, réponses, biologie et allogreffe discutées avec niveau de preuve ; sept FI suisses et quatre fenêtres médicamenteuses détaillées.'),
('Prévention et suivi','c95-11',['ALL','AML','ALAL','FASTURTEC'],'Prévention des complications et consignes, suivi de réponse/MRD et toxicités sont individualisés ; calendrier LLA après maintenance non transposé à toute LALA.'),
('Points clés','c95-14',['WHO','FLOW','ALAL','PROFILES17','MEBEKO26'],'Synthèse décisionnelle, quatorze Pareto et points chiffrés relient lignée, intensité, urgence et réponse ; PROFILES 2017/examen2026 séparé de la transition2028.'),
('Pièges','c95-e-5',['WHO','FLOW','ALAL','FASTURTEC'],'Cinq quiz et fenêtres reprennent MPO faible, BCR::ABL1 et LMC, leucostase sous100G/L, MRD versus RC et urate ex vivo ; dénominateurs et dose/indication restent visibles.')]
MATRIX=[
('Question clinique et examen fédéral','c95-0',['ALL','ALAL','PROFILES17','MEBEKO26','PROFILES-TRANS'],'Vignette fictive à34ans avec urgence, lignée et stratégie ; SSP effectivement relues, sans prédiction des sujets ni confusion référentiel2026/2028.'),
('Définition et périmètre CIM-10-GM','c95-1',['CIM','OFS-CIM','WHO'],'C95.0/.1/.7/.9 et caractère0/1, code additionnelC95.8! et exclusions expliqués ; codage2024 documenté sans certification de facturation2026.'),
('Classifications et stades','c95-who-icc',['WHO','FLOW','ALAL'],'OMS et ICC distinguées, groupes génétiques et hiérarchie ; pas stade TNM inventé ni seuil20% transféré aux LMA génétiquement définies.'),
('Épidémiologie suisse et européenne','c95-2',['OFS-CANCER','AML','ALL','KARASEK'],'Suisse2013–2017 agrégée C91–C95, comparateurs LMA/LLA et populations de revues explicites ; registre américain seulement descriptif.'),
('Normal vers pathologique','c95-s-semio',['NORMAL','NORMAL-RBC','NORMAL-WBC','NORMAL-HEMO','WHO'],'Six sciences et neuf étapes sémiologiques relient fonction normale, perturbation, signe, examen et traitement ; quatre originaux humains et quatre diagrammes causaux.'),
('Étiologies et facteurs de risque','c95-4',['OFS-CANCER','AML','ALAL','KARASEK'],'Expositions et contextes interrogés sans causalité individuelle automatique ; prédisposition constitutionnelle séparée des anomalies tumorales et du changement de lignée.'),
('Anamnèse et symptômes','c95-5',['AML','ALL','ALAL','RMS-NF'],'Plainte, tolérance, chronologie, traitement et entourage contextualisés ; fréquences des symptômes LLA ne sont pas sensibilités diagnostiques de LAPM.'),
('Examen clinique','c95-6',['AML','ALL','RMS-NF'],'Retentissement vital et organique, sang/peau, muqueuses et neurologie décrits ; la clinique ne détermine pas la lignée, et une présentation pauvre ne l’exclut pas.'),
('Drapeaux rouges et urgences','c95-9',['AML','APL','FASTURTEC','RMS-NF'],'Infection grave, hémorragie, leucostase et lyse requièrent action parallèle ; ATRA sur suspicion de LAP et protocole antibiotique actuel, sans attendre typage complet.'),
('Examens complémentaires','c95-e-1',['AML','ALL','FLOW','FASTURTEC'],'Hiérarchie clinique/laboratoire, transport, limites des méthodes, risque procédural et surveillance métabolique ; chaque test garde une question et une conséquence.'),
('Diagnostic différentiel','c95-8',['WHO','FLOW','ALAL','KARASEK'],'LMA/LLA aberrantes, LMC blastique, LAI, hématogones, BPDCN et fusion kinase confrontés ; panel et contexte priment sur positivité isolée.'),
('Prise en charge suisse et FI','c95-p-1',['GLIVEC','ICLUSIG','FASTURTEC','LITALIR','VESANOID','BLINCYTO','VENCLYXTO'],'Sept FI datées lues avec profondeur documentée ; mécanismes, indications, quatre fenêtres de dose/adaptation, précautions et limites d’extrapolation aux LAPM.'),
('Complications et pronostic','c95-12',['ALAL','KARASEK','IBFM','EBMT17','EBMT26'],'Cohortes de greffe sélectionnées, horizons2/3ans, survie et événements concurrents distingués ; aucune causalité ou prédiction individuelle tirée des pourcentages.'),
('Suivi, prévention, dépistage','c95-11',['ALL','AML','ALAL','FASTURTEC'],'MRD/cible/méthode/calendrier et suivi de personne détaillés ; fièvre et toxicités ont des consignes, sans dépistage universel inventé pour une affection rare.'),
('Situations particulières','c95-13',['IBFM','ALAL','GLIVEC','ICLUSIG','LITALIR','VESANOID'],'Enfant, adulte fragile, grossesse/fertilité et fonctions d’organe influencent stratégie ; doses adultes non extrapolées, greffe pédiatrique non automatique.'),
('Spécificités administratives suisses','c95-13',['OFSP','OAMAL','OFS-CIM','MEBEKO26'],'Indication, disponibilité, LS et art.71a–d séparés ; assurance-invalidité et lien professionnel documentés sans garantie, prix ou reconnaissance inventés.'),
('Diagnostic formel','c95-1',['WHO','FLOW','ALAL'],'CD19/intensité et combinaisons B, CD3epsilon, MPO et monocytes, populations et exclusions précisées ; faiblesse isolée et marqueurs associés non suffisants.'),
('Paramètres clés chiffrés','c95-e-2',['HUG','WHO','FLOW','AML','ALL','FASTURTEC'],'Normes adultes HUG2019 séparées des seuils diagnostiques/actes ;20%, intensité50%, minorité5%, MRD10^-4 et doses ont unité, méthode et population.'),
('Sous-codes couverts','c95-1',['CIM','OFS-CIM','WHO'],'C95.00/.01, .10/.11, .70/.71, .90/.91 et additionnel.8! couverts ; chronique exacerbée, rémission partielle/inconnue et absence de caractère2 expliquées.'),
('Points d’examen fédéral','c95-e-5',['PROFILES17','MEBEKO26','PROFILES-TRANS','WHO','FASTURTEC'],'Cinq quiz expliqués et quatorze synthèses évaluent décisions et pièges ; correspondances SSP2017 effectivement lues, sans allégation de fréquence d’épreuve.')]
def make(rows,kind):
 return [{'point':i,'title':title,'anchor':anchor,'sources':[BYKEY[k]['id'] for k in src],'status':'covered',kind:explanation,'clinical_certification':False} for i,(title,anchor,src,explanation) in enumerate(rows,1)]
points=make(MONO,'coverage_explanation');rubrics=make(MATRIX,'evidence')
for name,key,rows in [('monograph-14.json','points',points),('matrix-20.json','rubrics',rubrics)]:
 (OUT/name).write_text(json.dumps({'code':'C95','reviewed_at':now,'mode':'author_coverage_self_review',key:rows,'clinical_certification':False,'meaning':'Couverture relue par auteur, pas score de qualité ni certification humaine.'},ensure_ascii=False,indent=2)+'\n')
text='# C95 — couverture finale relue\n\nLa recherche initiale et sa porte VÉRITÉ restent conservées dans recherche_C95 ; ce document est un complément final, sans antidater la lecture ou la rédaction. 32entrées comprennent lectures ciblées, septFI, réutilisations attribuées et le résumé EBMT2026 explicitement limité.\n\n| Rubrique | État | Sources | Ancre | Couverture et limites |\n|---|---|---|---|---|\n'
for x in rubrics:text+=f"| {x['point']}. {x['title']} | couverte | "+', '.join(x['sources'])+f" | `{x['anchor']}` | {x['evidence']} |\n"
text+='\nCouverture ≠ validation médicale. Incidence suisse propreC95, remboursement individuel et protocole complet prescripteur ne sont pas établis. Les paragraphes de normal OpenStax sont paraphrasés ; seule l’image2016CCBY4 est reproduite. Les figures de cytométrie illustrent un diagnostic et ne fondent pas une recommandation thérapeutique américaine.\n'
(OUT/'coverage-final.md').write_text(text)
print('14 points et 20 rubriques documentés ; aucune clôture automatique.')
