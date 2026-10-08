# I83 — Varices des membres inférieurs (C-01-Cardiologie) : contrôles après injection locale

**Tous les contrôles canoniques exécutés réussissent sur les sources exactes de Claude `6d5797c6a902e430cd9d3e9dd5159ec507a1476a`, reprises dans `/workspace/Medina`.**

Base avant injection : `e434eac491c14e8c348aeff606d113350df5026b`. Dix fichiers nouveaux (huit HTML, deux glossaires), seule entrée I83 ajoutée dans `chapters.json` ; source et empreintes dans `INJECTION_LOCALE_6D5797C.json`. Le test S01 est adapté de **20 à 21 cours**, correspondant au cours réellement ajouté ; aucune autre assertion modifiée.

| Contrôle réellement exécuté le 8 octobre 2026 | Résultat |
| --- | --- |
| Construction HTML global et fragment S01, sorties externes distinctes | Deux codes de sortie 0 |
| Tests unitaires du checkout canonique | 118 tests, tous réussis |
| Statique I83 |OK, 40 836 mots, 47 fenêtres, 6 quiz, 6 Pareto |
| Navigateur global, ordinateur 1300 × 900 / mobile 390 × 844 |OK, aucune erreur |
| Natif I83, ordinateur 1360 × 900 / mobile 390 × 844 | 1 923 assertions, 0 échec, 47/47 fenêtres dans chaque viewport |
| Catalogue/outils S01 après adaptation du compteur 21 | 72 contrôles, `passed`, zéro erreur JavaScript |
| Routes I83/I87, quatre cas ordinateur/mobile | 41 assertions, zéro erreur |

Les rapports JSON et journaux préfixés `6D5797C_` sont archivés ici. Les commandes exactes, répertoires, variables ciblées, horaires UTC et codes de sortie sont conservés dans `6D5797C_COMMANDES_CANONIQUES.json`.

**Transport HTTP local.** Les helpers externes convertissent les navigations `file://` ; les autres destinations HTTP(S) restent bloquées. Le dernier test historique S01 conserve le libellé `file://`, mais cette navigation a elle aussi utilisé HTTP local : ce rapport n’annonce pas une validation de portabilité directe `file://`. Aucune assertion de contenu ou d’interaction désactivée. Les formats mobiles sont des viewports Chromium, sans certification matérielle iOS/Safari.

Les unités et la suite S01 sont rejouées après la modification de leur fixture. L’audit/reproductibilité des 22 fragments et les 76 contrôles des catégories ont réussi sur 0974d85 ; registre, rattachements, glossaires et outils de compilation sont inchangés depuis. Ces résultats restent attribués à leur SHA ; la CI Pages exécutera le build des 22 fragments au commit publié.

Les sources canoniques correspondent octet pour octet au SHA Claude retenu ; les remarques médicales bloquantes sont fermées par les contrelectures documentées. Ces succès techniques ne certifient ni l’ensemble des pages primaires non téléchargées ni la complétude CIM-11.
