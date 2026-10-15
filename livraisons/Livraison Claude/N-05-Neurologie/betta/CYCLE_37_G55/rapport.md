# Rapport G55 — Compression des racines et des plexus nerveux au cours de maladies classées ailleurs (N-05-Neurologie)

Cycle Betta 37, leçon 2 (agent de rédaction C37-A4-NEUR, Sonnet 5.5), 15.10.2026. Audit différé — revue IA, distincte d'une validation médicale humaine.

## Fichiers (octets)
- chapters/G55/G55_a.html : 37200
- chapters/G55/G55_b.html : 55677
- chapters/G55/G55_c.html : 33195
- chapters/G55/G55_d.html : 11565
- chapters/G55/G55_pop1.html : 37712
- chapters/G55/G55_pop2.html : 59684
- glossary/g55.py : 11 entrées conditionnelles (L5, G55.0, G55.1, G55.2, G55.3, G55.8, NG59, NG234, Parsonage-Turner, HC, Ibuprofen-Mepha)

## Structure
Quatre onglets. pA : 13 îlots (question clinique, définitions et classifications, fréquence, physiopathologie, causes, anamnèse, examen, démarche diagnostique et différentiel hiérarchisé, urgences, prise en charge, suivi, situations particulières ; dernier îlot = critères formels `div.alert` puis paramètres clés `div.key`), section `src`. pE : 4 îlots (hiérarchie question → examen → statut avec gold standard nommé, fiches d'interprétation, tableau configurations × examens, 4 cas cliniques). pS : 4 sciences (anatomie, histologie, physiologie, biochimie), chacune avec schéma SVG noir et blanc légendé et trois corrélations `key`. pP : 3 îlots (stratégie par phénotype, posologies sourcées, contre-indications et médicaments à éviter). Plan monographique classique : le code CIM n'a ni îlot ni tableau propre (une fenêtre de texte explique le code de manifestation).
Volume : environ 19 900 mots ; 71 templates (50 fenêtres de contenu, 21 Pareto) ; 6 quiz ; 6 figures SVG (2 en pathologie, 4 en sciences) ; 1 arbitrage de source sur la durée du traitement conservateur et 1 sur les gabapentinoïdes (NICE contre information professionnelle suisse), avec accès aux textes plus anciens ; 1 aide mnémotechnique marquée « aide pédagogique, non critère officiel ».

## Sources utilisées
S1 à S35 du dossier (sources.json) : revues suisses (Revue Médicale Suisse 2010–2016, Swiss Medical Weekly), européennes (Deutsches Ärzteblatt 2019–2025, NICE NG59 et NG234, méta-analyses européennes), informations professionnelles Swissmedic (ibuprofène, dexaméthasone, prégabaline, consultées le 15.10.2026). Les sources non européennes (S22, S29, S31, S32) ne servent que de définitions, de mécanismes ou de données descriptives, signalées comme telles. Aucune donnée hors dossier, hormis la définition d'usage du Lasègue croisé, signalée dans sa fenêtre comme non détaillée par les sources.

## Lacunes (reprises du dossier)
Aucune recommandation de la société suisse de neurologie ni du Swiss Medical Forum ; directives allemandes S2k non lues (citées via Kögl 2024) ; aucune recommandation de la Société européenne de neurologie ni de la Société européenne d'oncologie médicale ; plexopathies tumorales (G55.0) et G55.8 documentées seulement par résumés et cas ; plexus lombosacré non documenté ; aucun traitement de plexopathie documenté ; équivalent suisse du coordinateur britannique de compression médullaire non documenté ; items et seuils des scores SINS et Tokuhashi non lus ; informations professionnelles du paracétamol, des opioïdes, des autres anti-inflammatoires et des myorelaxants non lues ; sections d'interactions, mécanismes et effets indésirables des trois informations professionnelles non extraits ; valeurs normales de laboratoire et seuil de résidu post-mictionnel non fournis ; la grossesse et les insuffisances rénale ou hépatique n'ont pas de recommandation propre dans le dossier.

## Auto-contrôle (cahier W)
HTML bien formé (équilibre des balises vérifié sur a–d en continu, pop1, pop2) ; identifiants uniques et préfixés g55- ; 50 clés de fenêtre référencées et toutes définies, aucune fenêtre orpheline ; couvertures Pareto valides ; `build_medina.py G55` sur racine temporaire en liens symboliques : « G55 non couvertes: 0 », audit des abréviations = {} ; `test_preview.py G55` : seul échec, l'import dynamique de lesson-core.js, absent du dépôt (commun à tous les chapitres, déjà noté pour G53). Aucun fichier hors du dossier de livraison n'a été modifié ; chapters/ racine, glossary/ racine, chapters.json et git non touchés.
