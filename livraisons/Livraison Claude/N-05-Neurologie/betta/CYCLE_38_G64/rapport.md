# Rapport de rédaction G64 — cycle Betta 38, leçon 2 (C38-A4-NEUR, Sonnet 5.5)

Audit différé — revue IA, distincte d'une validation médicale humaine.

## Fichiers (octets)
- chapters/G64/G64_a.html 21 906 (en-tête, onglets, plan, parties 0 à 6)
- chapters/G64/G64_b.html 15 612 (parties 7 à 12, dont critères formels `div.alert` puis paramètres clés `div.key`)
- chapters/G64/G64_c.html 21 075 (onglet Examens e-1 à e-6 ; onglet Sciences : Anatomie, Histologie, Physiologie, Biochimie)
- chapters/G64/G64_d.html 11 994 (onglet Pharmacologie p-1 à p-6)
- chapters/G64/G64_pop1.html 13 232 et G64_pop2.html 13 796 : 34 fenêtres (20 explicatives, 14 Pareto `pareto-g64-*`)
- glossary/g64.py : 43 abréviations, définies lettre à lettre
- Total HTML : 97 615 octets.

## Sources utilisées
S1 à S12 de sources.json, uniquement. Aucune donnée extérieure au dossier de recherche. Posologies : S10 (prégabaline) et S11 (duloxétine) ; NNT/NNH : S9 ; vascularite : S7 ; biopsie cutanée : S8.

## Auto-contrôle du cahier W
- HTML équilibré (balises) sur chapitre et fenêtres : oui.
- Identifiants uniques, tous préfixés `g64-` (hors pA, pE, pS, pP) : oui.
- Toute clé `data-k` référencée existe (34 fenêtres, aucune manquante, aucune orpheline) ; onglets Sciences et `data-cover` Pareto valides : oui.
- Abréviations : chaque sigle visible est un bouton lié au glossaire ; restent hors glossaire seulement des codes CIM, des vitamines (B1, B6), C3 et des chiffres romains.
- `build_medina.audit()` non exécuté (ne touche pas la racine) ; contrôle équivalent fait par script local.

## Lacunes
- Pas de recommandation SSN ni Swiss Medical Forum en texte intégral ; S5, S6, S12 lues en résumé seul.
- Physiologie normale du nerf non sourcée : l'onglet Physiologie se limite à l'excitabilité nociceptive et à l'ischémie, et le dit.
- FI de l'amitriptyline non relue : aucune dose de tricyclique ; épidémiologie suisse absente ; incidence/prévalence de la PIDC non précisée ; événement mesuré par le NNH non précisé.
- Traitement du SGB et du POEMS absent du dossier : non cité.
- Déduction signalée dans le texte : lecture de G64 comme démarche devant une atteinte non étiquetée ; vignette et valeurs fictives (marquées).
- data-evidence absent : le registre de preuves n'est pas attribué avant injection.
