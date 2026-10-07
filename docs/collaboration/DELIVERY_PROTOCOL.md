# MEDINA — publier, recevoir et intégrer une livraison

Le propriétaire autorise de manière permanente les publications et contributions GitHub nécessaires à MEDINA. Claude Code a déjà publié des commits et des pull requests sur ce dépôt ; son accès en écriture est donc établi pour ces contributions. Chaque agent conserve sa connexion et sa branche. Aucun identifiant ni jeton n'est transféré entre les agents.

## Accès communs

- [Sources de MEDINA](https://github.com/vialdjoukang-spec/Medina).
- [Livraison Codex](https://github.com/vialdjoukang-spec/Medina/tree/main/livraisons/Livraison%20Codex).
- [Livraison Claude](https://github.com/vialdjoukang-spec/Medina/tree/main/livraisons/Livraison%20Claude).
- [Organisation dans le dépôt](../../organisation/MEDINA_Organisation.html) et [tableau de bord publié](https://vialdjoukang-spec.github.io/Medina/organisation.html).
- [Passation actuelle](HANDOFF_LATEST.md), [inventaire des livraisons](DELIVERIES_LATEST.md) et [reçus d'intégration](receipts/).

Toutes les sources publiques sont consultables par les deux agents. Les dossiers organisent les remises ; ils ne constituent ni une restriction d'accès ni un verrou. Les protections GitHub et les contrôles du projet restent applicables.

## Préparer un lot

Pour les nouveaux travaux, appliquer [FRAGMENTS_RESTANTS.md](FRAGMENTS_RESTANTS.md) : un chapitre actif par agent et un chapitre par lot, rapport et PR. Le chapitre doit être relu, contrôlé, intégré et publié avant le suivant. La répartition 11 Claude / 10 Codex des fragments restants remplace les rôles généraux de production/relecture ; les lots historiques et la mission cardiologie sont conservés.

Chaque agent ouvre sa branche depuis la version actuelle de la branche d'intégration `codex/sciences-cs-fragments-20261007`. Il identifie le commit de départ, les fichiers concernés et le travail attendu. Une relecture conserve aussi le commit du contenu effectivement examiné.

Chaque fragment possède un dossier sous `livraisons/Livraison Codex/<nom-du-fragment>/` et sous `livraisons/Livraison Claude/<nom-du-fragment>/`. Le nom exact provient du champ `label` d'`organisation/fragments.json`. Le dossier Codex contient `livraison.json` et la copie intégrale des HTML et JSON des cours sous `sources/chapters/<CODE>/`. Les fichiers communs restent accessibles par les liens de son README.

Avant une première contribution, le dossier Claude contient seulement un README et `livraison.template.json`. La préparation explicite d'une copie de travail ajoute les sources et `livraison.json` ; elle ne déclare aucune correction livrée. Les rapports de lots successifs peuvent être conservés dans des sous-dossiers datés. Les rapports historiques restent à leur emplacement original.

Le manifeste permet d'identifier le contenu sans ouvrir chaque fichier.

| Donnée | Contenu attendu |
| --- | --- |
| Livraison | Identifiant du lot, agent, date, branche et commit de départ. |
| Cours | Code et titre exacts pour chaque cours concerné ; référentiel du code indiqué. |
| Fragment | Identifiant et nom affiché, issus d'`organisation/fragments.json`. |
| Périmètre | Fichiers et sections traités, chemins des rapports et limites de couverture. |
| Empreintes | Pour chaque fichier, `target_path`, `source_path` et `sha256` de la source originale. Cette empreinte reste inchangée après correction du fichier copié. |
| Vérification | Commandes réellement exécutées, résultats et réserves non résolues. |
| Remise | Commit livré et lien de PR, consignés dans le reçu après publication. |

Les 22 noms de fragments proviennent d'`organisation/fragments.json`. Un intitulé de cours demeure associé à son code ; un numéro de fragment seul ne suffit pas à décrire une livraison. Une correction linguistique, un ajout de cours et une modification technique sont distingués.

## Commandes de remise

```bash
# Exporter les sources actuelles, en donnant leur commit de référence réel.
python3 tools/livraison.py export-codex --fragment ALL --source-commit <SHA-complet>
# Préparer explicitement une copie de travail pour Claude.
python3 tools/livraison.py prepare-claude --fragment S01
# Après correction des fichiers copiés et rédaction du rapport :
python3 tools/livraison.py check-claude "livraisons/Livraison Claude/C-01-Cardiologie"
python3 tools/livraison.py apply-claude "livraisons/Livraison Claude/C-01-Cardiologie"
```

L'export est reproductible et préserve une copie de source modifiée depuis le dernier export. Le contrôle Claude refuse les chemins hors périmètre, les liens symboliques, les sources absentes, les empreintes originales périmées et les copies sans correction. Les modifications d'un fragment doivent cibler ses propres cours.

L'injection examine tous les fichiers avant d'écrire dans les dossiers canoniques. Elle crée un nouveau reçu portant l'état **« injecté, reconstruction/contrôles à faire »**. Les corrections de glossaire, d'interface, de CS et les créations de nouveaux cours sont remises directement par branche et PR ; cet outil d'injection se limite aux HTML et JSON primaires des cours déjà intégrés.

Pour ajouter un fichier à un cours déjà intégré et annoncé dans le manifeste, utiliser une entrée `files` avec `operation: "add"`, `sha256: null` et `proposed_sha256` obligatoire, en conservant `source_path: "sources/" + target_path`. La cible doit être un fichier `.html` ou `.json` nommé `<CODE>_…`, directement sous `chapters/<CODE>/` du fragment déclaré, et ne pas exister. L'injection revérifie l'absence, crée le fichier atomiquement en mode `0644` et refuse toute collision ; un échec retire uniquement l'ajout créé par ce lot et restaure ses remplacements. Chaque banque `<CODE>_justifications.json` présente dans un cours touché est compilée après l'injection de tous les fichiers et avant le reçu, y compris si seuls ses HTML changent ; une compilation échouée déclenche le retour arrière. `check-claude` contrôle seulement les chemins, les empreintes, l'UTF-8 et la syntaxe JSON. Un remplacement conserve l'empreinte originale obligatoire ; `operation: "replace"` est facultatif et ne peut masquer un ajout.

## Audit croisé et injection — priorité du 8 octobre 2026

Claude et Codex travaillent en mode multi-agent, chacun sur un seul chapitre actif. Le cahier des charges de Claude est [CLAUDE_FRAGMENTS_CAHIER_DES_CHARGES.md](CLAUDE_FRAGMENTS_CAHIER_DES_CHARGES.md). Claude audite les sources proposées par Codex ; Codex audite celles proposées par Claude. Chaque audit indépendant porte sur le commit exact à injecter et les quatre onglets, leurs fenêtres, les sources, le glossaire et les contrôles. Corriger les réserves bloquantes et refaire l’audit concerné **avant injection**. Les contrôles et la reconstruction après injection confirment la version intégrée ; ils ne remplacent pas l’audit préalable. Une livraison historique est reprise suivant ces étapes sans effacer ses preuves.

## Publier et recevoir

1. L'auteur termine son lot et les contrôles adaptés, puis pousse ses sources et son dossier de remise. Il ouvre une PR vers la branche d'intégration et donne le commit exact. Il annonce le travail après le push.
2. L'agent chargé de l'intégration consulte toutes les branches et PR récentes, ouvre les rapports et relève les fichiers réellement modifiés. Un rapport reste recevable même s'il est placé hors du nouveau dossier de remise.
3. Il vérifie les différences, les sources médicales citées et les conflits. Il applique les changements aux sources canoniques, puis reconstruit MEDINA et les fragments concernés. Une copie de rapport ou de fichier HTML ne remplace pas cette intégration.
4. Il exécute les audits et les contrôles navigateur appropriés. Une réserve médicale conserve son état explicite ; une réussite technique ne la résout pas.
5. Il consigne un reçu dans `docs/collaboration/receipts/` : lot, commit reçu, fichiers intégrés, fragments concernés, commit d'intégration, contrôles, réserves et décision. Il actualise l'inventaire, la passation et le tableau de bord.
6. La publication depuis `main` intervient après intégration et vérification. Le déploiement Pages est contrôlé séparément. Le tableau distingue une contribution disponible sur une branche d'une modification effectivement publiée dans les cours.

Les états « livré », « reçu », « intégré », « contrôlé » et « publié » décrivent des étapes différentes. La publication du tableau de bord doit reprendre les contributions les plus récentes et leurs vrais états, sans annoncer comme intégré un lot en attente.

## Lots antérieurs et absence de manifeste

Une ancienne livraison sans manifeste reste examinée. Le responsable de réception reconstitue son périmètre à partir des commits, fichiers, rapports et PR ; il conserve les preuves originales et ajoute un reçu de rapprochement. Il ne refuse pas un travail parce que sa remise précède ce protocole.

Une session sans accès GitHub en écriture peut remettre un rapport et un patch. Après avoir ajouté et committé les nouveaux fichiers, `git format-patch` permet de les inclure dans la remise. Le responsable de réception vérifie l'application et publie la contribution sur une branche identifiée.

## Couverture et complétude

Le rapport et le tableau indiquent les sections réellement relues. La correction d'un extrait ne certifie pas le cours entier. Les codes actuels du catalogue proviennent de la CIM-10-GM 2024 ; ils ne démontrent pas une couverture CIM-11. Aucun système n'est déclaré complet sans l'inventaire et les preuves prévus par [la règle CIM-11](../COMPLETUDE_CIM11.md).
