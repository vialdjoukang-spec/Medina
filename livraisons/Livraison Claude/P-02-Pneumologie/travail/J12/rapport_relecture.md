# J12 — Pneumonies virales et pneumonies d’autres causes (P-02-Pneumologie) — rapport de relecture différée

Auto-audit par Agent différé opus 5.5 · 09.10.2026 · cours unique couvrant J12, J16 et J17 (CIM-10-GM 2024 ; code dans l’en-tête seulement).
Sources relues : `travail/J12/chapters/J12/` (6 fichiers), `travail/J12/glossary/j12.py`, `rapport_auteur.md` (réserves 1 à 13). Le brouillon de l’auteur reste intact dans ce dossier. La version relue est injectée dans `chapters/J12/` et `glossary/j12.py`.

**Cette relecture est une revue par IA. Elle ne vaut pas validation médicale humaine.** Aucun médecin n’a relu ce cours.

## Méthode

Deux passes successives et distinctes ont couvert les quatre dimensions de la section 13 de `LEADERSHIP_CLAUDE_2026-10-08.md`. La **passe 1** a relu les six fichiers en entier. Elle a confronté chaque chiffre, seuil et dose à la source primaire, téléchargée de nouveau par le relecteur, puis corrigé et renforcé le texte. La **passe 2** a relu en entier le texte issu de la passe 1, sous forme extraite (environ 15 300 mots), et corrigé les défauts restants. Ensuite sont venus les contrôles techniques et l’injection.

Les sources ont été téléchargées indépendamment de l’auteur le 09.10.2026 :
- recommandations SSI en JSON par l’API `https://ssi.guidelines.ch/api/reader/query/guideline` (POST `{"id":…,"language":…}`), versions et dates de validation lues dans les métadonnées ;
- PDF officiels (OFSP, Plan de vaccination, ECIL, EACS) convertis par `pdftotext` ;
- textes intégraux PMC par `efetch` (db=pmc) ; résumés PubMed par `efetch` ; métadonnées par `esummary` ;
- informations professionnelles suisses par `python3 tools/swissmedic_fi.py texte <gtin>` (AIPS via AmiKo).

## Corrections de la passe 1

### Exactitude médicale et scientifique
| Point | Brouillon | Source lue | Correction |
|---|---|---|---|
| Tocilizumab et baricitinib | « tocilizumab ou baricitinib si aggravation » (îlot 9, fenêtre, onglet Pharmacologie) | SSI COVID-19, v. 36193 (05.02.2026) : ajout après 12 à 24 h sans amélioration des besoins en oxygène ; tocilizumab « si le baricitinib n’est pas disponible ou est contre-indiqué » | Ordre corrigé : baricitinib, ou à défaut tocilizumab ; critère des 12 à 24 h ; tocilizumab en injection intraveineuse unique ; contre-indications relatives présentées comme telles |
| Baricitinib sans remdésivir | Seule l’indication suisse (avec remdésivir) | AIPS Olumiant (11.2025) ; SSI « can be administered without concomitant remdesivir » | Les deux sources citées ; contre-indication si la thromboprophylaxie l’est (AIPS et SSI) |
| Remdésivir ambulatoire | Aucune condition d’instauration | SSI, limitation OFSP jusqu’au 31.12.2026 | Traitement précoce ambulatoire instauré par un centre spécialisé ou un hôpital universitaire (fenêtre, quiz 2) ; durée sous oxygène : au moins 5 et au plus 10 jours (AIPS Veklury), 5 jours (SSI) |
| Bilan hospitalier | PCR du SARS-CoV-2 systématique | SSI Pneumonie, v. 41043 (09.09.2026) : PCR SARS-CoV-2 « pendant la pandémie » ; Gram et culture si analyse dans les 4 h | Précisé ; test du SARS-CoV-2 exigé avant tout antiviral (SSI COVID-19) |
| Échographie pulmonaire | « Si un opérateur qualifié est présent » | SSI Pneumonie : alternative « si personnel qualifié et si radiographie pas disponible » | Double condition rétablie (îlot 7, Examens, fenêtre Imagerie) |
| Antibiothérapie empirique | Amoxicilline seule en ambulatoire | SSI Pneumonie | Amoxicilline sans comorbidité ; amoxicilline-acide clavulanique avec comorbidité ; macrolide systématique dans la pneumonie sévère hospitalisée |
| Haut débit nasal | « Réduit le recours à l’intubation » | ESICM 2023 (PMC10354163), rec. 3.1 | Recommandation forte pour réduire l’intubation ; aucun effet démontré sur la mortalité |
| Mécanisme du haut débit et du décubitus ventral | « Lavage de l’espace mort, léger effet de PEP » (non sourcé) | ESICM 2023, texte intégral | FiO₂ plus stable, réduction de l’espace mort anatomique, PEP de 3 à 5 cm d’eau ; décubitus : poumon plus homogène, meilleur rapport ventilation-perfusion, contraintes réduites |
| Pneumonie varicelleuse | « Ventilés dans les 24 à 48 heures » ; corticoïdes sans effectifs | Mirouse 2017, résumé | Délai médian d’un jour ; 10 patients sous corticoïdes contre 60 témoins appariés ; aucune recommandation suisse ou européenne lue ne tranche |
| Co-infection | « 14 à 15 % des cas » | Ruuskanen 2011 (PMC7138033) | Deux études : 14 % (35/242) et 15 % (45/304) ; associations rhinovirus ou influenza A avec *S. pneumoniae* |
| Surinfection à *S. aureus* | « Après une grippe, la SSI ajoute la clindamycine… » | SSI Pneumonie | Seulement en cas de surinfection d’une grippe **à *S. aureus*** |
| CMV au lavage | « Charge de 200 à 500 UI/mL » | ECIL-7, diaporama final | « Supérieure à 200 à 500 UI/mL » ; charges plus faibles : probable excrétion ; ganciclovir au moins trois semaines (maladie à CMV) |
| Hammond 2022 | 7,01 % → 0,77 % et 13 décès présentés ensemble | Résumé PubMed | Analyse intermédiaire (≤ 3 jours) distinguée de l’analyse finale (13 décès, tous sous placebo) |
| Paxlovid, contraception | « Contraception jusqu’à 7 jours » | AIPS Paxlovid (08.2026) | Éviter une grossesse jusqu’à 7 jours ; méthode supplémentaire jusqu’à un cycle après l’arrêt (ritonavir et contraceptifs combinés) |
| Dexaméthasone, corticoïde au long cours | « N’est pas interrompu » (attribué à la SSI, absent de son texte) | AIPS Dexaméthasone Galepharm (06.2022) | Attribué à l’AIPS, chez le patient sans besoin d’oxygène |
| Ganciclovir | Contraception féminine seule | AIPS Cymevene (01.2026) | Ajout de la contraception barrière masculine jusqu’à 90 jours ; mécanisme UL97 → monophosphate → triphosphate reformulé selon l’AIPS |
| Triméthoprime-sulfaméthoxazole | Durée absente pour la pneumocystose | AIPS Bactrim (03.2023) : 14 jours ; EACS 12.0 : au moins 21 jours | Les deux durées citées ; atovaquone 21 jours attribuée à l’EACS et à l’AIPS Wellvone |
| Foscarnet | « Alternative » sans statut | AIPS Foscavir : rétinite à CMV du sida seulement | « Hors indication suisse » dans les tableaux et la fenêtre |
| Fièvre Q | Durée absente | OFSP, page Fièvre Q | Antibiothérapie habituelle de deux semaines, qui vise aussi à prévenir la forme chronique |
| Sous-diagnostic du VRS | « Les adultes consultent souvent après le pic » (non sourcé) | OFSP et CFV, VRS 2026, ch. 4.3 | Excrétion plus faible et plus brève (3 à 4 jours) ; tests rares ou tardifs |
| Létalité du VRS | « Létalité hospitalière » | OFSP et CFV, VRS 2026 | « Taux de létalité » (terme de la source) |
| Rhinovirus | « Circule surtout en été et en automne » | Rapport Sentinella 2023/2024 (texte) | Affirmation absente du texte lu : retirée |
| Dommage alvéolaire | « Hypoxémie réfractaire à l’oxygène standard » ; « l’hypoxémie précède les signes auscultatoires » | Ruuskanen, Gattinoni | Formulations non sourcées remplacées par l’évolution vers le SDRA |
| Phénotype H | Absent | Gattinoni 2020 (PMC7154064) | 20 à 30 % de la série, critères du SDRA sévère |
| Suivi des lymphocytes T anti-CMV | « L’ECIL propose de suivre » | ECIL-10 CMV | Peut aider à personnaliser la prévention, niveau de preuve faible (CIIt) |
| Diagnostic différentiel | Œdème cardiogénique, verre dépoli « n’excluant pas une bactérie » (non sourcés) | SSI (embolie pulmonaire parmi les causes d’aggravation, tuberculose si symptômes persistants), OFSP (condensation lobaire du VRS), Ruuskanen (aucun algorithme fiable) | Reformulé sur ces sources |
| Vaccination après pneumonie | « Pneumocoque selon le plan, grippe annuelle » | SSI Pneumonie | Pneumocoque conseillé si facteur de risque, à envisager chez tous ; grippe dès 65 ans ou facteur de risque |
| Nirsévimab chez l’adulte | « Hors autorisation (ECIL) » | AIPS Beyfortus (07.2026) | Autorisation suisse limitée au nourrisson et à l’enfant ; données adultes insuffisantes selon l’ECIL |
| Foyers en institution | Attribués au hMPV et aux virus parainfluenza | Ruuskanen | Foyers mortels décrits pour le hMPV (et le rhinovirus), non pour les virus parainfluenza |

### Réserves de l’auteur tranchées
- **Réserve 2 (hors indication)** : maintenue et rendue visible là où la molécule apparaît : tocilizumab (absent de l’AIPS Actemra, vérifié : aucune occurrence de « COVID ») et foscarnet (AIPS limitée à la rétinite à CMV du sida). Ribavirine et cidofovir : aucune AIPS ; schémas ECIL, lacune nommée.
- **Réserve 3 (aciclovir)** : confirmée. L’AIPS Zovirax i.v. ne donne une dose « varicelle de l’immunodéprimé » que chez l’enfant (500 mg/m²) ; la lacune nommée de l’adulte est conservée.
- **Réserve 4 (Chlamydia)** : confirmée ; la lacune est désormais énoncée aussi dans l’îlot 9. Le spectre est vérifié : *C. pneumoniae* sensible (AIPS Klacid), *C. psittaci* CMI 0,03 mg/L (AIPS Doxycyclin-Mepha).
- **Réserve 6 (corticoïdes)** : arbitrage de l’auteur confirmé. SSI 2026 (« clairement indiqués » dans la pneumonie sévère, même sans choc) et ERS/ESICM/ESCMID/ALAT 2023 (Q6 : choc seulement, non applicable aux pneumonies virales grippe, SARS, MERS) ont été relus ; la source applicable la plus récente est retenue pour la pneumonie sévère bactérienne ou indéterminée.
- **Réserve 9 (EACS)** : la version 12.0 est lue en texte intégral. Le résumé des changements de la version 12.1 à la version 13 (eacs.sanfordguide.com) ne mentionne pas la pneumocystose ; le passage de la 12.0 à la 12.1 n’a pas été vérifié. La fenêtre le dit.
- **Réserve 11 (clé RECOVERY)** : le cours garde « Recovery » en casse mixte, nom propre de l’essai ; l’audit ne le détecte pas comme abréviation. La clé de `glossary/i35.py` n’est pas touchée, car aucun autre cours ne doit être modifié.
- **Réserve 12 (mobile)** : mesure du relecteur : `scrollWidth` = 390 px dans les quatre onglets ; aucun défilement de page.
- **Réserve 13 (`tests/audit_sciences.py`)** : J12 figure déjà dans la liste des nouvelles productions sans base Git ; aucune modification n’est nécessaire.

### Sources et plan
- Plan monographique classique conservé (îlots 0 à 13). Aucun îlot ni tableau n’est consacré au code CIM ; le code n’apparaît que dans l’en-tête.
- Le titre affiché est aligné sur l’entrée prévue de `chapters.json` : « Pneumonies virales et pneumonies d’autres causes ».
- Références ajoutées : OFSP et CFV VRS 2026 (îlot 7), OFSP Fièvre Q, AIPS Klacid et Doxycyclin-Mepha (îlot 9), AIPS Olumiant (Pharmacologie 3), AIPS Beyfortus (Pharmacologie 4), Recovery (Immunologie).
- Aucune recommandation américaine ne fonde une conduite. Les essais nord-américains (Hammond, Gottlieb) sont cités comme données ; la recommandation de 2023 est retenue au titre de l’ERS, de l’ESICM et de l’ESCMID. L’OMS n’est citée qu’à travers la SSI.

### Rédaction
- Phrases de fabrication retirées : « les agents traités dans ce cours », « le tableau relie ces trois éléments ».
- Phrases nominales réécrites en phrases complètes : carte « Forme typique », définitions du dommage alvéolaire, de la psittacose, de *C. pneumoniae*, mécanismes du remdésivir, du ganciclovir, du voriconazole et du nirsévimab, précautions de la doxycycline et du triméthoprime-sulfaméthoxazole.
- Attributions explicites ajoutées là où une affirmation venait d’une source sans la nommer (SSI, AIPS, ECIL, ESICM).
- L’en-tête porte le statut réel : « relu par un second agent d’intelligence artificielle, sans validation médicale humaine ».

## Corrections de la passe 2
La relecture intégrale du texte corrigé a encore modifié les points suivants :
- îlot 2 : épilogue « le pronostic dépend surtout de » (hiérarchie non sourcée) remplacé ;
- îlot 3 et fenêtre : phases de la COVID-19 datées « après l’infection » (SSI) ;
- îlot 4 : SARS-CoV-2 « hospitalisations accrues en hiver » (Plan de vaccination 2026) ; foyers en institution limités au hMPV ;
- îlot 7 : antécédent ambigu (« elle ») corrigé ; différentiels reformulés ;
- îlot 9 : ordre ambulatoire puis hôpital rétabli ; lacune *Chlamydia* énoncée ;
- îlot 10 : SARS-CoV-2 de l’immunodéprimé : excrétion **et** symptômes persistants ;
- Examens 1 : statuts des tests réécrits (influenza en saison, SARS-CoV-2 avant antiviral ; multiplex selon la conséquence) ;
- Anatomopathologie : « la bronche reste perméable » (non sourcé) retiré ;
- Immunologie : « les glucocorticoïdes atténuent » nuancé et rattaché à Recovery ;
- Pharmacologie : tocilizumab « injection intraveineuse unique » ; mortalité sans assistance respiratoire attribuée à Recovery ;
- fenêtres : liste des 26 virus présentée comme exemples (« parmi lesquels ») ; accord « Il a été décrit » ; adénovirus 2 à 12 % ; Pareto Diagnostic aligné sur l’îlot 7.

## Sources vérifiées (56 liens, tous contrôlés le 09.10.2026)

**PubMed (22), vérifiés par `esummary` : premier auteur, année et revue concordants.**
21435708 Ruuskanen 2011 Lancet · 21951385 Woodhead 2011 Clin Microbiol Infect · 27246595 Burk 2016 Eur Respir Rev · 27550990 Cordonnier 2016 J Antimicrob Chemother · 27550991 Alanio 2016 · 27550992 Maertens 2016 · 27550993 Maschmeyer 2016 · 28592328 Mirouse 2017 Crit Care · 28946931 Hogerwerf 2017 Epidemiol Infect · 29544767 Ullmann 2018 Clin Microbiol Infect · 30076119 Schauwvlieghe 2018 Lancet Respir Med · 30882289 Rybarczyk 2020 Acta Clin Belg · 31153807 Ljungman 2019 Lancet Infect Dis · 32142651 Hoffmann 2020 Cell · 32291463 Gattinoni 2020 Intensive Care Med · 32437596 Ackermann 2020 N Engl J Med · 32678530 Horby (RECOVERY) 2021 N Engl J Med · 33333012 Koehler 2021 Lancet Infect Dis · 34937145 Gottlieb 2022 N Engl J Med · 35172054 Hammond 2022 N Engl J Med · 37012484 Martin-Loeches 2023 Intensive Care Med · 37326646 Grasselli 2023 Intensive Care Med.

Les pages PubMed répondent par le proxy de la session avec le code 203 (contenu servi par le proxy) ; leur existence est établie par `esummary`.

Mode de lecture par le relecteur :
- **texte intégral PMC** : Ruuskanen (PMC7138033), Woodhead (PMC7128977), Gattinoni (PMC7154064), Grasselli (PMC10354163), Martin-Loeches (PMC10069946) ;
- **résumé** : les autres.

**URL officielles (HTTP 200, contenu lu)**
- SSI, Pneumonie acquise en communauté, v. 41043 validée le 09.09.2026 : https://ssi.guidelines.ch/guideline/3007/fr
- SSI, Infection respiratoire aiguë et syndrome grippal, v. 40978 validée le 01.09.2026 : https://ssi.guidelines.ch/guideline/5082/fr
- SSI, SARS-CoV-2/COVID-19, v. 36193 validée le 05.02.2026 (texte anglais) : https://ssi.guidelines.ch/guideline/3352/de
- OFSP et CFV, Recommandations VRS, mise à jour 2026 (PDF intégral) ; OFSP, page VRS ; OFSP, Plan de vaccination suisse 2026 (février 2026) ; OFSP, Bulletin 40/2024, rapport Sentinella 2023/2024 ; OFSP, page Fièvre Q.
- ECIL-10 virus respiratoires communautaires (septembre 2024), ECIL-10 CMV (2024), ECIL-7 CMV (2017) : diaporamas finaux. Le PDF ECIL-10 CMV a connu des coupures réseau transitoires ; il a répondu 200 (742 869 octets) au dernier essai.
- EACS 12.0 (octobre 2023), PDF intégral, section pneumocystose ; résumé des changements v12.1 → v13.
- ECDC, Facts about measles ; ECDC, Facts about Q fever.
- AIPS via AmiKo (produit et date de mise à jour confirmés dans le texte) : Paxlovid 08.2026 ; Veklury 12.2025 ; Dexaméthasone Galepharm 06.2022 ; Olumiant 11.2025 ; Actemra 09.2026 ; Cymevene 01.2026 ; Foscavir 06.2022 ; Zovirax i.v. 12.2025 ; Vfend 05.2026 ; Cresemba 01.2026 ; AmBisome 01.2025 ; Doxycyclin-Mepha 02.2024 ; Klacid 03.2026 ; Bactrim forte et Bactrim perfusion 03.2023 ; Wellvone 12.2025 ; Beyfortus 07.2026 ; Abrysvo 07.2026 ; Arexvy 06.2026 ; mRESVIA 08.2026.

Doses et contre-indications vérifiées mot à mot dans l’AIPS :
- **nirmatrelvir-ritonavir** : 300/100 mg toutes les 12 h pendant 5 jours ; DFGe 30 à 60 : 150/100 mg toutes les 12 h ; < 30, dialyse comprise : 300/100 mg au jour 1 puis 150/100 mg par jour ; proscrit en Child-Pugh C ; contre-indications listées (amiodarone, dronédarone, flécaïnide, colchicine, simvastatine, quétiapine, éplérénone, finérénone, sildénafil, tadalafil) ; grossesse non recommandée sauf nécessité ;
- **remdésivir** : 200 mg puis 100 mg ; 3 jours sans oxygène ; 5 à 10 jours sous oxygène ; aucune adaptation rénale ni hépatique ; compétition avec l’ATP ;
- **dexaméthasone** : 6 mg par jour jusqu’à 10 jours (COVID-19 sous oxygène) ;
- **baricitinib** : 4 mg par jour, 14 jours ou jusqu’à la sortie ; 2 mg si DFG 30 à 60 ; non recommandé < 30 ;
- **ganciclovir** : 5 mg/kg toutes les 12 h pendant 14 à 21 jours ; réduction dès une clairance < 70 mL/min ; seuils 500/µL, 25 000/µL, 8 g/dL ; contre-indiqué pendant la grossesse et l’allaitement ;
- **aciclovir** : 10 mg/kg toutes les 8 h (zona de l’immunodéprimé) ;
- **voriconazole** : 6 puis 4 mg/kg ; relais 200 mg ; TDM 1 à 5 µg/mL ; troubles visuels 26,2 % ; bilan hépatique 25,2 % ; contre-indications ;
- **isavuconazole** : 200 mg toutes les 8 h pendant 48 h puis 200 mg par jour ; biodisponibilité 98 % ;
- **amphotéricine B liposomale** : 3 à 5 mg/kg par jour au moins 14 jours ;
- **doxycycline** : 200 puis 100 mg ; contre-indiquée en insuffisance hépatique sévère ; grossesse et âge ≤ 12 ans ;
- **clarithromycine** : 250 à 500 mg toutes les 12 h ; moitié si clairance < 30 ;
- **triméthoprime-sulfaméthoxazole** : pneumocystose jusqu’à 20/100 mg/kg par jour en 4 prises, 14 jours ; prophylaxie 1 comprimé forte 3 fois par semaine ; nocardiose 480 à 640 mg de triméthoprime au moins 3 mois ; clairance 15 à 30 : moitié ; < 15 et troisième trimestre : contre-indiqué ; hyperkaliémie jusqu’à 60 % des patients à risque ;
- **nirsévimab** : 50 mg sous 5 kg, 100 mg dès 5 kg ; modification YTE prolongeant la demi-vie (≈ 71 jours).

## Contrôles techniques et rendu

| Contrôle | Résultat |
|---|---|
| Clés et gabarits | 51 `data-k` = 51 gabarits (45 fenêtres et 6 Pareto) ; tous préfixés `j12-` ou `pareto-j12-` ; aucun identifiant dupliqué ; ancres et couvertures Pareto valides |
| Classes | toutes dans la liste fermée de `CHAPTER_SPEC.md` |
| HTML | a+b+c+d concaténés bien formés (pile vide) ; chacune des 51 fenêtres bien formée |
| Contrat Sciences (logique de `tests/audit_sciences.py`) | navigation complète ; Virologie 447 mots, Anatomopathologie 353, Physiologie 381, Immunologie 445 ; une figure SVG `role="img"` légendée chacune ; les quatre liens présents |
| Glossaire | `glossary/j12.py` : 15 clés, ajout conditionnel (`_a`). Aucune collision avec `glossary/*.py` (vérifiée par le relecteur) |
| `build_medina.py J12` (copie superposée, J12 enregistré dans une copie de `chapters.json`) | `J12 non couvertes: 0` (équivalent de `audit() == {}` pour le cours) ; Pareto calculés : 6 %, 11 %, 6 %, 6 %, 6 % et 4 % |
| `build_front.py --fragment S02` (copie superposée, J12 ajouté à une copie de `course_groups.json`) | construit : 5,46 Mo, compressé à 2,72 Mo |
| Chromium 1194, `#/entry/J12` | titre correct ; 4 onglets non vides ; 51 mots verts et boutons Pareto ouverts dans les 4 onglets, les 4 disciplines et toutes les pages du pager, aucun « Fiche absente » ; aucune erreur JavaScript ni de console ; mobile 390 px : `scrollWidth` = 390 dans les 4 onglets |
| Tests unitaires | `tests.test_audit_glossary_boundaries`, `tests.test_fragment_surface_isolation` : 9 tests, OK |
| `tools/capture_lecon.py` | `captures/j12-1-ouverture.png`, `captures/j12-2-explication.png` (fenêtre « Les virus respiratoires communautaires »), `captures/captures.json` ; statut : relu, injecté, non enregistré dans `chapters.json` |

Le texte compte environ 16 800 mots références comprises, contre 15 900 dans le brouillon. La hausse vient des attributions et des nuances de preuve ajoutées (durées, conditions d’emploi, analyses intermédiaire et finale).

## Réserves restantes (non bloquantes)

1. **Hors indication suisse** : tocilizumab dans la COVID-19, foscarnet dans la pneumonie à CMV ; ribavirine et cidofovir sans AIPS trouvée (schémas ECIL, niveaux BII à CIII). Tous sont signalés dans le cours.
2. **Aciclovir de l’adulte** : aucune dose AIPS propre à la pneumonie varicelleuse ; la dose du zona de l’immunodéprimé est présentée comme telle.
3. **Chlamydia et psittacose** : aucune recommandation suisse ou européenne spécifique du traitement ; choix fondé sur le spectre AIPS (lacune nommée).
4. **Nocardiose** : terrains et radiologie non documentés par les sources lues (lacune nommée).
5. **ECIL** lu sous forme de diaporamas finaux (ECIL-7 CMV, ECIL-10 CMV et virus respiratoires), non d’articles intégraux.
6. **Lectures limitées au résumé** : Burk, Hogerwerf, Rybarczyk, Hoffmann, Ackermann, Mirouse, Schauwvlieghe, Ullmann, Koehler, Alanio, Maertens, Maschmeyer, Cordonnier, Ljungman, Horby (Recovery), Hammond, Gottlieb.
7. **EACS** : version 12.0 lue ; le passage de la 12.0 à la 12.1 n’a pas été vérifié pour la pneumocystose.
8. **Épidémiologie suisse** : rapport Sentinella 2023/2024 (ambulatoire, non spécifique des pneumonies), le plus récent trouvé.
9. **Notions physiologiques générales** encore formulées sans citation mot à mot : justification des signes d’alerte dans la fenêtre « Signes d’alerte » (travail respiratoire, hypoperfusion, échanges gazeux) ; propos introductifs des disciplines des sciences.
10. **Contentieux des corticoïdes** (SSI 2026 contre ERS/ESICM/ESCMID/ALAT 2023) : exposé dans sa fenêtre ; la SSI, plus récente, est retenue hors pneumonie virale documentée.
11. **Clé glossaire RECOVERY** : l’essai est écrit « Recovery » ; la clé de `glossary/i35.py` désigne un autre essai et reste inchangée.
12. `chapters.json`, `organisation/*` et `organisation/course_groups.json` n’ont pas été modifiés, comme demandé : l’enregistrement revient à l’orchestrateur (`{"code":"J12","covers":["J12","J16","J17"],"title":"Pneumonies virales et pneumonies d’autres causes","integrated":true}`, propriétaire S02). Les contrôles de construction ont été faits sur une copie superposée.

## Injection

- `chapters/J12/` : `J12_a.html`, `J12_b.html`, `J12_c.html`, `J12_d.html`, `J12_pop1.html`, `J12_pop2.html`.
- `glossary/j12.py` : glossaire de l’auteur, avec ajout conditionnel pour éviter toute collision.
- `livraisons/Livraison Claude/P-02-Pneumologie/travail/J12/captures/` : deux captures et `captures.json`.
- Aucune opération Git. Aucun autre cours, ni `chapters.json`, ni `organisation/*`, ni le brouillon de l’auteur n’ont été modifiés.
