# J93 — Pneumothorax (P-02-Pneumologie) — rapport de relecture différée

Auto-audit par Agent différé opus 5.5 · 08.10.2026 · cours unique couvrant J93 (J93.0, J93.1, J93.8, J93.9 ; CIM-10-GM 2024).
Sources relues : `travail/J93/` (6 fichiers HTML, `glossary/j93.py`, `rapport_auteur.md`).

**Cette relecture est une revue par IA. Elle ne vaut pas validation médicale.**

## 1. Déroulement

1. Première passe (fond, langue, resserrement) sur le texte de l’auteur, puis injection et contrôles verts.
2. En cours de mission, le coordinateur a transmis la **règle fondamentale de la section 11** de `LEADERSHIP_CLAUDE_2026-10-08.md` (aucune affirmation de mémoire ; sources suisses puis européennes ; aucune recommandation américaine comme fondement ; information professionnelle suisse pour les doses ; aucun îlot consacré au codage). Le cours a donc été **réécrit intégralement** sur les seules sources lues ci-dessous, puis réinjecté et recontrôlé.

## 2. Sources effectivement lues (08.10.2026)

| Source | Accès | Usage principal |
|---|---|---|
| Roberts et al., BTS 2023, Thorax (doi 10.1136/thorax-2022-219784) | Texte intégral (PDF BTS) | Définitions, recommandations, tableaux 4 et 5, indications chirurgicales, sortie, vol, plongée, grossesse, cataménial, mucoviscidose, familial, iatrogène et traumatique |
| BTS 2023, annexe 1 (parcours du pneumothorax) | Texte intégral | Six caractéristiques à haut risque, seuil de 2 cm, rythmes de suivi |
| Asciak et al., déclaration BTS sur les gestes pleuraux 2023 + annexe 12 | Texte intégral | Triangle de sécurité, bord supérieur de la côte, abord postérieur, lidocaïne (3 mg/kg, au plus 250 mg ; absence de consensus), talc 4–5 g dans 50 mL, clampage, aspiration, œdème de réexpansion |
| O’Driscoll et al., BTS oxygène 2017 (section 8.11.6, F5, F6) | Texte intégral | Cibles 94–98 % et 88–92 %, haute concentration 15 L/min, résorption jusqu’à 4 fois, toxicité au-delà de 60 % chez le lapin |
| Walker et al., recommandations ERS/EACTS/ESTS 2024, Eur Respir J (doi 10.1183/13993003.00797-2023) | **Résumé seulement** (texte intégral 403) | Surveillance (conditionnelle), aspiration préférée au drain (forte), ambulatoire, chirurgie précoce, sang autologue dans la forme secondaire |
| Harnedy et al., Breathe (ERS) 2025 (doi 10.1183/20734735.0250-2024) | Texte intégral (Europe PMC) | Épidémiologie (pics d’âge), étiologie (lésions emphysémateuses, porosité, métalloprotéinases), diagnostic (50 mL, sillon profond, imitations), échographie, fuite persistante, sang autologue, valves, recommandations ERS 2024 détaillées, causes familiales, maladies kystiques (≤ 10 %) |
| Jouneau et al., recommandations SPLF/SFMU/SRLF/SFAR/SFCTCV 2023, Ann Intensive Care (doi 10.1186/s13613-023-01181-2) | Texte intégral (Europe PMC) | Définition du grand pneumothorax, imagerie, tension et sites de décompression, ambulatoire, drain ≤ 14 French, aspiration −5 à −20 cm d’eau, pas d’oxygène systématique, analgésie, pleurodèse, vol (≥ 2 semaines), plongée, sports |
| Lott et al., ERC 2025, circonstances particulières, Resuscitation 2025;215:110753 | Texte intégral (PDF) | Diagnostic de tension, thoracostomie bilatérale au 4e espace axillaire moyen, aiguille de recours, prévalence 0,5 % et 13 %, patient ventilé |
| Tschopp et al., ERS 2015 | Résumé PubMed | Approche par les symptômes, talc calibré, rôle incertain des bulles |
| Melton 1979, Bense 1987, Walker 2018, Brown 2020, Hallifax 2020, Marx 2023, Tschopp 2002, Alrajhi 2012, Lichtenstein 2000, Collins 1995 | Résumés PubMed / Europe PMC | Chiffres repris tels qu’écrits dans les résumés |
| Informations professionnelles suisses (AIPS via AmiKo ; corpus `ref/fi/`) : Lidocaine Aguettant 10 et 20 mg/ml ; Paracetamol-Mepha 500 mg ; Morphini HCl Streuli | Texte intégral | Lidocaïne : 3–5 mg/kg, maximum 200 mg pour l’infiltration, signes et traitement de la toxicité ; paracétamol : > 40 kg, 500–1 000 mg toutes les 4–6 h, ≤ 4 g/j, ≤ 2 g/j si hépatopathie chronique ; morphine : prudence dans les maladies obstructives, association aux benzodiazépines |

## 3. Corrections et changements principaux

### Conformité à la règle de la section 11
- **Codage supprimé du contenu** : îlot 1 « Définition, classification et codage » devenu « Définition et classification » ; tableau des codes et paragraphe des exclusions retirés ; titres des fenêtres traumatique et iatrogène sans code ; clés `J95.80`, `S27.0`, `P25.1` retirées du glossaire (les codes J93.x restent dans l’en-tête).
- **Sources américaines retirées comme fondement** : site d’exsufflation ATLS remplacé par SPLF 2023 et ERC 2025 ; mesure ACCP supprimée ; clés `ACCP` et `ATLS` retirées.
- **Affirmations de mémoire retirées** : valeurs de pression pleurale (−5/−8 cm d’eau), vitesse de résorption (1,25–2,2 %/jour), limite d’aspiration de 2,5 L (BTS 2010 non lue), « 2 cm au hile ≈ 50 % », cabine à 2 400 m et +30 %, longueur de cathéter de 8 cm, valeurs normales des gaz du sang, tableau des différentiels (embolie, syndrome coronarien, pneumomédiastin), causes secondaires non documentées (pneumocystose, tuberculose, néoplasies, pneumopathies interstitielles) — **lacune nommée dans l’îlot 4**, tympanisme et vibrations vocales (fenêtre `j93-tympanisme` supprimée), mécanismes de l’œdème de réexpansion, détails phénotypiques des maladies génétiques, « talc non calibré → SDRA ».
- **Oxygène sourcé** : BTS 2017 lue (F5, F6, quadruplement) ; contentieux présenté avec la SPLF 2023, plus récente, qui recommande de **ne pas administrer systématiquement d’oxygène** dans le pneumothorax primaire (texte retenu).
- **Doses suisses** : lidocaïne plafonnée à 200 mg (information professionnelle suisse, prime sur la BTS 250 mg ; instillation pleurale signalée hors indication suisse) ; paracétamol aligné sur l’information suisse (4 à 6 heures, ≤ 2 g/j en cas d’hépatopathie). Talc : **aucune information professionnelle suisse** dans le corpus AIPS — lacune nommée, dose attribuée à la BTS.

### Corrections médicales et ajouts sourcés
- **Source primaire la plus récente** : la recommandation conjointe ERS/EACTS/ESTS 2024, absente de la version d’auteur, est désormais la référence européenne (fenêtre `j93-bts-ers` réécrite) : aspiration fortement préférée au drain pour le primaire symptomatique ; ni aspiration ni ambulatoire dans le secondaire ; chirurgie précoce proposable ; sang autologue dans la fuite persistante secondaire.
- **Contentieux explicités** (fenêtres à mots verts, texte retenu et texte contemporain) : délai avant l’avion (BTS 7 jours / SPLF ≥ 2 semaines, retenu) ; plongée après pleurodèse (BTS : possible après pleurectomie / SPLF : contre-indiquée même après pleurodèse, retenu) ; oxygène.
- **Décompression** : ERC 2025 lu (thoracostomie ouverte immédiate en cas d’arrêt ou d’hypotension sévère ; thoracostomies bilatérales au 4e espace intercostal axillaire moyen dans l’arrêt traumatique ; aiguille de recours) et SPLF 2023 (abord antérieur 2e espace médioclaviculaire ou axillaire 4e espace).
- Indications chirurgicales alignées sur la liste de la BTS 2023 (premier épisode sous tension, secondaire mal toléré…) ; « deuxième récidive » corrigé en « deuxième épisode ».
- Essai de Tschopp 2002 complété (récidive à 5 ans 5 % contre 34 %) ; essai de Marx (critère principal, non-infériorité non démontrée) ; Hallifax (8 événements liés au dispositif).
- Physiologie : mécanisme de résorption corrigé et sourcé (gradient d’azote décrit par la SPLF).
- Prise en charge : critères d’ambulatoire de la SPLF (4 heures, filière, contrôle à 24–72 h, entourage, accès < 1 h), drain ≤ 14 French, aspiration seulement en l’absence de réexpansion, clampage à éviter.

### Langue et forme
- Phrases resserrées et rythmées ; formules de fabrication supprimées ; infinitifs injonctifs convertis (« À retenir » des îlots 9 et 11, pharmacologie).
- **Traits d’union insécables (U+2011)** : remplacés par des traits d’union ordinaires (recherche et copie fiables). Solution conforme du projet : clé `Birt-Hogg-Dubé` (éponyme, sur le modèle de `Ehlers-Danlos`) ; reformulations pour les autres (« admissions britanniques », « centres australiens et néo-zélandais », « pneumologue valaisan Tschopp », « loi de Boyle » supprimée au profit d’une formulation physique générale).

### Glossaire
- `BTS` déjà défini dans `glossary/j90.py` : retiré de `j93.py`. `GRADE`, `CFTR` absents ailleurs : conservés. Ajouts : `SPLF`, `Birt-Hogg-Dubé`. Définitions de `FLCN`, `TSC1`, `TSC2`, `CFTR` réduites au contenu sourcé.

## 4. Volume (mots visibles, SVG exclus, références comprises)

| | Auteur | Après relecture |
|---|---|---|
| Total | 12 962 | 12 142 |
| Fenêtres | 43 + 6 Pareto | 42 + 6 Pareto |

Le gain brut est modeste (−6 %) : la réécriture a retiré l’inventé et le redondant, mais ajouté les recommandations ERS 2024, SPLF 2023 et ERC 2025, les contentieux exigés et les références datées dans chaque fenêtre (~700 mots de références). Le corps de l’onglet Pathologie est resserré ; le détail est dans les fenêtres.

## 5. Réserves restantes

1. **ERS/EACTS/ESTS 2024** : texte intégral inaccessible (403) ; recommandations reprises du résumé et de la revue Breathe 2025 (ERS), qui les détaille. Les positions ERS 2024 sur l’avion et la plongée n’ont pas été lues.
2. **Notions générales non adossées individuellement à une source** : quelques énoncés élémentaires de sémiologie et de physiologie restent formulés sans source primaire propre (fonction du couplage pleural, variation du volume d’un gaz avec la pression, signification de l’abolition du murmure en dehors de la tension, mesures de gravité initiales). À sourcer ou à valider par l’audit Codex.
3. **Gènes** (FLCN, TSC1/TSC2, FBN1, COL3A1, SERPINA1, CFTR) : nomenclature non confirmée par les sources lues, qui citent les syndromes sans leurs gènes.
4. Résumés seulement pour les essais et l’ERS 2015 ; BTS 2010 non lue (seule sa mention « avis chirurgical à 3–5 jours » est reprise, via la BTS 2023).
5. Talc stérile : aucune information professionnelle suisse trouvée (dispositif ou préparation hors corpus AIPS).
6. Exemple de l’annexe 12 BTS incohérent (« 3 mg/kg… soit 20 mL à 1 % pour 60 kg » = 200 mg > 180 mg) ; le cours calcule 180 mg.
7. Aucune donnée d’incidence suisse ; aucune recommandation suisse sur le pneumothorax identifiée.

## 6. Injection

- `chapters/J93/` : 6 fichiers ; `glossary/j93.py`.
- `chapters.json` : entrée `{"code": "J93", "covers": ["J93"], "title": "Pneumothorax", "integrated": true}` insérée après J96.
- `organisation/course_groups.json` : entrée J93, `owner` « S02 », `covers` ["J93"], `scope` en une phrase.
- `tests/audit_sciences.py` : J93 ajouté à la liste des nouvelles productions sans version de base (`('J40', 'J96', 'J84', 'J93')`).
- Aucune autre leçon modifiée ; aucune opération Git.

## 7. Contrôles (version finale)

| Contrôle | Résultat |
|---|---|
| `python3 -m unittest discover -s tests -p 'test_*.py'` | 230 tests, OK |
| Audit des sigles J93 (`transform` + `wrap_html` + `audit`) | `{}` |
| `test_v7.py --static J93` | OK (48 fenêtres, 3 quiz, 6 Pareto) |
| Contrat sciences (fonctions de `tests/audit_sciences.py`) | 4 disciplines (357 à 393 mots), 1 figure légendée chacune, 4 liens présents |
| Clés | 48 `data-k`, 48 gabarits, aucune orpheline |
| Pareto | 6 fractions (5 à 17 %) |
| `build_front.py --fragment S02` | OK |
| `build_front.py --all-fragments` | **Échec hors J93** : le fragment S01 ne se construit pas (`I70 … texte natif introuvable sous i70-10`), I70 étant en cours de modification par un autre agent dans l’arbre de travail. Avant la réécriture imposée par la section 11, le build complet et `tests/audit_fragments.py` (22 fragments, JavaScript valide, build reproductible) étaient verts. Le build signale aussi `J09 non couvertes 2` (`ECDC`, `Panton-Valentine`) et `I26 non couvertes 3`, sans lien avec J93. |
| Chromium `MEDINA_S02_respiratoire.html#/entry/J93` | Titre « Pneumothorax » ; 48/48 fenêtres ouvertes avec contenu ; aucune erreur JavaScript |
| `tools/capture_lecon.py … J93` | Réussite : `j93-1-ouverture.png`, `j93-2-explication.png` (dossier `scratchpad/captures` de la session) |

Empreintes SHA-256 :

```
5ea55d8bf42cb038db6408d7c8ef74d5da808dc81119046fd6bc172a6a1c8e3d chapters/J93/J93_a.html
ea22663a08e1ab60e8c647a9a380710999bd6c1d1fae76831320be6be6893ff8 chapters/J93/J93_b.html
24c382f5fcdbce782eede7b48b0ede8185cffeec35c534f76911525065a7af74 chapters/J93/J93_c.html
306001496a147176cee8463f3141c6a4b185fb7e8b93ae4b754f1fc441e57c63 chapters/J93/J93_d.html
eb047ab27d6d1ec6b2120b6e223825b528cdc6993378fcd15c01512dcdcf144c chapters/J93/J93_pop1.html
a24c851b5201859078635f421ec27b436e72d0665aef9b8f44c46fd4cd13465c chapters/J93/J93_pop2.html
1a9467ed12f239f50d9537b3249c53f27a8d706e7f72526005076e65d04ec7e0 glossary/j93.py
```

Statut : injecté, en attente de l’audit croisé Codex. La revue par IA et les tests techniques ne valent pas validation médicale.
