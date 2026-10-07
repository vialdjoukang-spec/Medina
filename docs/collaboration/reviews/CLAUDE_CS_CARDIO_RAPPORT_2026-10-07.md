# Rapport de relecture MEDINA — Sémiologie CS, examen cardiovasculaire

- Responsable : Claude (relecture des repères et des manœuvres).
- Mission et cours : ligne « Relecture des repères et manœuvres de CS » du journal `MEDINA_S01_2026-10-07.md` ; module S01 Sémiologie CS.
- Branche et commit de départ, SHA complet : branche locale `claude/review-cs-local`, créée depuis `bb134857e12245f46b4f329c1334ebd57251fcff`.
- Commit relu, SHA complet : `bb134857e12245f46b4f329c1334ebd57251fcff`.
- Date de la relecture : 7 octobre 2026 (Europe/Zurich).
- Fichiers examinés : `modules/cardiovascular_cs.html` (dix étapes, cas, liste de contrôle) ; `modules/cardiovascular_cs.js` (textes des repères des quatre modèles 3D).
- Fichiers modifiés : les deux mêmes. `cardiovascular_cs.css` et la géométrie 3D ne sont pas touchés.
- Mode de remise : rapport et patch `CLAUDE_CS_CARDIO_2026-10-07.patch`.
- État : proposition à intégrer ; contrôles statiques réussis ; contrôle navigateur non exécuté.

## État de la mission précédente

Le patch I48 (`CLAUDE_I48_ESC2024.patch`) n'est pas encore intégré au commit `bb13485`. Il s'applique toujours sans conflit sur ce commit (`git apply --check` réussi). La ligne « Relecture médicale de la confirmation ECG de I48 » peut passer à « rapport remis ; intégration en attente ».

## Sources lues

| Source | Passage | Accès, 07.10.2026 |
| --- | --- | --- |
| Chua Chiaco JMS, Parikh NI, Fergusson DJ. *The jugular venous pressure revisited*. Cleve Clin J Med 2013;80(10):638–644. DOI 10.3949/ccjm.80a.13039 | Référence de mesure ; critères de Wood (onde veineuse contre pouls artériel) ; reflux abdominojugulaire | Texte intégral, page 2 de l'article (mdedge.com) |
| Stanford Medicine 25, *Approach to the Exam for Diastolic Murmurs* (source déjà citée par le module) | Position de recherche de la fuite aortique | Extrait de la page |
| Walker HK, Hall WD, Hurst JW. *Clinical Methods*, 3ᵉ éd., chap. 27 « Diastolic Murmurs » (NCBI Bookshelf NBK346) | Apnée expiratoire relâchée ; diaphragme appuyé ; cloche à l'apex pour les bruits graves | Extrait du PDF |
| BJGP Open 2025;9(4):BJGPO.2024.0246, introduction ; J Clin Hypertens, tableau de synthèse des recommandations (doi 10.1111/jch.13978) | Mesure aux deux bras puis usage du bras le plus élevé ; seuils de différence divergents entre sociétés | Extraits |

## Observations

| ID | Fichier et repère stable | Passage actuel ou résumé | Conclusion et gravité | Correction proposée | Source |
| --- | --- | --- | --- | --- | --- |
| C01 | HTML, étape 5 « Observer la pression veineuse jugulaire » | Onde « non palpable », variable, « plusieurs oscillations » | **Lacune mineure.** Le critère le plus discriminant manquait : l'onde veineuse s'efface sous une légère pression à la base du cou. | Ajout : deux sommets par cycle, baisse inspiratoire, effacement à la pression ; contraste avec le pouls carotidien. | CCJM 2013, critères de Wood |
| C02 | HTML, étape 5, convention des 5 cm | « avec des limites anatomiques » ; aucun seuil d'anomalie | **Lacune mineure.** L'étudiant ne savait ni quand la hauteur est anormale ni dans quel sens la convention se trompe. | Ajout : la distance angle sternal–oreillette droite dépasse souvent 5 cm (≈ 8 cm à 30°, ≈ 10 cm à 45°), donc sous-estimation ; hauteur > ≈ 3 cm au-dessus de l'angle sternal = élevée. | CCJM 2013, « Which reference point to use? » |
| C03 | HTML, étape 5, variation respiratoire | Absence de diminution ou augmentation inspiratoire | **Conforme**, mais le signe n'était pas nommé. | Ajout : « signe de Kussmaul ». | CCJM 2013 |
| C04 | HTML, étape 8 « Poumons et abdomen » | « augmentation soutenue » pendant une pression abdominale | **Imprécision mineure** : critère temporel absent. | Élévation qui persiste plus de 10 s sous pression ferme, puis chute au relâchement. | CCJM 2013, « Abdominojugular reflex » |
| C05 | HTML, étape 7 « Utiliser la position… » ; JS, repère du foyer mitral | « phénomènes graves » | **Ambiguïté** : en français, « grave » se lit aussi « sévère ». Le texte parlait de basse fréquence. | « bruits graves, de basse fréquence » : troisième bruit, roulement de rétrécissement mitral, cloche légère. | Clinical Methods, chap. 27 |
| C06 | HTML, étape 7 ; JS, zone d'Erb | Fuite aortique recherchée « en expiration confortable » | **Imprécision mineure** de la manœuvre. | Après une expiration complète, respiration brièvement suspendue ; diaphragme appuyé fermement au bord sternal gauche. | Stanford Medicine 25 ; Clinical Methods, chap. 27 |
| C07 | HTML, étape 3 « Pression artérielle » | Mesure aux deux bras, sans conséquence pratique | **Lacune mineure.** | Ajout : les mesures suivantes utilisent le bras le plus élevé. **Aucun seuil chiffré ajouté**, car les sociétés divergent (10, 15 ou 20 mmHg). | BJGP Open 2025 ; J Clin Hypertens |
| C08 | HTML, étape 6 « Explorer le bord sternal » | « base de la main » | **Terminologie** : le terme d'usage est « talon de la main ». | Remplacement du terme. | Usage terminologique |
| C09 | HTML et JS, foyers, repères osseux, B1/B2, dédoublement, B4 et FA, échelle de Levine, Homans, sites de pouls, orthostatisme | — | **Conformes.** Le module distingue bien foyer d'écoute et position valvulaire, constatation et interprétation. | Aucune. | Concordance avec les sources ci-dessus |
| C11 | HTML, étape 2 « Priorité clinique » (écart signalé par Codex, ligne 10) | « une syncope persistante » | **Erreur terminologique** : une syncope est par définition transitoire. | « une syncope récente, surtout à l'effort ou précédée de palpitations, une altération persistante de la conscience ». | Définition de la syncope ; action clinique inchangée (évaluation urgente) |
| C12 | HTML, étape 5 « À retenir » (écart signalé par Codex, ligne 16) | « Une estimation jugulaire renseigne les pressions droites » | **Imprécision** : la jugulaire estime la pression auriculaire droite et, lorsqu'elle s'en écarte, la sous-estime. | Reformulation avec ce sens d'erreur. | CCJM 2013, « Key points » |
| C10 | HTML, étapes 4 et 8 (**non modifié**) | Pas de palpation de l'aorte abdominale, d'auscultation carotidienne ou fémorale, ni de comparaison radio-fémorale | **Lacune de complétude** pour un examen dit « complet ». Non corrigée, car je n'ai pas lu de source primaire pour ces manœuvres. | À ajouter par Codex ou dans une prochaine mission, avec source. | — |

### Principe des corrections

La sémiologie n'est utile que si l'étudiant sait **ce qui distingue** un signe de son imitateur et **à partir de quand** il devient anormal. Le module expliquait bien le mécanisme ; il manquait souvent le critère discriminant (C01) ou le seuil (C02, C04). Les corrections ajoutent ces deux éléments sans transformer un repère d'enseignement en certitude.

## Changements et remise

Neuf passages HTML et deux textes de repères 3D ont été modifiés, en phrases complètes. Aucune abréviation nouvelle. Patch : `CLAUDE_CS_CARDIO_2026-10-07.patch`, empreinte SHA-256 commençant par `fb65b90ed527e7f6`.

## Contrôles réellement exécutés

| Commande | Résultat | Détail |
| --- | --- | --- |
| Analyse syntaxique de `cardiovascular_cs.js` (Node) | Réussi | — |
| `MEDINA_OUT=$PWD/dist python3 build_front.py --all-fragments` | Réussi | 22 fragments |
| `python3 tests/audit_fragments.py` | Réussi | JavaScript valide, build reproductible |
| `python3 tests/audit_sciences.py --out /tmp/sci.json` | Réussi | `errors: []` |
| `python3 test_v7.py --static I48 I70 I71 I80` | Réussi | — |
| `git apply --check` du patch sur `bb13485` et sur `e7cbc52` | Réussi | — |
| `node tests/verify_sciences_cs.cjs` | **Non exécuté** | Chromium absent ; son téléchargement est bloqué dans cet environnement. À relancer par Codex. |

**Contrôles exécutés lors de l'intégration** par Claude Code, le 7 octobre 2026, sur `e7cbc52` avec les deux relectures appliquées. Le Chromium utilisé est celui préinstallé dans l'environnement (`chromium_headless_shell-1194`).

| Commande exacte | Résultat | Journal ou détail |
| --- | --- | --- |
| `MEDINA_OUT=$PWD/dist python3 build_front.py --all-fragments` | Réussi | 22 fragments construits |
| `python3 tests/audit_fragments.py` | Réussi | « audit réussi : 22 fragments, JavaScript valide, build reproductible » |
| `python3 tests/audit_sciences.py --out /tmp/medina-science-content.json` | Réussi | `errors: []` |
| `python3 test_v7.py --static I48 I70 I71 I80` | Réussi | I48 : 25 242 mots, 88 fenêtres, 4 quiz, 15 Pareto ; OK |
| `MEDINA_CHROMIUM_PATH=/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell MEDINA_QA_OUT=/tmp/medina-sciences-cs node tests/verify_sciences_cs.cjs` | **Réussi** | `{"result": "passed", "checks": 569, "errors": []}` |

## Limites

Cette relecture porte sur les repères et les manœuvres du module CS cardiovasculaire. Elle ne vérifie ni la géométrie des modèles 3D, ni le rendu mobile, ni les cours liés. Plusieurs sources sont des extraits, non des textes intégraux ; les seuils retenus (C02, C04) proviennent du seul texte intégral lu (CCJM 2013). Aucun statut d'audit n'est promu.
