# Rapport de rédaction — G24 Dystonie (N-05-Neurologie)

Cycle Betta 36, agent C36-A1-NEUR, leçon 2. Rédaction Sonnet 5.5 sur `recherche.md` + `sources.json` (24 sources), sans donnée extérieure au dossier. Date : 15.10.2026.

## Fichiers
- chapters/G24/G24_a.html (pathologie 0–6, ~32 Ko), G24_b.html (pathologie 7–12 avec critères formels puis paramètres clés en dernier îlot, ~29 Ko), G24_c.html (Examens e-1 à e-5 ; Sciences : Anatomie, Histologie, Physiologie, Biochimie ; ~28 Ko), G24_d.html (Pharmacologie p-1 à p-4, ~10 Ko), G24_pop1.html (~26 Ko), G24_pop2.html (~22 Ko)
- glossary/g24.py (entrées conditionnelles, sans mutation des glossaires existants)

## Contenu
- 4 onglets, 12 Pareto, 48 fenêtres (36 explicatives, 12 Pareto), 5 cas corrigés, 4 schémas SVG légendés, tableaux introduits et commentés ; environ 10 000 mots de cours et 4 000 mots de fenêtres.
- Plan monographique classique, sans îlot ni tableau consacré au code CIM (codage en fenêtre `g24-cim`, en prose).
- Sources : S1–S2 classification ; S3 ligne directrice DGN 2021 ; S4–S5, S9 consensus de classification et terminologie ; S6–S8, S17 épidémiologie ; S10–S16 informations professionnelles suisses (BOTOX, Xeomin, Dysport, Akineton, Haldol, Paspertin, Xenazine) ; S18–S24 physiopathologie, toxine, physiothérapie, qualité des recommandations.

## Auto-contrôle
HTML bien formé (balises appariées), identifiants uniques et préfixés `g24-`, toutes les clés de fenêtre référencées existent et toutes les fenêtres sont référencées, couvertures Pareto résolues (fractions calculées par le moteur), audit d'abréviations `build_medina.audit()` = `{}` avec `glossary/g24.py`, aucune recommandation américaine.

## Lacunes (reprises du dossier)
Aucune recommandation suisse ni ligne directrice EAN récente ; la ligne directrice DGN 2021 est expirée et en révision ; plusieurs sources ne sont lues qu'en résumé ; épidémiologie suisse publiée absente (chiffre associatif de 12 000) ; informations professionnelles L-dopa et baclofène oral non lues, doses de lévodopa reprises de la DGN ; remboursement suisse non vérifié ; rattachement CIM de la dystonie laryngée, du syndrome de Meige, de la crampe de l'écrivain et de la dystonie tardive non vérifié ; neuropathologie non lue (onglet Histologie volontairement mince et signalé) ; mécanisme du geste antagoniste et de la maladie de Wilson non établis dans les sources lues. Les vignettes et cas sont fictifs et signalés. Les développements des symboles de gènes et d'échelles (glossaire) sont des expansions conventionnelles, non issues du dossier.

Audit différé — revue IA, distincte d'une validation médicale humaine.
