# Rapport de rédaction — G58 Autres mononévrites (N-05-Neurologie)

Agent C38-A1-NEUR (Sonnet 5.5), cycle Betta 38, leçon 2. Base : `recherche.md` et `sources.json` (S1–S31), sans donnée extérieure.

## Fichiers livrés
| Fichier | Octets | SHA-256 (16 premiers) |
|---|---|---|
| `chapters/G58/G58_a.html` | 12338 | `ab85b9cbe6a06c07` |
| `chapters/G58/G58_b.html` | 32191 | `dac8f40b07949ec9` |
| `chapters/G58/G58_c.html` | 25477 | `5b3b01c49d1213b8` |
| `chapters/G58/G58_d.html` | 7289 | `9a95b52653e579e5` |
| `chapters/G58/G58_pop1.html` | 20107 | `9d862c7a0f28d908` |
| `chapters/G58/G58_pop2.html` | 23627 | `809975dabf4ed536` |
| `glossary/g58.py` | 8773 | `ec367748aa211848` |

## Contenu
- Pathologie : 13 îlots (question clinique à critères formels `alert` puis paramètres clés `key`), 2 figures SVG, 2 quiz, Pareto par grande partie.
- Examens : 6 îlots, 4 quiz de cas, référence histologique nommée (biopsie combinée nerf-muscle).
- Sciences : Anatomie, Histologie, Physiologie, Biochimie, chacune avec figure SVG légendée, encadré de corrélations cliniques et Pareto.
- Pharmacologie : 4 îlots, doses suisses (Lyrica, Neurontin, Prednisone Streuli) distinguées des doses citées par revue, alerte d’interactions.
- Fenêtres : 31 explicatives + 12 Pareto (`g58-…`, `pareto-g58-…`). Glossaire : 27 entrées (`glossary/g58.py`), `build_medina.audit` renvoie `{}`.

## Auto-contrôle (cahier W)
HTML bien formé (pile de balises équilibrée sur a–d et pop1–2) ; aucun identifiant dupliqué ; tous les identifiants préfixés `g58-` ; toute clé de fenêtre référencée existe et aucune fenêtre n’est inutilisée ; tous les `data-cover` Pareto et liens du sommaire pointent vers des îlots existants ; `bm.transform` et `pareto_ratios` s’exécutent sans erreur.

## Lacunes (reprises du dossier, L1–L11)
Aucune source de société savante suisse lue ; textes intégraux EULAR 2022 et PNS 2010 non lus (résumés) ; informations professionnelles du rituximab, de l’azathioprine, du méthotrexate, du mépolizumab, de la duloxétine et de l’amitriptyline non lues ; anatomie intercostale détaillée, épidémiologie suisse et traitement actuel de l’hépatite C absents (non rédigés) ; mécanismes d’action de la prégabaline, de la gabapentine et des glucocorticoïdes absents du dossier (non rédigés). Les `data-evidence` ne sont pas générés (registre de preuves hors périmètre).

## Statut
Audit différé — revue IA, distincte d’une validation médicale humaine.
