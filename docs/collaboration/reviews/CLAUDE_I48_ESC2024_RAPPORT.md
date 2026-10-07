# Rapport de relecture MEDINA — I48, confirmation ECG de la FA selon l'ESC 2024

- Responsable : Claude (relecture médicale, sources et clarté).
- Mission et cours : `docs/collaboration/CLAUDE_I48_ESC2024_2026-10-07.md` ; I48, fibrillation et flutter auriculaires.
- Branche et commit de départ, SHA complet : branche locale `claude/review-i48-local`, créée depuis `c3770739b58c96120c180a4ae0c68d00dde70a51`.
- Commit relu, SHA complet : `c3770739b58c96120c180a4ae0c68d00dde70a51`.
- Date de la relecture : 7 octobre 2026 (Europe/Zurich).
- Fichiers examinés : `chapters/I48/I48_a.html`, `I48_c.html` (onglet Examens `pE` seulement), `I48_pop2.html`, `I48_pop4.html` ; `I48_pop1.html` lu pour cohérence, non modifié.
- Fichiers modifiés : `I48_a.html`, `I48_c.html`, `I48_pop2.html`, `I48_pop4.html`.
- Mode de remise : rapport et patch `CLAUDE_I48_ESC2024.patch` (aucun identifiant GitHub).
- État : proposition à intégrer ; contrôles techniques réussis sur la branche locale.

## Source primaire lue

Van Gelder IC, Rienstra M, Bunting KV, et al. *2024 ESC Guidelines for the management of atrial fibrillation developed in collaboration with EACTS*. European Heart Journal 2024;45(36):3314–3414. DOI 10.1093/eurheartj/ehae176. Publication du 30 août 2024.

Deux accès au **texte intégral** ont été utilisés le 7 octobre 2026. Le premier est la version HTML de l'éditeur (academic.oup.com/eurheartj/article/45/36/3314/7738779) : § 3.1, § 3.2 et tableau 6 lus intégralement ; les tableaux de recommandations y sont des images non lisibles. Le second est un exemplaire PDF de la même publication (forening.sls.se/media/kfyncecr/2024-esc-guidelines.pdf), estampillé « Downloaded from academic.oup.com », avec le même DOI et la même pagination du journal. Les pages 3314 à 3339 y ont été lues. L'exemplaire indiqué par la mission (swiss-ablation.com) n'était pas accessible depuis mon outil de lecture.

Passages déterminants :

| Repère ESC 2024 | Page | Contenu vérifié | Classe, niveau |
| --- | --- | --- | --- |
| Recommandation, tableau 1 | 3328 | Une confirmation par ECG (12 dérivations, plusieurs ou une seule dérivation) est recommandée pour établir le diagnostic de FA clinique et commencer la stratification du risque et le traitement. **Aucune durée n'est fixée.** | I A |
| § 3.2 | 3327–3328 | L'ECG standard mesure 10 s ; la confirmation vaut lorsque la FA persiste sur tout le tracé standard. Pour les appareils à une ou plusieurs dérivations, 30 s ou plus constituent une opinion consensuelle, avec des preuves limitées. Les objets sans ECG (photopléthysmographie) sont exclus. | Texte |
| Tableau 6, « Clinical AF » | 3327 | La durée minimale en ECG ambulatoire n'est pas établie et dépend du contexte. Des périodes de 30 s ou plus peuvent signaler un problème clinique et conduire à prolonger la surveillance ou à stratifier le risque thromboembolique. Définitions éditées **par consensus**. | Consensus |
| Tableau 6, « Device-detected subclinical AF » | 3327 | Épisodes asymptomatiques sur dispositifs de surveillance continue, implantés **ou portés grand public** ; confirmation par un professionnel compétent sur électrogramme intracardiaque ou rythme enregistré en ECG. Note a : épisodes auriculaires rapides ≥ 170/min, généralement > 5 min. | Texte |
| Tableau 4 (révisées), § 3.2 | 3326 | La recommandation 2020 (12 dérivations ou une dérivation **≥ 30 s**, I B) est remplacée par la recommandation 2024 sans durée (I A). | — |
| Tableau 3 (nouvelles), § 10.3 | 3324 | La relecture d'un ECG (12 dérivations, une ou plusieurs dérivations) par un médecin est recommandée pour poser un diagnostic certain et commencer la prise en charge. **Aucune durée.** | I B |
| Tableau 3 (nouvelles), § 10.3 | 3324 | Dépistage populationnel prolongé par ECG à envisager dès 75 ans, ou dès 65 ans avec d'autres facteurs du CHA₂DS₂-VA. | IIa B |

## Observations

| ID | Fichier et repère stable | Passage actuel ou résumé précis | Conclusion et gravité | Correction proposée | Source | Consultation et accès |
| --- | --- | --- | --- | --- | --- | --- |
| R01 | `I48_c.html`, onglet `pE`, section 2A, `div.key` « Durée du tracé : interprétation » | « Après une alerte de dépistage, l'ESC propose une confirmation par ECG à 12 dérivations ou par un tracé mono- ou multidérivation de plus de 30 secondes » | **Erreur majeure.** Le seuil de 30 s appartient à la recommandation de 2020. La recommandation 2024 de dépistage ne fixe aucune durée. « Plus de 30 » transforme en outre « ≥ 30 » en « > 30 ». | Relecture médicale d'un tracé ECG (12 dérivations, une ou plusieurs) pour un diagnostic certain ; mention explicite que la recommandation 2024 ne fixe aucune durée et que le seuil venait de 2020. Ajout de la condition « FA sur tout le tracé » pour l'ECG de 10 s. | EHJ 2024, tableau 3 p. 3324 ; tableau 4 p. 3326 ; § 3.2 p. 3327–3328 | 07.10.2026, texte intégral |
| R02 | `I48_pop2.html`, `data-pop="i48-depist"`, rubrique « ECG à une dérivation » | « l'ESC recommande une confirmation […] de plus de 30 secondes, relu par un médecin » | **Erreur majeure**, identique à R01, aggravée par le verbe « recommande » qui attribue le seuil à une recommandation 2024. | Même correction que R01 ; le repère de 30 s est présenté comme un consensus issu de 2020. | Idem R01 | 07.10.2026, texte intégral |
| R03 | `I48_a.html`, îlot du diagnostic, paragraphe « Le diagnostic exige une documentation électrocardiographique… » | « peut documenter une FA typique » ; « Un épisode de cette durée justifie une évaluation » | **Ambiguïté mineure.** L'ESC exige que la FA persiste sur tout l'ECG standard ; la condition manquait. La phrase sur 30 s simplifiait le tableau 6. La mention « ne décide pas seul une anticoagulation » est une **interprétation du relecteur**, cohérente avec le tableau 1 (la confirmation ouvre la stratification du risque). | Condition de persistance sur tout le tracé ; place des appareils à une ou plusieurs dérivations ; reformulation fidèle du tableau 6 ; l'alerte optique « ne documente pas le rythme ». | Tableau 1 p. 3328 ; tableau 6 p. 3327 ; § 3.2 | 07.10.2026, texte intégral |
| R04 | `I48_c.html`, onglet `pE`, section 2B, tableau des enregistrements, ligne « Montre ou bague connectée » | « Faux positifs ; confirmation par ECG obligatoire » | **Ambiguïté mineure.** La ligne réunit photopléthysmographie et ECG à une dérivation. Or le tracé ECG d'une montre, relu par un médecin, peut lui-même confirmer le diagnostic. | Distinguer l'alerte optique (ECG obligatoire) du tracé ECG de la montre (diagnostic possible après relecture médicale). | Tableau 1 p. 3328 ; § 3.2 | 07.10.2026, texte intégral |
| R05 | `I48_pop2.html`, `data-pop="i48-ecg-fa"`, étape « 5. Diagnostic » | « Un ECG standard de 10 secondes peut documenter une FA » | **Ambiguïté mineure**, même nature que R03. | Condition de persistance sur tout le tracé ; durée ambulatoire « non établie » ; repère « 30 s ou plus ». | § 3.2 ; tableau 6 | 07.10.2026, texte intégral |
| R06 | `I48_pop4.html`, synthèses Pareto (liste « FA : activation auriculaire désorganisée… » et liste « La référence du diagnostic… ») | « Un ECG standard peut suffire » ; « Infraclinique = détectée par dispositif, sans ECG de surface » | **Ambiguïtés mineures** : condition de persistance absente ; la définition de l'infraclinique omettait le caractère asymptomatique et la surveillance continue. | Rappels alignés sur R01 à R05 ; mention que la recommandation de dépistage 2024 ne fixe aucune durée. | Tableau 6 p. 3327 ; tableau 3 p. 3324 | 07.10.2026, texte intégral |
| R07 | `I48_a.html`, paragraphe « La fibrillation auriculaire clinique… », bouton `data-k="i48-infraclin"` | Infraclinique « enregistrée par un stimulateur, un défibrillateur ou un moniteur implantable » ; vérification sur l'électrogramme intracardiaque seulement | **Incomplétude mineure.** L'ESC 2024 inclut les appareils portés grand public et admet la vérification sur un rythme enregistré en ECG. | Épisodes asymptomatiques, dispositif de surveillance continue le plus souvent implanté, appareils portés inclus ; vérification par un professionnel compétent sur électrogramme ou tracé ECG. | Tableau 6 p. 3327 | 07.10.2026, texte intégral |
| R08 | `I48_pop1.html`, `data-pop="i48-infraclin"` (**hors périmètre**) | « historiquement : fréquence auriculaire > 175/min pendant au moins 5 minutes » | **Conforme comme rappel historique**, mais la définition 2024 manque. **Non modifié** ; transmis à Codex. | Ajouter la définition 2024 : ≥ 170/min, généralement > 5 min, inspection visuelle obligatoire. | Tableau 6, note a, p. 3327 | 07.10.2026, texte intégral |
| R09 | `I48_pop2.html`, `i48-depist`, « Photopléthysmographie » ; `I48_a.html`, alerte de montre | Elle alerte mais ne pose pas le diagnostic ; un ECG est nécessaire | **Conforme.** | Aucune. | § 3.2 p. 3328 | 07.10.2026, texte intégral |
| R10 | `I48_pop2.html`, `i48-depist`, « Recommandations » ; `I48_pop4.html` | Dépistage populationnel prolongé dès 75 ans, ou 65 ans avec facteurs, classe IIa | **Conforme** pour la classe IIa B. | Aucune. | Tableau 3 p. 3324 | 07.10.2026, texte intégral |
| R11 | `I48_pop2.html` et `I48_pop4.html`, « Dépistage opportuniste dès 65 ans » | Mention sans classe | **Non vérifié en texte intégral.** La formulation 2024 (« évaluation de routine du rythme lors de tout contact de soins dès 65 ans ») apparaît dans un extrait du tableau de recommandations 31 (p. 3374), que je n'ai pas lu en entier. | Aucune ; vérification de la classe à faire sur la p. 3374. | Tableau 31 p. 3374 | 07.10.2026, extrait seulement |

### Mécanisme et portée des corrections

L'erreur centrale (R01, R02) a une conséquence pédagogique directe. Un candidat qui retient « l'ESC 2024 exige plus de 30 secondes » confond deux générations de recommandations. Il risque aussi de rejeter un tracé valide de 10 secondes. La version corrigée distingue désormais trois niveaux. La **recommandation** exige une confirmation ECG relue (I A au diagnostic, I B au dépistage), sans durée. Le **consensus** retient 30 secondes ou plus pour les appareils ambulatoires, avec des preuves limitées. L'**interprétation** rappelle qu'un épisode bref déclenche une surveillance ou une stratification du risque, et non une anticoagulation automatique.

## Changements et remise

Huit passages ont été réécrits dans quatre fichiers, en phrases courtes et complètes selon `docs/STYLE_REDACTION.md`. Aucune nouvelle abréviation n'a été introduite ; le glossaire est inchangé. L'onglet Sciences (`pS`) de `I48_c.html` n'a pas été touché. Le patch se nomme `CLAUDE_I48_ESC2024.patch` (empreinte SHA-256 commençant par `16a4694429406327`). Les observations R08 et R11 restent sans modification, car l'une sort du périmètre et l'autre n'a pas été vérifiée en texte intégral.

## Contrôles réellement exécutés

| Commande exacte | Résultat | Journal ou détail |
| --- | --- | --- |
| `python3 test_v7.py --static I48` (avant correction) | Réussi | 24 105 mots, 88 fenêtres, 4 quiz, 15 Pareto |
| `python3 test_v7.py --static I48` (après correction) | Réussi | 24 329 mots, 88 fenêtres, 4 quiz, 15 Pareto ; aucune abréviation non couverte |
| `MEDINA_OUT=$PWD/dist python3 build_front.py --all-fragments` | Réussi | 22 fragments construits |
| `python3 tests/audit_fragments.py` | Réussi | « audit réussi : 22 fragments, JavaScript valide, build reproductible » |
| `git apply --check CLAUDE_I48_ESC2024.patch` sur `c3770739…` | Réussi | — |
| `git apply --check CLAUDE_I48_ESC2024.patch` sur `origin/codex/sciences-cs-fragments-20261007` (`ed8d3ff`) | Réussi | Aucun conflit avec les enrichissements ultérieurs |
| `node tests/verify_s01_browser.cjs` | Non exécuté | Contrôle navigateur laissé à Codex lors de l'intégration |

**Contrôles exécutés lors de l'intégration** par Claude Code, le 7 octobre 2026, sur `e7cbc52` avec les deux relectures appliquées. Le Chromium utilisé est celui préinstallé dans l'environnement (`chromium_headless_shell-1194`).

| Commande exacte | Résultat | Journal ou détail |
| --- | --- | --- |
| `MEDINA_OUT=$PWD/dist python3 build_front.py --all-fragments` | Réussi | 22 fragments construits |
| `python3 tests/audit_fragments.py` | Réussi | « audit réussi : 22 fragments, JavaScript valide, build reproductible » |
| `python3 tests/audit_sciences.py --out /tmp/medina-science-content.json` | Réussi | `errors: []` |
| `python3 test_v7.py --static I48 I70 I71 I80` | Réussi | I48 : 25 242 mots, 88 fenêtres, 4 quiz, 15 Pareto ; OK |
| `MEDINA_CHROMIUM_PATH=/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell MEDINA_QA_OUT=/tmp/medina-sciences-cs node tests/verify_sciences_cs.cjs` | **Réussi** | `{"result": "passed", "checks": 569, "errors": []}` |
| `node tests/verify_s01_browser.cjs` | Non exécuté | Hors liste des contrôles demandés pour cette intégration |

Un test technique réussi ne valide pas la médecine.

## Limites de la conclusion

Cette relecture conclut sur la confirmation ECG de la FA dans les passages cités. Elle ne certifie ni l'anticoagulation, ni les posologies, ni la surveillance après accident vasculaire cérébral, ni le cours I48 entier. Le tableau de recommandations 31 (p. 3374) n'a pas été lu en entier. Les statuts d'audit, `DONE_COURSES` et `DONE_SYS` ne sont pas modifiés.
