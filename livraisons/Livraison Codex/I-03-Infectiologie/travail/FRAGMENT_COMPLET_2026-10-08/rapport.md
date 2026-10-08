# A41 — Sepsis et choc septique de l’adulte (I-03-Infectiologie) : reprise interne

Les deux compléments documentaires recherchés sont maintenant sourcés et intégrés dans une **nouvelle copie interne à contre-vérifier**. Aucun fragment complet, nouvel audit croisé final ou nouvelle injection n’est annoncé. Les dernières corrections médicales de Claude sont conservées.

## Base et périmètre

La copie est située dans `/workspace/work/medina-resume/livraisons/Livraison Codex/I-03-Infectiologie/travail/FRAGMENT_COMPLET_2026-10-08/sources/`. Elle contient les dix sources A41, avec comme base exacte **`a5563238887df2a72da7a9f663bdae9ab01f4bc8`**. Ce commit a injecté le chapitre A41 selon le dispositif précédent. Son injection historique ne constitue pas une preuve de complétude ou d’injection du fragment entier I-03-Infectiologie.

Le lot historique `e3307768ff4c3a6c3af2e790859ff36947c0279d`, ses copies partagées et le canonique restent conservés. Le rapport d’audit Claude présent à la base a556323 est lu et archivé dans les preuves. Il levait déjà ESP-03 sur l’identité du bicarbonate employé par Winter et gardait ESP-07 comme réserve mineure. La nouvelle copie conserve explicitement cette distinction : elle apporte les normes suisses du bicarbonate actuel et la source spécifique du contraste ; elle n’efface ni ne réécrit le verdict historique.

`A41_a.html`, `A41_pop1.html`, `A41_d.html` et `A41_pop_pa.html` sont identiques aux octets canoniques du SHA a556323. La réparation de l’encadré, la correction du sens de « TDM », les limites rénales de pipéracilline/tazobactam et la correction du cas de Mme R. sont conservées. Dans `A41_b.html`, la phrase « ils sont donc remplis » concernant les critères Sepsis-3 sous noradrénaline avec PAM 64 mmHg reste présente. Les exclusions du bicarbonate standard dans Winter ajoutées par Claude sont présentes dans C et la fenêtre de gazométrie.

## ESP-03 : bicarbonate actuel et matrices

**Source primaire suisse réellement obtenue et lue :** [UniversitätsSpital Basel, LM-Update 03/2023](https://www.unispital-basel.ch/dam/jcr%3Af60b0770-1163-4678-8bb3-9f8898ee70b9/2023_3%20Aenderungen%20Referenzwerte%20Klinische%20Chemie.pdf), document du **2 mai 2023**, application annoncée le **3 mai 2023**, pages 1–2. La page 2 a été rendue en image et contrôlée visuellement, pour éviter une attribution à la mauvaise colonne du tableau. Le document annonce une harmonisation entre analyseurs de gaz au lit et laboratoire central. Il donne le **bicarbonate actuel artériel**, séparé du veineux : femmes **21,2–27,0 mmol/L**, hommes **22,2–28,3 mmol/L**. La consultation du 8 octobre 2026 ne devient pas une date de publication et ne certifie pas un maintien inchangé de ces plages depuis 2023. Le compte rendu actuel du patient fait référence.

Cette source permet un repère suisse daté sans attribuer au bicarbonate actuel la plage **21–29 mmol/L** de [Viollier 14157](https://www.viollier.ch/de/analysis/14157), qui est celle du **bicarbonate standard**. La [fiche CHUV artérielle V16 du 16 juillet 2024](https://catalogue.chuv.ch/analyses-examens/laboratoires/fiche/DLA_INV_01_00717/gazometrie-arterielle) répertorie effectivement les deux paramètres calculés séparément. La fiche ne donne aucun intervalle normal de bicarbonate actuel.

Les surfaces corrigées sont :

- `sources/chapters/A41/A41_c.html`, section **a41-e-3**, paragraphes de mesure/attribution, nouvelle ligne du tableau « Bicarbonate actuel calculé », référence Bâle et exemple chiffré.
- `sources/chapters/A41/A41_pop_sciences_revision.html`, fenêtre **a41-gaz-read**, mêmes normes et datation, distinction des paramètres et des matrices de l’exemple.
- `sources/chapters/A41/A41_pop2.html`, fenêtre **pareto-a41-examens**, rappel de l’identité du bicarbonate et du profil cohérent.
- `sources/chapters/A41/A41_justifications.json`, entrée **a41-j-gazometrie**, limite sur les matrices et références CHUV/Bâle ajoutées ; accès au texte éditeur de Jung, effectivement reçu ici.

Pour la compensation, l’exercice utilise explicitement un bicarbonate actuel **calculé sur gaz artériel de 12 mmol/L**, avec PaCO₂ 20 mmHg et pH 7,40. La PaCO₂ attendue vaut **26 ± 2 mmHg**. Le calcul du trou anionique utilise désormais un **profil plasmatique simultané distinct**, avec sodium 140, chlorure 106 et bicarbonate enzymatique 12 mmol/L : **22 mmol/L**, puis **27 mmol/L** après correction pour albumine 20 g/L. La concordance des deux bicarbonates est une hypothèse de l’exercice ; elle ne les rend pas interchangeables. Aucune norme Medics n’est attribuée à un assemblage de matrices.

La [fiche Medics anionl](https://www.medics.ch/analysenverzeichnis/anionl), effectivement lue, publie sodium − chlorure − bicarbonate, **8–16 mmol/L**, sur sérum ou plasma Li-hépariné, sans équivalence démontrée avec un analyseur artériel. [Jung et coll. 2019, texte éditeur](https://link.springer.com/article/10.1186/s13613-019-0563-2), passages R1.1 et R1.3–R1.4 effectivement lus, étaye la compensation et la correction d’albumine ; cette recommandation ne constitue pas une norme de laboratoire suisse.

**Disposition proposée :** complément documentaire et ambiguïté des matrices traités dans la copie ; relecture interne ciblée attendue avant levée interne. Aucun nouvel acquittement Claude n’est revendiqué. Si la règle exige une norme explicitement confirmée actuelle en 2026 plutôt qu’un repère suisse daté, la limite sur la permanence des intervalles de Bâle demeure : aucun accès obtenu ne prouve cette permanence.

## ESP-07 : contraste iodé, urgence et risque rénal

**Source spécifique récente effectivement obtenue et lue :** [ESUR Contrast Media Safety Committee Guidelines 2025](https://www.esur.org/wp-content/uploads/2025/12/Guidelines-2025-ESUR-vf-1.pdf), section prévention de l’atteinte rénale associée au contraste iodé, **pages 15–18**. La page officielle [ESUR Guidelines 2025](https://www.esur.org/esur-guidelines-2025/) donne cet accès. La version 2025 remplace ici la simple suggestion historique de citer van der Molen 2018 ; il n’est pas nécessaire de s’arrêter au manuel v10 de 2018.

Les surfaces corrigées sont :

- `sources/chapters/A41/A41_c.html`, section **a41-e-4**, mot interactif ouvrant **a41-contraste-rein**, décision en urgence, individualisation de l’hydratation et référence ESUR datée.
- `sources/chapters/A41/A41_pop_sciences_revision.html`, nouvelle fenêtre **a41-contraste-rein** : rendement diagnostique, alternatives, voies d’injection, fonction rénale, urgence, prévention et surveillance.
- `sources/chapters/A41/A41_b.html`, section **a41-9**, cas de Mme R. : le scanner sans contraste localise son calcul ; cette illustration n’enseigne pas une interdiction du contraste due à l’atteinte rénale. Le même mot ouvre la fenêtre.
- `sources/chapters/A41/A41_pop2.html`, **pareto-a41-examens**, décision individualisée et référence ESUR.
- `sources/chapters/A41/A41_justifications.json`, nouvelle entrée **a41-j-contraste** sur la phrase native « une atteinte rénale n’est pas une raison automatique de renoncer à une imagerie indispensable ».
- `sources/glossary/a41.py`, définition du nouveau sigle **ESUR**, sans retirer les corrections du glossaire Claude.

La fenêtre précise les seuils selon l’exposition : DFG estimé **< 30 mL/min/1,73 m²** pour contraste intraveineux ou second passage artériel ; **< 45** pour premier passage rénal ou patient en soins intensifs. Une atteinte rénale aiguë connue ou suspectée est un facteur distinct. Les seuils guident les précautions, sans devenir des interdictions universelles. En urgence, la fonction rénale est recherchée si le délai peut être toléré sans dommage ; si elle ne peut être obtenue, les précautions sont adaptées à la voie et aux possibilités cliniques. Le choix du produit et de la dose reste diagnostique. L’hydratation est individualisée quand l’état du patient ne la permet pas ; elle ne s’ajoute pas automatiquement au remplissage septique.

Le texte reste un référentiel européen utilisé avec le protocole institutionnel suisse. Il ne revendique aucun protocole local HUG/CHUV, volume de produit, dose prophylactique ou préparation suisse non documentés. La surveillance rénale à 48 heures est attribuée à l’ESUR pour les patients à risque.

**Disposition proposée :** source spécifique et décision contextualisée ajoutées ; contre-vérification interne ciblée requise. Aucun avis externe nouveau ni protocole institutionnel suisse inventé.

## Vérifications et preuves

La compilation isolée passe **15 justifications sur 15 cibles**. Le contrôle statique du chapitre compilé compte **86 fenêtres et 159 déclencheurs** ; il ne trouve aucun identifiant ou template en doublon, aucune cible `data-k` ou `data-cover` manquante et aucun lien `_blank` sans `noopener`. La nouvelle fenêtre de contraste existe une seule fois et ses deux appels depuis C et B sont résolus. La syntaxe Python du glossaire passe et ESUR est défini. Les libellés rendus emploient « Hôpital universitaire de Bâle, bulletin du laboratoire 03/2023 » ; le titre allemand original reste conservé dans les preuves. Les quatre calculs illustratifs 26, 22, 27 et 200 sont vérifiés. Les empreintes finales correspondent au manifeste.

**Aucun build global ou T1 ni parcours navigateur n’a été exécuté par cette mission.** Les 4 350 assertions anciennes portent sur le gel historique ; elles ne sont pas réutilisées comme preuve du nouveau candidat. Les contrôles isolés ne certifient aucune revue clinique exhaustive ni complétude CIM-11.

Le dossier interne contient `manifest_interne.json` (dix empreintes de base et finales, statut incomplet), `provenance_sources.json` (URL, dates, portées de lecture, limites, fichiers et SHA-256), `controles_statiques.json`, `diff_interne.patch` et `preuves/` avec les six sources réellement obtenues, leurs extractions, la page 2 de Bâle et le rapport d’audit Claude historique. Aucun commit, publication, message externe, source canonique ou copie partagée n’a été modifié.

Accès non prétendus : l’ancienne URL esur-cm.org renvoie HTTP 403, mais le PDF officiel 2025 est reçu ; PMC Jung renvoie une page de vérification, mais le texte éditeur Springer est réellement reçu et lu. Les résultats de recherche ont servi à découvrir Bâle, puis le PDF primaire a été ouvert, téléchargé et vérifié directement.

Les réserves mineures du rapport Claude historique restent conservées : décubitus ventral et autres cotations SSC 2026, sources d’ANDROMEDA-SHOCK-2 et Leone, codage R65, repère prednisone, estimation de mortalité, gentamicine/dobutamine et activation globale de certains sigles. Elles ne sont pas clôturées par le présent travail ESP-03/ESP-07. Le fragment entier doit encore être achevé et auto-revu avant l’unique audit final prévu par les nouvelles consignes utilisateur.
