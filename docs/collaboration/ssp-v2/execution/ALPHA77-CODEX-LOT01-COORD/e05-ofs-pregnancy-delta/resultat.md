# E05 — preuve OFS et grossesse, lecture ciblée sans changement du cours

Candidat lu : `721b86af6bde93f751d8e785e1506b1836841b32`. Recherche du15octobre2026, heures UTC23:19–23:22. Périmètre : seule réserve «OFS applicable/pregnancycodes» de REMAINING-PROOF ; aucun audit général ni relecture BWPS/hydrocortisone/EUGOGO. Aucun statut, source, reçu0001 ou branche modifié. Les sept core restent propres et leurs empreintes sont dans source-readings.json.

## Résultat vérifiable

**L’édition CIM-10-GM2024 affichée en tête du cours est bien applicable en Suisse en2026.** Le tableau primaire OFS publié le31mars2026, ongletFR, A15/C15, donne «CIM-10-GM2024» / «2025-2026». A14/C14 donne «CIM-10-GM2026» / «Dès2027». URL : https://dam-api.bfs.admin.ch/hub/api/dam/assets/36518419/master ; ce fichier est un XLSX, conservé ici sous ofs-validity.xlsx. SHA256 `b122a82c797a627557affc1a30ccd764860d46694f3a5fb4d9621af7193169e4`.

Le Lisez-moi de l’archive OFS française CSV2024, daté31.10.2024, confirme l’entrée en vigueur le1erjanvier2025 et son caractère obligatoire pour le codage des diagnostics du relevé SpiGes (séjours stationnaires en hôpitaux). Cette obligation est hospitalière : elle ne certifie ni un remboursement ni une applicabilité universelle en ambulatoire. La page OFS courante classe les fichiers2024 sous «Instruments en vigueur…2026», et indique aucune mise à jour CIM aux1.1.2026 et1.7.2026. Les composants publics chargent un modèle JSON via current-node+.model.json ; ces deux modèles ont été obtenus et leurs URL sont consignées. Aucune restriction réseau n’a été contournée.

## Grossesse, post-partum et nouveau-né : portée exacte

Le ClaML primaire OFS2024 français obtenu en ligne (asset32686264, 31.10.2024) confirme :

- **E05** : inclusions «affection oculaire» avec renvoiH58.8* et «affection cardiaque» avec renvoiI43.8* ; exclusions «thyroïdite chronique avec thyréotoxicose transitoire»→E06.2 et «thyréotoxicose néonatale»→P72.1.
- **E06**, et non une exclusion directement portée par E05 : «thyroïdite du post-partum»→**O90.5**.
- **P72.1** : «Hyperthyroïdie transitoire néonatale», incluant «Thyréotoxicose néonatale».
- **O99.2** : «Maladies endocriniennes, nutritionnelles et métaboliques compliquant la grossesse, l’accouchement et la puerpéralité», inclusion «États en E00-E90». Exclusions : diabète→O24.-, malnutrition→O25, thyroïdite du post-partum→O90.5.
- **O99** porte la condition : états compliquant la grossesse, aggravés par elle, ou raison principale de soins obstétricaux sans rubrique spécifique indiquée dans l’index ; «Utiliser, au besoin, un code supplémentaire pour identifier une affection spécifique.» Le chapitreIV exclut les complications de grossesse/accouchement/puerpéralité→O00-O99.

**Aucune chaîne O99/O90/P72 n’est littéralement affichée dans les sept core E05 actuels.** S11 et la recherche existante citent E06.2/P72.1/O90.5 ; le coursA02 donne leurs exclusions en prose. Cette recherche confirme les libellés et renvois suisses correspondants, sans inventer des codes déjà affichés. O99.2 constitue une preuve de classement complémentaire utile à la réserve grossesse ; aucune consigne de séquençage systématique «O99.2+E05» n’est déduite sans la règle applicable du Manuel suisse de codage2026.

## Ce que cette preuve permet et ses limites

L’applicabilité suisse du millésime2024 est désormais étayée par une source primaire exacte ; les exclusions de S11 et la place distincte du post-partum sont confirmées par le ClaML suisse. La phraseA02 regroupe les exclusions du bloc thyroïdien ; si une future correction précise leur niveau, E06 porte directement O90.5 et E05 porte E06.2/P72.1. Ce constat ne change pas le cours dans cette mission.

Le Manuel suisse de codage2026, ses règles détaillées de séquençage et le codage d’un cas individuel de thyrotoxicose gestationnelle n’ont pas été lus ici : ces points restent non vérifiés. Aucun remboursement, traitement, dose, nouvelle validation clinique ou clôture n’est attesté. REMAINING-PROOF conserve toutes ses autres composantes. Les sources accessibles ont toutes réponduHTTP200 ; aucun échec d’accès primaire n’est masqué.

Voir `source-readings.json` pour les passages exacts XML, les cellules, les dates, URL et SHA256, ainsi que les requêtes réellement utilisées. Les téléchargements restent uniquement dans ce dossier de recherche scratch.
