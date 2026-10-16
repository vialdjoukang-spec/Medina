# Audit médical ALPHA77 — G81 Hémiparésie et hémiplégie (S08, N-05-Neurologie)

Mission `ALPHA1-CLAUDE-G81-MED` · branche `claude/alpha1/g81-med-g1` · worktree sur la base `103745ba` · sources figées `523832d9` · audit du 16 octobre 2026.
Audit IA — revue distincte d’une validation médicale humaine ; aucune source canonique modifiée.

## 1. Synthèse

Les sept fichiers ont été lus en entier ; leurs empreintes SHA-256 sont identiques au manifeste. La leçon est honnête sur ses lacunes et ses chiffres épidémiologiques sont exactement repris de leurs sources. Elle comporte toutefois **une erreur de dose dangereuse**, plusieurs **omissions décisionnelles** sur la reperfusion et les médicaments oraux, et **aucune sémiologie** : la voie motrice, la cotation de force et la topographie lésionnelle, cœur de l’hémiparésie, sont absentes.

| Gravité | Nombre | Constats |
|---|---|---|
| BLOQUANT | 1 | C01 |
| MAJEUR | 11 | C02 à C12 |
| MINEUR | 13 | C13 à C25 |
| ENRICHISSEMENT | 2 | C26, C27 |

**Calculs** : 582 nombres relevés, 271 occurrences calculables, toutes rattachées à l’un des 62 contrôles scriptés (`calculs/verifier.py`) ; 49 corrects, 1 arrondi, **4 faux**, 8 non vérifiables (tous convertis en constats ou propositions).

## 2. Constats par gravité

### BLOQUANT

**C01 — Plafond cumulé de BOTOX® absent.** Les paramètres clés (`g81-12`), l’îlot `g81-p-2` et la fenêtre `g81-botox` donnent « membre supérieur ≤ 360 U, membre inférieur ≤ 400 U par séance » et un intervalle de 2 mois au membre supérieur. L’information professionnelle suisse (mai 2025) ajoute une règle que la leçon omet : chez l’adulte, la dose cumulée sur 12 semaines ne dépasse pas **400 U**, toutes indications confondues [S15]. Le recalcul K26 montre l’enjeu : deux membres traités ensemble font 760 U, et une réinjection du bras à 2 mois fait 720 U en moins de 12 semaines. La FI rapporte des diffusions à distance parfois mortelles, notamment chez les adultes spastiques traités par fortes doses. Proposition : `propositions/G81_d_botox.html`.

### MAJEUR

- **C02 — Tableau du membre inférieur à 425 U.** La colonne « Dose initiale » additionne sept muscles à 425 U, au-dessus du maximum de 400 U (K25). La FI donne une dose par muscle traité, dans une enveloppe de 300 à 400 U répartie entre les muscles concernés [S15].
- **C03 — Anticoagulant oral direct sans règle.** La patiente de la vignette en prend un, mais la leçon ne dit ni la contre-indication de la FI [S25], ni la règle ESO 2021 : pas de thrombolyse si la prise date de moins de 48 h sans test spécifique ; anti-Xa < 0,5 U/mL : thrombolyse proposée par consensus [S9]. L’heure de prise manque dans l’énoncé (K03) ; la cohorte bernoise de 2023 n’est pas citée [S26].
- **C04 — Altéplase : FI suisse non utilisée.** La FI Actilyse® (juin 2025) fixe le maximum de 90 mg, un bolus de 10 % en une minute et une perfusion de 60 minutes. Elle impose aussi de traiter une pression supérieure à 185/110 mmHg et de corriger une glycémie inférieure à 2,8 ou supérieure à 22,2 mmol/L [S25]. Pour 62 kg, cela donne 5,6 mg en bolus puis 50,2 mg (K04, K05, K57, K58).
- **C05 — Ténectéplase exclue à tort.** Metalyse® 5000 U est autorisé en Suisse dans l’AVC ischémique : 3500 U, soit 17,5 mg, pour 60 à 70 kg, en un bolus unique [S22]. L’ESO 2023 en fait une alternative forte à l’altéplase et la préfère en cas d’occlusion d’un gros vaisseau [S23].
- **C06 — Thrombectomie mécanique absente.** L’ESO–ESMINT 2019 la recommande dans les 6 h (qualité haute) et de 6 à 24 h chez les patients sélectionnés (qualité modérée) [S27].
- **C07 — Sémiologie absente.** L’onglet Sciences ne contient aucun sous-onglet `g81-s-semio`, et la grille SEM compte 22 « non » sur 24 (voir § 4).
- **C08 — Baclofène et rein.** La leçon limite la prudence à l’insuffisance rénale terminale. Or la FI signale une encéphalopathie toxique au-delà de 5 mg/j chez l’insuffisant rénal, et prévoit un début vers 5 mg/j chez l’hémodialysé [S20]. La dose initiale standard de 15 mg/j atteint le triple de ce seuil (K34).
- **C09 — Tizanidine sans surveillance.** La FI impose un contrôle hépatique mensuel pendant 4 mois dès 12 mg/j, ce qui couvre toute la plage optimale citée (K32). Elle signale aussi l’interaction avec les antihypertenseurs, avec hypotension puis rebond [S16].
- **C10 — Définition déclarée absente à tort.** Les sources de sémiologie définissent l’hémiplégie comme une paralysie totale et l’hémiparésie comme une paralysie incomplète, avec une cotation de 0 à 5 [S28].
- **C11 — Voie motrice et topographie absentes.** La leçon ne parle ni d’atteinte corticale non proportionnelle, ni d’atteinte capsulaire proportionnelle, ni de syndromes alternes, ni de Brown-Séquard homolatéral [S28]. Le mot « controlatéral » n’apparaît dans aucun fichier, et le NIHSS n’est jamais nommé.
- **C12 — Sciences hors contrat.** `tests/audit_sciences.py` échoue sur les quatre disciplines : elles sont trop brèves, n’ont aucune figure et ne portent pas les libellés « Science → ». Aucune ne cite de source.

### MINEUR

C13 : pronostic, prévention secondaire et spécificités suisses restent des lacunes. C14 : les chiffres de sécurité des pseudo-AVC portent sur tous les patients, pas sur les seuls thrombolysés (K11). C15 : le rôle vestibulospinal est mineur chez l’homme. C16 : la tizanidine n’agit pas elle-même sur les récepteurs NMDA. C17 : l’AVC du réveil exige une thrombectomie non prévue. C18 : le 39,5 % est une incidence après un premier AVC avec parésie. C19 : les dénominateurs de la série zurichoise sont hétérogènes (K14). C20 : la mention « 3 à 5 séances » n’a pas été retrouvée dans la source (K35). C21 : la FI de Liorésal® prévoit une titration lente dans la spasticité d’origine cérébrale. C22 : l’erratum de l’étude de Genève de 2026 n’est pas mentionné. C23 : les causes d’échec de la toxine figurent dans la FI. C24 : la décomposition littérale de SMNS est incohérente. C25 : un libellé déborde de la figure 1 (K48). Propositions : `propositions/G81_mineurs.html`.

### ENRICHISSEMENT

C26 : doses maximales de Dysport® et de Xeomin selon leurs FI suisses [S29] [S30] (`G81_d_toxines.html`). C27 : points d’examen fédéral de sémiologie (cotation, syndrome pyramidal, face centrale ou périphérique, syndromes alternes).

## 3. Calculs

| Indicateur | Valeur |
|---|---|
| Nombres relevés (7 fichiers, texte visible) | 582 |
| Occurrences calculables (nombre + unité) | 271, toutes rattachées à un contrôle |
| Contrôles scriptés | 62 |
| Corrects | 49 |
| Arrondis | 1 (K48) |
| **Faux** | **4** : K26 → C01, K25 → C02, K34 → C08, K11 → C14 |
| Non vérifiables | 8 : K03, K05, K06, K08, K14, K32, K35, K61 |

Les contrôles corrects couvrent notamment les points suivants. Le délai de la vignette fait 105 min, et la fenêtre se ferme à 11 h 40. La dose d’altéplase donne 55,8 mg, arrondis à 56 mg. Le taux de pseudo-AVC vaut 15 044/60 703, soit 24,8 %. Les sensibilités de Nowak correspondent à 15/17, 11/17 et 8/17. Le rapport de vraisemblance positif des anticorps neutralisants vaut 140. La somme des doses maximales du membre supérieur atteint 360 U, et 6 U/kg font 372 U pour 62 kg. Les schémas de titration de la tizanidine et du baclofène sont cohérents. Les quatre erreurs relevées sont des **erreurs d’omission ou d’attribution** : aucun chiffre de la leçon n’est mal reproduit depuis sa source.

## 4. Rubrique 21 — Sémiologie fondamentale et analytique

Statut : **absente** (MAJEUR, C07). Les sous-onglets réels sont `g81-s-anat`, `g81-s-histo`, `g81-s-physio` et `g81-s-bioch`.

| Critère | Résultat |
|---|---|
| SEM-01, 02, 03 | non (SEM-03 : `audit_sciences` échoue déjà sur les disciplines existantes) |
| SEM-04 | oui, sur la leçon actuelle (`test_v7.py --static G81` OK) |
| SEM-05 à SEM-18 | non |
| SEM-19 à SEM-21 | non évaluables (discipline absente) |
| SEM-22, SEM-23 | non (aucun bouton, aucune capture possible) |
| SEM-24 | oui |

La proposition `propositions/G81_c_semio.html` comporte sept îlots `g81-sm-1` à `-7`, issus de la sémiologie UMVF [S28], de Trompetto [S4], de Nowak [S13], de Pohl [S6] et des FI. Elle couvre :

- les définitions et la cotation de 0 à 5 ;
- le tonus à deux vitesses, les réflexes, la technique du Babinski et la dissociation automatico-volontaire ;
- une figure de raisonnement non anatomique sur quatre étages ;
- les syndromes pyramidal, alterne et de Brown-Séquard ;
- le raisonnement en cinq étapes, l’examen systématique en neuf temps et une synthèse orale ;
- trois cas corrigés, dont un sur la formulation d’une limite.

Elle déclare explicitement les valeurs absentes : aucune sensibilité n’est publiée pour le Babinski, la spasticité ou l’asymétrie faciale. Huit fenêtres l’accompagnent dans `G81_pop_semio.html`.

## 5. Matrice des 21 rubriques

| N° | Rubrique | Statut | Ancre ou constat |
|---|---|---|---|
| 1 | Question clinique | couvert | g81-0 |
| 2 | Définition, CIM-10-GM | partiel | g81-1 ; C10 |
| 3 | Classifications | partiel | g81-1 ; C10, C11 |
| 4 | Épidémiologie | partiel | g81-2 ; C22 |
| 5 | Normal → pathologique | partiel | g81-3 ; C11 |
| 6 | Étiologies | partiel | g81-4 |
| 7 | Anamnèse | partiel | g81-5 ; C03 |
| 8 | Examen clinique | partiel | g81-6 ; C07 |
| 9 | Urgences | partiel | g81-8 ; C03, C04, C06 |
| 10 | Examens | partiel | g81-e-1 à e-4 ; C06 |
| 11 | Différentiel | partiel | g81-7 ; C14 |
| 12 | Prise en charge (FI datées) | partiel | g81-9, g81-p-* ; C01, C04, C05, C26 |
| 13 | Complications, pronostic | partiel | g81-10 ; C13 |
| 14 | Suivi, prévention | partiel | g81-10 ; C09, C13 |
| 15 | Situations particulières | partiel | g81-11 ; C08 |
| 16 | Spécificités suisses | absent | lacune |
| 17 | Critères formels (alert) | partiel | g81-12 ; C10 |
| 18 | Paramètres clés (key) | partiel | g81-12 ; C01, C04 |
| 19 | Sous-codes CIM | couvert | G81.0, G81.1, G81.9 |
| 20 | Points d’examen fédéral | partiel | C27 |
| 21 | Sémiologie | absent | C07 |

## 6. Figures

La leçon contient deux schémas non anatomiques, conformes à la règle des figures, et aucune figure anatomique. La proposition ajoute un seul schéma, lui aussi non anatomique : un arbre de raisonnement d’environ 11,9 px à 390 px.

## 7. Lacunes principales

- **Résumés seuls.** Seuls les résumés de l’ESO–ESMINT 2019, de l’ESO 2023, de Meinel 2023 et de Dziewas 2021 ont été lus. Les critères d’imagerie de la thrombectomie restent à lire.
- **Erratum de Genève 2026.** Son texte est inaccessible (HTTP 403).
- **Aucune source suisse de sémiologie neurologique ni de conduite automobile après AVC.** La seule source européenne de sémiologie retenue date de 2013 (UMVF).
- **Valeurs sémiologiques non chiffrées** dans les sources lues, de même que la grille NIHSS.
- **Captures navigateur non réalisées.** La lisibilité des figures n’a été estimée que par calcul géométrique.

## 8. Tableau de bord

| Élément | Valeur |
|---|---|
| Leçon | G81 — Hémiparésie et hémiplégie (S08, N-05-Neurologie) |
| Fichiers lus / empreintes conformes | 7 / 7 |
| Sources lues | 27 (8 FI suisses en texte intégral ou par section, 5 lignes directrices ESO/ESMINT, 1 cours universitaire, 13 articles, résumés ou notices) |
| Constats | 27 (1 BLOQUANT, 11 MAJEUR, 13 MINEUR, 2 ENRICHISSEMENT) |
| Calculs | 271 occurrences, 62 contrôles, 4 faux, 8 non vérifiables |
| Propositions | 10 fichiers dans `propositions/` |
| Contrôles techniques | `test_v7 --static` OK ; `audit_sciences` en échec (C12) |
| Alerte | **C01 à corriger avant toute republication** de la pharmacologie de la toxine botulique |
