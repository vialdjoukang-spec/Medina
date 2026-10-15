# Rapport G52 — Affections des autres nerfs crâniens (N-05-Neurologie)

Cycle Betta 37, leçon 2 (agent de rédaction C37-A3-NEUR, Sonnet 5.5), 15.10.2026. Audit différé — revue IA, distincte d'une validation médicale humaine.

## Fichiers (octets)
- chapters/G52/G52_a.html : 30456
- chapters/G52/G52_b.html : 21931
- chapters/G52/G52_c.html : 26724
- chapters/G52/G52_d.html : 8080
- chapters/G52/G52_pop1.html : 17712
- chapters/G52/G52_pop2.html : 19537
- glossary/g52.py : 14 entrées conditionnelles (ICHD-3, Collet-Sicard, Aguilera-Pena, Arnold-Chiari, EAN, PNS, GOS, TDI, HLA-B*1502, HLA-A*3101, H47.0, H93.3, H49.0, H49.2)

## Structure
Quatre onglets : pA (13 îlots, dernier îlot = critères formels `div.alert` puis paramètres `div.key`), pE (5 îlots dont 5 cas cliniques), pS (4 sciences : anatomie, histologie, physiologie, génétique et biochimie ; 4 figures SVG), pP (3 îlots : stratégie, doses sourcées, interactions et médicaments à éviter). 12 Pareto, 32 fenêtres de contenu (44 templates) dont deux arbitrages de source (traitement antithrombotique de la dissection ; oxcarbazépine hors indication suisse) et une aide mnémotechnique marquée « non critère officiel ».

## Sources utilisées
S1 à S19 du dossier (sources.json), chaque affirmation étant suivie de son étiquette courte ; références en fin d'îlot et de fenêtre. Sources américaines (Keane 2005, Lu 2018) citées uniquement comme données descriptives. Aucune donnée hors dossier, hormis des repères élémentaires signalés comme tels (définitions des composantes d'un test olfactif, numérotation des nerfs). Les chiffres romains IX, XI, XII et VIII sont écrits avec une entité HTML pour éviter la collision avec les facteurs de coagulation du glossaire racine ; le label du consensus rhinologique est « Consensus européen 2023 » pour éviter la collision de ERS avec European Respiratory Society.

## Lacunes (reprises du dossier)
Aucune recommandation suisse spécifique (SSN, Swiss Medical Forum) sur G 52 ; Revue Médicale Suisse lue en résumé seulement ; AWMF/DGHNO et DGN non lues ; G 52.2 (nerf vague) sans source spécifique ; syndromes de Vernet et de Tapia non définis ; syndrome d'Eagle et carcinome oropharyngé non sourcés ; liste des médicaments altérant l'odorat non relevée ; section COVID-19 du consensus non détaillée ; traitement antithrombotique actuel de la dissection (ESO) non lu, la conduite de 1998 est écartée ; gabapentinoïdes sans information professionnelle suisse lue ; doses de l'oxcarbazépine, des corticoïdes et du dupilumab non relevées ; grossesse et insuffisance rénale non traitées ; aucune épidémiologie suisse.

## Auto-contrôle (cahier W)
HTML bien formé (équilibre des balises sur a–d et pop1–pop2), identifiants uniques et préfixés g52-, toutes les clés de fenêtre existent (aucune orpheline), couvertures Pareto valides, `build_medina.audit()` = {} avec glossary/g52.py, transformation `transform`, `wrap_html` et `pareto_ratios` exécutées sans erreur. Aucun fichier hors du dossier de livraison n'a été modifié ; aucun contrôle navigateur n'a été exécuté.
