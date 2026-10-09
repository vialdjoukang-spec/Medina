# Rapport d’auteur — R06 — Dyspnée et anomalies de la respiration (P-02-Pneumologie)

Rédacteur de la chaîne interne Claude, 09.10.2026. Cours unique couvrant toute la catégorie R06 (dyspnée aiguë et chronique, orthopnée, stridor, sifflement, respiration périodique de Cheyne-Stokes, hyperventilation, hoquet). **Version de travail : ni relue par l’agent différé, ni injectée, ni validée par un médecin.** Revue IA et contrôles techniques seulement.

## Fichiers

- `chapters/R06/R06_a.html` — en-tête, onglets, onglet Pathologie îlots 0 à 6 (figure 1, Pareto clinique).
- `chapters/R06/R06_b.html` — îlots 7 à 14 (Pareto diagnostic-urgences-traitement, Pareto anomalies-fin de vie, Pareto critères) ; dernier îlot : critères formels `div.alert` puis paramètres clés `div.key`.
- `chapters/R06/R06_c.html` — Examens (4 îlots, 4 quiz, Pareto) et Sciences (Neurophysiologie, Mécanique ventilatoire, Échanges gazeux, Contrôle de la ventilation ; 4 figures SVG `role="img"` légendées ; liens Science → clinique / examen / traitement / À retenir).
- `chapters/R06/R06_d.html` — Pharmacologie (4 îlots, Pareto) ; ferme le template.
- `chapters/R06/R06_pop1.html` — 38 fenêtres cliniques et diagnostiques.
- `chapters/R06/R06_pop2.html` — 19 fenêtres (traitement, deux contentieux, monographies) et 6 Pareto.
- `glossary/r06.py` — 9 clés : ESMO, SFMU, SRLF, ORL, ELS, ESRS, HAS, BEAMS, MORDYC. Aucune n’existe dans `glossary/*.py`. **Collision de rédaction parallèle** : ESMO existe aussi dans `travail/J69/glossary/j69.py` et SRLF dans `travail/J95/glossary/j95.py` (dossiers non injectés) ; mes définitions sont rendues neutres, le relecteur n’en conserve qu’une. BEAMS : développement non donné dans la publication lue, écrit honnêtement comme nom propre.

## Plan

Pathologie : 0 question clinique (homme de 71 ans, dyspnée d’effort et orthopnée, double cause cardiaque et BPCO) ; 1 définitions (ATS 1999 reprise par ERS/ESMO, ERS/ESICM 2024, détresse vs insuffisance respiratoire, aiguë/chronique, syndrome de dyspnée chronique, tableau des anomalies respiratoires) ; 2 épidémiologie et pronostic (SFMU 2025, cohorte suisse de Belkin 2025, ESMO, ERS/ESICM) ; 3 genèse de la sensation (décharge corollaire, afférences, dissociation neuromécanique, composante limbique, spirale ; figure 1) ; 4 causes par étage et multimorbidité ; 5 anamnèse (descripteurs, orthopnée, équivalent angineux, mMRC, échelles, dyspnée « invisible ») ; 6 examen (fréquence respiratoire sur 30 s, SpO₂, signes de lutte et d’épuisement) ; 7 démarche aiguë (SFMU) et chronique en trois niveaux (ERS Breathe) ; 8 urgences (alerte SFMU et Revue médicale suisse, obstruction haute, épiglottite, angio-œdème, fumées) ; 9 traitement symptomatique (ERS 2024, ESMO 2020, oxygène, contentieux opioïdes) ; 10 stridor, obstruction laryngée induite, sifflement, Cheyne-Stokes (contentieux servo-ventilation), Kussmaul ; 11 hyperventilation/respiration dysfonctionnelle et hoquet ; 12 dyspnée réfractaire et fin de vie (palliative.ch Bigorio, directive Spitäler fmi 2023) ; 13 suivi et situations particulières (sujet âgé, insuffisance rénale, BPCO sévère et contre-indications Swissmedic, obésité, altitude, cas récapitulatif) ; 14 critères formels et paramètres clés.

Périmètre : les maladies causales sont renvoyées sans être redéveloppées (J45, J44, I26, I50, J96). Le code CIM n’apparaît que dans l’en-tête ; les sous-codes R06.x ne sont pas cités (ils déclenchaient l’audit des abréviations). Remarque pour le relecteur : dans la CIM-10-GM 2024 (BfArM, lue le 09.10.2026), l’hyperventilation psychogène et le hoquet psychogène sont exclus de R06 (F45.33) ; le cours traite néanmoins le syndrome d’hyperventilation comme diagnostic différentiel de la dyspnée.

## Sources consultées (09.10.2026)

| Source | Mode d’accès réel |
|---|---|
| Le Borgne et al., recommandations SFMU/SRLF « Prise en charge de la dyspnée aiguë en urgence », validées mars-mai 2025 (sfmu.org) | Texte intégral PDF (pdftotext) : définitions, champs 1 à 3, argumentaires |
| Holland et al., recommandation ERS sur les symptômes des maladies respiratoires graves, Eur Respir J 2024 (PMID 38719772) | **Résumé seulement** (texte intégral bloqué, HTTP 403 sur ersnet.org, non libre sur PMC) |
| Holland et Lewis, Eur Respir Rev 2024 (PMC11522974) | Texte intégral (éditorial de synthèse des revues préparatoires) |
| Smallwood et al., opioïdes, Eur Respir Rev 2024 (PMC11462312) ; Ahmadi et al., oxygène, Eur Respir Rev 2025 (PMC11880903) | Résumés (chiffres repris) |
| Hui et al., recommandation ESMO sur la dyspnée du cancer, ESMO Open 2020 (PMC7733213) | Texte intégral : introduction, évaluation, encadré des recommandations, section opioïdes |
| Johnson et al., syndrome de dyspnée chronique, Eur Respir J 2017 (PMID 28546269) | Résumé |
| Demoule et al., déclaration ERS/ESICM, Eur Respir J 2024 (PMID 38387998) | Résumé ; définition reprise via SFMU 2025 |
| Keane et Brennan, Breathe (ERS) 2025 (PMC11915126) ; Nic Aodha Bhuí et Fahy, Breathe 2025 (PMC12171858) | Texte intégral |
| O’Donnell et al., Adv Ther 2020 (PMC6979461) | Texte intégral (mécanismes, tableaux 1 et 3) |
| Elbehairy et al., orthopnée et BPCO, Eur Respir J 2021 (PMID 32972985) | Résumé |
| Belkin et al., Swiss Medical Weekly 2025 (doi 10.57187/s.3785) | Résumé |
| Bestall et al., Thorax 1999 (PMID 10377201) ; HAS, guide du parcours BPCO 2019 (tableau 4, échelle mMRC en français) | Résumé ; texte intégral PDF HAS |
| Lavanchy et al., « Dyspnée haute chez l’adulte », Revue médicale suisse 2015 | Texte intégral PDF |
| Halvorsen et al., déclaration ERS/ELS sur l’obstruction laryngée induite, 2017 (PMID 28889105) | Résumé |
| Ludlow et al., Breathe 2023 (PMC10567073) ; Robson, Breathe 2017 (PMC5343732) | Texte intégral |
| Randerath et al., Eur Respir Rev 2024 (PMC10966472) | Texte intégral (passages ciblés : définitions, gain de boucle, seuil d’apnée, insuffisance cardiaque, altitude, opioïdes) |
| Randerath et al., déclaration ERS/ESRS 2025 sur la servo-ventilation (PMID 40571320) ; Cowie et al., SERVE-HF, 2015 (PMID 26323938) | Résumés |
| Du Pasquier et al., Revue médicale suisse 2020 (PMID 32558453) ; Sauty, Revue médicale suisse 2008 (PMID 19127893) | Résumés (articles payants) |
| Canonica et al., hoquet chronique, Revue médicale suisse 2024 ; Steger et al., Aliment Pharmacol Ther 2015 (PMID 26307025) ; Alshargi et al., 2026 (PMC13340612) | Résumés (Canonica, Steger) ; texte intégral (Alshargi) |
| Guglielmo et al. 2023 et Aubagnac et al. 2025, platypnée-orthodéoxie, Revue médicale suisse | Résumés |
| Schreier et al., Revue médicale suisse 2025 | Résumé (cité une fois, article payant) |
| palliative.ch, recommandations Bigorio sur la dyspnée, 2003 (versions française et allemande) | Texte intégral PDF |
| Spitäler Frutigen Meiringen Interlaken, directive « Dyspnoe in der Palliative Care », 26.01.2023 | Texte intégral PDF |
| Service de soins palliatifs du CHUV, Palliative Flash n° 11, 2008 | Texte intégral PDF |
| Abernethy et al., Lancet 2010 (PMC2962424) ; Galbraith et al., 2010 (PMID 20471544) ; Ekström et al., BEAMS 2022 (PMC9682426) ; Verberkt et al., MORDYC 2020 (PMC7432282) | Résumés |
| Informations professionnelles suisses via `tools/swissmedic_fi.py` (AmiKo) : Morphini HCl Streuli® (01.2026), Sevredol® (05.2024), Palladon® (04.2026), Temesta® (11.2022), Dormicum® injectable (04.2026), Liorésal® (01.2025), Neurontin® (04.2025), Paspertin® (01.2020), Nozinan® (10.2022), Haldol® (11.2024) | Texte intégral ; indications, posologie, contre-indications, mises en garde, mécanisme |
| CIM-10-GM 2024, bloc R00–R09 (BfArM) | Texte intégral HTML (périmètre seulement) |

Liens : 38 URL externes testées, toutes en succès (HTTP 200 ; PubMed répond 203 via le mandataire). Les 12 PMID et 14 PMCID ont été vérifiés (esummary et Europe PMC : premier auteur, année, revue concordants). Aucune recommandation américaine ne fonde une conduite : la définition ATS 1999 est citée parce que l’ERS et l’ESMO la reprennent ; la définition polysomnographique de Cheyne-Stokes est attribuée à l’American Academy of Sleep Medicine telle que citée par la revue ERS ; GINA 2024 n’intervient qu’au travers de Keane (seuil de réversibilité).

## Arbitrages

1. **Contentieux opioïdes** (fenêtre `r06-contentieux-opioides`) : Bigorio 2003 (morphine premier choix) / ESMO 2020 (cancer : morphine orale 10–30 mg/24 h en première intention pharmacologique) / ERS 2024 (maladies respiratoires graves : suggère de ne pas utiliser les opioïdes). Source primaire applicable la plus récente : ERS 2024 hors cancer ; ESMO 2020 dans le cancer ; derniers jours de vie : aucun essai, pratique suisse palliative.ch. Textes en vigueur liés.
2. **Oxygène** : Bigorio 2003 (efficace même sans hypoxémie) supplanté par ERS 2024 et ESMO 2020 ; exposé dans `r06-oxygene`.
3. **Servo-ventilation** (`r06-contentieux-asv`) : SERVE-HF et revue ERS 2024 (contre-indication si FEVG < 45 %) contre déclaration ERS/ESRS 2025 (plus récente, pratique d’experts) ; retenue comme la plus récente en précisant qu’il ne s’agit pas d’une recommandation formelle.
4. **Bigorio, divergence interne** : morphine initiale 5 mg/4 h (version française) contre 2,5 mg/4 h (version allemande) ; les deux sont signalées dans `r06-d-morphine`.

## Réserves honnêtes

1. **Aucune validation médicale humaine.**
2. **Hors indication suisse** : tous les traitements symptomatiques (morphine, hydromorphone, midazolam sous-cutané, lorazépam pour la dyspnée, baclofène, gabapentine, métoclopramide pour le hoquet). **Contre-indication Swissmedic** : Sevredol® et Palladon® dans la BPCO ou l’asthme sévères — exposée en alerte (îlot p-3) et dans l’îlot 13.
3. **Lacunes nommées** : aucune information professionnelle suisse de la chlorpromazine sur AmiKo ; aucune dose suisse de baclofène ou de gabapentine pour le hoquet ; adrénaline en aérosol non vérifiée dans une information professionnelle suisse ; glycopyrronium et butylscopolamine (râles terminaux) cités d’après Bigorio 2003 sans vérification Swissmedic ; position de la recommandation ESC sur l’insuffisance cardiaque et la servo-ventilation non relue (texte ESC bloqué, HTTP 403) ; seuils chroniques du peptide natriurétique renvoyés à I50 pour la même raison ; aucune prévalence suisse de la dyspnée chronique en population générale ; aucun texte mediX consacré à la dyspnée n’a pu être consulté (site à accès réservé) ; grossesse non traitée faute de source lue.
4. **Résumés seulement** pour la recommandation ERS 2024 (texte intégral inaccessible) et plusieurs essais et articles suisses payants ; les chiffres repris figurent dans ces résumés.
5. **Bigorio 2003** est ancien mais reste le texte en vigueur publié par palliative.ch ; la directive bernoise de 2023 (Spitäler fmi) est un document hospitalier régional, non une recommandation nationale.
6. **Volume** : environ 16 800 mots tout compris (cours 9 300, fenêtres 7 400, y compris textes des figures et références), légèrement au-dessus de la cible indicative ; le relecteur peut condenser certaines fenêtres (urgences ORL, monographies).
7. `tests/audit_sciences.py` exigera d’ajouter R06 à la liste des nouvelles productions sans base Git (décision du relecteur).

## Contrôles effectués (copie scratchpad : dépôt + `chapters/R06` + `glossary/r06.py` + entrée R06 temporaire dans une copie de `chapters.json`)

- `python3 build_medina.py R06` : **`R06 non couvertes: 0`** ; six Pareto calculés (5 à 9 % du texte couvert).
- Clés : 57 `data-k` de fenêtres + 6 Pareto, toutes avec leur `template data-pop` ; toutes préfixées `r06-` ou `pareto-r06-` ; aucun identifiant dupliqué ; aucune fenêtre orpheline ; ancres du sommaire valides.
- Contrat Sciences (logique de `tests/audit_sciences.py`) : 4 disciplines de 300 à 399 mots, une figure légendée et accessible chacune, les quatre liens présents, navigation complète.
- Playwright (Chromium 1194 de `/opt/pw-browsers`, appelé par `executable_path`, car le Playwright installé attend le build 1243 absent) : 76 mots verts cliqués dans les quatre onglets, 63 clés distinctes ouvertes, **aucune « Fiche absente »**, 6 Pareto ouverts avec fraction calculée, 4 quiz cliqués ; **aucune erreur JavaScript propre au cours** — seule erreur : `preview/lesson-core.js` absent de la coque (environnement, identique à J12 et J84) ; mobile 390 px : `scrollWidth` = 390 dans les quatre onglets. Figures relues visuellement après correction des chevauchements de libellés (captures de travail dans le scratchpad, non livrées).
- Non fait (rôle du relecteur) : captures `tools/capture_lecon.py`, build `--all-fragments`, tests unitaires, entrée `chapters.json` (`covers` : R06), injection et scellement.
