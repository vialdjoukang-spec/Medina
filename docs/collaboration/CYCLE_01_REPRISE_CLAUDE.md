# Cycle 1 — remise ouverte à Claude

Vial autorise la publication maintenant, sans contre-audit préalable, puis la relecture par Claude le **14 octobre 2026, Europe/Zurich**. Cette intention n'est pas une session ni une automatisation démarrée. Lire [l'exception](instructions/CYCLE_01_EXCEPTION_CLAUDE_VIAL_2026-10-13.md) et les instructions actuelles en tête d'AGENTS.md/CLAUDE.md.

## Accès direct aux quatre cours

| Chapitre | Cours public | Sources canoniques |
| --- | --- | --- |
| I63 — Infarctus cérébral | [Neurologie](https://vialdjoukang-spec.github.io/Medina/fragments/MEDINA_S08_nerveux.html#/entry/I63) | [chapters/I63](https://github.com/vialdjoukang-spec/Medina/tree/main/chapters/I63) |
| E11 — Diabète sucré de type 2 | [Endocrinologie](https://vialdjoukang-spec.github.io/Medina/fragments/MEDINA_S05_endocrinien-metabolique.html#/entry/E11) | [chapters/E11](https://github.com/vialdjoukang-spec/Medina/tree/main/chapters/E11) |
| N17 — Insuffisance rénale aiguë | [Néphrologie](https://vialdjoukang-spec.github.io/Medina/fragments/MEDINA_S04_renal-voies-urinaires.html#/entry/N17) | [chapters/N17](https://github.com/vialdjoukang-spec/Medina/tree/main/chapters/N17) |
| D50 — Anémie par carence en fer | [Hématologie](https://vialdjoukang-spec.github.io/Medina/fragments/MEDINA_S06_hematopoietique-lymphatique.html#/entry/D50) | [chapters/D50](https://github.com/vialdjoukang-spec/Medina/tree/main/chapters/D50) |

Les sept fichiers par cours comprennent quatre onglets, deux ensembles de fenêtres et le glossaire `glossary/<code>.py`. Le registre [courant](../../organisation/CYCLE_01_REPRISE_CLAUDE_2026-10-13.json) donne les 28 empreintes. Les revues antérieures restent dans les dossiers du Cycle 1 du 11 octobre. Leur portée porte sur les sources historiques ; les quatre fichiers D50 corrigés le 13 octobre ont une [trace distincte](reviews/2026-10-13/CYCLE_01/corrections_D50.json).

## Consultation, relecture et corrections

Il n'y a plus de verrou STOP immuable sur ces quatre cours. Claude peut travailler sur sa branche, auditer les sources actuelles, appliquer ses corrections et publier sans contre-audit préalable ni nouvelle autorisation de Vial. Les autres sources et leurs gardes demeurent protégées.

Après une correction, produire un rapport technique réel lié aux 28 empreintes courantes. Il comporte `files`, `result: "passed"`, `desktop: true`, `mobile: true`, `javascript_errors: []`, `missing_windows: []`. Un résultat n'est favorable qu'après les vérifications correspondantes. Le contrôle existant fournit le format et sa portée technique ; son réemploi après modification de sources est refusé.

Puis tracer les corrections, sans modifier les anciens rapports :

```bash
python3 tools/cycle1_claude_receipt.py \
  --checks docs/collaboration/reviews/rapport_technique_Claude.json \
  --reason "Description des corrections réellement appliquées"
python3 -m unittest discover -s tests -p 'test_*.py'
# Après commit, contrôler les changements réels :
python3 tools/espace.py garde HEAD^ HEAD
```

Cet outil met à jour les empreintes et le rapport de changements, pas la qualification d'audit. Déposer le rapport clinique réel séparément, avec portée, sources consultées, réserves, auteur, version examinée et date. Aucune étape non faite n'est déclarée réalisée. Le nouveau reçu ne certifie ni une complétude CIM-11 ni une validation médicale humaine.

## Affectation des cycles

Un seul cycle actif par IA responsable, sous-agents inclus. Le Cycle 1 est remis à Claude pour sa relecture différée après publication. Codex peut ensuite préparer le Cycle 2 autorisé, avec un registre et des contrôles propres ; les cours du Cycle 2 ne sont pas produits par cette remise. Les IA différentes peuvent travailler sur des cycles différents.
