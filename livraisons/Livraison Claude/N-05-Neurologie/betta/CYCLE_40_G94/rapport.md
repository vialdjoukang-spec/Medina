# Rapport G94 — Affections du cerveau au cours de maladies classées ailleurs (cycle Betta 40, agent C40-A4-NEUR, rédaction Sonnet 5.5)

Audit différé — revue IA, distincte d'une validation médicale humaine.

## Fichiers produits
- chapters/G94/G94_a.html : 22378 octets
- chapters/G94/G94_b.html : 18114 octets
- chapters/G94/G94_c.html : 22889 octets
- chapters/G94/G94_d.html : 7745 octets
- chapters/G94/G94_pop1.html : 13712 octets
- chapters/G94/G94_pop2.html : 18961 octets
- glossary/g94.py : 5316 octets

Environ 10 400 mots ; 35 fenêtres (dont 8 Pareto) ; 4 quiz de cas cliniques ; 13 îlots de pathologie (0 à 12), 5 îlots d'examens, 3 sciences (anatomie, physiologie, biochimie) avec 3 schémas SVG noir et blanc, plus la figure de séquence diagnostique, 4 îlots de pharmacologie.

## Sources utilisées (recherche.md / sources.json uniquement)
S1 CIM-10-GM 2024 (BfArM) ; S2 Sonneville 2023 ; S3 Shankar-Hari 2026 (résumé) ; S4 OUTCOMEREA 2025 (résumé) ; S5 Kasanmoentalib 2010 (résumé) ; S7 EANO-ESMO 2023 ; S8 EFNS 2010 (résumé) ; S9 Donovan 2019 (résumé) ; S10 ESO 2013 (résumé, section hydrocéphalie non lue) ; S11 EASL 2022 (exclusion seulement) ; S12 information professionnelle Benerva ; S13 information professionnelle dexaméthasone Galepharm. S6 (ESCMID 2016) non lue : aucune recommandation n'en est tirée. Aucune donnée extérieure au dossier n'a été ajoutée.

## Lacunes déclarées dans le cours
- Aucune source suisse de société savante ; aucune épidémiologie suisse ; ESCMID non lue ; conduite sur l'hydrocéphalie de l'hémorragie sous-arachnoïdienne non lue.
- Physiologie normale du liquide cérébrospinal, anatomie ventriculaire, encéphalopathies endocriniennes autres que Wernicke, G94.31 hors sepsis, G94.39, G94.8, causes parasitaires, pédiatrie, grossesse, sujet âgé : non sourcés, signalés comme tels.
- Dosages : pas de posologie de méningite de l'adulte pour la dexaméthasone ; contre-indications et interactions de la thiamine et de la dexaméthasone non lues ; divergence thiamine 3 × 200 mg (EFNS) contre jusqu'à 200 mg/jour (information suisse) présentée dans une fenêtre.
- Complément calculé (et signalé comme tel) : 17 à 39,5 % de cytologies initiales négatives, déduits des taux de positivité lus ; schémas anatomiques établis pour la leçon, non issus d'une source anatomique.
- Aucun îlot ni tableau consacré au code CIM : le périmètre est dans la fenêtre g94-cim.

## Auto-contrôle (cahier W)
- HTML bien formé (pile de balises vide, chapitre et fenêtres) ; identifiants uniques et préfixés g94- ; chaque clé data-k a sa fenêtre, aucune fenêtre orpheline ; couvertures Pareto résolues.
- Audit des abréviations (build_medina.audit avec glossaire G94 chargé) : 0 non couverte.
- test_preview non exécuté (injection hors périmètre de cette tâche).
