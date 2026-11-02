# E00 — paquet de reprise et auto-relecture

Le cours est repris dans la branche réservée `codex/alpha77/e00-integrate-g1`, sur la base `8a512893acbab9caa0dcfdd0e8682a44ea72fda6`. Les relectures médicale, linguistique et visuelles sont celles de l’auteur IA, explicitement marquées `self_review`. Elles ne constituent ni une revue indépendante ni une validation médicale humaine. Aucune PR ni publication sur main.

## À voir

- [Aperçu natif autonome](E00-apercu-autonome.html), ouvrant E00 avec les octets de la figure originale incorporés.
- [Sémiologie sur ordinateur](1440-semiology.png) et [sur téléphone](390-semiology.png).
- [Anatomie originale annotée](1440-anatomy-original.png) et [histologie sur téléphone](390-histology-original.png).
- [Interactions à 24 pixels](1440-font24-pharmacology.png), [mode livre à 24 pixels](390-book24-pharmacology.png), [colonne thérapeutique accessible par défilement du tableau](390-font24-table-right.png).
- [Fenêtre de calcul de dose](390-dose-popup.png) et [normes, seuils et cibles](1440-examinations.png).

## Étendue vérifiée

Six fichiers HTML : 11,474 → 18,410 mots mesurés sur toutes les surfaces, fenêtres comprises. Les nombres ne sont pas des notes de qualité. Sciences : 1 207 → 4 179 mots, quatre → six disciplines, trois → sept occurrences de figures. Les sept occurrences comprennent deux affichages du même original humain et cinq schémas/graphique non anatomiques.

La sémiologie est le premier sous-onglet, avec neuf sections et le titre contractuel exact. Les [14 points monographiques et 20 rubriques](coverage-14-20.md) sont reliés à des ancrages existants et à leurs sources. Cinquante-six fenêtres sont référencées,52identifiants sont uniques,26cibles Pareto sont résolues et les cinq quiz ont été testés.

## Corrections principales

- Absorption d’Euthyrox : diminution relative pouvant atteindre20%, et non absorption absolue à20%. FI suisse, annexe SwissPedDose, posologies adultes/pédiatriques, interactions, contre-indications et grossesse distinguées.
- Seuil de TSH>20 replacé dans la confirmation sérique néonatale vers la deuxième semaine ; zone6–20 et avis expert explicités. Suivi central fondé principalement sur fT4, axe surrénalien sécurisé avant substitution.
- Prévention suisse OSAV : apport total, complément individualisé et posologie médicamenteuse séparés. Pas d’huile iodée prescrite sans FI exacte.
- Médianes d’iodurie interprétées comme indicateurs de groupe ; sous-groupes OSAV et étude primaire non fusionnés. Données anciennes datées et population des études conservée.
- Contribution hormonale maternelle non présentée comme exclusive jusqu’à une date fixe. Observation historique au scanner non transformée en indication systématique. Hypothèse mammaire du thiocyanate séparée du schéma thyroïdien.
- Collision TPO corrigée localement : la fenêtre explique la thyroperoxydase, sans modifier le glossaire partagé de thrombopoïétine.

## Origine des figures et sources

L’original OpenStax College de2013, figure1811, provient de Commons et est accompagné de sa preuve de licence CC BY3.0 propre à cette version. La licence actuelle du manuel2e édition n’est pas utilisée pour la figure. Les numéros sont superposés dans la page ; aucun pixel original n’a été retouché. Le dessin anatomique et la micrographie sont présentés comme normaux, sans prétendre montrer une lésion de carence.

Le registre S101–S115 documente les lectures suisses, puis européennes et les sources scientifiques de contexte, avec version, section, population, limites et empreinte. Les résumés historiques réellement relus sont séparés du titre seul sur le sélénium. Le manifest public contient des paraphrases fidèles ; les54fichiers acquis, soit6 773 004octets, restent dans le cache externe `/tmp/medina-source-cache/endocrinologie/E00`. Aucun texte intégral non libre n’est publié dans ce paquet.

## Contrôles

- `betta_verite.py` : réussi avant la rédaction, puis contrôle final enregistré dans `betta-verite-final.log`.
- `audit_sciences.py` : réussi sur la base exacte, six disciplines substantielles et figures accessibles.
- Contrôle statique : références de fenêtres, identifiants, cibles Pareto, image originale et progression de profondeur vérifiés.
- Build natif S05 isolé : réussi. Aperçu autonome : deux occurrences du JPEG original incorporées, SHA inchangé.
- Chromium1440×960 et390×844 : quatre onglets, six sous-onglets, neuf sections de sémiologie, clavier Entrée/Espace, ouvertures/fermetures des fenêtres, cinq quiz, Pareto, Navigo, livre et taille24 réellement appliquée. Aucun débordement du document ; tableau mobile défilable dans son cadre, dernière colonne atteinte. Aucune erreur JavaScript.
- Le document exact est servi en mémoire à une origine interceptée ; toute autre requête est bloquée. Aucun serveur HTTP réel n’a été testé. Le premier essai sur origine opaque avait remis la taille à17 ; il est conservé comme preuve non concluante, puis remplacé par le test correct avec stockage fonctionnel.
- Contrat du harness : réussi ; quatre reçus `self_review`, certification clinique et autorisation de publication main àfalse.

## Réserves conservées

- Le seuil suisse de rappel TSH sur buvard n’a pas été trouvé ; le cours le dit et ne substitue pas un seuil sérique européen.
- La prévalence suisse contemporaine du syndrome E00 n’est pas établie par les sources lues ; la fréquence1/3500 décrit l’hypothyroïdie congénitale, non E00.
- Le catalogue français canonique reste OFS2024. La comparaison BfArM2026 ne constitue pas une validation administrative suisse pour2026 ; aucun code partagé modifié.
- Sélénium : titre seul d’une référence historique, sans résumé obtenu. Aucun mécanisme détaillé ni traitement n’en est déduit.
- Les descriptions historiques sont souvent des résumés ; leurs limites sont explicites. Aucun effet de récupération neurologique tardive ni performance diagnostique n’est inventé.
- Absence de FI suisse de spécialité iodée : aucune dose d’huile iodée présentée comme ordonnance suisse. La couverture surrénalienne du différentiel central reste spécialisée, sans schéma de glucocorticoïde inventé.
- L’auto-relecture IA n’est ni indépendante ni une certification médicale humaine. Aucune note médicale numérique n’est attribuée.
- Rendu Chromium avec origine interceptée et document exact ; aucun serveur HTTP réel, aucune publication de site testée.

Les empreintes des six chapitres, du glossaire et de l’image source sont liées à l’aperçu par [source-binding.json](source-binding.json). La veille peut détecter une modification ultérieure ; elle ne certifie pas le contenu médical. Tokens, coût et note médicale numérique restent `null`. Les scripts de rédaction sont des traces à exécution unique ; seuls les scripts de contrôle sont destinés à être rejoués.
