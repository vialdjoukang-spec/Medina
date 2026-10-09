# A16 — contrôle technique et visuel

Contrôle du 9 octobre 2026, preview `dist/apercus/infectiologie.html`, sources de travail I-03 `sources/chapters/A16`. Revue technique uniquement ; aucune validation médicale et aucune édition clinique.

Les sept fichiers HTML assemblés sont équilibrés. Les quatre panneaux pA/pE/pS/pP, les 14 îlots de pathologie, cinq d’examens, six de sciences et cinq de pharmacologie sont présents. Les 24 ancres ont des cibles uniques. Les six sous-onglets scientifiques correspondent chacun à leur panneau. Aucun identifiant dupliqué, aucune classe hors contrat, aucun placeholder et aucune cible Pareto manquante.

Les 38 appels data-k correspondent à 37 fenêtres uniques ; un appel réutilise sa fenêtre. Aucune fenêtre manquante ou dupliquée. Cinq quiz sont présents, dont trois en examens. Le manifeste contient les sept fichiers HTML A16 et glossary/a16.py ; les huit SHA-256 correspondent aux fichiers.

Chromium /usr/bin/chromium a été exécuté à 390, 768 et 1440 px (hauteur 900). Les quatre panneaux, les six sous-onglets scientifiques, une fenêtre contextuelle (ouverture/fermeture) et le retour d’un quiz fonctionnent aux trois largeurs. La largeur du document égale celle du viewport ; aucun élément visible dépassant le viewport et aucune erreur JavaScript relevés. Captures et mesures : /workspace/work/a16-qa-captures/result.json et PNG des panneaux et fenêtres.

Aucun défaut technique bloquant détecté sur cette version. Serveur local dist : http://127.0.0.1:8765, session 88836 laissée active pour les captures du coordinateur.
