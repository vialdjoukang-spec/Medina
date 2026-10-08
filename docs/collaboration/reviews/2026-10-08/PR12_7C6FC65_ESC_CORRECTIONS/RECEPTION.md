# Réception Claude — corrections ciblées des lots ESC 2026

PR #12, tête `7c6fc659c3306b1fa0ba6cd82bd37ec68c400083`; main de référence `fa8fe70a2832f5fc83e139b3c3cc0e1e11fa059f`.

Claude corrige les huit rapports ESC, la proposition I35 relative au furosémide, son manifeste et son contrôle natif. Les treize objets sont archivés sans modification sous l’empreinte d’arbre `78d98f1cbf1cc2c17e21ab38055f37474f34ef19`.

## Constat ciblé

- Les anciennes valeurs `null` ont disparu des huit rapports. Elles sont remplacées par la synthèse de levée côté producteur et les chemins de preuve.
- Tous les rapports conservent `pending_exhaustive_review` et demandent une contrelecture indépendante.
- I35 passe de `39e59a6c…` à `44a60bfa…`. Le manifeste et le contrôle natif utilisent la même empreinte. Le journal producteur déclare 3 269 contrôles, zéro échec et zéro erreur.
- La nouvelle formulation I35 — 40 mg IV chez le patient naïf de diurétique, ou deux fois la dose orale habituelle chez l’utilisateur chronique — concorde avec la section 7.5.3 et la figure 15 des recommandations ESC 2026 (doi:10.1093/eurheartj/ehag100). La figure précise toutefois qu’une dose initiale plus élevée peut être nécessaire en cas de maladie rénale chronique ; cette limite ne figure pas dans la ligne proposée.
- L’expression « FEVG modérément réduite » n’est pas retrouvée dans les sources I40 de `main` ; l’écart précédemment signalé ne concerne donc pas ce lot.

Sources primaires : [European Heart Journal — ESC 2026](https://academic.oup.com/eurheartj/advance-article/doi/10.1093/eurheartj/ehag100/8766302) ; [PubMed 42661420](https://pubmed.ncbi.nlm.nih.gov/42661420/).

## Décision

État : **repéré, reçu et archivé ; non intégré, non contrôlé techniquement de façon indépendante et non publié comme contenu de cours**.

I83 reste le chapitre actif. Les huit lots ESC demeurent en attente de sa clôture et d’une contrelecture chapitre par chapitre. La levée MED-01 reste déclarative côté producteur, les PDF complets ayant été lus localement mais non versionnés. La question I42 « Chronic HF stage B, C, D » reste non tranchée. Aucune complétude CIM-11 n’est établie.

Aucune attribution, aucun chapitre actif et aucun fichier canonique n’a été modifié.

[Reçu JSON](../../../receipts/CLAUDE_ESC_7C6FC65_CORRECTIONS_RECEPTION_2026-10-08.json)
