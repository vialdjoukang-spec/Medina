# Rapport d’auteur — J12 — Pneumonies virales et pneumonies à micro-organismes particuliers (P-02-Pneumologie)

Rédacteur de la chaîne interne Claude, 09.10.2026. Cours unique couvrant J12, J16 et J17. **Version de travail : ni relue par l’agent différé, ni injectée, ni validée par un médecin.** Revue IA et contrôles techniques seulement.

## Fichiers

- `chapters/J12/J12_a.html` — en-tête, onglets, onglet Pathologie îlots 0 à 6 (figure 1, Pareto clinique).
- `chapters/J12/J12_b.html` — îlots 7 à 13 (quiz, Pareto diagnostic, Pareto urgences et traitement, Pareto critères) ; dernier îlot : critères formels `div.alert` puis paramètres clés `div.key`.
- `chapters/J12/J12_c.html` — Examens (4 îlots, 4 quiz, Pareto) et Sciences (Virologie, Anatomopathologie, Physiologie respiratoire, Immunologie ; 4 figures SVG `role="img"` légendées ; liens Science → clinique / examen / traitement / À retenir).
- `chapters/J12/J12_d.html` — Pharmacologie (4 îlots, Pareto) ; ferme le template.
- `chapters/J12/J12_pop1.html` — 34 fenêtres cliniques, diagnostiques et préventives.
- `chapters/J12/J12_pop2.html` — 11 fenêtres de monographies et 6 Pareto.
- `glossary/j12.py` — 15 clés nouvelles : CMV, VZV, hMPV, ACE2, TMPRSS2, ECIL, ECMM, ISHAM, CFV, UL97, UL54, mRESVIA, SARS, SARS-CoV, MERS. Aucune n’existe dans `glossary/*.py` ni dans les glossaires des dossiers `livraisons/` au 09.10.2026 (vérification par chargement de tous les modules et recherche dans les dossiers de travail).

## Plan

Pathologie : 0 question clinique (pneumonie à VRS d’une patiente de 79 ans avec BPCO) ; 1 définition SSI et classification agent × terrain, définitions ECIL ; 2 épidémiologie (méta-analyse de Burk, Sentinella 2023/2024, fardeau du VRS OFSP 2026, psittacose, fièvre Q) ; 3 physiopathologie (ACE2/TMPRSS2, dommage alvéolaire diffus, atteinte endothéliale, deux phases de la COVID-19, surinfection) ; 4 agents et terrains ; 5 anamnèse ; 6 examen et signes d’alerte ; 7 diagnostic (imagerie, PCR, CRP/procalcitonine, différentiels) ; 8 urgences et complications ; 9 traitement de l’immunocompétent ; 10 immunodéprimé (CMV, VRS, adénovirus, hMPV, Aspergillus, SARS-CoV-2) ; 11 suivi et prévention (vaccins VRS et COVID-19, nourrisson, prophylaxies) ; 12 situations particulières et cas récapitulatif ; 13 critères formels et paramètres clés.

Choix de périmètre : la grippe (J09–J11) et les pneumonies bactériennes usuelles (J13–J18) sont renvoyées à leurs cours. Dans la CIM-10-GM 2024 (BfArM, lue le 09.10.2026), la pneumocystose (B48.5) est exclue de J16 ; elle n’est traitée ici que comme diagnostic différentiel de l’immunodéprimé (fenêtre `j12-pcp`). L’ornithose et la fièvre Q relèvent de J17.8. Le code CIM n’apparaît que dans l’en-tête.

## Sources consultées (09.10.2026)

| Source | Mode d’accès réel |
|---|---|
| SSI, Pneumonie acquise en communauté, version 41043 validée le 09.09.2026 (ssi.guidelines.ch/guideline/3007/fr) | Texte intégral via l’API JSON `api/reader/query/guideline` |
| SSI, Infection respiratoire aiguë et syndrome grippal, version 40978 validée le 01.09.2026 (5082/fr) | Texte intégral, même API |
| SSI, SARS-CoV-2/COVID-19, version 36193 validée le 05.02.2026 (3352, texte allemand/anglais) | Texte intégral, même API ; pas de version française |
| OFSP et CFV, Recommandations VRS, mise à jour du 28.09.2026 (PDF) | Texte intégral (pdftotext), chapitres 1, 3, 4, 5, 6 |
| OFSP, page VRS | Texte intégral HTML |
| OFSP et CFV, Plan de vaccination suisse 2026 (février 2026) | Texte intégral PDF : VRS (1.1, figure 1), COVID-19 (3.1.k) |
| OFSP, Rapport annuel sur les virus respiratoires 2023/2024, Bulletin 40/2024 | Texte intégral PDF ; aucun rapport 2024/2025 trouvé |
| OFSP, Fièvre Q | Texte intégral HTML |
| ECIL-10, virus respiratoires communautaires, septembre 2024 (diaporama final) | Texte intégral PDF |
| ECIL-10, CMV, 2024 ; ECIL-7, CMV, 2017 (diaporamas finaux) | Texte intégral PDF |
| ECIL-5 : Alanio, Maertens, Maschmeyer, Cordonnier, JAC 2016 (PMID 27550991, 27550992, 27550993, 27550990) | Résumés PubMed |
| Ljungman et al., ECIL-7, Lancet Infect Dis 2019 (PMID 31153807) | Résumé ; contenu détaillé tiré des diapositives ECIL-7 |
| EACS, version 12.0, octobre 2023 (PDF) | Texte intégral, section pneumocystose ; résumé des changements v12.1 → v13 lu (aucune modification de la pneumocystose) ; v12.1 et v13 en PDF non accessibles |
| Ullmann et al., ESCMID-ECMM-ERS aspergillose 2018 (PMID 29544767) | Résumé |
| Koehler et al., ECMM/ISHAM CAPA 2021 (PMID 33333012) | Résumé |
| Schauwvlieghe et al., Lancet Respir Med 2018 (PMID 30076119) | Résumé |
| Martin-Loeches et al., ERS/ESICM/ESCMID/ALAT 2023 (PMID 37012484, PMC10069946) | Texte intégral (questions 1, 2, 5, 6) |
| Grasselli et al., ESICM SDRA 2023 (PMID 37326646, PMC10354163) | Texte intégral (recommandations extraites) |
| Gattinoni et al., Intensive Care Med 2020 (PMID 32291463, PMC7154064) | Texte intégral (éditorial) |
| Ruuskanen et al., Viral pneumonia, Lancet 2011 (PMID 21435708, PMC7138033) | Texte intégral |
| Burk et al., Eur Respir Rev 2016 (PMID 27246595) | Résumé (chiffres repris) |
| Woodhead et al., ERS/ESCMID LRTI 2011 (PMID 21951385, PMC7128977) | Texte intégral, partie étiologique |
| Recovery Collaborative Group, NEJM 2021 (PMID 32678530) ; Hammond et al., NEJM 2022 (PMID 35172054) ; Gottlieb et al., NEJM 2022 (PMID 34937145) | Résumés PubMed |
| Hoffmann et al., Cell 2020 (PMID 32142651) ; Ackermann et al., NEJM 2020 (PMID 32437596) ; Mirouse et al., Crit Care 2017 (PMID 28592328) | Résumés PubMed |
| Hogerwerf et al., 2017 (PMID 28946931) ; Rybarczyk et al., 2020 (PMID 30882289) | Résumés PubMed (texte intégral inaccessible) |
| ECDC, Facts about measles ; Facts about Q fever | Texte intégral HTML |
| CIM-10-GM 2024, bloc J09–J18 (BfArM) | Texte intégral HTML (périmètre seulement, non cité dans le cours) |
| Informations professionnelles suisses via `tools/swissmedic_fi.py` (AmiKo) : Paxlovid (08.2026), Veklury (12.2025), Dexaméthasone Galepharm amp. (06.2022), Olumiant (11.2025), Actemra (09.2026), Cymevene (01.2026), Foscavir (06.2022), Prevymis (02.2025), Zovirax i.v. (12.2025), Vfend (05.2026), Cresemba i.v. (01.2026), AmBisome (01.2025), Doxycyclin-Mepha (02.2024), Klacid (03.2026), Zithromax (03.2023), Bactrim forte et Bactrim i.v. (03.2023), Wellvone (12.2025), Pentacarinat (12.2020), Beyfortus (07.2026), Enflonsia (11.2025), Synagis (07.2016), Arexvy (06.2026), Abrysvo (07.2026), mRESVIA (08.2026) | Texte intégral ; sections Indications, Posologie, Contre-indications, Grossesse, Mécanisme lues pour les molécules citées |

Tous les liens du cours (56 URL externes) ont été testés : HTTP 200. Les 22 PMID ont été vérifiés par `esummary` (premier auteur, année, revue concordants). Aucune recommandation américaine ne fonde une conduite ; l’ERS 2023, co-signée par des sociétés européennes, est retenue à ce titre. Les essais publiés sont cités comme données.

## Réserves honnêtes

1. **Aucune validation médicale humaine.** Le cours est une version de travail revue par IA.
2. **Hors indication suisse ou sans information professionnelle** : tocilizumab dans la COVID-19 (absent de l’information Actemra) ; foscarnet dans la pneumonie à CMV (information Foscavir limitée à la rétinite à CMV du sida) ; ribavirine et cidofovir (aucune information professionnelle trouvée sur AmiKo) — schémas attribués à l’ECIL dans le cours.
3. **Aciclovir et pneumonie varicelleuse de l’adulte** : l’information professionnelle n’a pas de ligne dédiée ; la dose de 10 mg/kg toutes les 8 heures (zona de l’immunodéprimé) est présentée comme telle (lacune nommée).
4. **Chlamydia** : aucun texte suisse ou européen spécifique du traitement de *C. pneumoniae* ou de la psittacose n’a été trouvé ; macrolide et doxycycline sont justifiés par le spectre des informations professionnelles (lacune nommée dans `j12-chlamydia`).
5. **Nocardiose** : terrains et radiologie non documentés par les sources lues (lacune nommée).
6. **Contentieux corticoïdes** : SSI 2026 (corticoïdes dans toute pneumonie sévère) contre ERS 2023 (seulement en cas de choc, non applicable aux pneumonies virales) ; arbitrage exposé dans `j12-contentieux-cortico`, source la plus récente retenue pour la pneumonie sévère de cause bactérienne ou indéterminée, décision individuelle pour la pneumonie virale non COVID.
7. **ECIL** : lu sous forme de diaporamas finaux (ECIL-7, ECIL-10), non des articles intégraux ; niveaux de preuve souvent BIII ou CIII.
8. **Résumés seulement** pour plusieurs essais et consensus (voir tableau) ; les chiffres repris figurent dans ces résumés.
9. **EACS** : version 12.0 lue ; la version 13 existe en application web, son résumé des changements ne touche pas la pneumocystose.
10. **Épidémiologie suisse** : rapport Sentinella 2023/2024, le plus récent trouvé ; données ambulatoires, non spécifiques des pneumonies.
11. **Glossaire** : la clé `RECOVERY` existe déjà (i35, essai de chirurgie de la sténose aortique). Pour éviter un renvoi faux, le cours écrit « Recovery » en casse mixte ; le relecteur peut préférer renommer la clé d’i35. Les nouvelles clés génériques `SARS`, `SARS-CoV`, `MERS` s’appliqueront aussi aux autres cours (définitions neutres). « ALAT » est évité : la recommandation 2023 est écrite « ERS, ESICM, ESCMID et Asociación Latinoamericana de Tórax ».
12. **Mobile** : les tableaux à trois colonnes défilent horizontalement à 390 px, comme dans J84 injecté (comportement du moteur, hors de mes fichiers) ; aucun débordement de page (scrollWidth = 390).
13. `tests/audit_sciences.py` exigera d’ajouter J12 à la liste des nouvelles productions sans base Git (décision du relecteur).

## Contrôles effectués (copie scratchpad : dépôt + `chapters/J12` + `glossary/j12.py` + entrée J12 temporaire dans une copie de `chapters.json`)

- `python3 build_medina.py J12` : **`J12 non couvertes: 0`**, six Pareto calculés (5 à 12 % du texte).
- Clés : 51 `data-k`, toutes avec leur `template data-pop` ; toutes préfixées `j12-` ou `pareto-j12-` ; aucun identifiant dupliqué ; aucune fenêtre orpheline.
- Contrat Sciences (logique de `tests/audit_sciences.py`) : 4 disciplines de 349 à 441 mots, une figure légendée et accessible chacune, les quatre liens présents, navigation complète.
- `test_preview.py J12` (Chromium headless 140, build 1187, installé pour l’occasion) : seul échec, l’erreur d’environnement `preview/lesson-core.js` absent de la coque, identique à celle signalée pour J84. Contrôle Playwright complémentaire : 70 mots verts cliqués dans les quatre onglets et les quatre disciplines, aucune « Fiche absente », 6 Pareto ouverts, **aucune erreur JavaScript** hors `lesson-core.js` ; rendu ordinateur et mobile vérifié visuellement (captures de travail dans le scratchpad, non livrées).
- Volume : environ 16 000 mots (cours, fenêtres, références), 45 fenêtres, 6 Pareto, 5 quiz, 5 figures SVG.
- Non fait (rôle du relecteur) : captures `tools/capture_lecon.py`, build `--all-fragments`, tests unitaires, entrée `chapters.json` (`covers` : J12, J16, J17), injection et scellement.
