N17 — Complément sur la provenance des figures

L’inventaire relève **12 figures médicales : 8 SVG et 4 images cliniques**, ainsi que 4 icônes de navigation. L’instruction de Vial transmise au coordinateur rend non recevables les structures anatomiques dessinées par IA.

**Deux constats MAJEURS sont ajoutés : figure 4, néphron et territoires ; figure 5, structure tubulaire normale et lésée.** Ces figures demandent un remplacement par un original publié, sourcé et réutilisable. Aucune recherche d’image, requête vers un site de figures, création de remplacement ni modification canonique n’a été effectuée. Les copies proposées dans la première livraison contiennent encore ces figures : elles restent des propositions avec réserves et ne sont pas recevables comme version finale sur ce point.

| Figure | Type et origine documentaire | Statut sous la nouvelle instruction | Lecture / vue |
|---|---|---|---|
| 1 — Conditions de fonction rénale | SVG causal : perfusion, lésion, obstacle et conséquences | Hors interdiction anatomique ciblée | Code et textes lus ; rendu non vu |
| 2 — Séquence clinique | SVG d’algorithme de décision | Hors interdiction anatomique ciblée | Code et textes lus ; rendu non vu |
| 3 — Formes ECG | Courbes SVG synthétiques, d’après UKKA ; aucun tracé de patient prétendu | Hors interdiction anatomique ciblée ; limites de calibration conservées | Code et textes lus ; rendu non vu |
| 3 bis — ECG clinique | JPEG attribué à Agbayani et Gonzales, Commons, CC BY 4.0 déclarée | Pas de rejet pour anatomie IA démontré ; droits selon provenance locale | JPEG vu pendant l’audit initial ; métadonnées lues |
| 4 — Néphron et territoires | Dessin anatomique SVG original local, d’après StatPearls | **MAJEUR : non recevable ; original sourcé requis** | Code, géométrie et légende lus ; rendu non vu |
| 5 — Tubule normal et lésé | Dessin de microstructure/histologie SVG local, d’après Gaut et Liapis 2021 | **MAJEUR : non recevable ; original sourcé requis** | Code, géométrie et légende lus ; rendu non vu |
| 5 bis — Biopsie clinique | JPEG de l’article BMC Nephrology 2018, DOI 10.1186/s12882-018-1121-0, CC BY 4.0 | Pas de rejet pour anatomie IA démontré ; limites médicales M05 maintenues | JPEG et texte original vus/lus pendant l’audit initial |
| 6 — Créatinine hors équilibre | SVG causal qualitatif en boîtes textuelles | Hors interdiction anatomique ciblée | Code et textes lus ; rendu non vu |
| 7 — Transport distal | SVG compartimental : urine, cellule, sang, canaux et pompe | **Réserve** : schéma causal simplifié, pas anatomie authentique. Si l’interdiction vise toute cellule dessinée, un remplacement est également requis ; aucune recevabilité anatomique prononcée | Code et textes lus ; rendu non vu |
| 8 — Effets des traitements | SVG causal en boîtes textuelles | Hors interdiction anatomique ciblée | Code et textes lus ; rendu non vu |
| 9 — Cylindres urinaires | Microphotographies JPEG attribuées à Mohsenin 2017, CC BY 4.0 déclarée | Pas de rejet pour anatomie IA démontré ; droits selon provenance locale | JPEG vu pendant l’audit initial ; métadonnées lues |
| 10 — Hydronéphrose | Échographie JPEG attribuée à Cerevisae, CC BY-SA 4.0 déclarée | Imagerie clinique anatomique attribuée ; pas dessin IA démontré | JPEG vu pendant l’audit initial ; métadonnées lues |

La provenance IA des SVG est **documentaire** : ils sont présents à l’identique, octet pour octet, dans la livraison Codex de l’auteur `C01-R-NEPH`. Le fichier `revue_auteur.json` désigne le runtime `/root/c01_r_neph_resume` et `provenance_finale.json` indique une production originale par un auteur unique. Le reçu de remise conservé dans le dépôt rattache cette livraison au coordinateur Codex. Cette chaîne permet d’attribuer la production locale des SVG à l’auteur IA déclaré ; elle ne prouve pas l’emploi d’un générateur d’images, n’authentifie pas une personne et ne constitue pas un journal de génération trait par trait. Les empreintes et chemins exacts figurent dans `inventaire-figures.json`.

Les mentions « d’après StatPearls » ou « d’après Gaut et Liapis » fournissent une référence de contenu ; elles n’identifient pas un original iconographique publié ni ses droits. Aucune licence propre aux SVG n’a été identifiée. Les quatre images cliniques ont des sources et licences dans `assets/img/cycle1/n17/ATTRIBUTIONS.json`, lu sans modification ; leurs empreintes sont conformes. Les pages de droits n’ont pas été rouvertes pour ce complément. L’absence de génération IA démontrée n’est pas une expertise forensique certifiant l’histoire complète de chaque image.

Les quatre petits SVG de la barre des sciences sont des cercles avec une croix : ils relèvent de l’interface, sans structure anatomique ni valeur clinique. Leur code a été lu ; aucun rendu nouveau n’est déclaré vu. L’« Anatomie » du libellé d’un bouton ne transforme pas son icône en planche anatomique.
