# MEDINA — dossiers de livraison

Les deux agents partagent toutes les sources du dépôt. Ces dossiers rendent leurs contributions faciles à retrouver et à intégrer.

| Dossier | Contenu |
| --- | --- |
| [Livraison Codex](https://github.com/vialdjoukang-spec/Medina/tree/main/livraisons/Livraison%20Codex) | Lots de création, d'intégration et de contrôle publiés par Codex. |
| [Livraison Claude](https://github.com/vialdjoukang-spec/Medina/tree/main/livraisons/Livraison%20Claude) | Lots de relecture, corrections, rapports et journaux publiés par Claude. |

Chaque dossier possède 22 sous-dossiers de fragments, nommés d'après `organisation/fragments.json`. Les remises identifient les **codes et titres des cours**, les **identifiants et noms des fragments**, les fichiers concernés, le commit de départ, les contrôles et les réserves. Les rapports successifs peuvent être conservés dans des sous-dossiers datés.

Codex publie les sources complètes sous `<nom-du-fragment>/sources/chapters/`, avec le manifeste `livraison.json`. Chaque dossier Claude reçoit un README et un modèle vide. Une copie de travail préparée explicitement reste distincte d'une livraison corrigée.

Les sources restent dans leurs dossiers canoniques. L'auteur pousse sa branche et ouvre une pull request ; le responsable de réception vérifie, intègre, reconstruit et contrôle avant la publication des cours. L'autorisation permanente du propriétaire dispense de redemander son accord pour les publications courantes de MEDINA.

- [Protocole commun](../docs/collaboration/DELIVERY_PROTOCOL.md).
- [Organisation de MEDINA](../organisation/MEDINA_Organisation.html) et [tableau de bord publié](https://vialdjoukang-spec.github.io/Medina/organisation.html).
- [Dernière passation](../docs/collaboration/HANDOFF_LATEST.md), [inventaire](../docs/collaboration/DELIVERIES_LATEST.md) et [reçus](../docs/collaboration/receipts/).

Les anciens rapports et lots sans manifeste restent recevables. Leur périmètre est rapproché des commits et documenté dans un reçu. Les états de livraison, d'intégration et de publication restent distincts ; une contribution partielle ne certifie ni un cours entier ni la complétude CIM-11 d'un système.

L'outil `tools/livraison.py` exporte les paquets, prépare une copie Claude sur demande explicite, contrôle les empreintes et peut injecter les fichiers corrigés dans les sources canoniques. La reconstruction et les contrôles du projet restent une étape séparée. Les [commandes et conditions d'intégration](../docs/collaboration/DELIVERY_PROTOCOL.md) figurent dans le protocole commun.
