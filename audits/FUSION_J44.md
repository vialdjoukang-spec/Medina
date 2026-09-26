# J44 — Journal de fusion Claude × Alpha (26 septembre 2026)

**Chapitre** : J44 Bronchopneumopathie chronique obstructive (couvre J43 et J44).
**Base** : version Alpha (7 fichiers, dont `J44_pop3.html`), corrigée par son audit du 25–26.09.2026 (`_alpha/audits/J44.md`).
**Méthode** : comparaison mot à mot de chaque îlot, fenêtre et Pareto ; restauration dans la base Alpha de tout contenu Claude exact, utile et cohérent ; refus de tout contenu Claude correspondant à une correction volontaire de l'audit Alpha ou redondant ; vérification web des chiffres restaurés (moteur de recherche ; goldcopd.org, PubMed Central et compendium.ch étant bloqués par le proxy, voir réserves).
**Contrôle** : `python3 test_v7.py --static J44` → **OK** — 10 256 mots (Claude 7 591, Alpha 9 675), **50 fenêtres**, 4 quiz, 7 Pareto ; aucune abréviation non couverte, toutes les fenêtres existent, clés préfixées, ratios Pareto valides (îlots existants).

## 1. Tableau des sections

Mots = texte visible de l'îlot ou de la fenêtre (balises exclues). « Fusion » = version livrée.

| Section | Mots Claude | Mots Alpha | Mots fusion | Décision | Justification |
|---|---|---|---|---|---|
| En-tête `chap-head` / `status` | — | — | — | Alpha + fusion | Code identique. Statut réécrit : « Révision du 26.09.2026 (fusion) », GOLD 2026 (novembre 2025, v1.3 du 8.12.2025), déclaration GOLD/GLI de mars 2026, Ligue pulmonaire et OFSP rétablis, « audit indépendant en attente · non validé par une revue humaine ». |
| j44-0 Question clinique | 210 | 221 | 221 | Alpha | « Deux seules mesures prouvées sur la survie… » simplifiait à l'excès (signaux de mortalité IMPACT/ETHOS) : correction volontaire de l'audit Alpha. |
| j44-2 Épidémiologie | 184 | 226 | 282 | Alpha + 2 restaurations vérifiées | Restauré : sous-diagnostic chiffré (81 % des BPCO spirométriques non diagnostiquées, Lamprecht, Chest 2015) et tabagisme suisse (24 % des 15 ans et plus, Enquête suisse sur la santé 2022). Refusé : « trois premières causes de décès » (rang OMS instable : 4ᵉ en 2021 dans la fiche OMS), « mortalité ~20 % dans l'année » (chiffre retiré par l'audit), VNI « réduction de mortalité » (raccourci HOT-HMV corrigé). |
| j44-4 Facteurs de risque | 155 | 157 | 191 | Alpha + restauration corrigée | Claude : « environ 15 % des BPCO ». Alpha l'avait retiré comme non vérifié. Vérifié : fraction attribuable **14 % (IC 95 % 10–18 %)**, déclaration officielle ATS/ERS 2019 (Blanc et al.). Valeur exacte et source restaurées. |
| j44-5 Anamnèse | 258 | 297 | 358 | Alpha + restaurations | Alpha ajoute 13 mots verts vers des fiches (antécédents et signes fonctionnels). Détails Claude rétablis : dyspnée « persistante, aggravée au fil des années » ; toux « souvent le premier symptôme… toux du fumeur » ; expectoration « habituellement muqueuse » ; sifflements « variables d'un jour à l'autre » ; signes généraux (perte musculaire, anxiété, dépression, cancer bronchique) ; comorbidités métaboliques (renvoi à l'îlot 11). |
| j44-6 Examen clinique | 181 | 250 | 250 | Alpha | Alpha contient tout le texte Claude plus le bloc 6.1 (8 fiches d'examen). Rien à restaurer. |
| j44-7 Démarche diagnostique | 271 | 298 | 360 | Alpha + restaurations | Accord GOLD/GLI de mars 2026 conservé (vérifié). Restauré : doses du test (400 µg de salbutamol, 160 µg d'ipratropium ou les deux ; cohérent avec l'îlot 1), préférence ERS/ATS pour la limite inférieure de la normale, surdiagnostic chez le sujet âgé et sous-diagnostic chez le jeune par le seuil fixe (vérifié), motif de la répétition entre 0,60 et 0,80 (variabilité, autre visite). |
| j44-8 Exacerbation | 549 | 570 | 637 | Alpha + restaurations | Alpha retenu pour `pH ≤ 7,35` (formulation GOLD et ERS/ATS) et « persistante après traitement initial ». Restauré : équivalence 6,0 kPa ; « d'après la proposition de Rome » ; résultat de REDUCE (non-infériorité de 5 jours contre 14, essai suisse 2013) ; choix empiriques habituels selon GOLD et aide de la CRP ; seuils et danger de l'oxygène à haut débit dans la correction du quiz. Refusé : « bénéfice plus grand si éosinophiles ≥ 300/µL » pour la corticothérapie systémique (retiré par l'audit), « intensifier » remplacé par « réévaluer ». |
| j44-9 Traitement de fond | 374 | 490 | 499 | Alpha + précision | Restauré : réhabilitation pour les groupes B et E (GOLD : symptômes et/ou risque élevé d'exacerbation). Refusé : « 6 à 12 semaines » (GOLD 2026 : bénéfice optimal à 6–8 semaines, correction volontaire) ; formule absolue sur CSI + BALA (nuance Alpha conservée). Encadré « Application en Suisse » conservé (limitation Trelegy vérifiée). |
| j44-10 Stade avancé | 232 | 285 | 318 | Alpha + restauration réattribuée | HOT-HMV : PaCO₂ > 53 mmHg et critère combiné (Alpha, exact). Restauré le seuil Claude **≥ 52 mmHg** sous sa vraie source : GOLD, survie sans réhospitalisation après hospitalisation récente en cas d'hypercapnie diurne persistante marquée. Refusé : « réduit réadmissions et mortalité (HOT-HMV) ». |
| j44-12 Situations particulières | 202 | 244 | 266 | Alpha + restaurations | Cas récapitulatif Alpha (AMLA + BALA, trithérapie à discuter selon la limitation suisse) retenu : l'indication et la limitation suisses de Trelegy exigent un traitement préalable. Restauré : surestimation de l'obstruction par le seuil fixe chez le sujet âgé ; trithérapie « de préférence en un seul inhalateur ». Refusé : « après 70 ans » (âge non sourcé). |
| j44-13 Critères formels + références | 298 | 325 | 476 | Alpha + restaurations | Restauré : « (GOLD 2026) », exemples de symptômes et de facteurs de risque, mention ERS/ATS, exclusion de la bronchiolite oblitérante. Références : liens Alpha conservés ; titres complets Claude (Rome, ERS/ATS 2022), Ligue pulmonaire suisse et objets du rapport GOLD 2026 rétablis ; ajout des sources des chiffres restaurés (Blanc 2019, Lamprecht 2015, Office fédéral de la statistique). |
| j44-e-2 Spirométrie et volumes | 188 | 302 | 321 | Alpha + restaurations | Figure Alpha à axes gradués retenue. CPT comparée aux limites de référence (Alpha, ERS/ATS 2022). Restauré : préférence ERS/ATS pour la limite inférieure de la normale ; DLCO habituellement normale dans l'asthme et la bronchite chronique sans emphysème. Refusé : « CPT > 120 % = distension » comme seuil (gardé comme repère d'usage dans le glossaire). |
| j44-sa Anatomie (−9 mots chez Alpha) | 115 | 106 | 118 | Alpha + légende complétée | Pourquoi −9 : Alpha a raccourci les trois étiquettes du SVG (« : centre de l'acinus », « : acinus entier », « : périphérie, sous la plèvre ») pour supprimer un chevauchement, et reporté le sens dans une légende plus courte. Fusion : étiquettes courtes gardées, légende rétablie avec la correspondance type → localisation. |
| j44-p-1 Classification | 148 | 161 | 161 | Alpha | Même contenu ; Alpha sépare la stratégie GOLD des limitations suisses. |
| j44-p-2 Doses | 140 | 221 | 221 | Alpha | Refusé : roflumilast « 250 µg pendant 4 semaines » (Daxas suisse : 500 µg une fois par jour après le petit déjeuner, correction volontaire) ; azithromycine « un an ou plus » (hors indication suisse). |
| j44-p-3 Sécurité | 211 | 230 | 234 | Alpha + restauration | Contre-indications suisses du roflumilast (insuffisance hépatique modérée à sévère, grossesse, allaitement) confirmées. Restauré : exemple de la rifampicine. |
| Fenêtre j44-cat | 44 | 67 | 73 | Alpha + précision | Renommage CAT → CAAT confirmé ; nom employé par GOLD 2026. (Année « 2025 » ajoutée à la fusion puis retirée après contre-lecture : non sourcée, le nom CAAT figure déjà dans une publication de 2023 ; voir § 7.) |
| Fenêtre j44-gaz | 76 | 88 | 88 | Alpha | `≤ 7,35`, persistance, confirmation de l'hypoxémie. |
| Fenêtre j44-vni | 52 | 69 | 69 | Alpha | Idem ; ajout du choix du mode et du lieu. |
| Fenêtre j44-rehab | 53 | 91 | 103 | Alpha + restauration | Restauré : programmes ambulatoires et hospitaliers reconnus par la Société suisse de pneumologie (vérifié). Refusé : 6–12 semaines. |
| Fenêtre j44-d-triple | 53 | 82 | 82 | Alpha | Limitation suisse ajoutée par Alpha ; preuves IMPACT/ETHOS identiques. |
| Pareto clin | 122 | 140 | 140 | Alpha | Même couverture (`j44-0` à `j44-6`) ; formulation pronostique corrigée. |
| Pareto diag | 57 | 68 | 75 | Alpha + restauration | Restauré : « en état stable », « 400 µg de salbutamol ». |
| Pareto exa | 66 | 72 | 72 | Alpha | Cohérent avec j44-8 (`≤ 7,35`, persistance). |
| Pareto tt | 79 | 105 | 105 | Alpha | Nuance CSI + BALA. |
| Pareto crit | 83 | 109 | 109 | Alpha | HOT-HMV sur critère combiné. |
| Pareto exam | 69 | 82 | 82 | Alpha | Plus de seuil fixe de CPT. |
| Pareto pharma | 62 | 62 | 62 | identique | — |
| 20 fiches sémiologiques `j44-a-*`, `j44-s-*`, `j44-p-*` (J44_pop3.html) | 0 | 1 197 | 1 197 | Alpha ajouté | Absentes de Claude ; exactes ; clés préfixées ; exigence « chaque antécédent et chaque signe cliquables ». |
| Autres îlots et fenêtres (j44-1, 3, 11, e-1, e-3 à e-6, sp, sb, sg, 22 fenêtres) | = | = | = | identiques | Aucune divergence. |

## 2. Glossaire `glossary/j44.py`

- **Union des clés** : les 32 clés Claude (20 appels `a()` et 12 essais `t()`) + `CAAT` (Alpha), soit 33 clés. Aucune clé perdue. (Décompte corrigé après contre-lecture ; voir § 7.)
- **CPT** (conflit) : définition Alpha (limites de référence, restriction sous la limite inférieure) fusionnée avec l'information Claude : distension au-dessus de la limite supérieure de la normale, « le repère de 120 % de la valeur prédite reste souvent employé », pléthysmographie préférable en présence d'obstruction.
- **HOT-HMV** : définition corrigée pour la cohérence avec le cours (critère combiné réadmission ou décès, 4,3 contre 1,4 mois, PaCO₂ > 53 mmHg, pas de preuve isolée sur la mortalité) ; l'ancienne formule « moins de réadmissions » était reprise dans les deux versions.
- **CAT** : mention du nom actuel CAAT, employé par GOLD 2026, scores interchangeables (année de renommage retirée après contre-lecture ; voir § 7).

## 3. Restaurations (contenu Claude réintroduit dans la base Alpha)

1. Sous-diagnostic chiffré de la BPCO (j44-2), avec source vérifiée (Lamprecht 2015 : 81,4 %).
2. Tabagisme en Suisse, 24 % des 15 ans et plus en 2022 (j44-2), daté et attribué à l'Office fédéral de la statistique.
3. Fraction attribuable professionnelle, corrigée de « environ 15 % » à **14 %** (IC 95 % 10–18 %, ATS/ERS 2019) (j44-4).
4. Caractéristiques sémiologiques : dyspnée persistante et progressive, toux premier symptôme, expectoration muqueuse, sifflements variables, perte musculaire, anxiété-dépression, cancer bronchique, comorbidités métaboliques (j44-5).
5. Doses du test de bronchodilatation (400 µg de salbutamol, 160 µg d'ipratropium) (j44-7, Pareto diag).
6. Préférence de l'ERS et de l'ATS pour la limite inférieure de la normale (j44-7, j44-13, j44-e-2) et biais du seuil fixe selon l'âge (j44-7, j44-12).
7. Motif de la répétition de la spirométrie entre 0,60 et 0,80 (j44-7).
8. PaCO₂ 45 mmHg = 6,0 kPa (j44-8).
9. Définition de l'exacerbation « d'après la proposition de Rome » (j44-8).
10. Résultat de REDUCE : non-infériorité de 5 jours contre 14 (j44-8).
11. Antibiothérapie empirique habituelle et aide de la CRP (j44-8).
12. Seuils et risque de l'oxygène à haut débit dans la correction du quiz (j44-8).
13. Réhabilitation pour les groupes B et E (j44-9).
14. Seuil GOLD PaCO₂ ≥ 52 mmHg, réattribué à GOLD sur le critère survie sans réhospitalisation (j44-10).
15. Trithérapie « en un seul inhalateur » (j44-12).
16. Critères formels : attribution GOLD 2026, exemples, bronchiolite oblitérante (j44-13).
17. DLCO normale dans l'asthme et la bronchite sans emphysème (j44-e-2).
18. Correspondance type d'emphysème → localisation, dans la légende de la figure 3 (j44-sa).
19. Rifampicine comme inducteur enzymatique (j44-p-3).
20. Reconnaissance des programmes de réhabilitation par la Société suisse de pneumologie (fenêtre j44-rehab).
21. Références : titres complets (Rome, ERS/ATS 2022), Ligue pulmonaire suisse, objets du rapport GOLD 2026 (activité de la maladie, biothérapies, vaccinations).

## 4. Refus (contenu Claude non réintroduit)

| Contenu Claude | Motif |
|---|---|
| « Deux seules mesures prouvées sur la survie » (j44-0) | Simplification corrigée par l'audit Alpha. |
| « Trois premières causes de décès » (OMS) (j44-2) | Rang variable selon l'année (4ᵉ en 2021 dans la fiche OMS) ; « principales causes » suffit. |
| Mortalité « de l'ordre de 20 % » dans l'année suivant une hospitalisation (j44-2) | Chiffre de pronostic retiré par l'audit Alpha, population et période non sourcées. |
| VNI à domicile « réduit réadmissions et mortalité (HOT-HMV) » (j44-2, j44-10, Pareto crit) | Faux pour HOT-HMV (critère combiné) : correction volontaire. |
| Réhabilitation « 6 à 12 semaines » (j44-9, fenêtre) | GOLD 2026 : bénéfice optimal à 6–8 semaines. |
| Corticothérapie systémique « bénéfice plus grand si éosinophiles ≥ 300/µL » (j44-8) | Retiré par l'audit ; les éosinophiles ne sont pas un seuil obligatoire d'administration. |
| Roflumilast 250 µg pendant 4 semaines (j44-p-2) | Non conforme à la présentation suisse Daxas 500 µg. |
| Azithromycine « un an ou plus » (j44-p-2) | Durée des essais ; usage hors indication suisse. |
| CPT « > 120 % : distension » comme seuil (j44-e-2, Pareto exam) | ERS/ATS 2022 : limites de référence ; le repère reste mentionné dans le glossaire. |
| « Après 70 ans » (j44-12) | Âge non sourcé. |
| Trithérapie d'emblée dans le cas récapitulatif (j44-12) | Indication et limitation suisses de Trelegy : traitement préalable exigé ; la trithérapie reste mentionnée comme option GOLD. |
| `pH < 7,35` (j44-8, j44-13, fenêtres) | GOLD et ERS/ATS écrivent `pH ≤ 7,35` ; valeur Alpha homogène dans les quatre onglets, les fenêtres et le Pareto. |
| Figure débit-volume à deux panneaux (j44-e-2) | Remplacée par la figure Alpha à axes gradués (exigence § 4.4). |

## 5. Cohérence interne vérifiée

- Acidose hypercapnique : `pH ≤ 7,35` et `PaCO₂ ≥ 45 mmHg` dans j44-8, j44-13, fenêtres gaz et VNI, Pareto exa.
- HOT-HMV : PaCO₂ > 53 mmHg et critère combiné dans j44-2, j44-10, Pareto crit, glossaire. Le seuil ≥ 52 mmHg n'apparaît que dans j44-10, attribué aux rapports GOLD antérieurs à 2026 et distingué du critère d'inclusion de HOT-HMV (après contre-lecture, § 7).
- Réhabilitation : 6–8 semaines dans j44-9 et la fenêtre.
- Roflumilast 500 µg dans j44-p-2 ; aucune mention restante de 250 µg comme schéma suisse.
- Trithérapie : « option initiale si ≥ 300/µL (GOLD) » + limitation suisse dans j44-9, j44-12, j44-p-1, fenêtre d-triple.
- Seuil spirométrique : `< 0,70` dans un contexte évocateur (GOLD/GLI 2026) partout ; limite inférieure de la normale pour les populations plus larges.
- Pareto : 7 ratios, `data-cover` inchangés et valides.

## 6. Réserves

1. **Collision de glossaire `REDUCE`** (hors de mon périmètre d'écriture) : `glossary/q21.py` définit `REDUCE` (fermeture du foramen ovale, 2017) et, chargé après `j44.py`, écrase la définition BPCO. Dans J44, un clic sur « REDUCE » affiche donc l'essai de cardiologie. À corriger par l'intégrateur (renommer la clé de q21 ou rendre le glossaire propre au chapitre).
2. Clé `ERS` : la définition effective vient de `j18.py` (« co-auteur des recommandations de 2023 pour les pneumonies communautaires sévères ») ; elle n'est pas fausse mais elle est incomplète pour J44.
3. Vérifications faites par moteur de recherche, sans lecture du texte intégral (goldcopd.org, PubMed Central et compendium.ch bloqués par le proxy) : déclaration GOLD/GLI, groupe E GOLD 2026, CAAT, fraction attribuable 14 %, tabagisme 24 %, sous-diagnostic 81,4 %, limitation Trelegy, reconnaissance des programmes par la Société suisse de pneumologie, contre-indications du Daxas. À confronter au texte intégral lors de l'audit indépendant.
4. La phrase GOLD « survie sans réhospitalisation… PaCO₂ ≥ 52 mmHg » est attestée dans des versions antérieures de GOLD ; sa formulation exacte dans le rapport 2026 reste à confirmer.
5. La fenêtre j44-rehab (Alpha) dit « commencée pendant l'hospitalisation ou dans les 4 semaines » : l'effet d'une réhabilitation commencée pendant l'hospitalisation est discuté (essai de Greening, 2014, sans bénéfice sur les réadmissions). À relire contre GOLD 2026.
6. La liste des antibiotiques empiriques est attribuée à GOLD (formulation stable depuis plusieurs éditions) ; à confirmer dans l'édition 2026.
7. Contrôle statique seulement : rendu navigateur, clic sur chaque fiche et débordement mobile non testés dans cette tâche.
8. Statut inchangé : auto-audit, audit indépendant et revue humaine en attente ; aucune note sur 20.

## 7. Corrections après contre-lecture (26.09.2026)

Contre-lecture indépendante de la fusion : 13 écarts signalés, chacun vérifié avant correction. Contrôle final : `python3 test_v7.py --static J44` → **OK** (10 525 mots, **51 fenêtres**, 4 quiz, 7 Pareto) ; `python3 test_v7.py --static J44 Q21` → **OK**.

| # | Écart | Vérification | Décision et correction |
|---|---|---|---|
| 1 | Année « 2025 » du renommage CAT → CAAT (fenêtre j44-cat, glossaire `CAT`, ligne j44-cat du § 1) | Fondé. Le nom CAAT figure dans Tomaszewski et al., *Respiratory Research* 2023 (« Chronic Airways Assessment Test: psychometric properties in patients with asthma and/or COPD ») ; aucune source n'appuie 2025. | **Corrigé** : année supprimée. Fenêtre : « Le questionnaire est désormais nommé Chronic Airways Assessment Test (CAAT), nom employé par GOLD 2026 ; ses scores sont interchangeables avec ceux du CAT. » Glossaire `CAT` aligné. Lignes du § 1 et du § 2 corrigées. |
| 2 | Collision de la clé `REDUCE` (q21.py) | Fondé à l'origine, **déjà résolu** hors de mon périmètre : `glossary/q21.py` définit désormais la clé `Gore REDUCE` ; `B.G['REDUCE']` renvoie la définition BPCO (« 5 jours de prednisone non inférieurs à 14 jours »). | Aucune modification dans J44. Contrôle `--static J44 Q21` : OK. Réserve 1 du § 6 levée. |
| 3 | Seuil PaCO₂ ≥ 52 mmHg attribué à GOLD sans version (j44-10) | Fondé. Formulation retrouvée par moteur de recherche dans des éditions antérieures (dont le rapport 2018) ; texte 2026 inaccessible (goldcopd.org bloqué). | **Corrigé** (§ 12.3) : « Les rapports GOLD antérieurs à l'édition 2026 (formulation non confirmée dans le texte 2026) retiennent… (PaCO₂ ≥ 52 mmHg). Les deux seuils ne s'opposent pas : 53 mmHg est le critère d'inclusion de l'essai HOT-HMV, 52 mmHg le repère de sélection proposé par GOLD. » Fourchette « 2019 à 2025 » proposée par la contre-lecture non retenue : non vérifiée. |
| 4 | Repère de 120 % dans le glossaire `CPT` | Fondé (contradiction de ton avec j44-e-2 et le Pareto exam). | **Corrigé** : « (un repère historique de 120 % de la valeur prédite est parfois cité ; il ne remplace pas la limite supérieure de la normale) ». |
| 5 | Fenêtre j44-d-roflu : dépression qualifiée de contre-indication, vraies contre-indications absentes | Fondé. Information suisse (pharma-kritik, compendium) : contre-indications = insuffisance hépatique modérée à sévère (Child-Pugh B ou C), grossesse, allaitement ; dépression avec idées suicidaires = mise en garde. | **Corrigé** : rubrique « Contre-indications et précautions » alignée sur j44-p-3 (contre-indications suisses ; déconseillé en cas de dépression avec idées suicidaires ; surveiller poids et humeur). |
| 6 | Tableau 8.3 « Ventilation » et Pareto tt non harmonisés | Fondé. | **Corrigé** : tableau « VNI si acidose hypercapnique persistante après traitement initial (pH ≤ 7,35 et PaCO₂ ≥ 45 mmHg) ; réduit l'intubation et la mortalité ». Pareto tt : « trithérapie d'emblée si éosinophiles ≥ 300/µL (option GOLD ; vérifier l'indication et la limitation suisses de la spécialité) ». |
| 7 | IMC « < 21 » (j44-6) contre « ≤ 21 » (fenêtre j44-bode) | Fondé : BODE attribue 1 point pour IMC ≤ 21 kg/m² (Celli 2004). | **Corrigé** : « ≤ 21 kg/m² : facteur pronostique défavorable, 1 point de l'indice BODE ». |
| 8 | Antécédents métaboliques non cliquables ; redite « fatigue » (j44-5) | Fondé. | **Corrigé** : bouton `j44-a-metab` et nouvelle fiche « Comorbidités métaboliques et osseuses » dans `J44_pop3.html` (questions ; traitement selon les recommandations habituelles ; risque osseux lié aux corticostéroïdes systémiques, à la dénutrition et à l'inactivité ; renvoi à l'îlot 11, sans chiffre nouveau). Second « fatigue » supprimé. |
| 9 | Lamprecht 2015 : population et étendue absentes (j44-2) | Fondé. Vérifié : adultes de 40 ans et plus, 44 sites, 27 pays, 30 874 participants ; 81,4 % non diagnostiqués, de 50,0 % (Lexington) à 98,3 % (Ile-Ife). | **Corrigé** : « chez les adultes de 40 ans et plus de 44 sites dans 27 pays, 81 % … (50 à 98 % selon les sites) ». |
| 10 | Fenêtre j44-rehab : début hospitalier sans nuance (réserve 5) | Fondé. Vérifié : Ryrsø et al., *BMC Pulmonary Medicine* 2018 (début pendant l'hospitalisation ou dans les 4 semaines ; mortalité RR 0,58 [0,35–0,98] ; réadmissions RR 0,47) ; Greening et al., BMJ 2014 (début hospitalier : réadmissions à un an non réduites, HR 1,1 ; mortalité à un an plus élevée, OR 1,74 [1,05–2,88]). | **Corrigé** : méta-analyse datée, nuance de l'essai de 2014 et conduite pratique alignée sur j44-8 (« dans les 4 semaines suivant la sortie »). Les deux références ajoutées dans j44-13 (BMJ écrit en toutes lettres pour le contrôle des abréviations). Réserve 5 du § 6 levée. |
| 11 | Statut « fusion des versions Claude et Alpha » visible ; date des références | Fondé. | **Corrigé** : statut « Révision du 26.09.2026 · référentiel GOLD 2026… » ; références « versions consultées les 25 et 26.09.2026 ». |
| 12 | Définitions partagées hors contexte (`BPCO`, `ERS`, `PaO₂`, `SpO₂`, `AMLA`, `CSI`) | Fondé (valeurs effectives vérifiées), non fautif pour J44. | **Non corrigé ici** (hors périmètre, confié à l'intégrateur). Une redéfinition dans `j44.py` serait sans effet pour `ERS`, `PaO₂`, `AMLA`, `CSI` (fichiers chargés après) et, pour `BPCO` et `SpO₂`, écraserait silencieusement toute correction ultérieure de `cardio_1.py` ou `cardio_2.py` : à traiter dans les fichiers propriétaires ou par un glossaire propre au chapitre. |
| 13 | Décompte des clés du glossaire (§ 2) | Fondé : 33 clés (32 Claude + `CAAT`), identique au nombre de clés Alpha. | **Corrigé** au § 2. |

Réserves restantes : 3 (vérifications par moteur de recherche, sans texte intégral), 4 (formulation GOLD 2026 du seuil de 52 mmHg, désormais attribuée aux éditions antérieures), 6, 7 et 8 du § 6 ; point 12 ci-dessus à la charge de l'intégrateur.


## 8. Levée des réserves en texte intégral (26.09.2026)

Accès réseau ouvert : les réserves du § 6 et du § 7 ont été confrontées aux sources primaires lues en texte intégral ; le détail (point, URL, verdict, correction) figure dans `audits/J44.md`, section « Vérification en texte intégral — 26.09.2026 ».

- Réserve 3 (vérifications par moteur de recherche) : **levée**. Déclaration GOLD/GLI (texte intégral, PMC13084305), groupe E (GOLD 2026, figure 2.13), CAAT (GOLD 2025 et 2026), fraction professionnelle de 14 % (texte intégral de Blanc 2019), sous-diagnostic de 81,4 % (Lamprecht 2015), limitation de Trelegy (compendium.ch), programmes accrédités par la Société suisse de pneumologie (pneumo.ch) et contre-indications de Daxas (information professionnelle suisse) confirmés ou corrigés. Tabagisme : 23,9 % et non 24 %. Contre-indications de Daxas : grossesse et allaitement relèvent de « ne doit pas être administré », non de la rubrique des contre-indications.
- Réserve 4 (seuil de 52 mmHg) : **levée par correction**. « PaCO₂ ≥ 52 mmHg » figure dans GOLD 2019 à 2022 ; GOLD 2023, 2024 et 2026 écrivent « > 53 mmHg ». L’énoncé du § 5 et de la ligne 3 du § 7 (« seuil attribué aux rapports antérieurs à 2026, 52 mmHg repère de sélection GOLD ») est donc remplacé, dans le chapitre, par la formulation de GOLD 2026 (figure 3.17) et la mention datée des éditions 2019 à 2022.
- Réserve 6 (antibiothérapie empirique) : **levée par correction**. GOLD 2026 ajoute la quinolone chez certains patients, précise les indications (purulence et un autre symptôme, culture positive antérieure, ventilation) et retient 5 jours.
- Écarts supplémentaires corrigés lors de cette relecture : sévérité de l’exacerbation (classification de Rome adoptée par GOLD 2026), critères de sortie, oxygénothérapie de longue durée (« deux fois sur trois semaines », « plus de 15 h/jour »), vaccinations (Plan suisse 2026 et recommandation VRS 2026), indication suisse des trithérapies fixes, roflumilast et azithromycine, ipratropium (pas d’aérosol-doseur seul en Suisse), UPLIFT remplacé par POET-COPD pour la comparaison avec un BALA, mortalité d’ETHOS limitée à la dose de 320 µg de budésonide, voyage aérien, chiffre non sourcé de l’expiration forcée retiré.
- Réserves restantes : voir `audits/J44.md` (NEJM 2004, déclarations ATS/ERS 2003 et ERS 2017, site de la Ligue pulmonaire, tous inaccessibles ; contrôle navigateur et revue humaine en attente).
