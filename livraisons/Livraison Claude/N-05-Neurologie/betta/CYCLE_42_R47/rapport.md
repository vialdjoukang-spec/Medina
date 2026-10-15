# R47 — Troubles du langage, non classés ailleurs · rapport de rédaction (cycle Betta 42, leçon 1)

Agent C42-A4-NEUR (rédaction, Sonnet 5.5) · 15.10.2026 · fragment N-05-Neurologie · porte de vérité : `VÉRITÉ OK · CYCLE_42_R47` avant et après rédaction.

## Fichiers livrés (dossier de la leçon uniquement)
| Fichier | Contenu | Taille |
|---|---|---|
| `chapters/R47/R47_a.html` | en-tête, 4 onglets, panneau pA îlots 0–7 | 27 858 o |
| `chapters/R47/R47_b.html` | pA îlots 8–15, références `src`, pager | 26 616 o |
| `chapters/R47/R47_c.html` | pE (e-1 à e-5, 5 quiz) et pS (anatomie, physiologie, neuropathologie, 3 figures SVG) | 28 254 o |
| `chapters/R47/R47_d.html` | pP (p-1 à p-3), fermeture du chapitre | 5 937 o |
| `chapters/R47/R47_pop1.html`, `_pop2.html` | 44 fenêtres, dont 9 Pareto | 22 534 o + 23 765 o |
| `glossary/r47.py` | 5 abréviations et sigles, 5 noms propres, 16 codes CIM-10-GM (entrées conditionnelles) | 4 120 o |

Volumes : environ 9 800 mots de cours, 4 700 mots de fenêtres, 27 îlots, 44 fenêtres, 5 quiz de cas cliniques (vignettes fictives), 3 figures SVG noir et blanc légendées, 9 boutons Pareto.

## Matrice de complétude (reprise de `recherche.md`, avec onglet et identifiant HTML)
| Rubrique | Statut | Onglet · identifiant HTML |
|---|---|---|
| 1. Question clinique et enjeu pour l'examen fédéral | ✔ | pA · `r47-0`, `r47-14` |
| 2. Définition et périmètre CIM-10-GM | ✔ | pA · `r47-1` (tableau des sous-codes) ; fenêtres `r47-cim`, `r47-aphasie-def`, `r47-dysarthrie-def`, `r47-apraxie` |
| 3. Classifications et stades | ✔ | pA · `r47-2` (2.1 à 2.4) ; pS · `r47-s-neuro-cours` (figure 3) ; fenêtres `r47-syndromes`, `r47-huber`, `r47-app`, `r47-dysarthries`, `r47-art` |
| 4. Épidémiologie suisse puis européenne | ✔ (dysarthrie : LACUNE) | pA · `r47-3` ; fenêtres `r47-bale`, `r47-calcul-bale`, `r47-copenhague` |
| 5. Normal → pathologique | ✔ | pA · `r47-4` ; pS · `r47-s-anat-cours` (figure 1), `r47-s-physio-cours` (figure 2) ; fenêtres `r47-lateralisation`, `r47-dysarthrie-topo`, `r47-recuperation` |
| 6. Étiologies et facteurs de risque | ✔ | pA · `r47-5` ; pS · `r47-s-neuro-cours` ; fenêtre `r47-corticoides` |
| 7. Anamnèse et symptômes | ✔ (fréquences des symptômes : LACUNE) | pA · `r47-6` ; fenêtre `r47-aura` |
| 8. Examen clinique | ✔ (sensibilité et spécificité des signes isolés : LACUNE) | pA · `r47-7` ; fenêtre `r47-examen-lit` |
| 9. Drapeaux rouges et urgences | ✔ | pA · `r47-9` (encadré `alert` et tableau) ; fenêtres `r47-alteplase`, `r47-eso-thrombolyse`, `r47-ait-dysarthrie` |
| 10. Examens complémentaires | ✔ (seuil du Language Screening Test : LACUNE) | pE · `r47-e-1` à `r47-e-4` ; fenêtres `r47-last`, `r47-last-de`, `r47-art`, `r47-simulateurs` |
| 11. Diagnostic différentiel | ✔ | pA · `r47-8` (tableau) ; pE · `r47-e-3` ; fenêtre `r47-simulateurs` |
| 12. Prise en charge suisse | ✔ (médicaments : une seule information professionnelle lue) | pA · `r47-10` (10.1 à 10.4) ; pP · `r47-p-1`, `r47-p-2`, `r47-p-3` ; fenêtres `r47-eso-aphasie`, `r47-cochrane`, `r47-rehab-suisse`, `r47-degam`, `r47-stroke-unit` |
| 13. Complications et pronostic | ✔ | pA · `r47-11` ; pS · `r47-s-physio-cours` ; fenêtres `r47-recuperation`, `r47-copenhague` |
| 14. Suivi, prévention, dépistage | ✔ | pA · `r47-12` ; pE · `r47-e-2` |
| 15. Situations particulières | ✔ (grossesse : LACUNE ; insuffisance rénale ou hépatique : LACUNE sur la conduite) | pA · `r47-13` (cartes et cas récapitulatif) ; pP · `r47-p-2` (plus de 80 ans) |
| 16. Spécificités suisses | ✔ (ordonnance sur les prestations, assurance-invalidité : LACUNE) | pA · `r47-14`, `r47-10` (10.1) ; fenêtre `r47-conduite` |
| 17. Critères formels du diagnostic | ✔ | pA · `r47-15` (`div.alert`) ; fenêtres `r47-app`, `r47-aura` |
| 18. Paramètres clés chiffrés | ✔ | pA · `r47-15` (`div.key` avec tableau) |
| 19. Sous-codes CIM-10-GM couverts | ✔ | pA · `r47-1` (R47, R47.0, R47.1, R47.8, R48, R49) ; fenêtre `r47-cim` ; glossaire `r47.py` |
| 20. Points d'examen fédéral | ✔ | pA · `r47-14` (six pièges) ; pE · `r47-e-5` (cas 1 à 5) ; fenêtres `r47-profiles`, `r47-mnemo` ; Pareto `pareto-r47-synthese` |

## Sources utilisées
Les 29 sources de `sources.json` sont mobilisées : S1–S2 (périmètre), S3 (revue suisse, texte intégral), S4 (Bâle-Ville), S5–S6 (dépistage), S7 (European Stroke Organisation 2025, texte intégral), S8 (Cochrane), S9 (Copenhague), S10 (aphasie primaire progressive), S11–S16, S19–S20, S24–S26 (résumés ou sections), S17 (information professionnelle Actilyse®, juin 2025), S18 (European Stroke Organisation 2021, section), S21–S22 (CHUV, Réseau hospitalier neuchâtelois), S23 (manuel MSD : sémiologie et anatomie seulement), S27 (article de logopédistes, fréquences de seconde main), S28 (classification des céphalées), S29 (PROFILES). Chaque fenêtre porte un bloc « Limite » qui rappelle le niveau de lecture (résumé, section, texte intégral).

## Lacunes signalées dans la leçon (requêtes tentées : voir `recherche.md`)
- Ligne directrice allemande sur les dysarthries (AWMF 030/103) et sur l'aphasie (030/090), DEGAM « Schlaganfall » : non lues ; fréquences de séances rapportées de seconde main et étiquetées comme telles (`r47-degam`).
- Ordonnance sur les prestations (logopédie), assurance-invalidité, guide d'aptitude à la conduite : aucune règle de remboursement ni de prestation n'est énoncée (îlot `r47-14`).
- Seuil pathologique du Language Screening Test ; sensibilité et spécificité des signes cliniques isolés ; prévalence de la dysarthrie ; fréquences des symptômes ; traits sonores de chaque type de dysarthrie ; liste complète des signes d'appui des variantes de l'aphasie primaire progressive ; définition formelle de l'apraxie de la parole.
- Grossesse ; insuffisance rénale ou hépatique pour la conduite thérapeutique ; aucune revue de Swiss Medical Forum ou de Revue Médicale Suisse sur l'aphasie lue.
- Pharmacologie : seule l'altéplase est monographiée (sections lues de l'information professionnelle). Aucune interaction, aucun « médicament à éviter » ni tableau de doses supplémentaire n'est affirmé, faute de source ; l'onglet le dit explicitement (`r47-p-3`).
- Divergence déclarée, non tranchée : l'information professionnelle (juin 2025) cite les symptômes mineurs ou rapidement améliorés parmi les contre-indications, la recommandation européenne de 2021 recommande la thrombolyse pour un accident vasculaire cérébral mineur invalidant (`r47-9`, `r47-p-2`, `r47-eso-thrombolyse`).

## Choix de rédaction à signaler à l'auditeur
- Développements de sigles (Language Screening Test, Boston Diagnostic Aphasia Examination, CIAT, MIT, ICHD-3) : terminologie usuelle, hors dossier ; pour CIAT et MIT, le glossaire précise que la revue lue n'emploie que le sigle et que le protocole n'est pas détaillé.
- L'ordre en quatre étapes de la démarche diagnostique (îlot `r47-8`) est une synthèse pédagogique des sources, annoncée comme telle ; le moyen mnémotechnique `r47-mnemo` est étiqueté « aide pédagogique, non critère officiel ».
- L'association des régions d'imagerie aux variantes de l'aphasie primaire progressive suit l'ordre de présentation du dossier (fenêtre `r47-app`, figure 3).
- Le calcul de dose de l'altéplase pour 70 kg (`r47-calcul-alteplase`) et la vérification 80 ÷ 269 (`r47-calcul-bale`) sont des calculs illustratifs à partir de chiffres sourcés.
- Les initiales d'auteurs ont été omises des références pour éviter des entrées de glossaire sans objet.
- Entrées existantes du glossaire du dépôt (PROFILES, NIHSS, CHUV, BfArM) : elles sont reprises telles quelles et, pour PROFILES, la définition existante vient d'une autre leçon ; l'entrée n'est pas écrasée (règle de non-mutation).

## Auto-contrôle (cahier W)
- HTML bien formé : concaténation `_a` à `_d` et fenêtres vérifiées par analyseur (aucune balise orpheline).
- Identifiants uniques et préfixés `r47-` ; 44 clés de fenêtre référencées, toutes présentes, aucune fenêtre inutilisée.
- Construction de contrôle dans une copie hors dépôt (`build_medina.py R47`) : `R47 non couvertes: 0`, aucune erreur Pareto.
- Contrôle navigateur (copie hors dépôt) : 35 fenêtres vertes et 26 abréviations ouvertes sans « fiche absente », 4 onglets et 3 volets de sciences parcourus, aucune erreur JavaScript propre au cours. Le script `test_preview.py` signale l'échec préexistant `Failed to fetch dynamically imported module: lesson-core.js`, identique sur le cours N17 de référence, absent du dépôt.
- Aucune modification de `chapters/`, `glossary/`, `chapters.json` à la racine ni de git.

Audit différé — revue IA, distincte d'une validation médicale humaine.
