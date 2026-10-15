# Rapport de rédaction — G03 (cycle Betta 34, leçon 1, agent C34-A1-NEUR, Sonnet 5.5)

G03 — Méningite due à des causes autres et non précisées (N-05-Neurologie). Rédaction fondée uniquement sur `recherche.md` et `sources.json` (19 sources, S1 à S19).

## Fichiers (taille en octets)
-  27726 G03_a.html
-  24978 G03_b.html
-  25373 G03_c.html
-  14290 G03_d.html
-  18493 G03_pop1.html
-  11713 G03_pop2.html
- 122573 total
- glossary/g03.py : 4535

Empreintes SHA-256 :
```
b5c9d03b1ff754f12a45623bff2ff4642030ce60d726188cffaf97ea59d2503e chapters/G03/G03_a.html
fe9e123f0027f05f312c5e93e8ad2c6fb49a55756a7da66ecdfbb6beee5ad712 chapters/G03/G03_b.html
e8c24233083ac3eb1da282359315cf83721168a04eee733e6ecd52566b0c3731 chapters/G03/G03_c.html
31bd3f49fe27246ccbe3d23440c561a8f78633289db48f1abad4d919a96390ca chapters/G03/G03_d.html
2e57e747678ba707be783d202391bf7bab95043135f2811aebcca60094a62bb8 chapters/G03/G03_pop1.html
b02d90732a0bc572a40a387693d79e7b9261d0aa6d51fc6ee8cbbd666c03b44a chapters/G03/G03_pop2.html
97a050ada05083be685012d9f0f9fe8d962396eea764ab49d5c132deb73f309d glossary/g03.py
```

## Contenu
- Quatre onglets : Pathologie (îlots 0 à 12, dernier îlot = critères formels `div.alert` puis paramètres clés `div.key`), Examens (5 îlots, standard de référence nommé, tableau diagnostics × configurations, 4 quiz de cas), Sciences (physiologie, virologie et immunologie, cytologie ; 2 schémas SVG légendés), Pharmacologie (5 îlots).
- 37 fenêtres (`data-pop`) dont 8 Pareto, 3 pour l’onglet Pathologie, 1 pour les Examens, 3 pour les Sciences, 1 pour la Pharmacologie ; fenêtres de monographie : ceftriaxone, ampicilline, dexaméthasone, aciclovir, valaciclovir, ibuprofène, immunoglobulines (Privigen®) ; aide mnémotechnique marquée « non critère officiel ».
- Sources utilisées : S1 à S19. S5 (ESCMID 2016) uniquement telle que rapportée par S4.

## Auto-contrôle (cahier W)
- HTML bien formé sur la concaténation a+b+c+d ; identifiants uniques et tous préfixés `g03` ; toute clé `data-k` possède son `template data-pop` ; aucune fenêtre orpheline ; toutes les clés nouvelles préfixées `g03-` / `pareto-g03-`.
- Moteur `build_medina.audit` (copie hors racine, glossaire g03 ajouté) : 0 abréviation non couverte. Construction d'un aperçu hors dépôt et parcours navigateur : 177 mots verts et abréviations ouverts sur les 4 onglets, aucune fiche absente, aucune erreur JavaScript (hors la requête `lesson-core.js` du coque, absente de la racine et indépendante du cours).
- Aucun fichier hors du dossier de la leçon n'a été modifié ; aucun `git`.

## Lacunes (reprises du dossier de recherche, non comblées)
- Aucune source suisse spécifique ni épidémiologie suisse ; les chiffres d'incidence sont nord-américains, danois ou de seconde main.
- Texte intégral ESCMID 2016 et revues sur la méningite chronique non lus (résumés seuls) ; volumes de liquide, ponctions répétées et biopsie méningée non détaillés.
- Critères diagnostiques formels de Mollaret, guide pédiatrique et rattachement des formes médicamenteuses à G03.8 non vérifiés.
- Aucune information professionnelle suisse lue pour l'ampicilline, la dexaméthasone et la vancomycine ; mécanismes d'action et contre-indications des monographies non repris faute de source lue ; valeurs de référence du liquide normal absentes (seuils de décision seulement) ; grossesse non traitée.
- Anatomie et histologie des méninges non traitées dans les Sciences : aucune donnée correspondante dans le dossier.

Audit différé — revue IA, distincte d'une validation médicale humaine.
