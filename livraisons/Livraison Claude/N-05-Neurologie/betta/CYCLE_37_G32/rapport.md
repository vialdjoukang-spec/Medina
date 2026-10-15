# Rapport de rédaction — G32 (cycle Betta 37, leçon 1, N-05-Neurologie)

Agent C37-A1-NEUR (rédaction, Sonnet 5.5). Date : 15.10.2026. Dossier d'entrée : `recherche.md` et `sources.json` (13 sources). Aucune donnée extérieure n'a été utilisée.

## Fichiers livrés
| Fichier | Octets | Contenu |
|---|---|---|
| chapters/G32/G32_a.html | 18 683 | En-tête, quatre onglets, plan, pathologie sections 0 à 6 |
| chapters/G32/G32_b.html | 18 502 | Pathologie sections 7 à 13 (dernier îlot : `div.alert` puis `div.key`) |
| chapters/G32/G32_c.html | 16 828 | Examens (4 îlots), Sciences (anatomie, histologie, physiologie, biochimie) |
| chapters/G32/G32_d.html | 7 202 | Pharmacologie (4 îlots) |
| chapters/G32/G32_pop1.html | 10 806 | 9 fenêtres (codage, DCS, épidémiologie, mécanismes, limites) |
| chapters/G32/G32_pop2.html | 26 128 | 21 fenêtres cliniques et 13 fenêtres Pareto |
| glossary/g32.py | — | 35 entrées lettre à lettre, ajout conditionnel (`add_if_absent`) |

Poids inférieur à N17 et D50 : la leçon est bornée par les sources lues (13 sources, 2 cas, séries courtes) ; aucun remplissage n'a été ajouté.

## Auto-contrôle du cahier W
- HTML bien formé : a+b+c+d concaténés sans balise orpheline ; pop1 et pop2 équilibrés.
- Identifiants uniques et préfixés `g32-` ; 388 `data-evidence` uniques `G32-C0001…`.
- Toutes les clés `data-k` ont leur `template data-pop` et inversement (0 manquante, 0 inutilisée) ; clés `g32-…` et `pareto-g32-…`.
- Chaque îlot de la pathologie, des examens, des sciences et de la pharmacologie est couvert par un Pareto (`data-cover` valide).
- Abréviations listées dans le glossaire ; `build_medina.audit()` et `test_preview.py` n'ont pas été exécutés (consigne : ne rien toucher hors du dossier).
- Avertissement de statut dans l'en-tête : « Revue par intelligence artificielle · Aucune validation médicale humaine · Audit différé ».

## Sources utilisées
S1 à S13, chacune citée dans les fenêtres (`p.src`). S13 (RöFo) n'est mentionnée que comme existence d'une référence.

## Lacunes (reprises du dossier)
- Aucune recommandation de société savante lue (NICE 403, BSH introuvable, Swiss Medical Forum inaccessible) ; posologies fondées sur l'information professionnelle suisse, des revues et des séries.
- G32.8* : définition de code seulement, aucune source clinique.
- Revues Zou 2024 et Keddie 2018 non lues ; schéma méthionine et anesthésie signalés comme tels.
- Date de révision de l'information professionnelle Vitarubine® non extraite ; absorption de la B12 non développée.
- Code causal † non établi pour la myélopathie au protoxyde d'azote (seul E53.8† listé).
- Le cas à choix multiples de la leçon est une vignette fictive explicitement marquée.

Audit différé — revue IA, distincte d'une validation médicale humaine.
