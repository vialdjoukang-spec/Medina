# J84 — Pneumopathies interstitielles diffuses (P-02-Pneumologie) — rapport de relecture différée

Auto-audit par Agent différé opus 5.5 · 08.10.2026 · cours unique couvrant J84 (J84.0, J84.1, J84.8, J84.9 ; CIM-10-GM 2024, codes dans l'en-tête seulement).
Sources relues : `travail/J84/chapters/J84/` (6 fichiers), `travail/J84/glossary/j84.py`, `rapport_auteur.md`. Le brouillon de l'auteur est conservé intact dans ce dossier ; la version relue est injectée dans `chapters/J84/` et `glossary/j84.py`.

**Cette relecture est une revue par IA. Elle ne vaut pas validation médicale.**

## Règles appliquées

Cahier de la chaîne interne, `STYLE_REDACTION.md`, consignes d'interaction et de densité, sections 7 à 9 puis **section 11 (règle fondamentale du 08.10.2026)** de `LEADERSHIP_CLAUDE_2026-10-08.md`, reçue en cours de relecture : aucune affirmation de mémoire, sources suisses puis européennes, aucune recommandation américaine comme fondement, information professionnelle suisse (AIPS) prioritaire, aucun contenu enseigné sur les codes CIM.

## Réserves de l'auteur : traitement en source primaire

| Réserve | Source lue | Résultat |
|---|---|---|
| 1. Monographies suisses non lues | `tools/swissmedic_fi.py` (AIPS, texte intégral) ; concordance vérifiée avec `ref/fi/L01EX09_Ofev_65330.md` (mise à jour 03.2025) et `ref/fi/L04AX05_Esbriet_66422.md` (mise à jour 08.2022) | **Lue.** Indications suisses : Ofev® = FPI, PID fibrosantes chroniques à phénotype progressif, PID de la sclérodermie ; Esbriet® = FPI seule. Doses, adaptations hépatiques et rénales, contre-indications, conduite devant les transaminases, interactions et surveillance réalignées sur l'AIPS (voir corrections). Les références britanniques (medicines.org.uk) ont été retirées. |
| 2. Nérandomilast | Recherche AIPS (`chercher jascayd`, `nerandomilast`) : aucun résultat ; absent de `ref/fi/INDEX.md`. Page EMA de Jascayd et résumé européen des caractéristiques (sections 4.2 à 4.5, texte intégral du PDF) | Aucune information professionnelle suisse au 08.10.2026. Autorisation de la Commission européenne le 15.07.2026 (FPI et FPP). Toutes les mentions FDA et « étiquetage américain » ont été supprimées. Posologie européenne : 18 mg deux fois par jour ; 9 mg si diarrhée ou perte de poids mal tolérées ou avec un inhibiteur puissant du CYP3A ; jamais de réduction sous pirfénidone ou sous inducteur du CYP3A ; surveillance du poids et de l'état psychique ; non recommandé en Child-Pugh C et en insuffisance rénale terminale. |
| 3. ISHLT 2021 | Leard et al., J Heart Lung Transplant 2021, tableau 3, texte intégral (PDF) | **Erreur corrigée.** L'auteur mélangeait les critères de 2014 et 2021 (distance < 250 m et « PINS fibrosante quel que soit le niveau fonctionnel » appartiennent à 2014). Orientation 2021 : dès le diagnostic d'UIP histologique ou d'aspect UIP certain ou probable ; CVF < 80 % ou DLCO < 40 % ; baisses relatives en deux ans (CVF ≥ 10 %, DLCO ≥ 15 %, CVF ≥ 5 % avec aggravation) ; tout besoin d'oxygène ; connectivite ou forme familiale. Inscription : en six mois malgré le traitement, baisse absolue de CVF > 10 %, de DLCO > 10 % ou de CVF > 5 % avec progression radiologique ; SpO₂ < 88 % ou perte > 50 m au test de marche ; hypertension pulmonaire ; hospitalisation pour déclin, pneumothorax ou exacerbation. |
| 4. ERS/EULAR 2025 | Résumé PubMed (Antoniou, Ann Rheum Dis 2025, doi 10.1016/j.ard.2025.08.021) et liste des recommandations reproduite par RheumNow ; texte intégral inaccessible (ERJ : 403, pas de PMC) | Confirmé et précisé : dépistage par TDM de toute sclérodermie, connectivite mixte et myopathie inflammatoire (hors myosite à inclusions), et des polyarthrites rhumatoïdes et syndromes de Gougerot-Sjögren à facteurs de risque ; sclérodermie : mycophénolate, rituximab, cyclophosphamide, nintédanib suggérés, association nintédanib-mycophénolate suggérée, tocilizumab recommandé dans la forme diffuse récente inflammatoire ; pirfénidone suggérée seulement dans la PID rhumatoïde d'aspect UIP (preuves insuffisantes ailleurs) ; nintédanib suggéré dans toute connectivite avec FPP. La gradation exacte reste celle du résumé secondaire. |
| 5. Ciprofloxacine et surveillance hépatique de la pirfénidone | AIPS Esbriet® | Confirmé : ciprofloxacine 750 mg deux fois par jour → pirfénidone 534 mg trois fois par jour (exposition + 81 %) ; prudence aux doses de 250 ou 500 mg ; bilan hépatique mensuel six mois puis tous les trois mois ; tabac : exposition réduite de 50 %. |
| 6. Chiffres d'essais | Résumés PubMed lus | INPULSIS : **corrigé** (−114,7 contre −239,9 mL et −113,6 contre −207,3 mL ; le chiffre « −223,5 mL » n'a pas été retrouvé) ; ASCEND 47,9 %, INBUILD −80,8 contre −187,8 mL, SENSCIS −52,4 contre −93,3 mL, PANTHER 8 contre 1 décès et 23 contre 7 hospitalisations, FIBRONEER-IPF et -ILD, Cochrane 2021 (+40,07 m) : confirmés. GAP : **corrigé** en 6, 16 et 39 % (valeurs du résumé ; 5,6/16,2/39,2 % et le barème de points n'ont pas été lus et ont été retirés). MUC5B : **corrigé** (fréquence allélique 38 % contre 9 % ; OR 9,0 et 21,8 pour la FPI). EXAFIP : 45 % contre 31 %, **différence non significative (p = 0,10)**, désormais précisé. ACE-IPF : 14 contre 3 décès (Noth 2012, résumé PubMed), ajouté. AmbOx (84 patients, SpO₂ ≤ 88 %) : résumé lu. |
| 7-8. Épidémiologie et recommandation suisses | — | Lacune maintenue et nommée (aucune incidence suisse publiée identifiée ; position suisse Funke-Chambour 2017 citée, non relue). |
| 9. `tests/audit_sciences.py` | — | J84 ajouté à l'exemption (tuple déjà étendu à J96 par l'autre relecteur ; insertion ciblée). Le script ne peut de toute façon pas s'exécuter dans ce clone : le commit de base `c50a28a2` est absent (échec dès I50). Contrat sciences vérifié manuellement avec ses fonctions : 5 disciplines de 298 à 354 mots, une figure accessible chacune, quatre liens présents. |

## Corrections principales

### Fond médical
1. **Mortalité de l'exacerbation aiguë** : « près de la moitié des patients hospitalisés meurent » n'était appuyé par aucune source lue ; remplacé par 29,5 % de mortalité hospitalière dans une cohorte de 78 exacerbations définies selon les critères de 2016 (Yoo, Sci Rep 2022, PMC9130993). Les critères de Collard 2016 ont été contrôlés sur leur reproduction dans des articles PMC (le texte original n'est pas accessible).
2. **Transplantation** : tableau ISHLT réécrit d'après le texte 2021 (voir réserve 3).
3. **Pharmacologie alignée sur l'AIPS** : arrêt de l'Ofev® si 100 mg deux fois par jour reste mal toléré ; conduite devant les transaminases (> 3 LSN : interruption ou 100 mg ; > 5 LSN ou signes hépatiques : arrêt définitif) ; Esbriet® (> 3 à ≤ 5 LSN sans bilirubine : réduction ou interruption ; avec hyperbilirubinémie ou ≥ 5 LSN : arrêt définitif) ; réductions d'Esbriet® pour troubles digestifs (267 mg deux à trois fois par jour) et photosensibilité (267 mg trois fois par jour) ; contre-indications suisses de la pirfénidone (insuffisance hépatique sévère ou terminale, clairance < 30 mL/min ou dialyse, fluvoxamine) ; test de grossesse avant Ofev® ; insuffisance rénale et protéinurie rares sous nintédanib ; diarrhée 62,4 % contre 18,4 % (INPULSIS, AIPS).
4. **Indications** : pirfénidone dans la PID rhumatoïde signalée « hors indication suisse ».
5. **Suivi** : le seuil non sourcé « baisse de CVF de 5 à 10 % en six à douze mois » a été remplacé par les critères sourcés (FPP 2022, inscription ISHLT).
6. **Classification** : tableau ATS/ERS 2013 vérifié sur le texte (PMC5803655, tableaux 1 et 2) ; fenêtre réécrite sur les apports réels de la révision.
7. **Chiffres retirés faute de source lue** : survie médiane de 3 à 5 ans, « plus de deux cents causes », 70-100 m², épaisseurs de la barrière (0,2-0,6 µm), part de surface des pneumocytes I, taille et nombre d'acinus du lobule, compliance de 200 mL/cm d'eau, temps de transit 0,75/0,25 s, formule cellulaire normale du lavage et seuil d'éosinophilie de 25 %, distance de marche de 400 m, seuils de PaO₂ de l'oxygénothérapie, durée « huit à douze semaines » de la réhabilitation, barème de l'indice GAP, MMP-7, ambrisentan, « survie un peu meilleure » des porteurs de MUC5B.

### Plan et forme (règle 4)
- L'îlot 1 ne contient plus de tableau ni de paragraphe sur les sous-codes CIM (ni le cinquième caractère) ; le tableau de la classification des pneumopathies interstitielles idiopathiques prend sa place. Les codes restent dans l'en-tête et le glossaire.
- Les liens vers des cours inexistants (`#/entry/J67`, `#/entry/D86`) ont été supprimés.

### Efficacité et langue
- Pathologie et fenêtres resserrées : suppression des paraphrases (cartes « forme typique » redondantes avec l'îlot 0, lectures de tableaux qui répétaient les en-têtes, épilogues doublant l'annonce), fusion des fenêtres génétiques redondantes avec l'onglet Sciences, raccourcissement des fenêtres à structure répétitive.
- Phrases nominales et infinitifs injonctifs convertis ; titres et annonces centrés sur le problème médical ; aucune phrase décrivant la fabrication du cours.

## Volume

| | Brouillon auteur | Version injectée |
|---|---|---|
| Mots (texte sans balises, 6 fichiers) | 14 219 | 12 047 (−15 %) |
| Fenêtres | 47 (dont 6 Pareto) | 47 (dont 6 Pareto) |

La réduction nette est modérée parce que la relecture a ajouté des données vérifiées (ISHLT 2021, ERS/EULAR 2025, AIPS, résumé européen du nérandomilast, Cochrane, AmbOx). Le cours couvre plusieurs entités (FPI, PINS, connectivites, FPP), ce qui explique l'écart avec J40 (≈ 9 800 mots selon la même mesure).

## Réserves restantes (non bloquantes)

1. **Sciences fondamentales** : les mécanismes cellulaires (TGF-β et intégrine αvβ6, lysyl oxydase, mécanotransduction, télomèropathies et anticipation, SFTPC), la topographie lobulaire et la loi de Fick restent des notions de manuel non rattachées à une source primaire lue ; à sourcer lors de l'audit Codex.
2. Énoncés cliniques appuyés sur la recommandation 2018 et la position suisse 2017, citées mais non relues en texte intégral par le relecteur : facteurs de risque, signes cliniques (prévalence des crépitants, hippocratisme), composition de la discussion multidisciplinaire, bilan sérologique.
3. ERS/EULAR 2025 lue par le résumé et une reproduction secondaire, non en texte intégral.
4. Critères de Collard 2016 contrôlés sur des reproductions secondaires (texte original inaccessible).
5. Codes J84.10/J84.11, J84.80/81, J84.90/91 : vérifiés sur gesund.bund.de (catalogue GM récent), non sur le catalogue BfArM 2024 (page indisponible) ; ils n'interviennent plus que dans le glossaire.
6. Clé `FDA` conservée dans `glossary/j84.py` (inutilisée par le cours, inoffensive).

## Injection

- `chapters/J84/` : 6 fichiers relus. `glossary/j84.py` : glossaire de l'auteur corrigé (J84.0, GAP, INPULSIS, EXAFIP, ACE-IPF, CAPACITY, MUC5B) et complété par `CYP3A`, `AmbOx` et `AIPS`.
- `chapters.json` : entrée `{"code": "J84", "covers": ["J84"], "title": "Pneumopathies interstitielles diffuses", "integrated": true}` insérée après J86 ; entrées J90 et J86 de l'autre relecteur préservées.
- `organisation/course_groups.json` : entrée J84 ajoutée en fin de liste (`owner` « S02 », `covers`, `scope`) ; entrées J90 et J86 préservées.
- `tests/audit_sciences.py` : `'J84'` ajouté au tuple d'exemption (`('J40', 'J96', 'J84')`).
- Aucune opération Git ; aucun autre cours ni dossier de travail modifié.

## Contrôles

| Contrôle | Résultat |
|---|---|
| `python3 -m unittest discover -s tests -p 'test_*.py'` | 230 tests, OK |
| Audit des sigles (`build_medina.py J84`) | `J84 non couvertes: 0` |
| Fenêtres | 47 gabarits ; aucun `data-k` sans gabarit ; 2 fenêtres atteintes depuis le glossaire seulement (`j84-fpi-def`, `j84-genetique`) ; aucun identifiant dupliqué |
| `MEDINA_OUT=…/out_j84 python3 build_front.py --all-fragments` | 22 fragments construits ; S02 : 2 363 448 octets |
| Chromium 1194 (playwright), `MEDINA_S02_respiratoire.html#/entry/J84` | Titre « Pneumopathies interstitielles diffuses » ; 4 onglets non vides ; 65 mots verts cliqués dans les 4 onglets et les 5 disciplines, 65 fenêtres ouvertes avec contenu ; aucune erreur JavaScript ni de console |
| `tools/capture_lecon.py … J84` | Réussite : `j84-1-ouverture.png`, `j84-2-explication.png` (dossier `captures` du bloc-notes de session) |
| `tests/audit_fragments.py` | Échec à l'étape de reproductibilité : deux constructions successives de `MEDINA.html` diffèrent, parce que d'autres agents modifiaient au même moment des chapitres intégrés (I47, J18, J40, J44…, tailles différentes entre les deux constructions). Sans lien démontré avec J84 ; à relancer sur une arborescence stable. |
| `tests/audit_sciences.py` | Non exécutable dans ce clone (commit de base absent) ; contrat vérifié manuellement (voir réserve 9 de l'auteur). |

Empreintes SHA-256 des fichiers injectés :

```
e75b1e5bbdc581fd2f21370bf928b7eccd8aa243121e98b7249d590362a06523  chapters/J84/J84_a.html
46b1af27a53971ef49f2493eba0f3d996588331a283b3d11ec308013a3f93d92  chapters/J84/J84_b.html
cc3c0afffdecf6756ddb394dce522496c9eb9ade39a872aaf1e557b90b5c0d7d  chapters/J84/J84_c.html
de4cfb2d3d7416d3652da84f1250ea554580198de5909ee8267b6b4af41ddc15  chapters/J84/J84_d.html
4867154591eda488b4304c1244321dd1c661e1c26eccaa25d15a9c1be488af5d  chapters/J84/J84_pop1.html
9a69946a89743edb89c23c0722b304a1d6fd5aeb7f78bbf42149f3f459f802c8  chapters/J84/J84_pop2.html
bc756ed020485d6f8c4a805a281e09f2be4b6b5f21d5e8c93326845c80f2079a  glossary/j84.py
```

Statut : injecté, en attente de l'audit croisé Codex. La revue par IA et les tests techniques ne valent pas validation médicale.
