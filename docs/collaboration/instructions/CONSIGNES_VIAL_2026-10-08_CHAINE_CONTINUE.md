# MEDINA — Consignes de Vial du 8 octobre 2026 : chaîne continue, cardiologie complète, bouton Examen fédéral

Destinataires : **Claude Code** (modèle Opus 5.5 à la demande de Vial) et **Codex**. Ce document s’applique aux deux IA à parts égales. Il complète le protocole par fragment du 8 octobre 2026 et prime sur toute consigne antérieure incompatible. Les travaux, preuves et injections antérieurs restent conservés.

## 1. Principe directeur : un processus continu qui n’attend pas

- **Aucune IA n’attend que Vial demande de continuer.** Après chaque livraison, la tâche suivante de la file démarre immédiatement.
- Le processus ne s’arrête que dans deux cas : **(1)** tous les fragments attribués à l’IA sont rédigés, auto-revus et transférés à l’autre IA pour audit ; **(2)** Vial écrit explicitement « STOP ».
- **Interruption par Vial pour une correction** : la correction passe en priorité absolue, elle est livrée et signalée à Vial, puis la production reprend en arrière-plan là où elle s’était arrêtée. Une interruption n’est jamais un STOP.
- Les sous-agents de production continuent pendant le traitement d’une correction ; seul le fichier concerné par la correction est verrouillé jusqu’à sa livraison.

## 2. Cardiologie (C-01-Cardiologie) : enchaînement jusqu’à la fin

- Claude enchaîne **tous les chapitres CIM-10-GM 2024 restants** du fragment C-01-Cardiologie, organisés **par catégorie**.
- Inventaire au 8 octobre 2026 : **76 catégories CIM** rattachées à C-01, **21 cours présents**, **18 catégories sans cours**, regroupées en **9 cours** ci-dessous.
- Chaque intitulé suit le format **code — intitulé (libellé complet du fragment)**.

| Cours | Catégories couvertes | Contenu central |
| --- | --- | --- |
| I51 — Complications des cardiopathies (C-01-Cardiologie) | I51, I52 | Thrombus intracardiaque, complications mécaniques, Tako-tsubo, cœur et maladies systémiques |
| I73 — Autres maladies vasculaires périphériques (C-01-Cardiologie) | I73 | Raynaud, thromboangéite oblitérante, érythromélalgie, acrocyanose |
| I77 — Autres atteintes des artères, artérioles et capillaires (C-01-Cardiologie) | I77, I78, I79 | Dysplasie fibromusculaire, dissections non aortiques, Rendu-Osler |
| I85 — Varices œsophagiennes et d’autres localisations (C-01-Cardiologie) | I85, I86 | Hypertension portale, rupture variceuse (Baveno VII) |
| I89 — Lymphœdème et atteintes lymphatiques (C-01-Cardiologie) | I88, I89 | Reprise de la version I89-3 et levée des réserves Codex |
| I95 — Hypotension et anomalies tensionnelles isolées (C-01-Cardiologie) | I95, R03 | Hypotension orthostatique, effet blouse blanche |
| I97 — Troubles circulatoires après actes médicaux (C-01-Cardiologie) | I97, I98, I99 | Syndrome post-péricardiotomie, complications périopératoires |
| R00 — Palpitations, anomalies du rythme et souffles (C-01-Cardiologie) | R00, R01 | Démarche symptomatique de premier recours |
| R02 — Gangrène (C-01-Cardiologie) | R02 | Ischémie critique, pied diabétique, gangrène sèche et humide |

- Fin de la cardiologie : fragment entier auto-revu, puis **remise à Codex pour relecture** (audit croisé unique, corrections et injection par Codex, selon le protocole par fragment). Le statut INJECTÉ reste immuable.
- Aucune complétude CIM-11 n’est déclarée par cette liste : elle couvre la CIM-10-GM 2024 du catalogue local ; le rapprochement CIM-11 reste exigé avant certification.

## 2 bis. Tous les fragments : complétude CIM sans lacune

- La règle de la cardiologie s’applique **à chaque fragment produit par Claude ou par Codex** : **toutes les catégories CIM** rattachées au fragment reçoivent un cours fondé sur la CIM, seul ou regroupé avec des catégories voisines dans un cours explicitement déclaré (`covers`). **Aucune catégorie ne reste sans cours.**
- Le producteur dresse l’inventaire exhaustif des catégories du fragment au démarrage, le publie dans la pile (section 4) et démontre à la remise que chaque catégorie est couverte.
- Toutes les instructions valides à ce jour restent applicables simultanément : protocole par fragment, justification des affirmations, sources datées, police et lisibilité, isolement des spécialités, thème clair, un auteur par fichier. En cas de doute, appliquer la règle la plus exigeante pour la qualité.

## 3. Bouton « Isolate Federal – CH Exam »

- Un bouton nommé exactement **« Isolate Federal – CH Exam »** figure dans chaque frontend de fragment.
- En appuyant dessus, **les catégories restent affichées**, mais les chapitres correspondant aux **situations cliniques communes de la pratique quotidienne et aux situations d’examen fédéral** passent **en surbrillance « poudre d’or »** (fond doré, scintillement discret, contraste conservé). Un second appui rétablit l’affichage normal ; le choix est mémorisé localement.
- La liste est centralisée dans `organisation/federal_exam.json`, par fragment. Elle s’appuie sur les objectifs fédéraux (*Exigences MED 2026*, OFSP) et les situations de départ PROFILES ; elle constitue une **sélection éditoriale**, pas une pondération officielle. Chaque IA complète la liste de ses fragments lors de leur production ; l’autre IA la contrôle à l’audit.
- Le bouton respecte le thème clair exclusif, la police Atkinson Hyperlegible Next et les contrastes élevés.

## 4. Pile visible des prochains fragments

- La pile des prochains fragments est visible en permanence dans `organisation/PILE_FRAGMENTS.html` (et sa source JSON) : **au minimum le fragment suivant de chaque IA, avec toutes ses catégories et toutes ses leçons** (cours rédigés, à venir, groupements prévus).
- Claude : fragment suivant **P-02-Pneumologie**. Codex : fragment actif **I-03-Infectiologie**, puis **N-05-Neurologie**.
- La pile est régénérée par `tools/pile_fragments.py` à chaque livraison.

## 5. Parallélisme par catégories

- Chaque IA emploie **plusieurs sous-agents en parallèle, chacun responsable d’une catégorie** (ou d’un cours regroupant plusieurs catégories) du fragment actif. Cette règle remplace l’ancienne limite d’un seul chapitre en production par agent.
- **Un auteur par fichier** : un sous-agent écrit uniquement les fichiers de son cours. **Le producteur ne modifie jamais les sources canoniques** (`chapters/`, `glossary/`, `chapters.json`) : ses cours vivent dans `livraisons/Livraison <IA>/<fragment>/travail/sources/` puis dans l’espace de remise ; seul l’auditeur les injecte après l’audit croisé (garde `tools/espace.py garde`). Un intégrateur unique tient les registres de travail et la pile.
- La production du fragment suivant peut être préparée (inventaire, pile, recherches) pendant l’audit du fragment précédent ; elle ne rouvre jamais un fragment INJECTÉ.

## 6. Qualité : exigences maintenues sans exception

- Justifier chaque affirmation : mécanisme causal, conséquence clinique, limites, source primaire datée. Ne pas confondre association et causalité.
- Sources suisses d’abord (sociétés savantes, OFSP, Swissmedic, Compendium daté), puis européennes et internationales acceptées en Suisse. Aucun chiffre ni posologie inventés.
- Quatre onglets, Pareto par grande partie, dernier îlot (critères formels puis paramètres clés), quiz, glossaire sans abréviation orpheline, `B.audit` = `{}`.
- Style : `docs/STYLE_REDACTION.md` ; phrases complètes ; aucun remplissage ni répétition ; aucun plafond de mots.
- Revue IA, tests automatiques et validation par un médecin ne sont jamais assimilés.
- Frontend : thème clair exclusif, police Atkinson Hyperlegible Next, une couleur vive par spécialité, isolement strict de chaque spécialité.

## 6 bis. Précisions de Vial (8 octobre 2026, suite)

- **Captures de chapitre** : règle levée par Vial le 8 octobre 2026 (« plus besoin de Capture »).
- **Captures d’écran à chaque livraison** : toute livraison montrée à Vial est accompagnée de captures réelles du rendu (ordinateur et mobile), produites dans un navigateur et envoyées directement dans la conversation.
- **Tout évoquer, sans bavardage** : un chapitre peut aborder toute notion utile, mais chaque phrase doit apporter une information, un mécanisme ou une décision. Aucun remplissage, aucune transition creuse, aucune répétition.
- **Sémiologie CS dans tous les fragments concernés** : le module « Sémiologie CS » (compétences cliniques d’examen et d’interrogatoire), aujourd’hui présent en cardiologie, est produit pour **chaque fragment où il s’applique** (pneumologie, gastroentérologie, neurologie, endocrinologie, néphrologie, hématologie, gynécologie, obstétrique, rhumatologie et orthopédie, urologie, dermatologie, ORL, ophtalmologie, urgences, médecine des âges de la vie, etc.). Il fait partie de la complétude du fragment, figure dans sa navigation et suit le modèle `modules/cardiovascular_cs.*`. Les fragments sans examen clinique propre (par exemple éthique et droit) en sont dispensés après justification écrite.

## 7. Réciprocité Claude ↔ Codex

- Codex applique les sections 1, 3, 4, 5 et 6 à ses propres fragments (file : T1, S08, S04, T4, S16, S07, S15, S11, T5, T6).
- Codex audite la cardiologie dès sa remise complète par Claude ; Claude audite chaque fragment Codex remis complet.
- Toute remise, tout audit et toute injection reçoivent un accusé dans `docs/collaboration/receipts/` avec commit exact et empreintes.

## 8. Emplacement et traçabilité

- Ce document : `docs/collaboration/instructions/CONSIGNES_VIAL_2026-10-08_CHAINE_CONTINUE.pdf` et sa source `.md`, référencés dans `CLAUDE.md`, `AGENTS.md` et `COORDINATION.md`.
- Il est lu à chaque reprise par les deux IA avant toute production.
