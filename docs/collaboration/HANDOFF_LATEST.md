# MEDINA — dernière passation

## Nouvelle organisation — 8 octobre 2026

Les **21 fragments hors C-01-Cardiologie** sont attribués : **11 fragments entiers à Claude, 10 fragments entiers à Codex**. Lire [FRAGMENTS_RESTANTS.md](FRAGMENTS_RESTANTS.md), [production_plan.json](../../organisation/production_plan.json) et [CODEX_CHAINE_FRAGMENTS.md](CODEX_CHAINE_FRAGMENTS.md). Un chapitre actif par responsable ; contrôle, intégration et publication avant le suivant. Codex prend le relais de GPT « work » et ouvre maintenant **A41 — Sepsis et choc septique de l’adulte (I-03-Infectiologie)** à la base actuelle `39b7ff0cc585c59ffbb99fb448940daa1950b34d`. La cardiologie conserve son backlog et ses réserves ; elle n'est pas déclarée complète. Les sous-agents progressent en parallèle dans le seul chapitre courant ; les sentinelles contrôlent la réception, la relecture médicale et les vérifications techniques. Claude audite Codex et Codex audite Claude **avant injection**. Toutes les catégories restent sous leur fragment respectif ; les citer comme **code — intitulé (libellé complet du fragment)**.

Les paragraphes datés du 7 octobre ci-dessous restent un historique ; les états les plus récents de l’intégration et les reçus doivent être relus avant production. La première organisation a été publiée sur `main` à `20915d9a36f0ebc65a79ec6428357727dd5afe6c` et sur l'intégration à `b6e5d18c2c2383893819c4c0834d6402bbe30e67`. Les sources cliniques de ces branches divergent : ne pas remplacer leurs corrections par une copie ancienne lors d'une publication de coordination.

## Réception et veille — état du 8 octobre 2026

Claude a accusé lecture de son [cahier des charges](CLAUDE_FRAGMENTS_CAHIER_DES_CHARGES.md) dans `livraisons/Livraison Claude/C-01-Cardiologie/ACCUSE_PRISE_EN_CHARGE_2026-10-08.md` (commit `7aba794a1d77979052e6104a3a5afc05698046db`, document de mission lu à la base d'intégration `b6e5d18c2c2383893819c4c0834d6402bbe30e67`). Cet accusé ne constitue pas un audit de la production Codex.

La première tête reçue `d8dae520c4d19213d0aa0099f3da34ca974b2c1d` a fait l'objet de trois rapports indépendants : [réception](reviews/2026-10-08/VEILLE_CLAUDE/RECEPTION.md), [contrelecture médicale ciblée](reviews/2026-10-08/VEILLE_CLAUDE/AUDIT_MEDICAL.md) et [audit technique](reviews/2026-10-08/VEILLE_CLAUDE/AUDIT_TECHNIQUE.md). Une tête ultérieure `3f90204dc663d6f7dee3e98bbd5819d457b6a586` comporte une nouvelle remise comparative, reçue dans [RECEPTION_ACTUALISEE.md](reviews/2026-10-08/VEILLE_CLAUDE/RECEPTION_ACTUALISEE.md). Relire les sections datées des audits : un contrôle de la première tête ne valide pas la suivante. Les sources primaires ESC restent à consulter indépendamment et aucune nouvelle injection clinique n'est autorisée par la seule détection.

La veille [tools/claude_watch.py](../../tools/claude_watch.py) inspecte toutes les têtes de branches et de PR par Git, y compris les livraisons historiques sur branches neutres, conserve les empreintes et déduplique les candidats. L'état local reste hors checkout : `/workspace/medina-env/claude-watch/{status,queue,state}.json`. La boucle locale relève les changements toutes les cinq minutes tant que son processus et la machine vivent. Le [workflow GitHub](../../.github/workflows/claude_watch.yml) prévoit une collecte toutes les quinze minutes sur la branche par défaut et conserve les JSON comme artefacts ; l'ordonnanceur GitHub peut retarder les exécutions. Il détecte et met en file, sans lancer une session IA, auditer médicalement ni injecter automatiquement.

Pour A41, lire le [rapport de reprise](../../livraisons/Livraison%20Codex/I-03-Infectiologie/travail/A41-2026-10-08/rapport.md) et la [demande à Claude](../../livraisons/Livraison%20Codex/I-03-Infectiologie/travail/A41-2026-10-08/DEMANDE_LECTURE_CROISEE_CLAUDE.md). Le chapitre reste actif pendant l'inventaire, la vérification des sources et la lecture croisée. Les autres fragments restent dans leur file ; aucune fermeture ni complétude CIM-11 n'est déduite des contrôles logiciels.

Mise à jour : 7 octobre 2026. **Lot 4 I48 : intégré, vérifié et publié.** Le contenu contrôlé est publié sur l’intégration et `main` au commit `e856ed16893ba5c4ffc3bd4c9ca78a38ce533de6` ; [ouvrir I48](https://vialdjoukang-spec.github.io/Medina/fragments/MEDINA_S01_cardiovasculaire.html#/entry/I48). Le déploiement Pages a réussi et le contenu servi a été comparé intégralement au build testé. Le [tableau commun](../../organisation/MEDINA_Organisation.html) et sa [version publiée](https://vialdjoukang-spec.github.io/Medina/organisation.html) réunissent les 22 fragments, les 265 blocs et les 1 636 catégories du catalogue historique. Les plateformes originales reprennent désormais cette organisation : catégories numérotées, chapitres ordonnés, codes discrets en haut à droite et couleurs lisibles.

## Priorité : expliquer pourquoi

La règle de Vial vaut pour chaque affirmation médicale et chaque décision, dans les quatre onglets et tous leurs contenus. Les ajouts ciblés de ce lot comprennent **197 fenêtres physiopathologiques sur 15 cours**, avec 197 cibles explicites, conséquences cliniques, limites et sources. Le bilan initial de I50 — Insuffisance cardiaque dispose notamment d’explications distinctes pour anémie, sodium et potassium. L’injection se fait au moment de la compilation, sans réécriture silencieuse des HTML canoniques.

**La relecture exhaustive de toutes les affirmations n’est pas terminée.** Le [suivi par cours](MECHANISMS_PLAN.json) garde les 30 cours de départ en `pending_exhaustive_review`. La répartition retenue est 15 Codex / 15 Claude ; la [mission Claude](MECHANISMS_CLAUDE.md) précise ses cours, la revue attendue et la remise. [Sa consigne commune reçue](MISSION_JUSTIFICATION_2026-10-07.md) est alignée sur ce partage ; sa proposition originale est archivée intacte.

La production suit **C-01-Cardiologie en premier**, avec le partage **15 Codex / 15 Claude**. Les fenêtres suivent le passage concerné : synthèse, mécanisme causal, conséquence clinique, limites et sources. Aucun quota arbitraire de mots ; garder les précautions qui changent la décision visibles dans le texte principal. I48 sert de pilote livré ; la revue exhaustive de la suite reste ouverte.

## Nouveau cours regroupé

**J40 — Bronchite** réunit J20, J40, J41 et J42 dans un cours : aiguë, chronique simple et mucopurulente, avec leurs limites diagnostiques. La bronchite chronique n’est pas assimilée automatiquement à la BPCO. Les quatre onglets, 40 fenêtres, cinq unités de Sciences, quiz et Pareto sont accessibles dans P-02-Pneumologie. Les variantes restent consultables dans les catégories ; la recherche n’affiche qu’une carte Bronchite. Le total est désormais **31 cours intégrés**.

## Livraisons Claude reçues et injectées

| Livraison | État |
| --- | --- |
| Alpha, PR #1 | Fusion historique conservée. |
| Relecture FA et CS, PR #8 | Intégrée ; reçu historique conservé. |
| Audit global lot 1, PR #9 | Huit cours / 17 sources intégrés auparavant ; reçu conservé. |
| PR #10, lots 2 et 3, tête `be6a909059200711493064bd9c96a7437d71c019` | 27 sources injectées après contrôle des empreintes : sept sources I48 et vingt fichiers Sciences. Original et rapports Claude conservés sous Livraison Claude. Contrelecture I48 et deux arbitrages I10/I42 documentés. |
| PR #11, mission, tête `45d34a9bd3034a141239d9cefc774804c10163fb` | Consigne reçue ; proposition initiale archivée, répartition publiée alignée sur le suivi. |
| PR #12, lot 4 I48, tête reçue `b1f19c3510c1a828650867da033ebe2fbf30142e` | **Injecté, vérifié et publié** au commit `e856ed16893ba5c4ffc3bd4c9ca78a38ce533de6`, arbre identique au commit local testé `201c9c1a4c5b60e4126338e944355a0b2a5e9cc1`. Huit sources I48 et glossaire repris ; les 11 arbitrages sont conservés. Adaptations ciblées, priorité des fenêtres vertes sur leurs abréviations imbriquées, publication atomique des HTML. [Reçu](receipts/CLAUDE_I48_LOT4_2026-10-07.json) et [rapport Codex](../../audits/INTEGRATION_I48_LOT4_2026-10-07/README.md). |

Le lot I48 contient désormais 66 578 mots, 100 fenêtres natives et 206 déclencheurs verts dans les quatre onglets, plus 15 dans Pareto. Les contrôles techniques finaux comprennent 80 tests unitaires et 7 891 contrôles navigateur réussis, puis 54 contrôles sur la version publique après déploiement. Un inventaire ultérieur a repéré **huit cours supplémentaires remis par Claude** à `b6db50cb` : I30, I33, I35, I34, I00, I40, I42 et I44. Ils sont [reçus, avec contrôle et injection en attente](receipts/CLAUDE_EIGHT_COURSES_PENDING_2026-10-07.json) ; ils ne sont pas déclarés intégrés. Le manifeste reprend aussi I48 : ne pas écraser ses adaptations Codex publiées. Les quatre propositions I48_pop1–pop4 ont aussi changé depuis `b1f19c3` ; les comparer à trois voies avant une prochaine injection. Les étapes « faites » de Claude restent des résultats annoncés, à vérifier.

Les [reçus](receipts/) distinguent réception, injection, vérification et commit publié. Les réserves médicales héritées restent ouvertes, notamment certains schémas J44/J18 et les points I48 non couverts par les arbitrages documentés. Une relecture de prose ne certifie pas tout le cours.

## Dossiers et accès permanents

Le dépôt entier est partagé par GitHub. Après publication, les 22 dossiers [Livraison Codex](../../livraisons/Livraison%20Codex/) contiennent les sources complètes, banques incluses, et un manifeste portant le commit réel de la remise. Déposer les corrections sous [Livraison Claude](../../livraisons/Livraison%20Claude/) sur sa branche, conformément au [protocole](DELIVERY_PROTOCOL.md). Codex examine les différences, contrôle les empreintes puis injecte dans les fichiers canoniques avant reconstruction. L’autorisation permanente de Vial couvre ces contributions et publications ; elle ne remplace pas la connexion GitHub effective et ne justifie aucun transfert de secrets.

## Contrôles et limites

Les rapports des mécanismes ciblés se trouvent dans [audits/MECANISMES_2026-10-07](../../audits/MECANISMES_2026-10-07/). La réception du lot 4 I48 et ses preuves finales sont dans [audits/INTEGRATION_I48_LOT4_2026-10-07](../../audits/INTEGRATION_I48_LOT4_2026-10-07/). Ils distinguent les fenêtres ciblées compilées, les vérifications navigateur et les contrelectures médicales partielles. Le workspace a été restauré à une ancienne version durant le lot : certaines banques ont été régénérées, puis les contrôles ont été refaits. Les résultats perdus ne sont pas présentés comme validation des fichiers nouveaux.

Le catalogue reste **CIM-10-GM 2024**. La complétude **CIM-11 n’est pas établie** : ne déclarer aucun système achevé sans inventaire validé de toutes les catégories et sous-catégories demandées. PR #6 accueil/QCM reste une branche distincte à traiter séparément.

À chaque reprise et avant publication, lire [les livraisons repérées](DELIVERIES_LATEST.md), les branches/PR et leurs nouvelles pages, les dossiers Claude et les reçus. La présence d’un manifeste facilite le suivi ; son absence ne justifie pas d’ignorer une livraison ancienne. Vérifier séparément le déploiement du site.
