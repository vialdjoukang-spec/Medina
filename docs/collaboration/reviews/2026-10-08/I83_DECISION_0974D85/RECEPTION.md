# Réception pour décision — I83 — Varices des membres inférieurs (C-01-Cardiologie)

**Avis réception : recevable pour une intégration sélective. Aucun blocage de présence, d’empreinte, de collision de glossaire ou de catalogue constaté.** Cette conclusion autorise à préparer les dix sources ci-dessous et la seule entrée de catalogue ; elle ne remplace pas la décision médicale ni les tests actuels du poste technique. Aucune injection réalisée par cette sentinelle.

- Tête Claude figée : `0974d854db292ae0311e435b3daea5fbed187e25` (commit du 8 octobre 2026 à 01:28:54 UTC).
- Base main demandée : `ea105ace0046c71492cc6a69ff4c61698ef2ce34`.
- Premier audit comparé : `8dfa6ba453fc872591b79e5720c914ce47964470`.
- Les dix sources sont identiques depuis `6b76e12a1b9431111e8a1d5d9ef4d28c949f67b6` (01:01:30 UTC). Les commits ultérieurs complètent les preuves et les rapports.
- Lecture des objets Git et analyse SHA256, JSON et AST écrites pour cette réception. Aucun code, import ou script entrant exécuté ; aucun checkout, mutation Git ou fichier canonique modifié.

## Périmètre exact à reprendre

Huit HTML et deux glossaires sont nouveaux sur la base main. Tous existent, ont des empreintes conformes au dernier tableau du rapport reçu et sont inventoriés dans `INVENTAIRE.json` avec leurs blobs Git. Les huit HTML diffèrent réellement de la version du premier audit ; les deux glossaires restent identiques à cette première remise.

| Fichier | Octets | SHA256 de la source reçue |
| --- | ---: | --- |
| `chapters/I83/I83_a.html` | 52803 | `1610615e2f39a888d4ccb46b46b56a4ea0c5195f19dfd8af68cac511f7f0ff76` |
| `chapters/I83/I83_b.html` | 52952 | `d336d0b4e4977212ffa192fe2c57a535db54f288daa2ce014c022d513ed9da9a` |
| `chapters/I83/I83_c.html` | 60210 | `ed129bc2d10d36cca74a8a0ab6d3994e9ba101e65ffe3392e84ada8473e48261` |
| `chapters/I83/I83_d.html` | 29910 | `8f4743ecd4d49746529b5d1ed7a13a5ed2285af33fb14a8795fa8116342244b3` |
| `chapters/I83/I83_pop1.html` | 32279 | `a790feb6f96e5805da69f398daf23a617813424a44dad8d14d94e1b2348e36cd` |
| `chapters/I83/I83_pop2.html` | 42158 | `e19683146892162c19e526fda676e558f21d42e894738b6a90ab3475086b1d55` |
| `chapters/I83/I83_pop3.html` | 17601 | `c0c1dda088686b7abf4f2b38f4f858298a37c46e1d3003f50e06c6b221697c42` |
| `chapters/I83/I83_pop4.html` | 26210 | `8b5a5d007ff4d789e15199bc19a658cc8a35b5388afb89f2804c6e521ba904d1` |
| `glossary/fragments_medina.py` | 2649 | `8d3ecb13d21a3e1e0c53b144e024a564f5aaa0501dc6518b19dff05ebdc0fced` |
| `glossary/i83.py` | 12435 | `b041af30d40c15eb16c0063dc7d83fa0a57c364608d36ccb38003bf2af7636b4` |

`chapters.json` passe de 31 à 32 entrées. L’unique différence de structure est cette proposition :

```json
{"code":"I83","covers":["I83","I87"],"title":"Varices des membres inférieurs","integrated":true,"wave":9,"added":"2026-10-08"}
```

Aucune entrée existante n’est retirée ou modifiée. Aucun code ou `covers` de main ne revendique I83/I87 (C-01-Cardiologie). Le drapeau `integrated:true` décrit la proposition reçue, pas une injection déjà faite sur main. Le champ `covers` donne une route ; le cours indique expressément que I87.8/I87.9 (C-01-Cardiologie) ne sont pas développés et ne revendique aucune complétude CIM-10-GM ou CIM-11.

Les glossaires ajoutent 33 clés de cours et 5 clés de noms complets de fragments. Analyse des 912 clés `a(...)` existantes sur main : **aucune collision**, aucun doublon entre les 38 clés nouvelles. Le fichier partagé de fragments est absent de main et constitue bien un ajout, pas le remplacement d’un fichier existant. Syntaxe Python analysée sans exécution.

Le manifeste racine `livraisons/Livraison Claude/C-01-Cardiologie/livraison.json` est absent de cette tête. Le paquet est une remise de nouveau chapitre par branche avec catalogue/glossaire et lot de preuves, pas un lot `apply-claude`. Ne pas conditionner cette remise à un ancien manifeste ; ne pas fusionner toute la branche pour injecter ce seul chapitre.

## Corrections réellement reçues

Le lot `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83/` contient **20 fichiers** ; toutes les tailles et empreintes sont dans l’inventaire. Le rapport reçu est le blob `4a6d8f42a3ca45b6b7eb5f64282b09ac0abb905d`, SHA256 `2b06dd18e42a58abad3daf34febec68858d43c7a692e910a076383c674486482`. Ses paragraphes initiaux et premiers tableaux restent historiques : appliquer l’Addendum 4 pour les empreintes de cours, les Addenda 6 et 7 pour les dernières pièces.

- `CORRECTIONS_AUDIT_CODEX.json` contient 27 éléments : 19 marqués corrigés et 8 qualifiés par Claude. Les quatre limites marquées fermées dans `LIMITES_FERMEES.json` sont des décisions du producteur, pas quatre validations indépendantes.
- La contre-indication suisse du diabète aux sclérosants apparaît maintenant dans `I83_d.html:48,50` et `I83_pop4.html:26,27,67` : elle n’est plus rétrogradée en simple contre-indication relative au motif du silence ESVS.
- L’EHIT III reçoit explicitement une anticoagulation curative et une surveillance échographique hebdomadaire dans `I83_pop2.html:47,123`. Le glossaire inchangé mentionne IV, sans dire « seulement IV » ; harmonisation à trancher par l’auditeur médical.
- Les changements CEAP/3 mm, index artériel/compression, mousse et diamètre, phase aiguë de thrombose superficielle, délai de toxicité et portée de la dose ESVS sont présents dans les deltas de cours. Leur fidélité médicale doit être jugée sur les textes finaux par le poste médical, pas par le statut JSON du producteur.
- Le commit `0974d854db292ae0311e435b3daea5fbed187e25` répond explicitement à la réception Codex `43f4604` en corrigeant le précédent extrait Rapidocain qui mêlait sommaire et sections. Il ne modifie aucune des dix sources de cours/glossaire.

## Preuves suisses : présence et portée

**Rapidocain.** L’extrait final `preuves/rapidocain_extraits.md` est présent : 17 022 octets, SHA256 `262383bd90e0767c846f163b8fe31c67a5bc6f190a07d43d616ce92243bd6308`, blob `5106966c1976119e88615c7e84fad423309a4e82`. Il contient les lignes du texte de posologie, contre-indications, mises en garde, surdosage et pharmacocinétique. Sa preuve déclare les autorisations 20272/32381, version de juillet 2024, les URL Swissmedicinfo et deux empreintes de copies complètes. Ces copies ne sont pas versionnées ; l’empreinte de l’extrait ne doit pas être confondue avec celle du texte intégral déclaré `7b24cf…`.

Une condition présente dans cette nouvelle pièce nécessite une décision médicale concrète : la ligne source 305 interdit aussi les solutions avec conservateurs pour d’autres blocages nécessitant plus de 15 mL. `I83_pop4.html:50` associe la recette ESVS à 50 mL de lidocaïne à une présentation Swissmedic en flacon de 20 mL, sans préciser le choix sans conservateurs. Le poste médical a été alerté et examine cette compatibilité. La réception constate la condition ; elle ne résout pas sa portée clinique.

**Aethoxysklerol.** `PREUVE_AETHOXYSKLEROL_COMPRESSION.md` est présent, 2 724 octets, SHA256 `f4c730fd162b1e117ebb34c8743b127a08f88529870b772320f72ae07bc34be1`. Autorisation 33273, version de novembre 2022 et URL Swissmedicinfo/Compendium sont déclarées. Les durées différenciées de compression sont extraites. La copie complète n’est pas versionnée ; sa fidélité externe n’est pas certifiée par cette sentinelle.

**OFSP.** Le fichier versionné `preuves/ofsp_liste_specialites_20261001_veinotropes.ndjson` contient 7 Bundle FHIR valides, 105 604 octets, SHA256 `0aa489dc1b44431b2fdf59c421dd71a9036c8f16ab90c616e2d2788b79e40b45`. Les identifiants correspondent aux sept produits annoncés : Aesculamed forte, Daflon 500, Diosmin Hesperidin Zentiva, Doxium 500, Doxocur 500, Venoruton 1000 et Venoruton Forte. Les **15** extensions `reimbursementSL` portent toutes `Reimbursed`, `Listed` et `costShare=10`. Aucun champ de limitation n’est présent dans ces sept bundles.

Cela soutient les inscriptions positives et la quote-part déclarées. **Un sous-ensemble de sept produits ne prouve pas l’absence de tout autre produit dans la publication complète.** L’archive annuelle de 188 Mo et son membre français sont décrits avec URL et SHA256 mais ne sont pas versionnés. Les exclusions absolues de remboursement reposent donc sur la recherche déclarée par Claude dans l’archive complète ; les qualifier dans la décision médicale si cette recherche ne peut pas être contrôlée. Ne pas demander un doublon du sous-ensemble déjà reçu.

Aucun téléchargement de source officielle n’a été effectué dans ce poste. La fidélité externe des extraits ne doit pas être annoncée comme vérifiée à partir de leur seule cohérence interne.

## Ce qui conditionne encore l’injection maintenant

1. **Contrelecture médicale finale** des sources reçues, avec décision explicite sur la compatibilité Rapidocain/conservateurs et les éventuelles formulations absolues OFSP. Les deux anciens défauts bloquants disposent de corrections visibles ; ne pas les recopier comme absents de la remise actuelle.
2. **Validation technique de confiance sur la base main actuelle** avec extraction sélective des dix sources et ajout de l’entrée de catalogue. Les pièces producteur les plus récentes prétendent une simulation sur `31b086a938a4b5acfdcda7ad12a2908e4de42dde`, native 1 923 contrôles et S01 72 contrôles ; elles sont présentes mais n’ont pas été exécutées par cette sentinelle. Le test S01 doit correspondre à 21 cours après cet ajout, et cibler la construction contenant ce paquet.
3. **Reprendre le périmètre sélectionné** après fermeture des postes précédents. Les catégories et routes restent groupées sous C-01-Cardiologie. Un nouveau SHA Claude devra faire l’objet d’un delta ciblé ; ce rapport concerne uniquement `0974d854db292ae0311e435b3daea5fbed187e25`.

Pour la réception, il n’existe aucune raison structurelle de faire attendre un nouveau paquet identique. La décision restante porte sur les conditions médicales et le résultat de la validation actuelle, pas sur une absence de fichiers ou de remise.
