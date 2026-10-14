# Rapport de rédaction — D71 Anomalies fonctionnelles des granulocytes neutrophiles (H-08-Hématologie)

Cycle Betta 31, agent C31-A4-HEM, leçon 2 (Sonnet 5.5). Date : 14.10.2026.
Audit différé — revue IA, distincte d'une validation médicale humaine.

## Fichiers livrés (dossier CYCLE_31_D71)
- chapters/D71/D71_a.html (43 Ko) : en-tête, quatre onglets, Pathologie îlots 0 à 6 (question clinique, nosologie CIM-10-GM, épidémiologie, physiopathologie, causes, anamnèse, examen).
- chapters/D71/D71_b.html (43 Ko) : îlots 7 à 14 (diagnostic et différentiel, urgences, prophylaxie, traitement des infections et de l'inflammation, greffe, suivi, situations particulières, puis critères formels `alert` et paramètres clés `key`).
- chapters/D71/D71_c.html (31 Ko) : Examens (5 îlots, 5 fiches, tableau des configurations, 3 quiz) et Sciences (Physiologie, Biochimie, Hématologie cellulaire, Génétique ; 2 schémas SVG noir et blanc légendés).
- chapters/D71/D71_d.html (16 Ko) : Pharmacologie (5 îlots, tableau de doses sourcées, encadré d'interactions).
- chapters/D71/D71_pop1.html (33 Ko), D71_pop2.html (7 Ko) : 48 fenêtres dont 9 Pareto (clés `d71-…`, `pareto-d71-…`).
- glossary/d71.py : 45 entrées conditionnelles (CGD, LAD, CR3, CD18, gènes, DHR, NBT, PMA, etc.).
- Environ 12 800 mots de cours et 3 800 mots de fenêtres ; 7 quiz de cas pédagogiques fictifs (2 en Pathologie, 3 en Examens, 1 en Pharmacologie, 1 supplémentaire en îlot 7).

## Sources utilisées (toutes issues de sources.json, consultées le 14.10.2026)
CIM-10-GM 2024 (BfArM) ; Seger 2010, 2011, 2002 ; Güngör 2014 ; Reichenbach 2009 ; van den Berg 2009 (cohorte européenne) ; Staudacher et von Bernuth 2024 ; Yu 2021 ; Kuhns 2010 ; Mauch 2007 ; van de Vijver (Roos) 2012 ; Fekadu 2022 ; Roh 2020 ; Ahdab 2026 ; informations professionnelles Bactrim forte® (mars 2023), Itraconazole Sandoz® eco (novembre 2024), Posaconazol Zentiva® (octobre 2025). Aucune donnée hors dossier. Quelques articulations de raisonnement (ligne LAD-I du tableau des configurations, ordre des étapes de la sortie du neutrophile, lecture de la divergence des taux de colite) sont signalées comme telles dans le texte.

## Lacunes explicites (reprises dans l'îlot 14 et la fenêtre « Sources »)
Aucune recommandation officielle suisse, ESID ou EHA et aucun critère diagnostique formel lu (critères de l'îlot 14 opérationnels) ; aucune information professionnelle suisse pour l'interféron γ ni pour le voriconazole ; prophylaxie de la granulomatose hors indication libellée dans les informations suisses ; doses adultes absentes ; classification IUIS 2024 non lue ; codage de LAD-II et LAD-III non vérifié ; taux de colite divergents ; explication causale de la règle de la catalase absente des sources ; aucune valeur de référence chiffrée du DHR ni du NBT ; autres anomalies fonctionnelles (déficit en granules spécifiques) non documentées.

## Auto-contrôle du cahier W
- Quatre onglets pA, pE, pS, pP ; dernier îlot de la pathologie = critères formels (`div.alert`) puis paramètres clés (`div.key`) ; Pareto en fin de chaque grande partie (pathologie ×3, examens, sciences ×4, pharmacologie).
- HTML bien formé (analyse de pile balises : aucune erreur), identifiants uniques et préfixés `d71-`, toutes les clés `data-k` ont leur fenêtre (48 fenêtres, 0 manquante, 0 inutilisée), aucune clé non préfixée.
- Glossaire : `build_medina.audit` renvoie « D71 non couvertes: 0 ».
- Aperçu navigateur (harnais isolé hors dépôt) : cours construit sans erreur ; seule l'erreur d'environnement `lesson-core.js` du script d'origine apparaît, comme pour D63.
- Rien n'a été modifié dans chapters/ racine, glossary/ racine, chapters.json ni git.
