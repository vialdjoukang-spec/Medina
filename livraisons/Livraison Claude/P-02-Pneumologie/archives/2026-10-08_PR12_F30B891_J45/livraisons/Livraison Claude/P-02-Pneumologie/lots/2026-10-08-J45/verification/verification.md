# Vérification indépendante — J45 — Asthme (P-02-Pneumologie)

Copie : `scratchpad/wt_j45` (aucune opération Git). Référence : GINA 2026, rapport complet (mai 2026, PDF intégral `dl_gina/report2026.pdf`, pages imprimées citées) et guide de synthèse (juillet 2026), lus le 08.10.2026 ; figures 9-6 et encadrés 1-2, 4-2, 4-8A/B rendus en image et lus. Sauvegarde avant passe : `scratchpad/qa_j45/before/`.

## A. Erreurs trouvées et corrigées

| Passage | Avant → après | Source |
|---|---|---|
| Magnésium IV pédiatrique : `J45_b` 8.2, `J45_d` 5.4, fenêtre `j45-d-mg`, Pareto `urg` | « enfant de 2 ans et plus : 40–50 mg/kg (max 2 g) en 20–60 min » → « enfant de **2 à 5 ans** » | GINA 2026 : la dose en mg/kg figure seulement dans la section 12 (enfants ≤ 5 ans, p. 225 ; l’encadré 12-4, p. 220, indique 10–20 min) ; la section 9 (6–11 ans) ne donne que « 2 g en 20 min » (p. 188) |
| `J45_d` 5.3 | « aux urgences, GINA indique 1 mg/kg/j sans dépasser 50 mg » → « GINA l’exprime aussi en 1 mg/kg/j, au plus 50 mg » (passage du chapitre soins primaires, pas des urgences) | GINA 2026 p. 180 |
| `J45_d` 4, encadré des interactions CYP3A4 | « le médecin préfère la béclométasone ou le **ciclésonide**, moins dépendants de cette voie » (non sourcé ; le ciclésonide est métabolisé par le CYP3A4) → supprimé ; remplacé par la conduite GINA : ICS seul ou ICS-formotérol pendant le nirmatrelvir-ritonavir + 5 jours, ou autre antiviral ; budésonide- ou mométasone-formotérol pendant l’itraconazole | GINA 2026 p. 132 et 139 |
| `J45_b` 8.3 | « L’hospitalisation **s’impose** si… » → « **se discute** si… » (« Consider admission ») | GINA 2026, encadré 9-6, p. 186 |
| `J45_b` 11.1 | Après exacerbation : « puis dans les 2 à 3 mois » (repère de la section 12, ≤ 5 ans) → « puis régulièrement jusqu’au retour du contrôle » | GINA 2026 p. 189 |
| `J45_b` 9.4 | MART 6–11 ans « option dès le palier 3 » → « aux paliers 3 et 4 » (non recommandé au palier 5) | Encadré 4-8B, p. 91 |
| `J45_a` 4.3 | « étiqueter **non allergique** un patient sous corticostéroïde oral » → « type 2 faible » (le corticostéroïde abaisse les éosinophiles, pas le statut allergique) | Cohérence mécanistique, GINA p. 161 |
| `J45_a` 5.2 | Aggravation après l’effort « presque pathognomonique » → « très distinctive » | Encadré 1-2 (« very distinctive »), p. 28 |

Contrôlés et confirmés sans changement (texte ou figure lus) : critères de l’encadré 1-2 adulte/enfant (réversibilité, DEP > 10/13 %, provocation, effort, entre visites, biomarqueurs FeNO > 50/> 35 ppb), délais de suspension (≥ 4 h ; 24 h ; 36 h ; 36–48 h), algorithme 1-4 (VEMS > / < 70 %) ; classification 9-6 (≥ 94 / ≥ 92 / < 92 % ; DEP > 70 / 50–70 / < 50 % ; FR > 30), menace vitale, salbutamol 4 / 4–6 / 6–10 bouffées, budésonide-formotérol 160/4,5 × 2, ipratropium 4 × 20 µg ou 0,25 mg jusqu’à 3 fois, O₂ < 92 % cible 92–95 %, ≤ 96 % adulte, 93–95 % mieux que 100 %, mortalité plus basse sous O₂ titré (niveau A, p. 180), PaO₂ < 60 + PaCO₂ > 45 mmHg, gazométrie si < 50 %, critères de sortie, suivi 2–7 / 2–5 j, MART palier 4 à la sortie ; prednisone 40–50 mg 5–7 j, enfant 1–2 mg/kg max 40 mg 3–5 j, dexaméthasone 0,3–0,6 mg/kg max 12 mg ; Mg 2 g/20 min ; doses ICS (encadré 4-2, adulte et 6–11 ans) ; AIR/MART (4-8A/B : 12/8 inhalations, 72 µg, béclométasone-formotérol « same advice ») ; AIR −55 %/−65 %/−37 %, MART −32/−23/−17 % ; biothérapies (âges, doses, −44 %, −47–54 %, −56 %, 30–70 %, éosinophilie 4–13 %, > 1 500/µL, 0,2 % anaphylaxie, polysorbate, 4 mois / 6 mois dépémokimab, vaccin pas le même jour) ; LAMA −16–17 %, tiotropium dès 6 ans ; 3–10 % sévère, 65 % changement de catégorie ; seuils 150/300, FeNO ≥ 20 ; épidémiologie (30 %, 16 %, 59 %, RSV ×3, 13 %, 20 % prémenstruel, 96 %, 25–35 %), grossesse (tiers, 2e trimestre, 4–6 sem., 48 h/24 h), chirurgie, réduction 25–50 %, technique 70–80 %, 4–6 semaines, action plan (×4, 3 h), Ligue pulmonaire (1/10, 1/14).

Aucune affirmation médicale nouvelle n’a été créée ; les seuls ajouts sont des phrases d’introduction de tableau ou des renvois internes.

## B. Concision (mots, `wc -w` sur le fichier)

| Fichier | Avant | Après |
|---|---|---|
| J45_a | 5 922 | 5 154 |
| J45_b | 7 225 | 6 618 |
| J45_c | 10 148 | 9 352 |
| J45_d | 7 771 | 6 650 |
| J45_pop1 | 4 570 | 4 137 |
| J45_pop2 | 1 552 | 1 425 |
| J45_pop3 | 2 870 | 2 713 |
| J45_pop4 | 1 689 | 1 694 |
| **Total** | **41 747** | **37 743 (−9,6 %)** |

`test_v7` : 41 401 → 37 340 mots. Redites supprimées : redéfinitions répétées (asthme difficile/sévère dans `J45_b` 10 et `J45_d` 6, renvoi à 1.3) ; pièges doublons (réversibilité/BPCO fusionnés en 7.2) ; exacerbation recopiée dans `J45_d` 5 (oxygène, toxicité, sortie : renvoi à l’îlot 8, doses conservées) ; seuils GINA répétés dans les sciences (`j45-sx`, `j45-sb`) ; « À retenir » qui redisaient les corrélations ; fenêtres qui recopiaient le texte du même onglet (questions de contrôle, critères 1-2, délais de suspension, posologie MART, technique) ; méta-phrases (« le tableau se lit de gauche à droite… ») et infinitifs injonctifs. Doses, seuils, mécanismes, limites, sources et pièges conservés.

## C. Points non vérifiables

- Informations professionnelles suisses (Compendium) : limites MART, ipratropium, Trimbow, montélukast, critères de remboursement — inaccessibles.
- ERS 2017 (catégories PD20, contre-indications de la méthacholine), ERS/ATS 2022 : résumés seulement.
- Incohérence interne de GINA sur la durée de perfusion du Mg chez l’enfant (10–20 min encadré 12-4 ; 20–60 min texte) : texte retenu.
- Préférence de la béclométasone sous inhibiteur du CYP3A4 : non sourcée par GINA, retirée.
- Codage CIM-10-GM du 5e caractère et seuil de pouls paradoxal 25 mmHg : repris des rôles précédents, non relus.

## D. Contrôles (depuis la copie)

- `verifier_sigles.py J45 chapters/J45/*.html` → `{}`
- `test_v7.py --static J45` → `J45 mots 37340 fenêtres 46 quiz 8 pareto 8` puis **OK**
- `insert_justifications.py --course J45 --root .` → 15 fenêtres, **15/15 cibles**
- `build_front.py` → MEDINA.html 16 708 185 octets (9 916 302 compressés, 2 399 gabarits) ; `--all-fragments` → 22 fragments
- `audit_fragments.py` → « audit réussi : 22 fragments, JavaScript valide, build reproductible »
- `verify_course_native.cjs J45` → `{"result":"passed","checks":2282,"failures":0}`
- Identifiants, `data-k`, `data-pop` : aucun perdu ; équilibre des balises identique à l’état d’entrée ; `glossary/j45.py` inchangé ; dernier îlot (alert puis key) et Pareto conservés.

Le cours n’est pas déclaré validé : la revue reste ciblée sur les données à haut risque.
