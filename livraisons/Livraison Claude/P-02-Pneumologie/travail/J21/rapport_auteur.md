# Rapport d’auteur — J21 — Bronchiolite aiguë et infection aiguë des voies respiratoires inférieures (P-02-Pneumologie)

Rédacteur de la chaîne interne Claude, 09.10.2026. **Version de travail : ni relue, ni injectée, ni validée par un médecin.** Une revue par IA et des tests techniques ne constituent pas une validation médicale.

## Couverture

- J21 — Bronchiolite aiguë : J21.0 (VRS), J21.1 (métapneumovirus humain), J21.8 (autres micro-organismes précisés), J21.9 (sans précision)
- J22 — Infection aiguë des voies respiratoires inférieures, sans précision

Libellés contrôlés sur le catalogue BfArM CIM-10-GM 2024, bloc J20–J22 (https://klassifikationen.bfarm.de/icd-10-gm/kode-suche/htmlgm2024/block-j20-j22.htm, consulté le 09.10.2026). Les codes n’apparaissent que dans l’en-tête discret et le glossaire. Renvois sans second cours : J18 — Pneumonies de l’adulte, J40 — Bronchite (bronchite aiguë J20), J45 — Asthme.

Titre dans `organisation/FILE_FRAGMENTS_CLAUDE.json` : « Bronchiolite aiguë et infections respiratoires basses non précisées ». Le titre affiché suit la consigne de l’orchestrateur (« … infection aiguë des voies respiratoires inférieures ») ; à harmoniser par le relecteur au moment de l’injection (aucun fichier partagé modifié).

## Fichiers (tous dans `travail/J21/`)

| Fichier | Contenu | Mots (texte, hors SVG) |
|---|---|---|
| `chapters/J21/J21_a.html` | En-tête, onglets, îlots 0 à 6, figure 1, Pareto clinique | 2 527 |
| `chapters/J21/J21_b.html` | Îlots 7 à 13 (1 quiz, Pareto diagnostic, traitements, critères) ; dernier îlot `div.alert` puis `div.key` | 3 030 |
| `chapters/J21/J21_c.html` | Onglet Examens (4 îlots, 3 quiz, Pareto) ; onglet Sciences (anatomie, histologie, physiologie, microbiologie-immunologie ; figures 2 à 5) | 2 853 |
| `chapters/J21/J21_d.html` | Onglet Pharmacologie (4 îlots, Pareto) ; fermeture du template | 1 364 |
| `chapters/J21/J21_pop1.html` | 30 fenêtres (pathologie, clinique, examens) | 4 513 |
| `chapters/J21/J21_pop2.html` | 30 fenêtres (traitements, adulte, prévention, monographies) + 6 Pareto | 5 616 |
| `glossary/j21.py` | 16 clés nouvelles : J21.0, J21.1, J21.8, J21.9, SSPP, SAPP, CFV, NS2, NaCl, mRESVIA, MELODY, HARMONIE, MATISSE, CLEVER, ProHOSP, NG9 | — |

Total : environ 9 800 mots de corps de cours et 10 100 mots de fenêtres ; 66 fenêtres (60 + 6 Pareto), 4 quiz, 5 figures SVG noir et blanc légendées. Toutes les clés de fenêtres sont préfixées `j21-` ; aucune fenêtre existante n’est réutilisée.

## Plan

**Pathologie** : 0 Question clinique (nourrisson de 7 semaines) ; 1 Définitions et degrés de gravité (Europe/États-Unis, SSPP 2020, ERS/ESCMID chez l’adulte) ; 2 Épidémiologie et pronostic (OFSP 2026, registre suisse) ; 3 De l’épithélium cilié à l’hypoxémie (NS2, 120 µm, ventilation collatérale, atélectasie, shunt ; figure) ; 4 Virus et terrains à risque ; 5 Interroger les parents ; 6 Examiner le nourrisson ; 7 Diagnostic (aucun examen systématique ; différentiel hiérarchisé ; quiz) ; 8 Signes de gravité et complications (`alert`) ; 9 Prise en charge du nourrisson (critères d’hospitalisation, oxygène, haut débit, sonde, médicaments à ne pas prescrire, sortie) ; 10 Infection respiratoire basse de l’adulte (signes de pneumonie, CRP, diagnostics imitateurs, antibiotiques) ; 11 Suivi et prévention (algorithme suisse 2026, vaccination de l’adulte) ; 12 Situations particulières et cas récapitulatif ; 13 Critères formels (`div.alert`) puis paramètres clés (`div.key`).
**Examens** : question → examen → statut, examen de référence nommé (amplification génique pour le VRS ; diagnostic clinique) ; fiches d’interprétation (oxymétrie, gazométrie, biologie, radiographie, adulte) ; configurations diagnostiques ; 3 quiz.
**Sciences** : anatomie (calibre bronchiolaire, ventilation collatérale), histologie (cible ciliée, NS2, neutrophiles), physiologie (piégeage, atélectasie, pression positive, cible de saturation), microbiologie-immunologie (protéine F préfusionnelle, sites Ø et IV, région Fc, anticorps maternels) ; chaque discipline : figure + corrélations science → clinique / examen / traitement.
**Pharmacologie** : classes et place ; doses selon les informations professionnelles suisses ; précautions (`alert`) ; médicaments à éviter ; 7 monographies en fenêtres.

## Sources consultées (09.10.2026) et mode d’accès réel

| Source | Accès | Usage |
|---|---|---|
| OFSP et CFV, Recommandations pour la vaccination et l’immunisation contre le VRS, mise à jour 2026 (Bulletin, publié 28.09.2026) — bag.admin.ch PDF | Texte intégral (PDF, pdftotext) | Épidémiologie suisse (tableau 4, chap. 4.3), clinique adulte, diagnostic (PCR référence), produits, efficacité (MELODY, HARMONIE, CLEVER, MATISSE, RENOIR, AReSVi-006, mRESVIA, données en vie réelle), recommandations nourrisson, 2e saison, adulte (tableau 3), palivizumab |
| OFSP et CFV, Plan de vaccination suisse 2026 (février 2026, corrigé avril 2026) | Texte intégral (PDF) | Algorithme par mois de naissance, exceptions, 2e saison (chap. 3.1.i), co-administration |
| OFSP, page « Virus respiratoire syncytial humain (VRS) » | Page HTML lue | Transmission, otite, mesures d’hygiène |
| Barben, Regamey, Hammer. Bronchiolite aiguë – une mise à jour. Forum Médical Suisse 2020;20(9-10):155-159, doi:10.4414/fms.2020.08460 (Crossref vérifié) | Texte intégral (PDF CLOCKSS) | Définitions, gravité (tab. 2), hospitalisation (tab. 3), traitement ambulatoire/hospitalier (tab. 4-5), oxygène < 90 %, haut débit, sonde, restriction hydrique, sortie (tab. 6), différentiel |
| SAPP. Behandlung der akuten Bronchiolitis im Säuglingsalter. Paediatrica 2003;14(6):18-22 | Texte intégral (PDF) | Performances leucocytes/CRP, SIADH, sonde nasale (historique), décongestionnants, décision de ventiler |
| Pédiatrie Suisse, listes Top 5 « smarter medicine » 2021 (FR) et 2024 (DE) | Pages HTML lues | Antitussifs (3), corticoïdes/bronchodilatateurs (4), radiographie (2024, 5) |
| NICE NG9, Bronchiolitis in children (01.06.2015, mise à jour 09.08.2021) | Page « Recommendations » lue en entier | Critères diagnostiques, orientation, hospitalisation, seuils 90/92 %, traitements proscrits, CPAP, aspiration, gazométrie, liquides, sortie |
| Haute Autorité de santé, premier épisode de bronchiolite aiguë < 12 mois, texte des recommandations, novembre 2019 | Texte intégral (PDF) | Grille de gravité, vulnérabilité, environnement (grades), réanimation, examens, SSH, kinésithérapie, oxygène, haut débit/CPAP, médicaments, nutrition, suivi, fiche parents |
| Woodhead et al. Guidelines for the management of adult LRTI — full version. Clin Microbiol Infect 2011;17 Suppl 6:E1-59 (ERS/ESCMID), PMC7128977 | Texte intégral (Europe PMC XML) | Définitions, suspicion de pneumonie, CRP 20/100, diagnostics imitateurs, facteurs de complication, traitements symptomatiques, antibiotiques, surveillance, orientation |
| Pickles & DeVincenzo, J Pathol 2015 (PMID 25302625) | Texte intégral (Europe PMC) | Histopathologie, NS2, 120/250 µm, ventilation collatérale, piégeage, atélectasie, shunt |
| Øymar et al., Scand J Trauma Resusc Emerg Med 2014 (PMID 24694087) | Texte intégral (Europe PMC) | Répartition virale, apnées, crépitants/sibilants, CPAP |
| Jartti et al. (EAACI), Allergy 2019 (PMID 30276826) | Texte intégral (Europe PMC) | Profils VRS/rhinovirus, asthme ultérieur |
| Stucki et al., Euro Surveill 2024 (PMID 39328156) ; Hayes Vidal-Quadras et al., Swiss Med Wkly 2024 (PMID 39137355) | Résumés PubMed | Registre suisse ; saisonnalité post-COVID |
| Hammitt 2022 (MELODY), Drysdale 2023 (HARMONIE), Zar 2025 (CLEVER), Kampmann 2023 (MATISSE), Papi 2023, Walsh 2023, Franklin 2018, Cunningham 2015, Gajdos 2010, Rochat 2012, Little 2013, Schuetz 2009 (ProHOSP) | Résumés PubMed (efetch) | Chiffres d’essais |
| Revues Cochrane : Gadomski 2014, Hartling 2011, Fernandes 2013, Zhang 2023, Roqué-Figuls 2023, Smith 2017 | Résumés PubMed | Bronchodilatateurs, adrénaline, corticoïdes, SSH, kinésithérapie, antibiotiques |
| Informations professionnelles suisses (AIPS via AmiKo, `tools/swissmedic_fi.py`) : Beyfortus® (07.2026), Enflonsia® (11.2025), Abrysvo® (07.2026), Arexvy (06.2026), mRESVIA (08.2026), Dafalgan® enfant sirop (09.2025), Rinosedin® 0,05 % gouttes nasales (02.2025), Otrivin Rhume (02.2025) | Texte intégral | Doses, contre-indications, précautions, demi-vies, signal Guillain-Barré, prématurité, décongestionnants |

Tous les liens des fichiers ont été contrôlés le 09.10.2026 : 23 PMID par esummary (premier auteur, année, revue concordants), DOI 10.4414/fms.2020.08460 par Crossref, 10 URL officielles en HTTP 200. Aucune recommandation américaine n’est utilisée comme fondement de conduite ; les essais publiés (dont des essais à participation américaine) sont cités comme données.

## Arbitrages entre sources (fenêtres sur mots verts)

1. **Seuil d’oxygène** (`j21-oxygene-seuil`) : NICE 2021 retenu (90 % dès 6 semaines, 92 % avant 6 semaines ou comorbidité), concordant avec SSPP 2020 ; HAS 2019 (92 %) présentée comme texte antérieur.
2. **Critères de sortie** (`j21-sortie`) : NICE 2021 + SSPP 2020 ; HAS 2019 en comparaison.
3. **Sérum salé hypertonique** (`j21-ssh`) : revue Cochrane 2023 (effet modeste, certitude faible) contre recommandations NICE/HAS/SSPP ; recommandation suisse la plus récente retenue (non).
4. **Désobstruction nasale** (`j21-desobstruction`) : SSPP 2020 (lavage + aspiration superficielle) retenue, HAS 2019 et NICE 2015 exposées.
5. **Sonde gastrique** (`j21-nutrition`) : SAPP 2003 (sonde nasale déconseillée) supplantée par SSPP 2020, NICE et HAS.
6. **Xylométazoline** (`j21-xylometazoline`) : SSPP 2020 la mentionne ; l’information professionnelle suisse (Rinosedin® 0,05 %) l’interdit avant 1 an → l’IP prime.
7. **Rappel mRESVIA** : l’IP l’autorise après 12 mois ; l’OFSP ne le recommande pas (évaluation en cours) — signalé dans la monographie.

## Contrôles effectués (copie de travail dans le répertoire temporaire, aucun fichier du dépôt modifié)

- `build_medina.py J21` (avec entrée J21 ajoutée à une copie temporaire de `chapters.json`) : **J21 non couvertes : 0**, aucune erreur Pareto, aucun avertissement de glossaire.
- Clés : 66 `data-k` = 66 `data-pop`, aucune manquante ni orpheline ; 16 clés de glossaire nouvelles, **aucune collision** avec `glossary/*.py`.
- `test_preview.py J21` : échec unique « Failed to fetch dynamically imported module lesson-core.js », **identique sur J84 injecté** → défaut de l’environnement de prévisualisation, non du cours. Contrôle Playwright équivalent via serveur HTTP local : cours affiché, 4 onglets et 4 disciplines des sciences ouverts, toutes les fenêtres visibles ouvertes sans « Fiche absente », 6 Pareto avec fraction calculée, 4 quiz, aucune erreur JavaScript propre au cours, largeur mobile 390 px sans défilement horizontal.
- Deux captures de vérification (ouverture, fenêtre NICE) produites dans le répertoire temporaire ; les deux captures officielles par `tools/capture_lecon.py` restent à faire par le relecteur sur le frontend du fragment.

## Réserves honnêtes

1. **Recommandation suisse de prise en charge** : le dernier texte national formel date de 2003 ; la mise à jour SSPP 2020 est un article de revue évalué par les pairs, non une recommandation gradée. La conduite s’appuie donc aussi sur NICE (britannique) et HAS (française).
2. **ERS/ESCMID 2011** : seule recommandation européenne lue pour l’infection respiratoire basse de l’adulte ; ancienne. La recommandation S3 germanophone 2021 sur la pneumonie (co-signée SGP et SSI) n’a été lue qu’en résumé et n’est pas citée.
3. **Essais et revues Cochrane** : lus en résumé seulement (pas de texte intégral).
4. **Tableau 3 de la SSPP 2020** : la ligne « Enfants < 6–8 ans » est manifestement une coquille (probablement semaines) ; non reprise.
5. **Chiffres de vaccins de l’adulte** (efficacité de mRESVIA 83,7 %, revaccination Arexvy) : repris du bulletin OFSP 2026, publications originales non lues.
6. **Indices cliniques des diagnostics différentiels** (tableau de l’îlot 7, colonne « Indice ») : partiellement reformulés par l’auteur à partir des listes SSPP/HAS/NICE ; à contrôler par le relecteur.
7. **Énoncés de corrélation science → clinique** : chacun rattaché à Pickles 2015, Øymar 2014, OFSP 2026 ou aux recommandations ; quelques liaisons logiques (par exemple « l’oxygène relève la saturation sans lever l’obstruction ») sont des déductions directes non citées mot pour mot.
8. **Volume** : environ 19 900 mots au total, supérieur à J84 (12 047) ; le cours couvre deux populations (nourrisson et adulte) et la prévention 2026. Le relecteur peut resserrer les fenêtres redondantes (gravité/fréquence respiratoire/tirage).
9. Titre du cours à harmoniser avec `FILE_FRAGMENTS_CLAUDE.json` (voir Couverture).
