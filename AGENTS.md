# Collaboration MEDINA

## Répartition des 21 fragments restants — 8 octobre 2026

Lire [FRAGMENTS_RESTANTS.md](docs/collaboration/FRAGMENTS_RESTANTS.md) et [production_plan.json](organisation/production_plan.json) : **11 fragments entiers Claude, 10 fragments entiers Codex**, hors cardiologie. Toutes les catégories restent regroupées sous leur fragment. Chaque catégorie ou chapitre cité porte **code — intitulé (libellé complet du fragment)**, par exemple **J45 — Asthme (P-02-Pneumologie)**. Un seul fragment et **un seul chapitre actifs par agent**, un chapitre par remise ; terminer, relire, contrôler, intégrer et publier ce chapitre avant le suivant. Un blocage ne libère pas le chapitre. Les files respectent les rangs du registre ; la priorité cardiologie en cours et ses missions restent conservées. Aucun fragment n’est déclaré complet par cette attribution. Cette règle de progression prime sur les anciennes consignes de production par lots ou cycles pour les travaux nouveaux.

La session Codex actuelle prend le relais de GPT « work » comme coordinateur prioritaire ; conserver les travaux et commits antérieurs. **Mode multi-agent obligatoire** : Claude et Codex progressent en parallèle, avec plusieurs sous-agents spécialisés dans le seul chapitre actif de chacun et un auteur par fichier. **Claude audite Codex, Codex audite Claude avant injection** ; corriger les réserves bloquantes puis reconstruire et vérifier après injection. La mission précise de Claude est [CLAUDE_FRAGMENTS_CAHIER_DES_CHARGES.md](docs/collaboration/CLAUDE_FRAGMENTS_CAHIER_DES_CHARGES.md).


Vial autorise en permanence les publications et intégrations GitHub du projet. Lire `CLAUDE.md`, `docs/collaboration/README.md` et les instructions actuelles avant de modifier le contenu.

## Nomenclature et livraisons — exigence du 7 octobre 2026

Toute leçon doit être nommée **code CIM + intitulé complet**, y compris dans les liens, rapports et navigations. Tout fragment doit porter **initiale de la spécialité - rang de production à deux chiffres - nom littéral**, par exemple `C-01-Cardiologie`. Le registre partagé est `organisation/fragments.json` ; les identifiants techniques S01…T7 et les routes restent stables.

Consulter `organisation/MEDINA_Organisation.html` et `docs/collaboration/DELIVERY_PROTOCOL.md`. Remettre les sources sous `livraisons/Livraison Codex/<libellé>/` ; Claude dépose ses corrections sous `livraisons/Livraison Claude/<libellé>/`. Relire et vérifier l'injection dans les sources canoniques avant reconstruction et publication. Ne jamais déclarer un fragment achevé sur la seule présence d'un cours ou d'un regroupement `covers` : l'objectif de complétude porte sur la CIM-11, dont l'inventaire validé manque encore.

## À chaque reprise et avant une livraison

1. Vérifier les têtes GitHub de `main`, de la branche d'intégration et de **toutes les branches et PR**, avec leurs pages suivantes. Le clone local et la seule branche `claude/review-…` ne constituent pas un inventaire distant.
2. Exécuter `python3 tools/collaboration_sync.py --out docs/collaboration`. Si l'accès shell GitHub est bloqué, collecter les mêmes données par le connecteur puis utiliser `--snapshot <fichier.json>`. Lire `DELIVERIES_LATEST.md` et les contributions en attente avant de commencer un nouveau lot.
3. Accepter aussi les anciens rapports à plat, branches sans PR et patchs remis. Un manifeste ou un nouvel emplacement facilite le suivi ; son absence ne justifie pas d'ignorer une livraison.
4. Ouvrir rapport et diff ; enregistrer la réception. Rattacher chaque modification à ses sources et aux fragments réellement consommateurs. Reconstruire les HTML ; modifier uniquement une sortie générée ne constitue pas une intégration.
5. Conserver les commits et rapports du contributeur. Documenter les adaptations, conflits et réserves. Ne pas déplacer sa branche pour la remettre artificiellement au niveau de la nôtre.
6. Après contrôle, publier le commit d'intégration et un reçu sous `docs/collaboration/receipts/`, puis actualiser l'index et `HANDOFF_LATEST.md`. Citer le SHA exact, les chemins, les contrôles exécutés et les réserves. Vérifier la disponibilité distante avant d'annoncer le résultat.

« Repéré », « reçu », « intégré » et « contrôlé techniquement » désignent des preuves différentes. La fusion d'une relecture ciblée ne certifie ni les 30 cours ni la complétude CIM-11. Une branche publiée ne prouve pas que le site utilisant `main` a été reconstruit : vérifier séparément le déploiement.

## Mécanismes — nouvelle priorité

Chaque affirmation médicale doit comporter une justification causale ou clinique précise, ses limites et sa source. Préférer les mots cliquables et fenêtres contextualisées. Cette règle couvre les quatre onglets et tous les contenus associés. Priorité actuelle : les 20 cours présents du Fragment 01 sont répartis 10 Codex / 10 Claude, dans `docs/collaboration/MECHANISMS_PLAN.json` ; consigne opérationnelle `MECHANISMS_CLAUDE.md`. Ne jamais confondre enrichissement ciblé et relecture exhaustive. J40 — Bronchite est ajouté comme production distincte couvrant J20/J40/J41/J42. La complétude CIM-11 reste à établir.
