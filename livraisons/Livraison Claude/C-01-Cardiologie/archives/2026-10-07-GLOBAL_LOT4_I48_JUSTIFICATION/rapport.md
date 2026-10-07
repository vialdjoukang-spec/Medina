# Lot 4 — I48 — Fibrillation et flutter auriculaires : justification systématique

Date : 7 octobre 2026. Auteur : Claude. Fragment : C-01-Cardiologie (S01). Branche : `claude/loving-shannon-spwrhc`. Base : branche d’intégration `codex/sciences-cs-fragments-20261007`, commit `a6f18a150b1a67a2a53c14b3a7ec0b7fe6c6c74a`, où les lots 2 et 3 sont déjà injectés. Mission : `docs/collaboration/MECHANISMS_CLAUDE.md`, cours pilote.

## Résultat

Chaque affirmation relevée sans mécanisme porte désormais son pourquoi, soit dans le texte, soit dans une fenêtre ouverte par un mot vert.

| Élément | Nombre |
| --- | --- |
| Affirmations inventoriées sans mécanisme | 505, dans les 8 fichiers |
| Compléments intégrés au texte | 360 appliqués (198 acceptés tels quels, 162 corrigés), 2 rejetés |
| Mots verts ajoutés | 133 (132 ancres du plan et 1 ancre pour `i48-avk`) ; 12 ancres retirées, car elles se trouvaient dans la fenêtre visée |
| Fenêtres créées | 12 |
| Fenêtres existantes complétées | 41 |
| Fenêtres du cours | 88 → 100 |
| Corrections du cours actuel contre l'ESC 2024 | 12 passages |
| Volume du cours | 25 712 → 66 339 mots (texte principal 15 078 → 22 164, × 1,5 ; fenêtres 10 634 → 44 175, × 4,2) |

Les fenêtres créées sont : `i48-bilan`, `i48-brady-tachy`, `i48-cardiopathies`, `i48-causes-aigues`, `i48-cognition`, `i48-cycle-variable`, `i48-interactions`, `i48-k-torsades`, `i48-remod-inverse`, `i48-rs-embolie`, `i48-substrat`, `i48-troponine`. Le fichier [fenetres_types.html](fenetres_types.html) en montre trois.

**Volume.** Le cours a été multiplié par 2,6 ; le texte principal, par 1,5. Les fenêtres créées comptent environ 1 500 à 6 700 caractères ; les rubriques ajoutées, 900 à 5 100. Les brouillons de la session interrompue atteignaient 16 500 caractères ; ils ont été divisés par deux à quatre sans retirer de mécanisme. Le propriétaire doit dire si ce volume lui convient avant l'extension aux 14 autres cours.

## Rebasage sur les sources canoniques de Codex

Le lot avait été rédigé sur les copies du lot 2. Codex a ensuite injecté les lots 2 et 3 et appliqué onze arbitrages médicaux à I48 (`audits/MECANISMES_2026-10-07/CODEX_ARBITRAGES.json`). Le lot 4 a donc été refondu par une fusion à trois voies, avec pour base les copies du lot 2, d’un côté les sources canoniques de Codex et de l’autre le lot 4.

- Six arbitrages ont été repris mot pour mot : I48-02, I48-03, I48-04, I48-08, I48-10 et I48-11.
- Cinq passages avaient aussi été complétés par le lot 4 : I48-01 (sepsis), I48-05 (FA pré-excitée), I48-06 et I48-07 (CHAMPION-AF), I48-09 (anticoagulation après cardioversion). Le texte de Codex y est repris à l’identique, puis le mécanisme ou le mot vert du lot 4 y est ajouté.
- **CHAMPION-AF** : conformément à l’arbitrage de Codex, le texte ne mentionne plus d’excès d’AVC ischémiques (3,2 % contre 2,0 %). La fenêtre `i48-laao` explique désormais pourquoi la fermeture ne démontre aucune supériorité sur les AVC.
- **Sepsis** : le chiffre de 83 % de retour spontané en rythme sinusal en 48 heures est retiré, car cette donnée ne concerne pas spécifiquement le sepsis.
- Aucun texte « avant » d’un arbitrage ne subsiste dans les sources livrées.

## Méthode

1. **Inventaire** (session précédente) : 505 affirmations, plan par fichier et fusion en 53 fenêtres.
2. **Rédaction** : 27 brouillons existants rattachés à leur fenêtre par similarité du contenu ; 26 fenêtres rédigées.
3. **Vérification** : chaque fenêtre a été relue par un vérificateur médical sceptique. Les 26 fenêtres nouvelles ont reçu une **contre-vérification indépendante**, qui a encore corrigé des erreurs de fond. Les 362 compléments du texte ont été vérifiés un à un.
4. **Sources** : texte intégral de l'ESC 2024 sur la FA (Van Gelder et al., Eur Heart J 2024;45:3314-3414, doi:10.1093/eurheartj/ehae176), interrogé par recherche plein texte ; résumés PubMed des essais cités ; résumés européens des caractéristiques des produits (Brinavess, Multaq, Pradaxa et AOD).
5. **Application centrale** : `travail/lot4_I48_justification/appliquer_lot4.py`, d'abord à blanc (0 échec), puis en écriture. Les résultats bruts des agents sont conservés dans `travail/lot4_I48_justification/resultats/`.

## Erreurs du cours corrigées

| Passage | Avant | Après | Source |
| --- | --- | --- | --- |
| Symptômes (I48_a) | Absence de symptôme chez un patient sur trois environ | Environ un patient sur dix | ESC 2024, § 3.3 : 90 % décrivent des symptômes |
| FEVG 41–49 % (I48_b, I48_d) | « Au cas par cas, prudence pour la classe Ic » | Amiodarone ou dronédarone, classe Ic écartée | ESC 2024, figure 5 |
| Flécaïnide (I48_d) | Clairance < 35 mL/min : prudence | Ne pas utiliser | ESC 2024, tableau 13 |
| Amiodarone (I48_d, I48_pop4) | 600 puis 400 mg/jour (ESC 2020) | 200 mg × 3/jour pendant 4 semaines, puis 200 mg/jour ou moins | ESC 2024, tableau 12 |
| Métoprolol succinate (I48_d) | Maximum 400 mg/jour | Maximum 200 mg/jour | ESC 2024, tableau 12 |
| Classe Ic et freinateur (I48_c, I48_pop4) | Association « obligatoire », « toujours » | Association recommandée (classe IIa) | ESC 2024, tableau de recommandations 18 |
| Vernakalant (I48_b) | FEVG ≤ 40 % | FEVG ≤ 40 % ou insuffisance cardiaque NYHA III–IV | ESC 2024, tableau 13 |
| Troponine (I48_c) | « La cinétique tranche » entre types 1 et 2 | La cinétique signe une lésion aiguë ; le contexte distingue le type 1 du type 2 | Quatrième définition universelle de l'infarctus (Thygesen 2019) |
| Alcool (I48_a) | Arrêt de l'alcool | Trois verres standard par semaine au plus | ESC 2024, § 5.7 |
| Bêtabloquants et ICFEr (I48_pop4) | « Indispensables » | « Recommandés » ; le bénéfice en FA n'est pas établi | ESC 2024, § 7.1.3 |
| Surveillance après AVC (I48_c) | 72 heures attribuées à l'ESC 2024 | Attribution corrigée (ESC 2020) | ESC 2024, § 9.7 |
| Pharmacogénétique des antivitamines K (I48_c) | Haplotype VKORC1 fréquent associé à la résistance | Sensibilité accrue ; la résistance vient de mutations rares | Manuel de pharmacologie |

D'autres erreurs ont été corrigées dans le texte proposé avant son intégration : sidération auriculaire de plusieurs semaines et non de plusieurs jours, conversion spontanée de 69 % à 48 heures (et non 76 à 83 %), sources d'essais erronées (PALLAS, Nakazawa, Nuotio), allongement inexact de la longueur d'onde par la classe Ic. Le détail figure dans `journal.json` et dans les fichiers `*.contreverif.json`.

## Réserves à arbitrer

1. **Anticoagulation après cardioversion.** L'ESC 2024 se contredit : tableau de recommandations 15 (quatre semaines après toute cardioversion, classe I) et § 7.2.1 (facultative sans facteur de risque si le rythme sinusal revient en moins de 24 heures). Le texte suit l'arbitrage I48-09 de Codex (règle par défaut, exception possible) ; la fenêtre `i48-24h` expose les deux positions.
2. **Préférence pour l'antivitamine K dans le syndrome des antiphospholipides** : l'essai TRAPS ne portait pas sur des patients en FA ; la règle est extrapolée.
3. **Chiffres non relus en texte intégral** : guide EHRA 2021 (fractions rénales, demi-vies de 5 à 17 heures, règle de Child-Pugh), Friberg 2012 (retiré), demi-vie de la digoxine. Les chiffres de CHAMPION-AF suivent l'arbitrage I48-07 de Codex.
4. **Données suisses** : compendium.ch n'a pas été consulté ; les données de disponibilité, dont celle de l'andexanet alfa, et les informations professionnelles suisses restent à vérifier.
5. **ESC 2026 sur l'insuffisance cardiaque**, cité par le cours pour la définition de l'ICFEr (FEVG < 50 %) : non vérifiable par Claude, conservé tel quel.
6. **Dose de bolus de digoxine** : fenêtre existante 0,25–0,5 mg, tableau 12 de l'ESC 0,5 mg intraveineux.

## Fichiers livrés

- 8 copies corrigées dans `sources/chapters/I48/`, dont `I48_d.html`, ajouté pour la première fois au manifeste avec l'empreinte de l'original.
- `glossary/i48.py` : 5 entrées, AFFIRM, AVERROES, DIG, XII et Wolff-Chaikoff. Elles sont remises par la branche, car `apply-claude` ne traite pas le glossaire.
- `livraison.json` : empreintes originales inchangées, `proposed_sha256` mis à jour.

## Contrôles réellement exécutés

Les contrôles ont été exécutés sur la base `a6f18a1`, après copie temporaire des 8 fichiers dans `chapters/I48/`. Les sources canoniques ont ensuite été restaurées par `git checkout -- chapters/I48`.

| Commande | Résultat |
| --- | --- |
| `python3 test_v7.py --static I48 I70 I71 I80` | OK ; I48 : 66 339 mots, 100 fenêtres, 4 quiz, 15 Pareto. Un premier passage avait signalé des initiales d'auteurs et cinq termes ; les initiales ont été retirées des rubriques Source et les cinq termes ajoutés au glossaire. |
| `MEDINA_OUT=$PWD/dist python3 build_front.py --all-fragments` | Réussi, 22 fragments |
| `python3 tests/audit_fragments.py` | JavaScript valide, build reproductible |
| `python3 tests/audit_sciences.py` | `errors: []` |
| `python3 -m unittest discover -s tests` | 76 tests réussis |
| `node tests/verify_sciences_cs.cjs` | 609 contrôles, 0 erreur |
| `node tests/verify_s01_browser.cjs` | 71 contrôles, 0 erreur |
| `node tests/verify_justifications_recovery.cjs` | 2 310 contrôles, 0 erreur |
| `node tests/verify_categories.cjs` | 656 contrôles, 0 erreur |
| `node tests/verify_organisation.cjs` | OK, 740 contrôles |
| Contrôle navigateur ciblé d'I48 | 206 mots verts, 84 clés distinctes, aucune clé manquante ; `i48-bilan` et `i48-noeudav` s'ouvrent ; le renvoi `i48-bilan` → `i48-cg` fonctionne depuis la fenêtre ; aucune erreur JavaScript |
| `python3 tools/livraison.py check-claude "livraisons/Livraison Claude/C-01-Cardiologie"` | Conforme : 8 fichiers vérifiés, empreintes de départ égales aux sources canoniques de `a6f18a1` ; aucune injection |

## Suite

- Injection par Codex avec `apply-claude "livraisons/Livraison Claude/C-01-Cardiologie"`, puis fusion de `glossary/i48.py` (5 entrées) depuis la branche.
- Validation des fenêtres types et du volume par le propriétaire, puis extension aux 14 autres cours de Claude selon `MECHANISMS_CLAUDE.md` : I30, I33, I35, I34, I00, I40, I42, I44, I47, I49, I46, Q21, I71, I80.
