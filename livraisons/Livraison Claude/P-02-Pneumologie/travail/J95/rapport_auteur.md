# Rapport d’auteur — J95 — Complications respiratoires des actes médicaux et autres troubles respiratoires (P-02-Pneumologie)

Rédacteur de la chaîne interne Claude, 09.10.2026. Cours unique couvrant J95, J98 et J99. **Version de travail : ni relue par l’agent différé, ni injectée, ni validée par un médecin.** Revue IA et contrôles techniques seulement.

## Fichiers

- `chapters/J95/J95_a.html` — en-tête, onglets, onglet Pathologie îlots 0 à 6 (tableau des familles, tableau ARISCAT, Pareto clinique).
- `chapters/J95/J95_b.html` — îlots 7 à 13 (tableau des urgences, tableau de prévention, cas récapitulatif) ; Pareto diagnostic, urgences et traitement, suivi et critères ; dernier îlot : critères formels `div.alert` puis paramètres clés `div.key`.
- `chapters/J95/J95_c.html` — Examens (4 îlots dont 4 quiz, Pareto) et Sciences (Physiologie respiratoire, Biophysique alvéolaire, Anatomie, Anatomopathologie ; 4 figures SVG `role="img"` légendées ; liens Science → clinique / examen / traitement / À retenir).
- `chapters/J95/J95_d.html` — Pharmacologie (4 îlots, Pareto) ; ferme le template.
- `chapters/J95/J95_pop1.html` — 35 fenêtres cliniques, diagnostiques et thérapeutiques, dont un contentieux (`j95-contentieux-vni`).
- `chapters/J95/J95_pop2.html` — 7 monographies et 6 Pareto.
- `glossary/j95.py` — 10 clés nouvelles : ESAIC, EPCO, ARISCAT, SFAR, SRLF, EBMT, et 4 noms propres d’auteurs signalés par l’audit (Abu-Omar, Dajer-Fadel, Fuchs-Buder, McGrath), selon la convention de `glossary/j18.py` (Martin-Loeches). Aucune n’existe dans `glossary/*.py` ni dans les glossaires des dossiers `livraisons/` au 09.10.2026 (vérification finale faite).

## Plan

Pathologie : 0 question clinique (hypoxémie au deuxième jour d’une gastrectomie par laparotomie) ; 1 définitions (EPCO) et classification en quatre familles ; 2 épidémiologie et pronostic ; 3 physiopathologie (compression, résorption, obstruction ; shunt ; vasoconstriction hypoxique ; douleur, diaphragme, opioïdes, curarisation résiduelle) ; 4 facteurs de risque (revue suisse, score ARISCAT avec exemple chiffré ; ballonnet et cartilage ; nerf phrénique) ; 5 anamnèse ; 6 examen ; 7 diagnostic (EPCO, radiographie, échographie, TDM ; courbe débit-volume ; diaphragme) ; 8 urgences (insuffisance respiratoire postopératoire, œdème laryngé, canule bouchée ou déplacée, hémorragie, médiastinite) ; 9 prévention et traitement ; 10 extubation, trachéotomie, sténose ; 11 suivi et pronostic ; 12 diaphragme, pneumomédiastin, médiastinite, maladie chronique du greffon contre l’hôte, connectivites, obésité, grossesse, cas récapitulatif ; 13 critères formels et paramètres clés.

Choix de périmètre (CIM-10-GM 2024, BfArM, lue le 09.10.2026, bloc J95–J99) : J95 contient la dysfonction de trachéostomie (hémorragie, obstruction, sepsis, fistule trachéo-œsophagienne), les insuffisances pulmonaires postopératoires (J95.1 à J95.3), le syndrome de Mendelson (J95.4), la sténose sous-glottique (J95.5), le pneumothorax iatrogène (J95.80), la sténose trachéale (J95.81) et les insuffisances d’anastomose (J95.82). J98 contient les maladies bronchiques non classées ailleurs, le collapsus pulmonaire, l’emphysème interstitiel et médiastinal, l’emphysème compensateur, les maladies du médiastin (dont la médiastinite) et du diaphragme. J99 contient les atteintes pulmonaires de la polyarthrite rhumatoïde, des connectivites et de la maladie chronique du greffon contre l’hôte (stades 1 à 3). Renvois : syndrome de Mendelson → J69 ; pneumothorax iatrogène → J93 ; connectivites → M06, M32, J84 ; SDRA → J80 ; insuffisance respiratoire → J96. Le code CIM n’apparaît que dans l’en-tête.

## Sources consultées (09.10.2026)

| Source | Mode d’accès réel |
|---|---|
| CIM-10-GM 2024, bloc J95–J99 (BfArM) | Texte intégral HTML (périmètre ; cité seulement dans la fenêtre Mendelson) |
| Younossian, Adler, Bridevaux, Kherad, Rev Med Suisse 2011 (complications pulmonaires postopératoires) | Texte intégral HTML (revmed.ch) |
| Baskaralingam, Nicod, Manzoni, Rev Med Suisse 2020 (parésies et paralysies diaphragmatiques) | Texte intégral HTML (revmed.ch, via DOI) |
| Kharat, Plojoux, Rev Med Suisse 2021 (échographie diaphragmatique) | Résumé seulement (texte intégral réservé aux abonnés) |
| Kather, Steinack, Franzen, Swiss Med Wkly 2024 (traitement endoscopique des sténoses trachéales bénignes, Zurich) | Texte intégral PDF (smw.ch) |
| Ferreirinha, Caviezel, Weder, Opitz, Inci, Swiss Med Wkly 2020 (résection trachéale, Zurich), PMID 33378546 | Résumé PubMed |
| Jammer et al., définitions EPCO, Eur J Anaesthesiol 2015, PMID 25058504 | Résumé ; définitions détaillées lues dans le tableau 1 de Lee et al. 2025 (PMC11704732, texte intégral) |
| Abbott et al., Br J Anaesth 2018, PMID 29661384 | Résumé |
| Canet et al., Anesthesiology 2010 (ARISCAT), PMID 21045639 | Résumé ; points du score et seuils lus dans le tableau 3 et le texte de Lee et al. 2025 (texte intégral) |
| Zeng et al., atélectasie, partie I, Anesthesiology 2022, PMC9869183 | Texte intégral (manuscrit auteur PMC) |
| Lagier et al., atélectasie, partie II, Anesthesiology 2022, PMC9885487 | Texte intégral (manuscrit auteur PMC) |
| Hedenstierna et al., Anesthesiology 2019, PMID 31045901 | Résumé |
| Kirmeier et al., Lancet Respir Med 2019, PMID 30224322 | Résumé |
| Young et al., consensus international, Br J Anaesth 2019, PMID 31587835 | Résumé |
| Hemmes et al., Lancet 2014, PMC6682759 ; Bluth et al., JAMA 2019, PMC6582260 | Texte intégral PMC (méthodes et résultats) |
| Ferrando et al., Lancet Respir Med 2018, PMID 29371130 ; PRISM trial group, Lancet Respir Med 2021, PMID 34153272 ; Jaber et al., JAMA 2016, PMID 26975890 ; François et al., Lancet 2007, PMID 17398307 | Résumés PubMed |
| Leone et al., Société européenne d’anesthésiologie et ESICM, Eur J Anaesthesiol 2020, PMID 32132408 | Résumé (recommandations 1B citées) |
| Oczkowski et al., ERS, Eur Respir J 2022, PMID 34649974 | Résumé (huit recommandations conditionnelles) |
| Rochwerg et al., ERS/ATS VNI 2017, PMID 28860265 | Résumé seulement ; texte intégral bloqué (HTTP 403) ; **non cité dans le cours** |
| Fuchs-Buder et al., ESAIC 2023, PMID 36377554 | Résumé (recommandations R1 à R8) |
| Quintard et al., SFAR et SRLF, Ann Intensive Care 2019, PMC6342741 | Texte intégral (recommandations R5 à R7) |
| Trouillet et al., SFAR et SRLF, Ann Intensive Care 2018, PMC5854567 | Texte intégral |
| McGrath et al., Anaesthesia 2012, PMID 22731935 | Résumé ; algorithme lu à travers McGrath, Anaesth Rep 2021 (PMC8103083, texte intégral) et Wragg et al., Cureus 2025 (PMC12620918, texte intégral) |
| Monnier et al., Société européenne de laryngologie, 2015, PMID 25951790 ; Fiz et al., Laryngoscope 2020, PMID 31508817 ; Myer et al., 1994, PMID 8154776 | Résumés (grades de Myer et Cotton aussi lus dans Kather 2024) |
| Laveneziana et al., ERS, Eur Respir J 2019, PMID 30956204 | Résumé |
| Macia et al., 2007, PMID 17420139 ; Perna et al., 2010, PMID 19748792 ; Dajer-Fadel et al., 2014, PMID 24887879 | Résumés |
| Abu-Omar et al., EACTS 2017, PMID 28077503 ; De Feo et al., 2011, PMID 21841864 | Résumés (texte EACTS bloqué, HTTP 403) |
| Glanville et al., ERJ Open Res 2022, PMC9309343 | Texte intégral (tableau 1, épidémiologie, traitements) |
| Bos et al., ERS et EBMT, Eur Respir J 2024, PMID 38485149 | Résumé seulement |
| Brunelli et al., ESTS, Eur J Cardiothorac Surg 2020, PMC7825477 | Résumé structuré (PMC) |
| Gosselink et al., ERS et ESICM 2008, PMID 18283429 | Résumé |
| Informations professionnelles suisses via `tools/swissmedic_fi.py` (AmiKo) : Esmeron® (07.2026), Bridion® (02.2026), Robinul®-Néostigmine (04.2020), Naloxon OrPha (07.2026), Solu-Medrol® (08.2025), Kenacort®-A 10/A 40 (12.2021), Kenacort®-A Solubile (12.2021, lue, non citée), Pulmicort® (06.2023) | Texte intégral ; Indications, Posologie, Mises en garde, Interactions, Mécanisme lus |

Tous les liens du cours (49 URL externes) ont été testés : HTTP 200, sauf les 26 pages PubMed qui répondent 203 à travers le proxy de la session (page servie, contenu non lisible par curl) ; ces 26 PMID ont été vérifiés par `esummary` (premier auteur, année, revue, titre concordants). Aucune recommandation américaine ne fonde une conduite ; les essais (dont Bluth, réalisé dans 23 pays) sont cités comme données ; la revue de Lee et al. (Corée, 2025) n’est utilisée que comme reproduction des tableaux EPCO et ARISCAT, sources européennes d’origine.

## Arbitrages

1. **Contentieux VNI, CPAP ou haut débit après chirurgie** (`j95-contentieux-vni`) : Société européenne d’anesthésiologie et ESICM 2020, SFAR et SRLF 2019, ERS 2022. La source applicable la plus récente (ERS 2022) admet le haut débit nasal comme alternative à la VNI chez l’opéré à haut risque ; pour l’opéré déjà hypoxémique après laparotomie, VNI ou CPAP restent le premier choix (aucun texte plus récent contraire ; essai de Jaber).
2. **Obésité** : la revue suisse de 2011 ne la retenait pas comme facteur de risque de complications ; Lagier 2022 documente une atélectasie accrue. Les deux données sont présentées dans `j95-obesite`, sans trancher sur le risque de complication.
3. **Durée opératoire** : la revue suisse retient plus de 3 heures, ARISCAT 2 heures et plus ; le tableau suit ARISCAT (points), le texte cite la revue suisse.
4. **Corticoïde avant extubation** : délai SFAR « au moins six heures » retenu dans les paramètres clés ; schéma de 12 heures de l’essai de François présenté comme donnée, hors posologie autorisée.
5. **Atteintes des connectivites (J99.0, J99.1)** : renvoi aux cours M06, M32 et J84 ; seul le syndrome des poumons rétractés (Baskaralingam) est mentionné.
6. **Noms d’essais** (PROVHILO, PROBESE, POPULAR, iPROVE, PRISM) remplacés par le nom du premier auteur ou une description, pour éviter des clés de glossaire dont le développement n’a pas été vérifié.

## Réserves honnêtes

1. **Aucune validation médicale humaine.** Le cours est une version de travail revue par IA.
2. **Aucune recommandation suisse spécifique** (Société suisse d’anesthésiologie et de médecine périopératoire, Swiss Medical Forum) n’a été trouvée sur les complications pulmonaires postopératoires, la trachéotomie ou les sténoses ; les sources suisses sont deux revues de la Revue médicale suisse et deux séries zurichoises du Swiss Medical Weekly.
3. **Hors indication suisse** : méthylprednisolone en prévention de l’œdème laryngé (l’information Solu-Medrol® cite l’œdème laryngé aigu non infectieux, non la prévention) ; triamcinolone sous-muqueuse trachéale ; budésonide inhalé après plastie trachéale. Mentions explicites dans le cours.
4. **Résumés seulement** pour plusieurs recommandations (Société européenne d’anesthésiologie et ESICM 2020, ERS 2022, ESAIC 2023, EACTS 2017, ERS et EBMT 2024, Société européenne de laryngologie 2015) et essais ; les chiffres repris figurent dans ces résumés. Le texte intégral de l’algorithme britannique des urgences de trachéotomie (2012) n’a pas été accessible : la séquence est tirée de deux textes intégraux secondaires (McGrath 2021, Wragg 2025).
5. **Lacunes nommées dans le cours** : conduite devant une hémorragie massive par érosion du tronc artériel brachiocéphalique ; détail des recommandations EACTS sur la médiastinite ; détail des recommandations ERS et EBMT 2024. Non développés faute de source européenne lue pour l’adulte : maladies bronchiques J98.0 (broncholithiase, collapsus trachéobronchique), calcifications et kystes pulmonaires J98.4, infection respiratoire non précisée J98.7.
6. **Critères de bronchiolite oblitérante après greffe** : critères diagnostiques d’origine NIH (consensus américain), lus dans la revue européenne de Glanville (ERJ Open Research, journal de l’ERS) ; utilisés comme définition diagnostique, non comme recommandation de conduite. Le relecteur peut préférer les signaler comme tels.
7. **ARISCAT** : points lus dans une reproduction secondaire (Lee 2025) ; le texte intégral de Canet 2010 était inaccessible (HTTP 403).
8. **Cas cliniques** : patients fictifs ; l’évolution du cas récapitulatif est illustrative.
9. **Mobile** : les tableaux à trois colonnes défilent horizontalement dans leur cadre à 390 px (comportement du moteur, identique à J84 et J12) ; aucune page ne déborde (scrollWidth = 390).
10. `tests/audit_sciences.py` exigera d’ajouter J95 à la liste des nouvelles productions sans base Git (décision du relecteur).

## Contrôles effectués (copie scratchpad : dépôt + `chapters/J95` + `glossary/j95.py` + entrée J95 temporaire dans une copie de `chapters.json`, `covers` : J95, J98, J99)

- `python3 build_medina.py J95` : **`J95 non couvertes: 0`** ; six Pareto calculés (5 à 18 % du texte).
- Clés : 48 `data-k` distincts, tous avec leur `template data-pop` ; tous préfixés `j95-` ou `pareto-j95-` ; aucun identifiant dupliqué ; aucune fenêtre orpheline.
- Contrat Sciences (logique de `tests/audit_sciences.py`) : 4 disciplines de 416 à 441 mots, une figure légendée et accessible chacune, les quatre liens présents, navigation complète.
- Playwright (Chromium 1194 de `/opt/pw-browsers`, lancé par `executable_path`, car le paquet Python attend la révision 1243 absente) : 42 clés vertes distinctes ouvertes dans les quatre onglets et les quatre disciplines, aucune « Fiche absente » ni fenêtre vide ; 6 Pareto ouverts avec leur fraction ; **aucune erreur JavaScript** hors l’erreur d’environnement `preview/lesson-core.js` absent de la coque (déjà signalée pour J84 et J12) ; mobile 390 px sans défilement horizontal de page. Rendus ordinateur, fenêtre et mobile vérifiés visuellement (captures de travail dans le scratchpad, non livrées).
- Volume : environ 14 300 mots (cours, fenêtres, références), 42 fenêtres, 6 Pareto, 4 quiz, 4 figures SVG.
- Non fait (rôle du relecteur) : captures `tools/capture_lecon.py`, build `--all-fragments`, tests unitaires, entrée `chapters.json` (`covers` : J95, J98, J99), injection et scellement.
