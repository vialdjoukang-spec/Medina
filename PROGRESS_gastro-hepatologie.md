# PROGRESS — G-04-Gastroentérologie et hépatologie (fragment S03)

Branche : `course/gastro-hepatologie`. Générateur et sources : `livraisons/Livraison Grok/G-04-Gastroenterologie-hepatologie/`.
Statut des cours : rédigés et contrôlés techniquement (abréviations, fenêtres, Pareto) ; **non audités** (audit Claude/Codex et validation médicale à faire).

## Leçons rédigées
| Code | Leçon | Images .gif | Sources principales |
|---|---|---|---|
| K92 | Hémorragies digestives | 3 (Commons) | ESGE 2021, ESGE 2022, Baveno VII, BSG 2019, FI suisses |
| K25 (couvre K26, K27) | Ulcère gastroduodénal | 4 (Commons) | SSI H. pylori 2026, S2k DGVS 2023, ESGE 2021, WSES 2020, FI Nexium® et Pylera® |
| K21 (traite aussi K22.7 Barrett) | Reflux gastro-œsophagien et œsophage de Barrett | 4 (Commons) | S2k DGVS 2023, Lyon 2.0 (2024), ESGE Barrett 2023, FI Nexium®, Pantozol®, Gaviscon® |
| K85 | Pancréatite aiguë | 4 (Commons) | WSES 2019, ESGE 2018 (nécrosante), Atlanta révisée 2012, FI Novalgin®, Palladon® Inject, Meronem® |
| K80 | Lithiase biliaire : colique, cholécystite, calculs cholédociens, angiocholite | 4 (Commons) | EASL 2016, ESGE 2019, WSES 2020, directive suisse KSSG 2026, FI Voltarène®, Co-Amoxi-Mepha®, Ursofalk® |
| K74 | Fibrose et cirrhose du foie (cACLD, hypertension portale, prévention de la décompensation) | 4 (Commons) | Baveno VII 2022, EASL TNI 2021, EASL cirrhose décompensée 2018, Pugh 1973, FI Carvédilol Sandoz® |
| K70 | Maladie alcoolique du foie (stéatose, hépatite alcoolique, cirrhose, trouble de l’usage d’alcool) | 3 (Commons) | EASL 2018 maladie alcoolique, STOPAH 2015, Baveno VII, FI Prednisolone Streuli®, Campral®, Antabus® |
| K50 | Maladie de Crohn | 3 (Commons) | ECCO traitement médical 2024, ECCO-ESGAR 2019, Montréal 2005, STRIDE-II, FI Entocort CIR®, Remicade®, Imurek® |
| K51 | Rectocolite hémorragique | 3 (Commons) | ECCO traitement médical 2022 et chirurgical 2022, Montréal 2005, Truelove et Witts 1955, FI Pentasa®, Cortiment® MMX®, Xeljanz® |
| K52 (centré sur la colite microscopique K52.8) | Autres gastroentérites et colites non infectieuses | 3 (Commons) | UEG/EMCG 2021, FI Entocort CIR® |
| C18 | Tumeur maligne du côlon : cancer du côlon localisé | 3 (Commons) | ESMO côlon localisé 2020, UICC TNM 8 (tableau S1), OPAS art. 12e (01.07.2026), OFS/ONEC 2018-2022, FI Xeloda®, Eloxatine® |
| K35 | Appendicite aiguë | 3 (Commons) | WSES Jérusalem 2020, guide CHUV 2022, FI Co-Amoxi-Mepha i.v., Augmentin® |
| K57 | Maladie diverticulaire : diverticulose et diverticulite aiguë | 3 (Commons, dont 2 aussi dans les fenêtres) | WSES diverticulite 2020, guide CHUV 2022, FI Co-Amoxi-Mepha i.v., Augmentin® |
| K56 | Iléus paralytique et occlusion intestinale sans hernie (brides, occlusion colique, volvulus du sigmoïde) | 4 (Commons, dont 4 aussi dans les fenêtres) | WSES Bologne 2017, WSES volvulus du sigmoïde 2023, WSES urgences du cancer colorectal 2017, FI Paspertin® |
| K90 | Malabsorption intestinale : maladie cœliaque de l’adulte (autres malabsorptions signalées) | 4 (Commons, dont 4 aussi dans les fenêtres) | ESsCD 2025 parties 1 et 2, FI Entocort CIR® |
| K58 | Syndrome de l’intestin irritable | S3 DGVS/DGNM 2021 ; FI Colpermin, Duspatalin, Imodium, Constella, Saroten | 3 images réelles (Bristol, coloscopie, psyllium) ; 15 fenêtres ; règles justification et phrases complètes appliquées |

## Amendements du propriétaire appliqués (09.10.2026)
- Règle linguistique : connecteurs et transitions (`liaisons.py`, plans `chapitres/K92_liaisons.py`, `K25_liaisons.py` ; rédaction native dès K21).
- Règle de précision et d’interactivité : termes interactifs systématiques (`C.termes`, `liaisons.termes`) ; K92 36 → 54 fenêtres, K25 29 → 51, K21 41.
- Règle d’image : schémas générés supprimés (K92 Forrest, K25 profondeur, K21 Los Angeles) et remplacés par des images réelles Commons ; `Schema` désactivé dans `images.py`.

## Restantes (ordre des codes prioritaires du registre)
K58 ; puis les autres catégories de `nosology/fragments/S03.json`.

Priorité examen fédéral (jauge `federal_exam`, 13/89 rédigées au 09.10.2026) — catégories restantes : C15 C16 C17 C19 C20 C21 C22 C23 C24 C25 C26 K20 K22 K23 K26 K27 K28 K29 K30 K31 K36 K37 K38 K40 K41 K42 K43 K44 K45 K46 K55 K59 K60 K61 K62 K63 K64 K65 K66 K67 K71 K72 K73 K75 K76 K77 K81 K82 K83 K86 K87 Q39 Q40 Q41 Q42 Q43 Q44 Q45 R10 R11 R12 R13 R14 R15 R16 R17 R18 R19 S30 S31 S36 T18 T28.
Règles propriétaire ajoutées le 09.10.2026 : RAPPEL VERITE en tête de chaque chapitre ; images réelles aussi dans les fenêtres ; commentaire explicatif (physiopathologie) sous chaque image et tableau ; pas d’îlot ni de tableau consacré aux codes CIM.

## Points ouverts
- K58 : amitriptyline et rifaximine hors indication suisse (doses S3) ; à valider.
- K90 : doses de fer, vitamines et enzymes pancréatiques TODO (absentes des recommandations lues) ; budésonide en capsules ouvertes dans la forme réfractaire hors indication suisse ; justification pharmacocinétique de l’ouverture des capsules non tirée de la source (à vérifier) ; sprue tropicale et syndrome de l’anse borgne non traités (TODO) ; partie 2 ESsCD publiée en 2026 (version PMC lue).
- K56 : dose et produit de contraste hydrosoluble TODO (aucune FI suisse d’amidotrizoate trouvée dans AIPS) ; antiémétique sans effet prokinétique non désigné par les sources (TODO) ; iléus paralytique postopératoire, invagination et iléus biliaire sans recommandation dédiée lue (TODO) ; causes de l’iléus paralytique et onglet Sciences fondés sur des notions classiques, à vérifier ; image du volvulus du sigmoïde issue d’un enfant.
- K57 : co-amoxicilline dans la diverticulite non perforée hors libellé explicite de la FI ; onglet Sciences (points faibles vasculaires, loi de Laplace, Hartmann) fondé sur des notions classiques non tirées des recommandations lues : à vérifier ; hémorragie diverticulaire (K57.x1/x3) seulement mentionnée, renvoi à K92 ; recommandation ESCP 2020 non accessible (pas de PMC).
- K35 : traitement antibiotique premier hors libellé explicite de la FI co-amoxicilline ; composantes des scores AIR, AAS et Alvarado non détaillées (tableaux non lus) ; antibiotiques du traitement premier (molécules, durée 7-10 j des essais) à confirmer par une source suisse ; volet pédiatrique résumé.
- C18 : contentieux CAPOX 3 mois (ESMO) contre 6 mois (FI Xeloda®) ; doses 5-FU/acide folinique de FOLFOX non lues (TODO FI 5-FU) ; recommandation ESMO du cancer métastatique non lue (stade IV seulement nommé) ; K52 : tableau des sous-codes CIM retiré (règle 4 du prompt de vérité).
- K52 : entretien par budésonide hors indication suisse (FI : induction seule) ; rectite radique, colites toxiques et allergiques sans recommandation dédiée lue (TODO) ; dose de lopéramide TODO ; fraction de premier passage du budésonide à confirmer dans la FI.
- K51 : dose des corticoïdes IV et jour d’évaluation de la colite aiguë grave TODO (extraits ECCO chirurgical seulement) ; délai et rythme de la coloscopie de surveillance TODO ; contre-indications FI Pentasa® plus larges que l’ECCO.
- K50 : azathioprine hors indication suisse dans les MICI (FI Imurek®) ; doses d’entretien du risankizumab et de l’upadacitinib TODO (FI non lues) ; ECCO-ESGAR 2019 non téléchargeable (Cloudflare) : règle des biopsies citée de mémoire documentaire, à vérifier à l’audit ; aucune donnée d’incidence suisse.
- K70 : prednisolone hors indication suisse dans l’hépatite alcoolique (recommandée par l’EASL 2018) ; schéma IV de la N-acétylcystéine TODO (non détaillé dans la source) ; baclofène sans autorisation suisse dans le trouble de l’usage d’alcool ; pas de recommandation EASL plus récente que 2018 trouvée.
- K74 : carvédilol préféré par Baveno VII mais hors indication en Suisse et contre-indiqué par la FI si insuffisance hépatique manifeste ; posologie hépatologique du carvédilol TODO (absente des sources lues) ; surveillance du CHC renvoyée au cours C22 (TODO source EASL CHC).
- K80 : litholyse par Ursofalk® autorisée par la FI suisse mais non recommandée par l’EASL 2016 ; délai cholécystectomie après CPRE ≤ 72 h (EASL) vs ≤ 2 semaines (ESGE 2019) ; grille de risque cholédocien WSES adaptée de sources américaines (ASGE/SAGES), signalée.
- K85 : S3 DGVS Pankreatitis 2021 inaccessible (Thieme bloque le téléchargement) : cours fondé sur WSES 2019 et ESGE 2018 ; débit de Ringer lactate ESGE 2018 (5-10 ml/kg/h) antérieur aux essais récents de remplissage modéré, à arbitrer ; hydromorphone préférée par la WSES, sans source suisse spécifique.
- K25 : divergence FI suisses (trithérapie 7 j, IPP 20 mg 2×/j ; Pylera® 10 j) vs SSI 2026 (IPP 40 mg 2×/j, 14 j) : signalée dans le cours, à valider par l’audit.
- K21 : grade B de Los Angeles concluant (Lyon 2.0) vs non concluant (S2k 2023) ; chimioprévention IPP du Barrett (ESGE 2023 oui, S2k non) ; aucune spécialité orale d’anti-H2 trouvée dans AmiKo : signalés dans le cours.
- `preview/lesson-core.js` absent : erreur JS préexistante des aperçus (aussi sur J40), hors périmètre G-04.


## Balayage rétroactif (ordre du propriétaire, 09.10.2026)
Outil : /workspace/sweep/nominal.py (spaCy, détection des phrases sans verbe) puis relecture humaine ; contrôle des images réelles dans les fenêtres, de la justification et des connecteurs.
- K92 : FAIT (10.10.2026). Encadrés, cartes, Pareto, critères formels et 42 fenêtres sur 54 réécrits en phrases complètes ; justification ajoutée (cartes cliniques, signes, mesures du cirrhotique) ; 3 images réelles ajoutées dans les fenêtres Forrest, ligature et varices. Doses et codes inchangés (déjà vérifiés).
- K25 : FAIT (10.10.2026). Encadrés, Pareto, définitions formelles, populations particulières et 46 fenêtres sur 51 réécrits en phrases complètes, avec justification (localisation bulbaire, tests, résistances) ; 3 images réelles ajoutées dans les fenêtres (pneumopéritoine, ulcère/érosion, sténose). Doses et codes inchangés.
- K21 : FAIT (10.10.2026). Définitions formelles, encadrés, Pareto, paramètres clés et 39 champs de fenêtres réécrits en phrases complètes, avec justification (épreuve IPP, prise avant repas, seuils) ; 3 images réelles ajoutées dans les fenêtres (œsophagite, Barrett, sténose). Doses et codes inchangés.
- K85 : À FAIRE (220 phrases signalées par le détecteur avant tri, faux positifs compris).
- K80 : À FAIRE (204 phrases signalées par le détecteur avant tri, faux positifs compris).
- K74 : À FAIRE (127 phrases signalées par le détecteur avant tri, faux positifs compris).
- K70 : À FAIRE (164 phrases signalées par le détecteur avant tri, faux positifs compris).
- K50 : À FAIRE (153 phrases signalées par le détecteur avant tri, faux positifs compris).
- K51 : À FAIRE (153 phrases signalées par le détecteur avant tri, faux positifs compris).
- K52 : À FAIRE (110 phrases signalées par le détecteur avant tri, faux positifs compris).
- C18 : À FAIRE (166 phrases signalées par le détecteur avant tri, faux positifs compris).
- K35 : À FAIRE (122 phrases signalées par le détecteur avant tri, faux positifs compris).
- K57 : À FAIRE (117 phrases signalées par le détecteur avant tri, faux positifs compris).
- K56 : À FAIRE (148 phrases signalées par le détecteur avant tri, faux positifs compris).
- K90 : À FAIRE (108 phrases signalées par le détecteur avant tri, faux positifs compris).
- K58 : À FAIRE (54 phrases signalées par le détecteur avant tri, faux positifs compris).
