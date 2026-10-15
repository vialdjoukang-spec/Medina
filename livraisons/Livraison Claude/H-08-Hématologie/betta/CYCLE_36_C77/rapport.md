# Rapport de rédaction — C77 Tumeur maligne des ganglions lymphatiques, secondaire et non précisée (cycle Betta 36, agent C36-A3-HEM, Sonnet 5.5)

Audit différé — revue IA, distincte d'une validation médicale humaine.

## Fichiers (octets)
```
20550 chapters/C77/C77_a.html
15170 chapters/C77/C77_b.html
21925 chapters/C77/C77_c.html
 8569 chapters/C77/C77_d.html
21880 chapters/C77/C77_pop1.html
23698 chapters/C77/C77_pop2.html
10782 glossary/c77.py
```
Total des six fichiers HTML : 111 792 octets. Environ 7 300 mots dans les quatre onglets, 6 quiz (dont 3 dans l'onglet Examens), 60 mots verts, 55 fenêtres (35 explicatives, 20 Pareto), 4 schémas SVG noir et blanc légendés (un par science).

## Sources utilisées
Uniquement celles de recherche.md / sources.json (9 sources, consultées le 15.10.2026) : BfArM et OFS (CIM-10-GM 2024), Swiss Medical Weekly 2024 (Hanzalová et Matter), Onkopedia CUP 2025, ESMO CUP 2023 (métadonnées seulement), Bochtler 2023 (résumé), Eur J Med Res 2023 (cancer gastrique), informations professionnelles suisses du carboplatine et du paclitaxel. Aucune donnée extérieure au dossier.

## Auto-contrôle du cahier W
- HTML bien formé : analyse balise par balise des six fichiers, aucune balise déséquilibrée sur l'ensemble.
- Identifiants uniques, tous préfixés c77- ; toutes les clés data-k ont leur template data-pop, aucune fenêtre orpheline, toutes les clés de fenêtres préfixées c77- ou pareto-c77- ; chaque data-cover désigne un îlot existant.
- Quatre onglets pA, pE, pS, pP ; dernier îlot de la pathologie : div.alert (critères formels) puis div.key (paramètres clés), références ensuite ; Pareto en fin de chaque grande partie.
- Glossaire : build_medina.audit() renvoie 0 abréviation non couverte (« C77 non couvertes: 0 »), mesuré dans un répertoire de travail temporaire hors dépôt avec le glossaire racine et glossary/c77.py.
- Contrôle navigateur (copie de test_preview.py hors dépôt) : OK. L'erreur d'import dynamique « lesson-core.js » du script d'origine est antérieure à ce chapitre (identique sur D50) ; elle a été ignorée dans la copie de test.
- Aucun îlot ni tableau consacré au code CIM : le périmètre et les sous-codes sont dans une fenêtre (c77-codage) et dans une colonne du tableau de topographie.

## Lacunes (reprises du dossier de recherche, aucune comblée de mémoire)
Texte intégral ESMO 2023 et ligne directrice EHNS-ESMO-ESTRO 2020 non lus ; aucune épidémiologie suisse du CUP ou de C77 ; aucune recommandation d'une société suisse propre au CUP ; informations professionnelles du cisplatine, de la gemcitabine et de l'atézolizumab non lues (aucune dose donnée) ; dose initiale du paclitaxel non extraite ; mécanismes d'action des médicaments limités à leur classe ; interactions médicamenteuses absentes des extraits ; valeurs normales de laboratoire absentes ; urgences oncologiques aiguës, prévention, grossesse (hors contre-indication du carboplatine), conduite diagnostique chez l'enfant : non traitées faute de source ; primitifs des ganglions intra-abdominaux et intrapelviens non détaillés ; sens exact de l'écart 57 % contre 82 % (rupture capsulaire) non précisé dans le dossier ; mécanisme de la lymphangiogenèse issu d'une revue sur le cancer gastrique, généralisation à prudence.
