# Rapport de rédaction — I67 (cycle Betta 33, leçon 1, agent C33-A1-NEUR, Sonnet 5.5)

I67 — Autres maladies cérébrovasculaires (N-05-Neurologie). État au 15.10.2026. Audit différé — revue IA, distincte d’une validation médicale humaine.

## Fichiers produits
- chapters/I67/I67_a.html : 37228 octets — SHA-256 `d571a96775a3b95b4f750606fb3560db8c95cf1e661103be62dfea1b84498644`
- chapters/I67/I67_b.html : 33796 octets — SHA-256 `011a6dd38b83fc60040262a978f497c929f5b28ce02dd82095651db2dd350df2`
- chapters/I67/I67_c.html : 32351 octets — SHA-256 `c41a02032b34dcd5dc1b8830fe941057689151dd5d69ec267c83f13c08de21b6`
- chapters/I67/I67_d.html : 13655 octets — SHA-256 `cce44d969c196f01e9dfa4172a9c80da1f3174158cf5a7280d754023e281611a`
- chapters/I67/I67_pop1.html : 19244 octets — SHA-256 `8b96a93225fb533aca9785627961040cafd728d0add747ae99c9873cc2ea7aa9`
- chapters/I67/I67_pop2.html : 19584 octets — SHA-256 `0fa0e923c2e34b1e5d407bcf7f3572bf524f2cca4892cd96c7463d64524878e4`
- glossary/i67.py : 6804 octets

## Contenu
- Onglet Pathologie : 16 îlots (0 à 15), dont critères formels (alert) puis paramètres clés (key) en dernier îlot ; 3 Pareto ; 1 schéma SVG (quatre structures atteintes) ; tableaux par entité (classification, épidémiologie, facteurs de la thrombose veineuse, traitement, urgences).
- Onglet Examens : 5 îlots (question-examen, thrombose veineuse, urgence hypertensive/PRES/SVCR, artères, 5 quiz) ; gold standard nommé (angiographie par soustraction numérique).
- Onglet Sciences : Anatomie, Histologie, Physiologie, Biochimie, Génétique (corrélations cliniques, 5 Pareto).
- Onglet Pharmacologie : 5 îlots (classes, doses, interactions, effets indésirables, à éviter), 1 Pareto.
- 45 fenêtres (35 explicatives, 10 Pareto), 5 quiz, environ 15 300 mots au total.

## Sources utilisées
Uniquement le dossier de recherche (S1 à S24, `sources.json`) : CIM-10-GM 2024 ; S2k DACH 2023 sur la thrombose veineuse cérébrale et sa synthèse 2024 ; ESO thrombose veineuse 2017 (résumé), dissection 2021, anévrisme non rompu 2022, hémorragie sous-arachnoïdienne 2026, petites artères 2021 et 2024, moyamoya 2023, angéite primitive 2023 ; document de position ESC 2019 ; revues PRES/SVCR ; notices suisses Nimotop (perfusion, comprimés), Clexane, Pradaxa.

## Lacunes reprises sans les combler
Aucune recommandation propre à une société suisse ; ESO thrombose veineuse 2017 en résumé (fréquences cliniques absentes) ; dose et durée de la nimodipine orale selon l’ESO ; fistule artério-veineuse durale (I67.11), critères ICHD-3, score RCVS2, PHASES, composantes d’ELAPSS, stades de Suzuki non sourcés ; I67.2 renvoyée au cours I66, I67.88 et I67.9 codage seulement ; codage CIM du SVCR, du PRES et de l’hypertension maligne non vérifié ; notices suisses du labétalol, de la nicardipine, de l’urapidil, du nitroprussiate et des immunosuppresseurs non lues (doses de l’ESC citées comme telles) ; effets indésirables et surveillance biologique absents du dossier ; CIM-11 non établie. Contentieux nimodipine (ESO 2026 orale / notice suisse perfusion puis oral) présenté dans une fenêtre dédiée.

## Auto-contrôle (cahier W)
- HTML bien formé (analyse de balises : aucune erreur, aucune balise ouverte), identifiants uniques, tous préfixés `i67-`.
- Les 45 clés `data-k` ont chacune leur `template data-pop` ; aucune fenêtre inutilisée ; chaque `data-cover` de Pareto pointe vers des îlots existants (calcul par `build_medina.pareto_ratios`).
- Glossaire `glossary/i67.py` : 22 entrées conditionnelles (aucun terme existant écrasé) ; noms d’essais, de scores et de gènes non développés dans le dossier écrits honnêtement ; `build_medina.audit` sur une copie en mémoire (transform, pareto, wrap) : abréviations non couvertes = 0.
- Aucun fichier touché hors de ce dossier (ni chapters/, glossary/, chapters.json de la racine, ni git).
- Points de déduction pédagogique signalés dans le texte comme tels (raison des mesures de PA répétées, héparine non fractionnée avant procédure, lecture de la nimodipine sur la létalité, définition générale de la réserve cérébrovasculaire).
