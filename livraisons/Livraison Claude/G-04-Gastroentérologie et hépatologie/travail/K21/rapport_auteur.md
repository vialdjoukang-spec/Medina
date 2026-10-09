# Rapport d’auteur — K21 — Reflux gastro-œsophagien (G-04-Gastroentérologie et hépatologie)

Rédacteur de la chaîne interne Claude, 09.10.2026. Cours unique couvrant K21.0 et K21.9, avec l’œsophage de Barrett (K22.7) traité comme complication et la hernie hiatale (K44) comme facteur et complication anatomique. **Version de travail : ni relue par l’agent différé, ni injectée, ni validée par un médecin.** Revue IA et contrôles techniques seulement.

## Fichiers

- `chapters/K21/K21_a.html` — en-tête, onglets, onglet Pathologie îlots 0 à 6 (figure 1, Pareto clinique).
- `chapters/K21/K21_b.html` — îlots 7 à 13 (1 quiz, Pareto diagnostic, Pareto urgences et traitement, Pareto Barrett-suivi-critères) ; dernier îlot : critères formels `div.alert` puis paramètres clés `div.key`.
- `chapters/K21/K21_c.html` — Examens (4 îlots, 4 quiz, Pareto) et Sciences (Anatomie, Histologie, Physiologie, Biochimie et pharmacologie moléculaire, Biologie de la cancérogenèse ; 5 figures SVG `role="img"` légendées ; liens Science → clinique / examen / traitement / À retenir).
- `chapters/K21/K21_d.html` — Pharmacologie (4 îlots, Pareto) ; ferme le template.
- `chapters/K21/K21_pop1.html` — 37 fenêtres : 34 cliniques, diagnostiques et thérapeutiques, et 3 fenêtres de contentieux.
- `chapters/K21/K21_pop2.html` — 8 monographies et 6 Pareto.
- `glossary/k21.py` — 22 clés nouvelles : RGO, IPP, SIO, TEA, LA, OGD, ESGE, UEG, EAES, DGVS, H2, LINX, ICARUS, AspECT, K21.0, K21.9, K22.7, Hvid-Jensen, Ness-Jensen, El-Serag, Savary-Miller, Pantoprazol-Mepha.

## Plan

Pathologie : 0 question clinique (homme de 52 ans, obèse, pyrosis depuis quatre ans) ; 1 définitions (Montréal/DGVS, RGO « justifiant une décision » de Lyon 2.0, quatre phénotypes, Los Angeles, Barrett, hernie hiatale) ; 2 épidémiologie (Suisse 17,6 %, Europe 8,8–25,9 %, histoire naturelle, Barrett) ; 3 physiopathologie (barrière SIO-pilier, relaxations transitoires, hernie, poche acide, clairance, perception ; figure 1) ; 4 facteurs de risque ; 5 anamnèse et signes d’alarme ; 6 examen ; 7 diagnostic (traitement d’épreuve, test IPP, OGD, pH-métrie, différentiels hiérarchisés, quiz) ; 8 complications et urgences ; 9 traitement (mesures générales, IPP, long cours par phénotype, extra-œsophagien, chirurgie) ; 10 œsophage de Barrett (Prague, Seattle, intervalles ESGE, dysplasie) ; 11 suivi, désescalade, sécurité, *H. pylori* ; 12 situations particulières (grossesse, âge, foie et rein, clopidogrel, chirurgie bariatrique, cas récapitulatif) ; 13 critères formels et paramètres clés.

Choix de périmètre : l’œsophagite à éosinophiles (K20.0), l’achalasie (K22.0) et l’adénocarcinome de l’œsophage sont traités comme diagnostics différentiels ou complications, sans développement propre. La pédiatrie est hors périmètre (cours adulte). Le code CIM n’apparaît que dans l’en-tête.

## Sources consultées (09.10.2026)

| Source | Mode d’accès réel |
|---|---|
| Gyawali et al., consensus de Lyon 2.0, Gut 2024 (PMID 37734911, PMC10846564) | Texte intégral (efetch PMC) |
| Madisch et al., recommandation DGVS S2k RGO et œsophagite à éosinophiles, mars 2023 ; version anglaise Z Gastroenterol 2024;62:1786–1852 (PDF dgvs.de) | Texte intégral des chapitres 1 à 4 (RGO, chirurgie, Barrett) via pdftotext ; chapitre 5 (œsophagite à éosinophiles) non lu sauf recommandation 1.10 |
| Weusten et al., ESGE Barrett, Endoscopy 2023 (PMID 37813356, DOI 10.1055/a-2176-2440) | Texte intégral (Thieme, rendu par navigateur sans tête) |
| Markar et al., UEG et EAES, chirurgie du RGO, UEG J 2022 (PMID 36196591, PMC9731663) | Texte intégral |
| Markar et al., EAES hernies para-œsophagiennes, Surg Endosc 2023 (PMID 37910246) | Résumé |
| Pauwels et al., ICARUS, Gut 2019 (PMID 31375601) | Résumé |
| Boeckxstaens et al., Gut 2014 (PMID 24607936, PMC4078752) | Texte intégral |
| El-Serag et al., Gut 2014 (PMID 23853213, PMC4046948) | Texte intégral (partie Europe) |
| Schwenkglenks et al., épidémiologie suisse, Soz Praventivmed 2004 (PMID 15040129) | Résumé |
| Vidonscky Lüthold et al., IPP inappropriés en médecine de famille suisse, Swiss Med Wkly 2023 (PMID 37769322) | Résumé |
| mediX, guideline « Gastroösophageale Refluxkrankheit », révision 10/2023 | Partie publique seulement (définition, épidémiologie, facteurs de risque) ; suite derrière un identifiant |
| Dalex et al. (CHUV), Rev Med Suisse 2024 ; Briner et al. (HUG), Rev Med Suisse 2026 | Résumés seulement (texte intégral payant) ; Dalex cité, Briner non cité (il s’appuie sur une recommandation américaine) |
| Frühauf, compte rendu, Ars Medici 24/2024 (PDF rosenfluh.ch) | Texte intégral ; cité seulement pour « la chirurgie ne protège pas le Barrett du cancer » |
| Hvid-Jensen et al., NEJM 2011 (PMID 21995385) ; Jankowski et al., AspECT, Lancet 2018 (PMID 30057104) ; Moayyedi et al., Gastroenterology 2019 (PMID 31152740) ; Ness-Jensen et al., 2013 (PMID 23358462) | Résumés PubMed (AspECT aussi via le texte ESGE) |
| Tack et Pandolfino 2018 (PMID 29037470) ; Herregods et al. 2015 (PMID 26053301) ; Gyawali et al., Rome 2026, Gastroenterology (PMID 42031441) ; Zerbib et al., ESNM 2021 (PMID 33368919, non cité) | Résumés |
| Lundell et al., Gut 1999 (PMID 10403727) ; Rezaeinasab et al. 2025 (PMID 41116852, PMC12535775) | Résumé (Lundell) ; texte intégral (définitions des grades de Los Angeles) |
| Vakil et al., Montréal 2006 (PMID 16928254) | Non lu ; contenu cité d’après la DGVS, mention explicite dans la fenêtre |
| CIM-10-GM 2024, blocs K20–K31 et K40–K46 (BfArM) | Texte HTML (en-tête seulement) |
| Informations professionnelles suisses via `tools/swissmedic_fi.py` (AmiKo) : Nexium (06.2026), Pantoprazol-Mepha (12.2022), PANTOZOL Control (09.2026), Antramups (06.2026), Agopton (09.2026), Pariet (06.2026), Gaviscon (06.2023), Riopan (04.2025), Liorésal (01.2025) ; recherches négatives : famotidine, ranitidine, nizatidine, cimétidine, sucralfate (Ulcogant), vonoprazan | Texte intégral ; sections Indications, Posologie, Contre-indications, Mises en garde, Interactions, Grossesse, Mécanisme et Pharmacocinétique lues pour les molécules citées |

Liens : 23 URL externes ; 13 répondent HTTP 200, les 10 pages PubMed répondent 203 via le mandataire (contenu servi). Les 19 PMID ont été vérifiés par `esummary` (premier auteur, année, revue concordants). Aucune recommandation américaine ne fonde une conduite ; Lyon 2.0 (consensus international à forte participation européenne, dont Zurich, Bordeaux, Padoue) et ICARUS (Louvain) sont retenus comme consensus internationaux.

## Arbitrages (contentieux exposés en fenêtres vertes, source primaire applicable la plus récente retenue)

1. **Grade B de Los Angeles** (`k21-contentieux-lab`) : DGVS mars 2023 (tableau Lyon 1.0 : C/D seuls concluants) contre Lyon 2.0 (2023-2024 : B concluant) → Lyon 2.0.
2. **Fundoplicature totale ou partielle** (`k21-contentieux-fundo`) : UEG/EAES nov. 2022 (partielle postérieure suggérée) contre DGVS mars 2023 (selon l’expérience du centre) → DGVS 2023.
3. **Barrett : intervalles, chimioprévention, dysplasie de bas grade** (`k21-contentieux-barrett`) : DGVS mars 2023 contre ESGE 2023 (publiée après) → ESGE ; le cas récapitulatif applique l’IPP standard quotidien suggéré par l’ESGE.
4. **Renfort prothétique du hiatus** (fenêtre `k21-hernie-pe`) : DGVS (pas systématique) contre EAES 2023 (suggéré pour les hernies para-œsophagiennes volumineuses) → EAES pour cette indication.
5. **Symptômes extra-œsophagiens** : DGVS (IPP double dose 12 semaines) et Lyon 2.0 (exploration initiale) présentés ensemble dans l’îlot 9 et la fenêtre `k21-extra`.

## Réserves honnêtes

1. **Aucune validation médicale humaine.**
2. **Aucune recommandation de la Société suisse de gastroentérologie (SGG/SSG) sur le RGO n’a été trouvée** ; mediX n’a été lu que dans sa partie publique ; les articles de la Revue Médicale Suisse n’ont été lus qu’en résumé. Les sources suisses effectivement exploitées sont Schwenkglenks 2004, Vidonscky Lüthold 2023, la partie publique de mediX, les informations professionnelles Swissmedic et un compte rendu d’Ars Medici.
3. **Hors indication suisse** signalés dans le cours : double dose d’IPP pour symptômes extra-œsophagiens ou douleur thoracique (DGVS), neuromodulateurs, baclofène. Doses des neuromodulateurs non données (aucune source lue ne les fixe).
4. **Antihistaminiques H2, sucralfate, vonoprazan** : aucune information professionnelle trouvée sur AmiKo au 09.10.2026 ; le cours le dit sans affirmer un retrait du marché.
5. **Pantoprazol-Mepha** (12.2022) a servi de référence pour le pantoprazole oral, l’information de Pantozol® oral n’ayant pas été trouvée sous ce nom ; son indication emploie encore Savary-Miller (signalé dans la fenêtre `k21-la`).
6. **Résumés seulement** pour plusieurs études (tableau) ; les chiffres repris y figurent.
7. **Épidémiologie suisse** : seule donnée trouvée de 2004.
8. **Classification de la hernie** : les types I à IV ne sont pas définis (aucune source lue ne les détaille) ; le cours suit la description mécanistique de la DGVS et mentionne les types II à IV seulement comme champ de l’EAES.
9. **Glossaire — collision** : la clé `ESGE` existe aussi dans `livraisons/Livraison Claude/H-08-Hématologie/travail/D50/glossary/d50.py` (définition orientée capsule endoscopique). Le relecteur doit conserver une seule définition générique ; celle de `k21.py` est générique. Les clés `LA`, `TEA`, `H2` sont génériques (définitions neutres) ; aucun autre cours actuel ne contient ces sigles isolés.
10. **Mobile** : tableaux à quatre colonnes défilant horizontalement dans leur conteneur, comme dans les cours injectés ; aucun débordement de page (scrollWidth = 390).
11. `tests/audit_sciences.py` exigera d’ajouter K21 à la liste des nouvelles productions sans base Git (décision du relecteur).
12. La build complète signale `I51 non couvertes: 1 NEJMoa1406761`, préexistant et indépendant de K21 (vérifié sans `k21.py`).

## Contrôles effectués (copie scratchpad : dépôt + `chapters/K21` + `glossary/k21.py` + entrée K21 temporaire dans une copie de `chapters.json`, `covers` : K21, K22.7, K44)

- `python3 build_medina.py K21` : **`K21 non couvertes: 0`** ; six Pareto calculés (5 à 10 % du texte).
- Clés : 51 `data-k`, 51 `template data-pop`, toutes préfixées `k21-` ou `pareto-k21-` ; aucune fenêtre manquante ni orpheline ; aucun identifiant dupliqué ; tous les `data-cover` pointent vers des îlots existants.
- Contrat Sciences (logique de `tests/audit_sciences.py`) : 5 disciplines de 410 à 509 mots, une figure légendée et accessible chacune, les quatre liens présents, navigation complète.
- `test_preview.py K21` (Chromium 1194 local) : seul échec, l’erreur d’environnement `preview/lesson-core.js` absent, identique à J84 et J12. Contrôle Playwright complémentaire : 60 mots verts et Pareto cliqués dans les quatre onglets et les cinq disciplines, aucune « Fiche absente », quiz fonctionnels (rétroaction affichée), **aucune erreur JavaScript** hors `lesson-core.js` ; mobile 390 px : scrollWidth 390 sur les quatre onglets. Captures de travail dans le scratchpad (non livrées).
- Volume : environ 16 700 mots (cours, fenêtres, références), 45 fenêtres et 6 Pareto, 5 quiz, 6 figures SVG, 11 tableaux.
- Non fait (rôle du relecteur) : captures `tools/capture_lecon.py`, build `--all-fragments`, tests unitaires, entrée `chapters.json` et `organisation/course_groups.json`, injection et scellement.
