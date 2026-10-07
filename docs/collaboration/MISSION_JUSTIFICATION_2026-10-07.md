# Mission commune — justification systématique de chaque affirmation

Date : 7 octobre 2026. Demande du propriétaire, transmise à Codex et à Claude.

## Exigence

Toute affirmation d'un cours porte son **pourquoi**. Ce pourquoi est le mécanisme physiopathologique précis qui relie un fait à sa conséquence clinique, puis à la décision. Cette règle vaut pour les quatre onglets, les fenêtres, les tableaux, les listes, les quiz et les Pareto de tous les cours.

Le propriétaire a cité deux exemples :
- Un bilan qui écrit « anémie → facteur aggravant » doit expliquer par quel mécanisme l'anémie aggrave la situation.
- Un bilan qui cite le sodium ou le potassium doit justifier clairement pourquoi on les dose et ce que leur valeur change.

La forme préférée est la **fenêtre interactive** : un mot vert cliquable qui ouvre l'explication à l'endroit même de l'affirmation.

Les cellules de tableau laconiques sont proscrites. Une cellule qui énonce un fait doit, soit former une phrase complète qui donne la cause et la conséquence, soit porter un mot vert qui ouvre la fenêtre explicative. Une liste d'examens dit, pour chaque examen, pourquoi il est demandé et quelle valeur change quelle décision.

## Répartition retenue — 15 cours chacun

La proposition initiale de Claude est archivée sans modification. La répartition publiée dans MECHANISMS_PLAN.json fait foi ; les ajouts ciblés de Codex sont déjà engagés dans ses quinze cours.

| Claude — 15 cours | Codex — 15 cours |
| --- | --- |
| I48 — Fibrillation et flutter auriculaires | I50 — Insuffisance cardiaque |
| I30 — Péricardites, épanchement péricardique, tamponnade et constriction | I21 — Syndromes coronariens aigus et infarctus du myocarde |
| I33 — Endocardite infectieuse | I25 — Syndromes coronariens chroniques et angor |
| I35 — Valvulopathies aortiques | I10 — Hypertension artérielle |
| I34 — Valvulopathies mitrales, tricuspides et pulmonaires | J45 — Asthme |
| I00 — Rhumatisme articulaire aigu | J44 — Bronchopneumopathie chronique obstructive |
| I40 — Myocardites | D84 — Déficits immunitaires |
| I42 — Cardiomyopathies | M06 — Polyarthrite rhumatoïde |
| I44 — Troubles de la conduction et bradycardies | M32 — Lupus érythémateux systémique |
| I47 — Tachycardies paroxystiques supraventriculaires et ventriculaires | T78 — Anaphylaxie et allergies |
| I49 — Extrasystoles et autres arythmies | M31 — Vascularites systémiques |
| I46 — Arrêt cardiaque | I70 — Athérosclérose périphérique, artériopathie des membres inférieurs et ischémie aiguë |
| Q21 — Cardiopathies congénitales de l’adulte | J18 — Pneumonies de l’adulte |
| I71 — Anévrismes et dissections artérielles | I26 — Embolie pulmonaire aiguë |
| I80 — Thrombose veineuse profonde et thromboses veineuses | A41 — Sepsis et choc septique de l’adulte |

Les lots 2 et 3 de PR #10 sont désormais injectés avec contrelecture. Reprendre sur main publié et préserver les corrections d’intégration.

## Méthode commune

1. **Inventaire.** Relever, fichier par fichier, chaque affirmation sans mécanisme : cellule de tableau, item de liste, phrase isolée, encadré, Pareto, réponse de quiz.
2. **Choix de la forme.**
   - Une explication courte, de deux ou trois phrases, s'écrit dans le texte.
   - Une explication plus longue, ou une notion réutilisée à plusieurs endroits, devient une fenêtre, appelée par un mot vert `<button class="w" data-k="<code>-<clé>">…</button>`.
3. **Contenu d'une fenêtre.** La fenêtre suit l'ordre normal → perturbation → conséquence → décision. Elle se déclare par `<template data-pop="<code>-<clé>" data-title="…">`, avec ses rubriques `<div class="lab">…</div><p>…</p>`, dans un fichier `_pop*.html` existant du cours. Les rubriques usuelles sont « Physiologie normale », « Mécanisme », « Conséquence clinique », « Ce qui change la décision » et « Source ».
4. **Sources.** Un fait, un seuil ou une recommandation nouvellement écrit cite sa source primaire : organisme, année, section ou tableau, DOI. Une physiologie classique cite une référence de manuel ou une revue identifiée. Un mécanisme incertain est présenté comme tel.
5. **Contraintes techniques.**
   - La clé de fenêtre commence par le code du cours en minuscules.
   - Chaque bouton `data-k` doit avoir sa fenêtre.
   - Aucune abréviation n'est introduite sans entrée dans `glossary/`.
   - Les tests (`test_v7.py --static`, `audit_sciences.py`, les deux tests navigateur) doivent rester verts.
6. **Non-régression.** On ne retire aucune notion utile. On ne recopie pas une explication déjà présente ailleurs : on renvoie à la fenêtre existante.

## Exemples proposés par Claude — portée à vérifier

Ces exemples sont des pistes pédagogiques, pas une validation exhaustive. Les sources et les nuances doivent être contrôlées pour le cours concerné ; les fenêtres I50 sur anémie, sodium et potassium présentent les références individualisées. Le risque de torsades varie entre molécules et n’est pas identique pour le sotalol et l’amiodarone. Une anémie n’abaisse pas toujours le contenu en oxygène dans une proportion strictement identique, compte tenu de la saturation et de la fraction dissoute.


### Anémie dans le bilan d'une fibrillation auriculaire

Le contenu artériel en oxygène vaut environ 1,34 × hémoglobine (g/dL) × saturation + 0,003 × PaO₂ (mmHg), en mL d'oxygène par dL de sang. Quand l'hémoglobine baisse, ce contenu baisse dans la même proportion. L'organisme maintient l'apport d'oxygène en augmentant le débit cardiaque, sous l'effet d'une activation sympathique.

En FA, ce tonus sympathique accélère la conduction du nœud auriculoventriculaire, ce qui élève la fréquence ventriculaire. La diastole raccourcit, ce qui réduit le remplissage du ventricule gauche et la perfusion coronaire, qui a lieu surtout en diastole. Le contrôle de la fréquence devient plus difficile et une ischémie fonctionnelle peut apparaître.

Sous anticoagulant, une anémie est aussi un facteur de risque hémorragique modifiable (ESC 2024). Elle peut révéler un saignement occulte et elle réduit la réserve face à une hémorragie. Le bilan recherche donc sa cause avant de prescrire et pendant le suivi.

### Potassium et magnésium avant un antiarythmique ou une digoxine

Une hypokaliémie ralentit la repolarisation ventriculaire et favorise les post-dépolarisations précoces. Associée à un médicament qui allonge l'intervalle QT (sotalol, amiodarone), elle expose aux torsades de pointes.

Sous digoxine, le potassium entre en compétition avec la digoxine pour la pompe sodium-potassium. Une hypokaliémie augmente donc la fixation de la digoxine et sa toxicité.

Une hypomagnésémie entretient la fuite rénale de potassium et favorise elle aussi les torsades. On corrige donc le potassium et le magnésium avant d'introduire ces médicaments, et on les contrôle sous traitement.

## Remise et suivi

Chaque lot nomme ses cours par leur code et leur intitulé complet. Il donne :
- le nombre d'affirmations justifiées et de fenêtres créées ;
- les sources ;
- les réserves non résolues ;
- les contrôles exécutés.

La passation `HANDOFF_LATEST.md` indique l'avancement de chaque agent, cours par cours.
