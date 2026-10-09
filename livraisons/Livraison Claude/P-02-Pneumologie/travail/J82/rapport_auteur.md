# Rapport d’auteur — J82 — Éosinophilies pulmonaires (P-02-Pneumologie)

Rédacteur de la chaîne interne Claude, 09.10.2026. Cours unique couvrant J82 : pneumopathie chronique à éosinophiles (PCE), pneumopathie aiguë à éosinophiles (PAE), syndrome de Löffler ; aspergillose bronchopulmonaire allergique, granulomatose éosinophilique avec polyangéite (GEPA), syndrome hyperéosinophilique (SHE) et formes médicamenteuses en différentiel. **Version de travail : ni relue par l’agent différé, ni injectée, ni validée par un médecin.** Revue IA et contrôles techniques seulement.

## Fichiers

- `chapters/J82/J82_a.html` — en-tête, onglets, onglet Pathologie îlots 0 à 6 (figure 1, Pareto clinique).
- `chapters/J82/J82_b.html` — îlots 7 à 12 (quiz, Pareto diagnostic, Pareto urgences-traitement-suivi, Pareto critères) ; dernier îlot : critères formels `div.alert` puis paramètres clés `div.key`.
- `chapters/J82/J82_c.html` — Examens (4 îlots, 4 quiz, Pareto) et Sciences (Biologie cellulaire, Immunologie, Anatomie pathologique, Parasitologie ; 4 figures SVG `role="img"` légendées ; liens Science → clinique / examen / traitement / À retenir).
- `chapters/J82/J82_d.html` — Pharmacologie (4 îlots, Pareto) ; ferme le template.
- `chapters/J82/J82_pop1.html` — 33 fenêtres cliniques, diagnostiques, deux fenêtres de contentieux (durée de corticothérapie de la PCE ; dose de mépolizumab dans la GEPA) et essais MIRRA/MANDARA.
- `chapters/J82/J82_pop2.html` — 8 monographies (glucocorticoïdes, albendazole/mébendazole, ivermectine, itraconazole, mépolizumab, benralizumab, omalizumab, imatinib) et 6 Pareto.
- `glossary/j82.py` — 5 clés nouvelles : PCE, PAE, GEPA, SHE, HTLV-1. Aucune n’existe dans `glossary/*.py` ni dans les glossaires des dossiers `livraisons/Livraison Claude/*/travail/*/glossary/` (vérifié au début et à la fin de la rédaction). Les sigles déjà définis ailleurs mais non injectés (ISHAM dans j12) ont été évités : le cours écrit « groupe de travail international, Eur Respir J 2024 ».

## Plan

Pathologie : 0 question clinique (PCE d’une asthmatique de 46 ans) ; 1 définitions (seuils Valent 2023, Cottin 2005) et classification en trois groupes (cause identifiable, maladie systémique, forme idiopathique) ; 2 épidémiologie et pronostic (séries européennes ; lacune suisse nommée) ; 3 physiopathologie (réponse de type 2, IL-5, granules, fibrose ; figure 1) ; 4 causes et facteurs de risque ; 5 anamnèse (cartes forme typique / trompeuses) ; 6 examen extrathoracique ; 7 diagnostic en quatre temps et différentiels hiérarchisés par gravité ; 8 urgences (PAE, GEPA, SHE, hyperinfection à *Strongyloides*) ; 9 traitement par forme ; 10 suivi ; 11 situations particulières et cas récapitulatif ; 12 critères formels (PCE, PAE, aspergillose ISHAM 2024, GEPA ACR/EULAR 2022, SHE) et paramètres clés.

Périmètre vérifié dans la CIM-10-GM 2024 (BfArM, bloc J80–J84, lu le 09.10.2026) : J82 inclut l’infiltrat éosinophile avec asthme, le syndrome de Löffler et l’éosinophilie tropicale ; il exclut les formes médicamenteuses (J70.2–J70.4), l’aspergillose (B44), les parasitoses précisées et les connectivites/vascularites (M30–M36). Ces entités sont donc traitées en différentiel ; la GEPA renvoie au cours M31 déjà injecté (cohérence vérifiée : ANCA 30–40 %, mépolizumab 300 mg et benralizumab 30 mg toutes les 4 semaines, induction par cyclophosphamide ou rituximab des formes sévères). Le code CIM n’apparaît que dans l’en-tête.

## Sources consultées (09.10.2026)

| Source | Mode d’accès réel |
|---|---|
| Marchand et Cordier, Idiopathic chronic eosinophilic pneumonia, Orphanet J Rare Dis 2006 (PMID 16722612, PMC1464381) | Texte intégral PMC |
| Agarwal et al., recommandations révisées ISHAM-ABPA, Eur Respir J 2024 (PMID 38423624, PMC10991853) | Texte intégral PMC (critères, classification, traitement, tableau 6 des doses, grossesse) |
| Emmi et al., Evidence-Based Guideline EGPA, Nat Rev Rheumatol 2023 (PMID 37161084) | Texte intégral HTML nature.com (accès ouvert), énoncés 1 à 16 |
| Valent et al., critères des maladies à éosinophiles, Allergy 2023 (PMID 36207764, PMC9797433) | Texte intégral PMC |
| Previtero et al., PCE fibrosante, Eur Respir Rev 2026 (PMID 42419778, PMC13343205) | Texte intégral PMC |
| Jackson, Akuthota, Roufosse, Eur Respir Rev 2022 (PMID 35082127, PMC9489126) | Texte intégral PMC |
| Wechsler et al., MIRRA, N Engl J Med 2017 (PMID 28514601, PMC5548295) | Texte intégral PMC |
| Carnino et al., dépistage de *Strongyloides*, HUG et Swiss TPH, Trop Med Infect Dis 2021 (PMID 34941659, PMC8704417) | Texte intégral PMC |
| Marchand et al., 62 PCE, Medicine 1998 (PMID 9772920) ; Marchand et al., PCE et asthme, Eur Respir J 2003 (PMID 12882444) | Résumés PubMed |
| Philit et al., PAE idiopathique, 22 patients, 2002 (PMID 12403693) | Résumé PubMed (texte intégral inaccessible : 403) |
| De Giacomi et al., PAE, Chest 2017 (PMID 28286263) | Résumé PubMed (série citée comme données) |
| Cottin et Cordier, Allergy 2005 (PMID 15932372) ; Cottin 2023 (PMID 37055090) ; Cottin 2025 (PMID 41110928) ; Cottin et al., PCE après radiothérapie, 2004 (PMID 14738224) ; Cottin et al., GEPA respiratoire, Eur Respir J 2016 (PMID 27587545) ; Cordier et al., bronchiolite hyperéosinophilique, 2013 (PMID 23258778) | Résumés PubMed |
| Wechsler et al., MANDARA, 2024 (PMID 38393328) ; Grayson et al., ACR/EULAR 2022 (PMID 35106968) | Résumés PubMed (critères ACR/EULAR détaillés aussi dans Emmi 2023) |
| Jeong et al., Radiographics 2007 (PMID 17495282) | Résumé PubMed |
| Hoenigl et al., ascaridiose pulmonaire en Autriche, 2010 (PMID 20924692) ; Faridah et al., revue du syndrome de Löffler, 2026 (PMID 41161022) | Résumés PubMed |
| Cordaillat et al., éosinophilie chez le migrant, Rev Med Suisse 2025 (PMID 40313018) | Résumé français (texte intégral payant) |
| Conen et al., montélukast et Churg-Strauss, Swiss Med Wkly 2004 (PMID 15340881) ; Rigamonti et al., Swiss Med Wkly 2012 (PMID 22430939) | Résumés PubMed |
| Hellmich et al., EULAR 2022 (PMID 36927642) | Résumé PubMed (non cité dans le cours ; cohérence avec M31 vérifiée) |
| Informations professionnelles suisses via `tools/swissmedic_fi.py` (AmiKo) : Nucala (12.2025), Fasenra (03.2026), Sporanox (11.2024), Zentel (10.2025), Vermox 100 mg (07.2025), Prednisone Streuli (06.2026), Spiricort (06.2026), Solu-Medrol (08.2025), Glivec (07.2026), Cubicin (11.2022), Dupixent (01.2025), Xolair (03.2025), Cinqaero (03.2023, lue, non citée : asthme seul) | Texte intégral ; indications, posologie, contre-indications, mises en garde, grossesse, mécanisme |
| CIM-10-GM 2024, bloc J80–J84 (BfArM) | Texte intégral HTML (périmètre seulement) |

Liens du cours : 27 URL externes ; PMC, nature.com et swissmedicinfo.ch répondent HTTP 200 ; pubmed.ncbi.nlm.nih.gov répond 203 à travers le proxy (page servie). Les 18 PMID cités ont été vérifiés par `esummary` (premier auteur, année, revue concordants). Aucune recommandation américaine ne fonde une conduite ; les séries Mayo (De Giacomi 2017, cohorte fibrosante rapportée par Previtero) et les essais NEJM sont cités comme données. ACR/EULAR 2022 est recevable au titre de l’EULAR.

## Arbitrages

1. **Durée de la corticothérapie de la PCE** (fenêtre `j82-contentieux-duree`) : 6 à 12 mois (Marchand et Cordier 2006, texte le plus récent) et sevrage tenté dès 6 mois sans asthme sévère (Marchand 1998) ; positions compatibles, aucune recommandation suisse ou européenne plus récente.
2. **Mépolizumab dans la GEPA** (fenêtre `j82-contentieux-mepo`) : information professionnelle suisse 12.2025 (300 mg) retenue comme source primaire applicable la plus récente ; 100 mg (Emmi 2023) présenté comme choix hors posologie autorisée.
3. **Aspergillose** : prednisolone ou itraconazole en première intention selon ISHAM 2024 ; l’usage de l’itraconazole est signalé comme hors indication stricte (l’information Sporanox® réserve l’aspergillose à l’échec ou l’intolérance du traitement standard).
4. **GEPA** : traitée en résumé et renvoyée au cours M31, pour éviter un doublon et préserver la cohérence.

## Réserves honnêtes

1. **Aucune validation médicale humaine.** Version de travail revue par IA.
2. **Données suisses d’épidémiologie absentes** pour PCE, PAE et Löffler (lacune nommée dans l’îlot 2).
3. **PAE : dose et durée des glucocorticoïdes non fixées** par les sources lues (texte intégral de Philit inaccessible) ; lacune nommée dans l’îlot 9.
4. **Ivermectine : aucune information professionnelle suisse trouvée** sur AmiKo le 09.10.2026 ; dose tirée de Carnino 2021 ; lacune nommée dans la monographie.
5. **Usages hors indication suisse** signalés : anti-IL-5 dans la PCE (séries de cas, aucun essai randomisé), omalizumab dans l’aspergillose, itraconazole dans l’aspergillose bronchopulmonaire allergique (indication restreinte), prednisone orale dans la PCE (indication non nommée ; Solu-Medrol® cite la pneumopathie à éosinophiles rebelle).
6. **Résumés seulement** pour plusieurs séries (Philit, Marchand 1998 et 2003, De Giacomi, Cottin 2004/2016/2023/2025, MANDARA, Cordaillat) ; les chiffres repris figurent dans ces résumés.
7. **ISHAM 2024** est un consensus international (Delphi, coordination indienne) publié dans l’Eur Respir J ; il est retenu faute de texte suisse ou européen plus récent sur l’aspergillose bronchopulmonaire allergique. L’argumentaire français OrphaLung 2021 (PNDS ABPA, HAS) a été repéré mais non exploité au-delà de sa page de présentation.
8. **Syndrome de Löffler** : la chronologie de la migration larvaire n’est pas détaillée faute de source européenne en texte intégral ; le cours s’en tient aux résumés lus (Hoenigl, Faridah, Cottin).
9. **Mobile** : aucun débordement de page (scrollWidth = 390 dans les quatre onglets) ; les tableaux à trois ou quatre colonnes défilent dans leur cadre, comme dans J84 injecté.
10. `tests/audit_sciences.py` exigera d’ajouter J82 à la liste des nouvelles productions sans base Git (décision du relecteur).

## Contrôles effectués (copie scratchpad : fichiers du dépôt + `chapters/J82` + `glossary/j82.py` + entrée J82 temporaire dans une copie de `chapters.json`, `MEDINA_ROOT` pointé sur la copie)

- `python3 build_medina.py J82` : **`J82 non couvertes: 0`** (glossaire du dépôt + j82.py seulement, sans les glossaires des autres dossiers de travail) ; six Pareto calculés : clinique 5 %, diagnostic 11 %, urgences-traitement-suivi 7 %, critères 18 %, examens 5 %, pharmacologie 4 %.
- Clés : 41 `data-k` de fenêtres + 6 Pareto, toutes avec leur `template data-pop` ; toutes préfixées `j82-` ou `pareto-j82-` ; clés de fenêtres du glossaire j82 existantes ; aucun identifiant dupliqué ; aucune fenêtre orpheline.
- Contrat Sciences (logique de `tests/audit_sciences.py` appliquée au fichier) : navigation complète ; 4 disciplines de 344 à 412 mots, une figure légendée et accessible chacune, les quatre liens présents.
- Playwright (Chromium 1194 de `/opt/pw-browsers`, contexte `bypass_csp`) : 47 mots verts et boutons Pareto ouverts dans les quatre onglets et les quatre disciplines, **aucune « Fiche absente »**, **aucune erreur JavaScript propre au cours** (seule erreur : `preview/lesson-core.js` absent de la coque en `file://`, environnementale, identique à J12/J84) ; mobile 390 px sans défilement horizontal de page ; figures contrôlées visuellement sur captures de travail (scratchpad, non livrées), débordements de texte SVG corrigés.
- Volume : environ 15 000 mots tout compris (pathologie 4 700, examens et sciences 3 100, pharmacologie 1 400, fenêtres 6 200) ; 47 fenêtres (33 cliniques, 8 monographies, 6 Pareto) ; 5 quiz ; 5 figures SVG.
- Non fait (rôle du relecteur) : captures `tools/capture_lecon.py`, build `--all-fragments`, tests unitaires, entrée `chapters.json` (`covers` : J82), injection et scellement.
