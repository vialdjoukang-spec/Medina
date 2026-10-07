# MEDINA — répartition des 21 fragments restants

Consigne de Vial du **8 octobre 2026** : **11 fragments Claude, 10 fragments Codex ; progression d’un chapitre à la fois**. Le registre exécutable par les outils est [production_plan.json](../../organisation/production_plan.json). Les libellés restent ceux d’[organisation/fragments.json](../../organisation/fragments.json).

## Périmètre et équité

C-01-Cardiologie reste dans sa mission partagée actuelle ; son exclusion de ces 21 attributions ne signifie pas qu’il est achevé. La priorité cardiologie en cours reste à terminer et à contrôler avant d’activer les nouvelles files. Ce document organise les travaux suivants, sans déclarer une session Claude démarrée.

La répartition équilibre le volume du catalogue historique : **780 catégories Claude, 779 catégories Codex** sur les 1 559 catégories hors cardiologie. Elle répartit aussi les trois axes sans catégories : deux à Claude, un à Codex. Ces axes nécessitent un périmètre et des chapitres nommés ; zéro catégorie rattachée ne signifie pas zéro travail. Le volume historique n’est ni une mesure de difficulté médicale ni un inventaire CIM-11. Réexaminer la charge après constitution de l’inventaire officiel, sans changer un responsable en cours de chapitre.

Chaque propriétaire assure la production ou la reprise de ses chapitres, leur justification, leurs sources, leur qualité médicale et rédactionnelle et leur remise. L’autre agent assure la contrelecture indépendante du chapitre remis ; Codex coordonne l’injection, la construction et la publication. Cette contrelecture ne transfère pas la propriété du fragment. Les attributions de fragments remplacent les anciens rôles généraux « Codex crée, Claude relit » pour ce périmètre ; les missions et livraisons cardiologiques existantes sont conservées.

## Files de production

L’ordre de chaque file conserve les rangs du registre. Un agent responsable travaille sur un seul fragment actif et un seul chapitre actif. Claude et Codex progressent en parallèle dans leurs files respectives ; chacun répartit les tâches indépendantes de son chapitre entre plusieurs sous-agents spécialisés.

### Claude — 11 fragments

| Rang dans la file | Fragment | Catégories historiques |
| --- | --- | ---: |
| 1 | P-02-Pneumologie | 64 |
| 2 | G-04-Gastroentérologie et hépatologie | 102 |
| 3 | E-06-Endocrinologie et métabolisme | 77 |
| 4 | H-08-Hématologie | 44 |
| 5 | G-10-Gynécologie et sénologie | 50 |
| 6 | M-12-Médecine des âges de la vie | 0 |
| 7 | R-14-Rhumatologie et orthopédie | 155 |
| 8 | O-17-Oto-rhino-laryngologie et médecine bucco-dentaire | 80 |
| 9 | O-18-Ophtalmologie | 56 |
| 10 | M-19-Médecine d’urgence, traumatologie et toxicologie | 152 |
| 11 | E-22-Éthique médicale, droit et communication | 0 |

### Codex — 10 fragments

| Rang dans la file | Fragment | Catégories historiques |
| --- | --- | ---: |
| 1 | I-03-Infectiologie | 155 |
| 2 | N-05-Neurologie | 120 |
| 3 | N-07-Néphrologie | 27 |
| 4 | O-09-Oncologie, génétique médicale et soins palliatifs | 54 |
| 5 | O-11-Obstétrique et néonatologie | 134 |
| 6 | I-13-Immunologie et allergologie | 13 |
| 7 | U-15-Urologie et andrologie | 52 |
| 8 | D-16-Dermatologie | 89 |
| 9 | D-20-Diagnostic clinique et examens complémentaires | 0 |
| 10 | M-21-Médecine de premier recours et santé publique | 135 |

## Coordination et mode multi-agent

La session Codex actuelle prend le relais de la session GPT « work » comme coordinateur prioritaire pour cette organisation. Cette instruction ne supprime ni ne réinitialise aucun travail antérieur ; vérifier les changements concurrents et préserver les commits des autres sessions.

Les deux responsables travaillent en parallèle, chacun sur son chapitre courant. Utiliser plusieurs sous-agents pour les tâches indépendantes de ce chapitre : recherche des référentiels, rédaction de sections distinctes, sciences, examens, pharmacologie, fenêtres et contrôles. Le responsable fixe les fichiers attribués, rassemble les résultats et arbitre. Une exploration en lecture seule peut être parallèle ; deux sous-agents n’écrivent jamais simultanément dans le même fichier.

**Audit croisé avant injection : Claude audite le chapitre Codex, Codex audite le chapitre Claude**, sur les sources proposées et leur commit exact. Corriger les réserves bloquantes puis refaire l’audit affecté. L’injection intervient ensuite ; reconstruire et revérifier la version intégrée, publier et contrôler le déploiement. Une autoévaluation ou un sous-agent du producteur ne remplace pas cet audit croisé.

La mission opérationnelle de Claude est [CLAUDE_FRAGMENTS_CAHIER_DES_CHARGES.md](CLAUDE_FRAGMENTS_CAHIER_DES_CHARGES.md). Mettre les consignes à disposition sur les branches partagées sans déplacer ni écraser sa branche de travail. Une consigne publiée ne prouve pas sa lecture ou le démarrage de Claude.

## Progression obligatoire par chapitre

1. Avant de produire, lire les instructions actuelles, la passation, les reçus et toutes les contributions distantes disponibles. Reprendre les sources canoniques les plus récentes ; ne pas écraser une correction reçue avec une ancienne copie.
2. Après clôture de la priorité cardiologie, prendre le premier fragment de sa file. Choisir un seul chapitre : priorités du registre, puis ordre du catalogue. Commencer par revoir un cours existant si sa revue exhaustive reste ouverte. Claude commence ainsi par **J45 — Asthme** en P-02-Pneumologie ; Codex par **A41 — Sepsis et choc septique de l’adulte** en I-03-Infectiologie. Ces points d’entrée sont proposés, aucun n’est déclaré actif ici.
3. Enregistrer `agents.<agent>.active_chapter` dans le plan avec `fragment_id`, `code`, `title`, `stage`, `base_commit` et `report_path` (chemin relatif du rapport). Les étapes sont `writing`, `review`, `checks`, `integration` ; `blocked` conserve le même chapitre. Un seul objet ou `null` est permis : une liste de chapitres actifs est refusée par le validateur. Vérifier avec `python3 tools/production_plan.py` ; la construction du tableau exécute le même contrôle. Réserver le code primaire d’un cours commun, jamais une variante déjà couverte : M30 renvoie par exemple à M31 en I-13-Immunologie et allergologie, produit par Codex. Le validateur contrôle les attributions, le chapitre unique, le code et le titre canoniques, le SHA et le chemin du rapport. Il ne certifie pas les audits, la clôture ou la publication, dont les preuves restent dans les reçus. Pour les axes encore sans catégories, définir d’abord leur inventaire et leurs identifiants de chapitres dans les sources canoniques ; ne pas inventer de code CIM pour réserver un thème.
4. Terminer ce chapitre dans ses quatre onglets, fenêtres, figures, tableaux, quiz, Pareto, glossaire et sources. Chaque affirmation médicale et décision reçoit une justification causale ou clinique précise, ses limites et une référence. Conserver les précautions décisives dans le texte principal. Aucun quota de mots ne remplace cette exigence.
5. Remettre **un chapitre par lot, rapport et PR**, avec ses sources et leurs empreintes. Les fichiers partagés strictement nécessaires à ce chapitre sont inclus et expliqués. Aucun lot nouveau regroupant plusieurs chapitres ne respecte cette progression. Les anciennes remises restent recevables et sont contrôlées chapitre par chapitre ; cette règle n’efface pas les lots déjà reçus.
6. Faire la contrelecture médicale et rédactionnelle indépendante, corriger les réserves bloquantes, construire le cours et le fragment, puis contrôler le navigateur sur ordinateur et mobile. Une simple compilation, une présence de fenêtres ou un contrôle de syntaxe ne clôt pas un chapitre. Consigner les commandes réellement exécutées et le commit exact contrôlé.
7. Intégrer dans les sources canoniques, reconstruire, publier les sources et le reçu, puis vérifier leur disponibilité et le déploiement du cours. Le reçu porte le code et l’intitulé complet, les commits reçus et intégrés, la contrelecture et les résultats des contrôles. Après cette preuve seulement, archiver le rapport et mettre `active_chapter` à `null` avant de réserver le chapitre suivant.
8. Ne passer au fragment suivant qu’après achèvement et contrôle de son périmètre attendu. La [règle de complétude CIM-11](../COMPLETUDE_CIM11.md) reste obligatoire : l’inventaire versionné, les entités pertinentes et leurs passages spécifiques doivent être contrôlés. Les compteurs CIM-10 ou les regroupements `covers` ne certifient aucune complétude CIM-11.

Une tâche bloquée reste active ; demander une décision explicite au propriétaire pour la suspendre et ouvrir une autre tâche. La contrelecture du chapitre de l’autre agent reste une activité de vérification, sans ouvrir une deuxième production. Les sous-agents peuvent travailler en parallèle sur les sources, Sciences, Examens, Pharmacologie, fenêtres et contrôles du même chapitre, avec un responsable par fichier. Ne pas lancer plusieurs productions de chapitres chez le même responsable ni commencer le chapitre suivant pendant l’attente d’intégration ou de publication du précédent.

Le plan ne réalise pas de verrou distant entre sessions. Chaque reprise doit vérifier son dernier commit partagé avant de réserver ou libérer un chapitre ; les conflits et changements concurrents sont signalés. Les sources transversales et cours communs conservent un producteur unique, avec renvois contrôlés dans les fragments consommateurs.

## Remise et visibilité

Déposer les sources dans `livraisons/Livraison Claude/<libellé>/` ou `livraisons/Livraison Codex/<libellé>/` suivant [DELIVERY_PROTOCOL.md](DELIVERY_PROTOCOL.md). Le code et l’intitulé complet nomment le chapitre dans chaque rapport et navigation. Actualiser ce plan, le tableau de bord et la passation à chaque clôture ; garder séparés « attribué », « actif », « reçu », « intégré », « contrôlé » et « publié ».
