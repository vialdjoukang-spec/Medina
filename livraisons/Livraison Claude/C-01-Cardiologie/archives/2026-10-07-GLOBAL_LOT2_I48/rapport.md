# Rapport de relecture MEDINA — audit global, lot 2 : I48 — Fibrillation et flutter auriculaires

- Responsable : Claude Code (relecture médicale, didactique et linguistique).
- Mission et cours : `docs/collaboration/CLAUDE_AUDIT_GLOBAL_2026-10-07.md` ; **I48 — Fibrillation et flutter auriculaires**, fragment **C-01-Cardiologie** (S01).
- Branche et commit de départ, SHA complet : `claude/review-medina-global-20261007`, depuis `3636759adb8b74402f98ee8d48c6e8dd49f08a13` (tête de `codex/sciences-cs-fragments-20261007`).
- Commit relu, SHA complet : `3636759adb8b74402f98ee8d48c6e8dd49f08a13`. Les fichiers d'I48 y sont identiques à `7fa06329b3369f54ef0831ae9f6cdf90fce5f605`, commit source du manifeste ; ils contiennent les arbitrages de Codex de `f5c8395`.
- Date de la relecture : 7 octobre 2026 (Europe/Zurich).
- Fichiers examinés : les **huit** fichiers d'I48, lus en entier : `I48_a`, `I48_b`, `I48_c` (onglets Examens et Sciences), `I48_d`, `I48_pop1` à `I48_pop4` (88 fenêtres, dont 15 Pareto).
- Fichiers modifiés : `I48_a`, `I48_b`, `I48_c`, `I48_pop1`, `I48_pop2`, `I48_pop3`, `I48_pop4`. `I48_d` est relu sans modification.
- Mode de remise : copies corrigées sous `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I48/`, manifeste `livraison.json`, branche et pull request.
- État : proposition à injecter ; `check-claude` conforme ; contrôles techniques réussis sur une application temporaire.

## Méthode

Le texte des huit fichiers a été extrait bloc par bloc (titres, paragraphes, listes, lignes de tableau, encadrés, légendes, quiz et fenêtres), puis lu en entier. Chaque affirmation chiffrée ou recommandée a été comparée au texte intégral de l'ESC 2024 lorsque c'était possible. Les autres sources ont été consultées dans PubMed. Les corrections suivent `docs/STYLE_REDACTION.md` : phrases complètes, aucune formule nominale dans les paragraphes explicatifs, et des « À retenir » qui synthétisent sans recopier.

## Sources consultées

| Source | Accès, 07.10.2026 | Passages |
| --- | --- | --- |
| Van Gelder IC, et al. *2024 ESC Guidelines for the management of atrial fibrillation*. Eur Heart J 2024;45:3314–3414. DOI 10.1093/eurheartj/ehae176 | Texte intégral, exemplaire PDF de forening.sls.se (« Downloaded from academic.oup.com »), extrait localement | Tableau 6 et note a (épisodes auriculaires rapides) ; § 3.2 ; § 9.6 et tableau de recommandations sur la FA postopératoire ; texte du dépistage (« single-lead or continuous ECG tracing of >30 s ») ; recommandation « Routine heart rhythm assessment during healthcare contact… ≥65 years » (I C) ; anticoagulation « for at least 4 weeks in all patients after cardioversion » |
| Wijffels MC, Kirchhof CJ, Dorland R, Allessie MA. *Atrial fibrillation begets atrial fibrillation*. Circulation 1995;92:1954–1968. DOI 10.1161/01.cir.92.7.1954 | Résumé PubMed | Raccourcissement de la période réfractaire auriculaire pendant les 24 premières heures |
| Aebersold H, et al. Open Heart 2024;11:e002567. DOI 10.1136/openhrt-2023-002567 | Résumé PubMed | « Swiss-AF cohort, which enrolled 2415 AF patients from 2014 to 2017 » |
| Kahaly GJ, et al. *2018 ETA Guideline for the Management of Graves' Hyperthyroidism*. Eur Thyroid J 2018;7:167–186. DOI 10.1159/000490384 | Résumé PubMed | Dosage des anticorps anti-récepteurs de la TSH recommandé pour le diagnostic |
| Doshi SK, et al. *Left Atrial Appendage Closure or Anticoagulation for Atrial Fibrillation* (CHAMPION-AF). N Engl J Med 2026;394:2083–2094. DOI 10.1056/NEJMoa2517213 | Résumé PubMed | 3 000 patients ; critère composite 5,7 % contre 4,8 % (non-infériorité) ; saignements non procéduraux 10,9 % contre 19,0 % |
| Qassim ZAM, et al. J Clin Med 2026;15:6526. DOI 10.3390/jcm15176526 | Texte intégral PMC | « Ischemic stroke occurred numerically more often after LAAC » dans CHAMPION-AF |

## Observations

### Corrections médicales

| ID | Fichier et repère | Passage actuel | Conclusion et gravité | Correction | Source |
| --- | --- | --- | --- | --- | --- |
| L2-01 | `I48_a`, îlot 5.3, « Forme silencieuse révélée par un AVC » | « Le score CHA₂DS₂-VA passe à 5. » | **Erreur de calcul, majeure pour l'examen.** Avec les seules données du cas (79 ans, AVC), le score vaut 4 : 2 points pour l'âge et 2 pour l'AVC. Le sexe ne compte plus depuis l'ESC 2024. | « Son score CHA₂DS₂-VA vaut au moins 4 : 2 points pour l'âge et 2 pour l'AVC. » | ESC 2024, tableau du score CHA₂DS₂-VA (repris en 10.1 du cours) |
| L2-02 | `I48_pop1`, `data-pop="i48-infraclin"` (réserve **R08** de la PR #8) | « historiquement : fréquence auriculaire > 175/min pendant au moins 5 minutes » | **Définition périmée**, mineure. | « selon l'ESC 2024 : fréquence auriculaire d'au moins 170/min, durant généralement plus de 5 minutes ; chaque épisode est inspecté visuellement, car certains sont des artéfacts » | ESC 2024, tableau 6, note a |
| L2-03 | `I48_pop1`, `data-pop="i48-colaus"`, rubrique Swiss-AF | « recrutement clos en 2020 » | **Erreur factuelle**, mineure. | « recrutement de 2014 à 2017 » | Aebersold 2024 |
| L2-04 | `I48_a`, îlot 3.2 | « Après quelques jours d'arythmie, la période réfractaire se raccourcit » | **Imprécision**, mineure : le raccourcissement survient dès les 24 premières heures. | « Dès les premières 24 heures d'arythmie… » | Wijffels 1995 |
| L2-05 | `I48_b`, îlot 7.4 ; `I48_pop2`, `i48-depist` ; `I48_pop4`, `pareto-i48-diag` (réserve **R11**) | « dépistage opportuniste … (ESC 2020, repris en 2024) » ; « (ESC 2024, classe IIa) » appliqué aux deux dépistages | **Classe erronée**, mineure : l'évaluation de routine du rythme dès 65 ans est de classe I, niveau C ; seul le dépistage populationnel prolongé est de classe IIa, niveau B. | Libellé ESC 2024 et classes distinctes dans les trois passages. | ESC 2024, recommandation « Routine heart rhythm assessment… » (I C) |
| L2-06 | `I48_a`, îlot 5.3, « Forme trompeuse » | « TSH effondrée : maladie de Basedow. » | **Raccourci diagnostique**, mineur : une TSH basse prouve l'hyperthyroïdie, pas sa cause. | « TSH effondrée et anticorps anti-récepteurs de la TSH positifs : maladie de Basedow. » | ETA 2018 |
| L2-07 | `I48_c`, Biochimie, encadré « Corrélation biochimie → examens → thérapeutique » | « La demi-vie courte des antivitamines K sur le facteur VII » | **Erreur de formulation** qui inverse le mécanisme : c'est le facteur VII qui a une demi-vie courte. | « La demi-vie courte du facteur VII explique… » | Paragraphe précédent du même fichier |
| L2-08 | `I48_pop3`, `i48-inr` | « Il explore les facteurs II, VII et X. » | **Imprécision**, mineure : le temps de prothrombine explore aussi le facteur V et le fibrinogène. | « Il explore notamment les facteurs vitamine K-dépendants II, VII et X. » | Physiologie de la coagulation (aucun fait nouveau) |
| L2-09 | `I48_pop4`, `pareto-i48-anticoag` ; `I48_b`, sources | « CHAMPION-AF 2026 : moins de saignements, plus d'AVC ischémiques » ; « Essai CHAMPION-AF, NEJM 2026 » | **Synthèse incomplète** et référence imprécise. | Pareto : « non-infériorité sur le critère composite, moins de saignements non procéduraux, AVC ischémiques numériquement plus fréquents ». Référence complète : NEJM 2026;394:2083–2094, doi:10.1056/nejmoa2517213. | Doshi 2026 ; Qassim 2026 |

### Vérifications sans correction

| ID | Repère | Conclusion |
| --- | --- | --- |
| L2-10 | Durée du tracé : encadré `I48_c` 2A, `i48-depist`, `pareto-i48-ecg` | **Conforme à l'arbitrage de Codex** (`f5c8395`). Le texte de l'ESC 2024 mentionne bien, après une alerte, « a single-lead or continuous ECG tracing of >30 s or 12-lead ECG showing AF analysed by a physician ». Le tableau 31 ne fixe pas de durée. La conclusion R01/R02 du rapport du chat est donc à nuancer, comme Codex l'a fait. |
| L2-11 | FA postopératoire : `I48_b` îlot 14, `i48-poaf`, `pareto-i48-suivi` | **Conforme.** ESC 2024, § 9.6 : anticoagulation au long cours « should be considered » après chirurgie cardiaque **et** non cardiaque, classe IIa, niveau B. La mention IIb date de 2020. |
| L2-12 | Anticoagulation après cardioversion : `I48_b` 12.1, `i48-24h` | **Conforme.** ESC 2024 : au moins 4 semaines chez tous les patients, même si le CHA₂DS₂-VA vaut 0. |
| L2-13 | Cas récapitulatif `I48_b` ; quiz 2 `I48_c` ; exemple `i48-cg` | **Calculs conformes** : CHA₂DS₂-VA 3, Cockcroft-Gault ≈ 35 mL/min, apixaban 5 mg × 2 ; quiz ≈ 28 mL/min, 2,5 mg × 2 ; exemple ≈ 29 mL/min, CKD-EPI ≈ 45. |
| L2-14 | Doses : tableaux AOD (`I48_b` 10.3, `I48_d`), freinateurs et antiarythmiques (`I48_d`), oubli, relais, interruption périopératoire (`i48-periop`) | **Conformes** à l'EHRA 2021 et aux tableaux ESC 2020/2024 recoupés. |
| L2-15 | `I48_d` en entier | **Relu sans modification.** Les listes nominales de l'encadré « Interactions dangereuses » et des « Médicaments à éviter » sont des aide-mémoire ; leur forme est acceptable. |

### Corrections didactiques et linguistiques

| ID | Repère | Écart | Correction |
| --- | --- | --- | --- |
| L2-16 | `I48_a`, îlot 0 | Datation périssable : « Aucune nouvelle recommandation ESC … n'a paru en août 2026 : celle de 2024 reste en vigueur en septembre 2026. » | Phrase supprimée ; la date de consultation des sources reste en fin d'onglet. |
| L2-17 | `I48_pop3`, `i48-24h` | « la recommandation en vigueur en 2026 » | « l'ESC 2024 retient 24 heures ». |
| L2-18 | `I48_a`, îlot 5.2 | Répétition : la liste dit « un patient sur trois environ », puis le paragraphe répète « Environ un tiers des patients ne ressent rien ». | Phrase répétée supprimée. |
| L2-19 | `I48_a`, îlots 3.3, 3.4 et 6.1 | Phrase nominale (« D'abord, la perte de la contraction auriculaire, qui… ») ; sujet erroné (« la fréquence … peut dégénérer en fibrillation ventriculaire ») ; liste nominale de l'examen. | Phrases complètes ; boutons de fenêtre conservés. |
| L2-20 | `I48_b`, îlot 8 | Métadiscours : « L'ordre clinique diffère de l'ordre pédagogique » ; redondance « se traite d'abord par le traitement du sepsis ». | « Au lit du patient, la stabilité s'évalue avant la recherche de la cause » ; « le traitement du sepsis et le remplissage passent avant toute cardioversion ». |
| L2-21 | `I48_b`, îlot 8.2 (six complications) | Fragments nominaux et infinitifs (« Déficit brutal… Filière AVC immédiate », « Évaluer la gravité, arrêter… », « D'où l'association… »). | Six paragraphes réécrits en phrases complètes, contenu inchangé. |
| L2-22 | `I48_b`, îlots 10, 11.2 et 12.1 | « puis-je corriger » ; fragments nominaux des quatre choix de freinateurs et des deux situations de cardioversion. | Formulations impersonnelles et phrases complètes. |
| L2-23 | `I48_b`, îlot 13.3 | Un seul paragraphe de 14 phrases mêle pronostic, éducation, réadaptation et conduite automobile. | Scindé en deux paragraphes : pronostic et éducation, puis aptitude à la conduite. |
| L2-24 | `I48_b`, îlot 14 (huit situations) | Fragments nominaux ; répétition intégrale du schéma de trithérapie déjà détaillé en 10.3. | Phrases complètes ; renvoi au schéma de 10.3 au lieu de sa copie, en gardant l'information propre (clopidogrel de choix, pas de prasugrel ni de ticagrélor). |
| L2-25 | `I48_c`, cinq blocs « Interprétation guidée » | Gabarit cloné : 3 introductions « La figure relie… Elle montre les étapes utiles pour comprendre… » (dont une agrammaticale) ; 3 légendes génériques ; 3 paragraphes qui recopient mot pour mot les encadrés « Science → clinique » et « Science → examen » ; 5 « À retenir » qui recopient la dernière phrase du développement. | Introductions qui décrivent les cases de chaque figure ; légendes spécifiques ; paragraphes dupliqués supprimés ; « À retenir » de synthèse. La phrase « La décision combine les facteurs de risque et le contexte, séparément de la durée d'un tracé » devient : la décision d'anticoaguler une FA clinique repose sur les facteurs de risque, quelle que soit la forme temporelle (cohérent avec `i48-types`). |
| L2-26 | `I48_c`, Anatomie, Interprétation guidée | « un circuit autour de l'anneau tricuspide et l'isthme » | « tourne autour de l'anneau tricuspide et passe par l'isthme cavotricuspide ». |
| L2-27 | `I48_pop2`, `i48-preexc`, « Piège » | Logique inversée (« n'est pas … tant que la morphologie varie »). | La phrase dit désormais qu'une tachycardie irrégulière à QRS larges, polymorphe et rapide, évoque une FA pré-excitée. |

## Constat transversal à traiter dans un lot dédié

Le gabarit corrigé en L2-25 existe dans tous les cours enrichis le 7 octobre. Mesure sur `3636759` :

- **93** blocs « Interprétation guidée » ;
- **92** « À retenir » identiques à une phrase du développement ;
- **31** paragraphes après la figure qui recopient les encadrés « Science → » ;
- **31** introductions « Elle montre les étapes utiles pour comprendre… », dans 16 cours ;
- **40** légendes « Les flèches relient les mécanismes décrits dans le texte ».

Je propose d'en faire le lot 3, cours par cours, avec la même méthode que pour I48.

## Changements et remise

Les 58 remplacements portent sur 7 fichiers. Le glossaire, l'interface, le moteur et le build ne sont pas modifiés, et aucune abréviation nouvelle n'est introduite. Les copies corrigées et `livraison.json` se trouvent dans `livraisons/Livraison Claude/C-01-Cardiologie/`. Le manifeste ne garde que les fichiers d'I48 effectivement modifiés, avec l'empreinte de l'original (`sha256`) et celle de la proposition (`proposed_sha256`). Les sources canoniques `chapters/I48/` ne sont pas modifiées sur la branche : l'injection relève de `apply-claude`.

## Contrôles réellement exécutés

Les contrôles ont été exécutés après copie temporaire des sept fichiers corrigés dans `chapters/I48/`. Les sources canoniques ont ensuite été restaurées par `git checkout -- chapters/I48`.

| Commande exacte | Résultat | Détail |
| --- | --- | --- |
| `python3 test_v7.py --static I48 I70 I71 I80` | Réussi | I48 : 25 494 mots, 88 fenêtres, 4 quiz, 15 Pareto ; OK. Un premier passage avait signalé « SK » et un DOI en majuscules dans la nouvelle référence : la référence a été réécrite. |
| `MEDINA_OUT=$PWD/dist python3 build_front.py --all-fragments` | Réussi | 22 fragments |
| `python3 tests/audit_fragments.py` | Réussi | JavaScript valide, build reproductible |
| `python3 tests/audit_sciences.py --out /tmp/medina-science-content.json` | Réussi | `errors: []` |
| `MEDINA_CHROMIUM_PATH=…/headless_shell MEDINA_QA_OUT=/tmp/medina-sciences-cs node tests/verify_sciences_cs.cjs` | Réussi | 583 contrôles, 0 erreur |
| `MEDINA_CHROMIUM_PATH=…/headless_shell MEDINA_QA_OUT=/tmp/medina-s01 node tests/verify_s01_browser.cjs` | Réussi | 71 contrôles, 5 captures, 0 erreur |
| `python3 tools/livraison.py check-claude "livraisons/Livraison Claude/C-01-Cardiologie"` | Conforme | 7 fichiers vérifiés et modifiés ; aucune injection |

Un test technique réussi ne valide pas la médecine.

## Réserves et limites

- **CHAMPION-AF, chiffres d'AVC ischémiques.** Le cours cite 3,2 % contre 2,0 % à trois ans (`I48_b` 10.4, `i48-laao`). Le résumé de l'essai ne donne pas ces chiffres ; une revue de 2026 confirme seulement un excès numérique. Ils restent dans le texte en réserve, à vérifier sur le texte intégral du NEJM.
- **Réadaptation cardiaque.** La « recommandation ESC 2026 sur la réadaptation cardiaque » (`I48_b` 13.3) n'a pas été vérifiée.
- **Aptitude à la conduite.** Les délais attribués aux directives SSC/SSML 2024 (`I48_b` 13.3, `i48-s-synco`) n'ont pas été vérifiés sur le document suisse.
- **Données suisses.** Les chiffres CoLaus (0,9 %, 3,1 %, 4,7 %) et l'autorisation du vernakalant en Suisse depuis 2011 (`I48_d`) n'ont pas été vérifiés.
- **Rotors.** « entretenus en partie par des rotors localisés » (`I48_c`, Électrophysiologie) présente comme établi un mécanisme débattu. L'ESC 2024 ne traite pas des rotors ; aucune source primaire n'a été lue, le texte reste donc inchangé.
- **Grossesse.** La classe IIa du flécaïnide associé au bêtabloquant (`i48-grossesse`) n'a pas été vérifiée dans l'ESC 2025 sur la grossesse.
- **Objectifs.** La section « Objectifs » (« le médecin assistant sait… ») est conservée en attendant la décision du propriétaire sur ces sections.

Cette relecture couvre I48 en entier, mais elle ne certifie ni la complétude CIM-11 du fragment, ni les autres cours de C-01-Cardiologie. Aucun statut `DONE_*` n'est modifié.
