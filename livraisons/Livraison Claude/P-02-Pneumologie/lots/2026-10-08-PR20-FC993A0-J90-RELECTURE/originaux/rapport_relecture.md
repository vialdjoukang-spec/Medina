# J90 — Épanchements pleuraux (P-02-Pneumologie) — rapport de relecture différée

Auto-audit par Agent différé opus 5.5 · 08.10.2026 · cours unique couvrant J90 — Épanchement pleural, non classé ailleurs, J91 — Épanchement pleural au cours de maladies classées ailleurs, et J94 — Autres affections pleurales (CIM-10-GM 2024).
Sources relues : `chapters/J90/` (6 fichiers HTML), `glossary/j90.py` et `rapport_auteur.md` de ce dossier.

**Cette relecture est une revue par IA. Elle ne vaut pas validation médicale.**

## Relecture

J'ai relu intégralement les quatre onglets, les 49 fenêtres et les 6 Pareto. Le contrôle a porté sur les seuils, les doses, les essais, le codage, les mécanismes, la cohérence entre onglets et avec J86, ainsi que sur la langue.

## Vérifications en source primaire

| Point | Source lue | Résultat |
|---|---|---|
| Seuils pH ≤ 7,2 / 7,2–7,4 avec LDH > 900 UI/L / ≥ 7,4 ; glucose < 3,3 mmol/L sans pH ; artefacts de mesure | BTS Guideline 2023, texte intégral | Confirmés, y compris « l’héparine et l’anesthésique local abaissent le pH ; le délai et l’air résiduel l’élèvent ». |
| Cohérence avec J86 — Pleurésies purulentes et abcès du poumon (P-02-Pneumologie) | `travail/J86/` et `chapters/J86/` | Mêmes seuils et même sens des artefacts. La zone intermédiaire est désormais renvoyée vers J86 sans répétition (îlot 9 et fenêtre `j90-ph`). |
| Inhibiteurs de tyrosine kinase, première cause médicamenteuse d’exsudat | BTS Guideline 2023, texte intégral | Confirmé (« the most common drug implicated … being tyrosine kinase inhibitors »). |
| Lidocaïne 1 % : 3 mg/kg (max 250 mg), jusqu’à 4,5 mg/kg (max 300 mg), 7 mg/kg (max 500 mg) avec adrénaline | BTS Clinical Statement on pleural procedures 2023, texte intégral | Confirmé. Ajout : absence de consensus et intérêt d’un grand volume dilué (même source). |
| Œdème de réexpansion : surtout dans la première heure, symptomatique < 1 % ; plafond 1,5 L | BTS procedures 2023 | Confirmé. |
| Anticoagulants : warfarine 5 jours (INR ≤ 1,5), AOD 24–48 h, reprise 1 jour / 2–3 jours, clopidogrel et prasugrel 5 jours, ticagrélor 7 jours, aspirine et héparine prophylactique poursuivies | BTS procedures 2023 | Confirmé. Ajout de l’héparine prophylactique avant la reprise de l’AOD chez le patient à haut risque veineux. |
| Talc 3–4 g calibré, environ 75 % de succès à 3 mois, drain ≥ 12 F | BTS procedures 2023 | Confirmé ; le taux de succès est ajouté dans la fenêtre `j90-talc`. |
| Triglycérides > 1,24 mmol/L, cholestérol > 5,18 mmol/L, amylase > 1, chylothorax idiopathique ≈ 10 % | BTS procedures 2023 et BTS Guideline 2023 | Confirmés. |
| Coexistence infection–cancer ≈ 5 % ; poumon non expansible > 25 % | BTS Guideline 2023 | Confirmés. |
| TIME1 (320 patients ; échec 23 % anti-inflammatoire contre 20 % opioïde ; plus d’antalgie de secours ; drains 12 F non non inférieurs) | PubMed 26720026, résumé | Confirmé. |
| IPC-PLUS (43 % contre 23 % au 35e jour, 4 g au 10e jour) et « plus de 750 000 personnes par an en Europe et aux États-Unis » | PubMed 29617585, résumé | Confirmés. |
| AMPLE (10 contre 12 jours ; 4,1 % contre 22,5 %) | PubMed 29164255, résumé | Confirmé. |
| ERS/EACTS 2018 | PubMed 30054348, résumé ; texte intégral refusé (ERJ 403, PMC derrière vérification de navigateur) | Le résumé concorde : talc et cathéter efficaces, score LENT validé, biopsie tissulaire comme référence, aucune preuve pour un traitement oncologique à la place du drainage. Les détails restent appuyés sur la BTS 2023, plus récente et lue en texte intégral. |
| Libellés CIM-10-GM 2024, bloc J90–J94 | BfArM, page officielle | Confirmés ; voir la correction de J91 ci-dessous. |
| Talc stérile et lidocaïne en Suisse | Compendium (connexion requise), swissmedicinfo (application inaccessible à l’outil), oddb (protection anti-robot) | **Non lus.** Les fenêtres attribuent explicitement les doses à la BTS 2023 et renvoient à l’information professionnelle suisse du produit employé. |

## Corrections apportées

### Fond

1. **J91, code étoile.** Le tableau du codage citait « épanchement malin, lupique ou cardiaque » comme exemples de J91. La page BfArM ne liste aucune inclusion pour J91*, et l’épanchement cardiaque n’est pas une association croix-étoile établie. La cellule parle désormais d’un épanchement dû à une maladie codée ailleurs, une tumeur maligne par exemple, et rappelle que le code ne s’emploie jamais seul. La fenêtre `j90-codage-etoile` est harmonisée.
2. **J90, exclusions.** L’exclusion « pleurésie sans autre précision (R09.1) » a été ajoutée, conformément au BfArM. La clé `R09.1` a été ajoutée au glossaire.
3. **Cas récapitulatif.** Le talc était « instillé » pendant la thoracoscopie ; il y est pulvérisé (poudrage).
4. **Familles de causes.** L’annonce de l’îlot 4 parlait de « deux familles » alors que le tableau en distingue trois (transsudats, exsudats, liquides spécifiques). Elle est corrigée.
5. **Seuils de pH.** L’îlot 9 et la fenêtre `j90-ph` gardent les trois seuils décisionnels, identiques à J86. Le détail de la zone intermédiaire est renvoyé vers J86. Le mésothéliome est ajouté aux causes de pH bas (BTS 2023).
6. **Lidocaïne.** La fenêtre précise l’absence de consensus sur la dose maximale, l’intérêt du volume dilué, et l’attribution des repères. Le Pareto de pharmacologie précise « sans adrénaline, selon la BTS 2023 ».
7. **Œdème de réexpansion.** La conduite est reformulée en phrase complète, avec la régression spontanée chez la plupart des patients (BTS 2023).

### Langue et resserrement

- Les formules décrivant la fabrication du cours ont été supprimées : « Quatre compétences structurent ce cours », « que ce cours rassemble », « ce cours ne propose donc pas de chiffre national », « elle est traitée ici… sans second cours », « Le tableau associe chaque question… », « La fiche suivante rassemble… », « La fiche se lit dans l’ordre des colonnes », « Le tableau situe chaque classe… », « Le tableau se lit à partir du diagnostic… », « Le tableau montre… », « Le tableau rappelle… ».
- Les infinitifs injonctifs et les phrases nominales ont été convertis en phrases complètes : la liste ordonnée de la démarche diagnostique (îlot 7), l’« À retenir » de la pharmacologie, celui de l’anamnèse et la conduite de l’œdème de réexpansion.
- Les doublons ont été fusionnés entre le corps et les fenêtres, sans perte d’information. Sont concernés transsudat et exsudat, Starling, le mécanisme de la dyspnée (déjà développé dans l’îlot 3 et en Physiologie), l’hémothorax, le chylothorax, le fibrothorax, ainsi que les doses de talc reprises du tableau P-2. Les délais d’arrêt des anticoagulants restent dans la fenêtre, car celle-ci s’ouvre aussi depuis l’onglet Pathologie.
- Plusieurs phrases ont été resserrées et rythmées : définition, pronostic, mécanismes, terrain, examen clinique, prise en charge, épanchement malin et physiologie.

### Volume

| Mesure (texte visible, figures SVG exclues) | Avant | Après |
|---|---|---|
| Cours (onglets A à D) | 8 037 mots | 7 896 mots |
| Fenêtres et Pareto | 6 324 mots | 6 281 mots |
| Total | 14 361 mots | 14 177 mots (−1,3 %) |

Le décompte de l’auteur, environ 13 400 mots, n’inclut ni les tableaux ni les sommaires. Le gain de volume est modeste. Le cours était déjà dense, et les ajouts vérifiés compensent en partie les suppressions : délais de reprise des anticoagulants, consensus sur la lidocaïne, taux de succès du talc. Aucune information utile n’a été retirée.

## Réserves restantes (non bloquantes)

1. **Monographies suisses non lues.** Ni le talc stérile (statut d’enregistrement : médicament ou dispositif) ni une lidocaïne suisse n’ont pu être consultés : Compendium exige une connexion, swissmedicinfo et oddb sont inaccessibles à l’outil. Les doses sont attribuées à la BTS 2023. Pour mémoire, des informations professionnelles allemandes trouvées par recherche, sans texte suisse, indiquent un plafond de 300 mg sans vasoconstricteur.
2. **ERS/EACTS 2018** : seul le résumé a été lu.
3. **Aucune source suisse spécifique** sur les épanchements pleuraux ni aucune incidence suisse : la lacune est nommée dans l’îlot 2.
4. **Affirmations classiques non rattachées à une source lue en texte intégral**, sans contradiction relevée : sémiologie (matité, vibrations, frottement), latéralisation droite de l’épanchement cardiaque unilatéral et de l’hydrothorax hépatique, hypersensibilité dans la pleurésie tuberculeuse, épanchement de la prééclampsie, causes médicamenteuses classiques (amiodarone, méthotrexate, nitrofurantoïne, dérivés de l’ergot), pH et glucose bas dans la polyarthrite rhumatoïde, profils du tableau E-4.
5. **Codage de l’épanchement malin** (code de la tumeur et J91*) : il est conforme à la logique croix-étoile, mais les Deutsche Kodierrichtlinien n’ont pas été lues.
6. **Seuils chirurgicaux de l’hémothorax** (débit) : volontairement absents, faute de source lue.
7. **`tests/audit_sciences.py`** échoue avant même J90, sur I50 (« path exists on disk, but not in c50a28a… ») : le commit de base est indisponible dans ce clone. Aucune exemption n’a été ajoutée, car le problème est global et antérieur. Une exemption « nouvelle production » sur le modèle de J40 deviendra nécessaire pour J90 quand la base sera disponible.

## Injection

- `chapters/J90/` : 6 fichiers relus, identiques à ceux du dossier de travail.
- `glossary/j90.py` : 16 entrées (15 de l’auteur et `R09.1`). Juste avant l’injection, j’ai vérifié qu’aucune ne figurait déjà dans `glossary/*.py`, y compris `BTS` ; les fichiers `j84.py` et `j86.py` injectés en parallèle ne créent aucun doublon.
- `chapters.json` : une entrée a été insérée après J09, `{"code": "J90", "covers": ["J90","J91","J94"], "title": "Épanchements pleuraux", "integrated": true}`. Les entrées des autres relecteurs (J86, J93, J96) sont préservées.
- `organisation/course_groups.json` : une entrée J90 a été ajoutée avec `owner` « S02 », les mêmes `covers` et un `scope` d’une phrase ; l’entrée J86, ajoutée ensuite, est préservée.
- Aucun autre cours n’a été modifié. Aucune opération Git n’a été effectuée.

## Contrôles

| Contrôle | Résultat |
|---|---|
| `python3 -m unittest discover -s tests -p 'test_*.py'` | 176 tests, OK |
| Audit des abréviations (`build_medina.build` sur J90, sortie dans le dossier temporaire) | `{}` après l’ajout de `R09.1` |
| Clés des fenêtres | 55 `data-k`, 55 gabarits ; aucune clé manquante, orpheline ou en double ; aucune collision `j90-` avec un autre chapitre |
| Pareto | 6 fractions calculées (4 à 10 %) |
| `MEDINA_OUT=…/out_j90 python3 build_front.py --all-fragments` | Code de sortie 0 ; 22 fragments ; S02 : 4 193 777 octets. Le build signale « J86 non couvertes 1 », qui relève du relecteur de J86. |
| Chromium (`/opt/pw-browsers/chromium`), `MEDINA_S02_respiratoire.html#/entry/J90` | Titre « Épanchements pleuraux » ; 4 onglets non vides ; 55 fenêtres présentes avec contenu, 84 ouvertures réussies par clic dans l’interface ; aucune erreur JavaScript ni de console |
| `tools/capture_lecon.py … J90` | Réussite : `j90-1-ouverture.png`, `j90-2-explication.png` (fenêtre « Ponction pleurale ») dans `scratchpad/captures/` |
| `tests/audit_fragments.py` | Aucun défaut lié à J90. Les défauts signalés (« S02 manque des cours : J93 ») viennent de l’injection parallèle de J93, postérieure à mon build. |

Empreintes SHA-256 des fichiers injectés :

```
b7079dafe878d1ff78821ed7f33b3f1b1d4b08ca799be6568fbddcc085fddb65  chapters/J90/J90_a.html
41cb99eb93a492b87f831736424da2da3a6446b40b3ebcd145d13df7c7986566  chapters/J90/J90_b.html
bc6049dbc8c0a550e2209ad37f0702d51b045830655c69fd3c4a40d808b38008  chapters/J90/J90_c.html
a1ad59b7bc4282475c8ba97d42c37357f4c75394c841f3c42949d2032477665c  chapters/J90/J90_d.html
4799ab32e0a2d0a4330fcf66f2881d494738b2d12ce130bdb684374925e47f1c  chapters/J90/J90_pop1.html
6f71457cff8dd73103bf47641037089e8743030286b71f63c1617547d179506b  chapters/J90/J90_pop2.html
74f670cdc7e8ddf7bb025c2ac83ba8c2d6b2e6be53b7d68b618e9789bf7c0225  glossary/j90.py
```

Statut : injecté, en attente de l’audit croisé Codex. La revue par IA et les tests techniques ne valent pas validation médicale.
