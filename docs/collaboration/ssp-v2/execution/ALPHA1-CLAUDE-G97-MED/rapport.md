# Audit médical ALPHA77 — G97, affections du système nerveux après des actes médicaux (S08)

Mission `ALPHA1-CLAUDE-G97-MED`, branche `claude/alpha1/g97-med-g1`, base du manifeste `523832d9`, worktree sur `103745ba`. Audit mené le 16 octobre 2026 par un sous-agent Claude Code, modèle et effort conformes au manifeste. Les sept fichiers figés ont été lus en entier ; leurs empreintes SHA-256 sont **conformes** au manifeste.

## Verdict

La leçon est solide sur l’essentiel. Ses critères ICHD-3, la méta-analyse de l’aiguille atraumatique, les recommandations du consensus de 2023, les chiffres de l’hématome et de la cohorte pédiatrique européenne sont recopiés fidèlement. Quatre points doivent cependant être corrigés avant clôture.

1. **La sémiologie fondamentale et analytique est absente** (C01). Le sous-onglet n’existe pas, et l’onglet 1 énumère des signes sans chronologie chiffrée, sans technique ni raisonnement.
2. **Le contrat des sciences échoue** (C02). `tests/audit_sciences.py` relève 12 erreurs : aucun encadré « Science → clinique / examen / traitement » ni « À retenir ».
3. **Le plafond de 2000 mg/j de paracétamol manque** (C03). L’information professionnelle suisse l’impose en cas d’atteinte hépatique, d’alcoolisme, de malnutrition, de déshydratation ou de cachexie ; une patiente qui vomit après une brèche durale est concernée.
4. **Deux séries allemandes sont présentées comme suisses** (C04). Les cohortes de forme chronique viennent de Fribourg-en-Brisgau, non de Berne ; elles figurent pourtant parmi les « spécificités suisses ».

Aucune erreur ne justifie un constat BLOQUANT. Aucune dose dangereuse n’est prescrite, mais l’omission du plafond hépatique peut conduire à une surdose relative.

## Tableau de bord

| Indicateur | Valeur |
|---|---|
| BLOQUANT / MAJEUR / MINEUR / ENRICHISSEMENT | 0 / 4 / 18 / 4 |
| Occurrences numériques relevées (7 fichiers) | 699, dont 492 valeurs médicales |
| Grandeurs calculables recalculées par script | 76 / 76 |
| CORRECT / ARRONDI / FAUX / NON_VÉRIFIABLE | 41 / 30 / 1 / 4 |
| Contradictions de valeurs entre fichiers | 0 |
| `test_v7.py --static G97` | OK (14 132 mots, 54 fenêtres, 6 quiz, 14 Pareto) |
| `tests/audit_sciences.py` | échec, 12 erreurs |
| Sous-onglet sémiologie | absent (3 `data-s`, aucun `g97-s-semio`) |
| Figures | 3 schémas non anatomiques ; aucune figure anatomique IA |
| Sources de l’audit | 34 : 8 en texte intégral, 5 par sections, 20 en résumé, 1 non relue |

## Constats MAJEURS

**C01 — Sémiologie fondamentale et analytique absente** (`G97_c.html`, `data-s="g97-s-anat"`). La discipline n’existe pas. Les îlots g97-5 et g97-6 ne donnent ni la chronologie réelle (65 % des céphalées dans les 24 h, 92 % dans les 48 h [S31]), ni la manœuvre posturale décrite, ni la cotation motrice de 0 à 5 [S33], ni les quatre domaines du syndrome de mutisme cérébelleux (parole, troubles émotionnels, ataxie, hypotonie [S18]). *Proposition* : `propositions/G97_c_semio.html` (neuf sections `data-semiology`, trois cas corrigés), `G97_a_semio_clinique.html`, `G97_pop1_semio.html` (cinq fenêtres, à ajouter au `_pop1`), `glossary_g97_ajouts.py`.

**C02 — Contrat des sciences** (`G97_c.html`). Les encadrés s’intitulent « Anatomie → clinique », « Physiologie → traitement », « Preuves → décision ». La discipline « Preuves chiffrées » relève de la biostatistique ; histologie, biochimie et génétique manquent. *Proposition* : `propositions/G97_c_2.html`, avec le mécanisme de vasodilatation compensatrice et l’action de la caféine tirés du texte intégral de la revue de Thon 2024 [S8].

**C03 — Paracétamol : plafond réduit absent** (`G97_d.html`, piège G97-C0315). La FI suisse de Paracétamol Stada® (juillet 2026) écrit : « alcoolisme chronique, déficit d’alimentation chronique […] ou déshydratation […] La dose quotidienne ne doit pas dépasser 2 g » [S21]. Le recalcul K57 donne 2000 mg attendus contre 4000 mg affichés. *Proposition* : `propositions/G97_d_1.html` (tableau, piège, encadré, fenêtre, g97-12).

**C04 — Provenance des séries chroniques** (`G97_b.html`, 11.7). Kraus 2024 est une analyse « retrospective, single center », validée par le comité d’éthique de l’Université de Fribourg [S26]. Zander 2025 réunit 86 patients « from a tertiary medical care center in Freiburg, Germany » [S29]. « Berne » ne désigne que le score d’imagerie. *Proposition* : `propositions/G97_a_1.html` (sept remplacements).

## Constats MINEURS

| N° | Fichier et ancre | Constat |
|---|---|---|
| C05 | `_a` G97-C0076 | La certitude est élevée, non modérée, pour l’aiguille coupante et son calibre. La phrase « l’expérience de l’opérateur augmente le risque » dit l’inverse de la source [S5]. |
| C06 | `_a` G97-C0076 | « Niveau de ponction sans effet » : la source parle seulement du niveau d’insertion d’une péridurale [S5]. |
| C07 | `_b` 9.1 | Le cathéter intrathécal figure parmi les mesures de prévention, alors que son effet préventif n’est pas démontré [S5]. |
| C08 | `_b`, `_d`, `_pop2` | Le bloc occipital est indiqué après une rachianesthésie à l’aiguille de 22 G ou plus fine. La formule « 22 G ou moins » est ambiguë [S5]. |
| C09 | `_b`, `_c`, `_pop2` | La probabilité de 50 % se lit 16 jours après le **début** du mutisme. « Amélioration de 50 % » prête à confusion [S16]. |
| C10 | `_a` G97-C0078 | Le chiffre de 64 % d’hydrocéphalie porte sur 800 enfants (515/800), non sur la cohorte de 376 [S18]. |
| C11 | `_b` G97-C0473 | 20,4 % = 11/54 et 21,4 % = 12/56 : les étiquettes du résumé sont probablement inversées. Le point reste NON_VÉRIFIABLE sans le texte intégral [S28]. |
| C12 | `_a` G97-C0062 | L’IC publié pour l’anticoagulation (0,6–8,4 %) ne contient pas l’estimation de 0,44 %. Conclure « ne modifie pas » est donc fragile ; l’étude ne compte que les hématomes évacués [S10]. |
| C13 | `_c` G97-C0478 | Le dénominateur est 9/83, non 86 [S29]. |
| C14 | `_a`, `_b`, `_pop2` | « Sans augmenter la fuite » est inexact : le RR vaut 1,34 (0,83–2,14). La différence est non significative, ce qui ne démontre pas une absence d’effet [S20]. |
| C15 | `_pop2` G97-C0491 | Les définitions de l’échec diffèrent entre Genève et EPiMAP [S24 ; S27]. |
| C16 | `_d`, `_pop2` | Peyona® est une FI suisse de caféine seule, limitée à l’apnée du prématuré. Le mécanisme d’action de la caféine est désormais sourcé [S32 ; S8]. |
| C17 | `_d` alert p-3 | Deux mentions manquent pour l’ibuprofène : l’antécédent de bronchospasme après acide acétylsalicylique et la mise en garde dès la 20e semaine de grossesse [S22]. |
| C18 | `_b` 11.7 | Les codes O29.4, O74.5 et O89.4 classent la céphalée après rachianesthésie ou péridurale chez la femme enceinte, en travail ou en post-partum [S34]. |
| C19 | `_pop1`, `_c` | La phrase « s’applique aux adultes et aux enfants » ne figure pas dans l’ICHD-3 lue [S2]. |
| C20 | `_d` p-2 | La dose par prise de l’enfant de 9 à 12 ans est 400 à 600 mg, avec un intervalle de 6 à 8 h [S21]. |
| C21 | `_c` figures 1–3 | Le texte des figures mesure environ 7,3 à 7,8 px à 390 px ; la légende de la figure 1 est rognée. *Proposition* : `G97_c_figures.html`. |
| C22 | `_pop2` G97-C0421 | Le consensus propose les AINS à tout patient sans contre-indication ; il ne vise pas spécifiquement le post-partum [S5]. |

## Enrichissements

- **C23** : le mécanisme de la céphalée (baisse de pression et de volume, vasodilatation compensatrice, mécanisme exact inconnu) est disponible [S8].
- **C24** : la chronologie chiffrée est disponible (65 % des céphalées dans les 24 h, 92 % dans les 48 h, durée moyenne de 5 jours) [S31].
- **C25** : la définition complète du syndrome de mutisme cérébelleux est disponible [S18].
- **C26** : les intervalles ESAIC/ESRA sont décisionnels mais restent illisibles (HTTP 402). Aucun chiffre n’a été proposé de mémoire.

## Calculs (exigence « ne laisse rien passer »)

Le script `calculs/verifier.py` relève 699 occurrences numériques et les classe : 492 valeurs médicales, 78 dates, 70 numérotations, 51 codes ou rubriques et 8 âges de vignette. Il recalcule ensuite les 76 grandeurs calculables : différence absolue, nombre à traiter par deux méthodes, cohérence des RR et OR avec leurs IC, pourcentages à partir des effectifs, sommes, proportions de la figure 3, posologies par prise et par jour, conversion du seuil de pression et cohérence temporelle des six cas. Les 275 valeurs rapportées non calculables ont été confrontées aux sources lues.

| Verdict | Nombre | Détail |
|---|---|---|
| CORRECT | 41 | dont différence de 6,8 points, 113 + 113 + 110 = 336, 70 000 × 10⁶/L = 70 × 10⁹/L |
| ARRONDI | 30 | dont nombre à traiter 14,7 ≈ 15 (15,2 par le RR), 112/376 = 29,8 % ≈ 30 %, 229/591 = 38,7 % |
| FAUX | 1 | K57 : plafond de paracétamol de 4000 mg appliqué à une population limitée à 2000 mg (C03) |
| NON_VÉRIFIABLE | 4 | K30 (dénominateur EPiMAP de 19,8 %), K37 (C11), K43 et K44 (IC incohérents de la source, C12) |

`recalcules = calculables = 76` : l’audit des calculs est clos.

## Matrice des 20 rubriques

| Rubrique | Statut | Ancre ou remarque |
|---|---|---|
| 1. Question clinique | couvert | g97-0, 11.8 |
| 2. Périmètre CIM-10-GM | partiel | g97-cim ; renvoi obstétrical absent (C18) |
| 3. Classifications | couvert | ICHD-3 7.2, 7.2.1 et 7.2.2 conformes |
| 4. Épidémiologie | partiel | provenance bernoise erronée (C04) |
| 5. Normal → pathologique | partiel | mécanisme disponible (C23) |
| 6. Facteurs de risque | couvert | certitudes à corriger (C05, C06) |
| 7. Anamnèse et fréquences | partiel | C24, C25 |
| 8. Examen clinique | partiel | C01 ; sensibilité et spécificité non publiées |
| 9. Drapeaux rouges | couvert | g97-8 |
| 10. Examens | couvert | C13 |
| 11. Différentiel | couvert | g97-7.4, g97-e-3 |
| 12. Prise en charge suisse | partiel | C03, C17, C26 |
| 13. Complications et pronostic | couvert | réserves C09, C11 |
| 14. Suivi et prévention | couvert | g97-10 |
| 15. Situations particulières | partiel | grossesse (C17), sujet âgé non documenté |
| 16. Spécificités suisses | partiel | C04 ; lacunes déclarées |
| 17. Critères formels | couvert | g97-12 alert |
| 18. Paramètres clés | partiel | C03, C09 |
| 19. Sous-codes | couvert | quatre sous-codes donnés par leur seul libellé |
| 20. Examen fédéral | partiel | PROFILES non consulté |

## 21 — Sémiologie fondamentale et analytique

**Statut : absente, constat MAJEUR, bloquant pour la clôture du cours** (C01). La grille donne SEM-01 à SEM-03 non, SEM-04 oui (`test_v7` OK), SEM-05 à SEM-12 non (SEM-10 partiel), SEM-13 et SEM-14 partiels, SEM-15 à SEM-17 non, SEM-18 à SEM-21 non évaluables, SEM-22 et SEM-23 non, SEM-24 oui. La proposition respecte le contrat `SEMIOLOGIE_FONDAMENTALE_ANALYTIQUE_2026-10-15.yaml` : bouton `g97-tab-semio` en tête de barre, panneau `g97-s-semio`, neuf sections, un tableau des signes et un tableau des syndromes, raisonnement en cinq étapes, examen systématique en neuf temps, synthèse présentée et trois cas corrigés, dont un sur la formulation honnête d’une limite. Les fenêtres vont dans le `_pop1`. Aucune sensibilité ni spécificité n’a été trouvée : la proposition l’écrit, conformément à SEM-08.

## Lacunes principales

- Aucune source suisse de sémiologie ni de recommandation propre au sujet.
- Le texte intégral ESAIC/ESRA 2022 (HTTP 402) et la définition Delphi du mutisme (Springer) sont restés inaccessibles.
- Plusieurs sources n’ont été lues qu’en résumé (voir `sources.json`).
- Le résumé de Weiss 2025 ne permet pas d’attribuer les pourcentages aux groupes.
- Le codage hors grossesse en G97.0 ou en G97.1 n’a pas été vérifié dans l’index alphabétique.
- La lisibilité des figures a été calculée, non mesurée au navigateur ; aucune capture n’a été prise.

*Audit IA — revue distincte d'une validation médicale humaine ; aucune source canonique modifiée.*
