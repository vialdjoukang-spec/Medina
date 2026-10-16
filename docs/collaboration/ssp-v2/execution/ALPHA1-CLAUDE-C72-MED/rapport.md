# Audit médical Alpha, tour 1 — C72, tumeur maligne de la moelle épinière, des nerfs crâniens et d’autres parties du système nerveux central (S08)

Mission `ALPHA1-CLAUDE-C72-MED`, branche `claude/alpha1/c72-med-g1`, base de la mission `d1a488ad4f0031d7f2a4b47a0721e89a93475d77` (manifeste) ; base du worktree `32416a2080e67537641040a81252dec0b3e6d137` : START exécuté sur le premier main contenant l'approbation de la mission (PR #181). Sources figées identiques : empreintes SHA-256 conformes au manifeste. Audit médical agressif avec enrichissement, effort élevé, modèle conforme au manifeste. Revue du 16 octobre 2026.

## Lecture et empreintes

Les sept fichiers de la leçon ont été lus en entier : `C72_a.html` à `C72_d.html`, `C72_pop1.html`, `C72_pop2.html` et `glossary/c72.py`. Leurs SHA-256, recalculés, sont **conformes au manifeste** (base de sources `d1a488ad`). La première source lue est la recommandation EANO 2018 sur les tumeurs épendymaires ([PMC5909649](https://pmc.ncbi.nlm.nih.gov/articles/PMC5909649/)), aux sections *Treatment of ependymal tumors of the spinal cord*, *Table 1* et *Table 5*.

## Verdict

Le fond médical est solide. Il n’y a **aucun constat bloquant** au sens d’une erreur médicale ; l’absence de sémiologie (MAJ-01) bloque toutefois la clôture du cours et du lot. Les points vérifiés le sont presque tous : les doses de radiothérapie de l’EANO 2018, le bilan d’extension à deux ou trois semaines, les chiffres QUANTEC, la définition du syndrome de la queue de cheval, l’épidémiologie zurichoise et les informations professionnelles suisses. La leçon souffre en revanche de **trois défauts de structure**. La sémiologie est absente. Les sciences n’ont que quatre disciplines, trop brèves. Le périmètre de codage est inexact pour deux entités de comportement incertain.

| Gravité | Nombre |
|---|---|
| BLOQUANT | 0 |
| MAJEUR | 6 |
| MINEUR | 9 |
| ENRICHISSEMENT | 12 |

## Constats majeurs

1. **MAJ-01 — MAJEUR, bloquant pour la clôture du cours et du lot (AGENTS.md) : le sixième sous-onglet « Sémiologie fondamentale et analytique » est absent** (`C72_c.html`, `div.sci-bar`). Les signes de l’onglet 1 sont cités sans technique, sans valeur ni regroupement syndromique. La proposition complète figure dans `propositions/C72_c_semio.html`, avec ses neuf fenêtres dans `propositions/C72_pop2_semio.html`. Ces fenêtres s’ajoutent à `C72_pop2.html` : l’outil `alpha_publication` n’admet que `_pop1` et `_pop2`, il n’y a donc pas de fichier `_pop3`.
2. **MAJ-02 — Les sciences comptent quatre disciplines au lieu de cinq.** La discipline proposée est la *Physiologie des voies médullaires et du contrôle sacré* (`propositions/C72_c_physio.html`). C’est elle qui explique la parésie non radiculaire, l’ataxie, la dissociation des sensibilités et la différence entre cône et queue de cheval [S12] [S13] [S5].
3. **MAJ-03 — `tests/audit_sciences.py` échoue.** Les quatre disciplines totalisent 788 mots, et chacune reste sous le minimum de 280. Les libellés « Science → clinique / examen / traitement » manquent, et la Génétique n’a pas de figure. Les libellés proposés sont dans `propositions/C72_c_liens.html`.
4. **MAJ-04 — Le périmètre de codage est inexact.** La catégorie CIM-10 découle du code de comportement CIM-O [S20]. L’épendymome myxopapillaire (9394/1) et l’astrocytome pilocytique du nerf optique (9421/1) ont un comportement /1 [S21] : ils relèvent donc de D43.4 et D43.3, non de C72.1 et C72.3. Ces tumeurs restent toutefois à déclarer au registre. **Réserve** : la table CIM-O-3.2 en vigueur n’a pas été lue. Proposition : `propositions/C72_b_1.html`.
5. **MAJ-05 — La figure 5 est illisible à 390 px.** Le texte y est rendu à 7,3 px, alors qu’il porte les valeurs décisionnelles de dose et de risque. Les figures redessinées sont dans `propositions/C72_figures.html`.
6. **MAJ-06 — Les figures 1 et 3 sont des dessins anatomiques d’origine IA.** La figure 1 représente des coupes de moelle, la figure 3 la moelle, le cône terminal et les racines de la queue de cheval. Toutes deux ont été produites par l’agent de rédaction du cycle Betta 41, sans source iconographique, ce que la règle de Vial interdit. Elles sont reclassées `ANATOMIQUE_IA`. Aucun SVG de remplacement n’est proposé : la réserve est « figure anatomique à sourcer (original réel via Image_Clo_finder) ».

## Constats mineurs

- **MIN-01** : la FI suisse de Koselugo® (juin 2026) vise l’adulte et l’enfant dès 3 ans, avec un maximum de 50 mg par prise.
- **MIN-02** : la leçon déclare les interactions du témozolomide non lues, alors que la FI suisse les donne (acide valproïque, myélosuppresseurs, médicaments induisant une anémie aplasique). La surveillance hépatique manque aussi.
- **MIN-03** : D35.2 désigne l’hypophyse. Les règles de déclaration propres aux patients de moins de 20 ans sont omises.
- **MIN-04** : la relation dose-effet de 40 à 45 Gy est restreinte au bas grade, alors que la source ne fait pas cette restriction.
- **MIN-05** : la figure 4 est rendue à 7,8 px à 390 px. Les figures 1 et 3 avaient le même défaut, mais elles relèvent désormais de MAJ-06.
- **MIN-06** : trois causalités sont rédactionnelles et non sourcées (c72-2, c72-5, c72-e-1).
- **MIN-07** : l’urgence d’imagerie est attribuée à une revue radiologique qui ne parle pas d’imagerie. La synthèse suisse de Spirig la fonde mieux.
- **MIN-09** : devant une suspicion de MPNST, la leçon écrit « exérèse urgente » sans la condition posée par l’ERN GENTURIS (tableau 9, recommandations 4 et 5, 2023). L’exérèse primaire se fait si elle est sûre et faisable ; sinon, une biopsie guidée par l’imagerie est réalisée. Le refus de l’attente vigilante vise le MPNST, non tout signe d’alarme.
- **MIN-08** : un piège d’examen affirme « astrocytome pédiatrique ». Or l’astrocytome forme 30 à 40 % des gliomes intramédullaires de l’adulte [S3].

## Enrichissements proposés

ENR-01 à ENR-12 : sous-onglet de sémiologie, fenêtres, discipline de physiologie, libellés des sciences, piège de codage, déclaration au registre, Koselugo®, interactions du témozolomide, hétérogénéité du gliome H3 K27-altéré (grades historiques, 32 contre 23 mois [S10]), valeur chiffrée du résidu post-mictionnel et du toucher rectal, réattribution de l’urgence et figures non anatomiques 4 et 5 pour 390 px (réserve pour les figures anatomiques 1 et 3).

## 21 — Sémiologie fondamentale et analytique

**Statut : absente → MAJEUR, bloquant pour la clôture du cours et du lot (MAJ-01, AGENTS.md).** Ce n'est pas une simple lacune.

- **Sémiologie fondamentale.** Les symptômes sont nommés dans c72-5 et c72-6, mais aucune entrée ne comporte ses six éléments : définition, normal, technique, mécanisme, valeur et piège. Les sources lues ne donnent aucune fréquence chiffrée de symptôme. Cette lacune est déclarée par la leçon elle-même (c72-lacunes). Deux gestes ont pu être chiffrés pour cet audit, d’après des résumés. Le résidu post-mictionnel au seuil de 200 ml a une sensibilité de 82 % et une spécificité de 65 % [S14]. Le tonus anal a une sensibilité de 0,23 à 0,53 [S15].
- **Sémiologie analytique.** Il manque l’examen systématique numéroté, le tableau des syndromes, le raisonnement en cinq étapes et les cas corrigés. Les syndromes proposés (antérieur, voies longues, transverse, cône, queue de cheval) s’appuient sur deux synthèses universitaires suisses, de l’Inselspital [S12] et du CHUV [S13], lues en résumé.

| Critère | Résultat |
|---|---|
| SEM-01, SEM-02 | non |
| SEM-03 | non : `audit_sciences.py` échoue |
| SEM-04 | oui : `test_v7.py --static C72` affiche OK |
| SEM-05 à SEM-09, SEM-11, SEM-12, SEM-15 à SEM-18 | non |
| SEM-10, SEM-14 | partiel |
| SEM-13 | non : l’alerte existe dans l’onglet 1 (c72-8), mais aucune discipline de sémiologie ne la reprend |
| SEM-19 | oui pour les sources de la leçon |
| SEM-20, SEM-21 | sans objet |
| SEM-22, SEM-23 | non : aucune capture, la discipline n’existe pas |
| SEM-24 | oui |

Le « non » sur les critères bloquants SEM-01 à SEM-03 et SEM-13 tient à l’absence de la discipline. Il ne signale aucune erreur médicale. La proposition `C72_c_semio.html` y répond : elle suit la structure du § 4 b, ne contient aucun style en ligne, et sa figure tient dans une `viewBox` de 360 avec un texte de 17.

## Matrice des 20 rubriques

| Rubrique | Statut |
|---|---|
| 1 Question clinique ; 3 Classifications ; 6 Étiologies ; 10 Examens ; 11 Différentiel ; 13 Complications et pronostic ; 14 Suivi ; 17 Critères ; 18 Paramètres ; 20 Points d’examen | couvert |
| 2 Périmètre CIM-10-GM ; 19 Sous-codes | partiel (MAJ-04) |
| 4 Épidémiologie | partiel (aucun chiffre suisse propre à C72) |
| 5 Normal → pathologique | partiel (sciences, MAJ-02 et MAJ-03) |
| 7 Anamnèse ; 8 Examen clinique | partiel (MAJ-01) |
| 9 Urgences | partiel (MIN-07 ; délai horaire non sourcé) |
| 12 Prise en charge suisse ; 15 Situations particulières ; 16 Spécificités suisses | partiel (lacunes déclarées) |

## Figures

L’inventaire `image_clo_finder` trouve cinq figures SVG vectorielles. Les figures 1 et 3 sont des dessins anatomiques d’origine IA démontrée par le rapport du cycle Betta 41 : elles sont classées `ANATOMIQUE_IA` (MAJ-06). Les figures 2, 4 et 5 sont classées `SCHEMA_NON_ANATOMIQUE`. La lisibilité a été mesurée par un rendu Chromium sans interface, dans une colonne de 358 px. Les figures 4 et 5 sont trop petites (MIN-05 et MAJ-05) ; seule la figure 2 est conforme. Après la revue Codex, les SVG anatomiques proposés (figures 1 et 3) sont retirés de `propositions/C72_figures.html`. La coupe de moelle de la figure P (physiologie) est remplacée par un schéma logique en cases.

## Lacunes principales

- **Sémiologie suisse.** Aucune source de sémiologie universitaire suisse n’a été lue en texte intégral : seuls les résumés de Hess, Novy et Spirig l’ont été.
- **Codes de morphologie.** La table CIM-O-3.2 et le Blue Book OMS 2021 n’ont pas été lus. La page pathologyoutlines.com était inaccessible.
- **Nerfs crâniens.** L’esthésioneuroblastome, le gliome malin du nerf optique et le MPNST des nerfs crâniens restent non documentés.
- **Neuromonitorage.** L’affirmation « apport discuté », attribuée à Westphal, n’a pas été retrouvée dans l’extraction.
- **Mode de lecture.** Les lectures PMC ont été faites par extraction ciblée de passages, limitée aux 100 000 premiers caractères pour les textes longs.

## Tableau de bord

| Élément | Valeur |
|---|---|
| Leçon | C72, fragment S08 |
| Fichiers lus | 7/7, empreintes conformes |
| Sources lues | 22 (`sources.json`), dont 9 suisses, parmi lesquelles 3 FI Swissmedic datées |
| Constats | 0 bloquant · 6 majeurs · 9 mineurs · 12 enrichissements |
| Propositions | 12 fichiers dans `propositions/` |
| Contrôles | `test_v7.py --static C72` OK · `audit_sciences.py` échec (préexistant) · JSON valides · ancres vérifiées |
| Sources canoniques modifiées | aucune |

## Suite de la revue Codex (constat P1)

La fenêtre proposée `c72-sm-nf1-douleur` et l’alerte de `c72-sm-1` faisaient de tout signe d’alarme de la NF1 une indication d’exérèse sans surveillance. La ligne directrice ERN GENTURIS (eClinicalMedicine, 13.01.2023, tableau 9, recommandations 2 à 5) a été relue. Les deux textes sont corrigés : IRM régionale d’abord, puis TEP au FDG avant toute chirurgie. L’exérèse primaire n’intervient que si une ANNUBP ou un MPNST est suspecté et que le geste est sûr et faisable ; sinon, une biopsie guidée est réalisée. Le constat MIN-09 étend la correction à la leçon. La correction fait l’objet d’un commit de suivi, car le commit de traçabilité était déjà poussé et l’historique ne se réécrit pas.

Audit IA — revue distincte d’une validation médicale humaine ; aucune source canonique modifiée.
