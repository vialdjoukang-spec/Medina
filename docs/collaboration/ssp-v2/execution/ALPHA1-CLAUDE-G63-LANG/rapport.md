# Audit linguistique agressif — G63 Polynévrite au cours de maladies classées ailleurs

Mission ALPHA1-CLAUDE-G63-LANG, génération 1, branche `claude/alpha1/g63-lang-g1`. Base de la mission (manifeste) : `d1a488ad4f0031d7f2a4b47a0721e89a93475d77`. Base du worktree : `32416a2080e67537641040a81252dec0b3e6d137`. START exécuté sur le premier main contenant l'approbation de la mission (PR #181). Sources figées identiques : empreintes SHA-256 conformes au manifeste. Audit IA : revue distincte d’une validation médicale humaine ; aucune source canonique modifiée.

Horodatage : début non relevé (`date_debut` à `null`, l’heure n’ayant pas été notée au démarrage) ; fin 2026-10-16T06:12:25Z.

## Résumé pour Vial

Les sept fichiers de la leçon ont été lus en entier ; leurs empreintes SHA-256 sont conformes au manifeste. L’audit propose **59 remplacements locaux** (`propositions.json`), tous à ancre unique vérifiée mécaniquement et sans effet sur une notion clinique, et **67 renvois médicaux**. Parmi eux figurent 22 reformulations envisagées puis retirées des propositions applicables parce qu’elles touchent une classification, une population, une portée, une mesure statistique ou une dose. Trois constats sont transmis à l’audit MED.

Aucune reformulation n’affaiblit une obligation clinique : les formulations d’urgence de la section 8 passent à « il faut… ».

## Constats les plus graves

- **Sous-onglet Sémiologie absent** : MAJEUR, bloquant pour la clôture du cours et du lot (AGENTS.md), hors périmètre linguistique, transmis à l’audit MED. `G63_c.html` compte 4 `data-s` (anat, histo, physio, bioch) ; aucun sous-onglet « Sémiologie fondamentale et analytique », et 4 disciplines réelles au lieu de 5.
- **Libellés du glossaire G63.x** : la clé construit « Polynévrite tumorales », « Polynévrite infectieuses… » ; corrigé vers les libellés officiels du tableau de la leçon (G63-LANG-gloss-01 à 06).
- **Contresens apparent de statistique** (`G63_c`, e-2), renvoyé (G63-LANG-RM-29) : « un résultat pathologique manque parfois le risque réel » ; c’est un résultat normal qui manque un risque.
- **Renvois de fond** : généralisation « quelle que soit la maladie de base » contredite en 3.5 (G63-LANG-RM-01), maladie de base N18 présentée comme « neuropathie urémique » (G63-LANG-RM-11), « bilan étendu » défini de deux façons (G63-LANG-RM-19), dose de départ du sujet âgé identique à celle de l’adulte (G63-LANG-RM-42).

## Constats transmis à l’audit MED

- **G63-LANG-HP-01** — sous-onglet Sémiologie absent (voir ci-dessus).
- **G63-LANG-FIG-01** — ORIGINE_INCONNUE, avec réserve : six figures SVG sans légende de provenance ; figures 3 et 4 ouvertes comme les plus proches d’une représentation anatomique. Le contrôle linguistique porte sur le texte des figures, pas sur leur provenance ; lisibilité à 390 px (viewBox 640, figures 3 à 5) à vérifier.
- **G63-LANG-FIG-02** — légende de la figure 5 annonçant des hauteurs proportionnelles ; rapport hauteur/valeur de 17,4 à 18,8.

## Choix différés (non appliqués)

1. Espaces insécables globales (573 ponctuations doubles précédées d’une espace ordinaire, 10 guillemets, milliers).
2. Alternative « fibrillation atriale/auriculaire » : aucune occurrence dans G63.

## Renvois médicaux par fichier

| Fichier | Renvois |
|---|---:|
| chapters/G63/G63_a.html | 20 |
| chapters/G63/G63_b.html | 17 |
| chapters/G63/G63_c.html | 12 |
| chapters/G63/G63_d.html | 8 |
| chapters/G63/G63_pop1.html | 3 |
| glossary/g63.py | 2 |
| chapters/G63/G63_pop2.html | 5 |

Les renvois signalent des formulations posant une causalité, une fréquence, une chronologie ou un degré de certitude, ainsi que les reformulations touchant une notion clinique. L’audit ne dit pas que ces énoncés sont faux : il demande qu’une source lue les établisse.

## Tableau de bord

| Fichier | Propositions |
|---|---:|
| chapters/G63/G63_a.html | 12 |
| chapters/G63/G63_b.html | 15 |
| chapters/G63/G63_c.html | 15 |
| chapters/G63/G63_d.html | 7 |
| chapters/G63/G63_pop1.html | 3 |
| glossary/g63.py | 7 |
| **Total** | **59** |

| Catégorie | Nombre |
|---|---:|
| grammaire | 10 |
| phrase nominale | 9 |
| répétition | 8 |
| lourdeur | 5 |
| syntaxe | 4 |
| anglicisme | 4 |
| ambiguïté | 4 |
| lexique | 4 |
| méta-discours | 2 |
| registre | 2 |
| ponctuation | 1 |
| cohérence terminologique | 1 |
| précision | 1 |
| calque | 1 |
| cohérence | 1 |
| nombres | 1 |
| intitulé | 1 |

## Contrôles mécaniques

- Empreintes SHA-256 des 7 fichiers : conformes au manifeste.
- Unicité : 59 sur 59 `ancien` exactement une fois dans leur fichier ; aucun chevauchement (`verification_unicite.py`).
- Nombres : identiques avant et après, hors « deux à trois » en « 2 à 3 » (OG-05).
- Validation JSON : `python3 -m json.tool`.

## Lacunes

- Aucune source médicale n’a été relue : un audit linguistique ne vérifie pas les faits. Les 67 renvois médicaux sont posés sur la seule lecture du texte, sans avoir ouvert Sommer 2018, Feldman 2019, Julian 2019, Graus 2021, Adams 2016, Arnold 2016, Finnerup 2015, QualiCCare ni les informations professionnelles : « causalité / fréquence / chronologie » signifie « à confirmer dans la source », non « faux ».
- Aucun test en navigateur : l’effet des propositions sur l’affichage n’a pas été mesuré.
- build_medina.audit() n’a pas été exécuté ; la présence d’abréviations sans clé a été contrôlée par recherche textuelle.
- Les choix différés (espaces insécables, fibrillation) ne sont pas traités.
- Les figures n’ont pas été ouvertes en navigateur ; leur texte a été lu dans le SVG.
- Pas de correcteur externe (Antidote, LanguageTool) : lecture intégrale et contrôles mécaniques seulement.
- Correctif de traçabilité : 22 propositions initiales touchant une notion clinique (classification, population, portée, mesure, dose) ont été retirées des propositions applicables et reclassées en renvois médicaux.

## Observations globales

- **G63-LANG-OG-01** — Espaces insécables (différé) : 573 occurrences de ponctuation double précédée d’une espace ordinaire (avant ; : ! ?), 10 guillemets « » sans espace insécable, et séparateurs de milliers absents (2700, 3600, 4200, 100 000). Choix différé par la coordination : aucune proposition.
- **G63-LANG-OG-02** — Alternative « fibrillation atriale/auriculaire » (différé) : Aucune occurrence de « fibrillation » dans les sept fichiers de G63 ; rien à appliquer, choix différé conformément à la consigne.
- **G63-LANG-OG-03** — Noms de genre en italique : « Borrelia » est écrit en romain dans toute la leçon ; la convention typographique demande l’italique. Non proposé (modification de balisage).
- **G63-LANG-OG-04** — Phrases nominales dans les encadrés « À retenir » : Les encadrés clés procèdent par énumération de groupes nominaux (« Reins : adapter… », « Âge et cœur : prudence… »). Choix de style de la leçon ; non modifié pour ne pas affaiblir de consigne clinique.
- **G63-LANG-OG-05** — Unités et nombres : Les propositions ne changent aucune valeur. Seule conversion : « deux à trois fois » en « 2 à 3 fois » dans l’encadré de piège de l’hydroxocobalamine ; les décomptes de chiffres du texte visible de G63_d.html passent de 10 à 11 (« 3 ») et de 11 à 12 (« 2 ») pour cette seule raison.
- **G63-LANG-OG-06** — Abréviations sans clé dans g63.py : CDT, TSH, ANCA, HDL, NMDA, VIH, IgM, IgG, ESMO, QualiCCare et AL n’ont pas de clé dans g63.py mais en ont une dans d’autres glossaires du dépôt (recherche textuelle de la clé dans glossary/*.py). La conformité à build_medina.audit() n’a pas été exécutée.

*Audit IA — revue distincte d'une validation médicale humaine ; aucune source canonique modifiée.*
