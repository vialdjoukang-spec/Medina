# Rapport de rédaction — I66 (cycle Betta 32, leçon 2, agent C32-A1-NEUR, Sonnet 5.5)

I66 — Occlusion et sténose des artères cérébrales, n'entraînant pas un infarctus cérébral (N-05-Neurologie). État au 14.10.2026.

## Fichiers produits
- chapters/I66/I66_a.html : 31839 octets
- chapters/I66/I66_b.html : 30051 octets
- chapters/I66/I66_c.html : 30966 octets
- chapters/I66/I66_d.html : 13524 octets
- chapters/I66/I66_pop1.html : 19802 octets
- chapters/I66/I66_pop2.html : 22759 octets
- glossary/i66.py : 5585 octets

Empreintes SHA-256 :
- `I66_a.html` : d42dc687d576f1a6c4f325423ec452bbd99398836e21b907a867b2d5e2bb40d3
- `I66_b.html` : 92bd7679db4fc9213973f1c95c7c7f20c7726118425448b5c511d5e6fb747c6b
- `I66_c.html` : 993e37387b302c19401e5f7af2065a6ea5d3fb8af99575de4dd464668730929a
- `I66_d.html` : 894ad9201fbc329da8bd81c2b54ba69ae7df8bdaf16d0cf8084f6313a969b633
- `I66_pop1.html` : 8760e27c77e23a5227b691c5391e7a98b275210d2408ece2d2058436c88bc670
- `I66_pop2.html` : 4c16292adc70a5ad3831d3a6f303260b62be4a242105ea5217938b1a01920b04

## Contenu
- Onglet Pathologie : 15 îlots (0 à 14), dont critères formels (alert) puis paramètres clés (key) en dernier îlot ; 3 Pareto ; 2 figures SVG (mécanismes ; frontière I65/I66 et parois) plus 2 en sciences.
- Onglet Examens : 5 îlots (indication, fiches d'interprétation, configurations de la paroi, marqueurs de risque, 4 quiz de cas) ; gold standard nommé (angiographie numérisée).
- Onglet Sciences : Anatomie, Histologie, Physiologie, Biochimie, Génétique (une corrélation clinique par science, schémas).
- Onglet Pharmacologie : 5 îlots, 6 monographies en fenêtres, 1 quiz.
- 48 fenêtres (38 explicatives, 10 Pareto), 5 quiz, 161 mots verts dans les quatre onglets, 4 schémas SVG.

## Sources utilisées
Uniquement le dossier de recherche (S1 à S29, `sources.json`) : CIM-10-GM 2024 ; ESO maladie athéroscléreuse intracrânienne 2022, accident ischémique transitoire 2021, prévention secondaire 2022, moyamoya 2023, dissection 2021 ; revue bernoise 2021 (résumé) ; WASID, SAMMPRIS, VISSIT (via ESO), CASSISS, SONIA, CLAIR, Cochrane 2023 ; séries lausannoises et parisiennes ; notices suisses Aspirine Cardio, Plavix, Sortis, Brilique (AIPS, 14.10.2026).

## Lacunes reprises sans les combler
Aucune recommandation suisse spécifique ; seuils de vitesse du Doppler transcrânien absents ; sensibilité et spécificité de l'angio-tomodensitométrie non chiffrées ; épidémiologie suisse absente ; sémiologie de l'accident transitoire par territoire extrapolée des séries d'infarctus (dit dans le texte) ; composantes du score ABCD2 non reprises (absentes du dossier) ; cilostazol non retrouvé dans la base suisse, ticagrélor sans indication d'accident vasculaire cérébral ; divergence des cibles de LDL (1,4 contre 1,8 mmol/L) présentée dans une fenêtre dédiée ; ézétimibe et inhibiteurs de la PCSK9 non consultés dans l'information suisse ; aucun calendrier de suivi ni de surveillance biologique dans les sources ; CIM-11 non établie.

## Auto-contrôle (cahier W)
- HTML bien formé (analyse de balises : aucune erreur, aucune balise ouverte), identifiants uniques et tous préfixés `i66-`.
- Toutes les clés `data-k` ont leur `template data-pop` ; aucune fenêtre inutilisée ; chaque `data-cover` de Pareto pointe vers des îlots existants.
- Glossaire `glossary/i66.py` : entrées conditionnelles (aucun terme existant écrasé), 14 abréviations définies ; noms d'essais écrits honnêtement, sans développement lettre à lettre inventé.
- `build_medina.py` exécuté sur une copie de travail hors dépôt : `I66 non couvertes: 0`. Le test navigateur `test_preview.py` échoue sur une ressource (`lesson-core.js`) absente de l'environnement, y compris pour D50 : non attribuable à I66.
- Aucun fichier touché hors de ce dossier (ni chapters/, glossary/, chapters.json de la racine, ni git).

Audit différé — revue IA, distincte d'une validation médicale humaine.
