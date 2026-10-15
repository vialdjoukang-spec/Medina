# Rapport de rédaction — G98 — Autres affections du système nerveux, non classées ailleurs (N-05-Neurologie)

Cycle Betta 41 · agent C41-A3-NEUR (rédaction, Sonnet 5.5) · 15.10.2026. Porte de vérité franchie avant rédaction : `python3 tools/betta_verite.py` → VÉRITÉ OK.
Audit différé — revue IA, distincte d'une validation médicale humaine.

## Fichiers (octets)
chapters/G98/G98_a.html 23 066 · _b.html 26 696 · _c.html 19 797 · _d.html 10 909 · _pop1.html 20 130 · _pop2.html 9 444 ; glossary/g98.py ≈ 10 100. Environ 11 600 mots au total (corps et fenêtres).
Structure : 4 onglets. Pathologie : îlots g98-0 à g98-14 (dernier îlot = critères formels `div.alert` puis paramètres clés `div.key`). Examens : g98-e-1 à e-5 (e-5 = 5 cas fictifs d'entraînement). Sciences : 3 sous-onglets (g98-s-anat-body, g98-s-bio-body, g98-s-img-body). Pharmacologie : g98-p-1 à p-5 (p-4 prophylaxie antithrombotique, p-5 infection et cas 6). 21 fenêtres de contenu (mots verts) dont les nouvelles g98-qualiccare, g98-chantelau, g98-chronique, g98-enoxaparine ; 7 fenêtres Pareto (clin, crit, exam, s-anat, s-bio, s-img, pharma).

## Axe de la leçon
G98 est une catégorie résiduelle sans sous-code. Seule entité clinique rattachée : l'arthropathie de Charcot (G98† + M14.6-*), traitée comme neuro-ostéoarthropathie de Charcot. « Affection du système nerveux SAI » est présentée comme règle de codage, sans contenu clinique inventé.

## Matrice de complétude (reprise du dossier, avec le lieu de traitement)
| rubrique | statut | onglet et identifiant HTML |
|---|---|---|
| 1. Question clinique et enjeu pour l'examen fédéral | ✔ | Pathologie `g98-0` ; fenêtre `g98-qualiccare` |
| 2. Définition et périmètre CIM-10-GM (libellés OFS, inclusions, exclusions) | ✔ | Pathologie `g98-1`, `g98-2` ; fenêtres `g98-codage`, `g98-cno` |
| 3. Classifications et stades | ✔ | Pathologie `g98-3` (Eichenholtz 0–III, Chantelau, Sanders-Frykberg I–V) ; fenêtres `g98-eichenholtz`, `g98-chantelau`, `g98-sanders` |
| 4. Épidémiologie suisse puis européenne | ✔ partielle (aucune donnée populationnelle suisse, déclaré) | Pathologie `g98-4` |
| 5. Normal → pathologique | ✔ (normal physiologique non sourcé, déclaré) | Pathologie `g98-5` ; Sciences `g98-s-anat-body`, `g98-s-bio-body` ; fenêtres `g98-rankl`, `g98-bascule` |
| 6. Étiologies et facteurs de risque | ✔ | Pathologie `g98-6`, `g98-4` (diabète, tabac) |
| 7. Anamnèse et symptômes | ✔ | Pathologie `g98-7` |
| 8. Examen clinique | ✔ | Pathologie `g98-7` ; fenêtre `g98-thermometrie` |
| 9. Drapeaux rouges et urgences | ✔ | Pathologie `g98-9` (div.alert) |
| 10. Examens complémentaires | ✔ | Examens `g98-e-1` à `g98-e-4` ; Pathologie `g98-8` ; Sciences `g98-s-img-body` ; fenêtre `g98-irm` |
| 11. Diagnostic différentiel | ✔ (élément discriminant documenté seulement pour l'ostéomyélite, déclaré) | Pathologie `g98-8` ; fenêtre `g98-osteomyelite` |
| 12. Prise en charge suisse | ✔ | Pathologie `g98-10`, `g98-11`, `g98-13` ; Pharmacologie `g98-p-1` à `g98-p-5` ; fenêtres `g98-decharge`, `g98-enoxaparine` |
| 13. Complications et pronostic | ✔ | Pathologie `g98-4` ; Sciences `g98-s-anat-body` |
| 14. Suivi, prévention, dépistage | ✔ | Pathologie `g98-12` ; fenêtres `g98-remission`, `g98-reactivation`, `g98-chronique` |
| 15. Situations particulières | ✔ partielle (enfant, grossesse : lacune déclarée) | Pathologie `g98-13` ; Pharmacologie `g98-p-4` |
| 16. Spécificités suisses | ✔ partielle (AI/AVS/LAMal, conduite, assurance-accidents non lus, déclaré) | Pathologie `g98-13` (organisation des soins) ; `g98-0` ; fenêtre `g98-qualiccare` |
| 17. Critères formels du diagnostic | ✔ | Pathologie `g98-14` (div.alert) |
| 18. Paramètres clés chiffrés | ✔ | Pathologie `g98-14` (div.key) ; Pareto `pareto-g98-crit` |
| 19. Sous-codes CIM-10-GM couverts | ✔ G98 sans subdivision ; liens M14.6-*, A52.1†, E10–E14† .6, M49.4-* | Pathologie `g98-1` ; fenêtre `g98-codage` |
| 20. Points d'examen fédéral | ✔ partielle (objectifs PROFILES non vérifiés) | Pathologie `g98-13` (div.trap « Pièges classiques »), `g98-1`, `g98-8` ; Examens `g98-e-5` ; Pharmacologie `g98-p-4`, `g98-p-5` (cas fictifs) |

## Sources utilisées (sources.json)
S1, S2 (BfArM) et S14 (OFS) pour le codage ; S3 (IWGDF 2023) source internationale principale ; S10 (QualiCCare/SSED 2020) source suisse principale ; S4 (Rosskopf, Balgrist) ; S5 (Gratwohl) ; S6 (Waibel) ; S7 (Berli) ; S8 (Fischer) ; S11 (Rev Med Suisse 2013) ; S12 et S13 (Swiss Med Wkly 2014, 2013) ; S15 (information professionnelle Clexane®, février 2026, posologies citées comme repères hors protocole du Charcot). S9 non citée dans le texte (intérêt terminologique seulement).

## Lacunes conservées (non comblées de mémoire)
1. Épidémiologie suisse populationnelle : aucune ; chiffres de prévalence très hétérogènes.
2. Rien sur l'enfant ni la grossesse ; Charcot non diabétique, membre supérieur, colonne (M49.4) : pas de conduite.
3. Spécificités administratives suisses (AI/AVS/LAMal et chaussures orthopédiques, aptitude à la conduite avec plâtre jusqu'au genou, Suva/LAA) non lues : annoncées comme telles dans le cours.
4. Thromboprophylaxie : le document suisse recommande sans préciser molécule, dose ni durée ; posologies de Clexane® données comme repères d'indications nommées, jamais comme protocole du Charcot. Vitamine D et calcium : aucune posologie.
5. Objectifs PROFILES/SSP spécifiques à G98 et correspondance CIM-11 non vérifiés.
6. Définition détaillée du stade IV d'Eichenholtz « modifié » (S4) non lue ; contenu précis des niveaux de soins 1, 2 et 3 non défini dans S10.
7. Fonctionnement physiologique normal des voies sensitives et de la voie RANKL non sourcé : seules leurs conséquences sont décrites.
8. Plusieurs sources (S5–S9, S11–S13) lues au seul niveau du résumé ; aucune conduite thérapeutique ne repose sur elles seules.
9. Éléments discriminants chiffrés du différentiel (goutte, thrombose veineuse profonde, arthrose activée) absents des sources lues.

## Auto-contrôle
HTML bien formé (balises appariées par fichier), identifiants uniques et préfixés `g98-`, toutes les clés de fenêtres référencées existent et aucune fenêtre n'est orpheline, toutes les couvertures Pareto pointent des îlots existants, `build_medina.audit()` renvoie `{}` sur le corps et sur les fenêtres (glossaire du dossier chargé), aucune recommandation américaine comme fondement.
