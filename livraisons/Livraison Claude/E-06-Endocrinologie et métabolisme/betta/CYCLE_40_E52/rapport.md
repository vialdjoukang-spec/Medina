# Rapport de rédaction — E52 Carence en acide nicotinique [pellagre]

Cycle Betta 40, leçon 1, agent C40-A2-ENDO (Sonnet 5.5), fragment E-06-Endocrinologie et métabolisme. Date : 15.10.2026. **Audit différé — revue IA, distincte d'une validation médicale humaine.**

## Fichiers (dossier de la leçon uniquement)
| Fichier | Octets |
|---|---|
| chapters/E52/E52_a.html (îlots 0–6) | 37905 |
| chapters/E52/E52_b.html (îlots 7–13) | 26785 |
| chapters/E52/E52_c.html (Examens, Sciences) | 35259 |
| chapters/E52/E52_d.html (Pharmacologie) | 13173 |
| chapters/E52/E52_pop1.html (22 fenêtres de concepts) | 32347 |
| chapters/E52/E52_pop2.html (7 fenêtres pharmacologie, 10 Pareto) | 17077 |
| glossary/e52.py (20 entrées conditionnelles) | 6913 |

Au total : environ 16 700 mots, 39 fenêtres (clés `e52-…` et `pareto-e52-…`), 5 quiz de cas, 4 figures SVG noir et blanc légendées, 10 Pareto.

## Contenu
Onglet Pathologie : 14 îlots (question clinique, définitions et classifications, épidémiologie, du normal au pathologique, causes, anamnèse, examen, diagnostic, gravité et pièges, traitement, traitement de la cause, suivi et prévention, situations particulières avec cas récapitulatif, critères formels `div.alert` puis paramètres clés `div.key`). Onglet Examens : 5 îlots dont l'entraînement. Onglet Sciences : biochimie, physiologie, peau et histologie, neurobiologie. Onglet Pharmacologie : 5 îlots.

## Sources utilisées
Uniquement les sources S1 à S24 du dossier `sources.json` : ESPEN 2022, OMS 2000, DGE/ÖGE, CIM-10-GM 2024 (OFS, BfArM), revue systématique 2026, Serdaru 1988, étude cas-témoins Malawi 2022, cas rapportés, informations professionnelles suisses (Bécozyme forte mars 2026, Soluvit N novembre 2022, Cernévit juillet 2023), directives SMOB 2023. Aucune donnée extérieure au dossier n'a été ajoutée ; les formulations d'inférence sont signalées comme telles ou omises.

## Lacunes conservées (reprises du dossier)
1. Aucune source suisse propre à la pellagre ; épidémiologie suisse inconnue.
2. Aucune monopréparation suisse de nicotinamide ; 300 mg par jour non atteignable dans la posologie autorisée de Bécozyme forte (6 dragées contre 2 à 3) ; voie d'obtention non documentée (aucun contournement proposé).
3. Texte EFSA inaccessible : limites supérieures citées de seconde main par l'ESPEN.
4. Doses intramusculaires et intraveineuses « OMS » non retrouvées dans la source primaire : non utilisées.
5. Date de Casal (1763 ou 1735), mortalité actuelle, adoption suisse des valeurs DGE/ÖGE : non résolues.
6. Prise en charge de la maladie de Hartnup, liste complète des médicaments inducteurs, détails de l'information professionnelle de Cernévit : non documentés.

## Auto-contrôle du cahier W
- Contrôle de construction (copie de travail hors dépôt, `build_medina.py E52`) : **E52 non couvertes: 0**, aucune erreur Pareto.
- Contrôle navigateur (`test_preview.py E52`) : **OK** (l'erreur historique `lesson-core.js`, propre aux fichiers locaux, est ignorée comme dans `captures_front.py`).
- HTML bien formé : pile de balises vide ; identifiants uniques et préfixés `e52-` ; toute clé `data-k` possède son `template data-pop` et aucune fenêtre n'est orpheline.
- Abréviations : aucune hors glossaire (`audit()` renvoie vide) ; « IV », « /j » et abréviations non définies évités.
- Aucun fichier de la racine du dépôt (`chapters/`, `glossary/`, `chapters.json`) n'a été modifié ; aucune opération git.

## Empreintes (sha256, 12 premiers caractères)
```
da7575dd5850…  chapters/E52/E52_a.html
9c45858590ca…  chapters/E52/E52_b.html
ccb5e4d555ed…  chapters/E52/E52_c.html
053a5a583335…  chapters/E52/E52_d.html
5907ba05463f…  chapters/E52/E52_pop1.html
b5d264308efc…  chapters/E52/E52_pop2.html
a7f5247fb951…  glossary/e52.py
```
