# Lot I89-2 — I89 — Autres atteintes non infectieuses des vaisseaux et des ganglions lymphatiques (C-01-Cardiologie)

## Objet

Ce lot remplace `2026-10-08-I89` (tête `44bf7d4`, reçu par Codex en `1c39691`, non intégré). Il lève les trois réserves bloquantes de la [réception Codex](../../../../../docs/collaboration/reviews/2026-10-08/PR12_7775E6E_I89/RECEPTION.md) et corrige la mention erronée de la prégabaline dans le manifeste. Base : `main` `1c39691289c49cb701345026b5ab9334f5330225`, sans changement des chemins I89 depuis `918ef69`. Le reste du cours est identique au [rapport v1](../2026-10-08-I89/rapport.md), qui donne le périmètre, les catégories et les vérifications initiales.

Un sous-agent dédié a fait la correction. La consigne était minimale : retirer ou qualifier, sans affirmation nouvelle non sourcée. Son rapport détaillé, avec avant, après et source pour chaque passage, se trouve dans `CORRECTIONS_AUDIT_CODEX.md`.

## Réserves levées

| Réserve Codex | Correction | Source et accès |
| --- | --- | --- |
| 1. Doses d'octréotide hors indication dans le chylothorax | **Toutes les posologies sont retirées** de l'îlot p-4, du tableau des posologies, des encadrés, de la fenêtre `i89-d-octreotide` et du Pareto. Le texte dit désormais : « usage hors indication, aucun consensus, dose et durée fixées par le protocole du centre spécialisé ». Les indications, risques et interactions sont attribués à l'information professionnelle américaine. Plus aucune dose ni durée d'arrêt ne subsiste. | Information professionnelle américaine (DailyMed), déjà citée |
| 2. Vert d'indocyanine (Verdye) en Suisse | L'information professionnelle suisse est **inaccessible** : swissmedicinfo.ch renvoie une page vide et compendium.ch exige une connexion (consultation du 08.10.2026). La juridiction est donc **limitée explicitement partout**. Le SwissPAR du 29.06.2023 est cité au passé (autorisation du 24.04.2023, indications cardiocirculatoires, hépatiques et ophtalmologiques). L'iodure, les contre-indications thyroïdiennes, le délai avant un test à l'iode radioactif et l'interdiction de réinjection sont attribués à l'information australienne. L'érysipèle est attribué à l'AWMF 2017. Une phrase précise que le statut et la disponibilité suisses actuels se vérifient dans l'information professionnelle suisse en vigueur. | SwissPAR 2023 lu ; avis Swissmedic du 10.07.2023 lu, non repris |
| 3a. Myxœdème et glycosaminoglycanes | « Prend peu le godet » devient « ne garde habituellement pas le godet » ; « corrige cet œdème » devient « traite la cause ». | Safer 2011 (PubMed 22110782), texte intégral |
| 3b. Territoires du conduit lymphatique droit | « Plus court » est retiré ; la phrase précise « selon le schéma anatomique habituel ». | Kammerer 2016 (PubMed 27037010), texte intégral |
| 3c. Rôle valvulaire de FOXC2 et PIEZO1 | Le texte précise que la preuve vient de la souris. | Petrova 2004 (PubMed 15322537) ; Nonomura 2018 (PubMed 30482854), résumés |
| 3d. Rétention sodée sous anti-inflammatoires non stéroïdiens, corticoïdes et minoxidil | Chaque mécanisme est attribué à sa source. | Kim et Joo 2007 (PubMed 24459510) ; Cohn 2011 (PubMed 21896152) ; Liu 2013 (PubMed 23947590) |
| 3e. Pénicilline, protéines liant la pénicilline et peptidoglycane | La source est citée. | Kong 2010 (PubMed 20041868), texte intégral |
| Manifeste : prégabaline | **Mention corrigée** : le cours ne propose aucune dose de prégabaline. L'œdème périphérique fréquent est attribué à l'information EMA de Lyrica. | — |

## Contrôles (base `main` `1c39691`, sorties hors dépôt)

| Contrôle | Résultat |
| --- | --- |
| `verifier_sigles.py I89` | `{}` |
| `test_v7.py --static I89` | OK — 36 713 mots, 43 fenêtres, 8 quiz, 5 Pareto |
| `build_front.py`, `--all-fragments`, `tests/audit_fragments.py` | 22 fragments, JavaScript valide, build reproductible |
| `tests/verify_course_native.cjs I89` (1 360 et 390 px) | 2 595 contrôles, 0 échec |
| `tests/verify_s01_browser.cjs` (22 cours) | 73 réussis |
| `test_v7.py I89` | OK |
| `python3 -m unittest discover -s tests` | 118 tests OK |

## Réserves restantes

- **Verdye** : l'information professionnelle suisse en vigueur et la disponibilité en 2026 ne sont pas vérifiées. L'information australienne n'a pas été relue dans ce lot.
- **Portée de deux sources** :
  - Cohn 2011 énonce le mécanisme rénal pour l'hydralazine ; le cours l'applique au minoxidil, rangé dans la même classe des vasodilatateurs directs par cette revue.
  - Liu 2013 parle de rétention d'eau par effet minéralocorticoïde.
- **Inchangées depuis la v1** : divergence ISL/AWMF sur le diagnostic précoce, seuils des signaux d'alarme, nomenclature A46/B74/I88/R59, volume.
- **Couverture** : CIM-11 non établie ; I88 non couverte.
