# MEDINA — collaboration Codex et Claude

Ce dossier est le point d'entrée permanent pour consulter les livraisons, reprendre une mission et remettre une contribution.

- [Dernière livraison et travaux à relire](HANDOFF_LATEST.md).
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
| Authentification et écriture par Claude | Non vérifiées ; elles dépendent de sa connexion GitHub effective. |
| Verrou exclusif entre IA | Aucun verrou ajouté. |

Claude Code connecté à GitHub avec une identité disposant du droit d'écriture peut créer des branches, pousser ses commits et ouvrir des pull requests dans ce dépôt. Claude dans un chat disposant seulement de la lecture publique peut examiner les sources et remettre un rapport ou un patch ; l'accord textuel du propriétaire ne lui donne pas la capacité technique de pousser.

La connexion peut être effectuée depuis [Claude Code sur le Web](https://claude.ai/code), selon la [documentation officielle](https://code.claude.com/docs/en/claude-code-on-the-web). L'[application GitHub Claude](https://github.com/apps/claude) est une référence de connexion ; sa présence ici ne signifie pas qu'elle est installée ou autorisée pour ce dépôt. Aucun identifiant ni jeton du propriétaire n'est transféré entre agents.

## Répartition

| Responsable | Travail |
| --- | --- |
| Codex | Création et intégration, interface, modèles, construction et contrôles techniques. |
| Claude | Relecture intégrale, précision médicale, français professionnel, progression didactique et corrections documentées. |

Une attribution coordonne les fichiers ; elle ne bloque pas leur lecture ni leur accès GitHub. Les observations et les modifications sont identifiées par fichier, repère et commit. La disponibilité d'une mission ne prouve pas son démarrage : seul le rapport de Claude établit ce qu'il a effectivement relu.

## Cycle de livraison et de relecture

1. Codex termine un lot, exécute les contrôles adaptés, puis pousse les sources et leurs rapports avant d'annoncer la livraison.
2. Il actualise `HANDOFF_LATEST.md` avec le commit de contenu, les fichiers, les tests et les limites. Chaque nouveau lot reçoit une ligne dans la file de relecture, avec sa propre base de commit.
3. Claude lit les instructions à la tête actuelle de la branche, puis relit le contenu au commit fixé dans sa mission. Il consigne sa couverture réelle et travaille sur sa branche de contribution.
4. Avec une connexion GitHub autorisée en écriture, Claude pousse ses commits et ouvre une PR vers `codex/sciences-cs-fragments-20261007`. Sans cet accès, il remet un rapport et un patch suivant la procédure de [remise](reviews/README.md).
5. Codex compare les changements, vérifie les sources et les conflits, reconstruit et teste. Il intègre les corrections recevables et consigne le commit d'intégration ; il expose les réserves non résolues.

Une nouvelle livraison ne modifie pas rétroactivement la base d'une relecture engagée. Les changements concurrents sont signalés avec leurs commits ; les protections du dépôt restent applicables.

## Branches et états

- Branche de livraison et d'intégration : `codex/sciences-cs-fragments-20261007`.
- Branche de relecture globale : `claude/review-medina-global-20261007`, préparée avec le contenu de référence et les consignes publiées.
- Ancienne branche I48 : `claude/review-i48-esc2024-20261007` ; sa mission reste une sous-tâche de l'audit global.

Les états « publié », « relu », « corrigé », « testé techniquement » et « vérifié médicalement » restent distincts. Une rédaction révisée ne certifie pas la complétude CIM-11.
