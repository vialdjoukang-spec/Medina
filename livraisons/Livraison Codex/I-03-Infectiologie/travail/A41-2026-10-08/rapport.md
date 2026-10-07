# A41 — Sepsis et choc septique de l’adulte (I-03-Infectiologie)

## Prise en charge Codex — 8 octobre 2026

Fragment actif : **I-03-Infectiologie**, premier des dix fragments entiers de la file Codex. Chapitre unique actif : **A41 — Sepsis et choc septique de l’adulte (I-03-Infectiologie)**. Base canonique : `b6e5d18c2c2383893819c4c0834d6402bbe30e67`.

La mise en route suit la nouvelle consigne de chaîne séquentielle. Le backlog C-01-Cardiologie reste conservé avec ses réserves ; aucune complétude n’est déclarée.

## Périmètre de reprise

Les quatre onglets, toutes les fenêtres et justifications, figures, quiz, Pareto, glossaire, doses, indications et références sont inclus. Lire les sources canoniques de ce seul chapitre avant d’attribuer les missions ; un auteur par fichier. Pour ce chapitre, Pathologie occupe `A41_a.html` et `A41_b.html`, Examens et Sciences partagent `A41_c.html`, et Pharmacologie occupe `A41_d.html`. Attribuer les écritures selon ces fichiers réels : deux auteurs ne peuvent pas écrire simultanément les deux panneaux de `A41_c.html`.

- `chapters/A41/A41_a.html`
- `chapters/A41/A41_b.html`
- `chapters/A41/A41_c.html`
- `chapters/A41/A41_d.html`
- `chapters/A41/A41_justifications.json`
- `chapters/A41/A41_pop1.html`
- `chapters/A41/A41_pop2.html`
- `chapters/A41/A41_pop_pa.html`
- `chapters/A41/A41_pop_sciences_revision.html`

## État réel

Réservé pour inventaire et revue initiale ; aucune nouvelle rédaction médicale ni validation exhaustive n’est annoncée par ce rapport. La revue des référentiels actuels et l’audit croisé de Claude restent requis avant toute injection d’une correction. La source canonique reste intacte pendant cette phase.

Les missions spécialisées et les sentinelles sont détaillées dans `docs/collaboration/CODEX_CHAINE_FRAGMENTS.md`. Les livraisons Claude détectées sont examinées en parallèle comme activité de réception et d’audit, sans ouvrir une deuxième production Codex.

## Vérifications préparatoires et évolution de la base

À la base initiale `b6e5d18c2c2383893819c4c0834d6402bbe30e67`, la construction globale hors checkout et les contrôles statique/navigateur `test_v7.py A41` ont réussi : 42 803 mots mesurés par le test, 63 fenêtres, 8 quiz et 10 déclencheurs Pareto. Ces contrôles de fonctionnement ne sont pas une contrelecture médicale exhaustive.

Pendant la reprise, l'intégration distante a avancé à `39b7ff0cc585c59ffbb99fb448940daa1950b34d`, avec des changements préexistants dans les fichiers A41. Cette nouvelle base est conservée et devient le SHA demandé à Claude ; l'inventaire distingue les empreintes et les contrôles de l'ancienne base. Les corrections antérieures ne doivent pas être écrasées par une copie de `b6e5d18`.

Les sources officielles SCCM et WHO ont renvoyé `CONNECT 403` dans cette instance. Les domaines nécessaires sont proposés dans le brouillon de configuration cloud avec les instructions de redémarrage de la veille ; leur sauvegarde ne prouve pas encore l'accès. La vérification indépendante des recommandations et de la cartographie CIM-11 reste ouverte.
