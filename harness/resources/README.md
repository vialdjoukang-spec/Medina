# Ressources académiques d’imagerie proposées par Vial

Catalogue commun aux quatre auteurs : [imaging_catalog.json](imaging_catalog.json).
Consignation : **2 novembre 2026, 22 h 59 Europe/Zurich** (21 h 59 UTC).
Les dix intitulés et URL viennent de Vial. Cette liste est un index de recherche,
pas une bibliographie de cas lus ni une collection d’images réutilisables.

| Ressource | Accès observé par le connecteur |
|---|---|
| [Radiopaedia](https://radiopaedia.org) | fetch_failed_402 |
| [Radiology Assistant](https://radiologyassistant.nl) | page_text_returned |
| [Ultrasound Cases](https://www.ultrasoundcases.info) | page_text_returned |
| [Learning Radiology](https://www.learningradiology.com) | page_text_returned |
| [Eurorad (ESR)](https://www.eurorad.org) | fetch_failed_403 |
| [Case Stacks](https://casestacks.com) | page_text_returned |
| [Rad At Hand — Radiology Case Bank](https://radathand.com/radiology-case-bank) | page_text_returned |
| [Casimage (Université de Genève)](https://www.casimage.com) | unavailable_via_tool |
| [RadioSurf (Université de Berne)](https://elearning.medizin.unibe.ch) | redirected_minimal_page |
| [Modern Radiology (ESR e-Book)](https://www.myesr.org/undergraduate-education-radiology/ebook-undergraduate-education-radiology) | unavailable_via_tool |

Ces observations concernent la collecte ponctuelle des pages d’entrée. Les
échecs sont ceux du connecteur et ne prouvent pas une indisponibilité générale.
La redirection de RadioSurf vers MedSurf ne confirme pas que le module recherché
soit accessible. L’identité institutionnelle et l’URL actuelle de Casimage
restent à vérifier avant utilisation. Aucun contournement d’accès n’est prévu.

## Consigne de reprise des quatre auteurs

1. Partir du besoin de la leçon : modalité, région, normalité ou signe à expliquer.
   Rechercher dans ce catalogue avant de multiplier les requêtes généralistes.
   Conserver la priorité suisse puis européenne pour les recommandations cliniques ;
   un cas illustratif étranger ne devient pas une recommandation thérapeutique suisse.
2. Ouvrir et lire le **cas exact**, avec sa légende et ses limites. Consigner son URL,
   son auteur, sa date/version, les passages effectivement lus et la date réelle
   de lecture dans la recherche propre à la leçon. Une page d’accueil ne suffit pas.
3. Vérifier les droits de **la figure précise** : auteur, titulaire, licence,
   conditions de redistribution et d’annotation. Un accès gratuit ne vaut pas
   autorisation. Sans droit établi : lien vers le cas, aucune copie injectée.
4. Inspecter visuellement l’image réelle : modalité, plan, latéralité, repères,
   cohérence avec la légende et absence d’identifiants personnels. Ne pas déduire
   de l’image un diagnostic, une mesure ou une temporalité qu’elle ne démontre pas.
5. Conserver le fichier source, son empreinte et l’attribution ; ajouter les
   annotations françaises et les explications cliniques avec un lien explicite
   entre chaque repère et ce qui est réellement visible. Préserver une référence
   à l’original non modifié. Aucune anatomie générée par IA.
6. Contrôler l’aperçu ordinateur/mobile, les crédits et les liens. Les contrôles
   techniques, la self_review, une revue ciblée distincte et la revue de Vial
   restent des états séparés. Ne pas transformer une inspection en validation humaine.

Le cache de recherche et les empreintes existants peuvent éviter de télécharger
deux fois une même figure. Ce catalogue ne mesure ni tokens, ni coûts, ni économie.
Aucun téléchargement de masse, nouveau service ou script autonome n’est lancé.

## Traçabilité et veille

Les pièces cliniques et licences sont enregistrées dans le dossier réservé de
chaque leçon, puis liées à sa version finale par le mécanisme de provenance
existant. Ne jamais renouveler artificiellement activité auteur ou
`source-binding.json` lors d’une vérification de liens.

La veille existante du harness conserve son périmètre ; **elle ne surveille pas
automatiquement la disponibilité de ces dix sites**. Les champs d’accès ci-dessus
sont datés, ponctuels et ne constituent pas des signaux d’activité des auteurs.
Le relais GitHub workflow_dispatch de 600 secondes observe sans réveiller les
agents natifs ; ce document ne modifie pas ce fonctionnement.

Au contrôle natif de cette reprise, seul le parent était présent. Cette consigne
est déposée dans le dossier commun pour reprise : elle n’est pas présentée comme
un message reçu par les trois auteurs absents. Aucune nouvelle leçon, image
injectée ou revue utilisateur n’est attestée par l’ajout de ces ressources.
