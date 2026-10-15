# Mission exclusive Claude : audit sévère → corrections → injections → PR

**Mandat directement donné par Vial le 14.10.2026 à 22 h 29 Europe/Zurich.** Claude reprend les quatre cours G45/E10/N18/D64 sans confier à Codex une injection, un audit automatique fictif ou une PR. Aucun Cycle 3.

## 1. Vérifier les bases réelles
1. Examiner `AGENTS.md`, `CLAUDE.md`, `PROMPT_MEDINA.md`, `PROMPT_TRANSITION.md`, `CHAPTER_SPEC.md`, `docs/STYLE_REDACTION.md`, `docs/collaboration/instructions/CLARTE_BASES_CALCULS_VIAL_2026-10-11.md`, `organisation/execution-20261014/CONTRAT_REVUES.md`, le cahier du Cycle 2 et les derniers arbitrages de Vial.
2. Comparer les nouveaux HEAD de `main`, de la branche de remise et toutes les PR en cours ; ne pas écraser les contributions Claude déjà fusionnées au Cycle 1. Transcrire les SHA exacts.
3. Déclarer un responsable Claude unique du Cycle 2, dater le transfert. L'ancienne échéance du 14 octobre 08 h 00 ne doit pas être réutilisée comme autorisation de travail nocturne ; cette demande est une reprise **distincte et actuelle**.

## 2. Examiner les corrections préparatoires
1. Lire la livraison brute des 4 auteurs et les 4 `pass1.json` (ainsi que `G45/reserves_pass1.json`).
2. **Deux propositions superposables sur le fond mais non à cumuler mécaniquement** : (a) `G45_R1_R3_PROPOSITION.json` présent dans cette remise, deux fichiers proposés, jamais injectés ; (b) `tools/cycle2_reprise_01_safety.py`, 16 modifications préparées dans 8 fichiers, avec échec CI avant commit. Comparer leur contenu ; sélectionner une version cohérente, corriger doublons/ambiguïtés, ne pas appliquer aveuglément les deux.
3. Les documents d'archive des FI et de recommandations sont parfois **volontairement locaux** pour des raisons de droits de redistribution. Rechercher les sources permises ou les consulter à nouveau ; conserver URL, section, date réelle, locateurs et empreintes. Ne pas attester de lecture d'une archive inaccessible.
4. FI suisses des **produits/formulations exacts** d'abord, recommandations suisses puis européennes contextualisées. Vérifier spécialement les omissions d'Aspirine Cardio, Sortis, Eliquis, Baqsimi, Kerendia, Benadon, Exjade et Pegasys.
5. Corriger **les 25 réserves**, sans inventer de résultats. Rétablir intégrité des mots interactifs, quatre onglets, quiz, sciences, calculs et unités, tableaux, 32 figures, licences et 74 sous-codes.

## 3. Relectures indépendantes, sur versions figées
1. Demander les **secondes passes croisées** seulement après correction. Attribution historique : neurologie ↔ hématologie, endocrinologie ↔ néphrologie ; si aucun des relecteurs initiaux n'est disponible, expliciter la nouvelle affectation et ne pas se faire passer pour le relecteur antérieur.
2. Après les 4 clôtures croisées réelles, mener les contre-audits par agents distincts **à contexte neuf** : première passe, corrections, deuxième passe, avec empreintes de fichiers.
3. Contrôler réellement les 4 dimensions : **médecine, sources primaires/fiabilité, langue pédagogique, frontend**. Consigner les divergences et arbitrages. Aucun score 20/20 ni « validation humaine » sans preuve.

## 4. Vérifications techniques et visuelles
- Exécuter les tests actuels sans diminuer leurs seuils ; construire le portail et les fragments ; tester desktop/mobile.
- Contrôler navigation des 4 onglets, sous-onglets, fenêtres et lexique, quiz, liens, légendes, agrandissements, sorties et retours ; tests de non-régression.
- Vérifier 32 figures une par une : auteur, licence du fichier exact, URL, exactitude anatomoclinique, cohérence du texte alternatif et accessibilité.
- Produire **de vraies captures** ouverture/fenêtre par leçon et preuves d'exécution. Toute correction post-audit impose une relecture de sa nouvelle empreinte.

## 5. PR, injection, publication et arrêt
1. À l'issue des audits complets et sans réserve bloquante, préparer l'intégration **cours par cours** dans l'ordre **G45 → E10 → N18 → D64** ; ne jamais forcer `main` ni court-circuiter les gardes.
2. **Claude crée lui-même la PR**, renseigne sources, commits, liste des réserves résolues, tests et captures ; il prend en charge ses corrections, l'injection et l'intégration selon les règles du dépôt.
3. Valider l'injection canonique effective, lancer/relever GitHub Pages et **vérifier le rendu public réellement servi** après intégration. Conserver URLs, SHA et résultats ; ne pas appeler « publié » un simple `push`.
4. Après vérification finale : actualiser les registres honnêtement et déclarer le Cycle 2 clos. Ne pas lancer Cycle 3 ; arrêter les écritures conformément à l'ordre de Vial.

**Critères de clôture** : 4/4 cours corrigés, 25/25 réserves tranchées avec preuves, 4/4 revues croisées complètes et 4/4 contre-audits complets, contrôles et licences des 32 images, CI/QA satisfaisantes, PR Claude, 4 injections canoniques et vérification du site public. Aucune de ces conditions ne doit être cochée sans preuve réelle.
