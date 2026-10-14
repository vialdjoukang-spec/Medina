# D64 — Autres anémies : rapport de l’auteur correcteur C02-R-HEM (Cycle 2)

**Identité** : C02-R-HEM, `claude-code/session_01NNsXRGeno3p5fi2QvuhRCM/C02-R-HEM`. **Date** : 14 octobre 2026. **Statut** : corrections auteur terminées ; passe 2 de C02-R-NEUR et contre-audit C02-CA-HEM à venir. Revue par intelligence artificielle ; aucune validation médicale humaine.

## Méthode
Relevé d’entrée (`entree.json`) avant toute modification : empreintes identiques à la passe 1. Les archives locales citées par Codex étant absentes du dépôt, les 25 sources ont été **relues en ligne le 14 octobre 2026** (FI Benadon, Exjade, Pegasys, Zyvoxid via AmiKo ; HUG 2013 ; LUKS ×6 ; CSCQ 2011 ; MQZH 2015 ; SSH smarter medicine 2023 ; Onkopedia mars 2026 ; BfArM CIM-10-GM 2024 ; Genes 2022 ; Roy-Babbs 2019 ; GFHC 2022 ; BSH/EHA 2022 ; Iolascon 2017 ; Cazzola 2011 ; Cells 2020 ; PAC6 ; Traxler-Weiss 2013). Textes intégraux conservés hors dépôt ; empreintes dans le registre.

## Réserves de la passe 1 (8/8 traitées par l’auteur, à revalider en passe 2)
- **R01** : 21 annonces remplacées par des entrées cliniques ; 35 mots coupés rétablis ; 30 infinitifs ou réponses nominales réécrits ; glossaire réécrit lettre par lettre.
- **R02** : Benadon 150 mg limité à la carence provoquée par un antagoniste de la pyridoxine (FI 25635).
- **R03** : monographies complètes Benadon, Exjade dispersible (critères d’introduction, règles de créatinine adulte et enfant), Pegasys hors indication (contre-indications complètes) ; encadré d’interactions dangereuses.
- **R04** : nouveau registre `source_ledger_claude.json` (44 affirmations) ; hypothermie → Genes 2022 ; linézolide → FI Zyvoxid 55558 ; KIF23 → Roy-Babbs 2019 ; Exjade → FI ; CSCQ daté octobre 2011.
- **R05** : encadrés `alert` (urgences, critères formels, interactions) ; statut IA visible.
- **R06** : CDA I ≥ 20 % d’érythroblastes anormaux (propre au type I) ; crise aplasique à parvovirus B19 ; fausse thrombocytose des petits automates.
- **R07** : calcul complet de la saturation de la transferrine avec références LUKS ; chaîne enzymatique de l’hème ; sigles de figures traduits.
- **R08** : tableau conditionnel discriminant en dix branches, complémentaire de la figure publiée.

## Corrections médicales majeures
Codage BfArM : l’anémie réfractaire avec sidéroblastes en couronne relève de D46.1 et non de D64 ; inclusions de D64.3, D64.4, D64.8. Critères MDS-SF3B1 selon OMS 2022 (Onkopedia 2026, SSH). Perte du fer érythroblastique dans la biopsie rattachée à sa source. VGM mesuré et hématocrite calculé (CSCQ).

## Enrichissements
Différentiel hiérarchisé gravité puis fréquence pour les SSP 147 (pâleur) et 165 (anémie) ; tableaux de gravité suisse et de gradation réticulocytaire ; valeurs normales des sidéroblastes ; fréquence MQZH ; options XLSA et SLC25A38 ; expositions D64.2 ; types II et III, splénectomie, EPO, acide folique ; quiz 4.

## Images
Six images authentiques CC BY 4.0 conservées, ouvertes et vérifiées (licence relue dans le XML Europe PMC) ; aucune remplacée. Légende et texte alternatif de la figure 1 corrigés ; style en ligne retiré ; identifiants du cahier portés par `data-evidence`. Manifeste : `preuves/images_claude.json`.

## Contrôles
`python3 test_v7.py --static D64` sur clone jetable : **OK** (32 689 mots, 64 fenêtres, 22 quiz, 21 Pareto). Aperçu isolé (`tools/night_preview.py`, hors dépôt) : 317 mots verts ouverts, 0 fiche absente, 0 erreur JavaScript, 6 images chargées, pas de débordement à 390 px.

## Réserves ouvertes
Passe 2 et contre-audit indépendants ; validation médicale humaine ; vérification ligne par ligne de `contexte_suisse_claude.json` ; captures du contrôle coordinateur.
