# Collaboration MEDINA

Vial autorise en permanence les publications et intégrations GitHub du projet. Lire `CLAUDE.md`, `docs/collaboration/README.md` et les instructions actuelles avant de modifier le contenu.

## À chaque reprise et avant une livraison

1. Vérifier les têtes GitHub de `main`, de la branche d'intégration et de **toutes les branches et PR**, avec leurs pages suivantes. Le clone local et la seule branche `claude/review-…` ne constituent pas un inventaire distant.
2. Exécuter `python3 tools/collaboration_sync.py --out docs/collaboration`. Si l'accès shell GitHub est bloqué, collecter les mêmes données par le connecteur puis utiliser `--snapshot <fichier.json>`. Lire `DELIVERIES_LATEST.md` et les contributions en attente avant de commencer un nouveau lot.
3. Accepter aussi les anciens rapports à plat, branches sans PR et patchs remis. Un manifeste ou un nouvel emplacement facilite le suivi ; son absence ne justifie pas d'ignorer une livraison.
4. Ouvrir rapport et diff ; enregistrer la réception. Rattacher chaque modification à ses sources et aux fragments réellement consommateurs. Reconstruire les HTML ; modifier uniquement une sortie générée ne constitue pas une intégration.
5. Conserver les commits et rapports du contributeur. Documenter les adaptations, conflits et réserves. Ne pas déplacer sa branche pour la remettre artificiellement au niveau de la nôtre.
6. Après contrôle, publier le commit d'intégration et un reçu sous `docs/collaboration/receipts/`, puis actualiser l'index et `HANDOFF_LATEST.md`. Citer le SHA exact, les chemins, les contrôles exécutés et les réserves. Vérifier la disponibilité distante avant d'annoncer le résultat.

« Repéré », « reçu », « intégré » et « contrôlé techniquement » désignent des preuves différentes. La fusion d'une relecture ciblée ne certifie ni les 30 cours ni la complétude CIM-11. Une branche publiée ne prouve pas que le site utilisant `main` a été reconstruit : vérifier séparément le déploiement.
