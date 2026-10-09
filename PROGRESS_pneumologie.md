# PROGRESS — P-02-Pneumologie (branche course/pneumologie)

Inventaire de référence : `ANNEXE_FEUILLE_DE_ROUTE.md`, section P-02 (45 catégories CIM-10-GM à trois caractères).

## Fait sur cette branche (09.10.2026)
- J69 — Pneumopathies d’inhalation et atteintes respiratoires toxiques (couvre J68, J69, J70) : brouillon relu (relecture ciblée, une correction posologique), injecté.
- R06 — Dyspnée et anomalies de la respiration : brouillon relu (relecture ciblée), injecté.
- Planches morphologiques GIF (20) : J45, J44, J18, I26, J09, J90, J86, J93, J84, I27, J47, J80, J81, J12, J21, R04, J82, J67, J60, J69 — `assets/planches/pneumologie/`, fenêtres `<CODE>_pop_planche.html`, provenance et licences dans `assets/planches/pneumologie/PROVENANCE.json`.

- C34 — Cancers bronchopulmonaires primitifs (couvre C33, C34, C39) : rédigé et injecté (4 parties, 2 fenêtres de notions et de monographies, planche histologique GIF CC BY-SA 4.0) ; ESMO 2025/2023/2021, IASLC TNM 9, Swiss Cancer Screening Committee, OFS 2025, informations professionnelles Keytruda, Tagrisso, Imfinzi.

## Restant (catégories vides)
- C37/C38, C45 — tumeurs thoraciques
- Q32, Q33, Q34 — malformations congénitales
- R07, R09 — symptômes
- S20, S21, S23, S25, S27, S29 — traumatismes thoraciques
- T27 — brûlure et corrosion des voies respiratoires

## Notes de vérification
- `test_preview.py` signale sur toutes les leçons (J69 compris) une erreur JS d’import de `preview/lesson-core.js` propre à l’environnement de prévisualisation ; fenêtres, abréviations et onglets vérifiés sans fiche absente.
- `tests/audit_sciences.py` échoue sur J09 (référence de comparaison absente), antérieur à cette branche.

## Mise à jour 09.10.2026, 23 h (livraison directe sur main)
- Règle images réelles : 143 schémas SVG dessinés recensés dans les 25 leçons de pneumologie ; 43 remplacés par des images réelles sous licence libre (Wikimedia Commons, CDC ; provenance dans `assets/figures/pneumologie/PROVENANCE.json`), 100 retirés ; 10 algorithmes cliniques (J18, I26, J44, J45, J69) restitués en listes textuelles ; paragraphes de lecture des figures réécrits.
- Règle linguistique appliquée en révision complète : C34, J69.
- Révision linguistique (connecteurs logiques et transitions) FAITE et livrée sur main (09.10.2026, 23 h 50) : R06, J09, J18, J40, J44, J45, I26, I27, J12, J21, J47, J60, J67, J80, J81, J82, J84, J86, J90, J93, J95, J96, R04, R05. Insertion phrase par phrase (outil `conn.py`, gardes ordinaux et étiquettes), chiffres, fenêtres et termes interactifs inchangés ; proportion de phrases sans connecteur ramenée de ~0,8 à 0,12–0,25 selon la leçon ; « Ainsi » varié (Concrètement, De fait).
- Ancres de justifications réalignées (I26, J45) : la mise en minuscule après connecteur cassait `tools/insert_justifications.py` ; vérifier ces ancres après toute retouche.
- Restant, interactivité : aucune fenêtre nouvelle ajoutée pendant la révision linguistique ; densification des fenêtres à faire leçon par leçon.
- Restant, images : rechercher des images réelles sous licence libre là où une figure importante a été retirée sans remplacement.
- Restant, rédaction : C37/C38, C45, Q32–Q34, R07, R09, S20–S29, T27.

## Session du 10.10.2026, 0 h (S02, reprise)
- C45 — Mésothéliome (couvre tout C45 : plèvre, péritoine, péricarde) : rédigé et livré sur main (4 onglets, 16 fenêtres, 4 fenêtres illustrées, 6 images réelles Wikimedia Commons CC BY-SA 3.0/4.0, CC BY 3.0 et domaine public ; provenance dans `assets/figures/pneumologie/PROVENANCE.json`). Sources lues : ESMO 2022 (Popat), ERS/ESTS/EACTS/ESTRO 2020, CheckMate 743 (Lancet 2021 ; données à 3 ans via NICE TA818), RCP Alimta (EMA), Rev Med Suisse 2023, Suva, Unisanté. Jauge federal_exam : 26/40 (65 %).
- Points pour l’audit (C45) : le schéma posologique du nivolumab est celui de l’essai et de l’ESMO (3 mg/kg toutes les 2 semaines) ; le schéma autorisé en Suisse doit être lu dans les FI Opdivo et Yervoy. L’ajout de bévacizumab (option ESMO) n’a pas été vérifié dans la FI suisse. Le pémétrexed est documenté par le RCP européen, pas encore confronté à la FI suisse.

## Balayage rétroactif (ordre du propriétaire, 09.10.2026, 23 h 55)
Contrôle par leçon : phrases complètes (pas de phrase nominale hors cellules de tableau), connecteurs naturels, justification des termes et décisions, images réelles dans les fenêtres, physiopathologie sous chaque élément.

| Leçon | État du balayage |
|---|---|
| J45 | FAIT pour les fenêtres : 62 passages télégraphiques réécrits à la main en phrases complètes justifiées ; 3 images réelles ajoutées dans les fenêtres (éosinophiles, débitmètre de pointe, chambre d’inhalation). RESTE : listes d’algorithme de J45_b (paliers, algorithme diagnostique) à réécrire en phrases ; relecture des connecteurs insérés par script dans J45_a–d. |
| J44, J18, I26, J09, J90, J86, J93, J84, I27, J47, J80, J81, J12, J21, R04, J82, J67, J60, J69, R06, J40, J95, J96, R05, C34 | À FAIRE. Mesure initiale (outil `/workspace/s02w/audit.py`) : une seule image dans les fenêtres par leçon (la planche), aucune pour R06, J40, J95, J96 et R05 ; fenêtres de type Pareto et monographies encore télégraphiques ; connecteurs insérés par script à relire un par un. |
| C45 | Conforme à la rédaction (écrit selon les nouvelles règles). |

## Restant, rédaction (federal_exam)
C37/C38, Q32–Q34, R07/R09, S20–S29, T27 (14 catégories). Images déjà téléchargées pour ces leçons dans `/workspace/s02w/fig` (métadonnées `figmeta.json`) ; outils `expand.py`, `integ.py`, `injpop.py` dans `/workspace/s02w`.
