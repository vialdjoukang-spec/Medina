# Inventaire technique — E-06-Endocrinologie et métabolisme

Snapshot du tronc : `bc3a56fa8ef7abdc048e9bb0b4e94dd850b1c373`. Les 79 références distantes `origin/*` actualisées par le coordinateur représentent 78 têtes distinctes. Les 77 catégories S05 ont été recensées ; les 353 variantes de fichiers HTML sont décrites avec empreintes et branches dans `html-variants.json`.

Avant cette mission, le fragment public répond HTTP 200 et contient 25 cours. Les gabarits décompressés du site sont strictement identiques à ceux reconstruits localement sur le snapshot (`template-comparison.json`).

Un cours supplémentaire complet, **E59 — Carence alimentaire en sélénium**, est disponible dans Betta C42 : six HTML et un glossaire, 243 313 octets. Le commit isolé `802543fc99b0f022ca33aa9d815681af2c41822b` copie ces sept fichiers à l’identique dans les chemins canoniques, sans modifier les registres partagés. Les empreintes source/cible sont données dans `E59-source-hashes.json`. Les figures SVG sont intégrées ; aucun asset externe au lot n’est nécessaire. Les métadonnées proposées figurent dans `E59-metadata-proposal.json` ; le coordinateur centralise leur intégration et la publication.

**E60 — Carence alimentaire en zinc** ne possède que `recherche.md` et `sources.json` dans Betta C42. Ces travaux restent à publier comme recherche en cours ; aucun HTML de cours ni glossaire n’est inventé. Les 50 autres catégories ne possèdent aucun HTML ni recherche de leçon repéré aux têtes distantes examinées.

Les copies E11 de livraison et provenance diffèrent du canonique ; elles sont conservées et inventoriées sans remplacer ses corrections déjà intégrées. Les candidats Betta des 22 cours déjà injectés sont identiques aux HTML canoniques.

Contrôles exécutés : `test_v7.py --static` réussit pour les 25 cours du snapshot et pour E59 ; le build isolé S05 réussit (4 447 596 octets). Aucun chemin d’image locale manquant n’a été repéré dans les 25 cours. Le contrôle navigateur existant `test_v7.py` passe pour E59 sur ordinateur et mobile dans le frontend S05 complet, avec quatre onglets, fenêtres, Navigo, police et taille, mode livre et débordement horizontal. Deux captures réelles sont jointes ; l’ouverture a été inspectée. Le build brut dépourvu d’habillage n’était pas l’artefact livré et son essai Navigo a été remplacé par ce contrôle du frontend S05 complet. Le parcours borné des 25 cours initiaux passe : 50 routes sur ordinateur/mobile, 200 onglets et 168 ouvertures de fenêtres, sans erreur JavaScript retenue ni débordement mobile (`browser-smoke.json`). Le parcours historique de toutes les occurrences répétées a été interrompu volontairement ; aucun succès complet de cette commande interrompue n’est revendiqué.

Cette mission effectue un inventaire et des contrôles techniques. Aucun audit médical, aucune lecture indépendante de source clinique et aucune validation médicale humaine ne sont revendiqués. Les statuts historiques d’audit restent conservés. Les états ci-dessous décrivent le snapshot avant la publication centralisée de cette mission.

| Code | Intitulé | État au snapshot |
|---|---|---|
| C73 | Tumeur maligne de la thyroïde | Aucun contenu repéré |
| C74 | Tumeur maligne de la surrénale | Aucun contenu repéré |
| C75 | Tumeur maligne d’autres glandes endocrines et structures apparentées | Aucun contenu repéré |
| D34 | Tumeur bénigne de la thyroïde | Aucun contenu repéré |
| E00 | Syndrome d’insuffisance thyroïdienne congénitale | Publié avant mission |
| E01 | Affections thyroïdiennes et apparentées liées à une carence en iode | Publié avant mission |
| E02 | Hypothyroïdie par carence inapparente en iode | Publié avant mission |
| E03 | Autres hypothyroïdies | Aucun contenu repéré |
| E04 | Autres goitres non toxiques | Aucun contenu repéré |
| E05 | Thyréotoxicose [hyperthyroïdie] | Publié avant mission |
| E06 | Thyroïdite | Aucun contenu repéré |
| E07 | Autres affections de la thyroïde | Publié avant mission |
| E10 | Diabète sucré de type 1 | Publié avant mission |
| E11 | Diabète sucré de type 2 | Publié avant mission |
| E12 | Diabète sucré de malnutrition | Publié avant mission |
| E13 | Autres diabètes sucrés précisés | Aucun contenu repéré |
| E14 | Diabète sucré, sans précision | Publié avant mission |
| E15 | Coma hypoglycémique non diabétique | Aucun contenu repéré |
| E16 | Autres anomalies de la sécrétion pancréatique interne | Aucun contenu repéré |
| E20 | Hypoparathyroïdie | Aucun contenu repéré |
| E21 | Hyperparathyroïdie et autres maladies de la glande parathyroïde | Aucun contenu repéré |
| E22 | Hypersécrétion de l’hypophyse | Aucun contenu repéré |
| E23 | Hyposécrétion et autres anomalies de l’hypophyse | Aucun contenu repéré |
| E24 | Syndrome de Cushing | Aucun contenu repéré |
| E25 | Anomalies génito-surrénaliennes | Publié avant mission |
| E26 | Hyperaldostéronisme | Aucun contenu repéré |
| E27 | Autres maladies de la glande surrénale | Aucun contenu repéré |
| E28 | Dysfonction ovarienne | Aucun contenu repéré |
| E29 | Dysfonction testiculaire | Aucun contenu repéré |
| E30 | Anomalies de la puberté, non classées ailleurs | Publié avant mission |
| E31 | Dysfonctionnement pluriglandulaire | Aucun contenu repéré |
| E32 | Maladies du thymus | Publié avant mission |
| E34 | Autres troubles endocriniens | Publié avant mission |
| E35 | Anomalies endocriniennes au cours de maladies classées ailleurs | Publié avant mission |
| E40 | Kwashiorkor | Publié avant mission |
| E41 | Marasme nutritionnel | Publié avant mission |
| E42 | Kwashiorkor avec marasme | Publié avant mission |
| E43 | Malnutrition protéino-énergétique grave, sans précision | Aucun contenu repéré |
| E44 | Malnutrition protéino-énergétique légère ou modérée | Aucun contenu repéré |
| E45 | Retard de développement après malnutrition protéino-énergétique | Publié avant mission |
| E46 | Malnutrition protéino-énergétique, sans précision | Publié avant mission |
| E50 | Avitaminose A | Publié avant mission |
| E51 | Carence en thiamine [carence en vitamine B1] | Publié avant mission |
| E52 | Carence en acide nicotinique [pellagre] | Publié avant mission |
| E53 | Autres avitaminoses du groupe B | Aucun contenu repéré |
| E54 | Carence en acide ascorbique | Publié avant mission |
| E55 | Carence en vitamine D | Aucun contenu repéré |
| E56 | Autres avitaminoses | Publié avant mission |
| E58 | Carence alimentaire en calcium | Publié avant mission |
| E59 | Carence alimentaire en sélénium | Candidat HTML complet, non publié |
| E60 | Carence alimentaire en zinc | Recherche seule |
| E61 | Carences en autres éléments nutritionnels | Aucun contenu repéré |
| E63 | Autres carences nutritionnelles | Aucun contenu repéré |
| E64 | Séquelles de malnutrition et autres carences nutritionnelles | Aucun contenu repéré |
| E65 | Adiposité localisée | Aucun contenu repéré |
| E66 | Obésité | Aucun contenu repéré |
| E67 | Autres excès d’apport | Aucun contenu repéré |
| E68 | Séquelles d’excès d’apport | Aucun contenu repéré |
| E70 | Anomalies du métabolisme des acides aminés aromatiques | Aucun contenu repéré |
| E71 | Anomalies du métabolisme des acides aminés à chaîne ramifiée et du métabolisme des acides gras | Aucun contenu repéré |
| E72 | Autres anomalies du métabolisme des acides aminés | Aucun contenu repéré |
| E73 | Intolérance au lactose | Aucun contenu repéré |
| E74 | Autres anomalies du métabolisme des hydrates de carbone | Aucun contenu repéré |
| E75 | Anomalies du métabolisme des sphingolipides et autres anomalies du stockage des lipides | Aucun contenu repéré |
| E76 | Anomalies du métabolisme des glucosaminoglycanes | Aucun contenu repéré |
| E77 | Anomalies du métabolisme des glycoprotéines | Aucun contenu repéré |
| E78 | Anomalies du métabolisme des lipoprotéines et autres lipidémies | Aucun contenu repéré |
| E79 | Anomalies du métabolisme de la purine et de la pyrimidine | Aucun contenu repéré |
| E80 | Anomalies du métabolisme de la porphyrine et de la bilirubine | Aucun contenu repéré |
| E83 | Anomalies du métabolisme des minéraux | Aucun contenu repéré |
| E84 | Fibrose kystique | Aucun contenu repéré |
| E85 | Amylose | Aucun contenu repéré |
| E86 | Hypovolémie | Aucun contenu repéré |
| E87 | Autres déséquilibres hydro-électrolytiques et acido-basiques | Aucun contenu repéré |
| E88 | Autres anomalies métaboliques | Aucun contenu repéré |
| E89 | Anomalies endocriniennes et métaboliques après des actes médicaux, non classées ailleurs | Aucun contenu repéré |
| E90 | Anomalies nutritionnelles et métaboliques au cours de maladies classées ailleurs | Aucun contenu repéré |

[Capture d’ouverture d’E59](E59-ouverture-bureau.png) · [Capture de fenêtre d’E59](E59-fenetre-bureau.png)
