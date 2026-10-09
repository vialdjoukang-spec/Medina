# J86 — Pleurésies purulentes et abcès du poumon (P-02-Pneumologie) — rapport de relecture différée

Auto-audit par Agent différé opus 5.5 · 08.10.2026 · cours unique couvrant J85 — Abcès du poumon et du médiastin et J86 — Pyothorax (CIM-10-GM 2024).
Sources relues : `chapters/J86/*.html` (6 fichiers), `glossary/j86.py` et `rapport_auteur.md` de ce dossier.

**Cette relecture est une revue par IA. Elle ne vaut pas validation médicale.**

## Relecture

J'ai relu intégralement les quatre onglets, les 50 fenêtres et les 6 Pareto. Le contrôle a porté sur les chiffres, les seuils, les posologies, les mécanismes, les renvois et la cohérence entre onglets.

Chiffres contrôlés en source primaire (PubMed, résumés ; PMC, texte intégral pour Kuhajda) :
- **PILOT** (Corcoran 2020, doi:10.1183/13993003.00130-2020) : 546 patients recrutés, 542 analysés ; mortalité 10 % à 3 mois et 19 % à 12 mois ; RAPID 0–2 : 2,3 %, 3–4 : 9,2 %, 5–7 : 29,3 % ; statistique C 0,78. Confirmés.
- **Maskell 2006** (doi:10.1164/rccm.200601-074OC) : 50 % de streptocoques et 20 % d'anaérobies en communautaire ; 60 % de bactéries souvent résistantes en nosocomial ; mortalité nosocomiale 47 % contre 17 %, *S. aureus* 44 %, streptocoques 17 %. Confirmés.
- **SLIM** (Hassan 2023, doi:10.1183/23120541.00635-2022) : 50 patients, RAPID > 4 exclus, 14–21 contre 28–42 jours, échec 16,7 % contre 12,5 %. Confirmés.
- **Kuhajda 2015** (PMC4543327, texte intégral) : mortalité historique 75 %, actuelle 2,0–38,2 % ; durée totale 28–48 jours ; clindamycine 600 mg toutes les 8 heures par voie intraveineuse ; drainage percutané 11–21 %, succès 84 %, complications 16 % ; chirurgie 10 %, cavité > 6 cm ; normalisation radiologique à deux mois ; aminosides non recommandés. Confirmés.
- **MIST1, MIST2, critères de Light, liquide pleural normal (Noppen)** : chiffres cohérents avec les résumés cités par l'auteur, sans contradiction relevée.

## Corrections apportées

### Fond

1. **PILOT** : effectifs harmonisés (542 analysés sur 546 recrutés). Les valeurs contradictoires 542, 545 et 546 ont disparu. La phrase « plus de 30 % meurent ou sont opérés » n'est plus attribuée à PILOT : elle décrit l'état antérieur rapporté par ses auteurs.
2. **Maskell** : le texte attribuait 25 % des infections nosocomiales à « *S. aureus*, y compris résistant ». Ce chiffre concerne le seul staphylocoque résistant à la méticilline ; la cellule est corrigée.
3. **Abcès, réponse au traitement** : « défervescence en 4 à 7 jours » est remplacé par « amélioration de l'état général en 4 à 7 jours », conformément à Kuhajda.
4. **Clindamycine** : la dose orale de 300 mg toutes les 8 heures n'était pas sourcée. Elle est désormais située dans l'intervalle de 600 à 1 800 mg par jour de l'information professionnelle allemande de Dalacin C. La monographie suisse est déclarée non lue.
5. **Actilyse** : les indications ont été vérifiées dans l'information professionnelle allemande (fachinfo.de, avril 2026) : infarctus, embolie pulmonaire massive avec instabilité hémodynamique, accident vasculaire cérébral ischémique dans les 4,5 heures. Elles concordent avec le résumé britannique. Le lien a été ajouté.
6. **Contentieux du pH** : la fenêtre `j86-seuils-ph` nomme maintenant les deux sources et leur relation. La BTS 2023 (« ≤ 7,2 ») est la plus récente et elle est retenue. Les textes antérieurs, repris par J18 — Pneumonies de l'adulte (P-02-Pneumologie), écrivent « < 7,2 ». L'écart ne porte que sur un pH égal à 7,2.
7. **Durée d'antibiothérapie** : l'essai espagnol de deux contre trois semaines d'amoxicilline-acide clavulanique est ajouté d'après la synthèse de Skouras (Breathe 2023, doi:10.1183/20734735.0134-2023). Le sigle de l'essai n'est pas utilisé.
8. **Note suisse** : la fenêtre sur l'antibiothérapie pleurale cite le schéma de la Société suisse d'infectiologie pour la pneumonie d'inhalation, repris de J18 : amoxicilline-acide clavulanique 2,2 g toutes les 8 heures par voie intraveineuse. Le protocole local prime.
9. **Libellé A41** : le titre est corrigé en « A41 — Sepsis et choc septique de l'adulte ».

### Renvois sans répétition

- J18 — Pneumonies de l'adulte : la pneumonie et l'échec thérapeutique y sont renvoyés (îlot 0, fenêtres `j86-fievre-persistante` et `j86-seuils-ph`) ; J86 ne les redéveloppe pas.
- A41 — Sepsis et choc septique de l'adulte : le renvoi figure dans l'îlot 0 et dans la fenêtre `j86-sepsis`. Seul le contrôle de la source, propre à J86, est traité dans le cours.
- J90 — Épanchements pleuraux (injecté en parallèle) : la démarche exsudat ou transsudat y est renvoyée depuis la fenêtre `j86-light`.

### Efficacité et langue

- Les redondances ont été supprimées entre îlot 3, fenêtres `j86-ph`, `j86-pai1` et `j86-continuum`, ainsi qu'entre la définition de l'abcès (îlot 1) et la fenêtre `j86-abces-def`, recentrée sur les formes primaire et secondaire.
- Le protocole alteplase et dornase était répété sept fois. Il reste dans l'îlot 9, le tableau des doses, la fenêtre `j86-iet`, les paramètres clés et les Pareto. Les monographies d'alteplase, de dornase et d'amoxicilline-acide clavulanique renvoient au tableau des doses.
- Les îlots 7, 9, 10 et 11, les paragraphes de lecture des tableaux et les onglets Examens et Pharmacologie ont été resserrés. Les fenêtres MIST2, durée, ponction, échographie, cancer excavé et chirurgie vidéo-assistée ont été condensées.
- Les phrases nominales et les listes de mots-clés des fenêtres sont devenues des phrases complètes : définitions, arguments, signes, conduites.
- Le vocabulaire a été précisé : coque collagène, limpidité, fibrothorax, exacerbée.
- Le bandeau ne décrit plus le statut de fabrication (« version de travail ») et porte les référentiels, comme J09 et J40.
- Les sciences sont laissées au-dessus du seuil de 280 mots par discipline (anatomie 317, physiologie 285, biochimie 339, microbiologie 298), avec une figure légendée et les quatre liens de corrélation chacune.

### Volume

| Mesure (texte visible, schémas exclus) | Avant | Après |
|---|---|---|
| Total des 6 fichiers | 12 268 mots | 11 391 mots (−7 %) |
| Dont références bibliographiques | — | 561 mots |
| Corps des onglets Pathologie et Pharmacologie (a, b, d) | 4 929 | 4 326 (−12 %) |

J40 — Bronchite mesure 9 693 mots selon la même méthode. L'écart restant tient à la double couverture J85 et J86 : abcès, gangrène, médiastin et infection pleurale. Aucune notion utile n'a été retirée.

## Glossaire

La clé `BTS` existe déjà dans `glossary/j90.py`, injecté avant J86. Elle a été retirée de `glossary/j86.py`, avec un commentaire. Aucune autre clé de J86 (ESTS, MIST1, MIST2, RAPID, PILOT, SLIM, J85.0–J85.3, J86.0–J86.09, J86.9) n'existe dans un autre glossaire du dépôt au moment de l'injection. La description de PILOT est corrigée : 546 recrutés, 542 analysés.

## Injection

- `chapters/J86/` contient les 6 fichiers relus ; `glossary/j86.py` est injecté. Les copies de ce dossier de travail sont identiques.
- `chapters.json` : l'entrée `{"code": "J86", "covers": ["J85","J86"], "title": "Pleurésies purulentes et abcès du poumon", "integrated": true}` a été insérée après J90 par une édition ciblée. Les entrées J84 et J96, injectées en parallèle, sont préservées.
- `organisation/course_groups.json` : l'entrée J86 porte `owner` « S02 », les mêmes `covers` et un `scope` qui renvoie la pneumonie à J18, le sepsis à A41 et les épanchements non purulents à J90.
- `tests/audit_sciences.py` n'a pas été modifié : aucune exemption n'est nécessaire. Le script n'est appelé par aucun test unitaire. Il échoue d'ailleurs déjà avant J86 sur I50, dont le fichier est absent du commit de base dans ce clone. Ses critères ont été appliqués à J86 directement, sans erreur.
- Aucun autre cours n'a été modifié. Aucune opération Git n'a été effectuée.

## Réserves restantes (non bloquantes)

1. **Société suisse d'infectiologie** : il n'existe pas de recommandation lue pour l'empyème ou l'abcès, et le site est une application JavaScript. Le cours le signale et renvoie au protocole local.
2. **Monographies suisses** d'Actilyse, de Pulmozyme, de Dalacin C et du métronidazole : aucune n'a été lue (Compendium soumis à connexion, ch.oddb.org bloqué). Les indications d'Actilyse sont vérifiées dans les textes allemand (avril 2026) et britannique. Aucune dose de métronidazole n'est donnée. La dose orale de clindamycine est rattachée au texte allemand.
3. **Adaptation rénale** de l'amoxicilline-acide clavulanique : aucun chiffre n'est donné ; le cours renvoie à la fonction rénale.
4. **Connaissances classiques non rattachées à une source primaire relue** : seuil radiographique de 200 mL, examen peu sensible sous 300 mL, critères scanographiques de l'empyème et de l'abcès, hématocrite pleural supérieur à la moitié de l'hématocrite sanguin pour l'hémothorax, hippocratisme absent dans la BPCO non compliquée, bronchoscopie au-delà de 40 ans. Ces formulations sont prudentes ; aucune contradiction n'a été relevée.
5. **Déclaration ERS/ESTS 2023** : seul le résumé a été lu ; le texte intégral a été refusé à l'auteur (403).

## Contrôles

| Contrôle | Résultat |
|---|---|
| `python3 -m unittest discover -s tests -p 'test_*.py'` | 176 tests, OK (avant et après les injections parallèles de J84 et J96) |
| Audit des sigles (`build_medina.build` sur J86, copie dans le dossier temporaire) | `{}` après correction de « ERJ » écrit en toutes lettres |
| Clés des fenêtres | 56 clés `data-k`, 56 gabarits ; aucune clé manquante ni orpheline ; aucun identifiant dupliqué ; préfixes `j86-` |
| Pareto | 6 fractions calculées (4 à 11 %), aucun îlot introuvable |
| `MEDINA_OUT=…/out_j86 python3 build_front.py --all-fragments` | 22 fragments construits ; `MEDINA_S02_respiratoire.html` : 2 317 216 octets |
| Chromium (`/opt/pw-browsers/chromium`), `MEDINA_S02_respiratoire.html#/entry/J86` | Titre « Pleurésies purulentes et abcès du poumon » ; 4 onglets non vides ; 56 fenêtres ouvertes ; aucune erreur JavaScript ni erreur de console |
| `tools/capture_lecon.py … J86` | Réussite : `j86-1-ouverture.png` et `j86-2-explication.png` dans le dossier temporaire de la session |

Empreintes SHA-256 des fichiers injectés :

```
bb9e19c754141b62d064acbfdd7fc576e3df1b9855bee6f4a9b9f9a8c93bbb8e chapters/J86/J86_a.html
a09b26805294bbc6e0ca601d3a5403e9f24f253f8474fb98fbe919ec11bf7c6f chapters/J86/J86_b.html
20e35c6e3d71a6ec460c66a2b8d47d8f2e41a87fc08ed9e94bace40f7759dd3e chapters/J86/J86_c.html
e8c526cb52665e91994fc227b7c36ccabfa008dcbb3337f69c790ce1d629856e chapters/J86/J86_d.html
a366308f395abeb3e18f030f41ea1516bc163c6904924aff6391333668fa4948 chapters/J86/J86_pop1.html
9cbdbf5244764f483c199352f7e3bb147fee5a3ed1ce3e891a3cd151bac5aa8d chapters/J86/J86_pop2.html
c7d791f166a7cc59780cfe7662c143361ed2a7255ab11db4c998c83efe7d7bc8 glossary/j86.py
```

Statut : injecté, en attente de l'audit croisé Codex. La revue par IA et les tests techniques ne valent pas validation médicale.
