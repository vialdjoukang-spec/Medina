# MEDINA — transition directe vers Codex, 8 octobre 2026

Reprendre le dépôt `vialdjoukang-spec/Medina` à partir de cette branche de passation, `codex/transition-cardio-20261008`, puis rapprocher les dernières têtes de `main` et de `codex/sciences-cs-fragments-20261007`. La base distante vérifiée lors de cette passation est `83bff147e0aba6b31e7a080e098770b0a6b4250d`. Ne pas remplacer une correction plus récente par une ancienne copie.

## Instruction actuelle

Les instructions publiées du 8 octobre remplacent la priorité historique qui imposait d'achever la cardiologie avant toute autre file. Lire d'abord `AGENTS.md`, `CLAUDE.md`, `docs/collaboration/HANDOFF_LATEST.md`, `docs/collaboration/CODEX_CHAINE_FRAGMENTS.md`, `docs/collaboration/FRAGMENTS_RESTANTS.md`, `organisation/production_plan.json` et `docs/collaboration/SIGNAUX_CODEX.json`.

Codex reprend **A41 — Sepsis et choc septique de l’adulte (I-03-Infectiologie)**, déjà actif, au stade attesté par le plan et son rapport. Lire `livraisons/Livraison Codex/I-03-Infectiologie/travail/A41-2026-10-08/rapport.md` et `DEMANDE_LECTURE_CROISEE_CLAUDE.md`. Vérifier si Claude a depuis remis son audit au SHA demandé. Le chapitre demeure actif tant que sa chaîne n'est pas close. Conserver les réserves cardiologiques dans le backlog.

Les 21 autres fragments restent partagés **10 fragments entiers Codex / 11 fragments entiers Claude**. Les noms et files complets sont dans FRAGMENTS_RESTANTS.md. Un seul chapitre de production est actif par responsable ; plusieurs sous-agents peuvent travailler dans ce seul chapitre. Le dispositif prévoit 24 missions en quatre vagues de six, avec au maximum six sous-agents simultanés si la capacité de la session est de sept agents coordinateur compris. Un auteur par fichier ; le coordinateur seul réalise les opérations Git communes.

## Travail cardiologique préservé

La convergence du lot 5 et d'I48 est déjà documentée dans la passation actuelle. Ne pas refaire l'ancienne injection ni réutiliser les anciens contrôles pour un nouveau contenu. Préserver les adaptations médicales, le glossaire, le moteur et les comparaisons contextuelles.

Cette branche ajoute un **dossier de conservation**, `livraisons/Livraison Codex/C-01-Cardiologie/transition-20261008/`, pour les sources pédagogiques I73 — Autres maladies vasculaires périphériques et I95 — Hypotension, leurs glossaires, l'outil de transfert gelé et les rapports ciblés utiles. Ces copies proviennent du checkpoint local `939582701b4af43694fb56be3ae01917cc5dd8ce`, descendant de `505ee74d07622680c6513891e91b54fff628365a`. Elles restent des contributions de backlog : **aucune injection canonique, aucun enregistrement de catalogue, aucune activation d'un second chapitre et aucun déploiement ne sont réalisés par cette passation**.

I73 couvre I73/I77/I78 ; I79 reste un renvoi. I95 couvre I95. Les catégories prévues dans S01 sont respectivement `vaisseaux` et `pression`. Les sources avaient passé compilation isolée, package et check selon les rapports du gel ; le rendu officiel intégré reste à contrôler. Examiner les contrelectures et actualiser les sources avant toute utilisation. Le dossier conserve aussi les adaptations proposées aux anciens cours ; les rapprocher des corrections déjà publiées plutôt que les réappliquer automatiquement.

La branche de référence a encore des réserves MED-01/02/03 dans les remises cardiologiques ultérieures de Claude. L'ancienne tête `482a6799...` était incomplète ; la remise `f2e9934c...` a restauré 25 sources, mais n'a pas levé ces réserves médicales. Toute tête plus récente doit être examinée pour son delta. La tête Claude repérée lors de cette reprise est `a0b020489cceba1e7a0f90d791a8a122ab5aa07e` ; sa disponibilité ne constitue pas son audit.

## Exécution et qualité

Au début, inventorier toutes les branches et PR avec pagination, puis exécuter `python3 tools/collaboration_sync.py --out docs/collaboration` ou son mode snapshot si nécessaire. Relever les SHAs exacts, ouvrir rapports, reçus et différences. Ne pas conclure à l'absence d'une livraison depuis un index ancien.

Chaque affirmation médicale doit répondre à « pourquoi » : fonctionnement normal, perturbation, mécanisme précis, conséquence clinique et décision, avec limites et source primaire réellement consultée. Préférer les mots verts ouvrant des fenêtres contextualisées. Cette règle couvre les quatre onglets, tableaux, figures et flèches, quiz et distracteurs, Pareto, fenêtres, glossaires et références. La citation seule ne remplace pas l'explication. Garder les restrictions qui changent la décision dans le texte principal.

Vérifier les référentiels suisses, les informations professionnelles et les recommandations récentes. Distinguer causalité, association et hypothèse. Ne pas inventer de gold standard universel. Les sciences et schémas doivent expliquer la maladie concernée. Le français reste précis, professionnel et en phrases courtes complètes, sans quota de mots. Préserver le site existant, les onglets, les icônes, Navigo, les routes et l'affichage PC/mobile.

**Audit croisé avant injection : Claude audite Codex, Codex audite Claude.** Corriger les réserves bloquantes et faire contre-vérifier le SHA corrigé ; un sous-agent du producteur ne remplace pas l'autre responsable. Le trio de sentinelles contrôle séparément médecine, provenance et technique aux étapes délicates. Reconstruire après injection, exécuter les contrôles adaptés, publier sources et reçus, puis vérifier le déploiement et le contenu servi. Après clôture prouvée seulement, ouvrir le chapitre suivant.

Les anciennes preuves locales (95 tests unitaires et 49 171 assertions navigateur sur seize cours) concernent le gel antérieur ; elles ne certifient ni cette nouvelle branche, ni A41, ni l'intégration future d'I73/I95. Les archives complètes de tests, captures, téléchargements et historique local n'ont pas été exportées dans ce transfert restreint. Les preuves publiées plus récentes et leurs SHAs restent dans la passation et les reçus du dépôt.

Aucun fragment n'est déclaré complet sans inventaire officiel versionné et audit du périmètre CIM-11. Vial a déjà autorisé les publications et intégrations nécessaires au projet : poursuivre les opérations autorisées après les contrôles, sans confirmation routinière.
