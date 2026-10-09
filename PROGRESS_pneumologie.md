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
