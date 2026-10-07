# I48 — Fibrillation et flutter auriculaires : réception b6 et fusion bibliographique

Relecture du 7 octobre 2026. Proposition Claude : `b6db50cb2911fcbe0b09e64b79df03aab294e3df`. Référence originale immuable : `b1f19c3510c1a828650867da033ebe2fbf30142e`.

**Décision proposée : reprendre uniquement les corrections bibliographiques.** Les quatre propositions reçues ne contiennent aucune justification physiopathologique, indication, dose, limite clinique, fenêtre ou interaction nouvelle par rapport aux originaux b1. Remplacer les fichiers canoniques par ces propositions réintroduirait les formulations déjà contre-corrigées.

Les propositions reçues sont conservées dans `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07_B6DB50C_RECEPTION/nouvelles_propositions_I48/`. Les originaux b1 comparés demeurent dans `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I48/`. La réception n’est pas une validation médicale exhaustive.

## Delta exact contre b1

Les différences portent sur **39 lignes de sources**, toutes commençant par « Source » ou « Source complémentaire ». Après exclusion de ces seuls paragraphes, les contenus b1 et b6 sont identiques à l’octet. Les 100 éléments `template` — 17, 28, 29 et 26 dans les quatre fichiers — conservent leurs identifiants et leur ordre. Aucun bouton n’est ajouté ou déplacé.

| Fichier | Lignes bibliographiques modifiées | Apports cliniques nouveaux |
| --- | ---: | --- |
| `I48_pop1.html` | 10 | Aucun |
| `I48_pop2.html` | 9 | Aucun |
| `I48_pop3.html` | 13 | Aucun |
| `I48_pop4.html` | 7 | Aucun |

| Correction proposée par Claude | Occurrences |
| --- | ---: |
| `N Engl Med` → `N Engl J Med` | 25 |
| `Eur Heart` → `Eur Heart J` | 31 |
| `Eur Thyroid` → `Eur Thyroid J` | 2 |
| `Am Cardiol` → `Am J Cardiol` | 1 |
| `Am Med` → `Am J Med` | 1 |
| Direction de l’ouvrage de 1985 : ajout de Jalife | 1 |

Il s’agit de 60 corrections d’abréviations et d’une correction d’attribution. Le comptage fin de caractères décompose la dernière en trois opérations ; cela ne correspond pas à trois apports distincts.

## Vérification des références

Les abréviations et l’attribution sont concordantes avec les notices officielles ou les métadonnées des publications concernées :

- [NLM — The New England Journal of Medicine, identifiant 0255562](https://www.ncbi.nlm.nih.gov/nlmcatalog?cmd=PureSearch&db=journals&term=%220255562%22%5BNLM+ID%5D) : `N Engl J Med`.
- [Recommandations ESC 2024 sur la fibrillation auriculaire, PMID 39210723](https://pubmed.ncbi.nlm.nih.gov/39210723/) : `Eur Heart J`, volume 45, pages 3314–3414.
- [Bartalena et collaborateurs, recommandations ETA 2018, PMID 29594056](https://pubmed.ncbi.nlm.nih.gov/29594056/) : `Eur Thyroid J`, volume 7, pages 55–66.
- [Berger et Schweitzer, étude de 1998, PMID 9874066](https://pubmed.ncbi.nlm.nih.gov/9874066/) : `Am J Cardiol`, volume 82, pages 1545–1547.
- [Nakazawa et collaborateurs, étude de 1982, PMID 7091161](https://pubmed.ncbi.nlm.nih.gov/7091161/) : `Am J Med`, volume 72, pages 903–906.
- [Notice bibliographique CiNii de l’ouvrage *Cardiac Electrophysiology and Arrhythmias*](https://ci.nii.ac.jp/ncid/BA01450516) : ouvrage dirigé par Douglas P. Zipes et Jose Jalife, Grune & Stratton, 1985. L’attribution est aussi reprise dans les références de [*Reconsidering the multiple wavelet hypothesis of atrial fibrillation*, PMID 32585192](https://pubmed.ncbi.nlm.nih.gov/32585192/).

Pour harmoniser les initiales, la fusion proposée écrit **« Zipes DP, Jalife J (dir.) »**, plutôt que « Zipes, Jalife J (dir.) ». Aucun résultat médical n’est déduit de cette vérification bibliographique. La consultation du texte intégral ESC via Oxford et de l’article ETA via PMC a été bloquée par leurs interfaces ; leurs notices PubMed étaient disponibles. Les mécanismes et recommandations déjà arbitrés dans le canonique ne sont donc pas revalidés ici sur la seule base de notices bibliographiques.

## Contenu canonique à préserver

La fusion a été construite depuis les quatre fichiers canoniques actuels, en modifiant seulement leurs paragraphes bibliographiques concernés. Elle conserve **à l’octet tous les autres passages**, y compris les corrections médicales antérieures et l’administration lente de digoxine ajoutée après vérification du guide HUG.

La comparaison structurelle trouve 24 fenêtres dont le contenu hors bibliographie diffère déjà de b1. Elles doivent rester canoniques :

| Fichier | Fenêtres canoniques ayant reçu des corrections de fond depuis b1 |
| --- | --- |
| `I48_pop1.html` | `i48-noeudav`, `i48-vp`, `i48-infraclin`, `i48-colaus`, `i48-saos`, `i48-poids`, `i48-tachycm` |
| `I48_pop2.html` | `i48-preexc`, `i48-e-bas-debit` |
| `I48_pop3.html` | `i48-hasbled`, `i48-mitral`, `i48-laao`, `i48-24h`, `i48-eto`, `i48-inr`, `i48-bilan` |
| `I48_pop4.html` | `i48-avk`, `i48-d-frein`, `i48-d-flec`, `i48-d-amio`, `i48-d-drone`, `pareto-i48-rythme`, `pareto-i48-pharma`, `i48-d-dig` |

Cela préserve notamment les conditions d’anticoagulation après cardioversion, les limites des cohortes et essais, l’individualisation des cibles d’INR, la distinction entre sévérité mitrale et éligibilité aux AOD, les restrictions de classe Ic et de dronédarone, ainsi que les explications sur la pompe sodium-potassium. Le périmètre de TRAPS et les autres arbitrages présents dans les textes canoniques sont conservés, même lorsque leur fenêtre n’apparaît pas dans ce tableau de différences hors bibliographie.

La prescription intraveineuse de digoxine reste inchangée : dose adaptée au patient, injection lente et référence HUG du 16 juillet 2026. Le remplacement complet par `I48_pop4.html` b6 ferait perdre cette mise à jour.

## Fusion précise à appliquer par l’intégrateur

Les livrables de travail ont été produits uniquement en scratch :

- `/workspace/scratch/6eaecafb4b19/i48_b6_review/fusion_bibliographique.patch` : patch limité aux références ;
- `/workspace/scratch/6eaecafb4b19/i48_b6_review/fusion_proposee/I48_pop1.html` à `I48_pop4.html` : quatre fichiers canoniques avec cette seule fusion ;
- `/workspace/scratch/6eaecafb4b19/i48_b6_review/fusion_plan.json` : SHA complets avant/après, identifiants, décompte des opérations et commit local observé ;
- `/workspace/scratch/6eaecafb4b19/i48_b6_review/delta_original_to_b6.json` : relevé exhaustif du delta de caractères b1 → b6.

| Fichier canonique | SHA-256 avant fusion | SHA-256 de la proposition fusionnée |
| --- | --- | --- |
| `I48_pop1.html` | `8bdbd9801ce706aa986a2999eccc4b36e19f962c3b0a4788f7eba5709cd90476` | `61c19a8dd301df332a8f5c4e0a35bcdeb98623c27100ed9c83b62002b8019d07` |
| `I48_pop2.html` | `2f668a468b5957c18cc219e18c6d0a58c13f4bdbe3cf205d86b873ba6e51ddc0` | `124f677e9b2063f84f97c8a0e274d3545f110df20a5d99ada58660def78e4c90` |
| `I48_pop3.html` | `37499843c9b47ac193d90d8c7d77427b330c2235be5723b0204d97dcda94498a` | `0c58ea49995321aea86d6358573f60c2b96144b29e61d86d5ebba489df5ba6b6` |
| `I48_pop4.html` | `f0915cef14056c610ca7b2478402a722801ba1f1842486524d231f63c17eaf12` | `6cfc947f383677cf924d70b1b36dfd4d81ccd48f28b2fcfe4f8b914ecc78e913` |

L’intégrateur doit comparer ces SHA avec le canonique avant application. Si une modification intermédiaire a eu lieu, il faut réappliquer les seuls remplacements bibliographiques au nouvel état, plutôt que copier les fichiers proposés. Les originales b1 et b6 restent intactes. Cette relecture n’a modifié aucun fichier canonique ni aucun moteur de rendu.

## Vérification réalisée et limites

Les contrôles locaux de comparaison établissent l’égalité b1/b6 hors bibliographie et la conservation canonique/fusion hors bibliographie. Ils comparent aussi l’intégralité des ouvertures de `template` et de `button`, sans différence. La fusion proposée contient 61 remplacements bibliographiques, dont l’attribution normalisée.

Aucun test navigateur ou construction globale n’a été exécuté dans cette tâche de réception : la fusion reste une proposition tant que l’intégrateur ne l’a pas appliquée et vérifiée dans son lot. Aucune complétude de toutes les assertions médicales, de toutes les leçons ou de la CIM-11 n’est certifiée par ce rapport.
