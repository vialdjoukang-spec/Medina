# Rapport de rédaction — G96 (N-05-Neurologie) — Cycle Betta 41, leçon 1

Agent C41-A1-NEUR (rédaction, Sonnet 5.5), 15.10.2026. Porte de vérité : `python3 tools/betta_verite.py` affichait « VÉRITÉ OK » avant rédaction (26 sources). Mention : **Audit différé — revue IA, distincte d'une validation médicale humaine.**

## Fichiers (sous ce dossier)
| Fichier | Octets |
|---|---|
| `chapters/G96/G96_a.html` (onglet Pathologie, îlots 0 à 8) | 23 583 |
| `chapters/G96/G96_b.html` (Pathologie, îlots 9 à 12 et références) | 24 802 |
| `chapters/G96/G96_c.html` (onglet Examens, onglet Sciences) | 18 271 |
| `chapters/G96/G96_d.html` (onglet Pharmacologie) | 8 737 |
| `chapters/G96/G96_pop1.html` (30 fenêtres de contenu) | 23 815 |
| `chapters/G96/G96_pop2.html` (12 Pareto) | 5 855 |
| `glossary/g96.py` | 5 693 |
| Total | 110 756 |

Environ 11 300 mots, 7 quiz, 2 figures SVG, 42 fenêtres (30 de contenu, dont un moyen mnémotechnique marqué « aide pédagogique, non critère officiel », et 12 Pareto).

## Contrôles (cahier W)
- HTML bien formé (balises équilibrées), identifiants uniques et préfixés `g96-`, chaque `data-k` possède sa fenêtre et chaque fenêtre est appelée, tous les `data-cover` des Pareto existent.
- Essai de construction dans une racine isolée (`build_medina.build`) : `G96 non couvertes: 0`, `audit()` renvoie `{}`. Test navigateur non lancé.
- Glossaire : 17 entrées conditionnelles (ajoutées seulement si la clé est absente des glossaires existants), dont les six codes CIM-10-GM cités (G96.0, G96.1, G96.8, G96.9, G97.0, G97.1). Aucune autre abréviation nouvelle (OFSP, PCV, Hib, AINS, HIS, FLV écrits en toutes lettres).
- Aucun îlot ni tableau consacré au code CIM ; plan monographique classique. Aucune recommandation américaine comme fondement : [S14] et [S15] (origine nord-américaine) ne servent que de données diagnostiques, signalées comme telles.
- Sources citées dans le texte (attribut `data-src`) : S1 à S10, S12 à S26 ; S11 (céphalée post-traumatique) est citée par son nom dans le tableau du diagnostic différentiel.

## Matrice de complétude (reprise du dossier, avec onglet et identifiant HTML)
Onglets : pA = Pathologie, pE = Examens, pS = Sciences, pP = Pharmacologie.

| Rubrique | Statut | Onglet | Identifiant HTML |
|---|---|---|---|
| 1. Question clinique, enjeu examen fédéral | ✔ | pA | `g96-0` (vignette fictive, objectifs) |
| 2. Définition et périmètre CIM-10-GM | ✔ | pA | `g96-1` (définitions, paragraphe CIM-10-GM, rubriques 7.2.1 à 7.2.3 et codage G96.0 / G97.0), fenêtres `g96-ichd`, `g96-his`, `g96-rhino` |
| 3. Classifications et stades | ✔ | pA, pE | `g96-1` (types 1 à 3, score de Berne, rubriques ICHD-3, rhinorrhée traumatique ou non), `g96-e-2` (tableau du score) |
| 4. Épidémiologie suisse puis européenne | ✔ (aucun registre suisse) | pA | `g96-2` |
| 5. Normal → pathologique | ✔ | pA, pS | `g96-3` (Monro-Kellie, preuve bernoise, HIS sans fuite), `g96-s-anat-cours`, `g96-s-physio-cours` |
| 6. Étiologies et facteurs de risque | ✔ | pA | `g96-4` (tableau des facteurs), `g96-1` (arachnoïdite, encadré G96.1) |
| 7. Anamnèse et symptômes (fréquences) | ✔ | pA | `g96-5` (tableau des fréquences) |
| 8. Examen clinique | ✔ (sensibilité/spécificité non disponibles) | pA | `g96-6` |
| 9. Drapeaux rouges et urgences | ✔ | pA | `g96-8` (div.alert, tableau des complications, orientation) |
| 10. Examens complémentaires | ✔ | pA, pE, pS | `g96-7`, `g96-e-1` à `g96-e-6`, `g96-s-bioch-cours` |
| 11. Diagnostic différentiel | ✔ | pA | `g96-7` (tableau, y compris rubriques 7.2.1 et 7.2.2) |
| 12. Prise en charge suisse | ✔ (aucune recommandation suisse dédiée) | pA, pP | `g96-9`, `g96-p-1` à `g96-p-4` |
| 13. Complications et pronostic | ✔ | pA | `g96-8`, `g96-9` (rebond), `g96-10` |
| 14. Suivi, prévention, dépistage | ✔ | pA | `g96-10` (calendrier, vaccination antipneumococcique), fenêtre `g96-vaccin` |
| 15. Situations particulières | ✔ (HIS gravide et pédiatrique = lacune, dite dans le cours) | pA | `g96-11` (tableau enfant, grossesse, insuffisance rénale et hépatique, âgé) |
| 16. Spécificités suisses | PARTIEL | pA, pP | `g96-9` et fenêtre `g96-vaccin` (plan de vaccination 2026), `g96-p-2`, `g96-p-3`, `g96-p-4` (informations professionnelles Swissmedic), `g96-10` (lacune assurantielle et conduite dite explicitement) |
| 17. Critères formels du diagnostic | ✔ | pA | `g96-12` (div.alert : ICHD-3 7.2, 7.2.3, 7.2.1, 7.2.2) |
| 18. Paramètres clés chiffrés | ✔ | pA | `g96-12` (tableau puis div.key final) |
| 19. Sous-codes CIM-10-GM couverts | ✔ | pA | `g96-1` : G96.0 développé en deux volets ; G96.1 (encadré arachnoïdite, fenêtre `g96-arachno`) ; G96.8 et G96.9 déclarés résiduels sans contenu |
| 20. Points d'examen fédéral | ✔ (objectifs PROFILES non consultés) | pA, pE, pP | encadrés « Piège » de `g96-3`, `g96-5`, `g96-6`, `g96-7`, `g96-e-2`, `g96-e-4`, `g96-p-4` ; quiz de `g96-11`, `g96-e-2`, `g96-e-4`, `g96-e-6`, `g96-p-4` ; 12 Pareto |

## Lacunes (reprises du dossier, signalées dans le cours)
1. Aucune recommandation suisse dédiée (Société suisse de neurologie, Swiss Medical Forum) ni européenne (EAN) : base = consensus britannique 2023, revues de Fribourg et d'Oxford, études de l'Inselspital Berne (résumés pour une partie). Dit dans le cours (`g96-9`, sources citées).
2. G96.8 et G96.9 : aucune source clinique ; G96.1 : deux résumés seulement, traité comme repère bref (`g96-1`, `g96-arachno`).
3. Caféine : aucune information professionnelle suisse ; doses de la revue de Fribourg, déclarées hors information professionnelle (`g96-p-1`, `g96-p-4`, `g96-cafeine`).
4. HIS pendant la grossesse et chez l'enfant : aucune source ; aucune conduite proposée (`g96-11`).
5. Risque de méningite de 10 à 37 % dans la rhinorrhée : un seul résumé (`g96-8`, `g96-rhino`). Sidérose superficielle : 1,5 % contre 5 à 10 % selon les sources, présentée comme divergence (`g96-8`).
6. Suva/LAA, assurance-invalidité, liste des spécialités, aptitude à la conduite (hors consigne post-patch) : non trouvés ; dit à `g96-10`.
7. Objectifs PROFILES/SSP non consultés.
8. Colonne méningocoques du tableau de risque du plan de vaccination 2026 ambiguë pour la fistule : divergence avec la revue d'Oxford présentée dans la fenêtre `g96-vaccin`, la règle suisse de 2026 primant en pratique suisse.
9. Techniques du signe du halo, justification physique des séquences d'IRM, origine biochimique de la bêta-2-transferrine : absentes des sources, signalées comme telles et non inventées.
10. Le pourcentage de hausse du volume ventriculaire (18,8 %) est repris des auteurs ; il diffère du calcul sur les moyennes (15,3 à 18,0 mL), ce qui est noté dans le cours.
11. Posologies du paracétamol et de l'ibuprofène : antalgie générale, interactions non retenues dans les extraits ; dit dans `g96-p-4`.

Audit différé — revue IA, distincte d'une validation médicale humaine.
