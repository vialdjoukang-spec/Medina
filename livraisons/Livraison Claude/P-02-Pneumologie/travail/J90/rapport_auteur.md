# Rapport d’auteur — J90 — Épanchements pleuraux (P-02-Pneumologie)

Rédacteur de la chaîne interne Claude, 08.10.2026. Version de travail : ni relue, ni injectée, ni validée par un médecin. Une revue IA et des tests techniques ne constituent pas une validation médicale.

## Couverture

- J90 — Épanchement pleural, non classé ailleurs
- J91 — Épanchement pleural au cours de maladies classées ailleurs (code étoile)
- J94 — Autres affections pleurales : J94.0 — Épanchement chyleux ; J94.1 — Fibrothorax ; J94.2 — Hémothorax ; J94.8 ; J94.9

Libellés vérifiés sur la CIM-10-GM 2024 (BfArM, bloc J90–J94), consultée le 08.10.2026. Renvois sans second cours : J86 — Pleurésies purulentes et abcès du poumon (épanchement parapneumonique compliqué, fibrinolytiques), I50 — Insuffisance cardiaque, I26 — Embolie pulmonaire aiguë, J93 — Pneumothorax ; tuberculose pleurale (A15–A16) traitée pour son diagnostic seulement.

## Fichiers

- `chapters/J90/J90_a.html` — en-tête, onglets, îlots 0 à 6 (Pareto clinique)
- `chapters/J90/J90_b.html` — îlots 7 à 13 (Pareto diagnostic, prise en charge, critères) ; dernier îlot : `div.alert` critères formels puis `div.key` paramètres clés
- `chapters/J90/J90_c.html` — onglet Examens (5 îlots, 3 quiz, Pareto) et onglet Sciences (anatomie, histologie, physiologie, biochimie ; 3 schémas SVG + figure 1 de l’onglet 1)
- `chapters/J90/J90_d.html` — onglet Pharmacologie (3 îlots, Pareto), fermeture du template
- `chapters/J90/J90_pop1.html`, `J90_pop2.html` — 49 fenêtres `j90-…` et 6 Pareto `pareto-j90-…`
- `glossary/j90.py` — 15 clés nouvelles : BTS, ECOG, LENT, TIME1, TIME2, TAPPS, AMPLE, IPC-PLUS, J94.0, J94.1, J94.2, J94.8, J94.9, S27.1, Romero-Candeira

Volume : environ 7 100 mots de corps de cours, 6 300 mots de fenêtres ; 139 Ko de sources.

## Plan

Pathologie : 0 Question clinique ; 1 Définitions et codage ; 2 Fréquence et pronostic ; 3 Du liquide normal à l’épanchement (Starling, stomates lymphatiques, dyspnée diaphragmatique ; figure) ; 4 Causes et terrains ; 5 Anamnèse ; 6 Examen clinique ; 7 Démarche diagnostique (Light, gradient d’albumine) ; 8 Urgences et complications ; 9 Prise en charge selon la cause ; 10 Épanchement malin (talc, cathéter tunnellisé, poumon non expansible) ; 11 Chylothorax, hémothorax, fibrothorax ; 12 Suivi et situations particulières, cas récapitulatif ; 13 Critères formels et paramètres clés.
Examens : hiérarchie question → examen → statut, gold standard ; imagerie ; fiche d’interprétation du liquide ; profils biologiques × diagnostics ; biopsie ; 3 quiz.
Sciences : anatomie (paquet intercostal, innervation phrénique) ; histologie (mésothélium, stomates, bloc cellulaire) ; physiologie (Starling, réserve lymphatique, mécanique diaphragmatique, poumon non expansible) ; biochimie (protéines, LDH, pH/glucose, chylomicrons, adénosine désaminase).
Pharmacologie : stratégie par phénotype ; doses (talc, lidocaïne, diurétique) ; interactions anticoagulants/antiagrégants (`div.alert`), surveillance, médicaments inducteurs d’épanchement.

## Sources consultées (08.10.2026)

| Source | Accès | Usage |
|---|---|---|
| Roberts ME et al. BTS Guideline for pleural disease. Thorax 2023;78(Suppl 3):s1–s42, doi:10.1136/thorax-2022-219784 | Texte intégral (PDF BTS) | pH/LDH/glucose, cytologie (sensibilité 0,46), ADA, NT-proBNP, biopsie, épanchement malin (choix talc/cathéter, seuil 25 %, drainage quotidien, talc par cathéter), coexistence infection–cancer 5 %, inhibiteurs de tyrosine kinase |
| Asciak R et al. BTS Clinical Statement on pleural procedures. Thorax 2023, doi:10.1136/thorax-2022-219371 | Texte intégral (PDF BTS) | Critères de Light, volumes de prélèvement, triglycérides/cholestérol, hématocrite, amylase, 1,5 L, œdème de réexpansion < 1 %, lidocaïne, anticoagulants, talc calibré 3–4 g (~75 % de succès), drain ≥ 12F |
| Bibby AC et al. ERS/EACTS statement on MPE. Eur Respir J 2018;52:1800349 | Résumé PubMed (texte intégral refusé, 403) | Cadre européen de l’épanchement malin |
| Light RW et al. Ann Intern Med 1972;77:507 | Référence bibliographique (résumé indisponible) ; critères repris du texte BTS 2023 | Critères de Light |
| Roth BJ et al. Chest 1990;98:546 | Résumé PubMed | Gradient d’albumine 1,2 g/dL |
| Romero-Candeira S et al. Am J Med 2001;110:681 ; Chest 2002;122:1524 | Résumés PubMed | Effet des diurétiques ; exactitude 83 % vs 93 % |
| Noppen M et al. Am J Respir Crit Care Med 2000;162:1023 | Résumé PubMed | Volume normal 0,26 mL/kg, cellularité |
| Thomas R et al. Curr Opin Pulm Med 2015;21:338 | Résumé PubMed | Mécanisme de la dyspnée |
| Aggarwal AN et al. PLoS One 2019;14:e0213728 | Résumé PubMed | ADA : seuil 40 ± 4 U/L, Se 93 %, Sp 90 % |
| Janda S, Swiston J. BMC Pulm Med 2010;10:58 | Résumé PubMed | NT-proBNP pleural Se/Sp 94 % |
| Essais TIME1 (JAMA 2015), TIME2 (JAMA 2012), AMPLE (JAMA 2017), TAPPS (JAMA 2020), IPC-PLUS (NEJM 2018) | Résumés PubMed | Chiffres des essais cités |
| Clive AO et al. LENT, Thorax 2014;69:1098 | Résumé PubMed | Composantes et survies médianes |
| CIM-10-GM 2024, BfArM, bloc J90–J94 | Page officielle | Libellés et exclusions (S27.1, A15–A16) |
| Pneumotox (pneumotox.com) | Lien de ressource, non interrogé | Renvoi pour l’imputabilité médicamenteuse |

## Réserves

1. **Aucune source suisse spécifique** (Société suisse de pneumologie, OFSP) sur les épanchements pleuraux n’a été trouvée ; aucune donnée épidémiologique suisse n’est donnée (lacune nommée dans l’îlot 2).
2. **Compendium inaccessible** (connexion requise) : la monographie suisse du talc stérile et le statut d’enregistrement en Suisse (médicament ou dispositif médical) n’ont pas pu être confirmés ; la fenêtre `j90-talc` le signale. Les doses de lidocaïne proviennent du formulaire britannique cité par la BTS 2023, non de l’information professionnelle suisse ; la fenêtre `j90-lidocaine` le signale.
3. **ERS/EACTS 2018** : seul le résumé a été lu (texte intégral refusé) ; les recommandations détaillées s’appuient sur la BTS 2023, plus récente et lue en texte intégral (règle « source primaire la plus récente »).
4. Affirmations classiques non rattachées à une source lue en texte intégral : dyspnée/matité/vibrations (sémiologie), latéralisation droite de l’épanchement cardiaque unilatéral et de l’hydrothorax hépatique, centrifugation empyème/chyle, médicaments classiques (amiodarone, méthotrexate, nitrofurantoïne, dérivés de l’ergot ; dasatinib comme exemple d’inhibiteur de tyrosine kinase), lymphome comme cause de chylothorax, mécanisme d’hypersensibilité de la pleurésie tuberculeuse, TNM M1a implicite. À vérifier par le relecteur.
5. Développement des acronymes TAPPS et AMPLE : non développés dans les publications lues ; le glossaire l’indique honnêtement.
6. **Collisions possibles de glossaire** : la clé `BTS` sera vraisemblablement aussi créée par les rédacteurs parallèles de J86 et J93 ; le relecteur doit n’en conserver qu’une seule.
7. L’hémothorax : seuils chirurgicaux de débit (1,5 L immédiat, 200 mL/h) volontairement omis faute de source lue.

## Contrôles effectués (copie de scratchpad, non canonique)

Copie : `/tmp/claude-0/-home-user-Medina/c55d479e-3294-5d11-ab0a-987eb6887a74/scratchpad/J90/repo` (chapters.json temporairement complété, `integrated: false`).
- `build_medina.py J90` : **J90 non couvertes: 0**, aucune erreur Pareto ; 6 ratios Pareto calculés.
- Clés : 49 fenêtres + 6 Pareto, aucune manquante, aucun orphelin, aucun doublon, aucune collision avec les templates des autres chapitres ; identifiants tous préfixés `j90`.
- Navigateur (Chromium headless, 1300 px et 390 px) : 55/55 fenêtres ouvertes depuis les quatre onglets et les quatre sciences, sans « Fiche absente », sans erreur JavaScript propre au cours, sans défilement horizontal. L’erreur `lesson-core.js` du `test_preview.py` d’origine est environnementale (également présente sur J40).
- Captures de travail : `scratchpad/J90/J90_ouverture.png`, `scratchpad/J90/J90_fenetre.png` (fenêtre « Critères de Light »).
- Non exécutés (rôle du relecteur) : tests unitaires du dépôt, `build_front.py --all-fragments`, `tests/verify_course_native.cjs`.
