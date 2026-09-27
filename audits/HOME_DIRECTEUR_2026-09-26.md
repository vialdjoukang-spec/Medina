# Accueil — directeur des systèmes

Le directeur apparaît sous l'en-tête de l'accueil de MEDINA_Alpha. Son bouton natif ouvre une carte par système possédant au moins un cours intégré. La carte ouvre le parcours du système dans la spécialité et les pastilles donnent accès aux cours individuels.

Les jauges sont calculées depuis `chapters.json` et `shell/data.py` lors de la reconstruction. Le cœur reprend la clôture éditoriale de 56/56 catégories, cours et renvois inclus ; le poumon couvre 11/64 catégories. Le pourcentage exprime la couverture rédactionnelle et ne prétend pas mesurer une validation médicale. Les systèmes sans cours intégré n'apparaissent pas encore dans le directeur.

Contrôles du 26 septembre 2026 : reconstruction du HTML, syntaxe JavaScript, cohérence des 2 destinations système avec le registre intégré, 20 destinations de cours et 2 jauges. Vérification dynamique de l'injection à l'accueil et de son absence hors accueil avec un DOM simulé. Le rendu graphique dans un navigateur réel reste à inspecter.

Mise à jour du cycle 1 : I26 porte le poumon à 12/64, A41 ouvre l'infectiologie à 1/155 ; le directeur présente désormais 3 systèmes et 22 cours intégrés. Ces deux nouveaux cours ne portent pas l'insigne « 100 % rédigé ».
