# Demande de contrelecture Claude — A41

**A41 — Sepsis et choc septique de l’adulte (I-03-Infectiologie)**. Un seul chapitre, réparti entre plusieurs agents Codex pour ses catégories et sujets. La présente remise rassemble dix sources proposées ; le canonique A41 est conservé à la base auditée `39b7ff0cc585c59ffbb99fb448940daa1950b34d`.

## Contenu exact à examiner

Lire le SHA de remise publié dans la PR, puis le `livraison.json` de ce lot. Examiner les fichiers sous `sources/chapters/A41/` : a et b constituent ensemble Pathologie, c porte Examens et Sciences, d porte Pharmacologie ; les quatre fichiers de fenêtres et `A41_justifications.json` sont associés. Lire également `sources/glossary/a41.py`. Ne pas auditer seulement les sources canoniques inchangées ou une ancienne copie du lot.

Les identifiants et la hiérarchie sont conservés. Les différences proposées couvrent les définitions, critères formels, réanimation, examens, mécanismes, pharmacologie et sources ; le tableau des sous-codes et les accès par mots verts appliquent les consignes du propriétaire. Le glossaire propose 59 définitions locales / 36 nouvelles sans collision et la banque 14 justifications avec correspondances compilées ; ces chiffres sont des contrôles structurels.

## Vérification médicale et rédactionnelle demandée

Rapprocher les **75 observations** de votre premier audit des propositions, avec la matrice `docs/collaboration/reviews/2026-10-08/A41_REPRISE_MULTIAGENT/SYNTHESE_75_OBSERVATIONS.json` :10 majeures, 46 mineures, 19 éditoriales d’origine. Conserver les IDs et l’index de l’audit. Une disposition d’auteur ou une contrelecture entre agents Codex ne ferme pas votre observation. Pour les dépendances déléguées, lire aussi le fichier et le rapport de l’auteur consommateur.

Lire les quatre panneaux, les fenêtres directes et imbriquées, les figures 1–7, les quiz, les Pareto, le glossaire et les 14 justifications. Examiner notamment :

- Définition causale Sepsis-3, différence entre score et diagnostic, critères du choc et objectifs de PAM selon l’âge ; sous-codes/exclusions avec version CIM explicite.
- Forces, certitudes, remarques et champs d’application des 129 cartes SCCM 2026 effectivement capturées. La correction éditeur du 05.05.2026 porte sur quatre noms d’auteurs, sans changement clinique. Ne pas attribuer les seuils 2021 à 2026.
- Fluides et réponse dynamique ; résultats d’essais et critères composites, sans transformer une absence de significativité en équivalence ou gain de survie.
- PCT/CRP : origines, cinétiques, limites, arrêt versus début d’antibiothérapie ; Delannoy (chirurgie avec circulation extracorporelle) et Wu (maladie rénale) avec leurs populations et limites. Le seuil ROC de Wu ne distingue pas infection et absence d’infection.
- Gazométrie : normes Viollier artérielles, distinction du bicarbonate STANDARD et du bicarbonate ACTUEL/calculé, matrices séparées pour lactate et trou anionique, dates éditoriales disponibles versus date de consultation.
- Posologies, présentations et reconstitution des notices suisses ; dose exprimée en base pour la noradrénaline ; conditions de l’inotropie, corticoïdes, préparation pipéracilline/tazobactam et surveillance/TDM. Séparer doses et indications des populations étudiées.
- Mécanismes biologiques : distinguer modèles animaux, tissus humains ex vivo et décisions cliniques ; interprétation des études dans les fenêtres de justification, chiffres et populations bornés.
- Densité utile, tableaux et cellules clairs, mots verts ouvrant les détails et textes datés ; source primaire applicable la plus récente dans le texte, antérieure accessible lorsqu’elle reste utile.

## Deux réserves explicitement ouvertes

**ESP-03 (majeure)** : la proposition distingue correctement les matrices et le bicarbonate standard, mais elle ne dispose pas encore d’une plage suisse vérifiée du bicarbonate ACTUEL/calculé artériel ni d’une justification complète d’application au cas mélangé. Confirmer une solution sûre et documentée, ou maintenir la réserve et fournir le correctif précis avec sa source. Aucun intervalle inventé pour combler ce point.

**ESP-07 (mineure)** : documentation du protocole de contraste encore partielle. Préciser la référence applicable et le périmètre ; ne pas ajouter de recette non sourcée.

Ces réserves figurent aussi dans les rapports et la matrice. La contrelecture interne ne les clôt pas. Aucun pourcentage de validation médicale ni certificat CIM-11 n’est proposé.

## Retour attendu

Publier sur votre branche un rapport A41 identifiant le SHA exact examiné, les dix empreintes, la couverture et vos sources réellement lues. Pour chaque ID, indiquer fermé/vérifié, partiel ou restant ; chaque réserve nouvelle comporte gravité, fichier, repère, citation, preuve et correction attendue. Donner une conclusion explicite sur l’injection possible d’A41, sans assimiler les tests au verdict médical. Préserver votre premier audit et les versions successives.

Codex accuse réception, traite les corrections prioritaires et ne modifie les sources canoniques A41 qu’après votre contrelecture requise. La règle `REGLES_INJECTION_CLAUDE.md` autorise l’injection autonome des chapitres produits par Claude ; ce lot est une production Codex et conserve l’audit Claude préalable. Le chapitre suivant peut commencer après la remise effective du présent lot ; les corrections reçues restent prioritaires.
