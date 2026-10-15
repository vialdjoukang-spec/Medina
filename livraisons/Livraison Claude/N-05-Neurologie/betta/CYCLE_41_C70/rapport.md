# Rapport de rédaction — C70 — Tumeur maligne des méninges (N-05-Neurologie)

Cycle Betta 41, agent C41-A4-NEUR, rédaction Sonnet 5.5. Porte de vérité franchie avant rédaction (`VÉRITÉ OK · CYCLE_41_C70`). Axe retenu : méningiome anaplasique (malin) de grade 3 de l'OMS, avec le contexte de codage, de différentiel et de spécificités suisses. Le brouillon précédent (sources S1 à S12) a été révisé pour intégrer S13 à S20.

## Fichiers (octets)
- 20459 chapters/C70/C70_a.html (onglet Pathologie, îlots 0 à 5)
- 24824 chapters/C70/C70_b.html (îlots 6 à 13, références)
- 23308 chapters/C70/C70_c.html (onglets Examens et Sciences)
- 12177 chapters/C70/C70_d.html (onglet Pharmacologie)
- 20596 chapters/C70/C70_pop1.html ; 21482 chapters/C70/C70_pop2.html (49 fenêtres, dont 8 Pareto)
- 7092 glossary/c70.py (entrées conditionnelles, aucun terme existant écrasé)
- Total 129 938 octets ; environ 13 700 mots (fenêtres comprises) ; 7 quiz de cas cliniques ; 3 schémas SVG ; 3 sciences (anatomie, histologie, génétique).

## Matrice de complétude, avec onglet et identifiant HTML
Onglets : pA = Pathologie ; pE = Examens ; pS = Sciences ; pP = Pharmacologie. Les identifiants `c70-…` sont des îlots ; `[fenêtre]` désigne une clé `data-pop`.

| rubrique | statut | sources | onglet et identifiant |
|---|---|---|---|
| 1. Question clinique et enjeu pour l'examen fédéral | ✔ | S2, S4, S5 | pA `c70-0` ; enjeu d'examen pA `c70-12` |
| 2. Définition et périmètre CIM-10-GM | ✔ | S1, S18, S19 | pA `c70-1` ; [c70-cim], [c70-cimo] |
| 3. Classifications et stades | ✔ | S3, S4, S5 | pA `c70-1` (tableau des grades), `c70-9` (Simpson) ; [c70-who2021], [c70-grade2], [c70-simpson] |
| 4. Épidémiologie suisse puis européenne | ✔ (grade 3 suisse = LACUNE) | S14, S2, S5, S11 | pA `c70-2` ; [c70-zurich] |
| 5. Normal → pathologique | ✔ (anatomie détaillée = LACUNE) | S1, S2, S3, S5 | pA `c70-3` ; pS `c70-s-anat-cours`, `c70-s-histo-cours`, `c70-s-genet-cours` |
| 6. Étiologies et facteurs de risque | ✔ | S2, S7, S12 | pA `c70-4` ; [c70-cyproterone], [c70-nf2] |
| 7. Anamnèse et symptômes | ✔ (fréquences chiffrées = LACUNE) | S2, S5 | pA `c70-5` |
| 8. Examen clinique | ✔ (sensibilité et spécificité non disponibles) | S2, S5 | pA `c70-5` |
| 9. Drapeaux rouges et urgences | ✔ (état de mal = LACUNE) | S2, S5, S15 | pA `c70-8` ; pP `c70-p-2` ; [c70-dexa] |
| 10. Examens complémentaires | ✔ | S2, S4, S5, S6, S17 | pA `c70-6` ; pE `c70-e-1`, `c70-e-2`, `c70-e-3`, `c70-e-5` |
| 11. Diagnostic différentiel | ✔ (sarcoïdose = lacune partielle) | S6, S17, S2 | pA `c70-7` ; pE `c70-e-4`, `c70-e-5` ; [c70-mimes], [c70-leptomeninge] |
| 12. Prise en charge suisse | ✔ (aucune recommandation suisse en texte intégral = LACUNE) | S2, S5, S8, S9, S10, S11, S15, S16 | pA `c70-9` ; pP `c70-p-1` à `c70-p-5` |
| 13. Complications et pronostic | ✔ | S2, S5 | pA `c70-8`, `c70-10` ; [c70-chirurgie], [c70-recidive] |
| 14. Suivi, prévention, dépistage | ✔ | S2, S7 | pA `c70-10` (IRM tous les 3 à 6 mois) ; prévention pA `c70-4` (cyprotérone) |
| 15. Situations particulières | ✔ (grossesse = LACUNE) | S2, S4, S5, S16 | pA `c70-11` ; pP `c70-p-2` (adaptation rénale) |
| 16. Spécificités suisses | ✔ (Suva, assurance-invalidité, remboursement = LACUNE) | S13, S18, S8 | pA `c70-12` ; [c70-declaration], [c70-conduite] ; pP `c70-p-3` |
| 17. Critères formels du diagnostic | ✔ | S2, S3, S4, S5 | pA `c70-13` (`div.alert`) |
| 18. Paramètres clés chiffrés | ✔ | S2, S5, S7, S8, S14 | pA `c70-13` (`div.key`) |
| 19. Sous-codes CIM-10-GM couverts | ✔ | S1, S19 | pA `c70-1` ; [c70-cim] (C70.0, C70.1, C70.9 ; C79.3 en différentiel) |
| 20. Points d'examen fédéral | ✔ | S20, S17, S4, S8, S7, S13 | pA `c70-12` ; [c70-profiles] ; quiz pE `c70-e-6` |

## Sources utilisées
S1 à S20 de sources.json : CIM-10-GM 2024 (C69–C72 et C76–C80), EANO 2021, OMS 2021, cIMPACT-NOW 8, Di Nunno 2022, EANO et société européenne d'oncologie médicale 2023, informations professionnelles suisses d'Androcur-50 (juin 2022), d'Avastin (mai 2026), de la dexaméthasone Galepharm (janvier 2022) et du lévétiracétam Sandoz (avril 2023), quatre résumés suisses, guide suisse d'aptitude à la conduite (2019), registre des cancers de Zurich (2025), aide du registre national des cancers (état au 23 mai 2022), revue sur les simulateurs du méningiome (2019), objectifs PROFILES 2017. Aucune donnée extérieure au dossier.

## Lacunes (reportées dans la fenêtre c70-lacunes et la section Sources)
Aucune recommandation suisse de neuro-oncologie en texte intégral ni donnée suisse propre au grade 3 ; recommandation européenne de 2021 sur les complications neurologiques inaccessible (choix de l'antiépileptique, sevrage des corticoïdes, thromboprophylaxie non sourcés) ; tumeur fibreuse solitaire maligne et mélanome méningé non développés cliniquement ; immunohistochimie, grossesse, Suva, assurance-invalidité, remboursement non documentés ; code de morphologie exact par grade non lu ; sarcoïdose durale sans section lue ; chiffres de récidive contradictoires dans la source, présentés comme tels. Déductions pédagogiques signalées dans le texte : surveillance de la kaliémie sous dexaméthasone, motif de la prolongation de l'interdiction de conduire, rattachement des situations cliniques de PROFILES à C70.

## Auto-contrôle
HTML équilibré sur l'ensemble des quatre fichiers de chapitre ; identifiants uniques, préfixés `c70-` ; 49 clés de fenêtres toutes référencées et définies, aucune inutilisée ; couvertures Pareto toutes valides ; aucune abréviation hors glossaire (`build_medina.audit` exécuté sur copie de travail du glossaire, résultat `{}`). La construction complète et le test navigateur n'ont pas été lancés (dossier racine interdit).

Audit différé — revue IA, distincte d'une validation médicale humaine.
