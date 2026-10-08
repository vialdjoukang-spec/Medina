# Rapport Pharmacologie — J45 — Asthme (P-02-Pneumologie)

## 1. Fichiers modifiés
- **`J45_d.html`** : passe de 965 à environ 8100 mots, en 8 îlots. Les identifiants p-1 à p-4 sont conservés ; p-5 à p-8 sont nouveaux.
  - p-1 : classes et mécanismes, produits autorisés en Suisse.
  - p-2 : GINA 2026 (voies 1 et 2, enfant) et choix du dispositif.
  - p-3 : doses (corticostéroïde inhalé chez l'adulte, l'enfant de 6 à 11 ans et avant 5 ans ; AIR/MART).
  - p-4 : interactions (`alert`), surveillance mécanistique, médicaments à éviter.
  - p-5 : exacerbation et J46.
  - p-6 : asthme sévère, avec un tableau des 7 biothérapies.
  - p-7 : grossesse, enfant, sujet âgé.
  - p-8 : 2 quiz, critères formels (`div.alert`), paramètres clés (`div.key`), Pareto déplacé ici.
- **`J45_pop3.html`** : 10 fiches réécrites et 3 nouvelles (`j45-d-laba`, `j45-d-ipra`, `j45-d-o2`). Aucune clé supprimée.

## 2. Matrice des corrections
| Passage | Problème | Correction | Source | Accès |
|---|---|---|---|---|
| Voie 2 | Le SABA seul servait de secours. | GINA 2026 ajoute l'AIR budésonide-salbutamol. L'association n'est pas autorisée en Suisse, d'où des inhalateurs séparés. | GINA 2026 p.20-21, 92-96 ; Swissmedic 30.09.2026 | Texte intégral ; fichier |
| MART | La notion de « maximum 12 / 8 » était obsolète. | Consultation au-delà de 12 inhalations en 24 h (8 chez l'enfant de 6 à 11 ans). Étiquetages européens séparés. Équivalence 200/6 = 160/4,5 µg. | GINA encadré 4-8 ; SmPC britannique Symbicort | Texte intégral ; page lue |
| Doses de corticostéroïde inhalé | Le tableau était incomplet. | Béclométasone standard, mométasone, enfant de 6 à 11 ans, enfant de 5 ans ou moins. | GINA encadrés 4-2 et 11-3 | Texte intégral |
| Salbutamol en crise | « 4-10 bouffées toutes les 20 min » | 4 / 4-6 / 6-10 bouffées selon la gravité ; toxicité lactique. | GINA encadrés 9-4 et 9-6 | Algorithmes lus |
| Oxygène | Le point était absent. | Pas d'oxygène si la saturation est ≥ 92 % ; cible 92-95 % (≥ 92 % à 5 ans ou moins). | GINA p.20, 180 | Texte intégral |
| Croissance | « ~1 cm la première année » | 0,48 cm la première année ; taille adulte −1,2 cm ; effet non progressif. | Cochrane 2014 ; Kelly, NEJM 2012 | Résumés |
| Fénotérol | « GINA 2025 » | Non recommandé par GINA 2026 ; Berodual N reste autorisé en Suisse. | GINA p.100 ; Swissmedic | Texte intégral |
| Tiotropium | La disponibilité était présentée sans réserve. | Spiriva Respimat est enregistré pour la BPCO ; Trimbow 172/5/9 porte l'indication asthme. | Swissmedic | Fichier |
| Théophylline | La zone 10-20 mg/L n'était pas sourcée. | Zone retirée ; mécanismes ajoutés ; seule l'aminophylline injectable est autorisée en Suisse. | Barnes, AJRCCM 2013 | Résumé |
| Biothérapies | Les âges, critères et prédicteurs manquaient. | Tableau complet ; doses de charge du dupilumab ; omalizumab 75-600 mg ; dépémokimab non autorisé en Suisse. | GINA p.161-166 ; SmPC européennes | Texte intégral |
| Azithromycine | L'effet n'était pas chiffré. | −41 % ; diarrhée ; au moins 6 mois ; ECG au début et à 1 mois. | Gibson, Lancet 2017 | Résumé |
| Corticostéroïde oral | Le seuil cumulatif n'avait pas de source. | 0,5-1 g, soit environ 4 cures ; lien observationnel discuté. | Price 2018 ; GINA encadré 9-3 | Résumé |
| Bêta-2 agoniste de longue durée seul | L'interdiction n'était pas justifiée. | SMART 2006 : 13 décès contre 3. | Nelson, Chest 2006 | Résumé |
| Interactions | Il manquait les mécanismes. | Mécanismes ajoutés ; consigne pour le nirmatrelvir-ritonavir. | GINA p.46, 130 | Texte intégral |

## 3. Affirmations confirmées sans changement
- Mécanismes du corticostéroïde inhalé et du bêta-2 agoniste.
- Doses de budésonide, béclométasone extrafine, ciclésonide et fluticasone.
- Prednisone 40-50 mg pendant 5-7 jours ; enfant 1-2 mg/kg, au plus 40 mg.
- Magnésium 2 g en 20 minutes ; tiotropium 2 × 2,5 µg ; doses de montélukast.
- SYGMA et Novel START ; mépolizumab, benralizumab, tézépélumab ; réévaluation à 4 mois.

## 4. Propositions hors périmètre
1. **`J45_pop4.html`, `pareto-j45-pharma`.**
   - Remplacer `data-cover="j45-p-1,j45-p-2,j45-p-3,j45-p-4"` par `data-cover="j45-p-1,j45-p-2,j45-p-3,j45-p-4,j45-p-5,j45-p-6,j45-p-7,j45-p-8"`.
   - Remplacer la `<ul>` par les points suivants :
     - Tout asthmatique reçoit un corticostéroïde inhalé ; un bêta-2 agoniste de longue durée ne se prescrit jamais seul ; seul le formotérol associé sert de secours et de MART.
     - En Suisse, la voie 2 utilise un traitement de fond et du salbutamol séparés.
     - Doses faibles chez l'adulte : budésonide 200-400 µg, béclométasone extrafine 100-200 µg, fluticasone propionate 100-250 µg ; environ deux fois moins chez l'enfant de 6 à 11 ans.
     - Budésonide-formotérol 200/6 µg = 160/4,5 µg délivrés ; consulter au-delà de 12 inhalations en 24 heures (8 chez l'enfant).
     - Crise : salbutamol 4, 4-6 ou 6-10 bouffées ; oxygène si &lt; 92 %, cible 92-95 % ; prednisone 40-50 mg pendant 5 à 7 jours ; magnésium 2 g si échec.
     - Biothérapie choisie selon les éosinophiles, la FeNO, l'allergie et les comorbidités, jugée à 4 mois ; prednisone d'entretien en dernier recours.
     - Interactions : bêta-2 agonistes avec hypokaliémiants ; CYP3A4 avec fluticasone ou budésonide ; théophylline avec CYP1A2 ; bêtabloquants non sélectifs.
     - Montélukast : risque neuropsychiatrique ; corticostéroïde oral toxique dès 0,5-1 g cumulés.
2. **`J45_b.html`, îlot 8.2, paragraphe « Ipratropium ».** Après « …jusqu'à trois fois. », ajouter : « En Suisse, l'ipratropium seul n'est autorisé qu'en solution pour nébuliseur (0,25 mg par dose) ; des associations salbutamol-ipratropium pour nébuliseur existent. » Source : liste Swissmedic au 30.09.2026.
3. **`J45_b.html`, îlot 8.2, paragraphe « Sulfate de magnésium ».** Après « 2 g en 20 minutes chez l'adulte », ajouter : « ; chez l'enfant de 2 ans et plus, 40 à 50 mg/kg (au plus 2 g) en 20 à 60 minutes ». Source : GINA 2026 p.220.

## 5. Points non vérifiables et réserves
- **Informations professionnelles suisses inaccessibles** (compendium.ch et swissmedicinfo exigent une connexion). Les posologies suisses et les limitations de remboursement ne sont pas vérifiées. La disponibilité repose uniquement sur la liste Swissmedic des autorisations.
- **Non revérifiés :** délais d'action du salbutamol et du formotérol ; apoptose sous benralizumab ; mécanisme de l'hypoglycémie néonatale ; « budésonide le mieux documenté » pendant la grossesse ; place du cobicistat parmi les inhibiteurs ; mise en garde de la FDA (sources secondaires et DailyMed).
- **Pour l'assembleur :** l'îlot p-2 a été renommé, mais l'ancre de `j45-j-technique` reste valable.

## 6. Contrôles
- `verifier_sigles` sur `J45_d.html` et `J45_pop3.html` : `{}`.
- Toutes les clés `data-k` de mes fichiers ont leur fenêtre.
- Les 4 justifications ancrées dans `J45_d.html` compilent.
- `test_v7.py --static J45` : échec causé par d'autres fichiers (`J45_c` contient des initiales d'auteurs non couvertes ; `pareto-j45-sci` manque). La justification `j45-j-variabilite` est ambiguë dans `J45_a`.
