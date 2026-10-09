# J47 — Bronchiectasies (P-02-Pneumologie) — rapport de relecture différée

Auto-audit par Agent différé opus 5.5 · 09.10.2026 · cours unique couvrant J47 (CIM-10-GM 2024, code dans l'en-tête seulement).
Sources relues : `travail/J47/chapters/J47/` (6 fichiers). Le brouillon ne contenait **ni glossaire** (`glossary/j47.py` absent) **ni rapport d'auteur**. Le brouillon est conservé intact ; la version relue est injectée dans `chapters/J47/` et `glossary/j47.py`.

**Cette relecture est une revue par IA. Elle ne vaut pas validation médicale humaine.**

## Règles appliquées

`LEADERSHIP_CLAUDE_2026-10-08.md` sections 7 à 13 (règle fondamentale section 11, audit en quatre dimensions et double passe section 13), `CHAPTER_SPEC.md`, `PROMPT_MEDINA.md` § 10, `docs/STYLE_REDACTION.md`, `CONSIGNES_INTERACTION_DENSITE_SOURCES.md`. Modèle : `chapters/J84`.

## Passe 1 — constats sur le brouillon et corrections

### Dimension 2 — exactitude médicale et doses (erreurs corrigées)

| # | Brouillon | Constat (source lue) | Correction |
|---|---|---|---|
| 1 | Haut risque ERS 2025 = ≥ 2 exacerbations, exacerbation sévère, symptômes sévères, *Pseudomonas*, étiologie défavorable | Définition réelle (Breathe 2026, fig. 3) : ≥ 2 exacerbations/an, **1 exacerbation + symptômes sévères**, ou ≥ 1 exacerbation sévère hospitalisée ; *Pseudomonas*, étiologie, purulence = facteurs additionnels | Définition réécrite ; fenêtre `j47-risque` créée |
| 2 | ASPEN : « 1 721 adultes et 41 adolescents » | 1 721 patients **dont** 1 680 adultes et 41 adolescents (résumé NEJM, RCP européen) | Corrigé ; ajout 48,5 % contre 40,3 % sans exacerbation |
| 3 | Vaccin pneumococcique pour toute maladie respiratoire chronique | Plan de vaccination suisse 2026 : PCV seulement pour **bronchectasies dues à un déficit en anticorps** (BPCO ≥ GOLD 3, asthme sévère, ≥ 65 ans) | Corrigé (PCV20/PCV21) |
| 4 | VRS : dès 75 ans et dès 60 ans à risque | Mise à jour OFSP/CFV 2026 : dès 75 ans ; **18–74 ans avec bronchectasie sévère** ; non remboursé à l'automne 2026 | Corrigé |
| 5 | Macrolides : « réduction de 52 %, méta-analyse ERS 2025, qualité de vie cliniquement pertinente » | Non vérifiable (texte ERS inaccessible). Méta-analyse sur données individuelles (Chalmers 2019) : IRR 0,49, SGRQ −2,93 (modeste) | Remplacé par les chiffres lus d'EMBRACE, BAT, BLESS et de la méta-analyse |
| 6 | Antibiotiques inhalés : « −20 % exacerbations, −43 % sévères, résistance doublée » | Non vérifiable | Remplacé par PROMIS-I (0,58 contre 0,95 ; RR 0,61) et l'échec de PROMIS-II |
| 7 | Troubles digestifs azithromycine « jusqu'à un sur cinq » | BAT : 40 % contre 5 % | Corrigé |
| 8 | Azithromycine 250 mg/j ou 250–500 mg 3×/sem attribué à « ERS 2025 » | Doses lues : BTS (250 mg 3×/sem en départ), BAT (250 mg/j), EMBRACE (500 mg 3×/sem) | Attribution corrigée ; hors autorisation suisse confirmée (AIPS Azithromycine Sandoz®, 03.2023) |
| 9 | Ciprofloxacine : interaction tizanidine | AIPS Ciprofloxacin Zentiva® (08.2025) : **contre-indication** tizanidine et agomélatine ; contre-indiquée grossesse/allaitement ; plafond 1000 mg/j (ClCr 30–60), 500 mg/j (< 30) | Corrigé (onglets 1 et 4, fenêtre) |
| 10 | Colistiméthate 1–2 MUI 2×/j (BTS) | AIPS Colistin pour inhalation (07.2021) : 2 × 0,5 à 2 × 2 MUI, moyenne 2 × 1 MUI ; indication mucoviscidose seule ; bronchospasme très fréquent ; contre-indications (myasthénie, prématuré/nouveau-né) | Doses et statut alignés sur l'AIPS |
| 11 | Érythromycine 400 mg 2×/j dans le tableau des doses | Aucune forme orale d'érythromycine retrouvée dans l'AIPS (seulement i.v.) | Retirée du tableau ; conservée comme donnée d'essai (BLESS) |
| 12 | Brensocatib : examen cutané/gingival « imposé » ; induction CYP3A4 | RCP européen : effets cutanés et parodontaux rapportés ; infections fongiques ; prudence si PNN < 1000/mm³ ; vaccins vivants évités ; non recommandé en grossesse ; induction CYP3A4 possible | Reformulé selon le RCP ; autorisation UE 18.11.2025 confirmée (page EMA) ; mention de l'autorisation américaine retirée |
| 13 | ABPA : IgE ≥ 500 seulement | Critères ISHAM 2024 (texte intégral PMC) : sensibilisation (IgE spécifiques ≥ 0,35 kUA/L) + IgE totales ≥ 500 UI/mL indispensables, + 2 parmi IgG spécifiques, éosinophiles ≥ 500/µL, imagerie | Précisé ; traitement prednisolone ou itraconazole |
| 14 | Exacerbation : 7–10 jours non mentionnés | Breathe 2026 : 14 jours, raccourcis à 7–10 jours si germe sensible ou réponse rapide ; BTS : 14 jours toujours si *Pseudomonas* | Ajouté |
| 15 | Transplantation : VEMS < 30 % ou PaCO₂ > 50 mmHg (ERS 2025) | PaCO₂ non retrouvée ; BTS : ≤ 65 ans, VEMS < 30 % avec instabilité ou déclin rapide ; orientation précoce si hémoptysie massive, HTP sévère, soins intensifs, ventilation non invasive | Remplacé par les critères BTS |
| 16 | Réponse vaccinale pneumococcique « 6 semaines (ERS) » | BTS : 4 à 8 semaines après vaccin polysaccharidique | Corrigé ; précision que le PPV23 n'est plus recommandé en prévention en Suisse depuis 2014 |
| 17 | Score FACED : dyspnée mMRC 3–4 ; catégories ; BSI : mortalité 0–5,3 % / 9,9–29,2 % | FACED et BSI : barèmes lus (BTS 2018 tableaux 4 et 5, PMC) ; mortalités par catégorie non retrouvées | Barèmes complets ajoutés ; pourcentages de mortalité retirés ; AUC 0,80/0,88 (résumé BSI) |
| 18 | Éradication « ≈ 40 % » sans source | Conceição 2024 (méta-analyse) : 40 % à 12 mois ; 48 % systémique + inhalé contre 27 % systémique seul | Sourcé et précisé |
| 19 | Rapport broncho-artériel « ≥ 1 », « 1,5 », « deux tiers », effet de l'âge | Seul le critère BTS « > 1, lumière interne » a été lu | Harmonisé sur « > 1 » dans les quatre onglets ; chiffres non sourcés retirés |
| 20 | Chiffres non sourcés | Retirés : 15 battements/s, 200 cils, couche périciliaire 7 µm, 23 générations, mm/min, situs inversus ≈ 50 %, > 50 gènes (remplacé par > 30 gènes, ERS 2017), myéloperoxydase, IL-8/LTB₄, amylose AA, pneumothorax, « quelques centaines de mL », décubitus latéral, hippocratisme, anti-quorum des macrolides, pneumonies sous corticostéroïdes inhalés, sérum hypertonique 6–7 %, mannitol, N-acétylcystéine | — |

### Dimension 1 — rédaction et plan

- **Code CIM enseigné (règle 4)** : îlot 1 « Définition, formes et codage » avec paragraphe Q33.4/A15-A16/E84, ligne « le code devient A15-A16 » et Pareto « codée à part (E84) » : **supprimés** ; le code reste dans l'en-tête.
- Annonces recentrées sur le problème médical ; phrases d'inférence non sourcées (« l'écart reflète surtout… ») remplacées ; expressions imagées atténuées (« s'empile » → « s'organise ») ; « Erreur fréquente » ajoutée (encadré `trap`) dans les étiologies.
- Une fenêtre exposait une procédure interne (« non relu pour ce cours ») : reformulée en limite médicale.

### Dimension 3 — sources

Le brouillon citait l'ERS 2025 par un lien `publications.ersnet.org` (HTTP 403 depuis le proxy) et 54 liens ; 175 liens dans la version finale, tous vérifiés. Le **texte intégral de la recommandation ERS 2025 est inaccessible** (403, absent de PMC, Unpaywall négatif) : son contenu est repris de son **résumé PubMed** et du **résumé clinique en libre accès des mêmes auteurs (Breathe 2026, PMC13077454, texte intégral lu)**. Les données pratiques manquantes viennent du résumé BTS 2018 en libre accès (PMC6326298, texte intégral lu). Lien medicines.org.uk (britannique) remplacé par l'EMA. Aucune recommandation américaine ne fonde une conduite (la recommandation MNT 2020 est cosignée par l'ERS et l'ESCMID).

### Dimension 4 — frontend

Figure 1 (vortex) : boîte « Inflammation neutrophilique » trop étroite, texte au contact du cadre → élargie ; traits pointillés ajoutés pour figurer le vortex. Figure 3 (axonème) redessinée en neuf doublets réels. Figure 5 : croix ambiguë remplacée par un symbole d'inhibition. Glossaire créé (18 clés).

## Passe 2 — relecture intégrale du résultat de la passe 1

Relecture du texte rendu (12 352 mots extraits) et des 42 fenêtres. Corrections supplémentaires :
1. « RAPID » collisionnait avec une clé existante du glossaire (score RAPID d'infection pleurale) : acronyme retiré du texte, algorithme décrit en cinq étapes.
2. « Royaume-Uni » et « Covid-19 » détectés par l'audit des sigles : reformulés (« centres britanniques », « COVID-19 » couvert par le glossaire).
3. Libellés non sourcés : « crépitants (sécrétions…) » → « crépitants (valeur clinique) » ; sibilants rattachés à l'asthme/ABPA (Flume 2018) ; tuberculose : « altération générale, cavernes » retirés ; cible des corticostéroïdes inhalés « éosinophilique » → « bronchique ».
4. Phrase de l'îlot 4 sur les « tests de base » réécrite ; épilogue épidémiologique fondé sur EMBARC.
5. Développements de sigles d'essais non vérifiés (EMBRACE, BLESS) remplacés par « nom propre, non développable lettre à lettre » ; « cathepsine C » retiré de DPP1 (non lu). EMBARC, BAT et FACED développés d'après les textes lus.
6. Légende de la figure 3 corrigée (pas de « plein/creux »).

Aucune réserve bloquante après la passe 2.

## Sources vérifiées (preuve)

PubMed : vérification par eutils `esummary` (premier auteur, revue, année concordants) le 09.10.2026.

| PMID | Référence | Lu |
|---|---|---|
| 41016738 | Chalmers, Eur Respir J 2025;66:2501126 (ERS 2025) | résumé |
| 41988091 | Chalmers, Breathe 2026;22:260001 (résumé clinique ERS 2025) | texte intégral PMC |
| 30687502 | Hill, BMJ Open Respir Res 2018;5:e000348 (BTS) | texte intégral PMC (tableaux 4–7) |
| 34570994 | Aliberti, Lancet Respir Med 2022;10:298-306 | résumé |
| 37105206 | Chalmers, Lancet Respir Med 2023;11:637-649 (EMBARC) | résumé |
| 26293498 / 27730179 | Ringshausen, ERJ 2015 ; protocole EMBARC, ERJ Open Res 2016 (67/100 000) | protocole en texte intégral |
| 30215383 | Flume, Lancet 2018;392:880-890 | texte intégral PMC |
| 24328736 | Chalmers, AJRCCM 2014 (BSI) | résumé |
| 24232697 | Martínez-García, ERJ 2014 (FACED) | résumé |
| 28596426 | Hill, ERJ 2017 (exacerbation) | résumé |
| 40267423 | Chalmers, NEJM 2025 (ASPEN) | résumé |
| 22901887 / 23532241 / 23532242 / 31405828 | EMBRACE, BAT, BLESS, méta-analyse IPD | résumés |
| 39270696 | Haworth, Lancet Respir Med 2024 (PROMIS) | résumé |
| 38296344 | Conceição, Eur Respir Rev 2024 (éradication) | texte intégral PMC |
| 38423624 | Agarwal, ERJ 2024 (ABPA) | texte intégral PMC |
| 27836958 | Lucas, ERJ 2017 (DCP) | texte intégral PMC |
| 32636299 | Daley, ERJ 2020 (MNT) | texte intégral PMC |
| 27911604 | Chalmers, AJRCCM 2017 (élastase) | résumé |
| 16650970 | King, Respir Med 2006 | résumé |
| 19648517 | Murray, ERJ 2009 | résumé |
| 25372159 | Ittrich, Rofo 2015 (embolisation) | résumé |
| 34743315 | Reynolds, Drugs 2021 (*Pseudomonas*) | texte intégral PMC |
| 40901375 | Baker, ERJ Open Res 2025 (virus) | texte intégral PMC |
| 42758741 | De Soyza, PLoS One 2026 (définition de la colonisation) | texte intégral PMC |
| 27864314 | Bustamante-Marin, CSH Perspect Biol 2017 | résumé |
| 9596315 | O'Donnell, Chest 1998 (rhDNase) | résumé |

URL officielles (HTTP 200 le 09.10.2026) : Plan de vaccination suisse 2026 (PDF OFSP, lu) ; Recommandations VRS mise à jour 2026 (PDF OFSP, lu) ; RCP européen Brinsupri (PDF EMA, lu rubriques 4.1–5.1) ; page EPAR Brinsupri (200 lors de la lecture ; 429 de limitation de débit lors du contrôle final) ; AIPS via AmiKo (nom du produit vérifié dans la page) : Azithromycine Sandoz® 7680574820018, Ciprofloxacin Zentiva® 7680566500027, Colistin pour inhalation 7680549150027, Amoxi-Mepha® 7680449110190 (textes intégraux lus par `tools/swissmedic_fi.py`). Brensocatib : aucune information professionnelle dans l'AIPS (`chercher brensocatib`, `chercher brinsupri` : vides).

## Réserves restantes (non bloquantes)

1. **ERS 2025 non lue en texte intégral** (403 éditeur, absente de PMC) : recommandations reprises du résumé et du résumé clinique Breathe 2026 des mêmes auteurs ; niveaux de certitude GRADE non repris.
2. Critères cliniques détaillés du consensus Aliberti 2022 non lus (seul le principe de double exigence est cité).
3. Physiologie : rôle du canal CFTR dans la déshydratation du mucus et action osmotique du sérum hypertonique, notions de manuel non rattachées à une source primaire lue ; aucune valeur chiffrée n'est donnée.
4. Absence de donnée de prévalence suisse : lacune nommée dans le cours.
5. Colonnes du tableau des maladies chroniques du Plan 2026 (grippe, COVID-19, pneumocoque) reconstituées depuis une extraction PDF ; la ligne pneumocoque est confirmée par la liste textuelle du plan.
6. Contrôle navigateur fait sur une prévisualisation `build_medina` de la seule leçon (J47 n'étant pas encore dans `chapters.json`) : 58 ouvertures de fenêtres réussies, 4 onglets et 5 disciplines, aucun débordement à 390 px ; seule erreur JavaScript : chargement de `lesson-core.js` en `file://` (coque, ignorée par `test_v7.py`). À refaire sur le frontend du fragment après enregistrement par l'orchestrateur.
7. Volume : 14 040 mots contre 11 306 (+24 %), dû surtout aux références (175 liens) et aux données vérifiées ajoutées.

## Injection

- `chapters/J47/` : J47_a, _b, _c, _d, _pop1, _pop2 (42 fenêtres dont 5 Pareto, 3 quiz, 6 figures SVG).
- `glossary/j47.py` : 18 clés (BSI, FACED, EMBARC, DPP1, ASPEN, EMBRACE, BAT, BLESS, PROMIS, PROMIS-I, PROMIS-II, mucA, PCV20, PCV21, BMJ, ERJ, Bustamante-Marin, Martínez-García) ; **aucune collision** avec les autres `glossary/*.py`, aucune occurrence de ces clés dans les autres cours.
- `chapters.json`, `organisation/*` et les autres cours **non modifiés** (enregistrement laissé à l'orchestrateur). Aucune opération Git.

## Contrôles

| Contrôle | Résultat |
|---|---|
| `python3 test_v7.py --static J47` | OK (14 040 mots, 42 fenêtres, 3 quiz, 5 Pareto ; classes de la liste fermée ; aucun style en ligne ; clés préfixées) |
| Audit des sigles (`build_medina.build` sur J47) | non couvertes : 0 ; Pareto calculés |
| HTML bien formé (analyseur, 6 fichiers) | aucune balise orpheline |
| Clés : `data-k` sans gabarit / gabarits inutilisés / identifiants dupliqués | 0 / 0 / 0 |
| `python3 -m unittest discover -s tests` | 237 tests, OK |
| Chromium (playwright), prévisualisation J47 | voir réserve 6 ; captures `captures/j47-1-ouverture.png`, `j47-2-explication.png`, `j47-3-mobile-tableau.png` |
