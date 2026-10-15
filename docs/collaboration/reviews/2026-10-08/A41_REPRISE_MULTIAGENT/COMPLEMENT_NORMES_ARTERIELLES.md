# Complément de sources — normes artérielles A41

A41 — Sepsis et choc septique de l’adulte (I-03-Infectiologie). Observation ESP-03. Recherche et lecture : `/root/test_allocation`, 2026-10-08T12:35:10.380048+00:00.

Une source primaire suisse publique a été trouvée chez Viollier pour le pH, la PaCO₂ et la PaO₂ artériels. La recherche reste partielle pour le bicarbonate **actuel/calculé** artériel. Les normes sériques du trou anionique ne prouvent pas une équivalence avec un résultat artériel ou un calcul mélangeant des matrices. Cette réserve demeure.

## Résultats réellement obtenus

| Fiche primaire | Matrice explicitement publiée | Intervalle et unité | Limite d’utilisation |
|---|---|---|---|
| [Viollier 14136, pH arteriell](https://www.viollier.ch/de/analysis/14136) | Sang artériel, Li-héparine | 7,35–7,45 ; aucune unité imprimée, pH sans unité | Aucune date éditoriale explicite |
| [Viollier 14146, pCO2 arteriell](https://www.viollier.ch/de/analysis/14146) | Sang artériel, Li-héparine | Femmes 32–45 mmHg ; hommes 35–48 mmHg ; âge imprimé≥0Y | Ne valide pas35–45 universel |
| [Viollier 14156, pO2 arteriell](https://www.viollier.ch/de/analysis/14156) | Sang artériel, Li-héparine | 83–108 mmHg, femmes/hommes | FiO₂, altitude et âge non précisés ; pas cible thérapeutique |
| [Viollier 14157, Standard-Bikarbonat](https://www.viollier.ch/de/analysis/14157) | Sang artériel, Li-héparine | 21–29 mmol/L | **Bicarbonate standard**, pas bicarbonate actuel/calculé démontré |
| [Viollier 10236, Bicarbonat](https://www.viollier.ch/de/analysis/10236) | Sérum centrifugé, tube non ouvert ; enzymatique | 20–31 mmol/L | Comparateur sérique dosé uniquement |
| [Viollier 10245, Anionenlücke](https://www.viollier.ch/de/analysis/10245), [profil 10260](https://www.viollier.ch/de/analysis/10260) | Feuille 10245 sans matrice ; profil 10260 explicitement sérique | 3–11 mmol/L | Ni norme artérielle ni formule/convention publiées dans ces fiches |
| [Medics bic, Bicarbonat](https://www.medics.ch/analysenverzeichnis/bic) | Sérum ou plasma Li-hépariné, non ouverts ; enzymatique Roche | 22–29 mmol/L | Pas calcul de gazométrie |
| [Medics anionl, Anionenlücke](https://www.medics.ch/analysenverzeichnis/anionl) | Sérum/plasma, calculé | 8–16 mmol/L ; formule `Na − Cl − HCO₃` explicitement publiée | Pas démonstration d’équivalence avec artériel ou matrices mélangées |

Ces fiches sont des références de laboratoires différents. Leurs intervalles ne sont pas fusionnés et ne deviennent pas une table universelle. Dans les fiches Viollier, «Kapillare, Li-Heparin» décrit le récipient ; la matrice est explicitement «Blut arteriell».

## Extraits déterminants

Viollier 14157 : «Standard-Bikarbonat» ; «Material Blut arteriell (Hinweis beachten) Kapillare, Li-Heparin» ; «Referenzwerte Wert Sex 21.0 - 29.0 mmol/L f+m». Aucune formule de bicarbonate actuel/calculé ni équivalence entre ce résultat et le bicarbonate du cas n’est publiée dans la fiche.

Viollier 10245 : «Referenzwerte Wert Sex 3 - 11 mmol/L f+m». La feuille seule ne précise pas la matrice. Le profil 10260 donne «Material Serum zentrifugiert und ungeöffnet Serum-Gel-Tube, goldgelb (1)» et liste sodium, chlorure et bicarbonate. Il ne publie pas la formule.

Medics anionl précise : «Die Anionenlücke im Serum/Plasma bezeichnet die Differenz…» puis «Anionenlücke = [Natrium] - [Chlorid] - [Bicarbonat]». La méthode est «Berechnung», la référence «8.0 - 16.0 mmol/L». Le texte décrit une baisse possible en cas d’hypoalbuminémie ou d’hémodilution, sans formule chiffrée de correction. Cette fiche apporte une formule suisse sans potassium et un comparateur **sérique/plasmatique**.

Medics Blutgasanalyse précise que, du fait de la faible stabilité, la gazométrie doit se faire sur place à l’hôpital. Elle ne propose pas de table de normes artérielles.

## Dates et traces

Toutes les fiches citées ont réellement répondu HTTP200 le 8 octobre 2026. Aucune date éditoriale ou version explicite n’a été trouvée dans leur texte ni dans les champs datePublished/dateModified examinés. Il faut donc citer «catalogue public, consulté le 8 octobre 2026, date de version non indiquée», sans attribuer 2026comme année de publication. Les dates d’assets, copyright et en-têtes HTTP ne sont pas des preuves de version.

Les captures originales et extractions sont conservées hors dépôt dans `/workspace/medina-env/a41-normes-arterielles`. Le JSON joint contient les URL exactes, horaires UTC, matrice, unités, citations, tailles et SHA-256. Les valeurs du pH et des gaz proviennent exclusivement des fiches artérielles nommées ; aucun intervalle veineux, sérique ou étranger n’a été assimilé à une norme artérielle.

## Périmètre de recherche et réserve finale

Viollier : catalogue statique complet, profil artériel et analyses individuelles, contrôles veineux et comparateurs sériques. Medics : catalogue et trois recherches ciblées suivies des fiches correspondantes. Labor team : catalogue, inspection de l’appel public GET sans exécution de JavaScript, recherche Blutgas sans résultat et recherche Bicarbonat donnant seulement trois fiches calcium. Unilabs : page de configuration publique ; Risch : HTML de l’application RiBook sans tableau rendu ; Hirslanden : accueil sans fiche atteinte. Ces derniers catalogues n’ont pas été parcourus exhaustivement. Les découvertes Google/Bing ont été inexploitables et aucun extrait de moteur n’a servi de preuve clinique.

Ce périmètre n’établit pas l’inexistence d’une autre table suisse. Il établit les trois plages artérielles trouvées et les distinctions utiles. **ESP-03 reste partielle** pour le bicarbonate actuel/calculé artériel et pour toute équivalence non démontrée du trou anionique du cas. L’auteur review_plan a reçu les passages et limites ; décision de modification sous son ownership et celui de root. Aucun fichier source, canonique ou Git n’a été modifié par cette mission.
