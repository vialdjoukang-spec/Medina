# Rapport G93 — Autres affections du cerveau (cycle Betta 40, agent C40-A4-NEUR, rédaction Sonnet 5.5)

Audit différé — revue IA, distincte d'une validation médicale humaine.

## Fichiers produits
- chapters/G93/G93_a.html : 19395 octets
- chapters/G93/G93_b.html : 26715 octets
- chapters/G93/G93_c.html : 20095 octets
- chapters/G93/G93_d.html : 9108 octets
- chapters/G93/G93_pop1.html : 25044 octets
- chapters/G93/G93_pop2.html : 12416 octets
- glossary/g93.py : 5892 octets

Environ 12 000 mots ; 31 fenêtres (dont 8 Pareto) ; 4 quiz de cas cliniques ; 17 îlots de pathologie (0 à 16), 4 îlots d'examens, 3 sciences (anatomie, physiologie, biochimie) avec 3 schémas SVG noir et blanc plus la figure de Monro-Kellie, 5 îlots de pharmacologie.

## Sources utilisées (dossier recherche.md / sources.json uniquement)
S1 CIM-10-GM 2024 (BfArM) ; S2 recommandation européenne HII 2018 ; S3 Abbott 2023 (résumé) ; S4 ERC-ESICM 2021 ; S5 ERC-ESICM 2025 (existence seule, citée comme version non lue) ; S6 EUROMENE 2021 ; S7 Jha 2019 ; S8 EAN 2020 (résumé) ; S9 Schrör 2007 ; S10 Rabiei 2016 ; S11 information professionnelle Diamox ; S12 Mannitol 20 % ; S13 Aspirine. Aucune donnée extérieure au dossier n'a été ajoutée.

## Lacunes déclarées dans le cours (non comblées)
- Aucune recommandation suisse de société savante lue ; aucune donnée de fréquence suisse.
- Types cliniques d'engagement cérébral non décrits ; corticoïdes et sérum salé hypertonique (doses) non couverts.
- Dose d'acétazolamide dans l'HII, topiramate (information professionnelle), lévétiracétam et valproate : posologies non sourcées, indiquées comme telles.
- Critères de Friedman 2013 (figure) et classification de Frisén non lus ; valeurs ERC-ESICM datées 2021 avec mention de la version 2025 non lue.
- Reye (critères, biologie, traitement), kystes porencéphaliques, encéphalopathies G93.4 et post-radique : seule la nosologie est sourcée ; états de conscience (définitions) non lus ; directives suisses de mort cérébrale non lues.
- Conformément à la règle du projet, aucun tableau ni îlot n'est consacré au code CIM ; le périmètre est dans une fenêtre.

## Auto-contrôle (cahier W)
- HTML bien formé (analyseur de balises : pile vide) ; identifiants uniques et préfixés g93- ; toutes les clés data-k ont leur template data-pop et aucune fenêtre n'est orpheline.
- Audit des abréviations de build_medina (fonctions du dépôt, glossaire G93 chargé) : 0 non couverte. Pareto : ratios calculables, aucun îlot introuvable.
- test_preview non exécuté (injection hors périmètre de cette tâche).
