# MEDINA — collaboration Codex et Claude

Ce dossier est le point d'entrée permanent pour consulter les livraisons, reprendre une mission et remettre une contribution.

- [Chaîne des dix fragments Codex, sentinelles et veille](CODEX_CHAINE_FRAGMENTS.md).
- [Signaux Codex : demande A41 et retours à Claude](SIGNAUX_CODEX.json).
- [Réception de la remise comparative Claude et réserves](receipts/CLAUDE_ESC2026_20261008_RECEPTION.json).
- [Cahier des charges opérationnel de Claude](CLAUDE_FRAGMENTS_CAHIER_DES_CHARGES.md).
- [Répartition des 21 fragments et progression par chapitre](FRAGMENTS_RESTANTS.md).
- [Dernière livraison et travaux à relire](HANDOFF_LATEST.md).
- [Inventaire des branches et livraisons](DELIVERIES_LATEST.md) et [accusés de réception](receipts/).
- [Mission globale de Claude](CLAUDE_AUDIT_GLOBAL_2026-10-07.md).
- [Inventaire des fichiers à relire](CLAUDE_REVIEW_SCOPE_2026-10-07.json).
- [Dépôt des rapports et procédure de remise](reviews/README.md).
- [Modèle de rapport](REVIEW_TEMPLATE.md) et [sources communes](SOURCES_CANONIQUES.md).
- [Règle de complétude CIM-11](../COMPLETUDE_CIM11.md).

## Autorisation permanente

Le 7 octobre 2026, Vial a expressément autorisé les publications GitHub de MEDINA et demandé les mêmes possibilités de contribution pour Claude. Dans ce périmètre, Codex et Claude peuvent publier leurs travaux, leurs rapports, leurs branches et leurs demandes d'intégration sans redemander cet accord. Les corrections restent soumises aux contrôles du projet et aux protections GitHub applicables.

Cette autorisation prime sur les anciennes mentions exigeant un accord de publication pour chaque lot. Elle concerne le travail MEDINA ; elle ne crée pas une session authentifiée ni de nouveaux droits techniques pour un outil externe.

## Accès effectivement disponibles

| Accès | État |
| --- | --- |
| Lecture publique du dépôt | Vérifiée ; les sources publiées sont accessibles sans connexion. |
| Administration par le compte GitHub du propriétaire | Vérifiée. |
| Écriture par Claude Code | Vérifiée pour la livraison I48/CS : deux commits et PR #8 publiés le 7 octobre. Chaque session conserve sa propre connexion. |
| Verrou exclusif entre IA | Aucun verrou ajouté. |

Claude Code connecté à GitHub avec une identité disposant du droit d'écriture peut créer des branches, pousser ses commits et ouvrir des pull requests dans ce dépôt. Claude dans un chat disposant seulement de la lecture publique peut examiner les sources et remettre un rapport ou un patch ; l'accord textuel du propriétaire ne lui donne pas la capacité technique de pousser.

La connexion peut être effectuée depuis [Claude Code sur le Web](https://claude.ai/code), selon la [documentation officielle](https://code.claude.com/docs/en/claude-code-on-the-web). L'[application GitHub Claude](https://github.com/apps/claude) est une référence de connexion ; sa présence ici ne signifie pas qu'elle est installée ou autorisée pour ce dépôt. Aucun identifiant ni jeton du propriétaire n'est transféré entre agents.

## Répartition

| Responsable | Travaux sur les 21 fragments restants |
| --- | --- |
| Claude | Production et reprise complète de ses 11 fragments ; contrelecture des chapitres Codex. |
| Codex | Production et reprise complète de ses 10 fragments ; contrelecture des chapitres Claude, coordination de l’intégration et de la publication. |

La répartition attribue **des fragments entiers** ; leurs catégories restent sous leur fragment et sont citées comme **code — intitulé (libellé complet du fragment)**. La [répartition obligatoire](FRAGMENTS_RESTANTS.md) impose un chapitre actif et un fragment actif par agent. Les 21 files sont enregistrées dans [production_plan.json](../../organisation/production_plan.json). La cardiologie conserve sa mission partagée ; elle n’est pas certifiée achevée. Chaque nouveau lot porte sur un seul chapitre, à clore avant de commencer le suivant.

Une attribution coordonne les fichiers ; elle ne bloque pas leur lecture ni leur accès GitHub. Les observations et les modifications sont identifiées par fichier, repère et commit. La disponibilité d'une mission ne prouve pas son démarrage : seul le rapport de Claude établit ce qu'il a effectivement relu.

## Cycle de livraison et de relecture

Au début de chaque reprise et avant de publier, Codex et Claude consultent **toutes les branches et PR**. L'absence d'un rapport à l'emplacement recommandé n'est pas une preuve d'absence de travail. Les rapports historiques et les branches sans PR sont recensés.

```bash
python3 tools/collaboration_sync.py --out docs/collaboration
```

Le scanner lit GitHub et produit l'index ; il ne fusionne aucun changement. `GH_TOKEN` peut fournir l'authentification et n'est jamais affiché. Si GitHub n'est accessible que par le connecteur, conserver son inventaire complet dans un JSON puis exécuter la même commande avec `--snapshot <inventaire.json>`. Une lecture partielle reste signalée.

Le [contrôle GitHub](../../.github/workflows/collaboration.yml) produit aussi un résumé et un rapport téléchargeable lors d'une PR, d'un push sur une branche contenant ce workflow ou d'un lancement manuel. Pour une ancienne branche qui ne contient pas encore le workflow, une PR vers la branche d'intégration déclenche ce contrôle. Le scanner ne dépend pas de la présence d'un manifeste de livraison.

1. Codex termine un lot, exécute les contrôles adaptés, puis pousse les sources et leurs rapports avant d'annoncer la livraison.
2. Il actualise `HANDOFF_LATEST.md` avec le commit de contenu, les fichiers, les tests et les limites. Chaque nouveau lot reçoit une ligne dans la file de relecture, avec sa propre base de commit.
3. Claude lit les instructions à la tête actuelle de la branche, puis relit le contenu au commit fixé dans sa mission. Il consigne sa couverture réelle et travaille sur sa branche de contribution.
4. Avec une connexion GitHub autorisée en écriture, Claude pousse ses commits et ouvre une PR vers `codex/sciences-cs-fragments-20261007`. Sans cet accès, il remet un rapport et un patch suivant la procédure de [remise](reviews/README.md). Une livraison existante sur une autre branche est récupérée au même titre.
5. Codex ouvre les rapports et les différences, puis enregistre la réception dans `receipts/`. Il vérifie les sources et les conflits, reconstruit et teste. Le reçu indique ensuite le commit d'intégration, les adaptations et les réserves non résolues. L'index et la passation sont actualisés.

Le rattachement suit les chemins exacts : cours dans `chapters/<CODE>/`, déclarations dans `chapters.json` et `fragments.json`, glossaires globaux dans `glossary/`, CS cardiovasculaire dans `modules/cardiovascular_cs.*` pour S01. Une contribution SYSTEM nécessite une route d'affichage explicite. Les HTML sous `dist/` sont des résultats de construction.

Une nouvelle livraison ne modifie pas rétroactivement la base d'une relecture engagée. Les changements concurrents sont signalés avec leurs commits ; les protections du dépôt restent applicables.

## Branches et états

- Branche de livraison et d'intégration : `codex/sciences-cs-fragments-20261007`.
- Branche de relecture globale : `claude/review-medina-global-20261007`, préparée avec le contenu de référence et les consignes publiées.
- Ancienne branche I48 : `claude/review-i48-esc2024-20261007` ; sa mission reste une sous-tâche de l'audit global.

Les états « publié », « relu », « corrigé », « testé techniquement » et « vérifié médicalement » restent distincts. Une rédaction révisée ne certifie pas la complétude CIM-11.

## Justifications physiopathologiques

- [Répartition Codex / Claude et suivi par cours](MECHANISMS_PLAN.json).
- [Consigne exhaustive pour Claude et remise contrôlée](MECHANISMS_CLAUDE.md).
- [Consigne déjà transmise à Claude dans PR #10](https://github.com/vialdjoukang-spec/Medina/pull/10#issuecomment-6041361558).

Les contrôles techniques prouvent l’ouverture des fenêtres et la conservation du contenu ; ils ne prouvent pas que chaque affirmation a reçu sa justification ni que la CIM-11 est complète.
