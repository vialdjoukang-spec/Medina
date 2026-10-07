# Vérification des interfaces catégorielles

Les 22 fragments originaux exposent 1 636 catégories du catalogue local **CIM-10-GM 2024**, organisées en 265 blocs. Les 31 cours intégrés sont distingués des chapitres à produire. Cette vérification porte sur la navigation et la conservation du catalogue ; elle ne certifie pas une complétude CIM-11 ni une validation médicale exhaustive.

- 656 vérifications dans un navigateur réel sur les 22 fragments : aucune erreur JavaScript, aucune ressource distante demandée.
- Toutes les catégories conservées exactement une fois dans leurs blocs ; chapitres numérotés continûment dans chaque catégorie.
- Couleurs distinctes, contraste des titres et des codes supérieur ou égal à 4,5:1, codes discrets en haut à droite, aucune superposition ni débordement sur les écrans testés.
- Un cours « Bronchite » pour J20, J40, J41 et J42 ; renvois entre blocs et recherche unique avec les quatre intitulés associés.
- Renvois J46 → Asthme J45 et J43 → Bronchopneumopathie chronique obstructive J44 vérifiés.
- Onglets, QCM, fenêtres interactives, taille de lecture, mode Livre, Navigo et sémiologie CS conservés.
- 55 contrôles supplémentaires sur S02 ; 71 contrôles historiques S01 réussis.

La copie figée des 22 HTML a conservé exactement les mêmes empreintes SHA-256 avant et après les 656 contrôles. Les empreintes et le périmètre sont consignés dans `build_manifest.json`. Les résultats complets sont dans `categories_results.json` et `pulmonaire/categories_results.json` ; S01 est documenté dans `../s01/browser-results.json`.

T2, T5 et T7 signalent explicitement l’absence de catalogue CIM local. Les codes techniques S01…T7 restent des identifiants internes ; les noms publics suivent le registre des fragments.
