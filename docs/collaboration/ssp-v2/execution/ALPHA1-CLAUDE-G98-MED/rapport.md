# Audit médical ALPHA77 — G98, arthropathie de Charcot (S08)

Mission `ALPHA1-CLAUDE-G98-MED` · branche `claude/alpha1/g98-med-g1` · base `103745baaa38c76f18288758cc7f689e5091ccdb` · génération 1 · exécutant : sous-agent Claude Code (voir accusé issue 107) · modèle et effort : conforme au manifeste.
Début (premier téléchargement de source) 2026-10-16T09:54:06Z · fin 2026-10-16T10:15:57Z. Empreintes SHA-256 des 7 fichiers : **conformes au manifeste**.

> Audit IA — revue distincte d’une validation médicale humaine ; aucune source canonique modifiée.

## Synthèse

La leçon est solide sur l’essentiel décisionnel : codage croix-étoile exact, recommandations IWGDF 2023 reprises avec leurs forces et certitudes, décharge immédiate jusqu’au genou, IRM devant des radiographies normales, interdiction des antirésorptifs, posologies de l’énoxaparine conformes à la FI suisse de février 2026. Aucune erreur dangereuse n’a été trouvée : **0 BLOQUANT**.
Elle présente en revanche **5 constats MAJEURS** : l’absence du sous-onglet de sémiologie exigé par Vial, des sciences fondamentales sans normal ni figure (le contrôle automatique échoue), deux calculs faux sur des données décisionnelles (conversion 2 °C = 4 °F ; taux d’amputation de 52 % rapporté à un mauvais dénominateur), et l’omission des causes non diabétiques, qui sont précisément la population codée G98† : dans la cohorte suisse du Balgrist, 29,9 % des pieds de Charcot n’étaient pas diabétiques. S’y ajoutent **12 MINEURS** et **5 ENRICHISSEMENTS**, tous rédigés et sourcés dans `propositions/`.

## Calculs (exigence « ne laisse rien passer »)

Toutes les valeurs ont été inventoriées par script (`calculs/verifier.py`, conservé et réexécutable : `python3 calculs/verifier.py <racine du worktree>`), puis rapprochées une à une d’une règle de recalcul ou d’une valeur lue dans la source primaire. Le script échoue si une seule grandeur reste sans règle.

| Indicateur | Valeur |
|---|---|
| Occurrences relevées (chiffres + toutes lettres) | 349 |
| Étiquettes non calculables (stades, niveaux, numéros, années) | 126 |
| Grandeurs calculables | 223 |
| Recalculées ou rapprochées | 223 |
| Correctes | 213 |
| Arrondi | 0 |
| Fausses | 8 |
| Non vérifiables | 2 |
| Calculs propres aux propositions de l’audit | 12 (tous corrects) |

| Occurrence | Fichier | Valeur | Attendu | Verdict | Constat |
|---|---|---|---|---|---|
| N032 | G98_a.html | 0,1 | 0.1 | NON_VERIFIABLE | C20 |
| N033 | G98_a.html | 13 | 13.0 | NON_VERIFIABLE | C20 |
| N042 | G98_a.html | 30,1 | 30.82 | FAUX | C05 |
| N050 | G98_a.html | 72,3 | 72.28 | FAUX | C06 |
| N061 | G98_b.html | 4 | 3.6 | FAUX | C03 |
| N089 | G98_b.html | 52 | 60.47 | FAUX | C04 |
| N182 | G98_d.html | 70 | 70 | FAUX | C07 |
| N211 | G98_pop1.html | 4 | 3.6 | FAUX | C03 |
| N218 | G98_pop1.html | 52 | 60.47 | FAUX | C04 |
| N282 | G98_pop2.html | 70 | 70 | FAUX | C07 |

`recalcules = calculables` : la partie calculs est close. La valeur p = 0,0012 de la série de Düsseldorf concorde avec la source, mais son recalcul exact est impossible (effectifs du médio-pied par stade non publiés dans le résumé).

## Constats par gravité

### BLOQUANT (0)

Aucun.

### MAJEUR (5)

- **C01** — `G98_c.html` — Le sous-onglet « Sémiologie fondamentale et analytique » est absent. Décompte réel des data-s de G98_c.html : 3 (g98-s-anat, g98-s-bio, g98-s-img) ; aucun g98-s-semio, aucun data-semiology ni data-semiology-clinical. La sémiologie existante se limite à l'îlot g98-7 (« Anamnèse et examen », 1 mot vert : g98-thermometrie) : pas de tableau des signes, pas de technique du monofilament ni du diapason, pas d'examen vasculaire, pas de regroupement syndromique, pas de raisonnement en cinq étapes, pas de cas corrigé consacré au signe.  
  *Preuves* : [S1] Recommandation 1 et justification ; [S13] Annexe 1 ; [S3] PCA, Examen clinique. *Proposition* : propositions/G98_c_semio.html (bouton g98-tab-semio, panneau g98-s-semio, neuf sections data-semiology, figure non anatomique, 3 cas corrigés) ; propositions/G98_b_semio_clinique.html (section data-semiology-clinical="G98" dans g98-7) ; propositions/G98_pop1_semio.html (7 fenêtres g98-sm-*).
- **C02** — `G98_c.html` — Sciences fondamentales non conformes : tests/audit_sciences.py --codes G98 échoue (14 erreurs) : 0 figure dans les 3 disciplines, aucun des encadrés « Science → clinique. / examen. / traitement. », g98-s-anat (259 mots) et g98-s-img (241 mots) sous 280 mots. Le normal n'est pas exposé (« Les sources lues ne détaillent pas le remodelage osseux normal et le cours ne l'expose pas »), alors que S2 donne les valeurs radiographiques normales de l'arche et S1 la symétrie thermique normale. La leçon entière ne contient aucune figure.  
  *Preuves* : [S2] Role of conventional radiographs ; [S1] Justification des recommandations 1 à 5. *Proposition* : propositions/G98_c_sciences.html (normal radiographique, figures originales CC BY 4.0 de S2 à héberger après contrôle visuel, chaîne causale non anatomique, encadrés de corrélation dans chaque discipline).
- **C03** — `G98_b.html` — Conversion fausse d'un seuil décisionnel (calcul N061, N211) : pour un écart de température, ΔT(°F) = 1,8 × ΔT(°C) ; 2 °C = 3,6 °F et 4 °F = 2,22 °C. La source corrige elle-même l'équivalence. Même erreur dans la fenêtre g98-thermometrie (G98_pop1.html : « Une différence de 2 °C (4 °F) »).  
  *Preuves* : [S1] Justification des recommandations 1 à 5 ; [S1] Identification de la rémission. *Proposition* : propositions/G98_corrections.html, bloc C03 (deux remplacements).
- **C04** — `G98_b.html` — Dénominateur faux (calcul N089, N218) : 52 % correspond à 31 épisodes d'ostéomyélite sur 60 (51,7 %) ; rapporté aux 43 pieds, le taux est 26/43 = 60,5 %, aux 40 patients 26/40 = 65 %. La leçon omet en outre que le taux d'amputation n'était pas plus élevé dans la zone de Charcot (12/30 = 40 % contre 19/30 = 63 % hors zone, p = 0,09) ; seuls le niveau (majeure 20 % contre 10 %), la durée d'antibiothérapie et d'immobilisation différaient. Même erreur dans la fenêtre g98-osteomyelite.  
  *Preuves* : [S7] Résultats, Amputation rate ; [S7] Résultats ; [S7] Level of amputation. *Proposition* : propositions/G98_corrections.html, bloc C04 (deux remplacements).
- **C22** — `G98_a.html` — Affirmation inexacte sur les sources et lacune centrale du code : deux sources déjà citées par la leçon documentent les causes non diabétiques, c'est-à-dire précisément les Charcot codés G98†. S7 cite l'alcool, la carence en vitamine B12 ou en folates, les drogues intraveineuses, la syphilis tardive, la syringomyélie et la sclérose en plaques ; S6 (cohorte suisse) donne la répartition par pied : 70,1 % diabétiques, 14,7 % idiopathiques, 8,7 % éthylotoxiques, 2,2 % carence en B12, 2,2 % médullaires, 1,6 % inflammatoires, 0,5 % pharmacotoxique, soit 29,9 % de pieds non diabétiques (recalcul P11).  
  *Preuves* : [S7] Background ; [S6] Tableau 1, Cause of Neuropathy ; [S6] Introduction. *Proposition* : propositions/G98_a_etiologies.html.

### MINEUR (12)

- **C05** — `G98_a.html` — Calcul N042 : 49/159 = 30,82 %. Le résumé de la source imprime 30,1 %, son texte et son tableau 1 donnent 30,8 % : la leçon reprend l'erreur du résumé.  
  *Preuves* : [S6] Résultats et tableau 1. *Proposition* : propositions/G98_corrections.html, bloc C05.
- **C06** — `G98_a.html` — Calcul N050 : 72,3 % = 133/184 PIEDS, non des patients ; « la récidive 13,6 % » désigne la réactivation de 25/184 pieds.  
  *Preuves* : [S6] Ulcers and ulcer recurrence ; [S6] Reactivation. *Proposition* : propositions/G98_corrections.html, bloc C06.
- **C07** — `G98_d.html` — Calcul N182, N282 : la FI suisse ne demande pas de surveillance propre au sujet de plus de 70 ans en prophylaxie ; elle situe le risque hémorragique accru du sujet âgé « en particulier de plus de 70 ans » dans la fourchette THÉRAPEUTIQUE et précise que la prophylaxie ne s'accompagne pas d'une tendance accrue aux saignements. Même formulation dans la fenêtre g98-enoxaparine (G98_pop2.html).  
  *Preuves* : [S10] Mises en garde, Patients âgés. *Proposition* : propositions/G98_d_enoxaparine.html, bloc C07.
- **C08** — `G98_a.html` — La série de 71 cas provient de la consultation du pied diabétique de l'Université de Düsseldorf (Allemagne) ; elle est seulement publiée dans le Swiss Medical Weekly. « documenté en Suisse » (g98-0) et « série suisse-allemande » (g98-8, g98-10, correction du cas 5 en g98-e-5) sont inexacts. g98-4 l'attribue correctement à Düsseldorf.  
  *Preuves* : [S4] Affiliation (Europe PMC). *Proposition* : propositions/G98_corrections.html, bloc C08 (quatre remplacements).
- **C09** — `G98_a.html` — Une version 2023 (allemand) du document suisse existe ; elle qualifie l'IRM de « zwingend » (obligatoire) en deuxième ligne et admet le plâtre à contact total amovible comme alternative. La leçon ne cite que la version française 2020.  
  *Preuves* : [S14] ACF, Bildgebung ; [S14] ACF, Behandlung. *Proposition* : propositions/G98_corrections.html, bloc C09.
- **C11** — `G98_b.html` — Formulation catégorique : la source suisse écrit « n’est pas recommandée » (fixation interne) et « n’est en général pas recommandable » (chirurgie sans ulcère ni déformation instable) ; l'IWGDF admet la chirurgie à peau intacte en cas de douleur non contrôlée ou de déformation à haut risque d'ulcère, après une période de traitement conservateur.  
  *Preuves* : [S3] PCC, Traitement chirurgical ; [S1] Justification de la recommandation 24. *Proposition* : propositions/G98_corrections.html, bloc C11.
- **C12** — `G98_b.html` — Incohérence de seuil (SEM-20) : « ≥ 2 °C » (paramètres clés g98-14) contre « plus de 2 °C » (g98-7, S3) et « 2 °C » (S1) ; l'IWGDF précise que la précision diagnostique de ce seuil n'a jamais été démontrée.  
  *Preuves* : [S3] PCA, Examen clinique ; [S1] Recherche future. *Proposition* : propositions/G98_corrections.html, bloc C12.
- **C13** — `G98_b.html` — L'IWGDF parle d'un stimulateur « non compatible avec l'IRM » ; la revue du Balgrist d'une claustrophobie « sévère ». Même formulation en g98-e-4 (G98_c.html).  
  *Preuves* : [S1] Justification de la recommandation 9 ; [S2] CT and nuclear medicine imaging. *Proposition* : propositions/G98_corrections.html, bloc C13.
- **C18** — `G98_b.html` — Surinterprétation : l'IWGDF « suggère de ne pas utiliser » la biologie (recommandation conditionnelle, certitude faible) ; « inutile » est plus fort que la source.  
  *Preuves* : [S1] Recommandation 10. *Proposition* : propositions/G98_corrections.html, bloc C18.
- **C19** — `G98_b.html` — Le chiffre de 23 % vient d'une étude citée par la revue du Balgrist ; la cohorte suisse elle-même donne 13,6 % des pieds (délai médian 1,9 an), plus fréquente chez le diabétique de type 1 (6/18) que de type 2 (15/113). Les deux chiffres coexistent sans être reliés.  
  *Preuves* : [S2] Natural course of disease ; [S6] CN reactivation. *Proposition* : propositions/G98_corrections.html, bloc C19.
- **C20** — `G98_a.html` — Valeurs N032 et N033 NON_VERIFIABLE : le résumé de Gastaldi et coll. 2013 ne contient pas cette fourchette ; le texte intégral n'a pas été lu par l'audit.  
  *Preuves* : [S11] Résumé. *Proposition* : propositions/G98_corrections.html, bloc C20.
- **C21** — `G98_b.html` — Critère d'arrêt présenté comme général alors qu'il s'agit de la pratique du Balgrist ; les recommandations pratiques de l'IWGDF retiennent l'absence de signe clinique d'inflammation et la consolidation radiographique, et notent que l'IRM peut rester anormale après la résolution clinique.  
  *Preuves* : [S2] Monitoring of disease activity with MRI ; [S13] Section 5. *Proposition* : propositions/G98_corrections.html, bloc C21.

### ENRICHISSEMENT (5)

- **C10** — `G98_d.html` — La prophylaxie antithrombotique recommandée dure aussi longtemps que le plâtre (souvent 3 à 6 mois) ; la leçon ne donne aucun des points de sécurité que la FI suisse prévoit pour une héparine de bas poids moléculaire prolongée : numération plaquettaire avant et pendant le traitement (thrombopénie induite par l'héparine entre le 5e et le 21e jour), contre-indication en cas d'antécédent de moins de 100 jours, prudence en cas de rétinopathie diabétique, exposition accrue en cas de sous-poids. Aucune donnée d'efficacité indirecte n'est citée.  
  *Preuves* : [S10] Mises en garde, Surveillance de la numération plaquettaire ; [S10] Contre-indications relatives ; [S15] Résumé. *Proposition* : propositions/G98_d_enoxaparine.html, bloc C10.
- **C14** — `G98_b.html` — Rubrique 16 (spécificités suisses) absente : prise en charge AI/AVS des chaussures orthopédiques, aptitude à la conduite sous plâtre. L'audit n'a pu lire que la table des matières d'une circulaire AI non en vigueur (CMAI, état 2021, chiffres 4.01 à 4.04 OMAI) : aucune règle n'est proposée.  
  *Preuves* : [S16] Table des matières. *Proposition* : propositions/G98_b_decharge_suisse.html, bloc C14 (précision de la lacune).
- **C15** — `G98_c.html` — L'onglet Examens ne donne aucune valeur normale de radiographie, alors que S2 fournit les mesures normales de l'arche (Meary, hauteur du cuboïde, pente calcanéenne) et leur évolution dans le Charcot.  
  *Preuves* : [S2] Role of conventional radiographs. *Proposition* : propositions/G98_c_examens.html, bloc C15.
- **C16** — `G98_c.html` — Valeur diagnostique des imageries du Charcot actif absente : IRM à sensibilité élevée mais spécificité inconnue ; scintigraphie en trois temps sensibilité 89 %, spécificité 58 % (148 patients) ; imagerie nucléaire négative fortement contre le diagnostic.  
  *Preuves* : [S1] Justification des recommandations 8 et 9. *Proposition* : propositions/G98_c_examens.html, bloc C16.
- **C17** — `G98_b.html` — Effets indésirables de l'immobilisation prolongée et non-observance de l'appui partiel non traités (72 % de non-observance, 34 jours de guérison supplémentaires ; atrophie, chutes, inégalité de longueur et surélévation controlatérale) ; remise en charge progressive non mentionnée.  
  *Preuves* : [S1] Justification des recommandations 15 à 20 ; [S1] Prévention de la réactivation. *Proposition* : propositions/G98_b_decharge_suisse.html, bloc C17.

## Rubrique 21 — Sémiologie fondamentale et analytique

**Statut : absente (MAJEUR, C01).** Décompte des `data-s` de `G98_c.html` : 3 (g98-s-anat, g98-s-bio, g98-s-img) ; aucun `g98-s-semio`. La sémiologie existante tient dans l’îlot g98-7 (un seul mot vert). Valeurs disponibles : Aucune sensibilité, spécificité ni rapport de vraisemblance pour la chaleur, l’œdème, la rougeur, la douleur, le monofilament ou le diapason dans le diagnostic du Charcot (S1, S3, S13). Seules valeurs disponibles : concordance du site de l’écart thermique maximal avec la radiographie (92 % au diagnostic, 72 % au suivi) [S1] ; la précision du seuil de 2 °C n’est pas démontrée [S1].

La proposition `G98_c_semio.html` crée le bouton `g98-tab-semio` et le panneau `g98-s-semio` (neuf sections `data-semiology` : normal, signs, mechanisms, examination, interpretation, differentials, urgency, limits, sources), avec un tableau des signes, l’examen systématique en huit temps, une synthèse présentée, une figure de raisonnement non anatomique et trois cas corrigés (valeur d’un seuil, calcul de l’indice cheville-bras, plaie et urgence). `G98_b_semio_clinique.html` ajoute le marqueur `data-semiology-clinical="G98"` dans g98-7 ; `G98_pop1_semio.html` fournit les sept fenêtres `g98-sm-*`.

| Critère | Leçon actuelle |
|---|---|
| SEM-01 | non |
| SEM-02 | non |
| SEM-03 | non |
| SEM-04 | oui (test_v7.py --static G98 : « G98 mots 11585 fenêtres 28 quiz 6 pareto 7 — OK » sur la leçon actuelle) |
| SEM-05 | non |
| SEM-06 | non |
| SEM-07 | non |
| SEM-08 | non |
| SEM-09 | non |
| SEM-10 | non |
| SEM-11 | non |
| SEM-12 | non |
| SEM-13 | non (pas d’alert sémiologique ; l’alert g98-9 existe) |
| SEM-14 | non |
| SEM-15 | non |
| SEM-16 | non |
| SEM-17 | non |
| SEM-18 | non |
| SEM-19 | non évaluable (absente) |
| SEM-20 | non évaluable (absente) ; incohérence ≥/> 2 °C (C12) |
| SEM-21 | non évaluable |
| SEM-22 | non (bouton absent) |
| SEM-23 | non (aucune capture possible) |
| SEM-24 | oui (statut « Revue par intelligence artificielle · Audit différé · Aucune validation médicale humaine ») |

## Matrice des rubriques

| N° | Rubrique | Statut | Ancre |
|---|---|---|---|
| 1 | Question clinique et enjeu pour l’examen fédéral | couvert | g98-0 (vignette, trois questions) |
| 2 | Définition et périmètre CIM-10-GM | couvert | g98-1, g98-2, fenêtre g98-codage ; conformes à S12 |
| 3 | Classifications et stades | partiel | g98-3 ; stade IV de l’Eichenholtz modifié et classification de Brodsky non détaillés |
| 4 | Épidémiologie suisse puis européenne | partiel | g98-4 ; aucune donnée populationnelle suisse (déclaré) ; C05, C06, C20 |
| 5 | Normal → pathologique | partiel | g98-5, sciences : normal non exposé (C02) |
| 6 | Étiologies et facteurs de risque | partiel | g98-6 : causes non diabétiques absentes (C22) |
| 7 | Anamnèse et symptômes (fréquences) | partiel | g98-7 ; aucune fréquence de symptôme (non chiffrée dans les sources lues) |
| 8 | Examen clinique (signes, sensibilité/spécificité) | partiel | g98-7 ; technique et valeur absentes (C01) |
| 9 | Drapeaux rouges et urgences | couvert | g98-9 (alert), g98-0 |
| 10 | Examens complémentaires | partiel | g98-e-1 à e-4 ; valeurs normales et valeur des alternatives absentes (C15, C16) |
| 11 | Diagnostic différentiel (discriminants) | partiel | g98-8 ; discriminants IRM de S2 tableau 1 non exploités hors ostéomyélite |
| 12 | Prise en charge suisse | couvert | g98-9 à g98-11 ; C11 |
| 13 | Complications et pronostic | couvert | g98-4, g98-11 ; C04 |
| 14 | Suivi, prévention, dépistage | couvert | g98-12 ; C19, C21 |
| 15 | Situations particulières | partiel | g98-13 ; enfant et grossesse sans source (déclaré) |
| 16 | Spécificités suisses | partiel | g98-13 (niveaux de soins) ; assurances et conduite non lues (C14) |
| 17 | Critères formels du diagnostic (div.alert) | couvert | g98-14 alert |
| 18 | Paramètres clés chiffrés (div.key) | couvert | g98-14 key ; C12, C18 |
| 19 | Sous-codes CIM-10-GM couverts | couvert | G98 sans sous-code (S12) |
| 20 | Points d’examen fédéral | partiel | pièges g98-13 ; objectifs PROFILES non cités |
| 21 | Sémiologie fondamentale et analytique | absent | aucun sous-onglet g98-s-semio (C01) |

## Figures

La leçon ne contient **aucune figure** (inventaire `image_clo_finder` vide ; ni `figure`, ni `svg`, ni `img`). Aucune figure anatomique produite par une IA n’est donc en cause. Les figures anatomiques proposées sont des originaux de Rosskopf et coll. 2019 (Balgrist), sous licence CC BY 4.0 ; leur téléchargement a été refusé depuis la session, si bien qu’**aucun contrôle visuel n’a été fait** : l’intégrateur doit récupérer, contrôler et attribuer chaque original. Les deux schémas proposés sont des chaînes de raisonnement sans structure anatomique.

## Lacunes

- Texte intégral de Gastaldi et coll., Rev Med Suisse 2013 non lu (fourchette 0,1–13 % non vérifiable) : WebSearch « Gastaldi Ruiz Borens Charcot Revue médicale suisse 2013 » sans accès au texte.
- Séries Chantelau 2013 et 2014, Waibel 2022, Fischer 2026 lues en résumé seulement.
- Version française 2023 du document QualiCCare non trouvée ; seule la version allemande 2023 a été lue.
- Figures candidates (Rosskopf 2019, CC BY 4.0) non contrôlées visuellement : téléchargement refusé (Europe PMC 403, serveur Springer 404).
- Règles AI/AVS des chaussures orthopédiques (OMAI ch. 4.01–4.04 ; circulaire AVS 2024) et aptitude à la conduite sous plâtre : textes en vigueur non lus (rubrique 16).
- Aucune source de sémiologie universitaire suisse (UNIGE, UNIL) consacrée au pied neuropathique trouvée ; la technique d’examen repose sur les recommandations pratiques de l’IWGDF 2023.
- Aucune valeur de sensibilité, spécificité ou rapport de vraisemblance des signes cliniques du Charcot dans les sources lues.
- Version française OFS de la CIM-10-GM 2024 non relue (libellés allemands du BfArM vérifiés).
- tests/audit_sciences.py et test_v7.py n’ont pas été exécutés sur la leçon modifiée par les propositions (aucune écriture canonique autorisée) ; contrôle à faire à l’intégration.
- Hors périmètre médical, signalé au LANG : numérotation des cas pédagogiques non continue (1, 2, 3, 5 en e-5 ; 6 en p-4 ; 4 en p-5).

## Sources

Seize sources ont été consultées le 16 octobre 2026 (registre complet : `sources.json`). Première source lue : QualiCCare / SSED, Pied de Charcot (2020), section « Pied de Charcot aigu : examen clinique et traitement ». Les références de conduite sont suisses (QualiCCare/SSED, FI Swissmedic, cohortes du Balgrist) puis internationales (IWGDF, utilisée comme recommandation internationale) ; aucune recommandation nationale américaine n’est retenue comme conduite.

## Tableau de bord

| Élément | État |
|---|---|
| Leçon | G98 — Autres affections du système nerveux, non classées ailleurs : arthropathie de Charcot (S08) |
| Fichiers audités | 7 (empreintes conformes) |
| Constats | BLOQUANT 0 · MAJEUR 5 · MINEUR 12 · ENRICHISSEMENT 5 |
| Calculs | 349 relevés · 223 calculables · 223 recalculés · 8 faux · 2 non vérifiables |
| Sémiologie | absente (MAJEUR) ; proposition complète en 3 fichiers |
| Contrôles | test_v7 --static : OK · audit_sciences : échec (C02) · figures : 0 |
| Propositions | 9 fichiers dans `propositions/` |
| Alerte | Aucune validation médicale humaine ; propositions à intégrer par une mission d’enrichissement approuvée |
