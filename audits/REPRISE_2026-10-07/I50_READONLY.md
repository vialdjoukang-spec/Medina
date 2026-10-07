# I50 — Insuffisance cardiaque : relecture ciblée en lecture seule

Date : 7 octobre 2026. Base communiquée : `3cbe0f52`. Fragment : **C-01-Cardiologie**.

Les quatre onglets ont été lus dans `I50_a.html` à `I50_d.html`, ainsi que les quatre banques `I50_pop*.html`, les 21 entrées de `I50_justifications.json` et leur contrelecture existante. Les instructions `AGENTS.md`, le début de `CLAUDE.md` et `docs/STYLE_REDACTION.md` ont été consultés. Aucun cours, aucune banque ni aucune documentation commune n'a été modifié.

Les mécanismes de l'anémie, de la natrémie et des dyskaliémies sont **déjà expliqués** par `i50-j-anemie`, `i50-j-sodium` et `i50-j-potassium`. Leurs cibles sont déclarées dans `I50_c.html`, ancre `e-2`. Il faut conserver ces explications et les prolonger aux endroits qui restent incomplets. La présence d'une fenêtre ne corrige pas les formulations divergentes dans les tableaux, quiz et Pareto.

## Sept propositions concrètes

### 1. Anémie : ajouter la possibilité d'hémodilution à la fenêtre existante

- **Ancre/texte :** `I50_c.html`, `#e-2`, ligne 33 : « Anémie » ; « Facteur aggravant ; bilan martial ». Autre occurrence : `I50_b.html`, `#i50-11`, ligne 99, « Anémie sans carence martiale ».
- **Lacune non couverte :** `i50-j-anemie` explique le transport d'oxygène, mais pas la baisse de concentration liée à l'expansion du volume plasmatique.
- **Proposition :** compléter cette fenêtre : « Une augmentation du volume plasmatique peut abaisser l'hémoglobine sans réduction proportionnelle de la masse globulaire. Une anémie réelle et une hémodilution peuvent coexister. L'évolution sous décongestion contribue à l'interprétation ; elle ne remplace pas la recherche de carence, saignement ou maladie rénale. » Relier également la carte clinique à cette fenêtre. L'étude observationnelle d'Androne soutient cette distinction ; son petit sous-groupe ne fournit pas une prévalence universelle [1].

### 2. Sodium : distinguer le contrôle hydrique de la titration des traitements hyperkaliémiants

- **Ancre/texte :** `I50_c.html`, `#e-2`, ligne 35 : « Sodium, potassium » → « Titration IEC/ARNI/ARM ». `I50_b.html`, `#i50-11`, ligne 96 : « Restriction hydrique, optimisation de la décongestion ». `I50_pop4.html`, fenêtre `pareto-suivi`, ligne 109 : « Hyponatrémie : restriction hydrique ».
- **Lacune non couverte :** la fenêtre sodium décrit la dilution et les pertes possibles, mais la carte et le Pareto enseignent encore une conduite uniforme. Le rôle de la natrémie n'est pas celui de la kaliémie.
- **Proposition :** séparer les deux examens dans le tableau. Conserver `i50-j-sodium` pour concentration/eau/vasopressine. Ajouter une fenêtre de décision `i50-j-hyponatremie-conduite` : caractériser l'hyponatrémie, apprécier congestion ou déplétion et rechercher les symptômes neurologiques. La restriction hydrique relève du contexte dilutionnel ; une forme neurologique sévère exige une prise en charge urgente spécialisée. L'association pronostique ne prouve pas qu'une correction isolée améliore la survie [2].

### 3. Potassium : expliquer les interactions avec la digoxine

- **Ancre/texte :** `I50_pop4.html`, fenêtre `d-dig`, ligne 87 : « Toxicité […] Favorisée par l'hypokaliémie » ; « Interactions : amiodarone, vérapamil, clarithromycine (hausse des taux) ».
- **Lacune non couverte :** `i50-j-potassium` explique l'électrophysiologie et les pertes rénales. Il ne détaille pas ces interactions pharmacocinétiques.
- **Proposition :** enrichir `d-dig`, ou ajouter `i50-j-digoxine-interactions`. Distinguer sensibilité accrue lors d'un trouble électrolytique, accumulation lorsque la clairance rénale baisse et augmentation de l'exposition par inhibition de la glycoprotéine P. Expliquer que l'amiodarone et les bradycardisants ajoutent aussi un risque de ralentissement de conduction. Le contrôle des électrolytes, de la fonction rénale, du tracé et de la digoxinémie répond à ces mécanismes distincts [3].

### 4. BNP sous ARNI : corriger les contradictions avec la fenêtre déjà revue

- **Ancres/textes :** `I50_b.html`, `#i50-7`, ligne 12 : « seul le NT-proBNP reste interprétable » ; `I50_c.html`, `#e-2`, ligne 29 : « BNP ↑, NT-proBNP inchangé » ; `I50_c.html`, `#e-6`, lignes 96–98 : « la hausse du BNP est pharmacologique » et « seul le NT-proBNP reflète fidèlement la contrainte pariétale » ; `I50_pop4.html`, fenêtre `d-arni`, ligne 9 : « et non le BNP ».
- **Lacune :** ces formulations contredisent explicitement les limites correctes de `i50-j-neprilysine`.
- **Proposition :** harmoniser toutes les occurrences avec cette fenêtre. Le NT-proBNP est moins directement influencé par l'inhibition enzymatique ; il peut diminuer avec l'amélioration clinique. Le BNP conserve une valeur pronostique. Le quiz doit retenir « évolution compatible avec une amélioration, à confronter à la clinique », sans attribuer automatiquement toute hausse du BNP au médicament [4].

### 5. Créatinine : réparer les conditions du seuil et de la réduction du diurétique

- **Ancre/texte :** `I50_d.html`, `#p-4`, ligne 52 : « Une hausse jusqu'à 50 % (ou jusqu'à 266 µmol/L) est acceptable » ; « réduire le diurétique avant de réduire la TMF ». Répétition dans `I50_pop4.html`, fenêtre `pareto-pharma`, ligne 80.
- **Lacune :** `i50-j-rein-traitement` donne le mécanisme mais laisse subsister cette règle inconditionnelle. Le « ou » élargit incorrectement les conditions du repère ESC 2021.
- **Proposition :** préciser que le repère ESC cité associe une hausse **inférieure à 50 % ET une créatinine inférieure à 266 µmol/L**, dans son contexte. Distinguer la surveillance CKD sous IEC/ARA II : KDIGO 2024 signale une hausse supérieure à 30 % dans les quatre semaines comme seuil d'évaluation. Ne pas remplacer mécaniquement tout le tableau par un seuil unique. La diminution du diurétique dépend d'une déplétion ou de l'absence de congestion ; une congestion persistante interdit cette conclusion automatique [2,5].

### 6. Échocardiographie : remplacer « preuves directes » et expliquer E/e′

- **Ancre/texte :** `I50_c.html`, `#e-6`, ligne 93 : « L'oreillette gauche dilatée et le rapport E/e′ > 14 sont des preuves directes de pressions de remplissage élevées ». Tableau concerné : `#e-3`, lignes 52–54. Résumé : `I50_pop4.html`, fenêtre `pareto-exam`, ligne 76.
- **Lacune non couverte :** `i50-j-echo-relaxation` explique e′, mais pas le mécanisme du rapport ni les limites de l'association à la taille de l'oreillette.
- **Proposition :** écrire « indices indirects » et ajouter `i50-j-echo-remplissage`. E reflète la vitesse du remplissage mitral précoce ; e′ renseigne notamment sur la relaxation. Une pression atriale accrue peut maintenir E alors que e′ diminue. Le rapport s'interprète avec les autres paramètres, le rythme et les valvulopathies. La dilatation atriale a plusieurs causes et ne mesure pas directement la pression actuelle. Le référentiel ASE 2025 utilise des algorithmes multiparamétriques [6].

### 7. Histologie : rendre la figure conforme à sa propre explication

- **Ancre/texte :** `I50_c.html`, `#sh-i`, ligne 128 : « la “Matrice modifiée”, qui se divise en deux branches » ; légende : « une branche mécanique et une branche électrique ».
- **Constat du code :** le SVG contient quatre rectangles superposés et trois flèches verticales. Il dessine donc une chaîne « Matrice modifiée → Souplesse réduite → Conduction hétérogène → Retentissement […] ».
- **Proposition :** dessiner réellement deux branches parallèles : fibrose → rigidité/remplissage et fibrose → conduction/réentrée. Elles convergent vers les conséquences cliniques. La fenêtre `i50-j-fibrose` explique déjà la réentrée ; la figure doit porter cette même topologie. Aucun ajout de source n'est nécessaire pour constater l'incohérence entre texte et SVG.

## Sources primaires vérifiées et portée

1. Androne et coll., *Circulation*, 2003, [PMID 12538419](https://pubmed.ncbi.nlm.nih.gov/12538419/). Résumé original consulté ; étude observationnelle.
2. ESC 2021, texte publié dans l'*European Journal of Heart Failure*, sections 13.6–13.7 et accompagnement : [DOI 10.1002/ejhf.2333](https://onlinelibrary.wiley.com/doi/full/10.1002/ejhf.2333). Passages pertinents du texte intégral consultés.
3. [Information officielle DailyMed : digoxine, sections 5.3, 7.1–7.3](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9ca08b66-55eb-4155-a8bd-6fa2282adab4). L'information suisse d'amiodarone retrouvée sur Compendium confirme l'interaction, mais son détail complet n'a pas été récupéré ; aucune posologie suisse nouvelle n'est proposée.
4. Myhre et coll., analyse PARADIGM-HF, *JACC*, 2019, [PMID 30846338](https://pubmed.ncbi.nlm.nih.gov/30846338/). Résumé original consulté.
5. [KDIGO 2024, points 3.6.2–3.6.5 et 3.7.3](https://kdigo.org/wp-content/uploads/2024/03/KDIGO-2024-CKD-Guideline.pdf). Passages du PDF officiel consultés.
6. [ASE 2025, fonction diastolique et diagnostic d'ICFEp](https://www.asecho.org/wp-content/uploads/2025/07/Left-Ventricular-Diastolic-Function.pdf), figures 2–3, sections sur l'interprétation multiparamétrique et l'ICFEp. Passages du PDF officiel consultés.

Le résultat RED-HF a aussi été vérifié dans son [résumé original, PMID 23473338](https://pubmed.ncbi.nlm.nih.gov/23473338/) : la carte actuelle est cohérente sur l'absence de bénéfice et le surcroît thromboembolique. Ce point n'est donc pas présenté comme une erreur nouvelle.

Cette relecture **ne certifie pas l'ensemble des affirmations médicales**. Elle n'a pas réaudité toutes les doses, classifications, classes de recommandation ou nouveautés attribuées à ESC 2026. Les ancrages ont été relevés dans les sources ; le fonctionnement effectif des fenêtres dans le site reconstruit n'a pas été testé ici.
