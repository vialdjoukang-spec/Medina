# Remettre une relecture MEDINA

Les rapports de Claude et des autres relecteurs sont déposés dans ce dossier. Ils décrivent uniquement les fichiers et passages effectivement examinés.

Les rapports déjà publiés à plat restent valides et sont conservés. Le nouvel emplacement et `journal.json` servent aux prochains lots ; leur absence ne bloque pas la réception d'une ancienne livraison. Avant toute conclusion sur les travaux disponibles, lire [l'inventaire commun](../DELIVERIES_LATEST.md), puis ouvrir toutes les contributions en attente. Codex consigne son accusé dans [les reçus](../receipts/).

Pour chaque lot, utiliser `reviews/<date>/<CODE>/rapport.md` et `reviews/<date>/<CODE>/journal.json`. Employer `CS` pour la sémiologie et `GLOBAL` pour une synthèse transversale. Les chemins sont relatifs à `docs/collaboration/`.

Le rapport suit le [modèle commun](../REVIEW_TEMPLATE.md). Le journal donne pour chaque fichier : chemin, commit relu, sections ou fenêtres examinées, état et réserves. États : `non_lu`, `relu_sans_modification`, `corrige_propose`, `corrige_et_controle`, `reserve_non_resolue`. Un passage lu ne suffit pas à déclarer le fichier entier relu.

## Avec un accès GitHub en écriture

1. Lire la [dernière passation](../HANDOFF_LATEST.md) et les instructions actuelles. Travailler sur `claude/review-medina-global-20261007` ou une branche de contribution clairement identifiée.
2. Ajouter corrections, rapport et journal dans des commits. Préciser le commit de contenu réellement relu et la source primaire de toute modification médicale.
3. Pousser la branche et ouvrir une pull request vers `codex/sciences-cs-fragments-20261007`, avec périmètre, réserves et contrôles exécutés.
4. Codex compare, contrôle et intègre ; le rapport est complété par le commit d'intégration et les résultats pertinents.

L'autorisation permanente du propriétaire dispense de redemander son accord pour cette publication. Le push et la PR dans le dépôt nécessitent une session GitHub authentifiée avec les droits applicables.

## Sans accès GitHub en écriture

Remettre le rapport, le journal et un patch à Vial ou à Codex. Pour inclure les nouveaux fichiers, les ajouter et les committer avant d'exporter :

```bash
git add <fichiers-corriges> docs/collaboration/reviews/<date>/<CODE>/
git commit -m "Relire MEDINA : <perimetre>"
git format-patch --binary --stdout <commit-de-depart>..HEAD > MEDINA_CLAUDE_REVIEW.patch
```

Remplacer les éléments entre chevrons par les chemins et le SHA réels. Exécuter cette exportation sur une branche ne contenant que la contribution ; le commit de départ est le parent de ses premiers changements. `git format-patch` inclut les rapports nouvellement ajoutés, contrairement à un simple diff de fichiers non suivis.

La remise fournit aussi le nom du patch, la branche, le SHA de départ et celui de fin. Codex examine le patch, vérifie son application et les conflits, puis exécute les contrôles adaptés. Les réserves et les contrôles non exécutés restent explicites.

Aucun statut d'achèvement, d'audit intégral ou de complétude CIM-11 n'est promu par la seule réception d'un rapport.
