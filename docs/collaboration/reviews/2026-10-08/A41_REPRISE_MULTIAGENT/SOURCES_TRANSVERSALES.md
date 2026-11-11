# Sources transversales — A41 — Sepsis et choc septique de l’adulte (I-03-Infectiologie)

La page primaire SCCM SSC2026 est réellement accessible, archivée et lue : 129 cartes de recommandations, dont 46 nouvelles annoncées, publication affichée du 23 mars 2026. Chaque énoncé sélectionné, gradation et remarque est conservé dans `SOURCES_TRANSVERSALES.json` et `ssc2026.cards.json`. Le nombre historique 128 n’est pas vérifié dans une capture ancienne et aucune évolution de version n’est inventée.

Source primaire : https://www.sccm.org/clinical-resources/guidelines/guidelines/surviving-sepsis-campaign-international-guidelines-for-management-of-sepsis-and-septic-shock-2026

Capture `/workspace/medina-env/reprise-a41/sources/ssc2026.primary.html`, SHA256 `6266900db8ffb882bff477792023b20f24ece8387bbff854062b5b8b2788bcd1`. Le cache de Claude_spec a été réutilisé avec contrôle d’empreinte, sans requête doublonnée. SSC2021 PMC8486643 est également conservé comme texte primaire complet accessible, SHA256 `59987a3ccbb78857ed62a113e583bb474c16169fd8480bc82b0604c66c11b861`.

Le rectificatif primaire https://doi.org/10.1007/s00134-026-08410-9 a été obtenu et son corps lu. Publication en ligne et version of record : **5 mai 2026** ; numéro de revue : juin 2026. Il corrige le « c » ajouté pendant la composition à quatre noms d’auteurs : Alhazzani, Dionne, Honarmand et Rochwerg. « The Original Article has been corrected. The Publisher apologises for this mistake. » Aucun changement clinique ou de gradation n’est décrit ; ce rectificatif n’explique pas le compte 128/129. Capture `ssc2026_publisher_correction.html`, SHA256 `a1f34b5e0f2143c190622c5cc8f1026c0c7a04c9ab9c2b36e9319d6a9b33c64e`.

Les éléments utiles aux quatre auteurs ont été transmis avec les chemins et énoncés exacts : cultures avant antibiotiques si possible, lactate initial et sériel, contrôle du foyer idéalement sous six heures, MAP65 et adaptation60–65 après65ans, fluides/vasopresseurs simultanés selon instabilité, risques résistants/anaérobies/antifongiques, bêta-lactamines prolongées après charge, PCT pour arrêt avec évaluation clinique et contrôle du foyer. Les mentions de force et certitude restent celles des cartes primaires ; une absence de recommandation n’est pas transformée en recommandation faible.

LWW DOI7075 refuse l’accès avec HTTP402 ; pas de texte intégral revendiqué et aucun contournement. PubMed et EuropePMC servent ici aux métadonnées, distinctes de la lecture des cartes SCCM. Le PDF CHUV PCT accessible est ancien (liste Analyses2010), sans normes ni tableau de faux positifs/négatifs. La discordance d’unité lactate HUG signalée par l’auteur examens reste explicite ; aucune correction silencieuse.

Ownership : P1 écrit seulement a+pop1 ; P2 b+pop_pa ; P3 c+pop_sciences_revision ; P4 d+pop2 et assemble les sept Pareto. Root possède glossaire et banque. Aucun auteur ne partage un fichier avec un autre. Le candidat A41 demeure en écriture : aucun build du candidat lancé.

Le préflight après redémarrage passe : Python3.12.14, Node24.19.0, Playwright et Chromium151 disponibles ; HTTP local200, MDN_READY, A41 canonique quatre onglets et aucune erreur de page. Le serveur local fournit les ressources modulaires embarquées avec SHA256 vérifié. Les deux premiers essais de fixture sont conservés ; ils échouaient parce que la fixture ne servait pas lesson-core.js. Aucune assertion n’a été supprimée et aucun défaut applicatif n’est déduit de cette erreur de transport.

Les horaires Europe/Zurich, URL finales, statuts, empreintes et limites sont consignés dans le JSON. Ce rapport porte sur sources et disponibilité technique, pas sur un candidat A41 validé.

Le cache pharmacologique lu par Claude_spec est maintenant conservé hors /tmp sous `/workspace/medina-env/reprise-a41/sources/pharmacologie/`. L’index ARCHIVAGE.json relie chaque document à son URL, sa version et ses passages du rapport auteur ; les copies et les empreintes annoncées disponibles sont vérifiées. La sentinelle attribue explicitement cette lecture médicale à l’auteur.

Les captures temporaires de P1 sont également copiées avec vérification des empreintes dans `/workspace/medina-env/reprise-a41/sources/pathologie1/ARCHIVAGE.json`. Le niveau de lecture et les limites restent ceux documentés par sentinelle_medicale.
