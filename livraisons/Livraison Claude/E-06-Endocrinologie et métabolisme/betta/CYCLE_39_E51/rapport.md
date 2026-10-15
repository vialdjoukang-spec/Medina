# Rapport de rédaction — E51 Carence en thiamine (E-06-Endocrinologie et métabolisme)

Cycle Betta 39, leçon 2. Agent de rédaction C39-A2-ENDO (Sonnet 5.5). Date : 15.10.2026. Dossier de recherche : `recherche.md` et `sources.json` (22 sources). Aucune donnée extérieure au dossier n'a été utilisée.

## Fichiers livrés
| Fichier | Octets |
|---|---|
| `chapters/E51/E51_a.html` | 24623 |
| `chapters/E51/E51_b.html` | 30338 |
| `chapters/E51/E51_c.html` | 22873 |
| `chapters/E51/E51_d.html` | 12997 |
| `chapters/E51/E51_pop1.html` | 30935 |
| `chapters/E51/E51_pop2.html` | 28153 |
| `glossary/e51.py` | 9871 |

Total : 159718 octets. Fenêtres explicatives : 41 ; fenêtres Pareto : 19 ; entrées de glossaire : 31. Quatre onglets (pA, pE, pS, pP) ; pathologie en 14 îlots (0 à 13) se terminant par les critères formels (`div.alert`) puis les paramètres clés (`div.key`) ; quatre sciences (biochimie, physiologie, neuroanatomie, nutrition humaine) ; pharmacologie en 5 îlots ; 4 cas à choix multiples.

## Sources utilisées
S1 à S22 du dossier : CIM-10-GM 2024 (S1), ESPEN 2022 micronutriments (S2), EFNS 2010 (S3, résumé), Benerva® Swissmedic avril 2019 (S4), Revue Médicale Suisse 2022 (S5, résumé), revues et séries S6 à S11, DGE (S12), renutrition suisse (S13, S14), séries Oudman (S15 à S17), GLP-1 (S18), Cochrane 2013 (S19), Royal College of Physicians (S20), SMOB 2023 (S21), ESPEN foie 2019 (S22).

## Arbitrages explicités dans le cours
- Écart entre l'information professionnelle suisse (parentéral jusqu'à 200 mg par jour) et ESPEN/EFNS (600 à 1500 mg par jour) : mot vert « Benerva® et écart de doses » ; la source primaire applicable la plus récente (ESPEN 2022) prime pour la conduite.
- Écart de sensibilité de l'IRM (53 % contre lésions typiques 82 %) ; écart de mortalité entre séries anciennes et méta-analyse 2026 ; écart des réserves corporelles (25 à 30 contre 30 à 50 mg) ; figure 1 de S7 inversant les rapports de sexe : texte retenu.
- Ordre thiamine puis glucose : consigne EFNS maintenue ; absence de recommandation lue pour l'hypoglycémie signalée sans la combler.

## Lacunes (non comblées, non inventées)
- Aucune recommandation suisse dédiée à l'encéphalopathie de Wernicke ou au béribéri ; recommandations de médecine des addictions non trouvées.
- EFNS, Revue Médicale Suisse et algorithme suisse de renutrition lus en résumé seulement.
- Codage CIM-10-GM du syndrome de Korsakoff non vérifié (omis) ; pas de sous-code E51.0 dans le relevé local ; cartographie CIM-11 non établie.
- Seuils de laboratoire suisses du ThDP, rôle du magnésium, diagnostic différentiel détaillé, autres spécialités suisses à base de thiamine : non sourcés, non écrits.
- Valeurs D-A-CH : page de la DGE seule ; adoption par la Société suisse de nutrition non vérifiée.

## Auto-contrôle (cahier W)
HTML bien formé (balises équilibrées) ; identifiants uniques et préfixés `e51-` ; toute clé de fenêtre `data-k` possède sa fenêtre ; aucune fenêtre orpheline ; couvertures Pareto valides ; `build_medina.audit` renvoie `{}` avec le glossaire e51 ; aucun marqueur de gabarit résiduel. Ni `chapters/` racine, ni `glossary/` racine, ni `chapters.json`, ni git n'ont été touchés.

Audit différé — revue IA, distincte d'une validation médicale humaine.
