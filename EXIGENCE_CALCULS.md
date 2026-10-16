# Exigence CALCULS — audit médical ALPHA77 (ordre de Vial, 16.10.2026 : « ne laisse rien passer »)

S'ajoute au protocole `PROTOCOLE_ALPHA1_CLAUDE.md` (section A). Toute grandeur calculable de la leçon est
**recalculée par un script**, jamais vérifiée de tête. Aucune exception, y compris les quiz, cas corrigés,
fenêtres, tableaux, figures de données, Pareto et paramètres `div.key`.

## 1. Inventaire exhaustif (script obligatoire)
Extraire par script (regex sur les 7 fichiers) toute occurrence de : nombre + unité (mmol/L, mg/dL, µmol/L,
mL/min/1,73 m², g/kg, mg/kg, UI, mmol/h, mL/h, %, mOsm/kg, mmHg, kPa, g/L…), formule, score, seuil,
débit, posologie, intervalle de dose, conversion d'unités, vitesse de correction, calcul de déficit,
rapport ou pourcentage. Consigner l'inventaire complet dans `calculs/inventaire.json`
(`{id, fichier, ancre, valeur, unite, contexte}`), avec le **nombre total** d'occurrences relevées.

## 2. Recalcul (script `calculs/verifier.py`, exécuté et conservé)
Pour chaque occurrence calculable :
- formule exacte de la source primaire (citée `[Sx]`, section) ; constantes et coefficients exacts ;
- recalcul numérique à partir des données de l'énoncé (cas, quiz) ; tolérance d'arrondi explicite ;
- cohérence d'unités (analyse dimensionnelle) et facteurs de conversion (ex. créatinine µmol/L ÷ 88,4 = mg/dL ;
  glucose mmol/L × 18,016 = mg/dL ; urée ; calcium corrigé ; osmolalité calculée 2 Na + glucose + urée en mmol/L) ;
- bornes physiologiques et cliniques plausibles (valeur normale → pathologique) ;
- posologies : FI suisse datée (dose max/j, par prise, par kg, ajustement rénal ou hépatique, débit IV max,
  concentration max, voie), arrondis aux dosages commercialisés en Suisse ;
- scores (GCS, NIHSS, CHA₂DS₂-VASc, HAS-BLED, Wells, MELD, Child-Pugh, SOFA, qSOFA, KDIGO, eGFR CKD-EPI 2021
  sans coefficient ethnique, Cockcroft-Gault, etc.) : grille officielle lue, chaque item recompté ;
- vitesses de correction (natrémie ≤ 8–10 mmol/L/24 h selon la source, potassium, glycémie, osmolalité) et
  calculs de déficit (eau libre, bicarbonate, fer de Ganzoni…) : formule et hypothèses (poids, eau totale) contrôlées.
Sortie `calculs/resultats.json` : `{id, attendu, trouve, ecart, verdict: CORRECT|ARRONDI|FAUX|NON_VERIFIABLE, formule, source}`.

## 3. Gravité
- `BLOQUANT` : dose, débit, vitesse de correction ou seuil faux pouvant conduire à un geste dangereux.
- `MAJEUR` : résultat de calcul faux, formule erronée ou obsolète, unité erronée, score mal compté.
- `MINEUR` : arrondi incohérent sans conséquence décisionnelle.
- `NON_VERIFIABLE` : données insuffisantes dans l'énoncé → constat MINEUR « énoncé incomplet » avec proposition.

## 4. Rapport
Clé `calculs` dans `rapport.json` : `{total_releves, calculables, recalcules, correct, arrondi, faux,
non_verifiables, script: "calculs/verifier.py"}` ; tableau « Calculs » dans `rapport.md`. Si `faux > 0`,
chaque cas devient un constat avec proposition de remplacement exacte et sourcée. Un audit dont
`recalcules < calculables` n'est pas clos : il le dit explicitement dans `lacunes`.
