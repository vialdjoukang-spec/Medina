# Plan de progression lente de la tétrade — instruction de Vial, 11 octobre 2026

Vial demande un plan détaillé de 30 cycles, livré en PDF et en HTML à cases à cocher, et publié dans GitHub MEDINA. Chaque cycle prévoit quatre chapitres : un de Neurologie, un d’Endocrinologie et métabolisme, un de Néphrologie et un d’Hématologie. Ces quatre systèmes sont confirmés par la pièce jointe fournie par Vial pendant la préparation.

La chaîne demandée est : **un chapitre par agent → audit par binôme croisé → contre-audit par agents différés → contrôle par Codex, coordinateur → injection d’un chapitre à la fois**. Le cycle contient quatre injections successives. Les deux passes du Prompt sont maintenues dans chaque niveau d’audit. Une barrière rouge pleine de **0,5 cm** sépare les cycles ; elle ne peut être franchie sans clôture, preuves de passage et respect du Prompt de vérité.

Cette consigne remplace, pour les travaux futurs de cette tétrade, les instructions incompatibles de production par fragment entier, d’interdiction d’audit croisé ou d’injection avant contrôle final. Elle ne modifie pas les travaux et preuves historiques. Les sources, le contexte suisse, le plan monographique, les quatre onglets, les contrôles, la double passe et la distinction entre revue IA et validation médicale humaine restent obligatoires.

## Livrables et limites

- [HTML interactif](https://vialdjoukang-spec.github.io/Medina/progression/plan-tetrade-30-cycles.html).
- [PDF](https://vialdjoukang-spec.github.io/Medina/progression/plan-tetrade-30-cycles.pdf).
- [Attributions](../../../organisation/plan_tetrade_30_cycles.json) et [données enrichies](../../../organisation/progression/plan-tetrade-30-cycles.json).
- [Générateur](../../../tools/build_tetrade_plan.py) et [modèle](../../../organisation/tetrade_plan_template.html).

Le plan contient **120 missions sur 120 catégories actuellement sans cours intégré**, avec **deux brouillons Claude existants à reprendre** (E11 et D50), et inventorie les **270 catégories CIM-10-GM 2024 OFS** des quatre systèmes. Les sous-codes sont dans le périmètre de leur chapitre ; tout regroupement futur exigera une couverture démontrée. Cette planification ne certifie aucune complétude CIM-11 ou médicale.

Les agents C01-R-NEUR, C01-R-ENDO, C01-R-NEPH, C01-R-HEM, puis leurs homologues jusqu’à C30, sont des **missions prévues, non lancées**. Deux binômes échangent les chapitres : NEUR ↔ HEM et ENDO ↔ NEPH. Les agents Cxx-CA-* sont nouveaux, sans participation à la production ou à l’audit initial. Ils interviennent seulement après correction et clôture des audits croisés. Au plus quatre agents de travail sont actifs simultanément, plus le coordinateur.

Le HTML garde le suivi dans le navigateur et propose export/import JSON. Ses cases déclarent un état de suivi ; elles n’effectuent aucun audit, commit ni injection. Les preuves réelles et l’autorisation de passage restent contrôlées par le coordinateur. Les cycles futurs sont consultables mais leurs cases restent verrouillées selon les dépendances du plan.

## Préalable technique au cycle 1

`organisation/production_plan.json`, `tools/production_plan.py`, `tools/espace.py` et leurs tests continuent d’appliquer des protocoles historiques. Ils ne sont pas réécrits par la livraison de ce plan. **Avant toute injection médicale selon les nouveaux cycles, il faut les mettre en cohérence, documenter et tester les nouvelles gardes**. Aucun refus ne doit être contourné par désactivation d’une garde. La présente demande porte sur le plan ; aucun chapitre médical n’est produit ou injecté par sa publication.

## Présentation imposée

La police du plan et du PDF est **Atkinson Hyperlegible Next**, la police de référence des cours, embarquée. **Le bleu est interdit dans le plan.** La palette utilise vert, rouge, orange foncé et blanc, avec contrastes contrôlés. Les futurs cours Codex auront un corps bleu contrasté, des caractères bien visibles et jamais noirs, ainsi que des termes cliquables orange foncé. Cette dernière règle sera vérifiée lors de leur production ; elle ne recolore pas les cours existants dans la livraison du plan.

Inventaire initial : `main` **11c874ef6cea5049cbf4a837a6993c132850fddd**. Les brouillons E11 et D50 de Livraison Claude sont repérés et conservés ; les familles de sources indiquées sont à rechercher et à lire lors de chaque mission. La création d’un plan n’établit pas qu’un futur texte primaire a déjà été lu.
