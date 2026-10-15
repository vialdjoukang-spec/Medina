# Rapport G53 — Affections des nerfs crâniens au cours de maladies classées ailleurs (N-05-Neurologie)

Cycle Betta 37, leçon 1 (agent de rédaction C37-A4-NEUR, Sonnet 5.5), 15.10.2026. Audit différé — revue IA, distincte d'une validation médicale humaine.

## Fichiers (octets)
- chapters/G53/G53_a.html : 30246
- chapters/G53/G53_b.html : 26638
- chapters/G53/G53_c.html : 25686
- chapters/G53/G53_d.html : 11339
- chapters/G53/G53_pop1.html : 19467
- chapters/G53/G53_pop2.html : 21696
- glossary/g53.py : 12 entrées conditionnelles (B02.2, CXCL13, DGN, EANO, EFNS, HC, Herrero-Morant, ID, MRZ, Melkersson-Rosenthal, SNG, anti-MOG)

## Structure
Quatre onglets : pA (13 îlots, dernier îlot = critères formels `div.alert` puis paramètres `div.key`), pE (5 îlots dont 4 cas cliniques), pS (5 sciences : anatomie, histologie, physiologie, biochimie, immunologie ; 2 figures SVG de sciences, 2 de pathologie), pP (3 îlots : stratégie, doses sourcées, interactions et médicaments à éviter). 34 fenêtres de contenu et 13 Pareto (47 templates), dont un arbitrage de source (EFNS 2010 / revue 2016) et une aide mnémotechnique marquée « non critère officiel ».

## Sources utilisées
S1 à S32 du dossier (sources.json), chaque affirmation étant suivie de son étiquette courte ; références en fin d'îlot et de fenêtre. Sources américaines (Keane 2005, Stern 2018, Daly 2026, cohorte cardiaque 2024) citées uniquement comme données descriptives ou définitions, jamais comme fondement d'une conduite. Aucune donnée hors dossier, hormis trois repères anatomiques ou physiologiques élémentaires (trijumeau = nerf V, espaces sous-arachnoïdiens, barrière hémato-liquidienne) signalés comme tels dans leur fenêtre.

## Lacunes (reprises du dossier)
Aucune source suisse propre à G 53 (contribution suisse : Plan de vaccination 2026, informations professionnelles Swissmedic, directives DGN coapprouvées par la SNG) ; AWMF 030-114 et directive de la parésie faciale non lues ; EFNS 2010, EDF-EADV, ERS 2021, Arztebl 2016/2019 lus au résumé ; doses d'antibiotiques de la neuroborréliose non extraites ; épidémiologie suisse du zona non lue ; G 53.8 sans directive (cas cliniques seulement) ; démarche LCR de la syphilis oculaire/otologique non extraite ; informations professionnelles suisses des antibiotiques, corticoïdes, méthotrexate, infliximab et produits intrathécaux non lues ; valeurs normales de référence du laboratoire non fournies.

## Auto-contrôle (cahier W)
HTML bien formé (analyse d'équilibre des balises sur a–d et pop1–pop2), identifiants uniques et préfixés g53-, toutes les clés de fenêtre existent (aucune orpheline), couvertures Pareto valides, audit des abréviations `build_medina.audit()` = {} (build G53 : non couvertes 0, avec glossary/g53.py), contrôle navigateur du rendu (fenêtres, onglets, mode livre) OK ; seul l'import dynamique de preview/lesson-core.js, absent de ce dépôt (donc commun à tous les chapitres), n'a pas pu être chargé. Aucun fichier hors du dossier de livraison n'a été modifié (le banc d'essai a utilisé une racine temporaire en liens symboliques).
