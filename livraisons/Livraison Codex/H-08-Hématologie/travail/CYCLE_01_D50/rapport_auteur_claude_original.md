# Rapport d’auteur — D50 — Anémie par carence en fer (H-08-Hématologie)

Rédacteur de la chaîne interne Claude, 09.10.2026. Cours unique couvrant D50, avec la carence martiale sans anémie traitée en articulation (îlot 11). **Version de travail : ni relue par l’agent différé, ni injectée, ni validée par un médecin.** Revue IA et contrôles techniques seulement.

## Fichiers

- `chapters/D50/D50_a.html` — en-tête, onglets, onglet Pathologie îlots 0 à 6 (Pareto clinique).
- `chapters/D50/D50_b.html` — îlots 7 à 14 (2 quiz, Pareto diagnostic, Pareto traitement, Pareto suivi et critères) ; dernier îlot : critères formels `div.alert` puis paramètres clés `div.key`, références principales.
- `chapters/D50/D50_c.html` — Examens (5 îlots, 3 quiz, Pareto) et Sciences (Physiologie, Biochimie, Hématologie cellulaire, Génétique ; 4 figures SVG `role="img"` légendées ; liens Science → clinique / examen / traitement / À retenir).
- `chapters/D50/D50_d.html` — Pharmacologie (5 îlots, Pareto) ; ferme le template.
- `chapters/D50/D50_pop1.html` — 48 fenêtres cliniques, diagnostiques, thérapeutiques et de situations particulières, dont 4 comportant un contentieux (seuil de ferritine, vitamine C, hypersensibilité selon la molécule, hypophosphatémie).
- `chapters/D50/D50_pop2.html` — 6 monographies, fenêtre d’interactions, contentieux des formes à libération modifiée, 6 Pareto.
- `glossary/d50.py` — 9 clés : VGM, TCMH, TSAT, MICI, BSG, ESGE, DMT1, FGF23, TMPRSS6.

## Plan

Pathologie : 0 question clinique (femme ménopausée, Hb 96 g/L, VGM 72 fl, ferritine 6 µg/L ; d’où vient la perte ?) ; 1 définitions OMS 2024 (seuils, gravité, altitude), carence martiale (consensus suisse), stades, carence absolue et fonctionnelle ; 2 épidémiologie (données suisses : recrues, employées hospitalières, grossesse, prescription de fer) et pronostic ; 3 physiopathologie (bilan du fer, hepcidine, ferroportine, stades biologiques, conséquences tissulaires) ; 4 causes (tableau mécanisme → causes → conduite) ; 5 anamnèse ; 6 examen ; 7 diagnostic et recherche de la cause (ferritine, CRP, TSAT, différentiels, algorithme d’exploration) ; 8 gravité et complications ; 9 objectifs et fer oral ; 10 fer intraveineux et transfusion ; 11 carence martiale sans anémie ; 12 suivi, récidive, prévention ; 13 situations particulières (grossesse, post-partum, MICI, insuffisance cardiaque et rénale, sujet âgé, cancer, chirurgie, enfant, cas récapitulatif) ; 14 critères formels et paramètres clés.

Choix de périmètre : l’anémie inflammatoire (D63), les recommandations de cardiologie (I50) et les hémoglobinopathies sont traitées comme différentiels ou renvois. Le code CIM n’apparaît que dans l’en-tête.

## Sources consultées (09.10.2026)

| Source | Mode d’accès réel |
|---|---|
| Nowak et al., étude Delphi suisse sur la carence martiale, Swiss Med Wkly 2019 (doi 10.4414/smw.2019.20097, PMID 31269223) | Texte intégral PDF (smw.ch), toutes les sections spécialisées |
| Clénin, carence martiale sans anémie, Swiss Med Wkly 2017 (PMID 28634965) | Texte intégral PDF, 17 pages, tableaux 1 à 3 |
| Biétry et al., Swiss Med Wkly 2017 (PMID 28695564) ; Meier et al., 2019 (PMID 31568551) ; Simic et al., 2023 (PMID 37229775) ; Karczewski et al., 2024 (PMID 38579297) ; Pereira Portela et al., 2024 (PMID 39137372) | Textes intégraux PDF (résumés et introductions lus ; chiffres repris des résumés) |
| Gstrein et al., Swiss Med Wkly 2017 (PMID 28695549) ; Hug et al., 2013 (PMID 24018778) | Résumés PubMed |
| gynécologie suisse (SGGG), avis d’experts n° 77, diagnostic et traitement de l’anémie ferriprive pendant la grossesse et le post-partum, 24.08.2022 | Texte intégral PDF (allemand) |
| OMS, seuils d’hémoglobine pour définir l’anémie, 2024 (handle 10665/376196) | Texte intégral PDF via l’API IRIS (tableaux 2 à 4, altitude, tabac) |
| OMS, ferritine et statut martial, 2020 (handle 10665/331505) | Texte intégral PDF via l’API IRIS (recommandations 1.1 à 1.4, tableau 1) |
| Snook et al., recommandations BSG 2021, Gut (PMID 34497146, PMC8515119) | Texte intégral PMC, recommandations 1 à 35 et sections |
| Pennazio et al., ESGE 2022 (PMID 36423618) | Résumé (recommandations principales 1 à 7) |
| Société européenne d’étude de la maladie cœliaque, recommandations 2025, partie 1 (PMID 40999951, PMC12704582) | Texte intégral PMC (sérologie, indications de dépistage) |
| Hoving et al., anémie ferriprive réfractaire au fer, Br J Haematol 2025 (PMID 39985323, PMC11985374) | Texte intégral PMC |
| Moretti et al., Blood 2015 (PMID 26289639) ; Stoffel et al., Lancet Haematol 2017 (PMID 29032957) | Résumés PubMed (résumé de Stoffel tronqué après l’étude 1 ; seuls les résultats de l’étude 1 sont repris) |
| Vaucher et al., CMAJ 2012 (PMC3414597) ; Favrat et al., Prefer, PLoS One 2014 (PMC3994001) | Résumés PubMed |
| Wolf et al., JAMA 2020 (PMC7042864) ; Schaefer et al., Br J Clin Pharmacol 2021 (PMC8247006) | Résumé (Wolf) ; texte intégral PMC (Schaefer, mécanisme FGF23) |
| Muñoz et al., consensus périopératoire, Anaesthesia 2017 (PMID 27996086) | Résumé seulement (cité pour son existence et sa participation zurichoise) |
| Informations professionnelles suisses via `tools/swissmedic_fi.py` (AmiKo) : Ferinject® (06.2025), Monofer® (06.2026), Venofer® (05.2025), Maltofer® (08.2021), ferro sanol® (04.2021), Tardyferon® (07.2025), Ferrum Hausmann® (05.2021), Feraccru® (08.2021) | Texte intégral ; indications, posologie, contre-indications, mises en garde, interactions, grossesse, effets indésirables, efficacité clinique |

Tous les liens du cours (30 URL externes) ont été testés : HTTP 200, sauf quatre pages PubMed qui répondent 203 au robot ; leurs PMID ont été vérifiés par `esummary` (premier auteur, année, revue concordants). Les deux identifiants IRIS de l’OMS ont été vérifiés par l’API (titre concordant). Aucune recommandation américaine ne fonde une conduite ; l’essai de Wolf (centres américains) et l’essai de Vaucher (cabinets français) sont cités comme données.

## Arbitrages

1. **Seuil de ferritine** (fenêtre `d50-seuil`) : OMS 2020 (15 µg/L), Delphi 2019 (30, ou 30–50 avec TSAT < 20 %), BSG 2021 (15/30 ; 45 pour l’exploration), gynécologie suisse 2022 (30). La source suisse la plus récente (2022) retient 30 µg/L, valeur appliquée.
2. **Vitamine C** (fenêtre `d50-vitc`) : Clénin 2017 contre BSG 2021 et gynécologie suisse 2022 ; les sources les plus récentes l’emportent (complément inutile).
3. **Formes à libération modifiée** (fenêtre `d50-mr`) : BSG 2021 ne les recommande pas ; les trois sels ferreux suisses sont autorisés sous cette forme. Présenté comme contentieux, usage suisse conservé avec contrôle de la réponse.
4. **Hypophosphatémie** : gynécologie suisse 2022 la juge sans portée clinique pendant la grossesse ; l’information professionnelle Ferinject® de 2025, plus récente, impose la surveillance des patients à risque. La seconde est retenue.
5. **TSAT et inflammation** : Clénin et la BSG décrivent une TSAT abaissée ; le consensus Delphi signale qu’elle peut être relevée par la baisse de la transferrine. Les deux mécanismes sont exposés dans `d50-tsat`.

## Réserves honnêtes

1. **Aucune validation médicale humaine.** Version de travail revue par IA.
2. **Swiss Iron Health Organisation** : le domaine siho.ch est désormais un domaine parqué (vérifié le 09.10.2026) ; aucune publication de cet organisme n’a pu être lue. Le consensus Delphi suisse de 2019 sert de référence suisse principale.
3. **mediX** : la page des guidelines exige une connexion ; aucun texte mediX sur la carence martiale n’a été lu.
4. **SSH/SGH (Société suisse d’hématologie)** : aucune recommandation publiée sur la carence martiale trouvée.
5. **ECCO 2015 (Dignass, PMID 25518052) et ECCO 2024** : textes intégraux inaccessibles (403 chez l’éditeur, aucun résumé PubMed pour 2015). Les seuils et conduites des MICI viennent de la section gastroentérologique du consensus Delphi suisse et de la BSG ; ECCO n’est pas cité comme source dans le cours.
6. **ESC (insuffisance cardiaque)** : mise à jour 2023 et recommandations ESC 2026 (PMID 42661420, 28.08.2026) inaccessibles en texte intégral (403) et sans résumé. La fenêtre `d50-ic` repose sur le Delphi suisse et Gstrein 2017 et renvoie les classes de recommandation au cours I50 ; aucun nom d’essai cardiologique n’est cité.
7. **Maastricht VI** : texte inaccessible ; non cité. La place d’Helicobacter pylori repose sur la BSG (méta-analyse : association faible, pas d’effet de l’éradication sur la réponse au fer).
8. **Résumés seulement** pour plusieurs essais (tableau) ; les chiffres repris figurent dans ces résumés. L’essai de Krayenbuehl (2011) est cité d’après la revue de Clénin, non lu directement.
9. **Hors indication** : érythropoïétine dans l’anémie du post-partum (signalée hors indication par gynécologie suisse) ; seuils spécialisés du Delphi (oncologie, néphrologie) présentés comme consensus d’experts, dont certains de niveau « consensus critique » (50–79 %).
10. **Glossaire** : la clé `ESGE` existe déjà dans le dossier de travail parallèle `G-04/.../K21/glossary/k21.py` ; ma définition reprend son développement littéral à l’identique (seule la phrase d’exemple diffère). Le relecteur injectant en second doit en garder une seule. Les clés `VGM`, `TCMH`, `TSAT`, `MICI` sont génériques et serviront à d’autres cours d’hématologie ou de gastroentérologie ; vérification de non-duplication faite le 09.10.2026 sur `glossary/*.py` et tous les dossiers `livraisons/Livraison Claude/*/travail/*/glossary/`.
11. **Volume** : environ 17 900 mots tout compris (corps des onglets environ 9 600, fenêtres environ 8 200, avec références et légendes), au-dessus de la cible indicative ; le relecteur peut condenser `d50-qui-explorer` et `d50-second`, qui recoupent partiellement l’îlot 7 et l’îlot E-2.
12. **Mobile** : aucune largeur de page supérieure à 390 px ; les tableaux larges défilent dans leur conteneur (comportement du moteur).
13. `tests/audit_sciences.py` exigera d’ajouter D50 à la liste des nouvelles productions sans base Git (décision du relecteur).
14. Entrée `chapters.json` à créer par le relecteur : `{"code":"D50","covers":["D50"],"title":"Anémie par carence en fer", ...}` ; vague et système à aligner sur `shell/data.py` (non vérifié par l’auteur).

## Contrôles effectués (copie scratchpad : dépôt + `chapters/D50` + `glossary/d50.py` + entrée D50 temporaire dans une copie de `chapters.json`)

- `python3 build_medina.py D50` : **`D50 non couvertes: 0`** ; six Pareto calculés (6 à 10 % du texte).
- Clés : 62 `data-k`, 62 `template data-pop`, aucune manquante, aucune orpheline, aucune fenêtre dupliquée ; toutes préfixées `d50-` ou `pareto-d50-` ; aucun identifiant dupliqué ; classes dans la liste fermée.
- Contrat Sciences (logique de `tests/audit_sciences.py`) : 4 disciplines de 321 à 399 mots, une figure légendée et accessible chacune, les quatre liens présents, navigation complète.
- Playwright (Chromium 1194 de `/opt/pw-browsers`, `executable_path` explicite) : mode livre, quatre onglets et quatre disciplines ; les 56 fenêtres cliniques et les 6 Pareto ouverts, **aucune « Fiche absente »** ; seules erreurs JavaScript : `preview/lesson-core.js` introuvable en `file://` (environnement, identique à J12 et J84) ; mobile 390 px : `scrollWidth` = 390 dans les quatre onglets. Rendu ordinateur et mobile, figures et une fenêtre vérifiés visuellement (captures de travail dans le scratchpad, non livrées) ; la figure 1 a été redessinée après contrôle visuel (chevauchement d’un trait et d’un texte).
- Volume : environ 17 900 mots, 62 fenêtres (dont 6 Pareto), 5 quiz, 4 figures SVG.
- Non fait (rôle du relecteur) : captures `tools/capture_lecon.py`, build `--all-fragments`, tests unitaires, entrée `chapters.json`, injection et scellement.
