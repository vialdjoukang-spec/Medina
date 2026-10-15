# Rapport de rédaction — R26 (N-05-Neurologie) — Cycle Betta 42, leçon 2

Agent C42-A1-NEUR (rédaction, Sonnet 5.5), 15.10.2026. Porte de vérité : `python3 tools/betta_verite.py` affichait « VÉRITÉ OK » avant rédaction (25 sources). Seules les données de `recherche.md` et `sources.json` sont utilisées. Mention : **Audit différé — revue IA, distincte d'une validation médicale humaine.**

## Fichiers (sous ce dossier)
| Fichier | Octets |
|---|---|
| `chapters/R26/R26_a.html` (en-tête, onglet Pathologie, îlots 0 à 4) | 29 807 |
| `chapters/R26/R26_b.html` (Pathologie, îlots 5 à 14 et références) | 41 523 |
| `chapters/R26/R26_c.html` (onglet Examens, onglet Sciences) | 25 049 |
| `chapters/R26/R26_d.html` (onglet Pharmacologie) | 10 787 |
| `chapters/R26/R26_pop1.html` (27 fenêtres de contenu) | 19 685 |
| `chapters/R26/R26_pop2.html` (22 fenêtres de contenu, 10 Pareto) | 22 958 |
| `glossary/r26.py` | 8 476 |
| Total | 158 285 |

Environ 11 600 mots dans les quatre fichiers de cours, 9 quiz (1 + 2 en Pathologie, 3 en Examens, 3 en Pharmacologie), 5 figures SVG noir et blanc légendées, 59 fenêtres (49 de contenu, dont un moyen mnémotechnique marqué « aide pédagogique, non critère officiel », et 10 Pareto). Les 25 sources S1 à S25 sont toutes citées (attribut `data-src`).

## Contrôles (cahier W)
- HTML bien formé (balises équilibrées sur le gabarit complet a + b + c + d, et sur chaque fichier de fenêtres), identifiants uniques et préfixés `r26-`, chaque `data-k` possède sa fenêtre, chaque fenêtre est appelée, tous les `data-cover` des Pareto et tous les renvois du sommaire existent.
- Essai de construction dans une racine isolée (`build_medina.build`, glossaires existants + `r26.py`) : les ratios des Pareto sont calculés, `audit()` renvoie `{}`. Test navigateur non lancé.
- Glossaire : entrées conditionnelles (`add_if_absent`, aucune mutation des glossaires existants) pour les codes CIM-10-GM cités (R26, R26.0, R26.1, R26.2, R26.3, R26.8, R27.0, A52.1, M62.3, G11), les sigles (SSP, WFG, TUG, SPPB, EMS, BFU, CHF, ISFM, CIM, SA) et les noms propres (StoppSturz, STOPPFall, DO-HEALTH, VITAL, Vi-De, VERFORA, Sanofi-Aventis, noms d'auteurs). Le sigle « GTI » du dossier n'est pas utilisé (lettres non définies dans le dossier) : le cours écrit « impossibilité de marcher ou de tenir assis ». Le moyen mnémotechnique « BD-FIC » est propre au cours, signalé comme tel.
- Aucun îlot ni tableau consacré au code CIM ; plan monographique classique. Aucune recommandation américaine comme fondement : S7 (co-auteurs américains) ne sert qu'à la sémiologie, S10 cite VITAL comme donnée probante ; S5 mentionne d'anciennes recommandations américaines et britanniques qui ne sont pas utilisées.
- Points signalés dans le cours comme limites des sources : les trois pourcentages de Bruneck (24,0 %, 17,4 %, 9,2 %) ne se réconcilient pas avec le total de 32,2 % dans le résumé lu ; le dossier nomme treize des quatorze classes STOPPFall ; la mise en garde « TIH J5–J21 » de Clexane est rendue par « entre le 5e et le 21e jour » ; les libellés français des codes viennent du registre du dépôt ; les développements des sigles SPPB et ISFM suivent l'usage courant (non détaillés dans le dossier).

## Matrice de complétude (reprise du dossier, avec onglet et identifiant HTML)
Onglets : pA = Pathologie, pE = Examens, pS = Sciences, pP = Pharmacologie.

| Rubrique | Statut | Onglet | Identifiant HTML |
|---|---|---|---|
| 1. Question clinique et enjeu pour l'examen fédéral | ✔ | pA | `r26-0` (vignette fictive, objectifs, SSP 96, 97, 98, 103), fenêtres `r26-vignette`, `r26-ssp` |
| 2. Définition et périmètre CIM-10-GM | ✔ | pA | `r26-1` (§1.1 marche normale, §1.2 périmètre et exclusions), fenêtres `r26-marche-normale`, `r26-exclusions` |
| 3. Classifications et stades | ✔ | pA | `r26-1` (§1.3 clinico-anatomique, Nutt, signes ; §1.4 risque de chute, fragilité, freezing), fenêtres `r26-nutt`, `r26-wfg`, `r26-chute-grave`, `r26-fragilite`, `r26-freezing`, `r26-mnemo` |
| 4. Épidémiologie suisse puis européenne | ✔ (troubles de la marche en Suisse : LACUNE L12, dite) | pA | `r26-2` (tableau BFU, Bruneck, international, trouble fonctionnel), encadré « Lacune » ; fenêtres `r26-bfu`, `r26-bruneck`, `r26-ems` |
| 5. Normal → pathologique | ✔ (immobilité : LACUNE L1, dite) | pA, pS | `r26-3` (cycle, vieillissement, intégration, stratégie protectrice, cognition, tableau des mécanismes, figure 1), `r26-s-anat-cours`, `r26-s-physio-cours`, `r26-s-biomeca-cours` (figures 3 à 5), `r26-11` |
| 6. Étiologies et facteurs de risque | ✔ | pA | `r26-4` (causes, tableau des risques relatifs BFU, STOPPFall, environnement) |
| 7. Anamnèse et symptômes (fréquences) | ✔ (fréquences : LACUNE L2, dite) | pA | `r26-5` (chutes, indices, peur de chuter) |
| 8. Examen clinique (sensibilité/spécificité) | ✔ (Se/Sp des signes usuels : LACUNE L3, dite) | pA, pE | `r26-6` (observation, tests, signes discriminants en cartes, Schellong), `r26-e-2` |
| 9. Drapeaux rouges et urgences | ✔ (délais chiffrés : LACUNE L4, dite) | pA | `r26-8` (div.alert, tableau de huit situations, complications) |
| 10. Examens complémentaires | ✔ (valeurs normales biologiques : LACUNE L5, dite) | pE, pS | `r26-e-1` à `r26-e-6` (gold standard par question), `r26-s-anat-cours` à `r26-s-biomeca-cours` |
| 11. Diagnostic différentiel | ✔ | pA | `r26-7` (tableau de dix-huit diagnostics et éléments discriminants, figure 2) |
| 12. Prise en charge suisse (FI datées) | ✔ (physiothérapie selon l'OPAS et niveaux de soins : LACUNE L6, dite) | pA, pP | `r26-9`, `r26-10`, `r26-11`, `r26-p-1`, `r26-p-2` (tableau des doses), `r26-p-3`, fenêtres `r26-clexane`, `r26-vide3`, `r26-madopar`, `r26-lioresal` |
| 13. Complications et pronostic | ✔ | pA | `r26-8` (complications), `r26-11`, `r26-12` (pronostic) |
| 14. Suivi, prévention, dépistage | ✔ | pA | `r26-12` (repérage opportuniste, suivi de la déprescription, prévention BFU) |
| 15. Situations particulières | ✔ (grossesse, boiterie de l'enfant : LACUNE L7, L8, dites) | pA | `r26-13` (tableau : âgé, démence, insuffisance rénale, grossesse, enfant, hôpital) |
| 16. Spécificités suisses | PARTIEL (LACUNE L6, L9, L10, L11, dites) | pA, pP | `r26-13` (recherche suisse, FI datées, conduite), `r26-2`, `r26-9`, `r26-p-2` ; fenêtre `r26-conduite` |
| 17. Critères formels du diagnostic | ✔ | pA | `r26-14` (div.alert : pas de critères formels, critères opératoires) |
| 18. Paramètres clés chiffrés | ✔ | pA | `r26-14` (tableau puis div.key final) |
| 19. Sous-codes CIM-10-GM couverts | ✔ | pA | `r26-1` §1.2 (R26.0, R26.1, R26.2, R26.3, R26.8 avec renvoi vers les sections qui les traitent ; exclusions G11.-, A52.1, R27.0, M62.3-), `r26-11` (R26.3), fenêtre `r26-exclusions` |
| 20. Points d'examen fédéral et pièges | ✔ | pA, pE, pP | `r26-0` (SSP) ; encadrés « Piège » et « Erreur fréquente » de `r26-1`, `r26-3`, `r26-5`, `r26-6`, `r26-7`, `r26-9`, `r26-10`, `r26-e-1` à `r26-e-5`, `r26-p-1`, `r26-p-3` ; quiz de `r26-1`, `r26-6`, `r26-7`, `r26-e-2`, `r26-e-3`, `r26-e-5`, `r26-p-2`, `r26-p-3` ; 10 Pareto |

## Lacunes (reprises du dossier, signalées dans le cours)
1. L1 — physiopathologie du déconditionnement et de l'immobilité : encadré « Lacune » de `r26-11`.
2. L2 — fréquences des symptômes : dernier paragraphe de `r26-5`.
3. L3 — sensibilité et spécificité des signes de marche usuels : `r26-6` (§6.4).
4. L4 — délais chiffrés des urgences médullaires et de la polyradiculonévrite : `r26-8`, fenêtre `r26-myelopathie`.
5. L5 — valeurs normales biologiques : `r26-e-3`, fenêtre `r26-ataxie-bilan`.
6. L6 — physiothérapie, ergothérapie (OPAS), niveaux de soins suisses : `r26-9` (§9.5), fenêtre `r26-exercice`.
7. L7 — troubles de la marche de la grossesse : tableau de `r26-13`.
8. L8 — boiterie et troubles de la marche de l'enfant : tableau de `r26-13`.
9. L9 — directive suisse d'aptitude à la conduite propre aux troubles de la marche : `r26-13`, fenêtre `r26-conduite`.
10. L10 — AI, Suva/LAA, LiMA : `r26-13`.
11. L11 — prévalence suisse des chutes et escarres à l'hôpital : encadré « Lacune » de `r26-2`.
12. L12 — épidémiologie suisse des troubles de la marche : encadré « Lacune » de `r26-2`.

Audit différé — revue IA, distincte d'une validation médicale humaine.
