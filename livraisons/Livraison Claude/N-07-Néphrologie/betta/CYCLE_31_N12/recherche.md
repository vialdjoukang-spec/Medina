# Dossier de recherche — N12 — Néphrite tubulo-interstitielle, non précisée comme aiguë ou chronique (N-07-Néphrologie)

Cycle Betta 31, leçon 1. Agent de recherche C31-A3-NEPH (Opus 5.5). Consultation : 14.10.2026.
Chaque fait est suivi de sa référence entre crochets ; les identifiants renvoient à `sources.json`. Rien n'est écrit de mémoire ; ce qui n'a pas été lu figure dans « Lacunes ».

## 0. Périmètre nosologique (à respecter par le rédacteur)

- Le bloc N10–N16 « Maladies rénales tubulo-interstitielles » **inclut la pyélonéphrite** ; si une maladie rénale chronique est présente, on ajoute un code N18.- [S1].
- **N12** = néphrite tubulo-interstitielle non précisée comme aiguë ou chronique ; **inclut** : néphrite interstitielle SAI, pyélite SAI, pyélonéphrite SAI. Aucun sous-code ; pas d'exclusion propre [S1, S2].
- Voisins : **N10** néphrite tubulo-interstitielle aiguë (inclut pyélonéphrite aiguë infectieuse ; germe codé par B95–B98) ; **N11.-** chronique (N11.0 reflux, N11.1 obstructive, N11.8, N11.9) [S1].
- Conséquence pédagogique : N12 est un code « d'attente ». Le cours doit enseigner les **deux visages** de la néphrite tubulo-interstitielle : (a) **immuno-allergique/inflammatoire** (néphrite interstitielle aiguë, NIA), (b) **infectieuse** (pyélonéphrite), et la démarche qui permet de préciser aigu/chronique (donc de recoder N10 ou N11).
- Sous-codes CIM-10-GM couverts : N12 (seul code ; source OFS dans `nosology/fragments/S04.json`).

## 1. Question clinique
Devant une insuffisance rénale aiguë (IRA) avec leucocyturie, ou une fièvre avec douleur lombaire, le clinicien doit distinguer l'atteinte interstitielle immuno-allergique (médicament à arrêter, corticoïdes éventuels) de l'atteinte infectieuse (antibiothérapie immédiate) [S3, S4].

## 2. Définition
- NIA (synonyme : néphrite tubulo-interstitielle) : inflammation tubulo-interstitielle et œdème interstitiel d'intensité variable, dont la conséquence principale est l'IRA [S3].
- Décrite en 1898 par Councilman au cours de la diphtérie et de la scarlatine [S3].
- Pyélonéphrite (IU haute) : douleurs de la loge rénale, fièvre, nausées, vomissements, avec pyurie (> 10 leucocytes/mm³) et culture avec uropathogène (≥ 10³ UFC/ml) [S4]. EAU : fièvre > 38 °C, frissons, douleur du flanc, nausées, vomissements ou sensibilité costo-vertébrale, avec ou sans signes de cystite [S7].
- IRA (définition à utiliser) : hausse de créatinine ≥ 26,5 µmol/l en 48 h, ou ≥ 1,5 × la valeur de base dans les 7 jours, ou diurèse < 0,5 ml/kg/h pendant 6 h [S10].

## 3. Classifications
- Selon l'évolution : NIA versus néphrite interstitielle chronique (NIC) ; la NIC est moins documentée, probablement moins fréquente ; causes toxiques et génétiques plus spécifiques de la NIC [S3].
- Selon l'étiologie de la NIA [S3, tableau 1] : médicamenteuse/immuno-allergique **70–75 %** ; maladies systémiques **10–20 %** ; infections **4–10 %** ; autres/idiopathiques **< 5 %**.
- IU selon SSI : « non compliquée » en l'absence d'anomalie structurelle/fonctionnelle, sonde, grossesse, greffe rénale ou immunosuppression ; le diabète bien équilibré n'est pas retenu comme facteur de complication par la SSI [S4].
- EAU 2026 : abandon de la dichotomie compliqué/non compliqué au profit de « IU localisée » versus « IU systémique » [S7].
- Stades KDIGO de l'IRA : 1 = 1,5–1,9 × base ou +26,5 µmol/l, diurèse < 0,5 ml/kg/h 6–12 h ; 2 = 2,0–2,9 ×, < 0,5 ml/kg/h ≥ 12 h ; 3 = 3,0 × ou créatinine ≥ 353,6 µmol/l ou épuration extrarénale, < 0,3 ml/kg/h ≥ 24 h ou anurie ≥ 12 h [S10].

## 4. Épidémiologie
- NIA retenue dans 1–10 % des biopsies rénales tout-venant (moyenne 2,8 %) ; Europe 1–4,7 % [S3].
- Registre espagnol : chez les > 65 ans, hausse de 1,6 à 12,3 % entre 1994 et 2009 (plus de biopsies, consommation d'antibiotiques et d'AINS) [S3].
- Biopsies faites pour élucider une IRA : NIA ≈ 13,5 % en moyenne [S3] ; 15–27 % selon Praga et González [S5].
- VIH : 11–13 % de NIA selon les séries [S3].
- Inhibiteurs de points de contrôle immunitaire (IPCI) : jusqu'à 4,9 % des patients [S3] ; IRA chez jusqu'à 20 % des patients sous IPCI, IRA liée aux IPCI ≈ 2–5 % ; néphrite tubulo-interstitielle dans 80–90 % des biopsies (consensus ADQI) [S12].
- Présentation classique (antibiotiques, rash, fièvre, éosinophilie) largement remplacée par des formes pauci-symptomatiques, surtout chez la personne âgée, avec AINS et IPP [S6].
- Suisse : 20–30 % des isolats urinaires cliniques résistants au TMP/SMX [S4].

## 5. Mécanismes — du normal au pathologique
- Les reins sont exposés aux antigènes endogènes et exogènes par leur débit sanguin élevé, leur activité métabolique et leur surface endothéliale [S3].
- Hypersensibilité retardée, trois phases : reconnaissance/présentation de l'antigène par les monocytes au contact de l'épithélium tubulaire ; phase régulatrice (activation des lymphocytes T) ; phase effectrice humorale [S3].
- Infiltrat (lymphocytes T, macrophages, éosinophiles, plasmocytes) → cytokines → matrice extracellulaire et prolifération fibroblastique → fibrose interstitielle et atrophie tubulaire, **détectables après 7 jours** si le traitement est retardé ; cette étape détermine le déclin rénal à long terme [S3, S5].
- Forme médicamenteuse : indépendante de la dose, récidive à la réexposition, manifestations extrarénales [S3].
- IPCI : rupture de tolérance immunitaire, latence de semaines à mois, persistance malgré l'arrêt [S3] ; activation de lymphocytes T CD8 résidents mémoire, cascade interféron-γ (revue 2026, hors Europe) [S13].
- Douleurs lombaires : distension de la capsule rénale par l'œdème interstitiel [S3].
- Atteinte tubulaire avant la hausse de créatinine possible : acidose métabolique hyperchlorémique, hyperkaliémie, syndrome de Fanconi (glycosurie, phosphaturie, uricosurie, amino-acidurie) dans l'atteinte proximale, défaut de concentration [S3].

## 6. Causes
- Médicaments [S3, tableau 1] : antibiotiques (bêtalactamines dont méticilline, ciprofloxacine, rifampicine, sulfamides, vancomycine, tétracycline, cotrimoxazole), AINS, IPP, diurétiques, IPCI, antiépileptiques ; autres : allopurinol, aciclovir, cocaïne, mésalazine.
- Série de 133 biopsies (1993–2011) : médicaments 70 %, dont antibiotiques 49 %, IPP 14 %, AINS 11 % [S3]. Série espagnole de 61 NIA médicamenteuses : antibiotiques 56 %, AINS 37 % [S8].
- Information professionnelle suisse : néphrite tubulo-interstitielle listée (fréquence inconnue) pour le pantoprazole [S17] ; néphrite interstitielle « rare » pour la ciprofloxacine [S15].
- Maladies systémiques : sarcoïdose > Sjögren > TINU > maladie à IgG4 > vascularites à ANCA ; lupus ; infiltrat avec ou sans granulomes [S3]. Diagnostics différentiels systémiques à évoquer : TINU, IgG4, DRESS, sarcoïdose [S6]. NIA cortico-dépendante récidivante reconnue [S6].
- Infections : bactéries (Brucella, Campylobacter, E. coli, Legionella, Salmonella, streptocoque, staphylocoque, Leptospira, Yersinia, diphtérie), virus (CMV, EBV, hantavirus, VIH, polyomavirus BK chez le transplanté, rougeole, Coxsackie, hépatites A et B, influenza, HSV), spirochètes, toxoplasmose, mycoplasme, tuberculose ; formes infectieuses presque toujours réversibles [S3].
- NIC : néphropathies endémiques toxiques (néphropathie des Balkans, acide aristolochique) ; jeunes travailleurs agricoles masculins ; asymptomatiques jusqu'au stade terminal ; biopsie : NIC avec atrophie tubulaire [S3].

## 7. Anamnèse
- Délai moyen 7–10 jours après exposition ; antibiotiques dès 24 h ; AINS après 6–18 mois ; IPP 10–11 semaines ; IPCI semaines à mois [S3].
- Liste exhaustive des médicaments, y compris IPP et AINS chez la personne âgée polymédiquée [S3, S6].
- Pyélonéphrite : douleurs loge rénale, fièvre, nausées, vomissements ; antécédents de pyélonéphrite, prétraitement par quinolone (modifie le choix empirique) [S4].

## 8. Examen clinique
- NIA : fièvre 35–70 %, rash 25–40 %, douleurs des loges rénales 25–40 %, arthralgies 25–40 % ; triade état subfébrile–rash–éosinophilie dans 10–20 % seulement ; hématurie macroscopique 5–15 % (formes médicamenteuses) ; oligurie 51 % dans une série [S3].
- Pyélonéphrite : signes systémiques (fièvre ou hypothermie, frissons, confusion, hypotension, tachycardie) orientent vers une IU systémique [S7].

## 9. Examens complémentaires
- Sang : créatinine/urée, formule avec répartition (éosinophilie 35–60 %, plutôt immuno-allergique) [S3].
- Urine : sédiment obligatoire ; leucocyturie stérile 75–85 %, hématurie 70–90 %, cylindres leucocytaires, protéinurie tubulaire le plus souvent < 1 g/24 h ; FeNa > 1 % ; protéinurie néphrotique rare sauf atteinte glomérulaire aux AINS ; **éosinophilurie** (Hansel) : spécificité 85 %, sensibilité 67 %, insuffisante ; cylindres leucocytaires hautement suggestifs **si pas de pyélonéphrite** [S3].
- Pyélonéphrite : stix ± sédiment, culture urinaire, 2 paires d'hémocultures [S4] ; culture et antibiogramme chez tous (EAU, fort) [S7].
- Imagerie NIA : échographie (reins augmentés de taille par l'œdème) ; scintigraphie au gallium, rôle non établi [S3].
- Imagerie pyélonéphrite : échographie pour exclure obstruction/calcul ; CT injecté si fièvre persistante à 72 h ou détérioration ; grossesse : échographie ou IRM [S7].
- Biopsie rénale = référence (« gold standard ») : infiltrat interstitiel (lymphocytes T, monocytes, plasmocytes, éosinophiles), œdème, tubulite ; glomérules et vaisseaux le plus souvent préservés ; granulomes (sarcoïdose, tuberculose, certains médicaments) ; neutrophiles nombreux → infection bactérienne ; éosinophiles → médicament ; immunofluorescence le plus souvent négative [S3].
- Biomarqueurs urinaires (CXCL9, TNF-α, IL-9…) prometteurs mais non validés [S11, S12].
- Enfant : culture indispensable ; ≥ 10⁴ UFC/ml sur sondage, ≥ 10⁵ UFC/ml sur mi-jet ; CRP < 20 mg/l ou PCT < 0,5 µg/l rendent la pyélonéphrite moins probable [S9].

## 10. Diagnostic et diagnostic différentiel
- Diagnostic de présomption par contexte et biologie ; certitude par biopsie, car les tests non invasifs sont peu spécifiques [S3].
- Biopsie à considérer si pas d'amélioration **5–7 jours** après l'arrêt de l'agent [S3] ; algorithme HUG : arrêt + surveillance 3–5 jours → biopsie si absence d'amélioration ou aggravation [S3, figure 3].
- Aucun signe clinique ne distingue de façon fiable l'IRA aux IPCI des autres causes ; biopsie = référence [S12].
- Différentiel systémique : TINU, maladie à IgG4, DRESS, sarcoïdose [S6] ; mimiques de l'IgG4 : infection, néoplasie, ANCA, Castleman, Sjögren [S14].
- Pyélonéphrite versus NIA : leucocyturie avec culture positive et fièvre/douleur lombaire (pyélonéphrite) [S4] versus leucocyturie stérile et IRA après exposition médicamenteuse (NIA) [S3].

## 11. Urgences
- Pyélonéphrite = maladie systémique → antibiothérapie immédiate, pas de prescription différée [S4].
- Patient instable : ceftriaxone i.v. ou gentamicine i.v. [S4] ; IU systémique/urosepsis grave ou obstruction : couverture large, durée totale habituelle 5–10 jours [S7].
- NIA : dialyse nécessaire dans 10–30 % des cas [S3].

## 12. Prise en charge suisse
### 12.1 NIA (forme médicamenteuse)
- Arrêt et éviction de la substance ; traitement de l'infection causale ; ± corticothérapie [S3].
- Corticoïdes : **aucun essai randomisé** ; études rétrospectives suggérant un bénéfice (récupération plus rapide, moins d'IRC et de dialyse) [S3, S5, S6].
- Délai : corticoïdes dans les 2 premières semaines après arrêt du médicament → meilleure récupération ; retard moyen de 34 jours → récupération incomplète ; corrélation entre retard et créatinine finale ; fibrose progressive avec le retard (61 patients, Espagne) [S8]. Corticoïdes précoces (dans les 7 jours après le diagnostic) selon Praga et González [S5].
- Pratique HUG : si évolution défavorable après quelques jours d'arrêt et NIA prouvée par biopsie, corticothérapie **au minimum 3 semaines** ; fibrose > 75 % → traitement symptomatique, ≤ 75 % → corticoïdes [S3, figure 3].
- Exemple de schéma documenté (cas clinique HUG, NIA sous nivolumab) : méthylprednisolone 500 mg/j i.v. 2 jours, puis prednisone 1 mg/kg en schéma dégressif sur 6 mois [S3]. **Ce n'est pas une recommandation générale** ; aucune dose standard n'est fixée par une source suisse lue.
- IPCI : corticoïdes débutés ≤ 3 jours après le diagnostic associés à une meilleure récupération ; dose et durée optimales incertaines ; récidive < 20 % à la réexposition [S12].
- Mycophénolate mofétil : amélioration rapportée dans la NIA [S3].
- Prednisone (FI suisse) : dose initiale habituelle 5–60 mg/j ; si > 8–10 jours, ne pas arrêter brusquement, décroissance par paliers ; plus de 2 semaines → risque d'insuffisance surrénale (jusqu'à un an) ; seuil de Cushing 7,5 mg [S16].
### 12.2 Pyélonéphrite de la femme adulte non enceinte (SSI)
- Patiente stable : ciprofloxacine 500 mg p.o. toutes les 12 h, 7 jours [S4]. FI suisse : pyélonéphrite simple 2 × 500 mg, 7 jours ; compliquée 2 × 500–750 mg, ≥ 10 jours [S15].
- Patiente instable ou prétraitée par quinolone : ceftriaxone 1 g i.v./j ou gentamicine 5 mg/kg i.v./j jusqu'à l'antibiogramme [S4]. FI ceftriaxone : adulte 1–2 g/j, jusqu'à 4 g ; aucune adaptation rénale sauf ClCr < 10 ml/min (max 2 g/j) [S18].
- Relais ciblé : TMP/SMX 160/800 mg/12 h 7–14 j ; ciprofloxacine 7 j ; amoxicilline 1000 mg/12 h (ou amoxicilline/clavulanate 875/125 mg/12 h) 7–14 j ; céfuroxime 500 mg/12 h 7–14 j ; privilégier le spectre le plus étroit ; durée courte de 7 jours bien documentée surtout pour la ciprofloxacine [S4].
- Écologie : ciprofloxacine et ceftriaxone ont un impact important sur le microbiote [S4].
- Fluoroquinolones (FI suisse) : tendinites et ruptures tendineuses, effets neurologiques, anévrisme/dissection aortique, régurgitations valvulaires ; adaptation : ClCr 30–60 → max 1000 mg/j ; < 30 → max 500 mg/j [S15].
### 12.3 Perspective européenne (EAU 2026)
- Per os : ciprofloxacine 500–750 mg × 2, 7 j ; lévofloxacine 500 mg × 1 (standard) ou × 2 (haute dose), 5 j ; cefpodoxime 200 mg × 2, 10 j ; ceftibuten 400 mg × 1, 10 j ; TMP/SMX 160/800 × 2, 14 j (réservé, précédé d'une dose parentérale longue) ; quinolones si résistance < 10 % [S7].
- Ne pas utiliser nitrofurantoïne, fosfomycine orale, pivmécillinam dans la pyélonéphrite (fort) [S7].
- Parentéral 1re ligne : ciprofloxacine 400 mg × 2, lévofloxacine 500 mg, céfotaxime 2 g × 3, ceftriaxone 2 g × 1 ; 2e ligne : céfépime, pipéracilline/tazobactam, gentamicine 6–7 mg/kg, amikacine 25–30 mg/kg ; carbapénèmes réservés aux germes multirésistants [S7].
- Relais oral après amélioration ; durée totale 7–10 j ; **homme** avec IU fébrile/pyélonéphrite : au moins 14 jours, de préférence par fluoroquinolone [S7].

## 13. Suivi
- Récupération ≈ 65 %, IRC ≈ 35 % ; environ un tiers évolue vers l'IRC [S3].
- Atteinte < 2 semaines → meilleur pronostic [S3].
- NIA médicamenteuse corticotraitée, 6 mois après biopsie : récupération complète 49 %, partielle 39 %, IRC 12 % [S3].
- Après toute IRA : réévaluer à 3 mois (résolution, apparition ou aggravation d'une MRC) [S10].
- Pyélonéphrite : adapter à l'antibiogramme ; enfant : réévaluation J3–5 [S4, S9].

## 14. Situations particulières
- **Enfant** (consensus suisse) : ≤ 30 j amoxicilline i.v. + aminoside ; 31–60 j amoxicilline i.v. + ceftriaxone ; > 60 j amoxicilline/clavulanate p.o. ou céphalosporine 3e génération (i.v. si mauvais état) ; durée 7–10 j ; relais oral après ≥ 3 j i.v. ; échographie rénale et vésicale dans ~6 semaines après une première IU ; cystographie mictionnelle réservée (CAKUT, dilatation, germe non E. coli, absence de réponse à 48 h, créatinine élevée, ≥ 2 pyélonéphrites) ; prophylaxie généralement non recommandée [S9]. Ciprofloxacine chez l'enfant dès 1 an seulement en 3e choix avec infectiologue [S15].
- **Grossesse** : dépistage unique de la bactériurie asymptomatique au début du 2e trimestre [S4] ; imagerie par échographie ou IRM [S7].
- **Homme** : exclu de la directive SSI [S4] ; EAU ≥ 14 j [S7] ; prostatite : FI ciprofloxacine 2–4 semaines (aiguë) [S15].
- **IPCI** : voir 12.1 [S12].
- **TINU** : rechute rénale fréquente (60 % dans une série monocentrique britannique de 10 patients), souvent pendant la décroissance des corticoïdes [S19].
- **VIH**, **transplanté rénal (BK)** : voir causes [S3].

## 15. Critères formels du diagnostic (pour `div.alert`)
Aucune source lue ne fournit de critères diagnostiques formels validés pour la NIA. Le rédacteur peut présenter, en le disant explicitement :
- Certitude : histologie (infiltrat interstitiel + œdème ± tubulite, glomérules préservés) [S3].
- Présomption : IRA (KDIGO [S10]) + exposition compatible + sédiment évocateur (leucocyturie stérile, cylindres leucocytaires hors pyélonéphrite, protéinurie tubulaire) [S3].
- Pyélonéphrite : symptômes typiques + pyurie > 10/mm³ + culture ≥ 10³ UFC/ml [S4].

## 16. Paramètres clés (pour `div.key`)
- NIA = 1–10 % des biopsies, ≈ 13,5 % des biopsies pour IRA [S3].
- Médicaments 70–75 % ; antibiotiques 49 %, IPP 14 %, AINS 11 % [S3].
- Triade complète 10–20 % ; éosinophilie 35–60 % ; leucocyturie stérile 75–85 % ; protéinurie < 1 g/24 h [S3].
- Biopsie si pas d'amélioration après 5–7 jours [S3] ; fibrose visible dès 7 jours [S3].
- Corticoïdes ≤ 2 semaines après l'arrêt [S8] ; ≥ 3 semaines de traitement (HUG) [S3].
- Pyélonéphrite : ciprofloxacine 500 mg × 2, 7 j ; ceftriaxone 1 g/j si instable [S4].
- IRC ≈ 35 % après NIA [S3].

## Lacunes explicites
1. Aucune recommandation de la Société suisse de néphrologie sur la NIA trouvée ; la revue HUG (Rev Med Suisse 2022) est la seule source suisse spécifique.
2. Aucune recommandation ERA ou KDIGO dédiée à la NIA trouvée ; aucune dose standard de corticoïdes validée par une recommandation européenne.
3. Directive SSI limitée à la femme adulte non enceinte ; aucune directive SSI lue pour l'homme ; l'article Primary and Hospital Care 2021 (hommes) et la directive mediX n'ont pas pu être lus (DNS / 403).
4. La directive SSI s'appuie partiellement sur des références IDSA/ESCMID (2011) et IDSA 2018 ; elle reste la source suisse en vigueur (validée 25.09.2025, valable jusqu'au 15.12.2026).
5. Les données de séries citées par la revue suisse (Muriithi 133 biopsies, Raghavan) sont américaines ; données épidémiologiques, non conduites thérapeutiques.
6. Néphrite interstitielle chronique : seule la revue suisse a été lue ; pas de source dédiée (N11 relève d'une autre leçon).
7. Pas de chiffres d'incidence suisse de la pyélonéphrite ni de résistance ANRESIS actualisée autre que TMP/SMX 20–30 %.
8. EAU 2026 lu par extraction partielle de la page web (sections 3.6 et partie de 3.7) ; les niveaux de preuve de 3.7 n'ont pas été lus.
