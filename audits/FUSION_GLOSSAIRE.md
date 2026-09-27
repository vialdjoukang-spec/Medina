# Fusion du glossaire Claude + Alpha : arbitrage (26.09.2026)

## 1. Méthode

1. **Inventaire par exécution isolée.** Un script d’analyse a exécuté chaque fichier `glossary/*.py` isolément, en interceptant `a()` (et `t()`, qui l’appelle), dans trois états : la branche Claude avant fusion (`git show 6790788:glossary/…`, commit de décompression, antérieur à toute fusion ; le commit aa01220 contient déjà `j18`, `i26` et `a41`), la branche Alpha (`/home/user/_alpha/glossary`) et le dépôt fusionné. Un second passage a rejoué le chargement réel de `build_medina.py` : `cardio_1` d’abord, puis l’ordre alphabétique, avec le dictionnaire `G` partagé. Ce passage reproduit exactement `build_medina.G`, soit 1 256 clés identiques avant arbitrage, ce qui valide l’interception.
2. **Clés examinées.** Ce sont les clés définies dans au moins deux fichiers du dépôt fusionné (52), plus les clés dont la valeur finale diffère entre les deux branches (39, dont 38 déjà comptées parmi les 52). Au total, 53 clés.
3. **Règles d’arbitrage.**
   - Développement lettre à lettre le plus littéral et le plus exact.
   - Libellé complet exact.
   - Définition générale, valable dans tous les chapitres qui emploient la clé. Elle fusionne les informations exactes des définitions candidates, sans aucun chiffre nouveau non vérifié.
   - Fenêtre `ref` conservée seulement si le `data-pop` existe (vérifié par recherche dans `chapters/*/*.html`) et si son contenu convient à l’ensemble des emplois. La répartition des emplois a été comptée avec l’expression régulière de `build_medina.py`, qui retient la clé la plus longue.
   - Années des essais vérifiées. COMPASS : publication princeps *N Engl J Med* 2017;377:1319-30.
4. **Écriture.** Les arbitrages sont regroupés dans `glossary/zz_fusion.py`, chargé en dernier grâce à son nom. Le fichier contient une en-tête explicative, puis un appel `a()` par clé, chacun précédé d’un commentaire (candidates, choix). Les autres fichiers de glossaire ne sont modifiés que pour résoudre une collision de sens.
5. **Contrôle de `j44.py`.** Le fichier était en cours de fusion par un autre agent. Il a d’abord été analysé dans sa version de 12:36, puis réanalysé dans sa version réécrite de 12:53 : seules les définitions de CAT et de CPT ont changé, et aucune clé n’a été ajoutée ni retirée. Dans les deux versions, une seule clé de j44 écrasait la définition d’un autre fichier : VNI, arbitrée. Voir aussi CPT et REDUCE ci-dessous. Une nouvelle clé de `j18.py` (CAP-START, 12:55) n’est définie nulle part ailleurs.
6. **Contrôle bloquant.** `python3 test_v7.py --static` sur les 30 chapitres intégrés affiche **OK**, avant comme après l’arbitrage.

## 2. Nombre de clés

| Ensemble | Clés |
|---|---|
| Branche Claude avant fusion (6790788) | 1 231 |
| Branche Alpha | 1 011 |
| Communes aux deux branches | 986 (dont 39 à valeur finale différente) |
| Propres à Claude / propres à Alpha | 245 / 25 |
| Union (dépôt fusionné avant arbitrage, aa01220) | 1 256 |
| Dépôt après arbitrage | 1 258 (+ `PReS`, + `Gore REDUCE`, créées par la résolution des collisions de sens) ; 1 259 à 12:59 avec la clé `CAP-START`, ajoutée en parallèle dans `j18.py` par un autre agent |
| Clés arbitrées dans `zz_fusion.py` | 49 |
| Clés encore définies dans plusieurs fichiers sans arbitrage | 0 |

Parmi les fichiers communs aux deux branches, un seul diffère : `j44.py`. Les écarts de valeur finale viennent donc de l’**ordre de chargement**. Un fichier propre à une branche (`i70`, `i71`, `m06`, `m31`, `m32`, `t78`, `i80` côté Claude ; `j18`, `i26` côté Alpha) écrasait une définition plus riche d’un fichier antérieur. Dans la plupart des cas, cette définition portait une fenêtre `ref`.

## 3. Tableau des arbitrages

Abréviations de la colonne « Candidates » : « fin. » = valeur finale avant arbitrage ; « C » = finale de la branche Claude ; « A » = finale de la branche Alpha.

| Clé | Candidates | Décision | Raison |
|---|---|---|---|
| ABCDE | i10 (aide-mémoire HTA secondaire, fenêtre, A) ; t78 (approche du patient grave, fin., C) | Approche ABCDE, définition enrichie, sans fenêtre | Collision de sens (§ 4) ; le sens majoritaire (I44, I46, T78) est conservé |
| ACTA2 | i35 (A) ; i71 (fin., C) | i35 | Définition exacte et plus complète (gène le plus fréquent des formes familiales non syndromiques) |
| ADN | i30 (fin.) ; i33 | Fusion | Même sens ; deux informations exactes et complémentaires |
| AMPLIFY | i26 (A ; enrichie à 12:59 par un autre agent : effectif et taux) ; i80 (fin., C) | Fusion ; développement complet vérifié ; « (2013) » ; effectif et taux d’i26 conservés | Remplace un développement non établi ; chiffres conformes à la publication princeps (*N Engl J Med* 2013) |
| ASTRAL | i10 (fenêtre i10-sar, A) ; i70 (fin., C) | Développement lettre à lettre d’i10, fusion, i10-sar | La fenêtre cite ASTRAL |
| aVL | i10 ; i21 (fin.) | Fusion (hypertrophie et miroir de l’infarctus inférieur) | Même sens ; définition générale |
| CAPRIE | i25 (fenêtre i25-d-clopi, A) ; i70 (fin., C) | Fusion (doses et population de l’essai), i25-d-clopi | La fenêtre cite CAPRIE ; précision : bénéfice dans l’artériopathie = analyse de sous-groupe |
| CD28 | i40 (A) ; m06 (fin., C) | i40 enrichi | Définition courte de m06 insuffisante |
| CD80, CD86 | i40 (fenêtre i40-d-2l, A) ; m06 (fin., C) | Fusion, sans fenêtre | La fenêtre (myocardite sous immunothérapie) est trop spécifique pour une molécule aussi employée dans M06 |
| Cockcroft-Gault | i48 (fenêtre, définition vide, A) ; i80 (fin., C) | Fusion, i48-cg | La fenêtre expose la formule |
| COL3A1 | i35 (fenêtre, A) ; i71 (fin., C) | i35, i35-marfan | Libellé exact (chaîne alpha 1) ; la fenêtre traite l’Ehlers-Danlos vasculaire |
| COMPASS | i21 (2017, fenêtre i21-dapt, A) ; i70 (2018, fin., C) | « Essai COMPASS (2017) », fenêtre **i25-d-riva** ; résultat précisé (critère composite ; baisse significative des décès cardiovasculaires et des AVC, non significative des infarctus) après contre-lecture, § 7 | Publication princeps de 2017. La fenêtre i21-dapt ne traite pas de COMPASS ; i25-d-riva décrit l’essai |
| CORAL | i10 (fenêtre, A) ; i70 (fin., C) | Fusion, i10-sar | Définition autonome ; i70 disait seulement « concordant avec ASTRAL » |
| CTLA-4 | d84 (« Antigen ») ; i40 (« Associated protein », fin., fenêtre) | i40 enrichi (haplo-insuffisance de d84), i40-d-2l | Développement exact (Cytotoxic T-Lymphocyte-Associated protein 4) ; 11 emplois sur 14 dans I40, fenêtre pertinente (abatacept) |
| D86.8 | i40 ; i42 (fin., fenêtre) | Développement en deux segments (i40), définition i42, i42-sarcoid | Même sens |
| DI | i10 ; i21 (fin.) | Fusion | « bras gauche par rapport au bras droit » : sens exact de la différence de potentiel |
| DRESS | i40 (fenêtre i40-eos, A) ; t78 (fin., C) | Fusion, sans fenêtre | Délai de 2 à 8 semaines, atteinte viscérale, réintroduction et provocation contre-indiquées. La fenêtre (myocardites à éosinophiles) ne convient pas aux 7 emplois de T78 |
| Ehlers-Danlos | i35 (fenêtre, A) ; m31 (fin., C) | Fusion (formes vasculaire et hypermobile), sans fenêtre (corrigé après contre-lecture, § 7) | I49 emploie la forme hypermobile (2 emplois) ; I35, I71 et M31 la forme vasculaire (10). i35-marfan ne traite que la forme vasculaire |
| ERS | j18 (fin., A) ; q21 (fenêtre q21-htap, C) | Libellé de q21, définition générale, sans fenêtre | Emplois dans I26, J18, J44, J45 et Q21 ; fenêtre propre aux cardiopathies congénitales |
| ESICM | i46 ; i49 (fenêtre i49-rosc, C) ; j18 (fin., A) | Fusion, sans fenêtre (corrigé après contre-lecture, § 7) | 28 emplois : 23 (I46 : 22, I49 : 1) visent les recommandations ERC-ESICM post-réanimation, 5 (J18) les recommandations ERS/ESICM/ESCMID/ALAT 2023 de la pneumonie communautaire sévère ; une fenêtre sur les soins après réanimation ne définit pas la société |
| FBN1 | i34 ; i35 (fenêtre, A) ; i71 (fin., C) | Fusion i34 + i35, i35-marfan | Définitions i34 et i35 complémentaires ; i71 réduite à « Syndrome de Marfan » |
| FDG | i33 (fenêtre i33-tep, A) ; m31 (fin., C) | Fusion, i33-tep | Fenêtre **partiellement** pertinente : titre, principe et préparation valables pour tous les emplois ; question clinique, lecture et « Place (ESC 2023) » propres à l’endocardite sur prothèse (6 emplois sur 25 ; 19 en I40, I42, I44 et M31). Conservée faute de fenêtre générale (i42-tep est propre à la sarcoïdose) |
| FOURIER | i21 (fenêtre, A) ; i70 (fin., C) | Fusion, i21-d-pcsk9 | La fenêtre cite FOURIER |
| GLP-1 | cardio_1 (A) ; i70 (fin., C) | Fusion | Les deux informations (événements cardiovasculaires, ICFEp) sont exactes |
| ITV | i34 (fin., i34-pisa) ; i35 (i35-continuite) | Fusion, i35-continuite ; « distance parcourue pendant la phase du cycle considérée (éjection ou régurgitation) » (corrigé après contre-lecture, § 7) | 15 emplois sur 18 dans I35 ; fenêtre générale |
| JAMA | i30 (A) ; t78 (fin., C) | Définition générale | T78 cite *JAMA Internal Medicine* ; la mention de l’essai AIRTRIP est propre à un chapitre |
| LDL | i10 ; i21 (A) ; i70 (fin., C) | Fusion sur i21 | i70 : « principal lipide », inexact (c’est une lipoprotéine) |
| Loeys-Dietz | i35 (fenêtre, A) ; i71 (fin., C) | i35, i35-marfan | Définition complète |
| MIRRA | i40 (fenêtre, A) ; m31 (fin., C) | Fusion ; développement vérifié ; i40-d-eos | Dose de 300 mg toutes les 4 semaines exacte ; la fenêtre traite du mépolizumab |
| PCSK9 | i21 (fenêtre, A) ; i70 (fin., C) | Fusion, i21-d-pcsk9 | Définition plus complète |
| PD-L1 | i40 (A) ; m31 (fin., C) | Fusion | Définition générale, qui inclut l’emploi dans M31 (artérite à cellules géantes) |
| PR3 | i33 (A) ; m31 (fin., fenêtre, C) | Développement « PR = PRotéinase », fusion, m31-anca | m31 développait R par « sérine protéase », ce qui est inexact |
| PRES | i10 (encéphalopathie, A) ; m31 (société de rhumatologie pédiatrique, fin., C) | Pas d’arbitrage : la clé m31 est renommée `PReS` | Collision de sens (§ 4) ; `PRES` revient à i10 |
| RANKL | i35 (A) ; m06 (fin., C) | Développement i35, fusion | Développement de m06 décalé d’une lettre |
| SARS-CoV-2 | i30 (A) ; m31 (fin., C) | Fusion | Syndrome inflammatoire pédiatrique ajouté (emplois dans M31 et I40) |
| SGLT2 | cardio_1 (fenêtre d-sglt2, A) ; i70 (fin., C) | Fusion, d-sglt2 | Développement homogène en anglais : coTransporter |
| SMAD3, TGFB2, TGFBR1, TGFBR2 | i35 (fenêtre, A) ; i71 (fin., C) | i35, i35-marfan ; R = Receptor | Définitions complètes ; la fenêtre cite ces gènes |
| SSI | i33 (fenêtre i33-prophy, C) ; j18 (fin., A) | Développement français littéral, fusion, sans fenêtre | 29 emplois sur 30 dans J18, sans rapport avec l’antibioprophylaxie |
| TEP | i25 (fin., i25-stressimg) ; i33 (i33-tep) | Fusion (perfusion et FDG), sans fenêtre (corrigé après contre-lecture, § 7) | 27 emplois sur 44 (I40, I42, I44) désignent la TEP au FDG de l’inflammation ; i25-stressimg compare les examens d’ischémie. Aucune fenêtre générale sur la TEP |
| TGF-β | i34 (fin.) ; i35 (fenêtre) | Fusion, i35-marfan | Même sens |
| TPMT | i40 (fenêtre, A) ; m32 (fin., C) | Développement i40, i40-d-aza | Développement de m32 inexact (P = « (S-) ») |
| V3, V5, V6 | i10 ; i21 (fin., fenêtre) | Fusion, i21-ecg-terr | Position « au niveau horizontal de V4 » pour V5 et V6 |
| VEGF | i10 (A) ; m31 (fin., C) | Fusion | Précision : le sunitinib inhibe la tyrosine kinase des récepteurs, ce n’est pas un anti-VEGF |
| VNI | cardio_1 ; j44 (fin., fenêtre) | Fusion, j44-vni | j44 écrasait le sens de l’œdème pulmonaire (I50) |
| HOPE | i10 (essai, 1 emploi) ; i46 (score, 3 emplois, fin.) | Pas d’arbitrage : i46 seul après résolution | Collision de sens (§ 4) |
| REDUCE | j44 (BPCO, 2 emplois) ; q21 (foramen ovale, 1 emploi, fin.) | Pas d’arbitrage : la clé q21 est renommée `Gore REDUCE` | Collision de sens (§ 4) ; `REDUCE` revient à j44 |
| CPT | j44 seul (versions Claude et Alpha différentes) | Pas d’arbitrage | Une seule définition dans le dépôt : celle d’Alpha, reprise par la fusion J44, plus complète |

## 4. Collisions de sens traitées

| Sigle | Sens majoritaire (conservé) | Sens minoritaire | Traitement | Fichiers modifiés |
|---|---|---|---|---|
| **PRES** | Syndrome d’encéphalopathie postérieure réversible (I10, définition i10 avec fenêtre i10-pres) | Paediatric Rheumatology European Society (M31, 2 emplois) | Sigle officiel **`PReS`** : nouvelle clé dans m31.py, définition enrichie (critères EULAR/PRINTO/PReS, Ankara 2008, publiés en 2010) ; définition PRINTO corrigée | `chapters/M31/M31_b.html` (2 occurrences), `glossary/m31.py` |
| **REDUCE** | Essai suisse de corticothérapie courte de l’exacerbation de BPCO (J44, 2 emplois ; *JAMA* 2013) | Essai de fermeture du foramen ovale perméable (Q21, 1 emploi) | Nom officiel **`Gore REDUCE`** (Gore REDUCE Clinical Study, *N Engl J Med* 2017) : nouvelle clé dans q21.py | `chapters/Q21/Q21_b.html`, `glossary/q21.py` |
| **ABCDE** | Approche ABCDE du patient grave (I44, I46, T78 : 6 emplois) | Deux aide-mémoire : causes d’hypertension secondaire (I10) et traitement de l’angor (I25), qui recevaient à tort la définition de l’approche | Écrits en toutes lettres : « … en cinq lettres, de A à E ». Titres des fenêtres i10-mnemo-abcde et i25-mnemo-abcde réécrits de même. Clé ABCDE d’i10 retirée, avec un commentaire | `chapters/I10/I10_a.html`, `chapters/I10/I10_pop2.html`, `chapters/I25/I25_b.html`, `chapters/I25/I25_pop4.html`, `glossary/i10.py` |
| **HOPE** | Score HOPE de l’hypothermie (I46 : 3 emplois) | Essai HOPE du ramipril, 2000 (I10 : 1 emploi) | Écrit en toutes lettres : « essais Heart Outcomes Prevention Evaluation et EUROPA ». Clé HOPE d’i10 retirée, avec un commentaire | `chapters/I10/I10_pop4.html`, `glossary/i10.py` |

Les autres clés définies plusieurs fois gardent le même sens dans toutes leurs définitions : dérivations électrocardiographiques, sociétés savantes, essais, gènes et molécules. REDUCE-AMI et REDUCE-IT sont des clés distinctes, non concernées.

## 5. Points signalés à l’intégrateur (hors du périmètre d’écriture de cette mission)

- `chapters/I70/I70_b.html` indiquait « COMPASS (2018) » dans la liste des essais. Le glossaire, I25 et la publication princeps donnent 2017. **Corrigé par l’intégrateur (commit 973c111)** : « COMPASS (2017 ; analyse de l’artériopathie des membres inférieurs, 2018) ». C’était la seule discordance d’année relevée entre les libellés « Essai … (AAAA) » du glossaire et les chapitres.
- `chapters/I25/I25_pop5.html`, fenêtre `i25-d-riva`, rubrique « Preuve » : « a réduit les décès cardiovasculaires, les AVC et les infarctus » laisse croire que chaque composante a diminué. Dans COMPASS (*N Engl J Med* 2017), seuls le critère composite, les décès cardiovasculaires et les AVC baissent significativement ; l’infarctus isolé ne baisse pas significativement (HR 0,86 ; IC 95 % 0,70-1,05). Formulation proposée : « a réduit le critère composite décès cardiovasculaire, AVC ou infarctus (baisse significative des décès cardiovasculaires et des AVC) ». De même, « sans hausse significative des hémorragies mortelles ou intracrâniennes ».
- Aucune fenêtre `ref` du glossaire final ne pointe vers une fenêtre absente.
- Si `glossary/j44.py` est encore modifié, relancer le contrôle. Aucune clé de j44 ne doit écraser une définition d’un autre fichier sans arbitrage dans `zz_fusion.py`. La clé `REDUCE` doit garder le sens BPCO, et `CAAT` (nouvelle) n’est définie nulle part ailleurs.

## 6. Contrôle

`cd /home/user/Medina && python3 test_v7.py --static <30 chapitres intégrés>` → **OK**.

## 7. Corrections après contre-lecture (26.09.2026)

Chaque écart signalé par la contre-lecture indépendante a été vérifié avant correction. Les décomptes d’emplois sont refaits avec l’expression régulière de `build_medina.py` sur le texte des chapitres, hors attributs ; un titre de fenêtre (`data-title`) contenant le sigle explique l’écart d’une ou deux unités avec un décompte par `grep` (ESICM : 28 contre 29 ; TEP : 44 contre 46 ; FDG : 25 contre 27).

| Écart | Vérification | Correction |
|---|---|---|
| TEP : fenêtre i25-stressimg (comparaison des examens d’ischémie) | Confirmé : 27 emplois sur 44 (I40 : 9, I42 : 15, I44 : 3) désignent la TEP au FDG de l’inflammation ; aucune fenêtre générale sur la TEP | `ref=None` dans `zz_fusion.py` ; la définition couvre la perfusion et le FDG |
| ESICM : fenêtre i49-rosc ; décompte « 23 sur 24 » dépassé | Confirmé : 28 emplois depuis la réécriture de J18 (I46 : 22, I49 : 1, J18 : 5) ; les 5 emplois de J18 visent les recommandations ERS/ESICM/ESCMID/ALAT 2023 | `ref=None` (même traitement que les sociétés ERS et SSI : une fenêtre sur un thème de recommandation ne définit pas la société ; I46 dispose de ses propres fenêtres post-réanimation) ; tableau du § 3 corrigé |
| FDG : i33-tep qualifiée de « fenêtre générale » | Confirmé : question clinique, lecture et « Place (ESC 2023) » propres à l’endocardite sur prothèse ; 19 emplois sur 25 hors endocardite | Fenêtre conservée (titre, principe et préparation valables pour tous les emplois ; i42-tep est propre à la sarcoïdose) ; commentaire de `zz_fusion.py` et § 3 corrigés : fenêtre **partiellement** pertinente |
| Ehlers-Danlos : fenêtre i35-marfan | Confirmé : la fenêtre ne décrit que la forme vasculaire ; les 2 emplois de I49 visent la forme hypermobile (10 emplois vasculaires en I35, I71 et M31) | `ref=None` ; la définition couvre les deux formes. COL3A1, propre à la forme vasculaire, garde i35-marfan |
| COMPASS : « a réduit les décès cardiovasculaires, les AVC et les infarctus » | Confirmé (*N Engl J Med* 2017;377:1319-30) : critère composite, décès cardiovasculaires et AVC significatifs ; infarctus isolé non significatif (HR 0,86 ; IC 95 % 0,70-1,05) | Définition réécrite : « a réduit le critère composite décès cardiovasculaire, accident vasculaire cérébral ou infarctus (baisse significative des décès cardiovasculaires et des accidents vasculaires cérébraux ; baisse non significative des infarctus) » ; « sans hausse **significative** des hémorragies mortelles ou intracrâniennes ». Même nuance signalée à l’intégrateur pour la fenêtre i25-d-riva (§ 5), hors du périmètre d’écriture |
| I70 : « COMPASS (2018) » contre « Essai COMPASS (2017) » | Déjà résolu : l’intégrateur a écrit « COMPASS (2017 ; analyse de l’artériopathie des membres inférieurs, 2018) » (commit 973c111) | Aucune ; § 5 mis à jour |
| ITV : « distance parcourue par le sang pendant l’éjection », puis ITV du jet régurgitant | Confirmé : incohérence interne | « pendant la phase du cycle considérée (éjection ou régurgitation) » |
| M31 : référence « Ozen S. et al. EULAR/PRINTO/PReS criteria (2010) » | Confirmé : le titre publié (*Ann Rheum Dis* 2010;69:798-806) écrit « PRES » ; la référence abrégée ressemblait à un titre littéral | Référence reformulée sans titre littéral : « Ozen S. et al. Critères EULAR/PRINTO/PReS de classification des vascularites de l’enfant (conférence de consensus d’Ankara 2008). Annals of the Rheumatic Diseases 2010. » (`chapters/M31/M31_b.html`). Le sigle officiel `PReS` est conservé dans le texte |
| Traçabilité : « HEAD » pour la branche Claude (1 231 clés) | Confirmé : 1 231 clés au commit 6790788, 1 256 au commit aa01220 (qui contient déjà `j18`, `i26` et `a41`) | § 1 et § 2 : « 6790788 (branche Claude avant fusion) » ; union datée d’aa01220 |

Valeurs effectives vérifiées par `python3 -c "import build_medina as B; print(B.G['CLÉ'])"` : TEP, ESICM et Ehlers-Danlos sans fenêtre ; FDG → i33-tep ; COMPASS → i25-d-riva ; ITV → i35-continuite ; COL3A1 → i35-marfan.

Remarque (non signalée par la contre-lecture, non modifiée) : CTLA-4 garde la fenêtre i40-d-2l (myocardite sous immunothérapie), alors que 3 de ses 14 emplois (D84) portent sur l’haplo-insuffisance de CTLA-4 ; cas analogue à ESICM, à trancher par l’intégrateur.

Contrôle après corrections : `python3 test_v7.py --static <30 chapitres intégrés>` → **OK**.
