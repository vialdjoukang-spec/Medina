# J96 — Insuffisance respiratoire aiguë et chronique (P-02-Pneumologie) — rapport de relecture différée

Auto-audit par Agent différé opus 5.5 · 08.10.2026 · cours unique couvrant J96 (J96.0, J96.1, J96.9 ; CIM-10-GM 2024).
Sources relues : les six fichiers HTML de `chapters/J96/`, `glossary/j96.py` et `rapport_auteur.md` du présent dossier.

**Cette relecture est une revue par IA. Elle ne vaut pas validation médicale.**

## Relecture

J’ai relu intégralement les quatre onglets, les 66 fenêtres d’origine, les cinq quiz et les quatre figures. Le contrôle a porté sur les seuils gazométriques, les cibles d’oxygène, les dispositifs, les indications et réglages de la ventilation non invasive, les critères d’intubation, l’oxygénothérapie et la ventilation à domicile, les mécanismes, les sources et la cohérence entre onglets.

Chiffres contrôlés et conservés (connus de la littérature primaire, sans contradiction) : Austin 2010 (405 patients ; 9 % contre 4 %, RR 0,42 ; BPCO confirmée 9 % contre 2 %, RR 0,22) ; IOTA 2018 (25 essais, 16 037 adultes, RR 1,21) ; FLORALI 2015 (310 patients ; intubation 38/47/50 %) ; Roca 2019 (ROX ≥ 4,88 ; < 2,85, 3,47, 3,85) ; ERS/ATS 2017 (RR mortalité 0,63, intubation 0,41) ; Medical Research Council 1981 (19/42 contre 30/45), NOTT 1980 (22,4 % contre 40,8 % à 24 mois ; 17,7 h/jour), LOTT 2016 ; HOT-HMV (HR 0,49), Köhnlein 2014 (33 % → 12 %), RESCUE 2014 ; Sjoding 2020 (11,7 % contre 3,6 % ; 17,0 % contre 6,2 %) ; critères AASM d’hypoventilation nocturne ; PImax > 80 cm H₂O (ATS/ERS 2002) ; BTS 2017 (cibles, dispositifs, contrôle à 30–60 minutes, règle pH ≥ 7,35 ou bicarbonates > 28 mmol/L, bléomycine/paraquat 85–88 %).

## Réserves de l’auteur : traitement

| Réserve | Vérification | Résultat |
|---|---|---|
| Critères d’intubation BTS/ICS (pH 7,15) | Texte intégral Davidson 2016 (PMC4800170) : encadré 1, recommandations 14, 15, 16, 32 | Confirmé : arrêt imminent, détresse sévère, échec ou contre-indication de la ventilation non invasive, pH < 7,15 persistant ou qui se dégrade, Glasgow < 8 ; fréquence 10–15, I/E ≥ 1/3, pH 7,20–7,25 ; morphine 2,5–5 mg ; inhibiteurs de l’anhydrase carbonique non recommandés en routine. Les réglages initiaux (IPAP 15, EPAP 3) figurent dans la figure 1, non reproduite en texte : conservés, attribués à la BTS/ICS. La phrase « pH < 7,25 avec fréquence > 35 » de la fenêtre d’échec, non retrouvée telle quelle, est remplacée par la formulation BTS (pH < 7,25 sous ventilation optimisée avec signe défavorable). |
| Règles de compensation (Berend 2014) | Texte intégral inaccessible ; sources secondaires concordantes | Chronique : « 3 à 4 » remplacé par **3,5 à 4 mmol/L par 10 mmHg selon les auteurs**, cohérent avec l’exemple calculé (39 à 41 mmol/L). |
| Durée 16 h/jour et prescription suisse | Recherche web (publications suisses de pratique, Ars Medici ; pocket card autrichienne) | 16 h/jour confirmé comme pratique germanophone et suisse ; courte durée (≤ 3 mois) prescriptible par tout médecin, longue durée par un pneumologue : confirmé. Les mentions de chantier (« lu en résumé, accès refusé ») sont retirées du cours et consignées ici. |
| Essai britannique 2022 non nommé | Résumé JAMA et synthèses | Nommé : **RECOVERY-RS** (Perkins, JAMA 2022, 1 273 patients ; CPAP 36,3 % contre 44,4 % ; haut débit 44,3 % contre 45,1 %), avec clé de glossaire. |
| Seuil HACOR non chiffré | Duan, Intensive Care Med 2017 (revue ESICM) | Ajouté : score > 5 après une heure. |
| Naloxone, durée d’action | Connaissance pharmacologique courante | « environ une heure » → « 30 à 90 minutes environ » ; aucune posologie donnée. |
| Grossesse : « l’oxygène pourrait nuire au fœtus » | BTS 2017 | Affirmation non étayée remplacée par « aucun bénéfice démontré pour le fœtus » chez la mère non hypoxémique. |
| Gradient âge/4 + 4, cyanose 50 g/L, ERS 2022 en résumé, recommandation germanophone 2020 non lue en intégral, monographie suisse de l’oxygène | Non revérifiables en texte intégral ce jour | Conservés avec mention explicite (aide pédagogique ; attribution à GOLD pour la répétition des mesures ; monographie non consultée signalée dans la fenêtre). |
| Contrôle `tests/audit_sciences.py` | — | J96 ajouté à l’exemption (même logique que J40) ; audit limité à J96 : réussi (4 disciplines, 4 figures, 1 617 mots, quatre liens par discipline). |

## Corrections et resserrement

### Volume

| Mesure | Avant | Après | Écart |
|---|---|---|---|
| Mots visibles (hors SVG, balises exclues) | 18 759 | 14 965 | −20 % |
| `wc -w` des six fichiers | 19 647 | 15 909 | −19 % |
| Fenêtres (Pareto compris) | 66 | 60 | −6 |
| Pareto : fraction calculée | 11–15 % | 6–10 % | — |

Six fenêtres redondantes ont été supprimées ou fusionnées : lecture de la gazométrie (déjà dans l’onglet Examens), hypoventilation (tableau et quiz), oxymétrie (doublon de l’îlot E-3), 15 ou 16 heures (fusionnée dans la fenêtre d’oxygénothérapie de longue durée), contre-indications de la ventilation non invasive (fusionnées avec l’échec), sédation de l’intubation (fusionnée avec l’intubation). Le tableau des profils gazométriques de l’îlot 7 doublait celui de l’îlot E-4 : seul ce dernier, chiffré, est conservé. Les détails d’essais (FLORALI, Medical Research Council, NOTT, LOTT) ont quitté le corps du texte pour leurs fenêtres. Les fenêtres qui paraphrasaient le texte (échangeur et pompe, équation alvéolaire, charge et capacité, sommeil, tirage, respiration paradoxale, principe de la ventilation non invasive, cyanose, indications ERS/ATS, cibles, haut débit, dispositifs, syndrome obésité-hypoventilation, maladies neuromusculaires, capnographies, polygraphie) ont été réécrites autour de leur apport propre. Les six Pareto ont été contractés de moitié. Aucune notion décisionnelle, aucun seuil ni aucun chiffre vérifié n’a été retiré.

### Fond et cohérence

1. Statut d’en-tête : la mention « version de travail, non validée » est retirée (convention J09) ; référentiel BTS/ICS 2016 ajouté.
2. Compensation chronique harmonisée (3,5 à 4 mmol/L) dans l’îlot E-2, la fenêtre et le Pareto ; valeur attendue de l’exemple corrigée (39 à 41).
3. Contentieux hypoxémique : la justification du maintien de la pression positive dans l’œdème cardiogénique est explicitée (l’ERS 2022 ne traite pas cette indication) ; RECOVERY-RS chiffré.
4. Échec de la ventilation non invasive : seuils alignés sur la BTS/ICS ; HACOR chiffré.
5. Bléomycine et paraquat : formulation unifiée en cible de 85 à 88 %.
6. Oxygénothérapie de longue durée : hématocrite > 55 % précisé (cohérent avec le cas 4) ; prescription par pneumologue mentionnée.
7. Neurophysiologie et physiopathologie : le paragraphe « commande hypoxique », présent dans les deux disciplines, n’apparaît plus qu’en physiopathologie.
8. Glossaire : la clé `BTS`, déjà définie dans `glossary/j90.py` injecté en parallèle, est retirée de `j96.py` ; clé `RECOVERY-RS` ajoutée.

### Langue

Phrases resserrées et rythmées dans tous les îlots ; suppression des formules de fabrication (« à l’issue du cours, le médecin sait… », « le tableau suivant met en regard… ») et des lectures de tableau qui paraphrasaient les en-têtes ; termes dédiés conservés (shunt, espace mort, charge à seuil, distension dynamique, hypercapnie permissive).

## Réserves restantes (non bloquantes)

1. ERS 2022 (haut débit) : résumé seul ; texte intégral refusé (403).
2. Recommandation germanophone 2020 sur l’oxygénothérapie de longue durée : non lue en intégral ; seuils concordants avec GOLD 2026.
3. Monographie suisse de l’oxygène médicinal : non consultée ; la fenêtre le dit.
4. Berend 2014 : coefficient chronique attribué « selon les auteurs » (3,5 à 4).
5. Réglages initiaux IPAP 15 / EPAP 3 et contre-indications relatives (pH < 7,15, ou < 7,25 avec signe défavorable) : figure 1 BTS/ICS, connue par synthèses secondaires.
6. Aucune donnée épidémiologique suisse retenue ; repères non revérifiés : gradient âge/4 + 4 (aide pédagogique), cyanose 50 g/L.

## Injection

- `chapters/J96/` (6 fichiers) et `glossary/j96.py` copiés depuis ce dossier.
- `chapters.json` : `{"code": "J96", "covers": ["J96"], "title": "Insuffisance respiratoire aiguë et chronique", "integrated": true}`.
- `organisation/course_groups.json` : même entrée, `owner` « S02 », `scope` en une phrase (J96.0, J96.1, J96.9 ; causes renvoyées à J18, J44, J45, I26 ; J80 exclu).
- `tests/audit_sciences.py` : J96 ajouté à l’exemption des cours absents du commit de base.
- Ces fichiers ont été intégrés par l’assembleur dans l’instantané `fc993a0` ; aucune opération Git n’a été faite par le relecteur.

## Contrôles

| Contrôle | Résultat |
|---|---|
| `python3 -m unittest discover -s tests -p 'test_*.py'` | 176 tests, OK |
| Audit des sigles (`build_medina.audit` après transformation) | `{}` |
| Clés des fenêtres | 60 gabarits ; aucun `data-k` sans gabarit ; aucune fenêtre orpheline ; aucun identifiant dupliqué |
| Pareto | 6 fractions calculées (6 à 10 %) |
| `python3 build_front.py --all-fragments` | 22 fragments construits |
| `tests/audit_fragments.py` | Réussi : 22 fragments, JavaScript valide, build reproductible |
| Chromium (`/opt/pw-browsers/chromium`), `MEDINA_S02_respiratoire.html#/entry/J96` | Titre correct ; 4 onglets non vides ; toutes les fenêtres s’ouvrent avec contenu ; aucune erreur JavaScript ni de console |
| `node tests/verify_course_native.cjs J96` | Réussi : 1 789 contrôles, 66 déclencheurs directs, 60 gabarits, 0 échec |
| `tools/capture_lecon.py … J96` | Réussi : `j96-1-ouverture.png`, `j96-2-explication.png` (dossier temporaire de session) |
| `tests/audit_sciences.py` restreint à J96 | Réussi ; le script complet échoue sur I50 (absent du commit de base), défaut préexistant sans lien avec J96 |

Empreintes SHA-256 :

```
8f95c475bc5b19bb20426dc03f9cd4a7f90ba221b018b68049b65f2c07fc8783 chapters/J96/J96_a.html
a683b22c65b97daf9e9e083bce2a413737c992e60a0c5b583b09f9f42944a3df chapters/J96/J96_b.html
3398653fbf9075f6c2629de2ff4690a7e05b596224a5f0a535a6db6e5663fe03 chapters/J96/J96_c.html
fd4b834d9491053b6bd8b458bed4f0a44f1c366f29ba61de96e1f502022d9176 chapters/J96/J96_d.html
e78bba9fbdbe205397128ac009240f4979bfca73b78f67f651eab4e66372a31a chapters/J96/J96_pop1.html
b3aa479e1a547642dff240a14ee67337c5ffcf8329751203a75e409c2ec34db0 chapters/J96/J96_pop2.html
bb91aa5de722e450fc6d2d428c459574b2a21231da7e1fdf566f9c7402b9bc67 glossary/j96.py
```

Statut : injecté, en attente de l’audit croisé Codex. La revue par IA et les tests techniques ne valent pas validation médicale.
