## INSTRUCTION PRINCIPALE — Claude Leader, 8 octobre 2026

Consigne directe de Vial, prioritaire sur toutes les sections ci-dessous qui lui sont contraires : **Claude est Leader du projet.** Lire [LEADERSHIP_CLAUDE_2026-10-08.md](docs/collaboration/LEADERSHIP_CLAUDE_2026-10-08.md). Claude rédige ses cours dans un français très agréable et captivant ; un **second agent distinct** les relit, renforce les points faibles et **injecte directement** (« Auto-audit par Agent différé opus 5.5 ») ; **Codex audite ensuite le fichier final injecté**. Claude améliore systématiquement les cours Codex reçus, sauf s’ils sont captivants et corrects sur le fond. Après ses onze fragments, Claude peut entamer les fragments Codex en ordre inverse de création (M-21 vers I-03). Une erreur médicale démontrée reste prioritaire.

Règles universelles ajoutées : **l’efficacité prime sur le volume** — information efficace, puissante, extrêmement didactique, claire, en termes médicaux dédiés, sans remplissage ni perte d’information utile ; **deux captures d’écran réelles par leçon** (ouverture de la leçon et fenêtre explicative ouverte, `tools/capture_lecon.py`), présentées dans le **panneau latéral**, non dans le fil du chat. Voir les sections 7 et 8 du même document.
Règle universelle de langue : un français **merveilleux à lire, riche, professionnel et esthétique, sans excès** (section 9). File de production Claude : `organisation/FILE_FRAGMENTS_CLAUDE.json`, un fragment à la fois, leçon par leçon (section 10).

> **Protocole remplacé pour les travaux nouveaux, 8 octobre 2026.** Lire [le protocole par fragment](PROTOCOLE_FRAGMENTS_2026-10-08.md) et [COORDINATION.md](../../COORDINATION.md). Fragment entier achevé et auto-revu avant audit croisé unique ; l’autre IA corrige puis injecte, INJECTÉ immuable, HTML clair. Les dispositions incompatibles ci-dessous sont conservées comme historique et ne donnent plus d’ordre d’action. Aucun chapitre isolé ne constitue une remise finale.

# MEDINA — collaboration Codex et Claude

Ce dossier est le point d'entrée permanent pour consulter les livraisons, reprendre une mission et remettre une contribution.

**Dernière consigne : STOP Codex avant changement des règles.** [Décision du 8 octobre](ARRET_CODEX_2026-10-08.md) : I83 v6 déjà injecté et publié ; I89, J45 et A41 non injectables. Production et veille automatique Codex en pause ; aucune relance avant les nouvelles instructions.

- [État des lieux étendu du 8 octobre, tableaux et jauges vérifiables](ETAT_DES_LIEUX_2026-10-08.md) et [dashboard interactif autonome](ETAT_DES_LIEUX_2026-10-08.html).
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

## Injection Claude et audit Codex

Appliquer [REGLES_INJECTION_CLAUDE.md](REGLES_INJECTION_CLAUDE.md). Claude injecte ses propres chapitres après revue interne et contrôles prescrits, sans réserve bloquante Codex ouverte ; Codex audite ensuite [la file ordonnée](FILE_AUDIT_CODEX.json). Le tableau de bord indique « en audit croisé » tant que cet audit n’est pas favorable. Une remise archivée est distincte d’une injection. Les chapitres Codex conservent leur contrelecture Claude préalable.
