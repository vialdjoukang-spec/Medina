# Rapport de rédaction : G90 Affections du système nerveux autonome (cycle Betta 40, leçon 2)

Agent C40-A1-NEUR (Sonnet 5.5), fragment N-05-Neurologie, 15.10.2026. Audit différé : revue IA, distincte d'une validation médicale humaine.

## Fichiers (octets)
chapters/G90/G90_a.html 32 993 ; G90_b.html 29 630 ; G90_c.html 37 033 ; G90_d.html 12 232 ; G90_pop1.html 29 936 ; G90_pop2.html 21 163 (total 162 987) ; glossary/g90.py (entrées conditionnelles : abréviations, codes CIM-10-GM, noms propres) ; rapport.md.

## Contenu
Quatre onglets. Pathologie : 14 îlots (g90-0 à g90-13), dernier îlot = critères formels (div.alert) puis paramètres clés (div.key), références en fin de partie. Examens : 7 îlots (hiérarchie avec référence par question, mesures orthostatiques et test d'inclinaison, tests autonomes et mesure de 24 heures, massage sinocarotidien, Horner, SDRC et tableau diagnostics × examens, 6 cas corrigés). Sciences : anatomie de la voie oculosympathique, physiologie (baroréflexe, natriurèse de pression, dysréflexie), génétique et immunologie, chacune avec schéma SVG et corrélations science → clinique, examen, traitement. Pharmacologie : 4 îlots (stratégie, midodrine, fludrocortisone, interactions et surveillance) et 2 cas. 52 fenêtres (dont 16 Pareto), 8 quiz, 46 mots verts, 6 schémas SVG légendés, environ 14 000 mots.

## Sources utilisées
Uniquement recherche.md / sources.json (S1 à S26) : CIM-10-GM 2024, ESC 2018 syncope, consensus AAS/EFAS 2018, standards European Pain Federation, informations professionnelles Swissmedic Midodrin Substipharm et Florinef, revue de Maamouri sur le Horner, revue de Eldahan sur la dysréflexie, dysautonomie familiale, tachycardie posturale, Revue médicale suisse (résumés). Aucune donnée ajoutée de mémoire ; les inférences pédagogiques (par exemple la raison du seuil de 30 mmHg, le rôle du baroréflexe dans la dysréflexie) sont signalées comme explications du cours.

## Lacunes reprises du dossier (signalées dans le texte et la fenêtre g90-lacunes)
Aucune recommandation de la Société suisse de neurologie ni du Swiss Medical Forum lue ; textes de la Revue médicale suisse lus en résumé ; seuils chiffrés de la tachycardie posturale non rédigés ; conduite aiguë de la dysréflexie issue d'une revue américaine (Veterans Affairs), présentée comme telle, sans dose, avec renvoi au protocole du centre spécialisé ; consensus de Valence, classes ESC du tableau de traitement, technique du massage sinocarotidien, épidémiologie suisse, informations professionnelles de la nifédipine, de la nitroglycérine et des bisphosphonates non lues. Rattachement CIM de la ganglionopathie auto-immune non confirmé. Aucune source lue sur grossesse, insuffisance rénale ou hépatique pour ces entités (dit dans le texte).
Choix de présentation : les segments médullaires sont écrits en toutes lettres (« 6e segment thoracique ») ; pas de tableau consacré au code CIM (les sous-codes figurent en fenêtre g90-codage, avec les pièges G23.8 et I95.1). Vignettes et cas déclarés fictifs ; calculs : 148 − 112 = 36 mmHg ; classe 168/104 mmHg = modérée.

## Auto-contrôle (cahier W)
HTML bien formé (pile vide sur a+b+c+d et sur les fenêtres) ; 0 identifiant dupliqué, tous préfixés g90- ; 0 clé de fenêtre sans template, 0 fenêtre orpheline, clés préfixées g90- ou pareto-g90- ; audit des abréviations (build_medina.audit avec le glossaire g90) : {} ; build_medina sur copie isolée : « G90 non couvertes: 0 » ; couvertures Pareto résolues ; classes toutes issues du modèle N17/D50. Le test navigateur test_preview.py ne s'exécute pas dans cet environnement (module lesson-core.js absent du dépôt ; même échec sur N17), il n'a donc pas été obtenu. Aucun fichier hors du dossier de livraison n'a été modifié ; ni chapters.json, ni git.
