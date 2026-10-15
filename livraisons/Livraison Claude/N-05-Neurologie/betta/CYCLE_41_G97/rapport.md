# Rapport de rédaction — G97, cycle Betta 41 (C41-A1-NEUR, Sonnet 5.5)

Affections du système nerveux après des actes médicaux, non classées ailleurs (N-05-Neurologie). État au 15.10.2026. Porte de vérité : `python3 tools/betta_verite.py` affiche « VÉRITÉ OK · CYCLE_41_G97 » avant rédaction. Le premier jet (sources S1 à S23) a été complété par les sources S24 à S30 et la section 18 du dossier.

## Fichiers (octets)
G97_a.html 28594 ; G97_b.html 30715 ; G97_c.html 24558 ; G97_d.html 10630 ; G97_pop1.html 25660 ; G97_pop2.html 25002 ; g97.py 6752. Total 151911. Empreintes : `sha256sum chapters/G97/* glossary/g97.py`.

## Contenu
Quatre onglets : Pathologie (13 îlots g97-0 à g97-12, dernier îlot = critères formels ICHD-3 en `alert` puis paramètres clés en `key`), Examens (g97-e-1 à e-4, six fiches, quatre cas corrigés), Sciences (anatomie, physiologie, preuves chiffrées, trois figures SVG légendées, corrélations cliniques), Pharmacologie (g97-p-1 à p-4). Monographie classique autour de quatre tableaux cliniques (céphalée post-ponction, hématome épidural postopératoire, mutisme cérébelleux, surdrainage), sans îlot ni tableau consacré aux codes. 54 fenêtres dont 14 Pareto ; 6 quiz ; 503 marqueurs data-evidence uniques ; glossaire : 6 abréviations du premier jet, EPiMAP et les 10 codes G97.x ajoutés (les autres sont déjà au glossaire du dépôt).

## Matrice de complétude (rubrique, onglet, identifiant HTML, statut)
| rubrique | onglet | identifiant HTML | statut |
|---|---|---|---|
| 1. Question clinique et enjeu | Pathologie | g97-0 ; g97-11 (11.8 pièges) | ✔ |
| 2. Définition et périmètre CIM-10-GM | Pathologie | g97-1 ; fenêtre g97-cim | ✔ |
| 3. Classifications et stades | Pathologie | g97-1 (1.1 ICHD-3, 1.2 parole, hématome) | ✔ |
| 4. Épidémiologie suisse puis européenne | Pathologie | g97-2 (cohorte genevoise, méta-analyse aiguille, hématome, mutisme) | ✔ partiel : aucun registre suisse |
| 5. Normal → pathologique | Pathologie ; Sciences | g97-3 ; g97-s-anat-cours ; g97-s-physio-cours | ✔ |
| 6. Étiologies et facteurs de risque | Pathologie | g97-4 | ✔ |
| 7. Anamnèse et symptômes | Pathologie | g97-5 | ✔ |
| 8. Examen clinique | Pathologie | g97-6 | ✔ ; sensibilité/spécificité non disponibles |
| 9. Drapeaux rouges et urgences | Pathologie | g97-8 (encadré alert, 8.1, 8.2) ; fenêtre g97-ddx-cppd | ✔ |
| 10. Examens complémentaires | Examens ; Pathologie | g97-e-1, g97-e-2 (fiches 1 à 6), g97-7 (7.2) | ✔ |
| 11. Diagnostic différentiel | Pathologie ; Examens | g97-7 (7.4) ; g97-e-3 ; fenêtre g97-postpartum | ✔ |
| 12. Prise en charge suisse | Pathologie ; Pharmacologie | g97-9 (9.1 à 9.7) ; g97-p-1 à g97-p-4 ; fenêtres g97-paracetamol, g97-ibuprofene, g97-bpe, g97-bpe-echec | ✔ partiel : aucune recommandation suisse ; caféine sans information professionnelle suisse |
| 13. Complications et pronostic | Pathologie | g97-8 (8.3, 8.4) ; g97-10 | ✔ |
| 14. Suivi, prévention, dépistage | Pathologie | g97-10 | ✔ |
| 15. Situations particulières | Pathologie ; Pharmacologie | g97-11 (11.1 à 11.6) ; g97-p-3 | ✔ ; sujet âgé = lacune |
| 16. Spécificités suisses | Pathologie | g97-11 (11.7) ; fenêtre g97-suisse | LACUNE partielle : déclaration, assurance-accidents, assurance-invalidité, aptitude à la conduite, remboursement non trouvés |
| 17. Critères formels du diagnostic | Pathologie | g97-12 (encadré alert, ICHD-3 7.2, 7.2.1, 7.2.2) | ✔ |
| 18. Paramètres clés chiffrés | Pathologie | g97-12 (encadré key) | ✔ |
| 19. Sous-codes CIM-10-GM couverts | Pathologie (fenêtre) | fenêtre g97-cim, ouverte depuis g97-1 ; aucun tableau ni îlot de codes | ✔ : G97.0, G97.2, G97.80, G97.81, G97.82 développés ; G97.1 par un fait ; G97.83, G97.84, G97.88, G97.9 par le libellé seul (LACUNE) |
| 20. Points d'examen fédéral | Pathologie ; Examens | g97-11 (11.8) ; g97-e-4 (cas 1 à 4) ; g97-7 et g97-12 (quiz) | ✔ ; objectifs PROFILES non consultés (LACUNE) |

## Auto-contrôle
HTML bien formé sur a+b+c+d et sur chaque fenêtre (0 erreur, aucune balise ouverte) ; identifiants et marqueurs data-evidence uniques ; identifiants préfixés `g97-` ; toute clé `data-k` possède sa fenêtre, aucune fenêtre orpheline ; couvertures Pareto valides ; `build_medina.audit()` renvoie `{}` sur l'assemblage avec le glossaire g97 ; porte de vérité OK.

## Sources utilisées (dossier uniquement)
S1 à S30. Lues en résumé seul, donc signalées comme telles : S6 à S20, S23 à S29 (S5 lu jusqu'au caractère 100000 sur 129083). Informations professionnelles suisses : S21 (paracétamol) et S22 (ibuprofène). Libellés suisses : S30 (OFS). Aucune donnée extérieure au dossier. Calculs propres au cours, signalés : différence absolue de 6,8 points et nombre à traiter d'environ 15 (incidences 11,0 % et 4,2 %).

## Lacunes et réserves
1. Aucune recommandation suisse (Revue Médicale Suisse 2008 inaccessible) ; le consensus de 2023 (S5), dirigé par des sociétés américaines et cosigné par l'ESRA et l'OAA, est présenté comme consensus international, corroboré pour l'aiguille (S7) et le moment du blood patch (S24, S27) par des données européennes ; jamais comme recommandation suisse.
2. Intervalles ESAIC/ESRA (S9) non chiffrés (résumé seul). Définition Delphi du mutisme (S15) non lue.
3. Surdrainage (G97.2) : aucune recommandation ; signes cliniques détaillés, réglage de valve et traitement non écrits.
4. G97.83, G97.84, G97.88, G97.9 : libellé seul ; G97.1 : un seul fait.
5. Caféine : aucune information professionnelle suisse ; dose d'après S5 seul.
6. Contentieux ibuprofène et allaitement : l'information professionnelle suisse déconseille, le consensus propose les AINS ; l'information suisse prime pour la Suisse.
7. Déclaration à l'Office fédéral de la santé publique, assurance-accidents (Suva), assurance-invalidité, aptitude à la conduite, remboursement, objectifs PROFILES : non trouvés, donc non écrits ; sujet âgé non documenté.
8. S24 à S29 : résumés PubMed seuls. S28 : population israélienne ; la lombalgie chronique n'est donnée que sous forme d'étendue (16,1 à 20,8 %) car l'attribution exacte aux groupes avec et sans patch n'est pas lisible dans le dossier.
9. Les lettres de grade A à D et I du consensus sont reprises sans définition détaillée (gradation américaine). Vignettes et cas fictifs.

Audit différé — revue IA, distincte d'une validation médicale humaine.
