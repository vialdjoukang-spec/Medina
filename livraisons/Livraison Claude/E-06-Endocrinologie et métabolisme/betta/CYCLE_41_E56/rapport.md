# Rapport de rédaction — E56 Autres avitaminoses (cycle Betta 41, leçon 1)

Agent C41-A2-ENDO (Sonnet 5.5), 15.10.2026. Fragment E-06-Endocrinologie et métabolisme. Porte de vérité franchie avant rédaction (`python3 tools/betta_verite.py` : VÉRITÉ OK). Audit différé — revue IA, distincte d'une validation médicale humaine.

## Fichiers (`chapters/E56/` et `glossary/`)
| Fichier | Contenu | Taille (octets) |
|---|---|---|
| `E56_a.html` | onglet Pathologie, îlots 0–6, plan du cours | 28 470 |
| `E56_b.html` | onglet Pathologie, îlots 7–15 (îlot 14 Spécificités suisses ; îlot 15 critères formels `div.alert` puis paramètres clés `div.key`) | 32 741 |
| `E56_c.html` | onglets Examens (pE) et Sciences (pS), 4 schémas SVG | 24 854 |
| `E56_d.html` | onglet Pharmacologie (pP) | 9 621 |
| `E56_pop1.html` | 18 fenêtres cliniques | 11 585 |
| `E56_pop2.html` | 5 monographies et 10 boutons Pareto | 7 625 |
| `glossary/e56.py` | 35 entrées, ajouts conditionnels | — |

Volume : environ 11 500 mots, 34 fenêtres, 6 quiz, 10 boutons Pareto.

## Matrice de complétude, avec onglet et identifiant HTML
Onglets : pA = Pathologie, pE = Examens, pS = Sciences, pP = Pharmacologie. Les identifiants sont ceux des `section.ilot` des fichiers ci-dessus.

| Rubrique | Statut | Onglet · identifiant HTML | Sources |
|---|---|---|---|
| 1. Question clinique et enjeu pour l'examen fédéral | ✔ | pA · e56-0 ; objectifs PROFILES et pièges : pA · e56-14 | S2, S5, S6, S13, S29 |
| 2. Définition et périmètre CIM-10-GM | ✔ | pA · e56-1, e56-14 (tableau de codage, fenêtres e56-codes, e56-spiges) | S1, S10, S28 |
| 3. Classifications et stades | ✔ partiel : formes étiologiques ; **LACUNE** stades (aucune classification officielle) | pA · e56-3, e56-4, e56-5 | S2, S5, S28 |
| 4. Épidémiologie suisse puis européenne | ✔ ; **LACUNE** prévalence suisse de la carence en vitamine E/K de l'adulte (seule la maladie hémorragique néonatale P53 est chiffrée) | pA · e56-2 | S3, S8, S11, S12, S14, S16, S17 |
| 5. Normal → pathologique | ✔ | pA · e56-3, e56-4 ; pS · e56-s-phys-body, e56-s-bioc-body, e56-s-neuro-body, e56-s-gen-body | S2, S5, S7, S9, S15, S18–S20 |
| 6. Étiologies et facteurs de risque | ✔ | pA · e56-5 | S2, S3, S5–S7, S11, S12, S19, S21, S22 |
| 7. Anamnèse et symptômes | ✔ ; fréquences non chiffrées dans les sources | pA · e56-6 | S2, S3, S5, S6, S14 |
| 8. Examen clinique | ✔ ; sensibilité/spécificité non disponibles | pA · e56-7 | S5, S6, S14, S21, S22 |
| 9. Drapeaux rouges et urgences | ✔ | pA · e56-9 | S2, S18, S24 |
| 10. Examens complémentaires | ✔ | pE · e56-e-1 à e56-e-5 ; pA · e56-8 | S2, S3, S5, S6, S13, S15, S16, S23 |
| 11. Diagnostic différentiel | ✔ | pA · e56-8 | S2, S5, S6, S13, S16 |
| 12. Prise en charge suisse | ✔ ; **LACUNE** posologie adulte de Konakion MM 10 mg (information professionnelle inaccessible), le cours renvoie à l'information en vigueur | pA · e56-10, e56-11, e56-12 ; pP · e56-p-1 à e56-p-5 | S2, S3, S5, S11, S18–S20, S27 |
| 13. Complications et pronostic | ✔ | pA · e56-9 (et e56-0) | S2, S5, S14, S22 |
| 14. Suivi, prévention, dépistage | ✔ | pA · e56-12, e56-13 | S2, S3, S5, S11, S23 |
| 15. Situations particulières | ✔ | pA · e56-13 ; pP · e56-p-3 | S2, S5, S17–S20, S25, S26 |
| 16. Spécificités suisses | ✔ codage SpiGes, catégories de remise, Liste des spécialités (fenêtre e56-sl), prophylaxie, SMOB ; **LACUNE** déclaration OFSP, Suva/LAA, aptitude à la conduite, AI (aucune source ; le cours le dit sans formuler de règle) | pA · e56-14, e56-12, e56-13 | S11, S23, S28, S30 |
| 17. Critères formels du diagnostic | ✔ critères opérationnels (aucun critère officiel : lacune) | pA · e56-15 (`div.alert`) | S2, S3, S5, S6 |
| 18. Paramètres clés chiffrés | ✔ | pA · e56-15 (`div.key`) | S2, S8, S9, S11, S18 |
| 19. Sous-codes CIM-10-GM (E56.0, E56.1, E56.8, E56.9) | ✔ ; E56.8 : aucune vitamine nommée, périmètre par exclusion seulement | pA · e56-14 | S1, S10, S28 |
| 20. Points d'examen fédéral | ✔ SSP 16, 138, 170 (rattachement pédagogique non officiel) et six pièges | pA · e56-14 | S29, S2, S3, S6, S13, S18, S28 |

## Lacunes reprises dans le cours
- E56.8 : aucune vitamine nommée ; le cours ne dresse pas de liste.
- Posologie adulte de Konakion MM 10 mg non sourcée ; aucune recommandation suisse spécifique sur la carence en vitamine E ou K de l'adulte ; aucune prévalence suisse de la carence en vitamine E.
- Classification en stades : aucune. Critères diagnostiques : opérationnels, non officiels.
- Statut SL lu dans une republication (AmiKo), à confirmer sur la Liste des spécialités officielle ; déclaration OFSP, Suva, conduite, AI : sans source.
- GeneReviews AVED et ECFS 2024 non lus ; valeur DGE de la vitamine E (8 mg/jour) issue d'une extraction automatisée ; unités lues par le contexte (« m » mis pour « µ » dans les PDF ESPEN et ECFS), seuil ECFS lu comme 300 µg/dL (fenêtre e56-unites).

## Sources utilisées
Uniquement `recherche.md` et `sources.json` (S1 à S30), dont les trois ajouts du complément : OFS CIM-10-GM 2024 ClaML (S28), PROFILES (S29), AmiKo (S30).

## Auto-contrôle
- Abréviations non couvertes : 0 (`build_medina.audit` avec le glossaire e56 ajouté, hors dépôt).
- Toutes les clés `data-k` ont leur fenêtre, aucune fenêtre orpheline ; identifiants uniques et préfixés `e56` ; couvertures Pareto valides (îlots 13 à 15 couverts par le même bouton) ; HTML bien formé sur a+b+c+d et sur les fenêtres.
- Aucune modification de `chapters/` racine, `glossary/` racine, `chapters.json` ni git.

Audit différé — revue IA, distincte d'une validation médicale humaine.
