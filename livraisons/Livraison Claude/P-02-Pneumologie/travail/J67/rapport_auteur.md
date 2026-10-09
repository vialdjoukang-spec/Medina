# Rapport d’auteur — J67 — Pneumopathies d’hypersensibilité et maladies des poussières organiques (P-02-Pneumologie)

Rédacteur de la chaîne interne Claude, 09.10.2026. Cours unique couvrant J66 et J67. **Version de travail : ni relue par l’agent différé, ni injectée, ni validée par un médecin.** Revue IA et contrôles techniques seulement.

## Fichiers

- `chapters/J67/J67_a.html` — en-tête (renvois J84, J45, J44), onglets, onglet Pathologie îlots 0 à 6 (figure 1, Pareto clinique).
- `chapters/J67/J67_b.html` — îlots 7 à 13 (Pareto diagnostic, Pareto traitement-byssinose-prévention, Pareto critères) ; dernier îlot : critères formels `div.alert` puis paramètres clés `div.key`.
- `chapters/J67/J67_c.html` — Examens (4 îlots, 4 quiz, Pareto) et Sciences (Anatomie, Histologie, Immunologie, Physiologie, Microbiologie ; 5 figures SVG `role="img"` légendées ; liens Science → clinique / examen / traitement / À retenir).
- `chapters/J67/J67_d.html` — Pharmacologie (4 îlots, Pareto) ; ferme le template.
- `chapters/J67/J67_pop1.html` — 35 fenêtres cliniques, diagnostiques et professionnelles (dont la fenêtre de contentieux `j67-contentieux`).
- `chapters/J67/J67_pop2.html` — 12 fenêtres (7 fiches d’examens et 5 monographies) et 6 Pareto.
- `glossary/j67.py` — 9 clés nouvelles : PHS, ODTS, Th1, FFP2, OLAA, LAA, RELIEF, S2k, STOP. Aucune n’existe dans `glossary/*.py` ni dans les glossaires des dossiers `livraisons/Livraison Claude/*/travail/*/glossary/` (revérifié en fin de rédaction, 09.10.2026).

## Plan

Pathologie : 0 question clinique (agriculteur laitier, accès fébriles après le foin) ; 1 définitions et classification (aiguë/chronique puis fibrosante/non fibrosante ; byssinose et ODTS situés) ; 2 épidémiologie et pronostic ; 3 physiopathologie (figure) ; 4 antigènes, sources et terrain ; 5 anamnèse (questionnaire suisse) ; 6 examen ; 7 diagnostic (critères S2k, niveaux de confiance 2020, différentiels hiérarchisés) ; 8 gravité et complications (`alert` en tête) ; 9 traitement (éviction, glucocorticoïdes, épargne, nintédanib, pirfénidone, transplantation) ; 10 byssinose et maladies des voies aériennes (J66) ; 11 suivi, prévention et maladie professionnelle (LAA, OLAA) ; 12 situations particulières et cas récapitulatif ; 13 critères formels et paramètres clés.

Articulation avec J84 : J84 renvoie la PHS à J67 (fenêtre `j84-hypersensibilite`) ; J67 renvoie à J84 dans l’en-tête et traite la FPI comme différentiel sans la redévelopper. Le code CIM n’apparaît que dans l’en-tête.

## Sources consultées (09.10.2026)

| Source | Mode d’accès réel |
|---|---|
| Koschel et al., recommandation S2k DGP/DGAKI sur la PHS, Respiration 2025 (PMID 39870058, PMC12215178 ; version allemande Pneumologie 2024, PMID 39227017) | **Texte intégral** (efetch PMC), toutes sections lues : définition, classification, épidémiologie, facteurs de risque, pathogenèse, variantes et tableaux 2–3, anamnèse, IgG, radiologie (tableaux 4–6), LBA, histologie (tableaux 7–8), provocation, éviction, critères (tableau 9), différentiel, traitement R10–R12, prévention, pronostic, maladie professionnelle |
| Raghu et al., recommandation ATS/JRS/Asociación Latinoamericana de Tórax 2020 (PMID 32706311, PMC7397797) | **Texte intégral** : résumé des recommandations, définition, sous-types, histoire naturelle, épidémiologie, pathogenèse, génétique, radiologie (tableaux 4–6), critères diagnostiques, question 3 (LBA) |
| Quirce et al., prise de position EAACI, Allergy 2016 (PMID 26913451) | Résumé |
| Pohle et al., questionnaire suisse d’exposition, Respiration 2023 (PMID 37088078) | Notice bibliographique seulement (pas de résumé ; texte Karger payant) |
| Schumacher, Clarenbach, Dressel, Ther Umsch 2024 (PMID 38655831, revue suisse) | Résumé (FR/DE) |
| Lacasse et al. 2003 (12842854) ; Kokkarinen 1992 (1731594) ; Mönkäre 1983 (6861923) ; De Sadeleer 2018 (30577667) ; Gimenez 2018 (28883091) ; Fernández Pérez 2013 (23828161) ; Tsutsui 2015 (26010749) ; Wells, INBUILD sous-groupes 2020 (32145830) ; Behr, RELIEF 2021 (33798455) | Résumés PubMed |
| Salisbury et al., Chest 2019 (PMC6514431) ; Nosotti et al., Transpl Int 2022 (PMC9008138) ; Spagnolo et al., Lancet Respir Med 2025 (PMC12538297) | Texte intégral (passages cités) |
| Byssinose : Nafees et al. 2023, Multitex (PMC9985716) | Texte intégral ; Nafees 2022 (35073782), Nafees 2024 ERJ (37857425), Shi 2010 EHP (20797932), Shi 2010 AJRCCM (PMC2913234, résumé), Christiani 1999 (10086207), Er 2016 (26489943) : résumés |
| ODTS : Vogelzang 1999 (10086208) | Résumé |
| LAA, art. 9 (RS 832.20) et OLAA, annexe 1, ch. 2 let. b (RS 832.202), état au 01.01.2026 | Texte intégral HTML Fedlex (via le point SPARQL officiel) |
| CIM-10-GM 2024, bloc J60–J70 (BfArM) | Texte intégral HTML (périmètre seulement, non cité) |
| Informations professionnelles suisses via `tools/swissmedic_fi.py` (AmiKo) : Ofev (03.2025), Esbriet (08.2022), Imurek (04.2026), CellCept Roche (09.2025), Prednisone Streuli (06.2026), Spiricort (06.2026, lu pour comparaison) | Texte intégral ; indications, posologie, contre-indications, mises en garde, interactions, grossesse, mécanisme |

Tous les liens externes (28) testés : HTTP 200 (PubMed renvoie 203 via le mandataire, page servie) ; les 18 PMID cités vérifiés par `esummary` (premier auteur, année, revue concordants).

## Arbitrages

1. **Source principale = S2k allemande 2024/2025** (européenne, la plus récente). La recommandation de 2020 est **ATS/JRS/Asociación Latinoamericana de Tórax** et **non ERS** contrairement à l’intitulé de la consigne : l’ERS ne la cosigne pas. Elle est présentée comme « recommandation internationale de 2020 » (non « ATS seule ») et utilisée pour la définition, la grille TDM et les niveaux de confiance ; la recommandation CHEST 2021 (américaine) n’est pas utilisée.
2. **Contentieux** S2k 2024 contre 2020 (classification, TDM, questionnaire, critères, cryobiopsie, provocation) exposé dans `j67-contentieux` ; la source primaire la plus récente (S2k) l’emporte ; le texte 2020 reste accessible.
3. **Abréviations** : « ALAT » évité pour la société latino-américaine (la clé `ALAT` = alanine aminotransférase, b18) ; « HP », « TLR2 », « IL-8 », « R1… », « Royaume-Uni » réécrits pour ne pas créer de clés ambiguës.

## Réserves honnêtes

1. **Aucune validation médicale humaine.**
2. **Hors indication suisse** : azathioprine, mycophénolate, pirfénidone, rituximab dans la PHS ; glucocorticoïdes : PHS non nommée (indication « états allergiques graves »). Aucune dose de mycophénolate propre à la PHS dans les sources lues (dose de transplantation rénale citée comme telle).
3. **Lacunes nommées** : aucune incidence suisse publiée ; questionnaire suisse non lu au-delà de sa notice ; documents et procédure d’annonce de la Suva non lus ; aucune recommandation européenne sur le traitement médicamenteux de la byssinose ; aucune donnée européenne récente propre à la maladie du lin et à la cannabinose ; mécanisme des couinements non détaillé.
4. **Résumés seulement** pour plusieurs essais et cohortes (voir tableau) ; EAACI 2016 lue en résumé.
5. Faits d’anatomie et d’histologie normales limités à ce que disent les sources lues (pas de manuel d’anatomie consulté) ; un relecteur peut enrichir avec une source histologique.
6. `tests/audit_sciences.py` exigera d’ajouter J67 à la liste des nouvelles productions sans base Git ; ce test échoue de toute façon dans le clone actuel sur I50 (base Git absente), indépendamment de J67.
7. J84 injecté écrit « ATS/ERS/JRS/ALAT » : « ALAT » y est relié à la clé alanine aminotransférase (signalement hors de mon périmètre).

## Contrôles effectués (copie scratchpad : dépôt + `chapters/J67` + `glossary/j67.py` + entrée temporaire J67, `covers` J66 et J67, dans une copie de `chapters.json`)

- `python3 build_medina.py J67` : **`J67 non couvertes: 0`** ; six Pareto calculés (6 à 22 % du texte).
- Clés : 53 `data-k`, 53 `template data-pop`, aucune manquante ni orpheline, aucune clé ni identifiant dupliqué, toutes préfixées `j67-` / `pareto-j67-` ; classes de la liste fermée uniquement.
- Contrat Sciences (logique de `tests/audit_sciences.py`) : navigation complète ; 5 disciplines de 339 à 437 mots, une figure légendée et accessible chacune, quatre liens présents.
- Playwright (Chromium `/opt/pw-browsers/chromium-1194`) : 60 clics sur mots verts et boutons Pareto dans les quatre onglets et les cinq disciplines, **aucune « Fiche absente »** ; seule erreur JavaScript : `preview/lesson-core.js` non chargé en `file://` (environnement, identique à J84/J12) ; mobile 390 px : `scrollWidth` = 390, aucun défilement horizontal de page. Captures de travail dans le scratchpad (non livrées).
- Volume : environ 16 000 mots (cours, fenêtres, références), 47 fenêtres + 6 Pareto, 4 quiz, 6 figures SVG.
- Non fait (rôle du relecteur) : captures `tools/capture_lecon.py`, build complet, tests unitaires, entrée `chapters.json`, injection et scellement.
