# Rapport d’auteur — R05 — Toux aiguë, subaiguë et chronique (P-02-Pneumologie)

Rédacteur de la chaîne interne Claude, 09.10.2026. Cours unique couvrant R05. **Version de travail : ni relue par l’agent différé, ni injectée, ni validée par un médecin.** Revue IA et contrôles techniques seulement.

## Fichiers

- `chapters/R05/R05_a.html` — en-tête (renvois J45, J44, J40, J21), onglets, onglet Pathologie îlots 0 à 6 (figure 1 : arc réflexe et sites de sensibilisation ; Pareto clinique).
- `chapters/R05/R05_b.html` — îlots 7 à 14 (quiz diagnostique ; signes d’alarme en `div.alert` ; traitement aigu/subaigu ; traits traitables ; toux réfractaire ; suivi ; situations particulières et cas récapitulatif ; dernier îlot : critères formels `div.alert` puis paramètres clés `div.key` ; Pareto diagnostic, prise en charge, critères).
- `chapters/R05/R05_c.html` — Examens (4 îlots, gold standard nommé, tableau de configurations, 4 quiz, Pareto) et Sciences (Neuroanatomie, Physiologie, Biologie cellulaire, Pharmacogénétique ; 4 figures SVG `role="img"` légendées ; quatre liens Science → clinique / examen / traitement / À retenir chacune ; 395 à 425 mots par discipline).
- `chapters/R05/R05_d.html` — Pharmacologie (classes, doses suisses, interactions en `div.alert`, surveillance et médicaments à éviter, Pareto) ; ferme le template.
- `chapters/R05/R05_pop1.html` — 40 fenêtres cliniques et diagnostiques (dont 4 fenêtres de contentieux : traitement d’épreuve, FeNO, sécrétolytiques/antitussifs, apnée du sommeil).
- `chapters/R05/R05_pop2.html` — 10 monographies et contentieux (dextrométhorphane, codéine, morphine, gabapentine, prégabaline, géfapixant, corticoïdes inhalés/antileucotriène, inhibiteurs de la pompe à protons, contentieux dose de morphine, contentieux effet du géfapixant) et 6 Pareto.
- `glossary/r05.py` — 7 clés nouvelles : P2X3, TRPV1, TRPA1, LCQ, COUGH-1, COUGH-2, McGarvey. Aucune n’existe dans `glossary/*.py` ni dans les glossaires des dossiers `livraisons/` (vérifié au début et à la fin de la rédaction). Les autres sigles utilisés (IEC, BPCO, FeNO, VEMS, CVF, TDM, ATP, CYP2D6, ERS, HUG, NICE, OFSP, SpO₂, PCR, ECG, BNP, NT-proBNP, NMDA, GABA, SARS-CoV-2, COVID-19, IgE…) existent déjà. Les sigles RGO, IPP, ORL, SAOS, DGP, AWMF, NAEB, HARQ ont été évités en écrivant les termes en toutes lettres.

## Plan

Pathologie : 0 question clinique (femme de 58 ans, toux sèche de 5 mois, allotussie, incontinence, IEC) ; 1 définitions et classification par durée (tableau) ; 2 épidémiologie et retentissement ; 3 physiopathologie (réflexe normal → sensibilisation périphérique et centrale, IEC, reflux, éosinophiles, tabac ; figure 1) ; 4 causes par durée (tableau causes fréquentes / graves) et traits traitables ; 5 anamnèse (cartes typique/trompeuse) ; 6 examen clinique (deux colonnes) ; 7 démarche diagnostique (bilan de base, bilan personnalisé en tableau, quiz) ; 8 signes d’alarme (alert) et complications ; 9 toux aiguë et subaiguë ; 10 traits traitables (tableau traitement × délai) ; 11 toux réfractaire/inexpliquée (thérapie de contrôle de la toux, neuromodulateurs, géfapixant) ; 12 suivi, pronostic, prévention ; 13 enfant, grossesse, sujet âgé, insuffisance rénale/hépatique, cas récapitulatif ; 14 critères formels et paramètres clés.

Le code CIM n’apparaît que dans l’en-tête. Asthme, BPCO, bronchite, bronchiolite, bronchiectasies (J47), pneumonies (J18) et pneumopathies interstitielles (J84) sont renvoyés à leurs cours.

## Sources consultées (09.10.2026)

| Source | Mode d’accès réel |
|---|---|
| Morice et al., ERS guidelines on the diagnosis and treatment of chronic cough in adults and children, Eur Respir J 2020;55:1901136 (PMID 31515408, PMC6942543) | Texte intégral (efetch PMC), y compris tableau 1 des recommandations |
| Société allemande de pneumologie (DGP), recommandation S2k « Fachärztliche Diagnostik und Therapie von erwachsenen Patienten mit Husten », AWMF 020-003, version 4.1, janvier 2025 | Texte intégral PDF (pdftotext), chapitres 1 à 12, tableaux et figures |
| HUG, Service de médecine de premier recours, stratégie « Toux chronique », 2025 (van Ruymbeke, Talbit et al.) | Texte intégral PDF (récupéré via WebFetch, pdftotext) |
| Van Ruymbeke et al., Rev Med Suisse 2025;21:1695 (PMID 40994066) | Résumé seulement (article réservé) ; contenu détaillé tiré de la stratégie HUG correspondante |
| NICE NG120, Cough (acute): antimicrobial prescribing, février 2019 | Texte intégral PDF |
| OFSP, « Coqueluche : la vaccination protège les nourrissons d’une évolution grave » | Texte intégral HTML |
| Singh et al., Peripheral and central mechanisms of cough hypersensitivity, J Thorac Dis 2020 (PMID 33145095, PMC7578480) | Texte intégral (efetch PMC) |
| Morice et al., Opiate therapy in chronic cough, AJRCCM 2007 (PMID 17122382) | Résumé PubMed |
| Ryan et al., Gabapentin for refractory chronic cough, Lancet 2012 (PMID 22951084) | Résumé PubMed |
| McGarvey et al., COUGH-1 et COUGH-2, Lancet 2022 (PMID 35248186) | Résumé PubMed (chiffres concordants avec l’information professionnelle Lyfnua) |
| Morice et al., cough hypersensitivity syndrome, Eur Respir J 2014 (PMID 25142479) | Résumé PubMed |
| Song et al., Eur Respir J 2015 (PMID 25657027) | Lettre sans résumé ; le chiffre de 10 % est repris de l’ERS 2020 qui la cite |
| Mallet et al., Swiss Med Wkly 2023 (PMID 36912371) | Résumé PubMed |
| Informations professionnelles suisses via `tools/swissmedic_fi.py` (AmiKo) : Lyfnua® (11.2024), Codein Knoll® (08.2026), Bexine® sirop (03.2026), Neurontin® (04.2025), Prégabaline Sandoz® (04.2024), MST Continus® (05.2024), Bisolvon® Pentoxyvérine (07.2023), Triofan® Antitussif Noscapine (03.2025), Resyl plus® gouttes, Bexine Antitussif Butamirate, Nexium® MUPS (06.2026), Montélukast Sandoz® (10.2023), Acétylcystéine 600 Sun Store | Texte intégral ; sections Indications, Posologie, Contre-indications, Mises en garde, Interactions, Grossesse, Effets indésirables, Mécanisme lues pour les molécules citées |

Tous les liens externes du cours (13 URL distinctes) ont été testés : HTTP 200 (PubMed renvoie 203 via le proxy, contenu servi). Les 6 PMID cités ont été vérifiés par `esummary` (premier auteur, année, revue concordants). Aucune recommandation américaine ne fonde une conduite : la BTS 2023 et les références américaines citées par les HUG n’ont pas été lues et ne sont pas citées ; le NICE (Royaume-Uni) est retenu comme source européenne pour la toux aiguë ; les essais (Morice, Ryan, McGarvey) sont cités comme données.

## Arbitrages

1. **Traitement d’épreuve** (fenêtre `r05-epreuve`) : ERS 2020 (essais séquentiels, corticoïde inhalé 2–4 semaines) ; DGP 01.2025 (essai de 4 semaines si suspicion) ; HUG 09.2025 (« plus recommandé » sans argument anamnestique). Source applicable la plus récente retenue (HUG) : pas d’essai sans indice clinique ; essai limité et évalué si un trait est suspecté (point commun aux trois).
2. **FeNO** (fenêtre `r05-feno`) : ERS 2020 (utilité prédictive non démontrée) contre HUG 2025 (utile, preuve modérée) ; HUG retenu, sans seuil consensuel.
3. **Sécrétolytiques et antitussifs dans la toux aiguë** (fenêtre `r05-miel`) : NICE 2019 (pas de mucolytique ; codéine inefficace) contre DGP 2025 (sécrétolytiques, dextrométhorphane, phytothérapie à la demande) ; DGP retenue comme option de confort ; avertissement HUG sur l’effet placebo.
4. **Dose de morphine** (fenêtre `r05-contentieux-morphine`) : essai et ERS 5–10 mg deux fois par jour ; DGP 10 mg deux fois par jour ; HUG « 5 à 10 mg par jour ». La formulation HUG, non appuyée par un essai, n’est pas retenue. Taux de réponse : ERS ~50 % contre DGP ~20 %, présenté comme incertitude.
5. **Effet du géfapixant** (fenêtre `r05-contentieux-gefapixant`) : HUG « −75 % contre placebo à 2 semaines » contre essais de phase 3 et information professionnelle (−18,5 % et −14,6 % contre placebo). Source primaire retenue.
6. **Apnée du sommeil** : HUG (CPAP efficace ≥ 6 semaines) contre DGP (preuves insuffisantes) ; HUG retenu avec mention de la faiblesse des effectifs.
7. **Fréquence de la toux sous IEC** : ERS et HUG ~15 % ; DGP ~10 % des femmes et 5 % des hommes ; les deux chiffres sont donnés.

## Réserves honnêtes

1. **Aucune validation médicale humaine.** Version de travail revue par IA.
2. **Hors indication en Suisse** : morphine (indication douleurs), gabapentine, prégabaline dans la toux ; ésoméprazole 40 mg deux fois par jour (au-delà de la posologie autorisée pour le reflux) ; corticoïdes inhalés et montélukast hors asthme. Tous signalés dans le cours.
3. **Géfapixant** : autorisé en Suisse (information professionnelle 11.2024) ; **disponibilité et remboursement non vérifiés** (lacune nommée dans la monographie).
4. **Morphine** : la plus petite force de sulfate de morphine retard lue (MST Continus®) est 10 mg ; la dose de 5 mg de l’essai n’a pas de forme suisse identifiée (Kapanol® et Sevre-Long® non lus).
5. **Éosinophilie sanguine** : l’ERS écrit « 0.3 cells/µL » ; interprété comme 0,3 G/L (300/µL), note de lecture explicite dans la fenêtre `r05-eos`.
6. **Épidémiologie suisse** : aucune prévalence suisse de la toux chronique de l’adulte trouvée (lacune nommée) ; seule une donnée pédiatrique zurichoise (Mallet 2023) est citée.
7. **Fréquence des métaboliseurs ultrarapides du CYP2D6 et de la syncope de toux** : non chiffrées par les sources lues (lacunes nommées).
8. **Antibiotiques de la toux aiguë** : schémas du NICE (britanniques) présentés comme tels ; l’antibiothérapie suisse est renvoyée aux cours J40 et J18. La recommandation SSI « Infection respiratoire aiguë » n’a pas pu être lue (API JSON exigeant un corps de requête) ; elle n’est pas citée.
9. **Résumés seulement** pour les essais morphine, gabapentine, COUGH-1/2 et le consensus ERS 2014 ; les chiffres repris figurent dans ces résumés ou dans l’ERS 2020 / l’information professionnelle.
10. **mediX** : aucune guideline mediX spécifique de la toux trouvée (recherche web) ; la source suisse principale est la stratégie HUG 2025. Swiss Medical Forum : aucun article récent sur la toux trouvé ; non cité.
11. **Volume** : environ 17 800 mots texte compris fenêtres et références (cible indicative 11 000–15 000) ; le relecteur peut condenser les fenêtres de contentieux et les lignes de références répétées.
12. **Clés génériques** : TRPV1, TRPA1, P2X3, LCQ sont neutres et réutilisables ; la clé `McGarvey` suit le modèle `McMyn`/`MacParland` (nom propre).
13. `tests/audit_sciences.py` exigera d’ajouter R05 à la liste des nouvelles productions sans base Git (décision du relecteur).

## Contrôles effectués (copie scratchpad : dépôt sans `.git`, `dist`, `livraisons`, `preview` + `chapters/R05` + `glossary/r05.py` + entrée R05 temporaire dans une copie de `chapters.json`)

- `python3 build_medina.py R05` : **`R05 non couvertes: 0`** ; 10 ratios Pareto calculés (8 à 24 % du texte).
- Clés : 56 `data-k`, 56 `template data-pop`, aucune manquante, aucune orpheline, aucun doublon ; toutes préfixées `r05-` ou `pareto-r05-` ; aucun identifiant dupliqué ; tous les `data-cover` existent.
- Contrat Sciences (logique de `tests/audit_sciences.py`) : 4 disciplines de 395 à 425 mots, une figure légendée et accessible chacune, les quatre liens présents, navigation complète.
- Playwright (Chromium 1194 de `/opt/pw-browsers`, `executable_path`) : 76 mots verts cliqués dans les quatre onglets et les quatre disciplines (mode livre), **aucune « Fiche absente »**, 6 Pareto ouverts ; seule erreur JavaScript : `preview/lesson-core.js` absent de la coque (erreur d’environnement, identique à J12 et J84) ; mobile 390 px : `scrollWidth = 390` dans les quatre onglets. `test_preview.py` non exécutable tel quel (version de Chromium attendue par Playwright absente). Rendu ordinateur et mobile vérifié visuellement (captures de travail dans le scratchpad, non livrées).
- Volume : environ 17 800 mots ; 50 fenêtres de contenu + 6 Pareto ; 5 quiz ; 5 figures SVG.
- Non fait (rôle du relecteur) : captures `tools/capture_lecon.py`, build `--all-fragments`, tests unitaires, entrée `chapters.json` (`covers` : R05), injection et scellement.
