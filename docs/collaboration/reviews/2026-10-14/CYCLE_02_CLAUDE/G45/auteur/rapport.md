# G45 — Accidents ischémiques cérébraux transitoires et syndromes apparentés (N-05-Neurologie)

**Auteur correcteur :** C02-R-NEUR (`claude-code/session_01NNsXRGeno3p5fi2QvuhRCM/C02-R-NEUR`), 14 octobre 2026.
**Statut :** corrections d'auteur remises pour la passe 2 de l'audit croisé (C02-R-HEM). Revue par IA, aucune validation médicale humaine. Ni commit ni push par l'auteur.

## Réserves de la passe 1 (corrigées, à lever par la passe 2)

| Réserve | Correction | Source relue le 14.10.2026 |
|---|---|---|
| R1 Aspirine Cardio | Onze contre-indications exactes, dont maladies inflammatoires de l'intestin et insuffisance cardiaque NYHA III–IV, dans la monographie et le tableau du corps ; portée limitée au produit exact | FI Aspirine Cardio 51795, mars 2026 |
| R2 Sortis | Cholestase, glécaprévir/pibrentasvir, arrêt immédiat si myopathie ou élévation significative de la créatine phosphokinase (seuil de la fiche : plus de cinq fois la limite chez le patient symptomatique), myalgie distinguée de la myopathie | FI Sortis 54085, avril 2025 |
| R3 Eliquis | Syndrome des antiphospholipides : non-recommandation (triple positivité), distincte des contre-indications ; hémorragie majeure : arrêt et mesures que la fiche propose d'envisager, sans dose imposée | FI Eliquis 61549, août 2026 ; Berne PDF p. 19 |
| R4 Thromboxane | Molécule, enzyme et récepteur distingués ; tableau de tous les symboles de la figure PharmGKB avec nom officiel ; seize clés de glossaire | HGNC, ChEBI, FI Aspirine Cardio |
| R5 Débit/résistance | Variables, unités, formule et réciproque, exemple fictif refaisable, effet d'une résistance doublée, limites | Maier et coll. 2026 ; Kho et coll. 2025 (CC BY) |
| R6 Sténose carotidienne | Imputabilité distinguée de l'indication (> 50 %), délai de quelques jours, statine haute dose, colloque, tableau chirurgie/stent, hyperperfusion, quiz | Berne PDF p. 13, 18, 19 ; résumé ESO 2021 |

Observations M1 (crédit Petit B), M2 (mot « reperfusion » coupé) et M3 (arrondi EXPRESS : 8,19 points ; rapport brut 0,21 distinct du rapport ajusté 0,20) corrigées.

## Choix entre les deux propositions préparatoires
- `G45_R1_R3_PROPOSITION.json` : non appliquée telle quelle (encadrés juxtaposés, listes incomplètes) ; son contenu, vérifié, est intégré au texte.
- `tools/cycle2_reprise_01_safety.py` : non exécuté ; il affirmait à tort que la FI Sortis ne fixe aucun seuil de créatine phosphokinase.

## Autres corrections médicales
- Plavix : inhibiteurs du CYP2C19 déconseillés au complet (dont fluoxétine, fluvoxamine, moclobémide), ISRS, arrêt 7 jours avant chirurgie, avertissement de la fiche sur l'association à l'aspirine après AIT, passage exact sur les métaboliseurs lents.
- Collisions de glossaire préexistantes : « thromboxane A2 » ouvrait l'albuminurie A2, « A1/A2, P1/P2 » l'albuminurie et la valve mitrale, « SC » la voie sous-cutanée.

## Enrichissements
- Différentiel hiérarchisé par gravité : neuf diagnostics, élément discriminant, examen décisif ; raisonnement de l'Examen fédéral (SSP 103, 205) ; quiz.
- Pharmacologie : tableau des doses FI/Berne, tableau contre-indications/non-recommandations, alertes interactions et arrêt.
- Calcul du multiple de la limite (exemple fictif) ; délais de conduite après AIT (non contraignants).

## Images
Neuf images ouvertes une à une et conformes à leur légende ; licences relues dans les métadonnées Commons. Aucune remplacée. Manifeste : `preuves/images_claude.json`.

## Contrôles
- `test_v7.py --static G45` : **OK** (la version Codex échouait sur quatre abréviations).
- Aperçu isolé (`tools/night_preview.py`) : 133 mots interactifs cliqués sans fiche absente, 0 erreur JavaScript, aucun débordement horizontal à 390 px.

## Réserves ouvertes (non bloquantes)
1. Textes intégraux ESO 2021, Claassen 2021 et Eren 2021 inaccessibles le 14.10.2026 : les affirmations correspondantes reposent sur l'archive Codex et la passe 1, ce que le registre indique ligne par ligne.
2. Recommandation sur l'amnésie globale transitoire : validité annoncée jusqu'à fin 2025, sans édition plus récente confirmée.
3. Pareto restés brefs (forme Codex).

## Preuves
`entree.json`, `sortie.json`, `auteur.json`, `controle_technique.json`, `empreintes_entree.json`, trois captures de contrôle ; registre `preuves/source_ledger_claude.json` (277 affirmations, `unverified_claims: []`).
