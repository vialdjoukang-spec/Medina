# Lot J45 — J45 — Asthme (P-02-Pneumologie)

## Identité et provenance

- **Responsable :** Claude (coordination, assemblage final, Git), branche `claude/loving-shannon-spwrhc`, PR #12.
- **Base :** `main` `a3b8ac4060529aaf339f17851305c07abac25cc8`. Les sources J45 sont inchangées depuis `3dac928`, la base de travail. Date : 8 octobre 2026.
- **Ordre :** remise faite selon la consigne du propriétaire du 8 octobre. Le chapitre suivant s'enchaîne une fois le précédent produit et remis pour audit : I83 v6 et I89-3 sont remis et médicalement acceptés. J45 est le premier chapitre de la file Claude après la cardiologie, comme le prévoit le cahier des charges.
- **Sous-agents (sept), un auteur par fichier et par phase :**

| Phase | Rôle | Fichiers possédés |
| --- | --- | --- |
| Rédaction | Pathologie, îlots 0–6 | `J45_a.html`, `J45_pop1.html` |
| Rédaction | Pathologie, îlots 7–13 : diagnostic, crise et état de mal (J46), traitement, asthme sévère, suivi, critères | `J45_b.html`, `J45_pop2.html` |
| Rédaction | Sciences | panneau Sciences de `J45_c.html`, `J45_pop4.html` |
| Rédaction | Pharmacologie | `J45_d.html`, `J45_pop3.html` |
| Assemblage | Assembleur unique : propositions croisées, onglet Examens, Pareto, justifications | tous les fichiers du chapitre |
| Vérification | Vérificateur indépendant : exactitude des données à haut risque et concision | tous les fichiers du chapitre |

Les rapports de chaque rôle sont dans `verification/`.

## Catégories, sous P-02-Pneumologie

| Catégorie | Traitement |
| --- | --- |
| J45 — Asthme | Traité en entier : définition, phénotypes et endotypes, diagnostic avec confirmation objective, différentiels, contrôle et risque futur, voies GINA 1 et 2, dispositifs et observance, asthme difficile et sévère, populations particulières, suivi |
| J46 — État de mal asthmatique | Traité : gravité, conduite aux urgences, oxygène, bronchodilatateurs, corticostéroïde, magnésium, critères d'insuffisance respiratoire, admission, sortie, physiopathologie (onglet Sciences) |

## Référence principale et accès

**GINA 2026**, rapport complet du 5 mai 2026 et guide de synthèse de juillet 2026, lus en **texte intégral** le 08.10.2026. Les encadrés 1-2, 1-4, 4-2, 4-8A et B, 9-4, 9-6 et 12-4 ont été lus en image. Les autres sources sont citées dans le cours avec leur statut d'accès : ATS/ERS 2019 et 2022, ERS 2017, ISHAM 2024, ACR/EULAR 2022, essais AMAZES, SMART, Perrin 2011, Ullemar 2016 et d'autres. Les matrices passage → correction → source → accès figurent dans `verification/*.md`.

## Principales corrections médicales

- **Diagnostic.** Les seuils de réversibilité suivent GINA 2026 :
  - adulte : VEMS ou CVF ≥ 12 % et ≥ 200 mL ;
  - enfant : ≥ 12 % de la valeur prédite.

  Le critère ERS/ATS 2022 est remis à sa place. Les critères formels exigent la **variabilité**, et non plus une obstruction sous la limite inférieure de la normale. Les délais d'arrêt des bronchodilatateurs sont précisés. Les catégories de PD20 à la méthacholine, qui étaient fausses, sont corrigées (ERS 2017).
- **Biomarqueurs.** Les éosinophiles sont **plus élevés** tôt le matin ; le texte disait l'inverse. Il faut rechercher une strongyloïdose dès 300/µL. Le texte donne aussi les seuils de FeNO selon GINA.
- **Crise et état de mal (J46).**
  - Classification de gravité GINA 2026, sans la fréquence cardiaque.
  - Oxygène si la saturation est < 92 %, avec une cible de 92 à 95 %.
  - Salbutamol : 4 / 4–6 / 6–10 bouffées selon la gravité.
  - Insuffisance respiratoire : PaO₂ < 60 mmHg avec PaCO₂ normale ou > 45 mmHg ; le texte disait 42 mmHg.
  - Hospitalisation « se discute ».
  - Magnésium IV en mg/kg chez l'enfant de **2 à 5 ans** seulement.
- **Traitement de fond.**
  - Voie 2 avec secours anti-inflammatoire. L'association budésonide-salbutamol n'est pas autorisée en Suisse.
  - MART : consulter au-delà de 12 inhalations en 24 h, 8 chez l'enfant de 6 à 11 ans, aux paliers 3 et 4.
  - Réduction du traitement après 2 à 3 mois.
  - Interactions sous inhibiteurs du CYP3A4 selon GINA ; la préférence non sourcée pour le ciclésonide est retirée.
- **Pathologie.** Le salbutamol seul est présenté comme une association, et non comme une cause, avec la mortalité. Les définitions de l'asthme sévère et de l'asthme difficile sont corrigées. La rémission n'est pas définie par GINA. Les critères de l'ABPA (ISHAM 2024) et de la granulomatose éosinophilique avec polyangéite (ACR/EULAR 2022) sont mis à jour.
- **Sciences.**
  - Les ILC2 produisent surtout IL-5 et IL-13.
  - Le benralizumab vise le récepteur de l'IL-5.
  - La réponse tardive commence à 3–4 h et culmine entre 6 et 12 h.
  - L'héritabilité est de 82 % (Ullemar 2016).
  - Une nouvelle discipline expose la physiopathologie de la crise et de l'état de mal.
  - Les affirmations causales non démontrées sont requalifiées.
- **Pharmacologie.** L'onglet passe de 965 mots à un exposé complet : classes, stratégie, doses par âge, interactions, exacerbation, biothérapies, grossesse, enfant et sujet âgé. La disponibilité est contrôlée sur la liste Swissmedic des autorisations.

**Concision.** Après l'assemblage, le vérificateur a supprimé les redites entre îlots, fenêtres et Pareto. Le volume passe de 41 747 à 37 743 mots ; toutes les doses, seuils, mécanismes, limites et pièges sont conservés.

## Fichiers livrés

Ce sont neuf fichiers primaires du cours, déclarés dans `livraison.json` : `J45_{a,b,c,d}.html`, `J45_pop{1..4}.html` et `J45_justifications.json`. Le glossaire n'est pas modifié. Le diff complet se trouve dans `controles/diff_main.diff`. Identifiants, `data-k`, `data-pop`, classes, critères formels et paramètres clés sont conservés. Une seule entrée de justification est modifiée : `j45-j-variabilite` reçoit `"occurrence": 1`.

## Contrôles (base `main` `a3b8ac4`, sorties hors dépôt)

| Contrôle | Résultat |
| --- | --- |
| `verifier_sigles.py J45` | `{}` |
| `test_v7.py --static J45` | OK — 37 340 mots, 46 fenêtres, 8 quiz, 8 Pareto |
| `tools/insert_justifications.py --course J45` | 15 fenêtres, 15/15 cibles |
| `build_front.py`, `--all-fragments`, `tests/audit_fragments.py` | 22 fragments, JavaScript valide, build reproductible |
| Empreinte SHA-256 du build `MEDINA_S02_respiratoire.html` | `ffa8cadcd553f9fbf2736737af10a161025ec60cf4cd3d413a513fbb312af8a1` |
| `tests/verify_course_native.cjs J45` (1 360 et 390 px) | 2 282 contrôles, 0 échec |
| `python3 -m unittest discover -s tests` | 118 tests OK |
| `tools/livraison.py check-claude --root <main a3b8ac4 propre>` | empreintes et chemins conformes |

## Réserves

- **Médicales et documentaires :**
  - informations professionnelles suisses inaccessibles : limites MART, ipratropium, Trimbow, montélukast et remboursement non vérifiés ;
  - ERS 2017 et ERS/ATS 2022 lus en résumé ;
  - GINA se contredit sur la durée de perfusion du magnésium chez l'enfant (10–20 ou 20–60 minutes) ; le texte est retenu ;
  - repris sans relecture primaire : le 5e caractère CIM-10-GM, le pouls paradoxal à 25 mmHg et l'ABPA ISHAM 2024 (résumé) ;
  - l'OFSP et la Société suisse de pneumologie n'ont pas été consultés.
- **Rédactionnelle :** le volume reste élevé pour un seul cours ; une passe supplémentaire reste possible selon l'ordre de grandeur que fixera le propriétaire.
- **CIM-11 :** couverture non établie. Aucune validation n'est déduite des tests.

## Demande de contrelecture

Audit croisé Codex des sources de ce lot (`sources/`), au commit qui publie ce rapport.
