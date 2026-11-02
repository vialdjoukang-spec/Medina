#!/usr/bin/env python3
"""Matrice de couverture rédigée par l'auteur ; ce script ne juge pas la médecine."""
from pathlib import Path
import json,datetime
from author_popups import SOURCE_ID
OUT=Path(__file__).resolve().parent
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
MONO=[
('Définition','c86-1',['CIM','OMS22','OMS-DC'],'Les sept sous-codes sont reliés à plusieurs entités, avec BPDCN de lignée dendritique et séparation du codage historique et du diagnostic biologique.'),
('Épidémiologie','c86-2',['SZO','ONKO','WHO-CUT','CARVAO'],'Les proportions suisses datées, registres cutanés et risques de thiopurines gardent population, dénominateur et horizon non annuel ; incidence actuelle par sous-code non inventée.'),
('Physiopathologie','c86-3',['OMS22','TSE','MOONLA','HLH23'],'Six sciences relient fonctionnement normal, tissu, anomalie et signes ; mécanismes EBV/P-gp/asparagine, microenvironnement TFH et régulation TIM-3 sont expliqués.'),
('Démarche clinique','c86-7',['ESMO25','CUT18','BPDCN23'],'Le parcours part du siège et de la gravité, choisit un prélèvement adapté, confronte phénotype et contexte puis extension, aptitude et stratégie sans batterie uniforme.'),
('Anamnèse','c86-5',['TSE','CARVAO','ESsCD26','KEMPF'],'Chronologie, siège, traitements, symptômes généraux, résolution des papules et contraintes du patient sont exposés avec lien mécanistique et diagnostics alternatifs.'),
('Examen clinique','c86-6',['TSE','CARVAO','KEMPF','HLH23'],'L’examen distingue fonctions vitales, organomégalie, ganglions, muqueuses, peau profonde et signes sanguins ; la normalité ganglionnaire ne rassure pas sur HSTL.'),
('Syndromes','c86-8',['HLH19','HLH23','ELZONRIS','ESsCD26'],'Hyperinflammation, complications digestives/respiratoires et toxicités sont reliées aux signes, aux seuils contextuels et à une prise en charge parallèle en cas de gravité.'),
('Diagnostic positif','c86-12',['OMS22','OMS-DC','ESsCD26','KEMPF'],'Critères formels intégrés pour ENKTL, TFH, BPDCN, RCD-II et pcALCL ; aucun marqueur isolé ni deux marqueurs hors contexte ne sont présentés comme diagnostic suffisant.'),
('Explorations','c86-e-1',['ESMO25','CUT18','ESGE22','BPDCN23'],'Chaque examen répond à une question, avec indications conditionnelles, limites de TEP/clonalité et risque de rétention ; références biologiques suisses datées séparées des seuils.'),
('Arbre diagnostique','c86-7',['ESMO25','LUPUS','WHO-CUT','ESsCD26'],'Les étapes prélèvement, classification, extension, terrain et réévaluation forment une séquence décisionnelle ; tableau différentiel et vignettes explicitent les bifurcations.'),
('Prise en charge','c86-9',['ESMO25','ADCETRIS','ELZONRIS','ONCASPAR','S2K'],'Stratégies par entité/aptitude, objectifs et choix partagés ; trois FI exactes, autorisation et remboursement distingués, autogreffe et allogreffe expliquées.'),
('Prévention et suivi','c86-10',['ESMO25','KEMPF','CARVAO'],'Suivi PTCL avec conditions de rémission et statut de greffe ; LyP à vie, RCD-II individualisé ; pas d’arrêt universel de thiopurine à deux ans.'),
('Points clés','c86-12',['ELZONRIS','ADCETRIS','MEBEKO26','PROFILES17'],'Calculs de pourcentage, poids-dose et conversion d’albumine ; seuils attachés à leur finalité et ancrage fédéral 2017/2026 versus2028 explicités.'),
('Pièges','c86-e-2',['HUG','ELZONRIS','KEMPF','ESMO25'],'Pièges repris dans les sections, les52fenêtres,14synthèses et cinqquiz : seuils distincts, populations, clonalité, surtraitement cutané et résultats de séries.')]
points=[{'point':i,'title':title,'anchor':anchor,'sources':[SOURCE_ID[k] for k in src],'status':'covered','clinical_certification':False,'coverage_explanation':explanation} for i,(title,anchor,src,explanation) in enumerate(MONO,1)]
MATRIX=[
('Question clinique et examen fédéral','c86-0',['ESMO25','PROFILES17','MEBEKO26','PROFILES-TRANS'],'Troisvignettes structurent les décisions ; SSP2017 réelles et transition examen2028 distinguées, sans prédiction d’épreuve.'),
('Définition et périmètre CIM-10-GM','c86-1',['CIM','OMS-DC'],'C86.0–C86.6 expliqués ; septsous-codes ne signifient pas septmaladies ni une lignée unique ; codage2024 non présenté comme certification2026.'),
('Classifications et stades','c86-stad-cutanee',['OMS22','WHO-CUT','ESMO25','KEMPF'],'OMS/ICC et nomenclature cutanée séparées du code ; extension systémique versus cutanée et limites de l’usage automatique d’AnnArbor.'),
('Épidémiologie suisse et européenne','c86-2',['SZO','ONKO','WHO-CUT','CARVAO'],'Sources suisses secondairesdatées et registres européens ; risque thiopurines limité aux hommes<35ans ; incidence suisse par sous-code reste nonétablie.'),
('Normal vers pathologique','c86-s-semio',['NORMAL-A','NORMAL-T','OMS22','TSE'],'Sixsciences, neufsections sémiologiques, quatreoccurrences originales et deuxdiagrammes causaux ; fonctions normales vers signes/examens/traitements.'),
('Étiologies et facteurs de risque','c86-4',['CARVAO','MOONLA','ESsCD26','OMS22'],'Associations distinguées des causes ; génotypes et populations explicites, pas fréquenceuniverselle HAVCR2 ni arrêt automatique aprèsdeuxans.'),
('Anamnèse et symptômes','c86-5',['TSE','CARVAO','KEMPF','ESsCD26'],'Site, évolution, immunosuppression, nutrition, signesgénéraux et résolutioncutanée orientent sans diagnostiquer seuls.'),
('Examen clinique','c86-6',['TSE','CARVAO','KEMPF'],'Fonctionsvitales, ORL, organes, peau/hypoderme, ganglions et signes sanguins ; données de séries ne sont pas sensibilités de tests.'),
('Drapeaux rouges et urgences','c86-8',['HLH19','HLH23','ELZONRIS','ESsCD26'],'HLH et organes, obstruction ORL, complication digestive, fuitecapillaire/LEMP/pancréatite ; actionpendant bilan si gravité.'),
('Examens complémentaires','c86-e-1',['ESMO25','ESGE22','HUG','BPDCN23'],'Hiérarchie, indications selonentité, prélèvement, limites TEP/clonalité, risque capsule et seuils biologiquescontextuels.'),
('Diagnostic différentiel','c86-7',['LUPUS','WHO-CUT','OMS-DC','ESsCD26'],'Panniculitelupique/SPTCL/gamma-delta, LyP/pcALCL/systémique, BPDCN/autrelignée et RCD/EATL comparés avec élémentsdiscriminants et limites.'),
('Prise en charge suisse et FI','c86-p-2',['ADCETRIS','ELZONRIS','ONCASPAR','ESMO25'],'TroisFI exactes ; doses de produit/indication, adaptations parschéma, G-CSF, bléomycine et LEMP ; posologieLLA pas transposée ENKTL.'),
('Complications et pronostic','c86-10',['WHO-CUT','CUT18','ELZONRIS','ESMO25'],'Survies spécifiques/globales, cohortes sélectionnées et dénominateurs de sécurité distincts ; pas pronostic individuel déduit du pourcentage.'),
('Suivi, prévention, dépistage','c86-10',['ESMO25','KEMPF','CARVAO'],'Suivi de rémission, LyPàvie, RCD-II et absence d’imagerie systématique PTCL ; prévention personnalisée et signes à signaler.'),
('Situations particulières','c86-11',['ADCETRIS','ELZONRIS','BPDCN23','MOONLA'],'Pédiatrie, fragilité, grossesse/fertilité, fonctionsd’organes, Crohn/cœliaque et SNC ; aucune extrapolation de dose adulte àl’enfant.'),
('Spécificités administratives suisses','c86-statut-ch',['OFSP','OAMAL','ADCETRIS','ONCASPAR'],'Autorisation, LS et art.71a–d expliqués ; limitations/remboursementindividuels2026 noncertifiés, conditions à vérifier avant décision.'),
('Diagnostic formel','c86-12',['OMS22','OMS-DC','ESsCD26','HLH19'],'Combinaisons et exclusions détaillées ; contexte, architecture et méthode gardés, pas raccourci EBER+CD56 ou TFH≥2 seuls.'),
('Paramètres clés chiffrés','c86-e-2',['HUG','ELZONRIS','ADCETRIS','CARVAO'],'RepèresHUG datés, critèresHLH, albuminepremièredose versus sous traitement, calculs depuisbases et population desrisques.'),
('Sous-codes couverts','c86-1',['CIM','OMS22','OMS-DC'],'Sept sous-codesC86.0àC86.6 couverts ; frontières C84.6/C84.7, MEITL, gamma-delta cutané et leucémieNK agressive conservées.'),
('Points d’examen fédéral','c86-e-5',['PROFILES17','MEBEKO26','PROFILES-TRANS','ESMO25'],'Cinqquiz expliqués et14synthèses ; situations cliniquesréelles du référentiel, pas d’affirmation sur fréquence de questions fédérales.')]
rubrics=[{'point':i,'title':title,'status':'covered','sources':[SOURCE_ID[k] for k in src],'anchor':anchor,'evidence':evidence} for i,(title,anchor,src,evidence) in enumerate(MATRIX,1)]
for name,key,data in [('monograph-14.json','points',points),('matrix-20.json','rubrics',rubrics)]:
 (OUT/name).write_text(json.dumps({'code':'C86','reviewed_at':now,'mode':'author_coverage_self_review',key:data,'clinical_certification':False,'meaning':'Couverture documentée, pas score de qualité ni certification médicale.'},ensure_ascii=False,indent=2)+'\n')
text='# C86 — recherche et couverture\n\n31sources avec passages, populations et limites ; une lecture de résumé explicitement nommée. Auto-relecture attribuée, sans certification humaine. Sources historiques conservées séparément.\n\n## Matrice de complétude\n\n| Rubrique | Statut | Sources | Ancre | Preuve et limite |\n|---|---|---|---|---|\n'
for x in rubrics:text+=f"| {x['point']}. {x['title']} | ✔ | "+', '.join('['+s+']' for s in x['sources'])+f" | `{x['anchor']}` | {x['evidence']} |\n"
text+='\n## Périmètre et limites\n\nC86.0, C86.1, C86.2, C86.3, C86.4, C86.5 et C86.6 : les correspondances ne remplacent pas une classification biologique. Incidence suisse par sous-code et remboursement individuel2026 non établis. Les recommandations européennes/internationales et FI suisses fondent la conduite ; OpenStax est utilisé seulement pour des bases biologiques normales paraphrasées, aucune recommandation clinique américaine ni figure reprise. Les passages téléchargés mais non parcourus ne sont pas déclarés lus.\n'
(OUT/'recherche_C86/recherche.md').write_text(text)
print('Couverture rédigée : 14 points / 20 rubriques ; vérification finale et source-binding encore requis.')
