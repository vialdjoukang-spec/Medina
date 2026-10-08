# J09 — Grippe (P-02-Pneumologie) — rapport de relecture différée

Auto-audit par Agent différé opus 5.5 · 08.10.2026 · cours unique couvrant J09, J10 et J11 (CIM-10-GM 2024).
Sources relues : `espace_partage/COURS_CLAUDE_A_AUDITER_PAR_CODEX/J09/sources/` (8 fichiers HTML, `glossary/j09.py`) et `rapport_auteur.md`. Le `chapters.json` de ce dossier, copie ancienne, n'a pas été utilisé.

**Cette relecture est une revue par IA. Elle ne vaut pas validation médicale.**

## Relecture

J'ai relu intégralement les quatre onglets et les 144 fenêtres. Le contrôle a porté sur les seuils, les posologies, l'adaptation rénale, les indications suisses, la vaccination OFSP 2026, les mécanismes, les sources et la cohérence entre onglets.

Les chiffres suivants ont été contrôlés et sont exacts :
- les essais CAPSTONE-1, CAPSTONE-2, BLOCKSTONE, FLAGSTONE et CENTERSTONE ;
- les méta-analyses de Dobson, de Muthuri, de Jefferson (Cochrane), de Merckx et de Wu, ainsi que l'étude de Kwong ;
- la définition globale du syndrome de détresse respiratoire aiguë de 2024 et les essais de Diaz Granados, Monto 2000 et Carrat.

## Réserves de l'auteur : traitement en source primaire

| Réserve | Vérification | Résultat |
|---|---|---|
| Cas humains de grippe A(H5N1) selon l'OMS au 31.03.2026 | Tableau OMS en texte intégral (WHO/GIP, données au 31 mars 2026) | 997 cas et 478 décès : chiffres confirmés. J'ai précisé que les détections asymptomatiques sont comprises et que la létalité apparente est biaisée par la détection. |
| Délai de déclaration de 2 heures (page OFSP) | Page OFSP « grippe aviaire H5N1, situation en Suisse » | Confirmé : déclaration téléphonique dans les 2 heures pour une suspicion de nouveau sous-type, avec isolement. L'incubation de 2 à 14 jours est confirmée et a été ajoutée à la partie Situations particulières. L'absence de cas humain en Suisse est confirmée. L'ordonnance du Département fédéral de l'intérieur n'a pas été lue (voir les réserves restantes). |
| Titre d'inhibition de l'hémagglutination de 1:40 | Hobson et collaborateurs, J Hyg 1972 (PubMed 4509641), résumé | La fenêtre `j09-anticorps-ha` a été réécrite : 1032 volontaires ; le titre protégeant la moitié des sujets se situe entre 1:18 et 1:36 ; le seuil de 1:40 dérive de ces travaux. J'ai supprimé la phrase de chantier qui décrivait la fabrication du cours (« non revérifié… »). |
| Rodríguez 2016, procalcitonine | PubMed 26702737, résumé | Confirmé : 972 patients, 20,3 % de co-infections ; un seuil de 0,29 ng/mL donne une valeur prédictive négative de 91,9 %, et de 94 % sans choc. J'ai précisé la cohorte. |
| CENTERSTONE, 7,2 % de résistance | PubMed 40267424, résumé | Confirmé : 9,5 % contre 13,4 % de transmission, 5,8 % contre 7,6 % de transmission symptomatique (différence non significative), 7,2 % de résistance chez les cas index et aucune résistance chez les contacts. J'ai ajouté l'âge des cas index (5 à 64 ans). |
| Vaccin à haute dose (≥ 75 ans, ou ≥ 65 ans avec un facteur de risque) | Plan de vaccination suisse 2026 en texte intégral (PDF, chapitre 3.1.e) et page OFSP sur la grippe | Confirmé. |
| OMS 2024 lue par résumé | Synthèse de Shen 2025 (PMC13277511) ; page de l'OMS inaccessible (captcha) | Les recommandations citées concordent : baloxavir conditionnel pour la forme non grave à risque élevé ; refus de l'oseltamivir et du baloxavir pour la forme non grave à faible risque ; oseltamivir conditionnel pour la forme grave ; refus des corticostéroïdes, des macrolides et des inhibiteurs de mTOR ; règle du test rendu en plus de 24 heures. La force de chaque recommandation reste reprise du résumé officiel en français. |
| Fenêtres sans référence | — | Une référence a été ajoutée aux 15 fenêtres qui n'en avaient pas : ddx-sepsis, ddx-covid, ddx-vrs, pneumonie-virale, sdra, decompensation-pec, myocardite, encephalite, rhabdo, reye, symptomatique, vaccin-efficacite, hygiene, criteres et la synthèse. Contrôle automatique : aucune fenêtre hors Pareto ne reste sans référence. |
| Péramivir et Relenza | Compendium | Le statut « aucune information professionnelle suisse » est conservé pour le péramivir. La commercialisation effective de Relenza n'est pas confirmée ; la formulation factuelle « information professionnelle publiée (octobre 2020) » est conservée. |

## Corrections apportées

### Corrections médicales et de cohérence

1. **Arbitrage des antiviraux : la contradiction entre onglets est levée.** L'onglet Pathologie retenait les CDC 2026, alors que l'onglet Pharmacologie et la fenêtre `j09-oms-risque` retenaient l'OMS 2024, qu'ils présentaient à tort comme la source la plus récente.
   - La source la plus récente est la page des CDC mise à jour le 10.03.2026, lue directement. Elle recommande l'oseltamivir ou le baloxavir, sans préférence générale, chez le patient ambulatoire à risque. Elle préfère l'oseltamivir chez l'hospitalisé et pendant la grossesse, déconseille le baloxavir pendant la grossesse et l'allaitement, et déconseille le baloxavir en monothérapie chez l'immunodéprimé sévère.
   - Ont été harmonisés : le tableau de la partie 9 et les paramètres clés (onglet Pathologie) ; le tableau et l'encadré « À retenir » de P-2 (onglet Pharmacologie) ; les fenêtres `j09-ph-contentieux` (réécrite en arbitrage OMS, IDSA et CDC, avec le texte de l'OMS toujours accessible), `j09-contentieux` et `j09-oms-risque` ; les Pareto « Pharmacologie » et « Diagnostic, urgences et prise en charge ».
2. **Indications suisses du baloxavir** (Compendium, Xofluza). La fenêtre `j09-baloxavir` indiquait une prophylaxie « dès l'âge d'un an », ce qui est erroné. Les indications corrigées sont : traitement dès 3 mois chez la personne en bonne santé, dès 12 ans chez la personne à risque élevé, prophylaxie dès 3 mois. Le lien vers le rapport public de Swissmedic, non vérifié, a été remplacé par l'information professionnelle.
3. **Délai de début de l'oseltamivir.** Le Compendium indique « début au cours des 36 h après l'apparition des symptômes ». La formulation imprécise « le jour des symptômes ou le lendemain » a été corrigée dans le tableau P-3 et dans les fenêtres `j09-ph-delai` et `j09-delai-pec`. Le résumé européen retient les deux premiers jours ; ce point est mentionné.
4. **Oseltamivir en dialyse.** Le tableau rénal indiquait « 30 mg avant la séance puis après chaque séance » et, en dialyse péritonéale, « 30 mg tous les 5 jours » ou « tous les 7 jours ». Ces schémas n'ont pu être contrôlés dans aucune source lue.
   - Le tableau suit désormais le résumé européen des caractéristiques du produit (Agence européenne des médicaments, lu en texte intégral). En hémodialyse : 30 mg après chaque séance en traitement, 30 mg après une séance sur deux en prophylaxie. En dialyse péritonéale continue ambulatoire : 30 mg en dose unique en traitement, 30 mg une fois par semaine en prophylaxie. À 10 mL/min ou moins sans dialyse : non recommandé.
   - Les paliers de clairance (plus de 60, plus de 30 à 60, plus de 10 à 30 mL/min) sont identiques dans les deux sources.
   - J'ai ajouté une lecture du tableau, l'avertissement sur la dialyse péritonéale automatisée et la référence de l'Agence européenne.
5. **Fenêtre `j09-ph-rein`.** L'affirmation invérifiable « information suisse de 2010 : seuil à 30 mL/min » a été remplacée par une mise en garde utile : les tableaux anciens conduisent à surdoser le patient dont la clairance se situe entre 30 et 60 mL/min.
6. **Vaccination OFSP 2026.** Le Plan de vaccination suisse 2026, lu en texte intégral, classe les personnes de 65 ans et plus en **vaccination complémentaire** et non dans la liste des groupes à risque. Le tableau de la partie 10, le tableau P-8 et les fenêtres `j09-risque` et `j09-vaccin-groupes` ont été harmonisés.
   - Libellés exacts du plan : « maison de soins ou établissement pour malades chroniques » ; « asplénie ou dysfonction splénique, hémoglobinopathies comprises » ; personnel paramédical, étudiants et stagiaires compris ; contact régulier ou professionnel avec des volailles domestiques ou des oiseaux sauvages, pour réduire le risque de coinfection et de réassortiment.
7. **Prévention du virus respiratoire syncytial chez l'adulte** (fenêtre `j09-ddx-vrs`). La recommandation de l'OFSP du 01.09.2025 est désormais précisée : toutes les personnes de 75 ans et plus, et les adultes de 60 ans et plus à risque élevé. Cette recommandation est publiée à part du plan 2026.
8. **Vaccin à haute dose.** La phrase « le vaccin n'est indiqué ni avant 65 ans » n'était pas vérifiée au regard de l'âge autorisé. Elle a été remplacée par « l'OFSP ne le recommande pas avant 65 ans ».
9. **Zanamivir.** Les âges pédiatriques non vérifiés (7 et 12 ans) ont été retirés de la monographie destinée à l'adulte.
10. Les CDC sont désormais accordés au pluriel partout (7 occurrences). L'unité est uniformisée en mL/min. Les Pareto ont été complétés : haute dose « ou dès 65 ans avec un facteur de risque », personnes de 65 ans et plus.

### Langue et forme

- Les formules qui décrivaient la fabrication du cours ont été supprimées (« Ce cours poursuit quatre objectifs », « ce cours retient », « le cours commence par », « la fenêtre montre », « du début du cours »).
- Les infinitifs injonctifs ont été convertis en phrases complètes : alertes d'interactions, monographies de l'oseltamivir et du zanamivir, fenêtres sur le paracétamol, les anti-inflammatoires non stéroïdiens, les cations polyvalents et les troubles neuropsychiatriques.
- Une phrase de lecture a été ajoutée aux tableaux qui n'en avaient pas : indications antivirales, comparaison des référentiels, groupes vaccinaux, tableau rénal.
- Les libellés des mots verts du diagnostic différentiel annoncent désormais leur destination entre parenthèses, comme le prévoit le contrat HTML.
- Plusieurs phrases ont été resserrées et rythmées : introduction, épidémiologie du virus A(H5N1), anamnèse, complications, traitement symptomatique.

## Réserves restantes (non bloquantes)

1. **Information professionnelle suisse de Tamiflu pour la dialyse.** Le texte intégral n'est pas accessible : le Compendium ne livre que la synthèse, et la recherche dans Swissmedicinfo n'a pas abouti. Le tableau de dialyse est donc attribué explicitement au résumé européen. L'auteur rapportait un autre schéma pour la dialyse péritonéale, à confronter à l'information suisse.
2. **OMS 2024.** La force exacte de chaque recommandation est reprise du résumé officiel en français et de la synthèse de Shen. Le texte intégral n'a pas été lu (captcha).
3. **Ordonnance sur la déclaration.** Le délai de 2 heures est appuyé sur la page de l'OFSP, non sur le texte de l'ordonnance du Département fédéral de l'intérieur.
4. **Recommandation de la Société suisse d'infectiologie** (saturation inférieure à 92 %, fréquence respiratoire d'au moins 22 et d'au moins 30 par minute). La page est une application JavaScript illisible par l'outil. Les seuils concordent avec le cours injecté J18 — Pneumonies de l'adulte (P-02-Pneumologie).
5. **Relenza.** La disponibilité commerciale en Suisse n'est pas confirmée.
6. **Données non revérifiées, sans contradiction relevée.** Réactogénicité d'Efluelda (41 % et 22,5 %), effets locaux selon l'OFSP (25 % et 5 %), excrétion virale des formes peu symptomatiques (Ip 2017).

## Injection

- `chapters/J09/` contient les 8 fichiers relus. `glossary/j09.py` est repris sans modification : 25 entrées, et le sigle CDC est déjà défini dans `glossary/j40.py`.
- Une entrée a été ajoutée à `chapters.json` après J40 : `{"code": "J09", "covers": ["J09","J10","J11"], "title": "Grippe", "integrated": true}`.
- Une entrée a été ajoutée à `organisation/course_groups.json` : `owner` « S02 », mêmes `covers`, `scope` en une phrase.
- Aucun autre cours n'a été modifié. Aucune opération Git n'a été effectuée.

## Contrôles

| Contrôle | Résultat |
|---|---|
| `python3 -m unittest discover -s tests -p 'test_*.py'` | 176 tests, OK |
| Audit des sigles du cours (`build_medina.audit` après la transformation du build) | `{}` |
| Clés des fenêtres | 144 fenêtres ; aucun `data-k` sans gabarit ; aucune fenêtre orpheline |
| Pareto | 5 fractions calculées (5 à 7 %), aucun îlot introuvable |
| `python3 build_front.py --all-fragments` | 22 fragments construits ; S02 : 3 501 074 octets, compressés à 2 057 020 octets |
| `MEDINA_FRAGMENTS=/mnt/user-data/outputs/fragments python3 tests/audit_fragments.py` | Audit réussi : 22 fragments, JavaScript valide, build reproductible |
| Chromium (playwright, `/opt/pw-browsers/chromium`) : `MEDINA_S02_respiratoire.html#/entry/J09` | Titre « Grippe » ; 4 onglets non vides (pA, pE, pS, pP) ; les 144 fenêtres s'ouvrent avec leur contenu ; aucune erreur JavaScript ni erreur de console |
| `tools/capture_lecon.py … J09` | Réussite : 2 captures (`j09-1-ouverture.png`, `j09-2-explication.png`) dans le dossier temporaire de la session |

Empreintes SHA-256 des fichiers injectés :

```
6da87126045da159e454b495cff1a35fbb05d26a6fd8ca33d97ffb4d60735037 chapters/J09/J09_a.html
6875e1910792a25a9180b55efd4e04a1aa4465b36217a356759fb73967dd259d chapters/J09/J09_b.html
d524485b6d9131ab254c61b5f6b2c2a01bcfee46b571390d00815ae152e21fae chapters/J09/J09_c.html
522cbb3a2fd6a215334d982df9e2245719eb25aec563de33b8858e78bd7f80ce chapters/J09/J09_d.html
6a48d054591fd35120fad12a045031665956c5da4902d9cf0fbee2a9abbeae36 chapters/J09/J09_pop1.html
3f03e85d9ebd09515daf7faa9e60a5ec1334a1a2bd4c6bf5a274f0bbf6e3d11b chapters/J09/J09_pop2.html
93507e80a2bf2a975d12375f1693616ed695f200dd82237366b9ad1efbcdf429 chapters/J09/J09_pop_pa.html
875ff8bd8e4b74b4e273b9f046fb6d3f10accbb4b18f794c98ccba24a8c45d27 chapters/J09/J09_pop_sciences.html
00c1bdb605b732b2ca985585ebeaefb8756a57d35a7f9a14edf6ec873e6bd517 glossary/j09.py
```

Statut : injecté, en attente de l'audit croisé Codex. La revue par IA et les tests techniques ne valent pas validation médicale.
