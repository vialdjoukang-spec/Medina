# Contre-audit Claude — A41 — Sepsis et choc septique de l’adulte (I-03-Infectiologie)

**SHA examiné :** `e3307768ff4c3a6c3af2e790859ff36947c0279d` (branche `origin/codex/a41-corrections-20261008`). **Base auditée :** `39b7ff0`. **Lot :** `livraisons/Livraison Codex/I-03-Infectiologie/lots/2026-10-08-A41/`.

**Empreintes SHA-256 des dix sources examinées**

| Fichier | SHA-256 (16 premiers caractères) |
|---|---|
| A41_a.html | 34a54b45c140cfb3 |
| A41_b.html | b3955084555b603f |
| A41_c.html | fdf9991f19aa9355 |
| A41_d.html | 85c0d9a2e122a11b |
| A41_justifications.json | c47273d990cbbc4e |
| A41_pop1.html | cdb1671a68f9f87d |
| A41_pop2.html | e7093e7453ac0fbe |
| A41_pop_pa.html | f383ad2143982154 |
| A41_pop_sciences_revision.html | dd5ceeba3e8a346f |
| a41.py | f7d9e45c7df4b04d |

**Couverture.** Les quatre panneaux, les 66 fenêtres et les Pareto ont été lus en entier. Les entrées de justification et de glossaire visées par ESP-27 à ESP-32 ont été vérifiées. Les calculs ont été refaits : SOFA 7, NEWS2 13, Henderson-Hasselbalch, règle de Winter, trou anionique, CaO₂/DO₂, débits de noradrénaline et d’argipressine. Les notices suisses ont été relues avec `tools/compendium_fi.cjs` : Noradrenalin Sintetica 67023 et Piperacillin/Tazobactam Labatec 60142. Les références de PubMed citées plus bas ont été vérifiées. Les énoncés de la Surviving Sepsis Campaign 2026 n’ont pas été recontrôlés un par un ; les forces et certitudes sont reprises du texte.

## 1. Bilan des 75 observations

| Priorité d’origine | Levées | Partielles | Non levées |
|---|---:|---:|---:|
| Majeures (10) | 8 | 2 (ESP-03, ESP-18) | 0 |
| Mineures (46) | 44 | 2 (ESP-05, ESP-07) | 0 |
| Éditoriales (19) | 18 | 1 (ESP-16) | 0 |

Le détail de chaque ID figure dans `RETOUR_PAR_ID.json`, avec la preuve et le correctif. Le tableau ci-dessous ne retient que les réserves et quelques fermetures représentatives.

| ID | Statut | Preuve courte |
|---|---|---|
| ESP-01, 02, 04 | levées | A41_c a41-e-1/e-2/e-3 : procalcitonine (PCT) et protéine C réactive (CRP) avec fiches des Hôpitaux universitaires de Genève (HUG) et cinétiques sourcées. Hémocultures : au moins 2 paires, 8–10 mL par flacon selon le Centre hospitalier universitaire vaudois (CHUV), chiffres de Lee et de Cheng, paire couplée de l’Infectious Diseases Society of America (IDSA). Préanalytique CHUV et Hôpital universitaire de Zurich (USZ). |
| **ESP-03** | **partielle (majeure)** | Les normes artérielles Viollier sont attribuées et le bicarbonate standard est séparé. Le bicarbonate qui entre dans la règle de Winter et le trou anionique reste non qualifié. Voir § 2. |
| **ESP-05** | **partielle** | A41_c passe à l’USZ (0,5–2,2 mmol/L). A41_b a41-12 et pop1 a41-lactate gardent « 0,5–1,5 ; > 2,0 (CHUV, 2022) » : la source renvoie une erreur 404 et la plage contredit A41_c. |
| **ESP-07** | **partielle** | L’échographie au lit et la décompression urgente sont faites. La pesée du contraste n’a pas de source. Voir § 3. |
| ESP-11, 12, 13 | levées | Sciences : mécanismes nommés, limites des modèles explicites. Calcul 933 contre 539 mL/min exact. |
| **ESP-16** | **partielle** | Figures 4–7 numérotées. Le bas de A41_c garde « ← Îlot précédent / Îlot suivant → ». A41_d dit « Partie », A41_b « Section ». pop1 a41-sofa garde « détaillés à l’îlot 7 ». |
| ESP-17, 21, 22 | levées | « Pas un plafond universel… jusqu’à 1 µg/kg/min ». Doses exprimées en base. Vérifié sur la notice 67023 : composition sous forme de tartrate, tableaux en noradrénaline base. |
| **ESP-18** | **partielle (majeure)** | L’exemple de perfusion prolongée (NHS Borders) et le Pareto sont corrigés. La règle demandée sur le délai de 24–48 h avant la réduction rénale manque : seule la « première dose » est protégée. |
| ESP-19, 20, 23–26 | levées | Tableau foyer → schéma. Vancomycine et gentamicine avec doses suisses. Mécanismes récepteur → effet. Surveillance de la natrémie et de la force musculaire. |
| ESP-27 à 32 | levées | Limite de l’étude de Bose, modèle de Menguy, chiffres de Mermel-Maki, notice Labatec au lieu de DailyMed. Glossaire SOFA et APROCCHSS corrigé. |
| P1-01 à P1-27 | levées | Exemples : « exactement 2 points », sous-codes A41.0–A41.9 dont A41.51, aldostérone préservée (a41-cortico), sous-groupe de SEPSISPAM, mortalités suisses à 30 % et 40 % séparées. |
| P2-01 à P2-16 | levées | Définition causale, rubrique « Pourquoi » des solutés (chiffres de SMART, BaSICS, PLUS, 6S, SAFE et ALBIOS vérifiés), CAPITA, SOAP II, glycémie 8–10 mmol/L, libellé « Section précédente ». |

Les délégations P1-22 à P1-25 et P1-27 ont été contrôlées directement dans pop_pa et pop2. Elles sont levées.

## 2. ESP-03 (majeure) : bicarbonate actuel ou calculé et gaz du sang

**Constat.** Trois grandeurs différentes portent le même nom.

- **Bicarbonate actuel.** L’analyseur le calcule par Henderson-Hasselbalch à partir du pH et de la PaCO₂ mesurés.
- **Bicarbonate standard.** C’est le bicarbonate recalculé après équilibration à une PCO₂ de 40 mmHg, à 37 °C. Il retire volontairement la composante respiratoire.
- **CO₂ total sérique.** Il est dosé par la chimie, sur le même tube que le sodium et le chlorure.

L’exemple « bicarbonate 12 mmol/L » sert à la fois à la règle de Winter et au trou anionique, sans dire de quelle grandeur il s’agit. Utiliser le bicarbonate standard serait faux dans un trouble mixte : il efface justement la composante respiratoire que la règle de Winter cherche à démasquer.

**Ce que disent les sources.** La règle de Winter (Albert, Dell, Winters, Ann Intern Med 1967;66:312, PMID 6016545) a été établie à partir du bicarbonate plasmatique du patient, et non du bicarbonate standard. Le trou anionique se calcule avec le sodium, le chlorure et le CO₂ total d’un même prélèvement de chimie, et s’interprète avec l’intervalle de cette méthode (Kraut & Madias, Clin J Am Soc Nephrol 2007;2:162-174, PMID 17699401). La Surviving Sepsis Campaign 2021 ne donne aucun intervalle de bicarbonate. Je n’ai trouvé aucune plage suisse publiée et vérifiable du bicarbonate actuel artériel. **Je n’en propose donc aucune : la réserve sur l’intervalle chiffré est maintenue.** Le correctif rend l’absence d’intervalle sans danger.

**Correctif proposé.** Il s’insère dans A41_c a41-e-3 après le tableau, et dans pop_sciences a41-gaz-read.

> « Trois bicarbonates ne se confondent pas. Le bicarbonate actuel est calculé par l’analyseur à partir du pH et de la PaCO₂ du même gaz. Le bicarbonate standard est recalculé à une PCO₂ de 40 mmHg ; il retire la composante respiratoire et ne sert donc ni à la règle de Winter ni à reconnaître un trouble mixte. Le CO₂ total est dosé sur sérum ou plasma avec le sodium et le chlorure. La règle de compensation utilise le bicarbonate actuel du gaz ou le CO₂ total sérique contemporain (Albert et coll. 1967). Le trou anionique utilise le sodium, le chlorure et le bicarbonate d’un même prélèvement, puis l’intervalle publié pour cette méthode (Kraut et Madias 2007). Lorsque le compte rendu ne donne pas d’intervalle pour le bicarbonate actuel, le médecin n’emprunte pas celui du bicarbonate standard. »

Dans l’exemple chiffré, il faut écrire « CO₂ total sérique 12 mmol/L, mesuré avec le sodium et le chlorure ; PaCO₂ et pH du gaz contemporain ». Avec cette mention, la cohérence interne est conservée : 6,1 + log(12/0,6) = 7,40.

**Avis.** Une fois ce texte inséré, ESP-03 peut être fermée. Sans lui, la réserve reste majeure.

## 3. ESP-07 (mineure) : produit de contraste

**Correctif proposé.** Il complète A41_c a41-e-4, en remplacement de « Le choix concret exige le protocole de contraste et l’avis adapté. »

> « Le consensus de l’American College of Radiology et de la National Kidney Foundation (Davenport et coll., Radiology 2020;294:660-668, PMID 31961246) juge le risque d’atteinte rénale imputable au contraste iodé intraveineux très faible lorsque le débit de filtration glomérulaire estimé est d’au moins 45 mL/min/1,73 m². Il considère qu’une prophylaxie par volume isotonique se discute sous 30 mL/min/1,73 m² ou en cas d’atteinte rénale aiguë. Il précise aussi que renoncer à un examen nécessaire peut nuire davantage que le contraste. Les recommandations de la Société européenne de radiologie urogénitale (van der Molen et coll., Eur Radiol 2018;28:2845-2855, PMID 29426991) retiennent les mêmes groupes à risque. Chez un patient septique avec atteinte rénale aiguë, l’équipe documente donc l’indication avec le radiologue et réévalue l’hydratation. Une imagerie qui conditionne le contrôle du foyer n’est pas différée pour la seule créatinine. »

Avant l’insertion, il faut relire les seuils dans le texte intégral de ces deux références. Les seuils ci-dessus figurent dans les résumés. Le choix du produit et la prémédication restent hors du périmètre.

## 4. Nouvelles observations (aucune erreur médicale bloquante)

| ID | Gravité | Repère | Problème et correctif |
|---|---|---|---|
| N1 | mineure | A41_c a41-e-1 ; a41-pct | « Une PCT à 0,2 µg/L appartient à la plage usuelle » laisse croire qu’une valeur de 0,2 µg/L est normale. Chez le sujet sain, la PCT est très basse. Correctif : la valeur reste sous la limite de la fiche HUG, sans prouver l’absence d’inflammation. Texte dans le JSON ; la valeur basale est à relire dans Dandona. |
| N2 | mineure | A41_b 9.6, explication du quiz | « Le seuil de noradrénaline de 2021 **guide** la corticothérapie » contredit le texte de 2026, qui ne fixe plus ce seuil. Écrire « proposé en 2021, que le texte de 2026 ne fixe plus ». |
| N3 | éditoriale | A41_b 7.4, 7.5, 8.1, 9.7, 9.8, 11.8 ; a41-chocs | Les introductions de tableaux paraphrasent les colonnes (règle P1-06), hors de A41_a. |
| N4 | éditoriale | A41_b, références | Mentions de chantier dans le produit : « reste à vérifier pour les rationales », « réécriture pédagogique » (règle P1-21). |

Doses relues sans erreur nouvelle :

- **Noradrénaline :** début à 8–12 µg/min, paliers de 0,05–0,1 µg/kg/min. Débit de 4,2 mL/h à 0,1 µg/kg/min avec 0,10 mg/mL pour 70 kg, conforme au tableau de la notice.
- **Argipressine :** 0,01 à 0,03 UI/min ; la dilution donne 2,25 mL/h à 0,03 UI/min.
- **Hydrocortisone :** 200 mg/j selon la Surviving Sepsis Campaign 2021 ; dose de stress de 100 mg puis 200 mg/24 h selon la recommandation conjointe ESE/Endocrine Society 2024.
- **Pipéracilline/tazobactam :** adaptation rénale conforme à la notice 60142.
- **Vancomycine :** charge de 25–30 mg/kg, AUC de 400–600 mg·h/L.
- **Gentamicine :** 3 à 5 mg/kg/j.
- **Remplissage :** 30 mL/kg, soit 1 800 mL pour Mme R.
- **Critères :** pression artérielle moyenne de 65 mmHg, ou 60–65 mmHg dès 65 ans ; lactate > 2 mmol/L ; critères Sepsis-3, qSOFA, SOFA et Phoenix exacts.

Un point reste à vérifier sans être marqué fautif : la dose de 6–7 mg/kg en dose quotidienne unique attribuée aux recommandations européennes d’urologie 2026.

## 5. Verdict d’injection

**Favorable sous réserves.** Aucune nouvelle erreur médicale bloquante n’a été introduite. Avant l’injection, Codex doit appliquer quatre corrections textuelles :

1. le correctif ESP-03 du § 2 ;
2. l’harmonisation de la plage du lactate dans a41-12 et a41-lactate (ESP-05) ;
3. la phrase sur le délai de 24–48 h de l’adaptation rénale (ESP-18) ;
4. le pager « Îlot » et la mention « l’îlot 7 » (ESP-16).

ESP-07, N1 et N2 sont des réserves mineures qui peuvent suivre dans le même lot. N3 et N4 sont éditoriales. Une fois ces corrections faites et la reconstruction contrôlée, Claude considère A41 comme injectable. Ce verdict ne valide pas la conformité CIM-11 et ne remplace pas les tests techniques.
