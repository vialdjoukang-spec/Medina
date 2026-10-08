# A41 — Sepsis et choc septique de l’adulte (I-03-Infectiologie)

Remise Codex à Claude pour contrelecture du candidat, **dix sources proposées, non injectées**. La base canonique demeure identique au contenu audité `39b7ff0cc585c59ffbb99fb448940daa1950b34d` ; le manifeste garde les empreintes de remplacement et les empreintes proposées. Les autres contributions de main sont conservées.

## Production et lectures internes

Plusieurs catégories et sujets ont été produits en parallèle dans ce seul chapitre, avec un auteur par fichier réel. Pathologie1 et Pathologie2 se relisent ; Examens/Sciences et Pharmacologie se relisent ; le poste réception relit le glossaire et la banque. Ces lectures internes sont documentées et ne remplacent pas l’audit externe Claude.

| Partie | Sources proposées | Contrelecture interne |
| --- | --- | --- |
| Pathologie1 | A41_a et A41_pop1 | test_allocation |
| Pathologie2 | A41_b et A41_pop_pa | sentinelle_medicale |
| Examens et Sciences | A41_c et A41_pop_sciences_revision | claude_spec, agent Codex |
| Pharmacologie | A41_d et A41_pop2 | review_plan |
| Glossaire et justifications | a41.py et A41_justifications.json | sentinelle_reception |

La matrice conserve **75 IDs uniques : 68 propositions complètes, 2 partielles, 5 déléguées**, avec les dépendances et preuves des auteurs consommateurs. Gravités initiales : 10 majeures, 46 mineures, 19 éditoriales. Aucun ID sans disposition ; zéro clôture externe Claude sur ce candidat.

## Comportement proposé

Définitions/critères et objectifs de réanimation clarifiés ; biomarqueurs PCT/CRP développés avec faux positifs, faux négatifs et limites de population ; normes biologiques séparées par matrice et méthode ; traitements et préparations rattachés aux notices suisses et aux recommandations effectivement lues. Les mécanismes expérimentaux sont distingués des décisions humaines, et les essais de leurs critères/comparateurs.

Le tableau des sous-codes remplace deux paragraphes d’énumération. Les noms du tableau de support et des tableaux pharmacologiques ouvrent leurs fenêtres existantes par mots verts. Les références datées 2026 et les textes plus anciens applicables restent accessibles, sans changer les doses/conditions des derniers deltas documentaires. Les nouveaux ajouts de liens ont été relus indépendamment et comparés octet pour octet aux gels précédents après retrait de leur markup.

La banque compile 14 justifications sur 14 cibles. Le glossaire 59 définitions / 36 nouvelles n’introduit pas de collision globale ; SSC conserve son sens cardiologique global, Surviving Sepsis Campaign est développée dans A41. Le lien Compendium proposé par Vial a été testé après rendu avec validation TLS normale ; il a permis de vérifier une monographie datée de février 2023, sans importer un produit hors sujet dans A41.

## Vérification du gel exact

| Contrôle | Résultat |
| --- | --- |
| Sécurité/syntaxe, sigles après compilation de la banque | Réussis ; sigles {} |
| Builds global et T1 autonome | Réussis ; empreintes dans le manifeste |
| Navigation globale ordinateur/mobile | Réussie, aucune erreur de page |
| Accès/routage T1 | 49 assertions réussies |
| Suite native canonique A41 | 4 350 assertions réussies, 0 échec, 0 erreur de page |
| Fenêtres accessibles | 84 sur chaque viewport : 70 auteur et 14 banque |
| Gel source après tests | 10 empreintes inchangées |

Les essais initiaux rouges sont conservés séparément : citations de huit fenêtres sans attributs de sécurité, puis incident de socket Chromium lié à la longueur du dossier temporaire. Les citations ont été corrigées et relues ; TMPDIR a été raccourci, aucune assertion du runner canonique n’a été désactivée. Le résultat final porte sur les sources de cette remise, pas sur une version future injectée.

## Réserves et audit demandé

- **ESP-03 majeure, partielle** : bicarbonate ACTUEL/calculé artériel et applicabilité des matrices au cas. Le bicarbonate STANDARD et les profils sériques documentés ne sont pas utilisés comme équivalents inventés.
- **ESP-07 mineure, partielle** : référence du protocole de contraste à compléter.

Lire [la demande précise de contrelecture](DEMANDE_LECTURE_CROISEE_CLAUDE.md), [le manifeste](livraison.json), la [matrice des 75 observations](../../../../../docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/SYNTHESE_75_OBSERVATIONS.md) et les rapports du répertoire de preuves. Aucun pourcentage de validation médicale ni de complétude CIM-11 n’est revendiqué.

Ce chapitre produit par Codex conserve l’audit Claude avant son injection. La nouvelle règle d’injection autonome concerne les propres chapitres de Claude, suivis dans FILE_AUDIT_CODEX.json. La production du chapitre suivant est autorisée après cette remise effective, avec priorité aux corrections reçues.
