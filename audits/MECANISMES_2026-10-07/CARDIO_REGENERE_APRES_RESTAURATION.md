# Banques cardiologiques — récupération et couverture, 7 octobre 2026

## Nature de cette livraison

L’environnement d’exécution a été remplacé par une version antérieure du dossier de travail. Le contenu complet de la banque I50 et de sa contrelecture était encore conservé : ils ont été restaurés. Les quatre banques I10, I21, I25 et I70 ne pouvaient pas être récupérées à l’identique depuis les seuls comptes historiques. Elles ont donc été **régénérées**, sur autorisation du responsable de l’intégration, après une nouvelle lecture des fichiers natifs et une vérification des sources médicales. Ce ne sont pas des restaurations bit à bit.

Les banques apportent des explications locales : affirmation choisie, mécanisme causal, conséquence clinique et limites. Elles ne modifient pas les HTML sources. Le compilateur crée les fenêtres et les liens dans la production. Les fichiers `_c.html` ont été relus dans leur état courant après l’intégration des sciences livrées par Claude ; les ancrages finaux sont contrôlés sur cet état.

## Contrôles exécutés sur les fichiers actuels

| Cours | Fenêtres | Cibles | HTML inventoriés | Statut |
|---|---:|---:|---:|---|
| I10 — Hypertension artérielle | 14 | 14 | 9 | Régénéré |
| I21 — Syndromes coronariens aigus et infarctus du myocarde | 13 | 13 | 10 | Régénéré |
| I25 — Syndromes coronariens chroniques et angor | 14 | 14 | 10 | Régénéré |
| I70 — Athérosclérose périphérique, artériopathie des membres inférieurs et ischémie aiguë | 15 | 15 | 6 | Régénéré |
| I50 — Insuffisance cardiaque | 21 | 21 | 8 | Restauré |

Les cinq banques ont été chargées par `tools.insert_justifications.load_course_justifications` après sa restauration. La validation du schéma, des identifiants, des ancres, des occurrences et des textes exacts a réussi. Les cibles sélectionnées sont hors des liens et boutons déjà présents. Deux occurrences ont été précisées : « Anémie » au **bilan initial** de I21, occurrence 2 ; « paresthésies » dans la description initiale de l’ischémie aiguë de I70, occurrence 1. Les comptes ci-dessus proviennent de cette nouvelle compilation, et non de la production perdue.

`CARDIO_REGENERATION_CONTROLES.json` conserve les empreintes SHA-256 des HTML actuels, l’inventaire des cibles et les nombres calculés. La validation du compilateur n’est pas une validation clinique exhaustive ni une vérification visuelle du site final ; cette dernière relève de l’intégration finale.

## Points explicitement justifiés

- **I10** : kaliémie normale malgré hyperaldostéronisme, quatrième bruit, potassium alimentaire, tabac, hypokaliémie orientant le bilan, rein, albuminurie, qualité du recueil urinaire, syndrome de Gordon, mutations de KCNJ5, troubles sodés et potassiques des thiazidiques, bradycardie, orthostatisme.
- **I21** : perception atypique avec neuropathie, poids et prasugrel, abord radial, anémie, plaquettes initiales, élimination rénale des anticoagulants, potassium et magnésium, hyperglycémie de stress, peptides natriurétiques, cicatrice et réentrée, thrombopénie immune sous héparine, oxygène en normoxémie, antiarythmiques de classe Ic.
- **I25** : diastole, froid, embolie et cicatrice ventriculaires, anémie, rein, lipoprotéine(a), sens des examens de tolérance, limites du score calcique, activation du clopidogrel, repolarisation sous ranolazine, symptômes musculaires, hémogramme et triptans.
- **I70** : neuropathie, perfusion pelvienne, monofilament, signes neurologiques de menace, rhabdomyolyse, ischémie digestive postprandiale, référence brachiale, vitesses Doppler, oxygénation cutanée, créatine kinase et potassium après reperfusion, contenu du sang en oxygène, double voie antithrombotique, interaction du clopidogrel et précaution cardiaque du cilostazol.
- **I50** : voir `I50_CONTRELECTURE.md`. La restauration maintient les explications distinctes de l’anémie, du fer/ferritine, du sodium, du potassium, de la fonction rénale et des autres éléments du bilan.

## Sources et prudence rédactionnelle

Sources primaires et institutionnelles : recommandations ESC, Endocrine Society 2025, KDIGO 2024 et conférence sur l’hyperkaliémie, AHA/ACC 2024, AHA sur le thrombus ventriculaire, ESVS et SVS, IWGDF 2023, ASH ; essais et études originales ; notices réglementaires précises sur DailyMed. Les études cellulaires, modèles et associations sont identifiés comme tels dans les fenêtres. Aucun seuil de transfusion, dose ou indication nouvelle n’est déduit d’un mécanisme expérimental.

Les notices étrangères servent à documenter un mécanisme et une interaction ; elles ne constituent pas une vérification du statut commercial ou d’une indication suisse. Les sources déjà vérifiées lors de la contrelecture I50 sont conservées, notamment les notices humaines exactes d’Entresto et de Lasix et les documents directs KDIGO et ASE. La notice vétérinaire de furosémide n’a pas été retenue.

## Ce que cette livraison ne permet pas encore de certifier

La relecture des HTML permet de sélectionner et contextualiser ces cibles ; elle ne constitue pas un registre exhaustif de chaque affirmation. Des seuils, délais, fréquences, critères diagnostiques, conduites dans les cas particuliers et passages déjà interactifs restent à suivre dans un audit assertion par assertion. Les fenêtres déjà explicatives ont été consultées pour éviter leur duplication ; elles n’ont pas toutes été réécrites.

Restent notamment à auditer : l’ensemble des valeurs de mesure et des modalités pratiques de I10 ; tous les algorithmes de troponine, délais de reperfusion et antithrombotiques de I21 ; l’ensemble des indices de physiologie invasive et des choix de revascularisation de I25 ; tous les critères de pressions, les décisions de revascularisation et les localisations artérielles de I70. La contrelecture I50 ne vaut pas certification de tout son cours. `exhaustive_review` reste explicitement faux pour les cinq banques.

L’exhaustivité **CIM-11** relève d’un rapprochement séparé entre le référentiel officiel et le catalogue des catégories/leçons. Le code I10, I21, I25, I70 ou I50 du corpus ne prouve pas à lui seul la complétude de ce référentiel.
