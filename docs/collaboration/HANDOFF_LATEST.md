# MEDINA — dernière passation

Mise à jour : 7 octobre 2026. Compléments contrôlés publiés sur les deux branches d’intégration au commit `f9b654810619ac8206500ca23821eff9816002c1`. Les remises S01/S02 sont exportées depuis ce commit. Le [tableau commun](../../organisation/MEDINA_Organisation.html) et sa [version publiée](https://vialdjoukang-spec.github.io/Medina/organisation.html) réunissent les 22 fragments, les 265 blocs et les 1 636 catégories du catalogue historique. Les plateformes originales reprennent désormais cette organisation : catégories numérotées, chapitres ordonnés, codes discrets en haut à droite et couleurs lisibles.

## Priorité : expliquer pourquoi

La règle de Vial vaut pour chaque affirmation médicale et chaque décision, dans les quatre onglets et tous leurs contenus. Les ajouts ciblés de ce lot comprennent **204 fenêtres physiopathologiques sur 15 cours**, avec 205 cibles explicites, conséquences cliniques, limites et sources. Le bilan initial de I50 — Insuffisance cardiaque dispose notamment d’explications distinctes pour anémie, sodium et potassium. L’injection se fait au moment de la compilation, sans réécriture silencieuse des HTML canoniques.

**La relecture exhaustive de toutes les affirmations n’est pas terminée.** Le [suivi par cours](MECHANISMS_PLAN.json) garde les 30 cours de départ en `pending_exhaustive_review`. La priorité actuelle du Fragment 01 est répartie **10 cours présents Codex / 10 Claude**, puis deux nouvelles productions chacun ; [le partage actuel](FRAGMENT_01_PRIORITE.md) remplace le partage historique 15/15 ; la [mission Claude](MECHANISMS_CLAUDE.md) précise ses cours, la revue attendue et la remise. [Sa consigne commune reçue](MISSION_JUSTIFICATION_2026-10-07.md) est alignée sur ce partage ; sa proposition originale est archivée intacte.

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
| PR #12, lot 4 — I48 — Fibrillation et flutter auriculaires | Injecté et publié au commit `e856ed1` par une session concurrente ; huit sources, glossaire et onze arbitrages conservés. Les compléments de cette reprise ajoutent une fenêtre ESC 2026 (101 natives au total), harmonisent les deux pièges et gardent les adaptations médicales publiées. Voir [le rapport](../../audits/CLAUDE_LOT4_2026-10-07/RAPPORT.md). |
| PR #12, lot 5 — justification systématique de 14 cours de C-01-Cardiologie et correctif des rubriques Source d’I48 | **Livré, en attente d’injection.** Branche `claude/loving-shannon-spwrhc`, base `75505d8`. 132 sources dans `livraisons/Livraison Claude/C-01-Cardiologie/sources/` (`check-claude` conforme) et `glossary/q21.py` (TBX1). 2 236 compléments, 203 mots verts, 42 fenêtres créées et 237 complétées, chaque cours relu par un vérificateur indépendant. I47, I49, I46, I71 et I80, transférés à Codex pendant le lot, sont livrés comme contribution recevable. [Rapport](../../livraisons/Livraison%20Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT5_JUSTIFICATION/rapport.md). |

Les [reçus](receipts/) distinguent réception, injection, vérification et commit publié. Les corrections de causalité et de figures J44/J18 et les harmonisations I50 de la reprise sont jointes. Les réserves non couvertes par la contrelecture ciblée restent ouvertes. Une relecture de prose ne certifie pas tout le cours.

## Dossiers et accès permanents

Le dépôt entier est partagé par GitHub. Après publication, les 22 dossiers [Livraison Codex](../../livraisons/Livraison%20Codex/) contiennent les sources complètes, banques incluses, et un manifeste portant le commit réel de la remise. Déposer les corrections sous [Livraison Claude](../../livraisons/Livraison%20Claude/) sur sa branche, conformément au [protocole](DELIVERY_PROTOCOL.md). Codex examine les différences, contrôle les empreintes puis injecte dans les fichiers canoniques avant reconstruction. L’autorisation permanente de Vial couvre ces contributions et publications ; elle ne remplace pas la connexion GitHub effective et ne justifie aucun transfert de secrets.

## Contrôles et limites

Les rapports de ce lot se trouvent dans [audits/MECANISMES_2026-10-07](../../audits/MECANISMES_2026-10-07/). Ils distinguent les fenêtres ciblées compilées, les vérifications navigateur et les contrelectures médicales partielles. Le workspace a été restauré à une ancienne version durant le lot : certaines banques ont été régénérées, puis les contrôles ont été refaits. Les résultats perdus ne sont pas présentés comme validation des fichiers nouveaux.

Le catalogue reste **CIM-10-GM 2024**. La complétude **CIM-11 n’est pas établie** : ne déclarer aucun système achevé sans inventaire validé de toutes les catégories et sous-catégories demandées. **Le Fragment 01 n’est pas achevé** : vingt cours présents, quatre productions prioritaires et périmètre complémentaire à vérifier avant de passer au Fragment 02. PR #6 accueil/QCM reste une branche distincte à traiter séparément.

À chaque reprise et avant publication, lire [les livraisons repérées](DELIVERIES_LATEST.md), les branches/PR et leurs nouvelles pages, les dossiers Claude et les reçus. La présence d’un manifeste facilite le suivi ; son absence ne justifie pas d’ignorer une livraison ancienne. Vérifier séparément le déploiement du site.

La préférence Anthropic Serif est enregistrée ; la police est absente de cette session. Les nouveautés ESC 2026 sont présentées dans des comparaisons dédiées I48/I50. Fenêtres : réponse directe puis mécanisme, conséquence, limites et source, sans quota de mots ni multiplication de volume.
