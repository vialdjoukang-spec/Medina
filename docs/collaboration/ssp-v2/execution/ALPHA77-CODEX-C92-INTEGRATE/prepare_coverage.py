"""Couverture de C92 attribuée à l'auteur, sans certification médicale."""
import json,datetime
from common import OUT,BYKEY
MONO=[
('Définition','c92-1',['OFS','WHO','ELN-AML'],'La famille C92 est distinguée des entités biologiques ; codage, diagnostic et statut de rémission ne sont pas confondus.'),
('Épidémiologie','c92-2',['ONKO-AML','OFS-CANCER','MLL'],'Données européennes et rareté sont contextualisées ; aucune incidence suisse spécifique C92 déduite des leucémies agrégées.'),
('Physiopathologie','c92-3',['NORMAL','WHO','ELN-AML','ELN-CML'],'Normal médullaire puis clone, différenciation et retentissement expliquent signes, mesures et décisions ; six sciences développées.'),
('Démarche clinique','c92-4',['ELN-AML','ONKO-APL','ELN-CML'],'Stabilisation et urgences précèdent une classification complète ; prélèvements et prise en charge avancent en parallèle.'),
('Anamnèse','c92-5',['ELN-AML','ELN-CML','PROFILES'],'Chronologie, saignements, infections, expositions, traitements, terrain et projet de vie orientent les hypothèses et la décision.'),
('Examen clinique','c92-6',['ELN-AML','CHUV-CML','SARCOMA'],'Signes vitaux, peau/muqueuses, organomégalie et anomalies focales sont reliés au mécanisme, sans performance chiffrée inventée.'),
('Syndromes','c92-7',['WHO','ONKO-APL','ELN-CML','MLL','SARCOMA'],'LAM, LPA, LMC, MDS/MPN neutrophilique et sarcome sont différenciés ; aucune stratégie unique imposée par le code C92.'),
('Diagnostic positif','c92-8',['WHO','ELN-AML','ELN-CML'],'Morphologie, immunophénotype et génétique forment un diagnostic intégré ; seuils OMS et ICC et limites des tests sont nommés.'),
('Explorations','c92-9',['ELN-AML','ELN-CML','SARCOMA'],'Cinq blocs détaillent numération/frottis, moelle/tissu, génétique, réponse/MRD et sécurité, avec question et limites pour chaque mesure.'),
('Arbre diagnostique','c92-10',['ELN-AML','ONKO-APL','ELN-CML','MLL'],'Chemin de gravité, morphologie, génétique et alternatives explicite ; un nombre ou une photographie ne clôture pas le raisonnement.'),
('Prise en charge','c92-11',['ELN-AML','ELN-LOW','ELN-CML','ONKO-APL'],'Intensité, biologie, personne, consolidation et support intégrés ; quinze FI suisses ciblées sont documentées avec leur portée.'),
('Prévention et suivi','c92-12',['ONKO-AML','ONKO-APL','ELN-CML'],'Calendriers et marqueurs dépendent de l’entité et du traitement ; TFR surveillée, toxicités et besoins de la personne sont détaillés.'),
('Points clés','c92-13',['ELN-AML','ELN-LOW','ELN-CML','VENCLYXTO'],'Seuils diagnostiques, réponses, jalons et adaptations sont distingués ; huit cas fictifs testent des décisions et leurs conditions.'),
('Pièges','c92-14',['OFS','WHO','ELN-AML','ELN-CML'],'C92.5/C93.1, code/biologie, compte/fonction, MRD/éradication et recommandation/indication sont séparés avec explication au patient.')]
MATRIX=[
('Question clinique et examen fédéral','c92-4',['PROFILES','MEBEKO','PROFILES-TRANS'],'Situations de départ et raisonnement de gravité reliés au cadre officiel ; aucune prédiction de question ni validation officielle du cours.'),
('Définition et périmètre','c92-1',['OFS','WHO'],'Sous-catégories C92, entités aiguës/chroniques, sarcome et codes voisins distingués à partir du fichier OFS français.'),
('Classifications et stades','c92-8',['WHO','ELN-AML','ELN-LOW','ELN-CML'],'OMS/ICC, ELN selon traitement et phases de LMC sont explicités ; nomenclature historique de FI ne vaut pas équivalence automatique.'),
('Épidémiologie','c92-2',['ONKO-AML','MLL','OFS-CANCER'],'Âges/fréquences des populations sources et limites des données rares conservés ; aucun taux suisse spécifique non établi.'),
('Normal vers pathologique','c92-s-semio',['NORMAL','NORMAL-WBC','NORMAL-HEMO','WHO'],'Six disciplines, neuf unités sémiologiques et huit figures scientifiques relient organisation normale, mécanismes, mesures et décisions.'),
('Étiologies et facteurs de risque','c92-2',['WHO','ELN-AML'],'Antécédents, traitements, prédisposition et facteurs de risque sont contextualisés sans causalité individuelle inférée d’une association.'),
('Anamnèse et symptômes','c92-5',['ELN-AML','CHUV-CML','ELN-CML'],'Début, progression, retentissement, infection, saignement, masse, traitements et projet parental explorés dans une trajectoire.'),
('Examen clinique','c92-6',['ELN-AML','SARCOMA','CHUV-CML'],'Évaluation vitale et signes orientés, avec absence de sensibilité/spécificité universelle inventée et réévaluation si évolution.'),
('Drapeaux rouges','c92-semio-urgency',['ELN-AML','ONKO-APL','TRISENOX'],'LPA, leucostase, lyse, sepsis, hémorragie, compression et complications du traitement identifiées ; urgences traitées en parallèle du bilan.'),
('Examens complémentaires','c92-e-1',['ELN-AML','ELN-CML','SARCOMA'],'Choix du matériel, frottis, cytométrie, caryotype/FISH/PCR, tissu et bilans de sécurité expliqués avec portée et discordances.'),
('Diagnostic différentiel','c92-semio-differentials',['WHO','MLL','SARCOMA'],'Réaction, autres néoplasies, cytopénies et masses concurrentes discutées ; une leucémie connue n’exclut pas infection ou toxicité associée.'),
('Traitement suisse et pharmacologie','c92-p-1',['CYTOSAR','DAUNOBLASTIN','VYXEOS','VENCLYXTO','SCEMBLIX'],'Six blocs couvrent intensif, LPA, moins intensif, FLT3, LMC et support ; formulations, dose, voie, interactions et contre-indications contextualisées.'),
('Complications et pronostic','c92-p-6',['ELN-AML','ELN-LOW','ELN-CML','EBMT'],'Risque adapté au traitement, MRD, lyse, infection, saignement, QT et différenciation ; survie de cohorte distincte de prédiction individuelle.'),
('Prévention, dépistage et suivi','c92-12',['ONKO-AML','ONKO-APL','ELN-CML'],'Surveillance clinique/moléculaire et toxicités précisée ; pas de dépistage universel de leucémie inventé ni de PCR uniforme pour toute LPA.'),
('Populations particulières','c92-p-6',['ELN-AML','ELN-CML','VESANOID','VYXEOS'],'Âge, fragilité, enfant, grossesse, fertilité et organes modifient choix et limites ; un schéma adulte ne devient pas pédiatrique.'),
('Cadre administratif suisse','c92-p-6',['OFSP','OAMAL','OFS'],'Autorisation, disponibilité et remboursement séparés ; aucune couverture individuelle, aucun prix ni validation exhaustive de facturation.'),
('Diagnostic formel','c92-8',['WHO','ELN-AML','ELN-CML','MLL'],'Critères biologiques, seuils avec exceptions et méthode documentés ; diagnostic précis et degré d’incertitude précèdent le codage final.'),
('Paramètres chiffrés','c92-13',['ELN-AML','ELN-CML','TRISENOX','VANFLYTA','VENCLYXTO'],'Blastes, CR/CRh/CRi, IS/MMR/MR4, QT et paliers de dose gardent unités, population et objectif ; OCR et unité hépatique douteuse non repris.'),
('Sous-codes couverts','c92-1',['OFS','WHO'],'C92.0/.1/.2/.3/.4/.5/.6/.7/.8/.9 et caractères de rémission expliqués ; aucun caractère de rechute ICD-10-CM importé.'),
('Synthèse et entraînement','c92-14',['PROFILES','MEBEKO','ELN-AML','ELN-CML'],'Huit exercices fictifs, quarante-deux fenêtres et neuf synthèses Pareto explicitent les décisions ; aucune certification médicale par ces compteurs.')]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
for filename,key,rows,field in [('monograph-14.json','points',MONO,'coverage_explanation'),('matrix-20.json','rubrics',MATRIX,'evidence')]:
 result=[{'point':i,'title':t,'anchor':a,'sources':[BYKEY[s]['id'] for s in src],'status':'covered',field:e,'clinical_certification':False} for i,(t,a,src,e) in enumerate(rows,1)]
 assert all(len(x[field])>=80 for x in result)
 (OUT/filename).write_text(json.dumps({'code':'C92','documented_at':now,'mode':'author_coverage_self_review',key:result,'clinical_certification':False,'meaning':'Couverture du contenu rédigé, pas score de qualité médicale ni validation humaine'},ensure_ascii=False,indent=2)+'\n')
text='# C92 — couverture documentée\n\nPorte de recherche passée avant rédaction ; 38 entrées initiales, trois FI ciblées supplémentaires après cette porte (41 au total). Les lectures ciblées et réutilisations sont attribuées, aucune lecture intégrale générale revendiquée.\n\n| Rubrique | Ancre | Sources | Couverture et limites |\n|---|---|---|---|\n'
for t,a,src,e in MATRIX:text+='| '+t+' | `'+a+'` | '+', '.join(BYKEY[s]['id'] for s in src)+' | '+e+' |\n'
(OUT/'coverage-final.md').write_text(text)
print('14 points et 20 rubriques documentés ; aucune clôture automatique.')
