# Lot 5 — Justification systématique de 14 cours de C-01-Cardiologie

Date : 7 octobre 2026. Auteur : Claude. Branche : `claude/loving-shannon-spwrhc`. Base : intégration `codex/sciences-cs-fragments-20261007` au commit `75505d8`. Mission : `docs/collaboration/MECHANISMS_CLAUDE.md`, après le cours pilote I48 (lot 4).

## Périmètre

Les 14 cours de la répartition 15/15 alors en vigueur ont été traités. Pendant le lot, Codex a révisé la répartition : I47, I49, I46, I71 et I80 lui reviennent désormais. Leur justification était déjà produite et vérifiée ; elle est livrée comme contribution recevable et reste à son arbitrage.

## Méthode

Chaque cours a suivi la même chaîne, décrite dans `travail/justification/` :
1. Deux producteurs se partagent les fichiers ; un seul pour I71 et I80, plus courts. Chacun relève les affirmations sans mécanisme, puis écrit soit un complément de une à trois phrases, soit une fenêtre créée ou complétée. Il vérifie lui-même chaque chiffre dans la recommandation de référence, téléchargée en texte intégral, et dans PubMed.
2. Un **vérificateur indépendant** contrôle chaque complément et chaque fenêtre. Il accepte, corrige ou rejette, fusionne les doublons entre producteurs et ajoute les corrections oubliées.
3. `appliquer_justifications.py` applique le tout aux sources canoniques. `finaliser.sh` lance ensuite le test statique et met à jour le manifeste.

Recommandations de référence : ESC 2025 myocardites et péricardites ; ESC 2023 endocardite ; ESC/EACTS 2025 valvulopathies ; ESC 2023 cardiomyopathies ; ESC 2021 stimulation ; ESC 2019 et 2022 arythmies ; ERC 2025 et ERC-ESICM 2025 ; ESC 2020 cardiopathies congénitales et ESC/ERS 2022 hypertension pulmonaire ; ESC 2024 aorte, ESVS 2024 et SVS 2022 ; ESVS 2021 et ESC 2019 maladie thromboembolique ; OMS 2024, WHF 2023 et recommandations australiennes 2025 pour le rhumatisme articulaire aigu. Ces textes ne sont pas versionnés, pour des raisons de droits d'auteur et de volume.

## Résultats

| Cours | Compléments appliqués | Mots verts | Fenêtres créées / complétées | Mots avant → après |
| --- | ---: | ---: | --- | --- |
| I30 — Péricardites, épanchement péricardique, tamponnade et constriction | 197 | 8 | 1 / 17 | 23 223 → 30 961 |
| I33 — Endocardite infectieuse | 151 | 14 | 2 / 25 | 24 133 → 33 006 |
| I35 — Valvulopathies aortiques | 150 | 9 | 3 / 20 | 26 480 → 34 280 |
| I34 — Valvulopathies mitrales, tricuspides et pulmonaires | 166 | 11 | 4 / 2 | 27 812 → 33 799 |
| I00 — Rhumatisme articulaire aigu | 117 | 18 | 2 / 13 | 21 464 → 27 035 |
| I40 — Myocardites | 188 | 20 | 3 / 25 | 24 113 → 33 447 |
| I42 — Cardiomyopathies | 150 | 18 | 4 / 4 | 29 325 → 35 848 |
| I44 — Troubles de la conduction et bradycardies | 139 | 14 | 5 / 17 | 26 783 → 35 308 |
| Q21 — Cardiopathies congénitales de l’adulte | 243 | 8 | 1 / 13 | 31 201 → 40 561 |
| I47 — Tachycardies paroxystiques supraventriculaires et ventriculaires *(transféré à Codex)* | 193 | 36 | 3 / 43 | 28 118 → 41 199 |
| I49 — Extrasystoles et autres arythmies *(transféré à Codex)* | 194 | 8 | 1 / 24 | 26 167 → 35 420 |
| I46 — Arrêt cardiaque *(transféré à Codex)* | 162 | 8 | 1 / 22 | 22 946 → 30 782 |
| I71 — Anévrismes et dissections artérielles *(transféré à Codex)* | 101 | 17 | 6 / 5 | 7 260 → 13 325 |
| I80 — Thrombose veineuse profonde et thromboses veineuses *(transféré à Codex)* | 85 | 14 | 6 / 7 | 7 292 → 14 030 |
| **Total** | **2 236** | **203** | **42 / 237** | **326 317 → 439 001 (× 1,35)** |

Les verdicts sont détaillés par cours dans `travail/justification/<CODE>/verification.json`, `verdicts/` et `out/*.contreverif.json`. Les vérificateurs ont rejeté 13 compléments, surtout pour redite, et en ont corrigé environ 350.

## Erreurs du cours corrigées : exemples par cours

- **I30** : volume d'hémopéricarde mortel (200 à 300 mL) ; doses de première ligne selon le tableau 13 de l'ESC 2025 ; anti-interleukine 1 (I A après échec avec CRP élevée, IIa C sur IRM) ; constriction transitoire traitée 3 à 6 mois ; corticoïdes dans la tuberculose (IIa C).
- **I33** : résistance de haut niveau à la gentamicine (> 128 mg/L) ; rifampicine (900 mg/j, au moins 6 semaines) ; échocardiographie dans la bactériémie à *S. aureus* (IIa) ; fièvre chez 78 % des patients (registre EURO-ENDO).
- **I35** : aspirine après TAVI (12 mois I A, puis long cours IIa C) ; tableau 11.1 (FEVG ≥ 50 % avec marqueur) ; relais d'héparine réservé au risque thromboembolique.
- **I34** : cibles d'INR des prothèses (tableau 10 de 2025) ; chiffres de TRISCEND II ; contre-indication des AOD limitée au rétrécissement mitral ≤ 2,0 cm² ; formule de Gorlin.
- **I00** : polyarthralgie, critère majeur en population à risque ; arrêt des anti-inflammatoires sans seuil de CRP ; doses d'aspirine et de valproate ; carbamazépine tératogène.
- **I40** : immunosuppression guidée par la biopsie (IIa B) ; hospitalisation selon le risque ; corticorésistance en 24 à 48 h ; TEP de la sarcoïdose (I B).
- **I42** : disopyramide (I avec bêtabloquant, QTc 500 ms) ; critères du défibrillateur (CMH, CMAVD, génotypes) ; tafamidis (ESC 2021).
- **I44** : incompétence chronotrope ; exploration négative (Brignole 2001) ; série de Scheinman relue sur l'article original ; seuil LMNA (ESC 2022).
- **Q21** : saignée dans l'érythrocytose ; angioplastie de la coarctation ; origine aortique anormale d'une coronaire ; embryologie de TBX1, glossaire compris.
- **I47** : QT long (DAI et dénervation de classe I) ; aspect de Brugada sous fièvre ; influence de la caféine sur l'adénosine réfutée.
- **I49** : flécaïnide dans la cardiomyopathie induite par les ESV (IIa, patients choisis) ; CRAVE ; FV idiopathique.
- **I46** : choc en cas de doute entre FV fine et asystolie ; adrénaline sous 30 °C ; figure de la réanimation de base (appel au 144 dès l'absence de réponse).
- **I71** : seuils thoraciques et de la bicuspidie ; surveillance de l'anévrisme abdominal ; esmolol ; métadiscours de l'onglet Sciences réécrit.
- **I80** : embolie silencieuse ; récidive ; dabigatran contre-indiqué sous 30 mL/min ; divergences entre l'ESC 2019 et l'ESVS 2021 exposées sans être tranchées.

## Correctif d'I48

Codex a injecté le lot 4 d'I48 (`e856ed1`) avant la réparation des rubriques Source. Le correctif part du canonique actuel, qui conserve les comparaisons ESC 2026 de Codex. Il ne restaure que les 38 rubriques abîmées des fichiers `I48_pop1` à `I48_pop4`, où « ESC », le « J » d'*Eur Heart J* et d'autres abréviations de revues avaient été retirés.

## Fichiers livrés

- `sources/chapters/<CODE>/` : copies corrigées des 14 cours et des 4 fichiers pop d'I48, soit 132 fichiers déclarés dans `livraison.json`. Les empreintes de départ sont celles de `75505d8` ; `check-claude` est conforme.
- `glossary/q21.py` : entrée TBX1 corrigée. Elle est remise par la branche et doit être fusionnée hors `apply-claude`.
- `travail/justification/` : consignes, outils (`appliquer_justifications.py`, `finaliser.sh`, `manifeste.py`, `verifier_sigles.py`), suivi, et résultats bruts et verdicts de chaque cours.

## Contrôles réellement exécutés

Les contrôles ont été exécutés après fusion de `75505d8`, avec copie temporaire des 15 cours dans `chapters/`, puis restauration par `git checkout -- chapters/`.

| Commande | Résultat |
| --- | --- |
| `python3 test_v7.py --static` sur les 15 cours, I70 et I50 | OK |
| `MEDINA_OUT=$PWD/dist python3 build_front.py --all-fragments` | 22 fragments |
| `python3 tests/audit_fragments.py` | JavaScript valide, build reproductible |
| `python3 tests/audit_sciences.py` | `errors: []` |
| `python3 -m unittest discover -s tests` | 76 tests réussis |
| `verify_sciences_cs.cjs` / `verify_s01_browser.cjs` | 609 / 71 contrôles, 0 erreur |
| `verify_justifications_recovery.cjs` / `verify_categories.cjs` / `verify_organisation.cjs` | 2 400 / 656 / 740 contrôles, 0 erreur |
| Ouverture navigateur des 15 cours | 1 795 mots verts, toutes les clés présentes, une fenêtre ouverte par cours, aucune erreur JavaScript |
| `python3 tools/livraison.py check-claude "livraisons/Livraison Claude/C-01-Cardiologie"` | Conforme, 132 fichiers |

## Incidents

1. **Données personnelles.** Trois agents producteurs (I33 P1, I33 P2, I42 P2) ont chacun interrogé une fois le service Unpaywall avec l'adresse e-mail du propriétaire, pour trouver une copie en libre accès des recommandations. Ces requêtes ont eu lieu avant l'ajout de la règle. L'adresse ne figure dans aucun fichier. Depuis, la règle figure dans `CONSIGNES.md` et a été transmise à tous les agents.
2. **Rubriques Source.** L'ancienne fonction de retrait des initiales supprimait aussi des sigles et des abréviations de revues. Elle est remplacée, et les cours touchés sont reconstruits ou réparés.
3. **Textes de recommandations dans l'historique.** Un ancien commit de cette branche (`64808cf`, réécrit depuis) contenait trois textes téléchargés (`I33/src/dl.bin`, `I34/src/esc2025.pdf`, `I35/src/esc2025_vhd.pdf`). Codex a fusionné ce commit avant sa réécriture : ces fichiers sont dans l'historique de la branche d'intégration. Ils ne sont plus suivis sur cette branche ; leur purge de l'historique d'intégration relève de Codex.
4. **Fichiers effacés.** Le producteur P1 d'I42 a vidé un dossier partagé. Les fichiers de P2 ont été restaurés depuis la sauvegarde automatique, et la consigne interdit désormais de vider un dossier partagé.

## Réserves principales

- **Données suisses** : compendium.ch n'a pas été consulté ; les informations professionnelles suisses (doses, Swissmedic) restent à vérifier.
- **Classes non relues directement** : dans plusieurs recommandations, les tableaux de classes sont des images. Les classes ont alors été lues dans les diaporamas officiels ou dans les traductions officielles (espagnole pour l'ESC 2019 et 2022, italienne en complément).
- **Non relus en texte intégral** : ESC 2015 sur les péricardites, AHA 2015 sur le rhumatisme articulaire aigu, ESC 2022 de cardio-oncologie, ACC/AHA 2018 et 2025, ESC 2018 sur la syncope.
- **Contradictions internes des recommandations, exposées dans le cours** : seuil du score de triage de la tamponnade ; constriction transitoire ; durée de la prévention de la fièvre ; anticoagulation après cardioversion (I48).
- Chaque cours conserve dans `verification.json` ses chiffres non retrouvés dans les sources, laissés tels quels.
- Cette passe couvre les affirmations relevées par les producteurs et les redites détectées ; elle ne certifie pas une relecture exhaustive de chaque cours, ni la complétude CIM-11.

## Suite proposée

- Injection par Codex : `apply-claude "livraisons/Livraison Claude/C-01-Cardiologie"`, puis fusion de `glossary/q21.py`.
- Productions confiées à Claude par la nouvelle répartition : I83 — Varices des membres inférieurs et I89 — Autres atteintes non infectieuses des vaisseaux et des ganglions lymphatiques ; comparaison des nouveautés ESC 2026 dans les dix cours actifs.
