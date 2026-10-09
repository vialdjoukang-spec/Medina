# R05 — Toux aiguë et chronique (P-02-Pneumologie) — rapport de relecture différée

Auto-audit par Agent différé opus 5.5 · 09.10.2026 · cours unique couvrant R05 (CIM-10-GM 2024 ; code dans l’en-tête seulement).
Sources relues : `travail/R05/chapters/R05/` (6 fichiers), `travail/R05/glossary/r05.py`, `rapport_auteur.md`. Le brouillon de l’auteur reste intact dans ce dossier. La version relue est injectée dans `chapters/R05/` et `glossary/r05.py`.

**Cette relecture est une revue par IA. Elle ne vaut pas validation médicale humaine.** Aucun médecin n’a relu ce cours.

## Méthode

Deux passes successives et distinctes ont couvert les quatre dimensions de la section 13 de `LEADERSHIP_CLAUDE_2026-10-08.md`. La **passe 1** a relu les six fichiers en entier. Elle a confronté chaque chiffre, seuil et dose à la source primaire, téléchargée de nouveau par le relecteur, puis corrigé, sourcé et resserré le texte. La **passe 2** a relu en entier le texte issu de la passe 1, sous forme extraite (corps, fenêtres, Pareto), et corrigé les défauts restants. Ensuite sont venus les contrôles techniques et l’injection.

Les sources ont été téléchargées indépendamment de l’auteur le 09.10.2026 :
- recommandation SSI par l’API `https://ssi.guidelines.ch/api/reader/query/guideline` (POST `{"id":"5082","language":"fr"}`), version et date de validation lues dans les métadonnées ;
- PDF officiels (Société allemande de pneumologie, HUG, NICE) convertis par `pdftotext` et lus en entier pour la Société allemande et les HUG ;
- textes intégraux PMC (BioC) pour l’ERS 2020 et Singh 2020 ; résumés PubMed par `efetch` ;
- page OFSP en HTML ;
- informations professionnelles suisses par `python3 tools/swissmedic_fi.py texte <gtin>` (AIPS via AmiKo) ;
- statut de remboursement de Lyfnua® par la base ywesee (ch.oddb.org).

## Réserves de l’auteur : décisions

| Réserve | Décision du relecteur |
|---|---|
| Volume de 17 800 mots | Resserré : 15 100 mots hors références, SVG et sommaires (16 080 dans le brouillon) ; 16 970 au total (17 760). Mesure comparable à J81 (14 880) et J12 (15 270). Fenêtres en doublon fusionnées, monographies allégées, un quiz redondant retiré (tomodensitométrie, déjà traitée par le quiz de l’îlot 7). |
| Éosinophiles ERS « 0,3 cells/µL » | Texte intégral relu : la valeur est littéralement écrite ainsi. La lecture 0,3 G/L (300/µL) est la seule biologiquement possible ; la note de lecture est conservée dans la fenêtre. |
| Morphine 5 mg sans forme suisse | Résolue : AIPS Kapanol® (11.2024, capsules retard 10 à 200 mg), MST® Continus® (05.2024, comprimés retard 10 à 200 mg, non sécables) et Sevre-Long® (30 à 200 mg) lues. **Aucune forme retard à 5 mg** : le cours l’écrit et précise qu’en Suisse seule la dose de 10 mg deux fois par jour est réalisable avec une forme retard. |
| Recommandation SSI non lue | Résolue : SSI « Infection respiratoire aiguë et/ou syndrome grippal chez l’adulte », version 40978 validée le 01.09.2026, lue en entier. Elle devient la source principale de la toux aiguë (voir ci-dessous). |
| Remboursement du géfapixant | Vérifié : les deux emballages de Lyfnua® (56 et 196 comprimés, catégorie B) figurent **sans prix public ni quote-part** dans la base ywesee, alors qu’un produit de la liste des spécialités (Kapanol®) y affiche prix et quote-part. Le cours écrit « absent de la liste des spécialités, donc non remboursé d’office ». |
| `tests/audit_sciences.py` | Non modifié (hors périmètre du relecteur). La logique du contrôle a été appliquée sur la copie : conforme. L’enregistrement de R05 dans `chapters.json` exigera d’ajouter R05 à la liste des nouvelles productions sans base Git, comme pour J81, J12 et J21. |

## Corrections de la passe 1

### Exactitude médicale et scientifique
| Point | Brouillon | Source lue | Correction |
|---|---|---|---|
| Toux aiguë : antibiotique | Règle et schémas du NICE (britanniques) seuls | SSI 01.09.2026, « Tests » et « Traitement » | Règle suisse : pas de CRP ni d’antibiotique si rhinorrhée, mal de gorge ou fièvre < 38,5 °C sans dyspnée, tachycardie ni râles (bénéfice < 1-3 %) ; CRP si fièvre ≥ 38,5 °C > 3 jours, dyspnée, FR ≥ 22, anomalie focale, pouls ≥ 100 ; CRP ≥ 100 mg/L antibiotique, < 50 symptomatique, 50-100 décision partagée ; amoxicilline 1 g/8 h. Schémas NICE retirés ; critères de haut risque NICE gardés comme repère européen |
| Traitement symptomatique (arbitrage) | Société allemande 2025 retenue comme source la plus récente | SSI 09.2026 | Arbitrage repris : SSI la plus récente. Dextrométhorphane « efficacité contestée » ; codéine = placebo ; miel, lierre-thym ; acétylcystéine, preuve faible ; bronchodilatateurs seulement si maladie des voies aériennes ; corticoïdes non soutenus |
| Radiographie dans la toux aiguë | Absente | SSI | Non recommandée en routine chez l’ambulatoire (performance limitée pour les consolidations) |
| Signes de gravité | Société allemande et HUG | SSI | Critères d’hospitalisation ajoutés : PAS < 90 mm Hg, FR ≥ 30, SpO₂ < 92 %, hémoptysie, stridor, maladie pulmonaire ou immunodéficience sévères |
| Géfapixant : remboursement | « Non vérifié » (lacune) | ywesee (ch.oddb.org) | Non remboursé d’office ; mention dans l’îlot 11, la pharmacologie, le Pareto et le cas récapitulatif (avec exclusion d’une apnée du sommeil avant prescription) |
| Géfapixant et apnée du sommeil | Interdiction sans motif | AIPS Lyfnua® | Motif ajouté : 180 mg le soir ont abaissé la SaO₂ nocturne chez des patients apnéiques |
| Morphine : forme et contre-indications | « Plus petit comprimé lu : 10 mg » ; contre-indications « BPCO ou asthme sévères » | AIPS Kapanol®, MST® Continus®, Sevre-Long® | Formes suisses listées ; contre-indications selon Kapanol® (troubles du centre ou de la fonction respiratoires, affections obstructives des voies aériennes, iléus paralytique, hypertension intracrânienne) ; association aux benzodiazépines |
| Codéine dans la toux chronique | « Non recommandée » | ERS 2020, recommandation 6a | « Sauf si elle est le seul opiacé disponible » |
| Macrolides | « N’améliorent pas la toux » (HUG) | ERS 2020, recommandation 5 | Nuance ajoutée : essai d’un mois admis dans la bronchite chronique réfractaire |
| Coqueluche du nourrisson | « Détresse respiratoire ou apnées » | OFSP | « Apnées » absent de la source : retiré. Ajout : rappel des proches si dernière dose > 10 ans (OFSP) ; recherche en contexte épidémique (SSI) |
| Tachycardie > 120 | « Embolie ou sepsis » | Société allemande, tableau 2 | « Embolie ou infection fébrile sévère (pneumonie) » |
| Distribution par sexe | « Traitement cortical » | ERS 2020 | « Traitement central de la sensation de toux » |
| Présentations trompeuses | « Exacerbations de BPCO » (non sourcé) | ERS ; Société allemande | Fausses routes prises pour des « infections bronchiques » (ERS) ; obstruction laryngée induite prise pour un asthme résistant (Société allemande) |
| Syncope de toux | « ECG et évaluation de l’aptitude à conduire » (non sourcé) | Société allemande, chapitres 2 et 11 | Conduite automobile retirée ; bilan cardiologique, ECG en tête |
| Complications mécaniques | « Résultent des pressions intrathoraciques élevées » (non sourcé) | HUG section 3 ; Société allemande | Mécanisme non sourcé retiré ; complications attribuées aux HUG, bloc AV vagal à la Société allemande |
| Incontinence | Mécanisme sphinctérien non sourcé | ERS ; AIPS Lyfnua® | Remplacé par les données ERS (un quart de formes sévères, rarement évoquées) |
| Dextrométhorphane et CYP2D6 | « Les inhibiteurs … favorisent le syndrome sérotoninergique » | AIPS Bexine® | Distinction : élévation réciproque des concentrations (CYP2D6) ; syndrome sérotoninergique avec les sérotoninergiques |
| Antitussifs et encombrement | « Contre-indiqués » pour toute la classe | AIPS Codein Knoll®, Bexine® | Contre-indication formelle pour la codéine ; prudence pour le dextrométhorphane |
| Questionnaire de Hull | « Versions multilingues », ERS citée | HUG section 5.5 ; ERS (absent) | Mention et référence ERS retirées |
| Bronchite bactérienne prolongée | « Une récidive impose une évaluation spécialisée » | ERS question 8 | Non sourcé, retiré ; ajout : antibiotique, dose et durée optimaux inconnus |
| Examen de référence | « Durée, premier critère (ERS) » | Société allemande, chapitre 6 | Diagnostic par anamnèse, examen, bilan de base puis réponse au traitement ciblé ; un examen de référence par trait |
| FeNO bas | Conclusion étendue aux corticoïdes | ERS question 2 | Essai antileucotriène et études observationnelles discordantes sur le corticoïde inhalé, distingués |
| Endoscopie nasale | « Signes peu spécifiques » (non sourcé) | HUG tableau 2 | Réservée aux symptômes de sinusite chronique résistants |
| Grossesse | Sans source | HUG section 5.16 | Attribuée aux HUG |

### Sources et plan
- Plan monographique conservé (îlots 0 à 14) ; le code CIM n’apparaît que dans l’en-tête.
- La SSI 2026 est ajoutée aux références des îlots 1, 7, 8 et 9 et aux fenêtres concernées ; le NICE n’y est plus qu’un repère européen.
- Aucune recommandation américaine ne fonde une conduite. La cohorte américaine post-COVID (citée par la Société allemande) et les essais (Morice, Ryan, McGarvey) sont des données.

### Rédaction et efficacité
- Doublons fusionnés entre corps et fenêtres : réflexe, IEC, tabac, reflux, ATP, allotussie, spirométrie, éosinophiles, tomodensitométrie, contentieux morphine et monographie morphine, géfapixant et son contentieux.
- Phrases de fabrication retirées : « sont détaillés dans la fenêtre », « deux contentieux sont exposés dans les fenêtres », « repris dans le tableau ».
- Les épilogues « À retenir » gardent un lien explicite vers la partie suivante, en moins de mots.

## Corrections de la passe 2
- Articles manquants après le resserrement (bilan de base ; liste des conséquences de l’îlot 2).
- Phrase elliptique de l’anamnèse (« un début après un rhume… ») complétée.
- Contagiosité de la coqueluche : « cesse en général après cinq jours » (OFSP), au lieu d’une formule ambiguë.
- Piège FeNO reformulé ; colonne « Toux des voies aériennes supérieures » de l’îlot Examens 3 : « possible si rhinite allergique » (non sourcé) remplacé par « variable ».
- Science → traitement (physiologie) : l’explication de la réponse placebo devient une hypothèse (« pourrait expliquer »).
- Pareto Pharmacologie : « jamais en cas de stase » remplacé par « à éviter ».
- Date des HUG harmonisée (« HUG 2025 »).

## Sources vérifiées (16 liens, contrôlés le 09.10.2026)

**PubMed (6), vérifiés par `esummary` : premier auteur, année, revue concordants** (les pages web renvoient 203 ou 429 par limitation de débit du proxy).
17122382 Morice 2007 Am J Respir Crit Care Med · 22951084 Ryan 2012 Lancet · 35248186 McGarvey 2022 Lancet · 25142479 Morice 2014 Eur Respir J · 25657027 Song 2015 Eur Respir J · 36912371 Mallet 2023 Swiss Med Wkly.

Mode de lecture : texte intégral PMC pour l’ERS 2020 (PMC6942543, tableau 1 compris) et Singh 2020 (PMC7578480) ; résumé pour Morice 2007, Ryan 2012, McGarvey 2022, Morice 2014, Mallet 2023 ; Song 2015 est une lettre sans résumé, citée au travers de l’ERS.

**URL officielles (HTTP 200, contenu lu)**
- SSI, Infection respiratoire aiguë et/ou syndrome grippal chez l’adulte, version 40978, validée le 01.09.2026 : https://ssi.guidelines.ch/guideline/5082/fr
- HUG, stratégie « Toux chronique » 2025, PDF de 12 pages lu en entier.
- Société allemande de pneumologie, S2k AWMF 020-003, version 4.1, janvier 2025, PDF lu en entier (chapitres 1 à 12, tableaux 1 à 5, figures 1 à 4).
- NICE NG120, février 2019 (recommandations 1.1.1 à 1.3, preuves sur miel, guaïfénésine, codéine).
- OFSP, « Coqueluche : la vaccination protège les nourrissons d’une évolution grave », HTML.
- ywesee, ch.oddb.org, Lyfnua® (prix et statut), comparé à Kapanol®.
- AIPS via AmiKo (date de mise à jour confirmée) : Lyfnua® 7680680650028 (11.2024) ; Codein Knoll® 7680192200285 (08.2026) ; Bexine® sirop 7680396390256 (03.2026) ; Neurontin® 7680525200104 (04.2025) ; Prégabaline Sandoz® 7680658970011 (04.2024) ; Nexium® MUPS 7680556090163 (06.2026) ; Montélukast Sandoz® 7680612220015 (10.2023) ; Bisolvon Pentoxyvérine 7680697790014 (07.2023) ; Triofan Antitussif Noscapine 7680688110012 (03.2025) ; SUN STORE Acétylcystéine 600 7680671910025 ; Kapanol® 7680538420094 (11.2024) ; MST® Continus® 7680442460742 (05.2024) ; SEVRE-LONG® 7680539520113.

Doses et contre-indications vérifiées mot à mot dans l’AIPS :
- **géfapixant** : 45 mg deux fois par jour ; 45 mg une fois par jour si DFGe < 30 sans dialyse ; dysgueusie 41 %, agueusie 15 %, hypogueusie 11 %, dans les 9 jours ; arrêt 22 % ; prudence sulfamides ; à éviter si apnée obstructive ; déconseillé pendant la grossesse ; COUGH-1/2 : −18,45 % et −14,64 % contre placebo ;
- **codéine** : 50 mg 1 à 3 fois par 24 h ; 100 mg par prise, 200 mg par jour ; contre-indiquée avant 18 ans, pendant l’allaitement, chez le métaboliseur ultrarapide ; 5 à 20 % transformés en morphine ; cimétidine ;
- **dextrométhorphane** : 25 mg 3 à 4 fois par jour ; 4 jours en automédication, 2 à 3 semaines sur prescription ; < 1 an ; IMAO et sérotoninergiques ≤ 14 jours ; 10 à 15 % de métaboliseurs lents ;
- **gabapentine** : titration 300-600-900 mg ; paliers rénaux 50-79, 30-49, 15-29, < 15 mL/min ; vertiges 12 % ; dépression respiratoire ; chutes ;
- **prégabaline** : 150 puis 300 mg après 3 à 7 jours ; **ésoméprazole** : 40 mg/j dans l’œsophagite, 20 mg dans le reflux symptomatique ; **montélukast** : 10 mg le soir ; **pentoxyvérine** : 15 mL 3 à 4 fois, au plus 90 mL (120 mg) ; **noscapine** : 1 à 2 comprimés de 15 mg 3 à 4 fois, avis après 7 jours ; **acétylcystéine** : réduction des ponts disulfures.

## Contrôles techniques et rendu

| Contrôle | Résultat |
|---|---|
| Clés et gabarits | 56 `data-k` = 56 gabarits (50 fenêtres, 6 Pareto) ; tous préfixés `r05-` ou `pareto-r05-` ; aucun identifiant dupliqué ; couvertures Pareto valides |
| Classes | toutes dans la liste de `CHAPTER_SPEC.md` (et classes structurelles du modèle) |
| HTML | a+b+c+d concaténés bien formés (pile vide) ; fenêtres bien formées |
| Glossaire | `glossary/r05.py` : 9 clés (P2X3, TRPV1, TRPA1, LCQ, COUGH-1, COUGH-2, McGarvey, MST, Sevre-Long) ; MST et Sevre-Long ajoutées par le relecteur (noms commerciaux signalés par l’audit) ; aucune collision avec `glossary/*.py` ni avec les dossiers `livraisons/`, vérifié avant et après injection |
| `build_medina.py R05` (copie superposée, R05 enregistré temporairement) | `R05 non couvertes: 0` ; Pareto calculés (5 % pour le premier) |
| Contrat Sciences (logique de `tests/audit_sciences.py`) | navigation complète ; 4 disciplines de 372 à 382 mots ; une figure légendée et accessible chacune ; quatre liens Science présents |
| `build_front.py --fragment S02` (copie superposée, R05 ajouté à `course_groups.json` de la copie) | 6,05 Mo, compressé à 2,92 Mo |
| Chromium 1194, `#/entry/R05` | cours affiché ; 78 clics sur les mots verts dans les 4 onglets, toutes les pages du pager et les 4 disciplines : 50 fenêtres distinctes, toutes avec contenu, aucune « Fiche absente » ; 6 Pareto ouverts avec fraction calculée ; aucune erreur JavaScript ni de console ; mobile 390 px sans défilement horizontal dans les 4 onglets |
| `tools/capture_lecon.py` | `captures/r05-1-ouverture.png`, `captures/r05-2-explication.png`, `captures/captures.json` (statut : relu, injecté, non enregistré dans `chapters.json`) |

## Réserves restantes (non bloquantes)

1. **Lectures limitées au résumé** pour Morice 2007, Ryan 2012, McGarvey 2022 et Morice 2014 ; leurs chiffres figurent dans ces résumés, dans l’ERS 2020 ou dans l’AIPS Lyfnua®.
2. **Aucune prévalence suisse** de la toux chronique de l’adulte ; seule une donnée pédiatrique zurichoise (Mallet 2023) est citée.
3. **Fréquence des métaboliseurs ultrarapides du CYP2D6 et de la syncope de toux** : non chiffrées par les sources lues (lacunes nommées dans le cours).
4. **Remboursement du géfapixant** : établi par l’absence de prix et de quote-part dans la base ywesee, non par une consultation directe de l’application de la liste des spécialités de l’OFSP (interface non accessible en lecture automatisée). Le remboursement au cas par cas n’a pas été recherché.
5. **Hors indication** : morphine, gabapentine, prégabaline, ésoméprazole 40 mg deux fois par jour, corticoïdes inhalés et montélukast hors asthme ; tous signalés.
6. **Éosinophilie sanguine** : la valeur ERS est lue 0,3 G/L (note de lecture explicite).
7. **Pédiatrie** : repères ERS seulement ; la recommandation pédiatrique allemande (GPP) est annoncée comme en préparation par la Société allemande et n’a pas été lue.
8. `chapters.json`, `organisation/*` et `tests/audit_sciences.py` n’ont pas été modifiés : l’enregistrement revient à l’orchestrateur. Les contrôles de construction ont été faits sur une copie superposée.

## Injection

- `chapters/R05/` : `R05_a.html`, `R05_b.html`, `R05_c.html`, `R05_d.html`, `R05_pop1.html`, `R05_pop2.html`.
- `glossary/r05.py` : glossaire de l’auteur, complété de deux noms commerciaux.
- `livraisons/Livraison Claude/P-02-Pneumologie/travail/R05/captures/` : deux captures et `captures.json`.
- Entrée proposée pour `chapters.json` : `{"code": "R05", "covers": ["R05"], "title": "Toux aiguë, subaiguë et chronique", "integrated": true}`.
- Portée proposée pour `organisation/course_groups.json` (`owner` S02) : « Cours unique : approche symptomatique de la toux de l’adulte, aiguë, subaiguë et chronique (signes d’alarme, traits traitables, toux réfractaire ou inexpliquée, antitussifs et neuromodulateurs), avec repères pédiatriques. Asthme, BPCO, bronchite, bronchiolite et pneumonies relèvent de leurs cours. »
- Aucune opération Git. Aucun autre cours, ni `chapters.json`, ni `organisation/*`, ni le brouillon de l’auteur n’ont été modifiés.
