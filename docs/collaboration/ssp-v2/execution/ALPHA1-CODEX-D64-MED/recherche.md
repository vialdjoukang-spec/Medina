# D64 — Autres anémies : audit médical Alpha, tour1

Lecture des sept fichiers et six figures achevée ; vérification externe ciblée, aucune validation exhaustive ni médicale humaine. D64.0, D64.1, D64.2, D64.3, D64.4, D64.8, D64.9 relus dans BfArM.

## Matrice de complétude

| Rubrique | Statut | Preuves et limites |
|---|---|---|
| 1. Question clinique et enjeu pour l’examen fédéral | LACUNE | S2,S7 ; d64-a01;d64-a09 ; SSP locaux lus ; PROFILES primaire non relu. |
| 2. Définition et périmètre CIM-10-GM | LACUNE | S6 ; d64-a02 ; D64.0/.1/.2/.3/.4/.8/.9 et exclusions BfArM contrôlés ; OFS français non relu. |
| 3. Classifications et stades | LACUNE | S8,S12 ; d64-a02;d64-a05 ; Couronnes et WHO2022 relus ; toute la hiérarchie ICC/WHO non revalidée. |
| 4. Épidémiologie suisse puis européenne | LACUNE | S1,S11 ; d64-a03 ; Données historiques reconnues ; incidence/prévalence suisse des formes rares non établie. |
| 5. Normal → pathologique | LACUNE | S14,S15 ; d64-s01–s03 ; Erreur ALAS confirmée ; toutes enzymes HIF/EPO/hepcidine non revérifiées. |
| 6. Étiologies et facteurs de risque | LACUNE | S7,S9 ; d64-a04 ; ALAS2/SLC25A38/globines relus ; inventaire complet des toxiques et variants non revalidé. |
| 7. Anamnèse et symptômes (fréquences) | LACUNE | S2,S11 ; d64-a07 ; Symptômes généraux et CDA relus ; fréquences rares non revalidées. |
| 8. Examen clinique | LACUNE | S2 ; d64-a08 ; Examen orienté lu ; performances des signes non revalidées. |
| 9. Drapeaux rouges et urgences | LACUNE | S2,S5 ; d64-a10 ; Critères urgence et restriction transfusionnelle ciblés confirmés ; toute situation cardiaque/pédiatrique non revalidée. |
| 10. Examens complémentaires | LACUNE | S2,S3,S4,S7 ; d64-a09;d64-e01 ; Normes locales et démarche génétique contrôlées ; réserve F01 et autres diagnostics non exhaustifs. |
| 11. Diagnostic différentiel | LACUNE | S2,S7 ; d64-a09 ; Alpha-thalassémie et dilution enrichies ; autres mimics pas tous sourcés. |
| 12. Prise en charge suisse et FI | LACUNE | S8,S10,S11 ; d64-a11 ; Complications fer/splénectomie relues ; risques chiffrés rares non exhaustifs. |
| 13. Complications et pronostic | LACUNE | S9,S10,S11 ; d64-p01 ; B6/IFN/splénectomie ciblés ; HSCT et protocoles de centre non validés exhaustivement. |
| 14. Suivi, prévention, dépistage | LACUNE | S17,S18,S19,S20 ; d64-p01;d64-p02 ; 4FI exactes lues par sections ; F02,F03,F10 ouverts, pas validation de toute prescription. |
| 15. Situations particulières | LACUNE | S11,S18,S19 ; d64-a12;d64-p02 ; Fer et sécurité médicamenteuse ciblés ; surveillance personnalisée hors indication manque. |
| 16. Spécificités suisses | LACUNE | S2,S11,S17,S18 ; d64-a12;d64-p02 ; Limites âge/grossesse/foie/rein lues ciblées ; protocoles pédiatriques et grossesse non exhaustifs. |
| 17. Critères formels du diagnostic | LACUNE | S3,S4,S16 ; d64-e01;d64-e03 ; Méthodes/units et calcul TSAT contrôlés ; données exactes du laboratoire patient restent requises. |
| 18. Paramètres clés chiffrés | LACUNE | S8,S14,S15 ; d64-e02;d64-s03 ; 6figures vues, erreur biochimique notée ; licences originales/rendu navigateur non revalidés. |
| 19. Sous-codes CIM-10-GM couverts | LACUNE | S2,S7 ; d64-a01;d64-a09 ; Cas et quiz lus ; liens SSP officiels et performances pédagogiques non validés. |
| 20. Points d’examen fédéral PROFILES/SSP | LACUNE | S1–S21 ; glossary/d64.py;7sources ; Lexique lu, cohérence ciblée ; validation ligne par ligne de tous faits externes non achevée. |

## Constats

- D64-F01 P1 : Une analyse des fractions Hb normale ne clôt pas la recherche de globinopathie : certaines alpha-thalassémies/CNV et variants instables requièrent un test ciblé. La table transforme une orientation en indication trop automatique. Sources : [S7], [S9].
- D64-F02 P1 : Le plafond20 omet le sous-plafond de sécurité de la FI du comprimé dispersible : sans mesure LIC et ferritine≤2000, ne pas dépasser10mg/kg. Si dose>10 et LIC<7 ou ferritine≤2000, réduire à≤10. Sources : [S18].
- D64-F03 P1 : Le cours donne une dose hors indication de peg-IFN mais pas de calendrier opérationnel de numération/biochimie ni de conduite devant toxicité psychiatrique ou cytopénie. La FI contient un calendrier concret, pour hépatites. Sources : [S19], [S11].
- D64-F04 P2 : Formulation exhaustive incompatible avec la définition par concentration et la branche hémodilution du successeur HUG2022 ; le propre popup a01 évoque déjà le volume. Sources : [S2].
- D64-F05 P2 : Le texte reprend une erreur du schéma publié. La réaction ALAS produit ALA, CoA et CO2 ; libération d’eau non conforme à IUBMB/Rhea. Sources : [S14], [S15].
- D64-F06 P2 : La phrase rapporte fidèlement LUKS, mais ne distingue pas stock épuisé et restriction de disponibilité sous inflammation. Une restriction fonctionnelle peut abaisser TSAT sans épuisement des stocks ; le cours insiste surtout sur le piège inverse de transferrine basse. Sources : [S16], [S13].
- D64-F07 P2 : Un successeur institutionnel HUG2022 a réellement été retrouvé. Les chiffres Hb/réticulocytes et urgence étudiés sont largement conservés ; les présenter comme seulement issus2013 manque actualisation. Sources : [S1], [S2].
- D64-F08 P2 : Enrichissement utile : HUG2022 précise niveau de la mer et baisse>10% avec symptômes pouvant justifier investigation malgré Hb au-dessus du seuil. Les valeurs de diagnostic ne sont pas des seuils de transfusion. Sources : [S2], [S5].
- D64-F09 P2 : Les définitions sont confirmées ; manque une explication de l’incertitude de comptage près des seuils. GFHC donne des intervalles suffisamment larges pour nuancer un chiffre isolé. Sources : [S8].
- D64-F10 P2 : La revue2019 consultée ne nomme pas alfa2a dans ce passage. La série primaire2020, résumé éditeur lu, utilise90–180µg initialement puis adaptation chez7patients dépendants des transfusions. Elle ne démontre pas que30–50 soit faux ; la provenance du produit exact reste insuffisante pour un tableau posologique. Sources : [S11], [S19], [S21].
