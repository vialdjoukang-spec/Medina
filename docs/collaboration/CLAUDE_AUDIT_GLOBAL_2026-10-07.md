# Claude — audit médico-rédactionnel intégral de MEDINA

> Répartition actualisée le 7 octobre 2026 : quinze cours existants par agent, selon [MECHANISMS_PLAN.json](MECHANISMS_PLAN.json) et [la mission Claude](MECHANISMS_CLAUDE.md). Cette mission historique définit la qualité attendue ; elle n’attribue plus les trente cours à Claude seul. Chaque affirmation doit désormais recevoir sa justification explicite.

Date : 7 octobre 2026. Statut : **mission publiée ; démarrage et lecture par Claude non confirmés**.

## Objectif et priorité

Relire toutes les productions actuellement intégrées dans les cinq fragments livrés. Corriger leur langue, leur précision médicale et leur progression didactique. Le texte doit être professionnel, épuré et agréable à lire. Son intérêt provient d'une question clinique claire, d'un mécanisme intelligible et de conséquences concrètes.

Cette mission **élargit la mission I48 à l'intégralité du périmètre**. Elle comprend I48, mais ne se limite ni à ce cours ni aux paragraphes récemment ajoutés. Les instructions actuelles du propriétaire priment sur les anciens prompts : une révision peut supprimer les répétitions et les commentaires de rédaction ; elle conserve chaque notion utile.

## Base exacte et accès

- Dépôt public : [vialdjoukang-spec/Medina](https://github.com/vialdjoukang-spec/Medina).
- Branche de livraison : [`codex/sciences-cs-fragments-20261007`](https://github.com/vialdjoukang-spec/Medina/tree/codex/sciences-cs-fragments-20261007).
- **Base pédagogique figée** : [`bb134857e12245f46b4f329c1334ebd57251fcff`](https://github.com/vialdjoukang-spec/Medina/tree/bb134857e12245f46b4f329c1334ebd57251fcff).
- [Inventaire exhaustif avec empreintes SHA-256](CLAUDE_REVIEW_SCOPE_2026-10-07.json).

Les empreintes du manifeste correspondent aux octets suivis dans Git à cette base. Cette mission, la règle de complétude CIM-11 et le guide rédactionnel portent les nouvelles instructions prioritaires ; elles priment sur les formulations historiques de `CLAUDE.md` et `PROMPT_MEDINA.md`. Le seul ajustement d'interface annoncé avec ces instructions remplace le libellé « catégories » de l'accueil et de son attribut d'accessibilité par « rubriques ». Il ne modifie aucun contenu médical ni l'inventaire des cours. Claude relève le commit de ce complément dans son rapport.

Claude travaille sur `claude/review-medina-global-20261007`, créée depuis la livraison des consignes, ou sur sa propre branche. Le contenu pédagogique reste celui de la base figée. Le propriétaire a autorisé de manière permanente les publications, pushes et pull requests nécessaires au projet. Les droits d'écriture dépendent de la connexion GitHub effective de Claude. Le dépôt reste accessible aux autres IA ; cette attribution n'ajoute aucun verrou GitHub. Une mission publiée ne prouve pas qu'une IA l'a commencée. [Accès et protocole commun](README.md) ; [zone de remise des rapports](reviews/README.md).

## Lecture préalable

Lire les instructions actuelles de `CLAUDE.md`, `PROMPT_MEDINA.md`, `CHAPTER_SPEC.md` et `docs/STYLE_REDACTION.md`, puis :

- [Modèle de rapport](REVIEW_TEMPLATE.md).
- [Sources canoniques et exigences de preuve](SOURCES_CANONIQUES.md).
- [Mission I48 et passages ESC 2024](CLAUDE_I48_ESC2024_2026-10-07.md).
- [Compte rendu de la livraison et limites des contrôles](../../audits/SCIENCES_CS_2026-10-07/README.md).
- [Règle prioritaire de complétude CIM-11](../COMPLETUDE_CIM11.md) et [relevé actuel des lacunes](../../audits/COMPLETUDE_2026-10-07/README.md).

Les référentiels cités constituent des points d'entrée. Leur présence dans le registre ne prouve pas la vérification de chaque affirmation du cours.

## Périmètre exhaustif

| Fragment | Cours intégralement concernés |
| --- | --- |
| S01 — Cardiovasculaire | I00, I10, I21, I25, I30, I33, I34, I35, I40, I42, I44, I46, I47, I48, I49, I50, I70, I71, I80, Q21 |
| S02 — Respiratoire | J45, J44, J18, I26 |
| S07 — Immunitaire | D84, M32, M31, T78 |
| S10 — Locomoteur | M06 |
| T1 — Agents et thérapeutique | A41 |

**Cours : 30 dossiers, 251 fichiers HTML sources, quatre onglets par cours, 140 disciplines scientifiques et 2 026 déclarations de fenêtres.** Le nombre de fenêtres inclut les développements, les anciens contenus et les Pareto ; il ne représente pas 2 026 fenêtres nouvellement créées.

Lire chaque fichier de `chapters/<CODE>/` recensé dans le manifeste : `_a.html`, `_b.html`, `_c.html`, `_d.html` et tous les `_pop*.html`. La lecture couvre les titres, paragraphes, listes, tableaux, encadrés, cas, quiz et corrections, critères diagnostiques, références, SVG, légendes, textes d'accessibilité et intitulés des boutons. Elle contrôle les répétitions et les contradictions entre les quatre onglets et les fenêtres.

**Glossaire : les 33 fichiers `glossary/*.py` suivis à la base.** Relire leurs textes affichés : définitions, développements littéraux, aides, titres et noms d'essais. Ce glossaire est global ; un sigle peut être utilisé dans plusieurs cours. Préserver les clés et la structure Python, signaler les collisions et vérifier les conséquences d'une définition modifiée.

**Sémiologie CS :** relire `modules/cardiovascular_cs.html` en entier : dix étapes, introduction, plan, tableaux, liens, trois cas corrigés, neuf cases de contrôle et sources. Dans `modules/cardiovascular_cs.js`, relire les textes des quatre modèles — thorax, cou, pouls, cœur — et de leurs 25 repères : titres, descriptions, légendes, consignes et textes d'accessibilité. Vérifier les termes anatomiques, les techniques et l'interprétation de chaque signe. Les modèles sont stylisés ; la correction rédactionnelle ne les transforme pas en représentation anatomique exacte.

**Interface et consultation :** relire uniquement les textes visibles de `shell/fragment.js`, `fragments.json` et `deliverables/review-2026-10-07/index.html`. Distinguer les rubriques éditoriales de l'accueil des catégories de la classification. Les corrections de libellé sont proposées à Codex ; Claude ne modifie pas les fonctions de navigation, le moteur, le build ou la géométrie des modèles.

Le manifeste recense **289 fichiers de contenu à relire**, hors documents de référence. Il donne les chemins exacts, les empreintes, les cours, les onglets, les identifiants de section et les clés des fenêtres.

## Critères de correction

1. Employer un français médical professionnel, précis et constant. Définir les termes utiles sans rendre le texte artificiellement solennel.
2. Entrer directement dans la notion. Supprimer les introductions « cet îlot présente », « cette partie explique » ou « le lecteur apprend ». Une entrée pédagogique pose un problème médical ; elle ne décrit pas la fabrication du cours.
3. Donner une idée utile par phrase. Employer des phrases complètes dans les explications ; garder des titres courts et des cellules de tableau adaptées à leur fonction.
4. Relier le fonctionnement normal à la perturbation, puis au signe, à l'examen ou à la décision. Nommer le mécanisme plutôt que recourir à une formule vague.
5. Supprimer les répétitions et les transitions clonées. Conserver les distinctions, exceptions, limites et informations utiles. Aucun quota de mots n'est imposé ; la longueur se justifie par le contenu.
6. Introduire et interpréter chaque figure et tableau par une information spécifique. Une légende précise les structures, les relations, le sens des axes et les limites réellement pertinentes.
7. Écarter les métaphores, les jeux de mots, les phrases de chantier, les compliments au cours et le remplissage. Les exemples cliniques servent à comprendre ou décider.
8. Distinguer constatation, interprétation et degré de certitude. Une précaution utile est située dans son contexte ; elle n'est pas répétée mécaniquement à chaque paragraphe.
9. Vérifier la cohérence des termes, valeurs, seuils et traitements entre texte, tableaux, figures, quiz, fenêtres, glossaire et Pareto.

Une correction purement linguistique conserve exactement le sens médical. Toute modification d'un fait, d'un seuil, d'une manœuvre, d'une dose ou d'une recommandation cite le passage primaire réellement consulté : organisme, version, URL ou DOI, section/tableau/page, date et type d'accès. Une source suisse applicable est recherchée en premier. Une affirmation non vérifiée reste explicitement en réserve dans le rapport ; elle ne devient pas un conseil médical nouveau.

## Écarts déjà repérés à contrôler

Ces exemples orientent la première passe ; ils ne remplacent pas la lecture complète.

| Repère à la base figée | Écart à examiner | Travail attendu |
| --- | --- | --- |
| `chapters/A41/A41_a.html:6` ; `chapters/J44/J44_a.html:17` | « Cet îlot présente… » | Remplacer le commentaire sur le cours par l'information clinique utile. |
| `A41_c.html:7`, `D84_c.html:40`, `M06_c.html:26`, `M31_c.html:47`, `M32_c.html:26`, `T78_c.html:55` dans leurs dossiers respectifs | « La figure organise les étapes de cette explication… » revient 21 fois. | Expliquer ce que montre chaque figure ; supprimer les phrases clonées sans supprimer ses limites utiles. |
| Mêmes fichiers | Les appels « La fenêtre… complète la lecture et ses limites » se répètent trois à cinq fois par cours. | Donner une destination précise seulement lorsque son ouverture apporte une information locale. |
| `chapters/I40/I40_c.html:197` | « Le lecteur distingue une explication de l'hétérogénéité et la décision de prélever » apparaît dans le développement puis dans « À retenir ». | Expliquer directement le rapport entre lésion focale, échantillonnage et indication de biopsie. |
| `chapters/A41/A41_c.html:7` | « une production liée à une difficulté énergétique » | Nommer le mécanisme du lactate avec précision et source. |
| `modules/cardiovascular_cs.html:20` ; `modules/cardiovascular_cs.js:13` | « phénomènes graves » peut confondre fréquence acoustique et gravité clinique. | Employer une terminologie acoustique explicite, après contrôle du contexte. |
| `modules/cardiovascular_cs.html:10` | « syncope persistante » | Réviser ce terme avec sa définition médicale et l'action clinique attendue. |
| `modules/cardiovascular_cs.html:16` | « une estimation jugulaire renseigne les pressions droites » | Corriger la construction et vérifier la précision de l'estimation. |

Certaines formulations « cet îlot » précèdent les enrichissements du 7 octobre. Elles restent dans le périmètre, puisqu'elles figurent dans les cours livrés. La formule « directement dans le bain » n'a pas été retrouvée lors de la recherche initiale ; elle ne doit pas être citée comme une occurrence du code.

## Complétude CIM-11 : contrôle distinct

le propriétaire exige un cours pour chaque leçon et catégorie de la CIM-11 applicable à chaque système. Les codes et les regroupements de la livraison actuelle proviennent de la **CIM-10-GM 2024**. La présence de trente cours, leur relecture linguistique et les tests navigateur ne démontrent donc pas une complétude CIM-11.

Ne certifier aucun système « complet CIM-11 » sans inventaire officiel versionné, rattachement explicite aux systèmes, correspondance documentée et preuve de traitement de chaque catégorie et sous-catégorie applicable. Un code présent dans le catalogue, un titre ou un lien ne constituent pas une leçon traitée. Une correspondance CIM-10/CIM-11 ne se déduit pas de la ressemblance des intitulés.

Claude signale les lacunes observées et les ambiguïtés de périmètre. L'audit exhaustif de classification se tient dans un rapport distinct. Une nouvelle leçon reste à produire et à auditer ; une réécriture élégante d'un cours existant ne comble pas cette absence.

## Répartition et remise

| Responsable | Périmètre réservé |
| --- | --- |
| Claude | Relecture et propositions de réécriture de l'ensemble des textes recensés, avec contrôle médico-rédactionnel et journal de couverture. Corrections sur sa branche ou dans un patch. |
| Codex | Intégration des propositions reçues, interface, navigation, géométrie, build et audits techniques. Création de nouveaux cours hors de ce périmètre. |

Codex préserve la base pédagogique de relecture. Une correction médicale urgente ou une contribution concurrente concernant ce périmètre est signalée par fichier et commit avant intégration. Le petit changement de libellé annoncé plus haut est documenté séparément. Claude ne modifie pas `DONE_COURSES`, `DONE_SYS` ni les badges d'achèvement.

Remettre un **rapport et un journal de couverture**, puis un patch ou une branche si des corrections sont proposées. Sans accès en écriture à GitHub, le rapport et le patch suffisent. Aucune communication directe entre les IA n'est présumée.

Le journal associe chaque fichier à son cours/module, son onglet et ses sections ou clés de fenêtres. Il utilise les états `non_lu`, `relu_sans_modification`, `corrige_propose`, `corrige_et_controle`, `reserve_non_resolue`. Il précise le commit relu et les sections réellement examinées. La lecture d'un seul passage ne permet pas de cocher le fichier entier. Un rapport intermédiaire annonce sa couverture réelle.

Chaque correction possède un identifiant, le fichier, un repère stable, le passage actuel, le remplacement proposé, le motif et la vérification du sens conservé. Si le sens médical change, elle porte la source précise. La relecture finale contrôle les corrections appliquées et les concordances entre supports. La remise énumère les réserves, les sources inaccessibles et les vérifications non exécutées.

Pour préparer un patch depuis la base figée, après les corrections locales :

```bash
git diff bb134857e12245f46b4f329c1334ebd57251fcff -- chapters glossary modules/cardiovascular_cs.html modules/cardiovascular_cs.js shell/fragment.js fragments.json deliverables/review-2026-10-07/index.html > MEDINA_CLAUDE_AUDIT_GLOBAL.patch
```

Les nouveaux fichiers nécessaires sont signalés et joints séparément s'ils ne figurent pas dans le diff. Aucune fusion sur `main` n'est demandée par cette mission. Codex compare le patch à la version courante, intègre les corrections retenues et relance les contrôles adaptés.

## Contrôles techniques utiles

```bash
python3 build_front.py --all-fragments
python3 tests/audit_fragments.py
python3 tests/audit_sciences.py --out /tmp/medina-science-content.json
python3 test_v7.py --static I00 I10 I21 I25 I30 I33 I34 I35 I40 I42 I44 I46 I47 I48 I49 I50 I70 I71 I80 Q21 J45 J44 J18 I26 D84 M32 M31 T78 M06 A41
MEDINA_QA_OUT=/tmp/medina-sciences-cs node tests/verify_sciences_cs.cjs
```

Le navigateur est détecté par `tests/browser_runtime.cjs` ; `MEDINA_CHROMIUM_PATH` reste facultative. Si Claude ne peut pas exécuter un contrôle, son rapport l'indique et Codex le prend en charge lors de l'intégration. Un contrôle technique réussi ne valide ni le fond médical ni la complétude de classification.

La livraison de cette mission permet de commencer la relecture. Seul un retour de Claude, accompagné de son périmètre effectivement relu, permet d'en déclarer l'avancement.
