# Rapport d’auteur — R04 — Hémoptysie (P-02-Pneumologie)

Rédacteur de la chaîne interne Claude, 09.10.2026. Cours unique couvrant R04 (hémoptysie et autres hémorragies des voies respiratoires), approche symptomatique de l’adulte ; l’épistaxis et le saignement pharyngé ne sont traités qu’en diagnostic différentiel. **Version de travail : ni relue par l’agent différé, ni injectée, ni validée par un médecin.** Revue IA et contrôles techniques seulement.

## Fichiers

- `chapters/R04/R04_a.html` — en-tête, onglets, onglet Pathologie îlots 0 à 6 (figure 1, Pareto clinique).
- `chapters/R04/R04_b.html` — îlots 7 à 12 (quiz, Pareto diagnostic, Pareto urgence et traitement, Pareto suivi et critères) ; dernier îlot : critères formels `div.alert` puis paramètres clés `div.key`.
- `chapters/R04/R04_c.html` — Examens (4 îlots, 4 quiz, Pareto) et Sciences (Anatomie, Anatomopathologie vasculaire, Physiologie, Hémostase et pharmacologie ; figures 2 à 5 `role="img"` légendées ; liens Science → clinique / examen / traitement / À retenir).
- `chapters/R04/R04_d.html` — Pharmacologie (4 îlots, Pareto) ; ferme le template.
- `chapters/R04/R04_pop1.html` — 35 fenêtres cliniques, diagnostiques et thérapeutiques, dont deux fenêtres de contentieux.
- `chapters/R04/R04_pop2.html` — 6 monographies (acide tranexamique, acide tranexamique nébulisé, terlipressine, concentré de complexe prothrombinique, idarucizumab, andexanet alfa) et 6 Pareto.
- `glossary/r04.py` — 1 clé nouvelle : `CIRSE`. Absente de `glossary/*.py` et des glossaires des dossiers `livraisons/Livraison Claude/*/travail/*/glossary/` (vérifié au début et à la fin de la rédaction, 09.10.2026). Toutes les autres abréviations employées (SpO₂, VEMS, INR, AOD, ECG, BPCO, SPLF, ERS, ESCMID, NICE, UI, PaO₂, TDM…) existent déjà ; les autres termes sont écrits en toutes lettres (embolisation des artères bronchiques, bacilles acido-alcoolo-résistants, anticorps anticytoplasme des neutrophiles, oto-rhino-laryngologique).

## Plan

Pathologie : 0 question clinique (fumeur de 58 ans, 100 mL de sang) ; 1 définition, pseudo-hémoptysie et degrés de gravité (tableau abondance, terrain, tolérance ; fenêtre de contentieux sur la définition de l’hémoptysie grave) ; 2 épidémiologie et pronostic (base hospitalière française, cohorte italienne ; lacune suisse nommée) ; 3 physiopathologie (double circulation, hypervascularisation systémique, asphyxie ; figure 1) ; 4 étiologies par mécanisme (règles : l’anticoagulant révèle une lésion ; la BPCO n’est pas une cause) ; 5 anamnèse (cartes forme typique et formes trompeuses) ; 6 examen ; 7 diagnostic (angioscanner examen clé, radiographie, bronchoscopie, biologie, différentiel hiérarchisé, quiz) ; 8 hémoptysie grave (`alert`), score de Fartoukh, complications ; 9 traitement (voies aériennes, endoscopie, embolisation, terlipressine et acide tranexamique, chirurgie, cause) ; 10 suivi et récidive ; 11 situations particulières (anticoagulé, cancer, aspergillome, grossesse, insuffisance rénale, enfant, cas récapitulatif) ; 12 critères formels et paramètres clés.

Renvois sans redéveloppement : J47 — Bronchectasies, I26 — Embolie pulmonaire, C34 — Cancer bronchopulmonaire (dans les fenêtres et le cas), J18 — Pneumonie (en-tête). Le code CIM n’apparaît que dans l’en-tête.

## Sources consultées (09.10.2026)

| Source | Mode d’accès réel |
|---|---|
| Théone S, Adler D, Schneider PA, Gasche-Soccal P, Younossian AB. Prise en charge de l’hémoptysie massive. Rev Med Suisse 2015;11:2157-62 (PMID 26742236), revmed.ch | Texte intégral HTML (page revmed.ch) ; notice de l’archive ouverte UNIGE |
| Collège des enseignants de pneumologie (SPLF), item 205 Hémoptysie, 2023 (cep.splf.fr, PDF) | Texte intégral PDF (pdftotext) |
| Kettenbach J et al. CIRSE Standards of Practice on Bronchial Artery Embolisation. Cardiovasc Intervent Radiol 2022 (PMID 35396612, PMC9117352) | Texte intégral PMC (XML) |
| Ittrich H et al. The diagnosis and treatment of hemoptysis. Dtsch Arztebl Int 2017 (PMID 28625277, PMC5478790) | Texte intégral PMC (HTML) |
| Fartoukh M et al. Respir Res 2007 (PMID 17302979, PMC1802746) | Texte intégral PMC |
| Mondoni M et al. Respir Res 2021 (PMID 34348724, PMC8336236) | Texte intégral PMC |
| Prutsky G et al. Cochrane 2016, CD008711.pub3 (PMID 27806184, PMC6464927) | Résumé et texte PMC disponible (résumé en langage simple, résultats principaux) |
| Moen CA et al. Interact Cardiovasc Thorac Surg 2013 (PMID 23966576, PMC3829500) | Résumé |
| Abdulmalak C et al. Eur Respir J 2015 (PMID 26022949) | Résumé |
| Fartoukh M et al. Respiration 2012 (PMID 22025193) | Résumé (score et probabilités) |
| Revel MP et al. AJR 2002 (PMID 12388502) ; Khalil A et al. Chest 2008 (PMID 17989162) ; Savale L et al. AJRCCM 2007 (PMID 17332480) | Résumés |
| Denning DW et al., ERS et ESCMID, aspergillose pulmonaire chronique, Eur Respir J 2016 (PMID 26699723) | Résumé (texte intégral ERJ inaccessible : 403) |
| Parrot A et al. Hémorragie alvéolaire, Rev Mal Respir 2015 (PMID 25891303) | Résumé |
| Forster F, Schulte W. Hämoptysen in der Schwangerschaft, Pneumologie 2019 (PMID 30895588) | Résumé (allemand et anglais) |
| Kovacs G et al. Eur Respir J 2009 (PMID 19324955) | Résumé ; seuil ESC/ERS 2022 de 20 mmHg lu dans Kularatne et al., PMC10971453 (non cité dans le cours) |
| Wand O et al. Chest 2018 (PMID 30321510) ; Gopinath B et al. Chest 2023 (PMID 36410494) | Résumés (essais cités comme données, non comme recommandations) |
| NICE NG12, recommandation 1.1.1 (nice.org.uk) | Texte intégral HTML |
| Informations professionnelles suisses via `tools/swissmedic_fi.py` (AmiKo) : Cyklokapron® (juin 2026), Tranexamic acid Leman® solution injectable (février 2024), Glypressine® (mars 2024), Beriplex® P/N (octobre 2022), Praxbind® (mars 2021), Ondexxya® (avril 2025) | Texte intégral ; Indications, Posologie, Contre-indications, Mises en garde, Interactions, Grossesse, Mécanisme lus pour chaque molécule citée |

Tous les liens du cours (26 URL externes) ont été testés : HTTP 200 pour revmed.ch, cep.splf.fr, PMC, NICE et AmiKo ; les 11 pages pubmed.ncbi.nlm.nih.gov répondent 203 avec une page de contrôle anti-robot dans cet environnement, mais leurs 11 PMID ont été vérifiés par `esummary` (premier auteur, année, revue, titre concordants). Aucune recommandation américaine ne fonde une conduite ; les essais Wand (Israël) et Gopinath (Inde), publiés dans Chest, sont cités comme données.

## Arbitrages

1. **Définition de l’hémoptysie grave (fenêtre `r04-contentieux-massive`)** : Rev Med Suisse 2015 (> 250 mL/24 h ou hémoptysie continue menaçante), revue allemande 2017 (100 à 1000 mL), CIRSE 2022 (> 100 mL/24 h, insuffisance respiratoire imposant l’intubation, instabilité hémodynamique), SPLF 2023 (≥ 200 mL chez le sujet sain, terrain, persistance). Source primaire applicable la plus récente retenue : SPLF 2023 (approche fonctionnelle) ; seuil CIRSE conservé pour l’indication d’embolisation.
2. **Terlipressine avant l’embolisation (fenêtre `r04-contentieux-terlipressine`)** : Rev Med Suisse 2015 (vasoconstricteur de choix de toute hémoptysie majeure active) contre Fartoukh 2007, CIRSE 2022 (facteur de récidive) et SPLF 2023 (réservée à l’embolisation indisponible ou à la menace vitale immédiate). Retenu : SPLF 2023, concordant avec CIRSE ; position suisse 2015 exposée.
3. **Ordre angioscanner et bronchoscopie** : SPLF 2023 et CIRSE 2022 (angioscanner d’abord, sauf voies aériennes à sécuriser) préférés à l’ordre non tranché d’Ittrich 2017.

## Réserves honnêtes

1. **Aucune validation médicale humaine.** Version de travail revue par IA.
2. **Swiss Medical Forum inaccessible** : les articles SMF repérés (DOI fms.2018.03194 et fms.2014.01825) n’ont pas pu être lus (medicalforum.ch et smf.swisshealthweb.ch refusés par le proxy, DNS en échec pour WebFetch) ; ils ne sont pas cités. La source suisse lue est la Revue médicale suisse 2015 (Hôpitaux universitaires de Genève), datée.
3. **Aucune recommandation DGP/AWMF ni ERS dédiée à l’hémoptysie trouvée** ; les revues allemandes de *Pneumologie* (Pizarro 2023, DOI 10.1055/a-1854-3022 ; DOI 10.1055/a-2061-9573) sont restées inaccessibles (Thieme protège par un écran anti-robot) et ne sont pas citées. La revue *Breathe* 2025 (« Massive » haemoptysis) est d’auteurs américains et décrit une simulation : non retenue.
4. **Hors indication suisse** : acide tranexamique dans l’hémoptysie (aucune information professionnelle ne la cite ; schémas autorisés les plus proches rapportés), acide tranexamique nébulisé (aucune forme pour inhalation ; schémas des essais), terlipressine (indication limitée aux varices œsophagiennes hémorragiques).
5. **Vitamine K adulte** : AmiKo ne renvoie que l’information professionnelle de Konakion MM paediatric pour les deux GTIN ; la dose adulte n’a pas été lue et n’est pas donnée (lacune nommée dans `r04-d-pcc`).
6. **Données suisses d’épidémiologie** : aucune trouvée ; lacune nommée dans l’îlot 2.
7. **Pédiatrie et grossesse** : aucune conduite européenne spécifique lue ; l’enfant est déclaré hors champ, la grossesse traitée par les informations professionnelles et un cas publié.
8. **Résumés seulement** pour plusieurs études (voir tableau) ; les chiffres repris figurent dans ces résumés.
9. **Tuberculose** : le guide suisse « La tuberculose en Suisse » (plateforme FMH) n’a été atteint que par sa fiche descriptive ; aucune règle d’isolement n’est donc énoncée, seule la recherche de bacilles acido-alcoolo-résistants (SPLF 2023).
10. **Mobile** : à 390 px, aucun débordement de page (scrollWidth ≤ 390 dans les quatre onglets) ; les tableaux à trois ou quatre colonnes défilent dans leur conteneur, comme dans J84 injecté.
11. `tests/audit_sciences.py` exigera d’ajouter R04 à la liste des nouvelles productions sans base Git (décision du relecteur).
12. **Scratchpad partagé** : le fichier `eu.sh` à la racine du scratchpad a été écrit par ce rédacteur (fonctions E-utilities) ; s’il existait auparavant pour un autre rédacteur, il a été remplacé. Une copie se trouve dans `r04src/eu.sh`. Les autres fichiers de travail sont sous `r04src/`, `r04ov/`, `r04tools/`, `r04shots/`.

## Contrôles effectués (copie scratchpad `r04ov` : dépôt + `chapters/R04` + `glossary/r04.py` + entrée R04 temporaire dans une copie de `chapters.json`)

- `python3 build_medina.py R04` : **`R04 non couvertes: 0`** ; six Pareto calculés (6 à 12 % du texte couvert).
- Clés : 47 `data-k` distincts (58 boutons), 47 `template data-pop`, toutes préfixées `r04-` ou `pareto-r04-` ; aucun identifiant dupliqué ; aucune fenêtre orpheline ni manquante.
- Contrat Sciences (logique de `tests/audit_sciences.py`) : 4 disciplines de 348 à 391 mots, une figure légendée et accessible chacune, les quatre liens présents, navigation complète.
- Playwright (Chromium 1194 de `/opt/pw-browsers`) : 58 mots verts cliqués dans les quatre onglets et les quatre disciplines, aucune « Fiche absente », 6 Pareto ouverts avec leur fraction ; seule erreur JavaScript : `preview/lesson-core.js` absent de la coque (erreur d’environnement identique à celle signalée pour J12 et J84) ; rendu ordinateur et mobile vérifié visuellement (captures de travail dans `r04shots/`, non livrées).
- Volume : environ 14 200 mots (cours, fenêtres, références), 41 fenêtres et 6 Pareto, 5 quiz, 5 figures SVG.
- Non fait (rôle du relecteur) : captures `tools/capture_lecon.py`, build `--all-fragments`, tests unitaires, entrée `chapters.json` (`covers` : R04), injection et scellement.
