# Audit linguistique agressif — G63 Polynévrite au cours de maladies classées ailleurs

Mission ALPHA1-CLAUDE-G63-LANG, génération 1, branche `claude/alpha1/g63-lang-g1`, commit de base `32416a20`. Audit IA : revue distincte d’une validation médicale humaine ; aucune source canonique modifiée. Fin de l’audit : 2026-10-16T06:05:01Z.

## Résumé pour Vial

Les sept fichiers de la leçon (quatre onglets, deux fichiers de fenêtres, glossaire) ont été lus en entier ; leurs empreintes SHA-256 sont conformes au manifeste. L’audit propose **81 remplacements locaux** (`propositions.json`), tous à ancre unique vérifiée mécaniquement, sans changement de chiffre, de dose, de seuil ni de source, et **45 renvois médicaux** là où une reformulation aurait créé ou modifié une causalité, une fréquence, une chronologie ou un degré de certitude. Trois constats sont transmis à l’audit MED (sous-onglets, provenance et lisibilité des figures, proportionnalité de la figure 5).

La leçon est bien construite : annonces directes, tableaux introduits et commentés, limites des sources nommées. Les défauts relevés tiennent surtout à des ellipses (phrases nominales), à des pronoms sans antécédent clair, à quelques répétitions et calques (« drapeaux rouges », « dose cumulée vie entière », « survol »), et aux libellés du glossaire des sous-rubriques, grammaticalement faux.

Aucune reformulation n’affaiblit une obligation clinique : les formulations d’urgence passent au contraire à « il faut… » (encadré de la section 8).

## Constats les plus graves

- **Libellés du glossaire G63.x** (`glossary/g63.py`) : la clé construit « Polynévrite tumorales », « Polynévrite infectieuses… », « Polynévrite d’autres maladies… » ; correction vers les libellés officiels du tableau de la leçon (propositions G63-LANG-gloss-01 à 06).
- **Ordre logique inversé dans une clé** (`G63_b`, section 6) : « le pied à risque se classe selon la fréquence des contrôles » alors que la catégorie fixe la fréquence (G63-LANG-b-07).
- **Comparaison fautive** (`G63_b`, question 2) : « dont l’évolution est plus rapide et motrice que la neuropathie alcoolique » (G63-LANG-b-09).
- **Contresens apparent de statistique** (`G63_c`, e-2), renvoyé : « un résultat pathologique manque parfois le risque réel » ; c’est un résultat normal qui manque un risque (RM-29).
- **Phrase illogique en fenêtre** (`G63_pop1`, neuropathie alcoolique) : « les vitamines B constituent la meilleure preuve disponible » (G63-LANG-pop1-02).
- **Renvois médicaux de fond** : généralisation « quelle que soit la maladie de base » contredite en 3.5 (RM-01), maladie de base N18 présentée comme « neuropathie urémique » (RM-11), « bilan étendu » défini de deux façons (RM-19), dose de départ du sujet âgé identique à celle de l’adulte (RM-42).

## Constats transmis à l’audit MED

- **G63-LANG-HP-01** — hors périmètre linguistique, MAJEUR, transmis à l’audit MED. Décompte réel des `data-s` de `G63_c.html` : 4 (`g63-s-anat`, `g63-s-histo`, `g63-s-physio`, `g63-s-bioch`). Aucun sous-onglet « Sémiologie fondamentale et analytique », et 4 disciplines réelles au lieu de 5.
- **G63-LANG-FIG-01** — ORIGINE_INCONNUE, avec réserve : six figures SVG sans légende de provenance ; figures 3 et 4 ouvertes comme les plus proches d’une représentation anatomique ; figures 1, 2, 5 et 6 non anatomiques. Le contrôle linguistique porte sur le texte des figures, pas sur leur provenance, transmise à l’audit MED, avec la lisibilité à 390 px (viewBox 640 pour les figures 3 à 5).
- **G63-LANG-FIG-02** — la légende de la figure 5 annonce des hauteurs proportionnelles ; le rapport hauteur/valeur varie de 17,4 à 18,8.

## Choix différés (non appliqués)

1. Espaces insécables globales (573 ponctuations doubles précédées d’une espace ordinaire, 10 guillemets, milliers).
2. Alternative « fibrillation atriale/auriculaire » : aucune occurrence dans G63.

## Renvois médicaux (échantillon par fichier ; liste complète dans `rapport.json`)

| Fichier | Renvois |
|---|---:|
| chapters/G63/G63_a.html | 15 |
| chapters/G63/G63_b.html | 11 |
| chapters/G63/G63_c.html | 9 |
| chapters/G63/G63_d.html | 7 |
| chapters/G63/G63_pop1.html | 1 |
| glossary/g63.py | 2 |

Les renvois signalent des formulations (« donc », « parce que », « explique », « s’additionnent », « fonde », « souvent », « tôt », « tardivement », « avant ») qui posent une causalité, une fréquence ou une chronologie. L’audit ne dit pas que ces énoncés sont faux : il demande que l’audit MED vérifie qu’une source lue les établit.

## Tableau de bord

| Fichier | Propositions |
|---|---:|
| chapters/G63/G63_a.html | 17 |
| chapters/G63/G63_b.html | 21 |
| chapters/G63/G63_c.html | 18 |
| chapters/G63/G63_d.html | 8 |
| chapters/G63/G63_pop1.html | 5 |
| chapters/G63/G63_pop2.html | 5 |
| glossary/g63.py | 7 |
| **Total** | **81** |

| Catégorie | Nombre |
|---|---:|
| grammaire | 11 |
| répétition | 10 |
| lourdeur | 9 |
| phrase nominale | 9 |
| ambiguïté | 8 |
| lexique | 6 |
| syntaxe | 5 |
| anglicisme | 4 |
| cohérence | 3 |
| méta-discours | 2 |
| précision | 2 |
| ponctuation | 2 |
| registre | 2 |
| cohérence terminologique | 2 |
| contresens | 2 |
| calque | 1 |
| unités | 1 |
| nombres | 1 |
| intitulé | 1 |

## Contrôles mécaniques

- Empreintes SHA-256 des 7 fichiers : conformes au manifeste.
- Unicité : 81 sur 81 `ancien` apparaissent exactement une fois dans leur fichier ; aucun chevauchement (`verification_unicite.py`, exécutable depuis la racine du worktree).
- Nombres : identiques avant et après, hors conversion « deux à trois » en « 2 à 3 » et ajout de « mL/min » (OG-05).
- Validation JSON : `python3 -m json.tool` sur `rapport.json` et `propositions.json`.

## Lacunes

- Aucune source médicale n’a été relue : un audit linguistique ne vérifie pas les faits. Les 45 renvois médicaux sont posés sur la seule lecture du texte, sans avoir ouvert Sommer 2018, Feldman 2019, Julian 2019, Graus 2021, Adams 2016, Arnold 2016, Finnerup 2015, QualiCCare ni les informations professionnelles : « causalité / fréquence / chronologie » signifie « à confirmer dans la source », non « faux ».
- Aucun test en navigateur : l’effet des propositions sur l’affichage n’a pas été mesuré.
- build_medina.audit() n’a pas été exécuté ; la présence d’abréviations sans clé a été contrôlée par recherche textuelle.
- Les choix différés (espaces insécables, fibrillation) ne sont pas traités.
- Les figures n’ont pas été ouvertes en navigateur ; leur texte a été lu dans le SVG.
- Pas de correcteur externe (Antidote, LanguageTool) : lecture intégrale et contrôles mécaniques seulement.

## Observations globales

- **G63-LANG-OG-01** — Espaces insécables (différé) : 573 occurrences de ponctuation double précédée d’une espace ordinaire (avant ; : ! ?), 10 guillemets « » sans espace insécable, et séparateurs de milliers absents (2700, 3600, 4200, 100 000). Choix différé par la coordination : aucune proposition.
- **G63-LANG-OG-02** — Alternative « fibrillation atriale/auriculaire » (différé) : Aucune occurrence de « fibrillation » dans les sept fichiers de G63 ; rien à appliquer, choix différé conformément à la consigne.
- **G63-LANG-OG-03** — Noms de genre en italique : « Borrelia » est écrit en romain dans toute la leçon ; la convention typographique demande l’italique. Non proposé (modification de balisage).
- **G63-LANG-OG-04** — Phrases nominales dans les encadrés « À retenir » : Les encadrés clés procèdent par énumération de groupes nominaux (« Reins : adapter… », « Âge et cœur : prudence… »). Choix de style de la leçon ; non modifié pour ne pas affaiblir de consigne clinique.
- **G63-LANG-OG-05** — Unités et nombres : Les propositions ne changent aucune valeur. Seule conversion : « deux à trois fois » en « 2 à 3 fois » dans l’encadré de piège de l’hydroxocobalamine (G63-LANG-d-05) et ajout de l’unité mL/min à la première tranche de clairance de la gabapentine : les décomptes de chiffres du texte visible passent de 10 à 11 (« 3 ») et de 11 à 12 (« 2 ») dans G63_d.html pour cette seule raison.
- **G63-LANG-OG-06** — Abréviations sans clé dans g63.py : CDT, TSH, ANCA, HDL, NMDA, VIH, IgM, IgG, ESMO, QualiCCare et AL n’ont pas de clé dans g63.py mais en ont une dans d’autres glossaires du dépôt (recherche textuelle de la clé dans glossary/*.py). La conformité à build_medina.audit() n’a pas été exécutée.

*Audit IA — revue distincte d'une validation médicale humaine ; aucune source canonique modifiée.*
