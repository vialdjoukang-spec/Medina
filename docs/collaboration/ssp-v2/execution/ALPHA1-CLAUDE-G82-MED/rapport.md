# Audit Alpha tour 1 — G82 — Paraparésie et paraplégie, tétraparésie et tétraplégie (N-05-Neurologie, S08)

**Mission** ALPHA1-CLAUDE-G82-MED · audit médical agressif avec enrichissement · génération 1 · branche `claude/alpha1/g82-med-g1`.
**Base du worktree** : `103745baaa38c76f18288758cc7f689e5091ccdb`. **Instantané des sources** (manifeste) : `523832d9ef6097607d3443f4398deee9cd0add11`.
**Exécutant** : sous-agent Claude Code (voir accusé issue 107) ; modèle et effort conformes au manifeste. **Début** : 16.10.2026, 09:15 UTC ; **fin** : voir `rapport.json`, clé `date_fin`.

## Lecture
Les sept fichiers ont été lus en entier : `G82_a`, `G82_b`, `G82_c`, `G82_d`, `G82_pop1`, `G82_pop2` et `glossary/g82.py`. Leurs empreintes SHA-256 sont **conformes au manifeste**. Chaque ancre citée a été vérifiée par script : elle apparaît une seule fois dans son fichier.

La **première source lue** est suisse : l’information professionnelle de Liorésal® (janvier 2025), rubrique « Posologie/Mode d’emploi », obtenue par `tools/swissmedic_fi.py`.

Contrôles exécutés : `test_v7.py --static G82` affiche OK ; `tests/audit_sciences.py --codes G82` **échoue**, car l’encadré « À retenir » manque dans les trois disciplines (C06).

## Verdict d’ensemble
La leçon est prudente et, sur ce que l’audit a pu confronter, **exacte dans ses chiffres**. Les données suisses d’incidence, de mortalité et de recours aux soins sont fidèles aux résumés SwiSCI. Le codage CIM-10-GM est conforme au BfArM, les recommandations AO Spine et EAU 2026 sont correctement rapportées, et les doses de baclofène et d’oxybutynine correspondent aux FI suisses. Aucune erreur dangereuse n’a été trouvée : **aucun constat BLOQUANT**.

Ses défauts sont des manques aux points de décision. La leçon déclare honnêtement ce qu’elle ignore, mais quatre de ces vides sont comblables par des sources lisibles. La sémiologie médullaire est absente. La dysréflexie autonome n’a pas de conduite immédiate. Le sevrage de baclofène intrathécal omet la priorité de la FI suisse. La compression médullaire non traumatique, urgence classique de l’examen fédéral, n’est pas traitée. Enfin, les grades AIS C et D perdent leur critère de statut moteur incomplet.

## Constats par gravité

| Gravité | Nombre |
|---|---|
| BLOQUANT | 0 |
| MAJEUR | 5, dont C01, bloquant pour la clôture |
| MINEUR | 11 |
| ENRICHISSEMENT | 4 |

### MAJEUR
- **C01 — Sémiologie absente (bloquant pour la clôture).** `G82_c.html` compte **3 `data-s`** : `g82-s-anat`, `g82-s-physio` et `g82-s-vesicale` ; `g82-s-semio` manque. L’onglet 1 ne décrit ni niveau sensitif, ni syndrome pyramidal, ni réflexes sacrés. Proposition : `G82_c_semio.html` (neuf sections du contrat, figure de raisonnement non anatomique, trois cas corrigés), `G82_pop3_semio.html` et le bloc C18 de `G82_enrichissements.html`.
- **C02 — Dysréflexie autonome sans conduite.** Le cas d’ouverture reste sans geste. Un protocole hospitalier européen de mai 2026 ordonne la conduite : asseoir le patient, desserrer, sonder sous lidocaïne en vidange fractionnée (500 mL, puis 250 mL toutes les 10 à 15 minutes), chercher un fécalome, puis les autres stimuli [S35]. La nifédipine à libération immédiate de ce protocole n’a pas été trouvée parmi les spécialités suisses [S36]. Aucune dose n’est donc proposée. Proposition : `G82_b_urgences.html`, bloc C02.
- **C03 — Sevrage de baclofène intrathécal.** La FI suisse place en premier le **rétablissement de l’apport intrathécal** ; le relais GABAergique ne sert que si cette reprise est retardée [S27]. Elle donne aussi le délai, des premières heures à quelques jours, et le diagnostic différentiel. La fenêtre de la leçon affirme à tort que ce délai n’est pas chiffré. Proposition : `G82_b_urgences.html`, bloc C03.
- **C04 — Compression médullaire non traumatique absente.** Une source universitaire européenne lue en texte intégral couvre le tableau, les causes par siège et le discriminant périphérique. Elle pose aussi que l’IRM se demande **en urgence** [S34]. Proposition : `G82_b_urgences.html`, bloc C04.
- **C05 — Grades AIS C et D.** ISNCSCI 2019 exige un statut moteur incomplet : contraction anale volontaire, ou épargne sensitive sacrée avec motricité plus de trois niveaux sous le niveau moteur [S2]. La leçon écrit seulement « motricité préservée ». Proposition : `G82_a_ais.html`.

### MINEUR
- **C06** : `audit_sciences.py` échoue (« À retenir » absent dans les trois disciplines).
- **C07** : les contre-indications de l’oxybutynine sont incomplètes. Manquent notamment la rétention par uropathie obstructive ou hyperplasie prostatique, la prudence en cas de neuropathie autonome et la dose initiale du sujet âgé, 2,5 mg deux fois par jour [S22].
- **C08** : la dose de départ d’environ 5 mg/j du baclofène concerne l’hémodialysé chronique, non toute insuffisance rénale [S20].
- **C09** : le calendrier mictionnel se tient de préférence trois jours consécutifs, et non « 2 à 3 jours » [S1, § 3.3.4.a].
- **C10** : 43,3 % rapporte des urodynamiques (122/282), non des patients [S16].
- **C11** : le Credé et la manœuvre de Valsalva sont découragés sauf pressions sûres à l’urodynamique. La miction réflexe déclenchée n’est pas « déconseillée » : elle exige éducation et surveillance [S1, § 3.4.2.a].
- **C12** : la thromboprophylaxie de 2017 est une recommandation faible, et non « recommandée » [S7].
- **C13** : le cône médullaire se trouve dans la région des **vertèbres** L1–L2 ; écrire « segments lombaires » prête à confusion [S2 ; S34].
- **C14** : Pareto : 53,3 % est arrondi à 54 %.
- **C15** : la décompression précoce repose sur des preuves modérées ; le résultat à 12 mois manque (RR 1,95) [S4].
- **C16** : le travail de Nature 2025 est une collaboration Lausanne–Calgary [S28].

### ENRICHISSEMENTS

| Id | Fichier | Apport | Proposition |
|---|---|---|---|
| C17 | G82_pop2 | FI suisse de Solu-Medrol® : traumatisme médullaire dans les 8 heures, mise en garde sur l’administration tardive, schéma Swisspeddose | G82_enrichissements.html |
| C18 | G82_b (pA) | Examen urogénital et réflexes sacrés, hypotension en position assise, section `data-semiology-clinical` | G82_enrichissements.html |
| C19 | G82_b | Spécificité suisse : aptitude à la conduite sous baclofène | G82_enrichissements.html |
| C20 | G82_b | Escarres, intestin, ostéoporose, douleur, respiration : mission d’enrichissement à ouvrir | aucun texte sans source |

## Calculs — « ne rien laisser passer »
Le script `calculs/verifier.py`, exécuté et conservé, fait l’inventaire des sept fichiers par expressions régulières. Il cherche les nombres avec unité, les pourcentages, les rapports, les cotations, les expressions arithmétiques et les codes. Chaque occurrence est rattachée à un contrôle scripté : arithmétique, dose de la FI, seuil, score ou concordance avec la source lue.

| Indicateur | Valeur |
|---|---|
| Occurrences relevées | 338 |
| Calculables ou vérifiables | 337 (1 non calculable : l’âge de la vignette) |
| Recalculées par script | 337 |
| Correctes | 329 |
| Arrondis | 4 (C14 ; C08 ×3) |
| Fausses | 4 (C09 ×2 ; C10 ×2) |
| Non vérifiables | 0 |
| Contrôles scriptés | 78 : 73 corrects, 2 arrondis, 3 faux (K20 → C05, K32 → C10, K55 → C09) |

Les contrôles suivants sont exacts :
- la vignette : 170 − 105 = 65 mmHg, au-dessus du seuil de 125 mmHg, avec un dépassement de 45 mmHg ;
- le cas 3 : une hausse de 18 mmHg ne remplit pas la définition ;
- le score moteur : 11 + 9 = 20 sur 50, niveaux moteurs C6, niveau neurologique lésionnel C5 ;
- la sensibilité : 28 × 2 = 56 points ;
- le codage : G82.12 et G82.64! ;
- la montée du baclofène : 15, 30, 45, 60 puis 75 mg/j, dans les bornes de la FI et réalisable avec les comprimés sécables suisses ;
- l’oxybutynine : 7,5 mg/j au départ, 20 mg/j au maximum ;
- la cohérence des intervalles de confiance (SMR 2,32, HR 3,62, RR 2,76) ;
- les proportions recalculées depuis les effectifs (122/282, 93/122, 2/18, 15/18, 280/1294).

**Aucun calcul faux n’entraîne de geste dangereux.**

## Rubrique 21 — Sémiologie fondamentale et analytique
**Statut : absente — MAJEUR (C01), bloquant pour la clôture.** La leçon a trois disciplines et aucun `g82-s-semio`. La sémiologie fondamentale n’existe que par fragments dans l’onglet 1 : l’examen ISNCSCI et les signes de la dysréflexie. La sémiologie analytique se réduit au tableau moelle, cône et queue de cheval de `g82-8`.

Grille SEM : SEM-04 et SEM-24 sont « oui » ; tous les autres critères sont « non » ou non évaluables (détail dans `rapport.json`). **LACUNE de valeur** : aucune sensibilité, spécificité ni rapport de vraisemblance n’est disponible dans les sources lues pour le niveau sensitif, le signe de Babinski, l’anesthésie en selle ou l’épargne sacrée. La proposition le déclare.

## Matrice des 20 rubriques
Rubriques **couvertes** : 1, 2, 4, 10, 18 et 19. **Partielles** : 3, 5 à 9, 11 à 15, 17 et 20. **Absente** : 16 (spécificités suisses). Le détail figure dans `rapport.json`, clé `matrice_20`.

## Figures
Les quatre figures sont des schémas non anatomiques en SVG ; aucune figure anatomique n’est dessinée par IA. La légende de la figure 2 répète l’imprécision sur le cône (C13). Le rendu à 390 px est estimé à environ 11,6 px, sans mesure au navigateur.

## Lacunes principales
- Aucune source suisse de paraplégiologie ni de sémiologie médullaire n’a été lue.
- Les lignes directrices AO Spine n’ont été lues qu’en résumé.
- NICE NG234 n’a pas pu être lu (HTTP 403).
- Aucune FI suisse d’antihypertenseur rapide n’a été lue pour la dysréflexie.
- Myélite, infarctus médullaire, sclérose en plaques et syndrome de Guillain-Barré n’ont pas de discriminant sourcé.
- Les complications de longue durée et les spécificités suisses (Suva, assurance invalidité) ne sont pas documentées.
- Aucune capture navigateur n’a été réalisée.

## Tableau de bord

| Élément | État |
|---|---|
| Cours | G82 — Paraparésie et paraplégie, tétraparésie et tétraplégie (S08) |
| Empreintes | 7/7 conformes |
| Constats | 0 BLOQUANT · 5 MAJEUR · 11 MINEUR · 4 ENRICHISSEMENT |
| Calculs | 338 relevés · 337 recalculés · 4 faux · 4 arrondis |
| Sémiologie | absente (MAJEUR, bloquant pour la clôture) |
| Sources | 37 (`sources.json`) ; 4 FI suisses datées |
| Propositions | 6 fichiers (`propositions/`) |
| Contrôles | test_v7 OK ; audit_sciences en échec (C06) |

*Audit IA — revue distincte d’une validation médicale humaine ; aucune source canonique modifiée.*
