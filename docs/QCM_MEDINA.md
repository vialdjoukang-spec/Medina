# QCM MEDINA — contrat pédagogique et technique

Version du 29 septembre 2026. Cette clarification de l’utilisateur prévaut sur toute ancienne assimilation des deux banques.

## 1. Deux finalités, trois formats partagés

| Espace | Point de départ | Finalité | Organisation |
|---|---|---|---|
| **MEDINA** | Un cours déjà présent dans MEDINA | Consolider les acquis, identifier une notion mal comprise, retourner à la leçon | Système → chapitre → objectif pédagogique → questions |
| **GLOBALITY** | Une situation clinique de départ, dite SSP (*Situations as Starting Points*) | Construire le raisonnement transversal à partir des situations du référentiel | SSP → problématiques → raisonnement → questions |

Les deux espaces utilisent les formats **A, K prime et menu long**. Un format de question ne détermine pas sa finalité pédagogique. La banque GLOBALITY et ses fichiers historiques ne sont pas un prérequis au fonctionnement des QCM MEDINA.

## 2. Parcours livré

`site/qcm.html` est une page autonome, copiée par la construction existante vers `_site/qcm.html`. Aucun service tiers ni fichier GLOBALITY n’est nécessaire.

- L’apprenant filtre le système, le chapitre, la notion ou le format.
- Chaque question indique son chapitre et son niveau pédagogique.
- La validation attend une réponse complète. Le menu long exige une sélection explicite après recherche.
- La correction affiche l’attendu, son explication, une source datée et le lien vers le chapitre MEDINA.
- Le bilan affiche les points, les questions entièrement réussies et les résultats par chapitre.
- L’apprenant peut recommencer la sélection ou reprendre les questions incomplètement réussies.
- Un changement de filtre démarre une nouvelle session. Aucun historique persistant n’est annoncé ni enregistré.

Paramètres facultatifs : `qcm.html?chapter=J45&format=K`. Les valeurs inconnues sont ignorées.

## 3. Lot initial et limites

| Chapitre intégré | Type A | K prime | Menu long | Total |
|---|---:|---:|---:|---:|
| J45 — Asthme | 1 | 1 | 1 | 3 |
| I50 — Insuffisance cardiaque | 1 | 1 | 1 | 3 |
| I26 — Embolie pulmonaire aiguë | 1 | 1 | 1 | 3 |
| **Total** | **3** | **3** | **3** | **9** |

Il s’agit de questions originales de consolidation. Ce petit lot n’est ni une banque exhaustive, ni une certification de maîtrise d’un chapitre, ni une reproduction d’un examen officiel. Les liens ouvrent le chapitre ; le nom de la partie à revoir est indiqué, sans prétendre ouvrir directement un îlot interne.

Le lecteur natif MEDINA a été ouvert depuis une correction du chapitre Asthme. Un chargement historique `lesson-core.js` absent de `_site` a été observé dans l’atlas ; il n’empêche pas le moteur natif d’afficher ce cours. Cette anomalie appartient à l’intégration de l’atlas et n’a pas été corrigée dans le présent périmètre QCM.

Niveaux : **1**, reconnaître une notion ; **2**, interpréter et relier ; **3**, choisir une étape du raisonnement clinique. Cette gradation est pédagogique et interne au module.

## 4. Schéma d’un item

Le tableau `QUESTIONS` et les dictionnaires `CHAPTERS`, `SOURCES`, `MENUS` vivent dans le script de la page. Les champs communs sont :

| Champ | Rôle et contrainte |
|---|---|
| `id` | Identifiant stable et unique, ex. `J45-A-01` |
| `type` | `A`, `K` ou `L` |
| `chapter` | Code d’un chapitre intégré, déclaré dans `CHAPTERS` et `chapters.json` |
| `level` | Entier pédagogique 1, 2 ou 3 |
| `topic` | Notions indexées pour la recherche |
| `section` | Partie du cours explicitement associée à l’objectif |
| `source` | Clé d’une source primaire datée et vérifiée |
| `title` | Énoncé autonome et sans ambiguïté |

Pour A : `options` contient les propositions ; `correct` est leur indice correct ; `why` explique l’attendu ; `distractors` explique chaque mauvais choix.

Pour K prime : `options`, `correct` et `reasons` contiennent exactement quatre éléments ; `correct` contient des booléens ; chaque proposition a sa justification spécifique.

Pour le menu long : `menu` désigne une liste de termes ; `correct` est un terme exact de cette liste ; `why` explique l’attendu. Les trois listes actuelles contiennent 16 ou 17 termes. Une saisie libre ne peut pas être notée comme réponse. Une nouvelle saisie efface la sélection antérieure.

Les entrées sont échappées avant insertion dans le HTML. Les termes du menu sont filtrés sans distinction de casse ou d’accents. Les choix natifs restent accessibles au clavier ; les groupes K prime utilisent des `fieldset` et `legend`.

## 5. Barème explicite

- **A et menu long** : 1 point pour l’attendu, 0 sinon.
- **K prime** : 0,25 point par jugement juste ; maximum 1 point par question.
- **Pourcentage** : somme des points / nombre de questions de la session × 100.
- Le nombre de questions entièrement réussies est affiché séparément.

Ce barème sert la consolidation et ne prétend pas reproduire le barème d’une épreuve officielle. Les points sont remis à zéro à chaque nouvelle session ; l’ancien résultat n’est pas présenté comme progression durable.

## 6. Références vérifiées

Consultation le 29 septembre 2026. Les énoncés ont été confrontés aux sources primaires et aux chapitres intégrés correspondants.

1. **Asthme** : Global Initiative for Asthma, [Summary Guide 2026](https://ginasthma.org/wp-content/uploads/2026/07/GINA-Summary-Guide-2026-WEB-WMS.pdf), notamment p. 5–9 et 15–17 : variabilité, examen normal possible, prévention des exacerbations, corticostéroïdes inhalés, technique d’inhalation.
2. **Insuffisance cardiaque** : Société européenne de cardiologie, [recommandations 2026](https://doi.org/10.1093/eurheartj/ehag100), diagnostic et tableau 7. Les questions portent sur l’échocardiographie et la sémiologie. Elles ne reprennent pas l’ancienne classification 2021 comme si elle était la version actuelle. La page de publication 2026 et les passages indexés du texte primaire ont été consultés ; le téléchargement intégral du texte dépassait la limite du lecteur web.
3. **Embolie pulmonaire** : Société européenne de cardiologie / Société européenne de pneumologie, [recommandations 2019](https://doi.org/10.1093/eurheartj/ehz405), § 4. Le cours I26 emploie ce cadre européen principal et distingue par ailleurs le cadre américain 2026. Les items portent sur les D-dimères, la probabilité clinique et l’imagerie diagnostique ; ils ne transposent pas les classifications pronostiques entre cadres.

Une relecture médicale indépendante reste à obtenir avant d’étendre la banque à des décisions thérapeutiques, posologies ou seuils complexes. Ce document ne constitue pas un audit complet des cours.

## 7. Critères d’audit avant extension

### Contenu

1. La question consolide un objectif identifiable du cours MEDINA.
2. Le chapitre est réellement intégré et son lien est fonctionnel.
3. La réponse attendue est univoque dans le contexte fourni.
4. Les distracteurs sont plausibles et leur rejet est expliqué.
5. Les quatre affirmations K prime sont autonomes, avec quatre justifications.
6. Le menu long comporte une liste cohérente et une réponse attendue présente une seule fois.
7. Les faits et dates sont contrôlés auprès d’une source primaire ; toute version historique est nommée.
8. Le niveau et la couverture ne sont pas confondus avec une mesure validée de maîtrise.

### Fonctionnement

1. Tous les formats se résolvent entièrement ; aucune réponse vide n’est validée.
2. Les corrections, transitions et scores fonctionnent pour les réponses justes, fausses et partielles.
3. La recherche du menu long ne sélectionne ni ne valide automatiquement le premier résultat.
4. Le changement de recherche efface toute sélection devenue ambiguë.
5. Les filtres incompatibles et les recherches sans résultat affichent une sortie explicite.
6. Le recommencement remet le score, la progression et les réponses à zéro.
7. Les liens de retour ouvrent le bon chapitre sans perdre la session courante.
8. Le clavier, le focus visible, les libellés des champs et le format mobile sont contrôlés dans un navigateur réel.

## 8. Suite proposée

Étendre chapitre par chapitre après audit, en couvrant successivement définition, mécanisme, sémiologie, examens, diagnostic, traitement et suivi. La persistance des résultats, l’espacement des répétitions et un tableau de maîtrise demandent une conception distincte : ils ne sont pas annoncés comme disponibles dans ce premier lot.

## 9. Vérifications du premier lot

- **95 assertions jsdom** : neuf questions, identifiants uniques, chapitres intégrés, parcours complet à 9/9, réponses verrouillées après validation, correction liée au bon cours, score partiel K prime, recherche du menu sans sélection automatique, effacement de sélection à la nouvelle saisie, choix faux, état vide, filtres combinés, réinitialisation, reprise des erreurs, paramètres URL et absence d’interprétation HTML des recherches. Aucune erreur JavaScript.
- **23 contrôles Playwright en Chromium réel**, réalisés par un agent distinct sur ordinateur et mobile 390 px : formats A/K prime/menu long, K prime à 0,75 point, recherche/sélection/effacement, absence de résultat, bilan à 2/3, reprise des erreurs, filtres. Aucun débordement horizontal à 390 px ni erreur JavaScript dans la page QCM.
- Deux retouches visuelles ont suivi : la bordure du quatrième groupe K prime a été rétablie et le bouton de reprise emploie le singulier pour une seule question. Les 95 assertions jsdom ont été relancées avec succès après ces retouches.
- Ces contrôles techniques ne constituent pas une validation médicale indépendante.
