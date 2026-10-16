# Audit médical Alpha, tour 1 — G72 « Autres myopathies » (S08)

Mission **ALPHA1-CLAUDE-G72-MED** · branche `claude/alpha1/g72-med-g1` · génération 1.
Base de la mission (manifeste) : `d1a488ad4f0031d7f2a4b47a0721e89a93475d77`. Base du worktree : `32416a2080e67537641040a81252dec0b3e6d137`. START a été exécuté sur le premier `main` qui contient l’approbation de la mission (PR #181). Les sources figées sont identiques : les empreintes SHA-256 des sept fichiers sont conformes au manifeste.
Exécutant : sous-agent Claude Code (voir accusé issue 107) ; modèle et effort conformes au manifeste. Horodatages UTC dans `rapport.json` ; l’heure de début n’a pas été relevée au lancement (première heure observée : 06:08:41Z).

## Synthèse

| Gravité | Nombre |
|---|---|
| BLOQUANT | 0 |
| MAJEUR | 11 (dont C01, **bloquant pour la clôture du cours et du lot**) |
| MINEUR | 10 |
| ENRICHISSEMENT | 3 |

La leçon est riche et, sur la plupart des chiffres, fidèle à ses sources. Nous les avons relues en texte intégral : consensus EAS 2015, Statland 2018, Rodriguez 2022, Latronico 2023, Simon 2017, EULAR/ACR 2017 et BfArM 2024. Trois faiblesses dominent pourtant :
- la **sémiologie fondamentale et analytique est absente** ;
- la **pharmacologie n’est pas alignée sur les informations professionnelles suisses** : il manque une contre-indication, les plafonds de dose et les statuts hors étiquette, et les doses de potassium dépassent les maxima de la FI ;
- un **contresens chiffré** porte sur la récupération de la myopathie alcoolique : les 85 % désignent une proportion de patients et non un gain de force.

Aucune erreur n’atteint le seuil d’une conduite dangereuse inventée. Les doses de potassium proviennent d’une revue publiée, mais elles doivent être replacées sous la FI suisse.

## Constats MAJEURS

1. **C01 — Sémiologie absente. MAJEUR, bloquant pour la clôture du cours et du lot (AGENTS.md).** Le bouton `g72-s-semio` et sa discipline n’existent pas. La grille est négative sur SEM-01 à 04, SEM-08 et SEM-13. Un sous-onglet conforme au contrat est proposé dans `propositions/G72_c_1.html` (bouton `g72-tab-semio`, panneau `role="tabpanel"`, neuf sections `data-semiology` titrées en `h3`, sources reliées par liens https), avec une figure non anatomique lisible à 390 px ; ses cinq fenêtres sont dans `propositions/G72_pop2_3.html` (cible `G72_pop2.html`) et le marqueur clinique `data-semiology-clinical="G72"` dans `propositions/G72_a_semio_clinique.html` (cible `G72_a.html`, pA).
2. **C02 — Quatre disciplines seulement.** `tests/audit_sciences.py` échoue avec cinq erreurs : aucun « À retenir » et une histologie de 265 mots. Une cinquième discipline, **Immunologie**, est proposée dans `G72_c_2.html`. Elle explique la forme anti-HMGCR, la myosite sous inhibiteur de point de contrôle et l’absence d’infiltrat dans la myopathie de réanimation.
3. **C03 — Interactions de l’atorvastatine incomplètes (FI avril 2025).** L’association au glécaprévir/pibrentasvir est **contre-indiquée**. Les plafonds sont de 10 mg/j avec la ciclosporine et de 20 mg/j avec le letermovir. Il faut éviter le gemfibrozil. Avec la daptomycine, la FI demande une interruption temporaire ou une CK deux à trois fois par semaine.
4. **C04 — Posologie de la statine déclarée absente, alors que la FI la donne.** La dose initiale est de 10 mg, la dose maximale de 80 mg, avec un palier d’au moins 4 semaines. Si une CK supérieure à 5 fois la limite se confirme avant traitement, la statine n’est pas commencée.
5. **C05 — Potassium au-delà des FI suisses.**

   | Voie | Dose du cours (revue de 2018) | Maximum de la FI suisse |
   |---|---|---|
   | Orale | 250 mmol/j | 150 mmol/j |
   | Intraveineuse | 20 mmol/h | 10 mmol/h et 40 mmol/L si K⁺ > 2,5 mmol/L |

   Le mannitol à 5 % n’est pas enregistré en Suisse.
6. **C06 — Usages hors étiquette non signalés.** Le rituximab, les IgIV, l’abatacept, le salbutamol et l’hydrochlorothiazide sont dans ce cas ; les FI suisses datées ont été vérifiées. Les conditions de prise en charge de ces emplois ne sont fondées sur aucune source suisse lue : elles restent en lacune.
7. **C07 — Le chiffre de « 85 % » est faux à quatre endroits, dont le `div.key`.**
8. **C08 — Alternatives aux statines obsolètes.** L’acide bempédoïque manque (Nilemdo, indiqué en cas d’intolérance aux statines ; ESC/EAS 2025 ; CLEAR Outcomes). Les données en aveugle de la CTT 2022 manquent aussi : plus de 90 % des plaintes ne sont pas dues à la statine.
9. **C09 — « Ptosis → myasthénie » est trompeur sous immunothérapie.** Le ptosis est présent chez 71,8 % des chevauchements publiés, dont la mortalité avoisine 40 %. L’évaluation cardiaque n’est pas prévue.
10. **C10 — Acétazolamide.** La réponse globale est de 46 %. Le cours omet l’aggravation possible avec une mutation de *SCN4A*.
11. **C11 — Figures 1 et 2.** Ce sont une silhouette et une coupe histologique dessinées par IA, sans original. Le cas relève de la règle de Vial ; la recherche sur Commons a été refusée (HTTP 429).

## Constats MINEURS

| Constat | Objet |
|---|---|
| M01 | Figures illisibles à 390 px : texte de 7,3 px ; deux lignes tronquées dans la figure 3 |
| M02 | Statland présenté tantôt comme « européen », tantôt comme « américain » |
| M03 | KCNJ18 : mauvais dénominateur |
| M04 | Antiarythmiques dans l’Andersen-Tawil : la source dit « avec prudence », le cours dit « à éviter » |
| M05 | Sarcoïdose codée M63.3* et non G72 |
| M06 | Critères de la myopathie de réanimation : « au moins deux nerfs » et « sans bloc de conduction » manquent |
| M07 | ABCDEF : les lettres sont développées dans Latronico 2023 |
| M08 | Critères de soutien des paralysies périodiques incomplets |
| M09 | Contre-indications Diamox incomplètes |
| M10 | Causalités et « notions de base » non sourcées |

## Enrichissements

| Enrichissement | Objet |
|---|---|
| E01 | Diurétiques épargneurs de potassium en prévention |
| E02 | Effet nocebo (CTT 2022) |
| E03 | Spécificités suisses et points PROFILES, sans source lue (lacune) |

## Rubrique 21 — Sémiologie fondamentale et analytique

**Statut : absente. Constat C01, MAJEUR, bloquant pour la clôture du cours et du lot.**

| Critère | Résultat | Critère | Résultat |
|---|---|---|---|
| SEM-01 | non | SEM-13 | non (`alert` présent dans l’onglet 1 seulement) |
| SEM-02 | non | SEM-14 | partiel |
| SEM-03 | non (audit_sciences échoue) | SEM-15 | non |
| SEM-04 | OK pour le fichier actuel | SEM-16 | non |
| SEM-05 | non | SEM-17 | non |
| SEM-06 | non | SEM-18 | non |
| SEM-07 | non | SEM-19 | sans objet |
| SEM-08 | non | SEM-20 | sans objet |
| SEM-09 | non | SEM-21 | sans objet |
| SEM-10 | partiel | SEM-22 | sans objet |
| SEM-11 | non | SEM-23 | non |
| SEM-12 | non | SEM-24 | oui |

Aucune sensibilité ni spécificité des signes ne figure dans les sources lues. La proposition l’écrit explicitement.

Réserve : Le validateur exige au moins six boutons data-s dans pS : 4 existants, plus l'Immunologie (G72_c_2), plus la Sémiologie (G72_c_1) = 6. Les deux propositions doivent être intégrées ensemble.

## Correctifs de la revue Codex (PR #195)

- **A — Contrat de sémiologie.** Proposition restructurée selon le contrat et le validateur ; fenêtres déplacées vers `_pop2` ; marqueur clinique proposé pour pA.
- **B — Réflexes conservés.** Reformulé fidèlement à S17 : ils font évoquer une autre cause et n’écartent pas à eux seuls une paralysie périodique.
- **C — Garantie de prise en charge.** Exigence retirée de `G72_d_3.html` ; lacune maintenue.
- **D — Registre des sources.** Les 29 entrées de `sources.json` portent tous les champs exigés ; les inconnues sont déclarées.

## Matrice des 20 rubriques (résumé)

- **Couvertes :** 1, 3, 6, 10, 13, 14, 17, 19.
- **Partielles :** 2, 4, 5, 7, 8, 9, 11, 12, 15, 18, 20.
- **Absente :** 16 (spécificités suisses).

Le détail des ancres figure dans `rapport.json`.

## Lacunes principales

- La recommandation ESMO 2022 est inaccessible (HTTP 403).
- Les tableaux ESC/EAS 2025 sont publiés en image ; la classe et le niveau de preuve n’ont pas été lus.
- Commons a répondu HTTP 429.
- L’index alphabétique de la CIM-10-GM n’a pas été consulté.
- Plusieurs FI n’ont pas été lues : triamtérène, spironolactone, éplérénone, corticoïdes, Praluent, Leqvio.
- Neuf sources du cours n’ont pas été relues : Solé, Allenbach, Hunziker et autres.

## Tableau de bord

| Élément | Valeur |
|---|---|
| Leçon | G72 — Autres myopathies (S08) |
| Fichiers lus | 7/7 en entier ; empreintes conformes au manifeste |
| Contrôles | `test_v7 --static` OK ; `audit_sciences` en échec (5 erreurs) |
| Sources lues | 29, dont 15 FI suisses datées et 7 en texte intégral |
| Propositions | 13 fichiers dans `propositions/` (aucun `_pop3`) |
| Figures | 2 ANATOMIQUE_IA, 2 SCHEMA_NON_ANATOMIQUE |
| Alertes | Sémiologie absente (bloquant pour la clôture) ; potassium au-delà des FI ; contre-indication glécaprévir/pibrentasvir absente |

*Audit IA — revue distincte d’une validation médicale humaine ; aucune source canonique modifiée.*
