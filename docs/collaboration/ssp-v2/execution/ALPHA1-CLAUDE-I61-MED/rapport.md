# Audit médical Alpha, tour 1 : I61, hémorragie intracérébrale (S08 Neurologie)

**Mission** : ALPHA1-CLAUDE-I61-MED · **Branche** : `claude/alpha1/i61-med-g1` · **Base** : `f664dd9e` (sources figées `bfc4576b`) · **Génération** : 1
**Exécutant** : sous-agent Claude Code (voir l’accusé de l’issue 107) · **Modèle et effort** : conformes au manifeste · **Date** : 15 octobre 2026

> Audit IA. Cette revue est distincte d’une validation médicale humaine. Aucune source canonique n’a été modifiée : les corrections sont des propositions, dans `propositions/`.

## 1. Lecture et intégrité

Les sept fichiers de la leçon ont été lus en entier : texte, tableaux, figures, quiz, fenêtres, Pareto, `div.alert`, `div.key` et glossaire. Leurs SHA-256 recalculées sont **conformes au manifeste** (7 sur 7). Le découpage réel diffère des intitulés attendus :

- `_a` contient la Pathologie, § 1 à 6 ;
- `_b` contient la Pathologie, § 7 à 12, et les références ;
- `_c` contient les Examens complémentaires, puis les Sciences fondamentales ;
- `_d` contient la Pharmacologie.

**Première source lue** : le protocole du réseau AVC bernois (version 08/2026), page 44-45 du document : chapitre « Non-traumatic intracerebral hemorrhage », schéma A-B-C-D et schéma de réversion [S1].

## 2. Appréciation générale

La leçon est solide. Ses chiffres suisses ont été recalculés sur les sources primaires et sont exacts :

- l’étude genevoise : 13,2/100 000, létalité de 32,5 % ;
- le registre suisse : 46,7 % d’hypertension, 39,1 % d’indépendance, 25,1 % de décès, rapports de cotes 1,33, 1,62 et 3,38 ;
- CADMUS, l’essai ANNEXA-I selon la FI suisse, les critères de Boston 2.0 et la méta-analyse de 2026 sur l’acide tranexamique.

Les doses de réversion du protocole bernois, les critères d’éligibilité de l’andexanet et de l’idarucizumab, les seuils tensionnels bernois et le seuil préhospitalier de 220 mmHg sont aussi conformes. Il en va de même pour les recommandations ESO sur l’évacuation cérébelleuse (> 15 ml, OR 0,44), la chirurgie mini-invasive (OR 0,49), la craniectomie décompressive (critères de SWITCH, 72 h), la dérivation ventriculaire externe et la prophylaxie antiépileptique.

**Aucune erreur bloquante** n’a été trouvée. Les faiblesses tiennent surtout à **une divergence suisse–européenne non signalée** sur un geste d’urgence, à **un écart avec la FI** pour une dose d’antidote et à **deux contresens de lecture** des sources.

## 3. Constats par gravité

### MAJEUR (5)

| Id | Fichier | Constat | Proposition |
|---|---|---|---|
| MED-01 | `_b` § 9.2 | Le cours dit le PCC « inefficace » dans l’hémorragie sous anticoagulant oral direct. C’est la position bernoise ; l’ESO 2025 admet le PCC après pesée du risque thrombotique (consensus 15/15) [S1, S2]. | `I61_b_1.html` : attribuer à Berne et ajouter un encadré de divergence |
| MED-02 | `_c` quiz § 3.3 | La même règle devient absolue dans le quiz et dans l’encadré « À retenir ». | `I61_c_1.html` |
| MED-03 | `_pop2` Pareto e03 | La même règle figure dans le Pareto. | Formulation attribuée (dans `rapport.json`) |
| MED-04 | `_pop1` i61-andexanet | Après plus de 10 mg de rivaroxaban pris il y a moins de 8 h, la FI suisse impose la dose élevée. Elle précise aussi que la faible dose n’a jamais été évaluée avec le rivaroxaban. Le cours renvoie au « protocole local » [S4]. | `I61_pop1_1.html` |
| MED-18 | `_c` § 4.1 | Contresens sur les critères d’Édimbourg : la règle d’exclusion (ni hémorragie sous-arachnoïdienne ni ε4) a bien une **sensibilité de 100 %** (IC 88-100). Le cours affirme l’inverse [S7]. | `I61_c_2.html` |

Commencez par MED-01 : ce choix se pose dès qu’un critère de l’andexanet manque, par exemple au-delà de 6 h. Un étudiant qui retient « jamais de PCC » se trompe dans un centre qui suit l’ESO.

### MINEUR (9)

| Id | Fichier | Constat |
|---|---|---|
| MED-05 | `_b` tableau de réversion | « Faible dose préférée par Berne » ne rappelle pas les cas où la FI impose la dose élevée. |
| MED-06 | `_a` § 6.1 | Le registre suisse utilise des catégories **mutuellement exclusives**, sans hiérarchie stricte ; le cours dit que « les causes ne s’excluent pas » [S14]. |
| MED-07 | `_a` § 3.2 | La récidive hémorragique dépasse l’infarctus en cas d’angiopathie amyloïde **et** de cause inconnue ; le cours écrit « seulement » l’angiopathie amyloïde. |
| MED-08 | `_a` § 3.4 | Les chiffres mondiaux (3,41 M de cas et 2,89 M de décès) ne sont pas sourcés. L’ESO donne environ 3,4 M et 2,8 M [S2]. |
| MED-09 | `_pop1` i61-diagram, `_c` | L’« arbre DIAGRAM » est en réalité l’arbre de Wilson 2017. Les c-statistiques 0,83 → 0,66 appartiennent au score DIAGRAM de Hilkens 2018, qui garde 0,88 avec l’angio-scanner. L’arbre de Wilson vient d’une cohorte sélectionnée (âge médian 49 ans, 45 % de causes macrovasculaires) [S8, S9]. |
| MED-10 | glossaire | DIAGRAM est attribué à Wilson ; le sigle n’est pas développé. |
| MED-11 | glossaire | CADMUS est déclaré « non développé », alors que la source en donne les initiales [S15]. |
| MED-17 | `_c` quiz | « Le seuil de 30 ml concerne la pression artérielle » est inexact : c’est le seuil du score ICH. |
| MED-19 | `_pop1` i61-boston | Les valeurs 74,5 % / 95,0 % concernent le sous-ensemble autopsique, pas les 341 participants. |

### ENRICHISSEMENT (5), propositions rédigées et sourcées

| Id | Ajout | Fichier de proposition |
|---|---|---|
| MED-12 | PRESTIGE-AF : infarctus 0,83 contre 8,60 et récidive d’HIC 5,00 contre 0,82 pour 100 patients-années ; marqueurs IRM de récidive (sidérose superficielle, HR 7,7) [S10, S11] | `I61_b_3.html` |
| MED-13 | ANNEXA-I selon la FI : sans prophylaxie, 22,8 % de thromboses contre 7,7 % ; avec prophylaxie, 4,9 % contre 4,8 %. L’HBPM est de nouveau efficace 4 h après l’andexanet [S4]. | `I61_b_4.html` |
| MED-14 | Analyse poolée INTERACT (11 312 patients) : OR 0,85 ; bénéfice nul vers 3 h. Pas d’abaissement préhospitalier systématique [S3]. | `I61_b_5.html` |
| MED-15 | Surmortalité à 3 mois sous antivitamine K (OR 1,71) et sous anticoagulant oral direct (OR 1,28) [S13] | `I61_a_4.html` |
| MED-16 | Transfusion plaquettaire : décès ou dépendance, OR 2,04 (1,12-3,74) [S2] | `I61_b_6.html` |

## 4. Matrice des 20 rubriques (leçon actuelle)

| # | Rubrique | Statut | Où |
|---|---|---|---|
| 1 | Question clinique, enjeu de l’examen | couvert | `_a` #i61-a01-partie-1 |
| 2 | Définition, CIM-10-GM | couvert | `_a` § 2 ; fenêtre i61-sous-codes |
| 3 | Classifications | couvert | `_a` § 2.2, § 6.1 ; i61-boston |
| 4 | Épidémiologie | couvert | `_a` § 3 (chiffres mondiaux non sourcés) |
| 5 | Normal → pathologique | couvert | `_a` § 4 ; Sciences |
| 6 | Étiologies, facteurs de risque | partiel | facteurs modifiables hors hypertension absents |
| 7 | Anamnèse, fréquences | partiel | `_b` § 8.1, sans fréquences |
| 8 | Examen clinique | partiel | `_b` § 8.2, sans sensibilité ni spécificité |
| 9 | Drapeaux rouges | couvert | `_b` § 8.2, § 9 ; i61-htic |
| 10 | Examens complémentaires | couvert | `_c` Examens |
| 11 | Diagnostic différentiel | couvert | `_b` § 7 |
| 12 | Prise en charge suisse | couvert | `_b` § 9 ; `_d` (MED-01 à 04) |
| 13 | Complications, pronostic | couvert | `_b` § 10 (mortalité par point du score ICH : lacune) |
| 14 | Suivi, prévention | partiel | `_b` § 10.5 (PRESTIGE-AF absent) |
| 15 | Situations particulières | couvert | `_b` § 11 |
| 16 | Spécificités suisses | partiel | conduite automobile d’origine allemande ; AI et LAA absentes |
| 17 | Critères formels (`div.alert`) | couvert | `_b` § 12.1 |
| 18 | Paramètres clés (`div.key`) | couvert | `_b` § 12.2 |
| 19 | Sous-codes | couvert | i61-sous-codes |
| 20 | Points d’examen fédéral | partiel | quiz ; PROFILES non officiel |

## 5. Lacunes de l’audit (déclarées, non comblées)

- **L-01** : la mortalité par point du score ICH. Seul le résumé de Hemphill 2001 est accessible.
- **L-02** : plusieurs consensus ESO 2025 n’ont pas été vérifiés. Ce sont le PCC à 10 UI/kg pour un INR de 1,3 à 1,9, la fermeture de l’auricule (PICO 6.3), les statines et la reprise des antiplaquettaires. La page PMC était tronquée et protégée par un captcha ; aucun constat n’est émis sur ces points.
- **L-03** : le plancher européen de 110 mmHg n’a pas été retrouvé dans le texte lu. Il figure probablement dans un encadré en image.
- **L-04 et L-05** : les facteurs de risque modifiables et le cadre suisse de la conduite et des assurances n’ont pas été recherchés.
- **L-06** : seules les FI d’Ondexxya et de Praxbind ont été relues. Les doses des autres produits n’ont pas été contre-vérifiées par cet audit.

## 6. Tableau de bord

| Élément | Valeur |
|---|---|
| Leçon | I61, hémorragie intracérébrale (S08 Neurologie) |
| Fichiers audités | 7, empreintes conformes |
| BLOQUANT / MAJEUR / MINEUR / ENRICHISSEMENT | 0 / 5 / 9 / 5 |
| Sources lues | 18 : 7 suisses (Berne, deux FI Swissmedic, registre suisse, registres suisse-norvégien, Genève, Kägi), 3 européennes (ESO–EANS 2025, ESO pression artérielle 2026, PRESTIGE-AF), puis revues et études |
| Propositions rédigées | 15 fichiers dans `propositions/` |
| Ancres vérifiées mécaniquement | 19 sur 19, chacune présente une seule fois |
| Alerte principale | La divergence entre Berne et l’ESO sur le PCC dans l’hémorragie sous anti-Xa doit être enseignée explicitement (MED-01 à 03) |

*Audit IA. Cette revue est distincte d’une validation médicale humaine. Aucune source canonique n’a été modifiée.*
