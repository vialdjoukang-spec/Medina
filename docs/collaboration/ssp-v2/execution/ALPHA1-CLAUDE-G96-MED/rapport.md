# Audit médical Alpha, tour 1 — G96 « Autres affections du système nerveux central : fuites de liquide céphalorachidien » (S08)

Mission **ALPHA1-CLAUDE-G96-MED** · branche `claude/alpha1/g96-med-g1` · génération 1.
Base du worktree : `103745baaa38c76f18288758cc7f689e5091ccdb`. Le manifeste fige les sources à `523832d9ef6097607d3443f4398deee9cd0add11`. Les empreintes SHA-256 des sept fichiers sont conformes au manifeste.
Exécutant : sous-agent Claude Code (voir accusé issue 107) ; modèle et effort conformes au manifeste. L’heure de début n’a pas été relevée au lancement (première heure observée : 09:50 UTC).
Première source lue : consensus britannique de 2023 [S2], section « Background » (https://pmc.ncbi.nlm.nih.gov/articles/PMC10511987/).

## Synthèse

| Gravité | Nombre |
|---|---|
| BLOQUANT | 0 |
| MAJEUR | 12 (dont C01, **bloquant pour la clôture du cours et du lot**) |
| MINEUR | 8 |
| ENRICHISSEMENT | 5 |

La leçon est fidèle à ses sources sur la plupart des chiffres. Nous avons relu en texte intégral le consensus britannique, la revue de Fribourg 2021, la revue d’Oxford 2025, l’article bernois sur la compliance et les quatre informations professionnelles suisses. Le score de Berne, les critères de l’ICHD-3 et les dix-sept fréquences du tableau 3 sont exacts. Quatre faiblesses dominent pourtant :
- la **sémiologie fondamentale et analytique est absente**, et les sciences ne comptent que trois disciplines ;
- **quatre calculs ou figures sont faux** : une somme de pourcentages, une contradiction sur la pression d’ouverture, une figure de Monro-Kellie inversée et un délai thérapeutique dépassé dans le cas récapitulatif ;
- la **pharmacologie n’est pas alignée sur les informations professionnelles suisses** : la leçon déclare absentes des interactions qui figurent dans les FI, omet des contre-indications et un plafond hépatique ;
- les **doses de caféine** reprises d’une revue dépassent de 1,5 à 3 fois le niveau de sécurité européen, sans le dire.

Aucune erreur n’atteint le seuil d’une conduite dangereuse inventée : les doses de caféine sont citées fidèlement d’une revue publiée, mais elles doivent être replacées sous le plafond de l’EFSA.

## Calculs

Le script `calculs/verifier.py` relève toutes les valeurs chiffrées des sept fichiers, puis recalcule chaque grandeur calculable à partir de l’énoncé et des sources. Chaque occurrence de l’inventaire est rattachée à au moins un contrôle.

| Indicateur | Valeur |
|---|---|
| Occurrences relevées | 270 |
| Contrôles calculables | 103 |
| Recalculés | 103 |
| Corrects | 88 |
| Arrondis | 5 |
| Faux | 10 |
| Non vérifiables | 0 |

| Contrôle | Objet | Résultat | Constat |
|---|---|---|---|
| D01 | Cas récapitulatif à six semaines | fenêtre conservatrice de deux semaines dépassée | C03 |
| P07 | Pression d’ouverture | 33,3 % + 31,9 % laisserait 35 % de pressions élevées (3 % dans la méta-analyse) | C04 |
| F02 | Figure 2, barre du sang | 80 → 40 : diminution, contraire à la légende | C05 |
| P04 | Rhinorrhée non traumatique | 30 + 17 + 16 = 63 %, non « plus de 100 % » | C07 |
| T01 | Seuil de l’hypertension intracrânienne idiopathique | 200 mm contre 25 cm dans la source la plus récente | C08 |
| Q07 | Caféine | 600 à 1200 mg/j, soit 1,5 à 3 fois les 400 mg/j de l’EFSA | C09 |
| Q04 | Paracétamol, foie | plafond de 2000 mg/j absent | C11 |
| S01 | Durées opératoires | 139 min attribuées à la suture par l’ordre de la phrase | C13 |
| F03, F04 | Lisibilité des figures | 7,8 et 7,3 px à 390 px | C17 |

## Constats MAJEURS

1. **C01 — Sémiologie absente. MAJEUR, bloquant pour la clôture du cours et du lot.** Le bouton `g96-s-semio` et sa discipline n’existent pas. La grille est négative sur SEM-01 à SEM-03, SEM-08 et SEM-13. Un sous-onglet conforme au contrat est proposé dans `propositions/G96_c_semio.html`. Il comprend le bouton `g96-tab-semio`, un panneau `role="tabpanel"`, neuf sections `data-semiology` titrées en `h3`, une figure non anatomique lisible à 390 px, trois cas corrigés et des sources liées. Le contrôle structurel du validateur passe sur un assemblage d’essai. Les sept fenêtres sont dans `G96_pop1_semio.html` (cible `G96_pop1.html`) ; le marqueur clinique `data-semiology-clinical="G96"` est dans `G96_a_semio_clinique.html`.
2. **C02 — Trois disciplines seulement.** `tests/audit_sciences.py` échoue avec quinze erreurs : aucun des quatre libellés exigés, une physiologie de 247 mots et une biochimie de 186 mots sans figure. `G96_c_liens.html` renomme et complète les encadrés. `G96_c_biomeca.html` ajoute une discipline « Biomécanique craniospinale » fondée sur l’article bernois lu en texte intégral. Le validateur exige six boutons : on en atteint cinq, et une sixième discipline reste à sourcer.
3. **C03 — Cas récapitulatif.** La patiente souffre depuis six semaines, et le cas propose encore un traitement conservateur de moins de deux semaines. Le consensus limite ce traitement à deux semaines après le début et demande d’offrir alors un patch non ciblé.
4. **C04 — Pression d’ouverture contradictoire.** La leçon écrit « basse chez un tiers seulement » et « normale chez 31,9 % ». Ces deux chiffres proviennent de séries opposées : une cohorte de 106 patients (34 % de pressions basses) et les méta-analyses (67 % de pressions basses, 32 % normales). La correction attribue la divergence en six endroits.
5. **C05 — Figure 2 inversée.** La figure de Monro-Kellie montre une baisse du sang après la fuite. La légende et la doctrine disent l’inverse.
6. **C06 — Figure 1 d’origine IA démontrée.** C’est un dessin SVG de la dure-mère créé lors du cycle Betta 41. Trois originaux CC BY 4.0 sont proposés (Luetzen 2021, figures 2, 4 et 6) ; leur contrôle visuel reste à faire.
7. **C07 — Sommes des sites de rhinorrhée.** La série non traumatique totalise 63 %, non plus de 100 %. La série traumatique décrit des sites de fracture, non des sites de fuite.
8. **C08 — Seuil obsolète de l’hypertension intracrânienne idiopathique.** La leçon retient plus de 200 mm (250 mm si l’indice de masse corporelle dépasse 30), d’après la revue de 2020. Sa propre source de 2025 retient plus de 25 cm.
9. **C09 — Caféine.** Les doses citées représentent 600 à 1200 mg par jour, soit 1,5 à 3 fois le niveau sans risque de l’EFSA, sans FI suisse et sans mise en garde.
10. **C10 — Diamox.** L’alerte affirme l’absence d’interactions, alors que la FI de juillet 2026 en liste. Elle déconseille l’association à un autre inhibiteur de l’anhydrase carbonique, comme le topiramate cité pour le rebond. Elle signale aussi l’acidose sévère avec l’acide acétylsalicylique à forte dose.
11. **C11 — Paracétamol.** Le plafond de 2000 mg par jour manque en cas de maladie hépatique chronique, d’alcoolisme ou de dénutrition. La rubrique des interactions est déclarée absente à tort.
12. **C12 — Ibuprofène.** La contre-indication « tendance accrue aux saignements » est omise, alors que l’hématome sous-dural est une complication de la maladie.

## Constats MINEURS

| Constat | Objet |
|---|---|
| C13 | Durées opératoires (139 min pour le sealing, 169 min pour la suture) mal attribuées |
| C14 | « Ne conduit pas » : la source dit « ne conduit pas lui-même pour rentrer » |
| C15 | FI Ferriprox incomplète (neutropénies répétées, contraception, 100 mg/kg/j, seuil de 1,5 × 10⁹/L) |
| C17 | Figures illisibles à 390 px |
| C18 | Incidence de 3,7 pour 100 000 : étude californienne, non britannique |
| C19 | Codes G97.80 et G97.2 absents |
| C20 | Signes d’alarme après patch incomplets |
| C21 | Patient asymptomatique avec collection : exploration et traitement à proposer |

## Enrichissements

| Enrichissement | Objet |
|---|---|
| C16 | Méta-analyse de 2021 : céphalée 97 %, orthostatique 92 %, IRM normale 19 %, premier patch 64 % |
| C22 | Choix du vaccin conjugué selon l’âge (plan 2026) |
| C23 | Échographie de la gaine du nerf optique (diminution de plus de 5 %), schéma bernois |
| C24 | Valeurs prédictives négatives du score de Berne (0,81) et du score de la Mayo Clinic (0,65) |
| C25 | Spécificités suisses : assurances et aptitude à la conduite, lacune |

## Rubrique 21 — Sémiologie fondamentale et analytique

**Statut : absente. Constat C01, MAJEUR, bloquant pour la clôture du cours et du lot.**

| Critère | Résultat | Critère | Résultat |
|---|---|---|---|
| SEM-01 | non | SEM-13 | non (`alert` présent dans `g96-8` seulement) |
| SEM-02 | non | SEM-14 | partiel |
| SEM-03 | non (`audit_sciences` échoue) | SEM-15 | non |
| SEM-04 | oui pour le fichier actuel | SEM-16 | non |
| SEM-05 | non | SEM-17 | non |
| SEM-06 | non | SEM-18 | non |
| SEM-07 | non | SEM-19 | non évaluable |
| SEM-08 | non | SEM-20 | non évaluable |
| SEM-09 | non | SEM-21 | non évaluable |
| SEM-10 | partiel | SEM-22 | non |
| SEM-11 | non | SEM-23 | non |
| SEM-12 | non | SEM-24 | oui |

La sémiologie fondamentale existe en partie dans les îlots `g96-5` et `g96-6`. Elle donne les fréquences et la technique des constantes, sans mécanisme par signe. La sémiologie analytique est absente. Aucune source lue ne donne la sensibilité ni la spécificité des signes cliniques ; la proposition l’écrit explicitement.

## Matrice des 20 rubriques (résumé)

- **Couvertes :** 1, 2, 3, 6, 7, 9, 13, 14, 17, 19.
- **Partielles :** 4, 5, 8, 10, 11, 12, 15, 16, 18, 20.
- **Absente :** aucune ; la rubrique 21 est absente.

Le détail des ancres figure dans `rapport.json`.

## Lacunes principales

- Aucune recommandation suisse ni européenne dédiée n’a été trouvée ; seul un compte rendu suisse a été lu (S30).
- La sensibilité et la spécificité des signes cliniques ne sont chiffrées dans aucune source lue.
- Le mécanisme des symptômes cochléovestibulaires n’est précisé par aucune source lue.
- Aucune source ne permet encore d’écrire la sixième discipline exigée par le validateur.
- S19 et S23 n’ont pas été relues ; plusieurs sources n’ont été lues qu’en résumé.
- Les spécificités suisses (Suva, assurance-invalidité, conduite) et les objectifs PROFILES n’ont pas été recherchés.
- Le contrôle visuel des figures candidates et les captures réelles n’ont pas été réalisés.

## Tableau de bord

| Élément | Valeur |
|---|---|
| Leçon | G96 — Autres affections du système nerveux central : fuites de liquide céphalorachidien (S08) |
| Fichiers lus | 7/7 en entier ; empreintes conformes au manifeste |
| Contrôles | `test_v7 --static` OK ; `audit_sciences` en échec (15 erreurs) ; ancres uniques vérifiées par script |
| Calculs | 270 relevés ; 103 contrôles recalculés ; 10 faux |
| Sources lues | 28 (dont 4 FI suisses datées, 1 source suisse, 2 méta-analyses) ; 2 sources de la leçon non relues |
| Propositions | 12 fichiers dans `propositions/` |
| Statut | Revue IA, distincte d’une validation médicale humaine ; aucune source canonique modifiée |
