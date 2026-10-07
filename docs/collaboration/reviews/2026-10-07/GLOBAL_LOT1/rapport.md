# Rapport de relecture MEDINA — audit global, lot 1 : formules clonées et métadiscours

- Responsable : Claude Code (relecture médicale, didactique et linguistique).
- Mission et cours : `docs/collaboration/CLAUDE_AUDIT_GLOBAL_2026-10-07.md`, premier lot des écarts déjà repérés. Cours touchés : A41, D84, M06, M31, M32, T78, I40, J44.
- Branche et commit de départ, SHA complet : `claude/review-medina-global-20261007`, depuis `d4309b0d3de9f2a79499ed3d95da5d5436778d88` (tête de `main` et de `codex/sciences-cs-fragments-20261007`, qui intègre déjà la PR #8).
- Commit relu, SHA complet : `d4309b0d3de9f2a79499ed3d95da5d5436778d88`.
- Date de la relecture : 7 octobre 2026 (Europe/Zurich).
- Fichiers examinés : les 17 fichiers listés dans `journal.json`, **pour les sections indiquées seulement**.
- Fichiers modifiés : `A41_a`, `A41_b`, `A41_c`, `A41_pop_sciences_revision`, `D84_c`, `D84_pop_sciences_revision`, `M06_c`, `M06_pop_sciences_revision`, `M31_c`, `M31_pop_sciences_revision`, `M32_c`, `M32_pop_sciences_revision`, `T78_c`, `T78_pop_sciences_revision`, `I40_c`, `J44_a`, `J44_b`.
- Mode de remise : branche et pull request vers `codex/sciences-cs-fragments-20261007`.
- État : proposition à intégrer ; contrôles techniques réussis.

## Périmètre et principe

Ce lot traite les formules répétées mécaniquement et le métadiscours signalés par la mission globale. Il ne vaut pas relecture intégrale des cours touchés : le journal précise, fichier par fichier, les sections réellement examinées. I48 en entier fera l'objet du lot suivant.

Le principe appliqué est celui de `docs/STYLE_REDACTION.md` § 3 : une annonce expose directement le problème médical. Une figure est introduite par ce qu'elle montre, et sa légende indique le sens de lecture ou la limite qui lui est propre. Un renvoi vers une fenêtre dit ce que son ouverture apporte à cet endroit précis. Toutes les notions utiles sont conservées ; seules les formules vides ou dupliquées disparaissent.

## Observations

| ID | Fichier et repère stable | Passage actuel ou résumé précis | Conclusion et gravité | Correction proposée | Source primaire | Consultation et accès |
| --- | --- | --- | --- | --- | --- | --- |
| L1-01 | `A41_c` (`a41-s-1` à `a41-s-4`), `D84_c` (`d84-sa`, `d84-si`, `d84-sg`), `M06_c` (`m06-sa`, `m06-si`, `m06-sg`), `M31_c` (`m31-sa`, `m31-si`, `m31-sg`), `M32_c` (`m32-si`, `m32-sh`, `m32-sg`), `T78_c` (`t78-sh`, `t78-si`, `t78-sp`, `t78-sb`, `t78-sg`) | « La figure organise les étapes de cette explication. Elle représente un raisonnement qualitatif et ne fournit pas une mesure individuelle. » — 21 occurrences identiques. | Écart didactique, mineur, répété : la phrase n'apprend rien sur la figure qu'elle introduit. | Une introduction propre à chaque figure, qui nomme ses quatre cases et la relation qui les unit. La limite « pas de mesure individuelle » est conservée là où une valeur chiffrée pourrait être imaginée : lactate (`a41-s-3`), fonctions immunitaires (`d84-si`), tryptase (`t78-sh`). | Texte de chaque section ; aucun fait médical ajouté, sauf L1-02 pour `a41-s-4`. | — |
| L1-02 | Les 21 `figcaption` des mêmes sections | « Le trajet simplifie les relations décrites dans le texte. » — 21 occurrences identiques. | Écart didactique, mineur, répété. | Une fin de légende spécifique : sens de lecture, distinction activité/dommage (`m06-sa`), cellules effectrices selon le groupe de vascularite (`m31-si`, repris du texte de la section), définition Sepsis-3 (`a41-s-4`). | Pour `a41-s-4` : Singer M, et al. *The Third International Consensus Definitions for Sepsis and Septic Shock (Sepsis-3)*. JAMA 2016;315(8):801–810. DOI 10.1001/jama.2016.0287 — définition déjà enseignée dans A41, îlot 1. | Définition reprise du cours ; pas de nouvelle consultation. |
| L1-03 | Renvois `data-k="<code>-science-reading"` des six fichiers `_c` | « La fenêtre … complète la lecture et ses limites. » — 20 occurrences, de trois à cinq fois la même fenêtre par cours. | Écart didactique, mineur : le renvoi ne disait pas ce que la fenêtre apporte. | **7 renvois réécrits** avec la destination précise : `a41-s-3`, `d84-si`, `m06-sa`, `m31-si`, `m32-sh`, `t78-sh`, `t78-sg`. **13 renvois supprimés** là où la fenêtre n'apporte rien de local. Chaque fenêtre reste accessible depuis la section dont elle approfondit le sujet. | Contenu des six fenêtres `*_pop_sciences_revision.html`. | — |
| L1-04 | Les six fenêtres `data-pop="<code>-science-reading"` | « À retenir. Le résultat répond à une question précise. Son interprétation exige les autres informations du patient. » — identique dans les six fenêtres. | Écart didactique, mineur. | Un « À retenir » propre à chaque fenêtre, résumant son contenu (lactate et perfusion ; nombre et fonction immunitaire ; activité et dommage articulaire ; ANCA ; sérologie lupique et rein ; tryptase aiguë et basale). | Texte de chaque fenêtre. | — |
| L1-05 | `A41_c`, `a41-s-3`, h3 « Plusieurs voies augmentent le lactate » (repère de la mission : `A41_c.html:7`) | « Une insuffisance d'apport peut favoriser une production liée à une difficulté énergétique. […] Le foie et d'autres organes contribuent à son élimination. » | **Imprécision**, majeure pour un passage de sciences fondamentales : le mécanisme n'était pas nommé. | Le lactate naît du pyruvate par la lactate-déshydrogénase, réaction qui régénère le cofacteur oxydé de la glycolyse. L'hypoxie, par débit faible ou microcirculation perturbée, ralentit l'oxydation mitochondriale. La stimulation bêta-adrénergique accélère la glycolyse en activant la pompe sodium-potassium du muscle, sans hypoxie. Le foie élimine la plus grande partie du lactate et le rein environ 30 %, par oxydation ou néoglucogenèse. | Garcia-Alvarez M, Marik P, Bellomo R. *Sepsis-associated hyperlactatemia*. Crit Care 2014;18(5):503. DOI [10.1186/s13054-014-0503-3](https://doi.org/10.1186/s13054-014-0503-3), PMC4421917. Sections « Normal lactate metabolism », « Adrenergic-driven aerobic glycolysis », « The argument in favor of tissue hypoxia ». | 07.10.2026, texte intégral via PubMed Central. |
| L1-06 | `A41_c`, `a41-s-3`, annonce | « Cette partie apprend à lire son évolution avec les autres signes de perfusion. » | Métadiscours, mineur. | « Son évolution se lit avec les autres signes de perfusion. » | — | — |
| L1-07 | `I40_c`, h3 « Interprétation guidée : Une lésion focale peut échapper à un prélèvement » et son « À retenir » (repère de la mission : `I40_c.html:197`) | « Le lecteur distingue une explication de l'hétérogénéité et la décision de prélever. » — deux fois. | Métadiscours et formule vague, mineurs. | Paragraphe : « L'hétérogénéité explique pourquoi une biopsie peut être faussement négative ; elle ne constitue pas, à elle seule, une indication de prélever. » « À retenir » : « Une biopsie négative n'exclut pas une myocardite focale. L'indication de prélever dépend de la décision que le résultat peut modifier. » | Reformulation fidèle au paragraphe existant ; aucun fait ajouté. La prise de position ESC 2013 sur les myocardites (Caforio ALP, et al. Eur Heart J 2013;34:2636–2648, DOI 10.1093/eurheartj/eht210) n'a pas été lue en texte intégral. | 07.10.2026, notice PubMed seulement. |
| L1-08 | `A41_a` (lignes 6, 17, 24, 60, 84, 124) ; `A41_b` (lignes 2, 36, 65, 128, 157) | « Ce cours enseigne… », « Cet îlot présente / définit / mesure / explique / répond / transforme / place / organise / couvre / adapte… », « le lecteur apprend… » | Métadiscours proscrit par la mission et par `STYLE_REDACTION.md` § 3, mineur, répété. | Onze annonces réécrites en exposé direct du problème médical, avec le même contenu. Les renvois numérotés utiles (« îlot 3 », « îlot 9 », « îlot 2 ») sont conservés. | Aucun fait modifié. | — |
| L1-09 | `J44_a` (lignes 17, 43, 93, 132, 192, 226, 268, 315) ; `J44_b` (lignes 2, 79, 137, 170, 213, 250) | « Cet îlot présente / fixe / mesure / explique / recense / transforme / décrit / expose / traite / construit / organise / adapte… », « le lecteur apprend à distinguer… » | Métadiscours, mineur, répété. | Quatorze annonces réécrites. La première occurrence développe toujours le sigle « bronchopneumopathie chronique obstructive (BPCO) ». | Aucun fait modifié. | — |

### Mécanisme et portée des corrections

La correction L1-05 est la seule qui modifie le contenu médical. L'ancienne phrase « une production liée à une difficulté énergétique » laissait croire à une cause unique et floue. Le texte nomme désormais les deux voies : l'hypoxie tissulaire et la glycolyse accélérée par la stimulation adrénergique. Il nomme aussi les organes qui éliminent le lactate. Cette distinction prépare directement la règle clinique déjà présente dans la section suivante : un lactate élevé ne prescrit pas automatiquement un nouveau bolus. La revue citée présente les deux théories ; le texte n'en privilégie aucune.

Toutes les autres corrections sont linguistiques ou didactiques et conservent exactement le sens médical.

## Changements et remise

Le lot comprend 17 fichiers sources et ce rapport avec son journal. Aucun glossaire n'est modifié et aucune abréviation n'est ajoutée : `test_v7.py --static` ne signale aucune abréviation non couverte. Les fonctions de navigation, le moteur et le build ne sont pas touchés.

Les observations hors de ce lot restent ouvertes :

- **« Cet îlot… »** : 21 occurrences dans J18 et I26. Elles sont prévues dans le lot des cours de la reprise du 26 septembre.
- **« Cette partie… »** : 17 occurrences en tête des disciplines scientifiques de A41, D84, I70, I71, I80, M06, M31, M32 et T78. Le même métadiscours est à traiter dans un lot « sciences ».
- **« Le lecteur… »** : 52 occurrences dans A41, I00, I26, I70, I71, I80, J18 et J44. Elles sont surtout dans les consignes de lecture des figures (« Le lecteur suit la flèche… ») et dans les sections « Objectifs ». Les consignes de lecture d'une figure sont utiles, mais leur formulation peut devenir directe (« La flèche centrale suit… »). Les sections « Objectifs du cours » relèvent d'un choix de structure du propriétaire ; elles sont conservées.

## Contrôles réellement exécutés

| Commande exacte | Résultat | Journal ou détail |
| --- | --- | --- |
| `python3 test_v7.py --static A41 D84 M06 M31 M32 T78 I40 J44 I48 I70 I71 I80` | Réussi | OK ; aucune abréviation non couverte |
| `MEDINA_OUT=$PWD/dist python3 build_front.py --all-fragments` | Réussi | 22 fragments |
| `python3 tests/audit_fragments.py` | Réussi | « audit réussi : 22 fragments, JavaScript valide, build reproductible » |
| `python3 tests/audit_sciences.py --out /tmp/medina-science-content.json` | Réussi | 140 disciplines, 145 figures, `errors: []` |
| `MEDINA_CHROMIUM_PATH=/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell MEDINA_QA_OUT=/tmp/medina-sciences-cs node tests/verify_sciences_cs.cjs` | Réussi | 565 contrôles, 0 erreur |

Le test navigateur compte 565 contrôles au lieu de 569. Il ouvre une fenêtre de lecture seulement si la **première** discipline d'un cours contient un renvoi. Ce renvoi a été supprimé de la première discipline de A41, D84, M31 et M32 (L1-03), d'où quatre contrôles de moins. Les fenêtres restent ouvertes et vérifiées dans M06 et T78. Si Codex souhaite conserver ce contrôle pour les six cours, le test peut cibler la première discipline qui contient un renvoi, au lieu de la première discipline.

Un test technique réussi ne valide pas la médecine.

## Limites de la conclusion

Ce lot ne certifie aucun cours entier. Les fichiers touchés n'ont été relus que dans les sections indiquées par le journal. La prise de position ESC 2013 sur les myocardites n'a pas été lue en texte intégral ; la correction L1-07 n'ajoute donc aucun fait. Les statuts `DONE_COURSES` et `DONE_SYS` ne sont pas modifiés, et aucune complétude CIM-11 n'est revendiquée.
