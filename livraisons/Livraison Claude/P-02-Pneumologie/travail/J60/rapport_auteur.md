# Rapport d’auteur — J60 — Pneumoconioses (P-02-Pneumologie)

Rédacteur de la chaîne interne Claude, 09.10.2026. Cours unique couvrant J60, J61, J62, J63, J64, J65 et J92 (plaques pleurales). **Version de travail : ni relue par l’agent différé, ni injectée, ni validée par un médecin.** Revue IA et contrôles techniques seulement.

## Fichiers

- `chapters/J60/J60_a.html` — en-tête (code CIM seulement dans l’en-tête), onglets, onglet Pathologie îlots 0 à 6 (Pareto clinique).
- `chapters/J60/J60_b.html` — îlots 7 à 13 (Pareto diagnostic, Pareto complications et traitements, Pareto prévention-reconnaissance-critères) ; dernier îlot : critères formels `div.alert` puis paramètres clés `div.key`.
- `chapters/J60/J60_c.html` — Examens (4 îlots dont 4 quiz, Pareto) et Sciences (Anatomie, Anatomopathologie, Physiologie, Immunologie et toxicologie ; 4 figures SVG `role="img"` légendées ; liens Science → clinique / examen / traitement / À retenir).
- `chapters/J60/J60_d.html` — Pharmacologie (4 îlots, Pareto) ; ferme le template.
- `chapters/J60/J60_pop1.html` — 32 fenêtres cliniques, diagnostiques et techniques.
- `chapters/J60/J60_pop2.html` — 15 fenêtres (monographies, contentieux, droit des assurances, prévention) et 6 Pareto.
- `glossary/j60.py` — 11 clés nouvelles : BIT, ICOERD, IGRA, AWMF, EFA, NLST, HLA-DPB1, et 4 noms d’auteurs composés (Marchand-Adam, Mora-Cuesta, Müller-Quernheim, Vu-Duc ; précédent : `Funke-Chambour` dans j84). Aucune n’existe dans `glossary/*.py` ni dans les glossaires des autres dossiers `livraisons/Livraison Claude/*/travail/*/glossary/` (revérifié en fin de rédaction, 09.10.2026).

## Plan

Pathologie : 0 question clinique (chauffagiste de 67 ans, plaques calcifiées et réticulations basales) ; 1 définition (Suva, AWMF) et classification par agent (silice, poussières mixtes, amiante, béryllium, métaux durs, fer, talc, aluminium) ; 2 épidémiologie suisse et mondiale, pronostic ; 3 physiopathologie (fraction alvéolaire, fibres OMS, cycle macrophagique de la silice, biopersistance de l’amiante, immunité) ; 4 expositions et facteurs de risque (métiers, fibres-années, dose cumulée de quartz, HLA-DPB1 Glu69) ; 5 anamnèse et latences ; 6 examen ; 7 diagnostic (BIT, TDM ICOERD, fonction, corps asbestosiques, test au béryllium, différentiel) ; 8 complications et urgences (silicoprotéinose, silicotuberculose, cancers, auto-immunité, atteintes pleurales) ; 9 traitement ; 10 déclaration et reconnaissance (LAA art. 9, OLAA annexe 1, fraction étiologique, critères d’Helsinki, Fondation EFA) ; 11 suivi, dépistage et prévention (hiérarchie STOP, valeurs limites, programme Suva 2019, dépistage TDM, tuberculose) ; 12 situations particulières (pierre artificielle, bérylliose déguisée en sarcoïdose, métaux durs, soudeurs, exposition indirecte, femme exposée, cas récapitulatif) ; 13 critères formels et paramètres clés.

Choix de périmètre : le mésothéliome (C45), le cancer bronchique (C34), la tuberculose (A15), la sarcoïdose (D86), la fibrose idiopathique (J84) et les maladies des poussières organiques (J66–J67, cours J67 en rédaction parallèle) sont renvoyés à leurs cours ; seules les notions nécessaires au diagnostic différentiel et à la déclaration sont données. Le périmètre CIM a été lu dans la CIM-10-GM 2024 (BfArM, blocs J60–J70 et J90–J94) et ne figure que dans l’en-tête.

## Sources consultées (09.10.2026)

| Source | Mode d’accès réel |
|---|---|
| Suva, fiche thématique Silicose (Stöhr, Miedinger, Jost), décembre 2012 | PDF intégral (pdftotext), version française |
| Suva, fiche thématique Maladies professionnelles causées par l’amiante, octobre 2019 | PDF intégral, version française (23 pages) |
| Suva, fiche thématique Bérylliose (Kunz, Jost), septembre 2012 | PDF intégral, version française |
| Suva Medical 2020, « Nouveautés relatives au suivi après exposition à l’amiante et au programme de dépistage par scanner » (trois articles) | Texte intégral HTML |
| Suva, « L’amiante rend malade » (maladies et prestations d’assurance) | Texte intégral HTML |
| Suva, « La silicose – la pire des maladies » (jalons historiques) | Texte intégral HTML |
| Suva, Explications concernant les VME et VBT, édition du 02.04.2026 | PDF intégral ; section amiante (0,01 fibre/ml) |
| Preisser et al., recommandation AWMF S2k Silicose, Respiration 2026 (PMID 42412737, PMC13577655) | Texte intégral PMC (efetch) |
| Wolff et al., critères d’Helsinki 2014, Scand J Work Environ Health 2015 (PMID 25299403) | PDF intégral (sjweh.fi) |
| Ferreiro et al., Asbestos and benign pleural diseases, Breathe (ERS) 2025 (PMC12070196) | Texte intégral PMC |
| Hoy et al., Current global perspectives on silicosis, Respirology 2022 (PMC9310854) | Texte intégral PMC |
| Getahun et al., recommandations OMS sur l’infection tuberculeuse latente, Eur Respir J 2015 (PMID 26405286, PMC4664608) | Résumé PubMed |
| Ligue pulmonaire suisse et OFSP, Tuberculose en Suisse, version 1.2024 | PDF intégral (chapitres 3, 4 et 7) |
| OFSP et CFV, Plan de vaccination suisse 2026 | PDF intégral (grippe, pneumocoque, COVID-19) |
| Kraus et Teschler, mise à jour AWMF amiante 2020, Pneumologie 2021 (PMID 33728629) | Résumé PubMed (texte allemand non lu) |
| Vu-Duc et Guillemin 1999 (10510836) ; Müller-Quernheim et al. 2006 (16540500) ; Marchand-Adam et al. 2008 (18757698) ; Hoy et al. 2018 (28882991) ; Howlett et al. 2024 (39107111) ; Mora-Cuesta et al. 2026 (41672090) ; Wells et al. 2020 (32145830) ; Nemery 1990 (2178966) ; Cosgrove 2015 (26152561) ; Takahashi et al. 2018 (30292280) ; Marchiori et al. 2010 (20155272) ; Fortarezza et al. 2025 (39438781) ; Moriyama et al. 2025 (40815182) | Résumés PubMed (efetch) ; chiffres repris de ces résumés |
| Feary et al., Artificial stone silicosis: a UK case series, Thorax 2024 (39107113) | Titre et notice seulement (pas de résumé disponible) ; cité uniquement pour l’existence d’une série britannique |
| Informations professionnelles suisses via `tools/swissmedic_fi.py` (AmiKo) : Ofev® (03.2025), Rimactan® (10.2023), Prednisone Streuli® (06.2026) | Texte intégral ; indications, posologie, contre-indications, mises en garde, interactions, grossesse, mécanisme, efficacité clinique (INBUILD) |
| CIM-10-GM 2024, blocs J60–J70 et J90–J94 (BfArM) | Texte intégral HTML (périmètre seulement, non cité dans le cours) |

Les 30 URL externes du cours ont été testées : HTTP 200, sauf PubMed (203, réponse servie par le proxy, page accessible). Les 15 PMID cités en lien ont été vérifiés par `esummary` (premier auteur, année, revue concordants). Aucune recommandation américaine ne fonde une conduite ; l’essai NLST et les séries publiées sont cités comme données. Les recommandations OMS publiées dans l’Eur Respir J sont présentées dans le contentieux tuberculose, où le guide suisse 2024 l’emporte.

## Arbitrages

1. **Contentieux tuberculose** (`j60-contentieux-tb`) : OMS 2015 (dépistage et traitement systématiques de l’infection latente chez le silicotique) contre guide suisse 2024 (dépistage systématique réservé aux situations listées, silicose désignée comme risque modéré et candidate prioritaire au traitement) et Suva 2012 (contrôles bactériologiques réguliers). Source applicable la plus récente retenue : guide suisse 2024, décision individuelle.
2. **Contentieux vaccination pneumococcique** (`j60-contentieux-vaccins`) : Suva 2012 (rappel tous les cinq ans, logique du vaccin polysaccharidique) contre Plan de vaccination 2026 (dose unique de vaccin conjugué). Plan 2026 retenu.
3. **Durée du traitement de la silicotuberculose** : prolongation à 8–12 mois attribuée explicitement à la recommandation allemande de 2022 citée par l’AWMF ; le guide suisse ne contient pas de schéma propre (lacune nommée dans la fenêtre).
4. **Nintédanib** : indication suisse « PID fibrosantes chroniques à phénotype progressif » ; l’extrapolation aux pneumoconioses est signalée (pneumoconioses non individualisées dans INBUILD selon les publications lues).
5. **Mésothéliome** : renvoi à C45 ; seules les notions d’attribution, de latence et de déclaration sont données.

## Réserves honnêtes

1. **Aucune validation médicale humaine.** Le cours est une version de travail revue par IA.
2. **Valeur limite du quartz** : 0,15 mg/m³ provient de la fiche Suva de 2012 ; la base de données VME actuelle de la Suva (application web) n’a pas pu être interrogée, et le document « Explications » 2026 ne donne pas la valeur du quartz. La fenêtre `j60-vme` le dit. La valeur européenne (0,1 mg/m³, directive 2017) est reprise de Hoy 2022, EUR-Lex étant inaccessible depuis l’environnement.
3. **Fiches Suva anciennes** : silicose et bérylliose datent de 2012, amiante de 2019 ; ce sont les versions publiées en ligne au 09.10.2026.
4. **Hors indication suisse** : corticoïdes dans la bérylliose (la prednisone n’a que la sarcoïdose symptomatique) ; rifampicine en monothérapie préventive (l’information professionnelle impose l’association pour traiter une tuberculose ; le schéma suit le guide national). Posologie des corticoïdes de la bérylliose non trouvée dans les sources lues (lacune nommée).
5. **Isoniazide** : la fiche AmiKo « Isoniazid Labatec » ne contient pas de texte ; doses et interactions tirées du guide suisse de la tuberculose (lacune nommée dans `j60-d-isoniazide`).
6. **Aluminose, graphitose, stannose et pneumoconiose des mineurs de charbon** : peu documentées par les sources européennes lues ; l’aluminose est déclarée lacune dans `j60-autres-poussieres` ; la pneumoconiose des mineurs est traitée comme forme de pneumoconiose à poussières mixtes selon l’AWMF (nodules noirs, emphysème, « black hole lung » non repris). Graphite et étain ne sont pas décrits faute de source lue.
7. **Résumés seulement** pour plusieurs études (tableau ci-dessus) ; la recommandation AWMF amiante 2020 n’a été lue qu’à travers le résumé de Kraus et Teschler.
8. **Intervalle de confiance du risque de tuberculose** : Hoy 2022 (2,88–5,58) et l’AWMF (2,88–5,88) divergent ; seul le risque relatif de 4,01 est donné dans le cours.
9. **Examen clinique** : aucune source lue ne décrit précisément les signes auscultatoires de l’asbestose ; l’îlot 6 s’en tient au mécanisme (élasticité, restriction, diffusion) et aux signes de complication.
10. **Volume** : environ 16 000 mots tout compris (texte, 47 fenêtres, références), un peu au-dessus de la cible indicative ; le relecteur peut condenser l’îlot 10 ou certaines fenêtres sans perte d’information.
11. **Glossaire** : LAA, OLAA et STOP existent dans des glossaires de travail parallèles (J67, J69) mais pas dans `glossary/` ; le cours les écrit en toutes lettres pour ne dépendre d’aucune injection préalable.
12. **Mobile** : aucun défilement horizontal de page à 390 px (scrollWidth = 390 sur les quatre onglets).
13. `tests/audit_sciences.py` exigera d’ajouter J60 à la liste des nouvelles productions sans base Git (décision du relecteur).

## Contrôles effectués (copie scratchpad : dépôt + `chapters/J60` + `glossary/j60.py` + entrée J60 temporaire dans une copie de `chapters.json`, `covers` : J60, J61, J62, J63, J64, J65, J92)

- `python3 build_medina.py J60` : **`J60 non couvertes: 0`** ; six Pareto calculés (clinique 6 %, diagnostic 11 %, complications et traitements 11 %, prévention et critères 6 %, examens 9 %, pharmacologie 6 %).
- Clés : 53 `data-k` (47 fenêtres + 6 Pareto), toutes avec leur `template data-pop`, aucune fenêtre orpheline ; identifiants tous préfixés `j60-` (ou `pA`, `pE`, `pS`, `pP`, `ch-J60`), aucun doublon ; ancres du plan toutes résolues.
- Contrat Sciences (logique de `tests/audit_sciences.py`) : navigation complète, 4 disciplines de 392 à 433 mots, une figure légendée et accessible chacune, les quatre liens présents.
- Playwright (Chromium 1194 de `/opt/pw-browsers`, `executable_path` explicite ; `test_preview.py` échoue faute du binaire attendu par Playwright 1.63) : 71 mots verts et boutons Pareto cliqués dans les quatre onglets et les quatre disciplines, aucune « Fiche absente », **aucune erreur JavaScript propre au cours** ; seule erreur : `preview/lesson-core.js` absent en `file://` (environnement, identique à J12 et J84). Mobile 390 px : pas de défilement horizontal de page. Captures de travail dans le scratchpad (non livrées).
- Non fait (rôle du relecteur) : captures `tools/capture_lecon.py`, build `--all-fragments`, tests unitaires, entrée `chapters.json`, injection et scellement.
