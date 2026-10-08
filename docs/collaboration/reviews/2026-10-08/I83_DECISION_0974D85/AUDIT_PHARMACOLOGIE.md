# Audit de Pharmacologie — I83 — Varices des membres inférieurs (C-01-Cardiologie)

> **État actuel au SHA `20bee19a6329f0a62126e9180bfc909207055e38` : PH-01 résolue** — le correctif de formulation de la tumescence est accepté. **PH-02 ouverte** — l’attribution causale de l’œdème par la seule chronologie reste à corriger. La **source de la procédure d’urgence intra-artérielle reste non contrevérifiée**, sans erreur de dose déclarée prouvée. Aucune injection n’a été effectuée par ce poste. L’addendum final détaille cette décision ; les constats historiques ci-dessous sont conservés comme preuves.

**Constat historique au commit `0974d854db292ae0311e435b3daea5fbed187e25` : corrections nécessaires avant injection.** La recette de tumescence assimile un mélange ESVS à une présentation suisse sans traiter les contraintes de formulation présentes dans les preuves reçues. Une règle d’attribution médicamenteuse de l’œdème est également trop affirmative. La fidélité des extraits à leurs pages officielles et plusieurs prescriptions chiffrées restent impossibles à contrevérifier extérieurement dans cette session : quatre lectures officielles ont été refusées par le proxy. Les anciennes preuves Rapidocain et Aethoxysklerol sont bien présentes et ont été lues ; leur absence n’est pas invoquée. **La contrelecture ultérieure au commit `20bee19` lève PH-01 ; voir l’addendum en fin de rapport.**

## Commit, couverture et méthode

- Contenu reçu et figé : `0974d854db292ae0311e435b3daea5fbed187e25`, branche Claude.
- Main de référence : `ea105ace0046c71492cc6a69ff4c61698ef2ce34`.
- Lecture intégrale des **89 lignes** de `chapters/I83/I83_d.html` et des **67 lignes** de `chapters/I83/I83_pop4.html`, soit les cinq sections de Pharmacologie, les sept fenêtres médicales et leur Pareto. Lecture des preuves documentaires suisses, du relevé de sources D, des corrections et des limites déclarées pertinentes.
- Contrôle EHIT limité aux passages de cohérence et au glossaire, signalé séparément ci-dessous. L’audit complet de Pathologie, Examens et Sciences est effectué par d’autres postes ; ce rapport ne prétend pas couvrir seul le chapitre entier.
- Lecture par `git show` des objets exacts ; aucun script de Claude exécuté, aucun fichier canonique modifié, aucune injection. Aucun build ou test navigateur par ce poste : ces contrôles sont reproduits par les autres auditeurs et le coordinateur.

| Objet lu au SHA reçu | SHA-256 |
| --- | --- |
| `chapters/I83/I83_d.html` | `8f4743ecd4d49746529b5d1ed7a13a5ed2285af33fb14a8795fa8116342244b3` |
| `chapters/I83/I83_pop4.html` | `8b5a5d007ff4d789e15199bc19a658cc8a35b5388afb89f2804c6e521ba904d1` |
| `lots/2026-10-08-I83/preuves/rapidocain_extraits.md` | `262383bd90e0767c846f163b8fe31c67a5bc6f190a07d43d616ce92243bd6308` |
| `lots/2026-10-08-I83/PREUVE_AETHOXYSKLEROL_COMPRESSION.md` | `f4c730fd162b1e117ebb34c8743b127a08f88529870b772320f72ae07bc34be1` |

Les chemins `lots/…` de ce rapport sont relatifs à `livraisons/Livraison Claude/C-01-Cardiologie/`. Les numéros de lignes des HTML désignent le commit reçu, et non une version intégrée sur main.

## Corrections nécessaires

### I83-PH-01 — Compatibilité de la présentation Rapidocain non établie

**Gravité : majeure ; bloque l’approbation de la recette opérationnelle.**

Localisation : `I83_pop4.html:50`, fenêtre `i83-d-tumescence`, « Composition et calcul » ; cohérence avec `I83_d.html:55`, `I83_pop4.html:53–54` et la synthèse `I83_pop4.html:67`.

La fenêtre donne la recette ESVS de 445 mL de cristalloïde + 50 mL de lidocaïne adrénalinée + 5 mL de bicarbonate, puis écrit que le produit « correspond à Rapidocain 10 mg/ml avec épinéphrine 10 µg/ml, en flacon de 20 mL ». Cette correspondance de concentrations est correcte arithmétiquement, mais ne démontre pas une équivalence opérationnelle de la formulation.

Deux éléments déjà remis doivent être confrontés :

1. La **preuve Rapidocain corrigée**, `lots/2026-10-08-I83/preuves/rapidocain_extraits.md:83`, reproduit la ligne **305** de la copie de l’information professionnelle : restriction des solutions multidoses contenant des conservateurs, dont l’interdiction pour les « autres blocages nécessitant plus de 15 ml ».
2. L’ancien extrait archivé sur main, sous `archives/2026-10-08_PR12_D94B11F_I83_MAIN31B_PROOFS/livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83/preuves/rapidocain_extraits.md:26–34`, contient réellement la **composition** de la forme avec épinéphrine : E216/E218, en plus des sulfites. Ses titres avaient mal découpé les sections ; cela ne transforme pas cette composition visible en preuve de posologie. La nouvelle preuve, lignes sources **309–310**, confirme aussi les précautions sulfites/conservateurs et leurs allergies.

**Limite exacte :** la restriction dit « blocages » ; elle ne démontre pas une interdiction universelle de toute infiltration ou de toute tumescence. Ce rapport ne fait pas cette extrapolation. Le défaut établi est l’assimilation pratique à ce flacon, sans exposer la restriction ni vérifier sa compatibilité avec le mélange périveineux de grand volume.

**Correction attendue :** retirer l’équivalence pratique au flacon Rapidocain 20 mL ; conserver la recette ESVS comme description de son référentiel et de son statut hors information professionnelle suisse. Exposer fidèlement les restrictions de formulation et d’excipients, distinguer infiltration/blocage et préciser que la forme effectivement utilisée doit avoir sa compatibilité établie dans le protocole local. Aucune autre marque, présentation ou dose n’est inventée ici. La réserve « hors information professionnelle » déjà présente traite le statut de la dose ; elle ne résout pas à elle seule le choix des excipients.

Références : information professionnelle Rapidocain/avec épinéphrine, Swissmedic **20272/32381**, juillet 2024, ligne source 305, 309–310 ; composition remise et archivée ; ESVS 2022, § 4.1.3, recommandations 19–20.

### I83-PH-02 — Chronologie présentée comme attribution causale de l’œdème

**Gravité : modérée ; correction clinique nécessaire avant publication.**

Localisation : `I83_d.html:82` : l’œdème apparu après introduction ou augmentation d’un médicament « lui est attribué jusqu’à preuve du contraire ».

La chronologie fait suspecter une cause médicamenteuse ; elle n’en apporte pas la preuve et n’exclut pas une cause concomitante cardiaque, rénale, hépatique ou thrombotique. Le chapitre reconnaît lui-même cette coexistence dans son cas clinique et demande, dans la fenêtre des phytothérapies, une consultation rapide devant douleur/gonflement/chaleur d’une jambe. Une instruction d’attribution automatique affaiblit ces précautions.

**Correction attendue :** faire de la chronologie un indice à vérifier avec le contexte, l’examen, les causes concurrentes et l’évolution après adaptation du traitement ; éviter l’attribution par défaut avant cette évaluation. La recherche d’un médicament reste pertinente et aucun arrêt automatique du traitement n’est demandé. Cette correction porte sur la force de l’inférence, sans ajouter de seuil diagnostique non sourcé.

## Prescriptions et preuves : vérifié, ou non vérifiable actuellement

### Polidocanol, concentrations et ancienne contre-indication diabétique

`I83_d.html:38–42` : conversions revérifiées indépendamment. **2 mg/kg × 70 kg = 140 mg ; 3 % = 30 mg/mL**, soit 4,666… mL ; 1 % = 10 mg/mL, soit 14 mL. **4 mL à 0,5 % = 20 mg**, et **4 mL à 3 % = 120 mg**. Le plafond est bien exprimé en masse et non en seul volume. « Environ 4,7 mL » est un arrondi pédagogique ; pour un calcul de plafond administrable, il faut éviter l’arrondi vers le haut.

Les concentrations et petits volumes restent ceux du texte suisse ciblé déjà contrevérifié dans l’audit historique : réticulaires 0,25–0,5 %, petites varices 1 %, moyennes 2–3 %, plafond 2 mg/kg/j. Le présent accès externe n’a pas permis une nouvelle lecture intégrale de la monographie ; aucune extrapolation de la version allemande n’est faite.

**Ancienne I83-MED-01 : corrigée dans le périmètre relu.** `I83_d.html:47,50`, `I83_pop4.html:26–27,67` conservent le diabète comme contre-indication selon les deux informations suisses, reprennent « généralement contre-indiquée » pour Aethoxysklerol et distinguent l’écart avec l’ESVS. Le mécanisme proposé n’est plus présenté comme justification réglementaire démontrée. La correction de rédaction demandée par l’audit historique est réalisée ; cela ne revendique pas un nouvel accès officiel réussi aujourd’hui.

Les limites de mousse sont distinctes du plafond de masse et du liquide : `I83_d.html:42–43` n’applique pas automatiquement la mousse à Aethoxysklerol, et distingue Sclerovein. Les limites volumétriques ESVS et la monographie Sclerovein complète n’ont pas pu être relues extérieurement ici ; leur concordance complète reste **non certifiée**, sans erreur de conversion démontrée.

### Compression Aethoxysklerol : ancienne réserve documentaire corrigée

`I83_pop4.html:24` concorde avec les passages effectivement remis dans `PREUVE_AETHOXYSKLEROL_COMPRESSION.md`, rubrique « Posologie/Mode d’emploi » : varicosités **au moins 2–3 jours**, veines réticulaires/petites varices **5–7 jours ou plus**, varices moyennes/grandes **4–6 semaines ou plus**. La phrase distingue ensuite la durée Sclerovein. La marche d’au moins 30 minutes et la position horizontale/surélevée concordent avec cet extrait. La durée n’est plus inversée entre télangiectasies et veines réticulaires.

**Réserve historique Aethoxysklerol/compression : corrigée par concordance documentaire.** La preuve nécessaire est présente ; pas de demande de la fournir à nouveau. L’authenticité de sa transcription à la page officielle demeure distincte, l’accès externe ayant échoué.

### Rapidocain, dose et toxicité : preuve corrigée réellement exploitée

`I83_d.html:55` et `I83_pop4.html:50–55` : les calculs sont justes. **50 mL × 10 mg/mL = 500 mg** dans 500 mL, soit **1 mg/mL = 0,1 %** ; **50 mL × 10 µg/mL = 500 µg**, soit **1 µg/mL** ; **15 mg/kg × 70 kg = 1 050 mg**, soit 1 050 mL à cette concentration.

La preuve corrigée, blob `5106966c1976119e88615c7e84fad423309a4e82`, contient réellement les données utilisées. Elle ne doit pas être confondue avec le hash `7b24cf1d…` de la copie complète non versionnée. Tableau source **135–143** : infiltration jusqu’à **400 mg** à 5 ou 10 mg/mL ; lignes **303–304/470–472** : doses réduites chez certains patients âgés ou en insuffisance rénale/hépatique ; lignes **307–312** : contre-indications ; **358–363** : effets toxiques additifs et interactions ; **410–416** : surdosage et signes de toxicité.

Les **5/7 mg/kg pédiatriques** de la preuve ne sont pas substitués à la posologie adulte dans le cours. Les **15 mg/kg de tumescence** ne sont pas présentés comme autorisation suisse : le texte oppose explicitement cette littérature au tableau d’infiltration. Ce point documentaire est amélioré et concordant.

**Ancienne réserve sur le délai : corrigée rédactionnellement.** La fenêtre rattache maintenant **20–30 minutes au surdosage décrit par l’information suisse**, mentionne un passage encore retardé en tumescence et ne fixe pas sa surveillance à ce délai. L’extrait source **410** distingue également 1–3 minutes après injection intravasculaire. Aucune durée précise de pic/surveillance propre à la tumescence n’est certifiée par ce rapport. PH-01 sur la formulation reste ouverte.

### Injection intra-artérielle de sclérosant : conduite chiffrée non contrevérifiable

**Gravité potentielle : majeure ; résultat : impossible à vérifier actuellement, sans erreur de dose déclarée prouvée.** Localisations : `I83_d.html:61`, résumé `I83_pop4.html:67`.

Le texte prescrit **5–10 mL de lidocaïne à 1 ou 2 % et 500 UI d’héparine par la même aiguille**, position basse et hospitalisation vasculaire. L’extrait Aethoxysklerol remis concerne la compression, pas cette rubrique d’urgence. Le dossier décrit ses monographies sources, mais les passages d’urgence exacts ne sont pas reproduits dans les deux preuves suisses ciblées lues. Les accès professionnels externes ont échoué. Le calcul de lidocaïne donne 50–200 mg ; ce calcul ne certifie ni la pertinence de la dose d’héparine ni les conditions d’administration.

Pour fermer ce point à fort impact, confronter la procédure au passage exact de la monographie suisse pertinente, en précisant la formulation anesthésique et les conditions de prise en charge ; ne pas transférer automatiquement ici la préparation adrénalinée de tumescence. **Ne pas remplacer 500 UI par une autre dose sur une supposition ou une monographie étrangère.** La situation requiert une prise en charge spécialisée urgente ; le Pareto ne doit pas faire disparaître ses conditions.

## Reste de l’onglet et des fenêtres, entièrement lu

| Ensemble | Résultat de lecture |
| --- | --- |
| Stratégie médicamenteuse (`I83_d.html:5–18`) | Rôle symptomatique et absence de correction du reflux explicités ; limites des essais et non-substitution à compression/intervention présentes. Classes ESVS citées avec recommandations ; nouvelle vérification extérieure du tableau primaire impossible ici. |
| Veinotropes et doses (`I83_d.html:20–34`) | Doses et prises cohérentes entre corps, monographies et Pareto : fraction flavonoïque 500 mg × 2 ou 1 000 mg × 1 ; oxérutines 500 mg × 2 ou 1 000 mg × 1 ; dobésilate 500–2 000 mg/j ; vigne rouge 360–720 mg/j, maximum trois mois. Absence de posologie inventée pour marronnier. Les monographies complètes correspondantes ne sont pas présentes dans les extraits ciblés et n’ont pas été relues extérieurement ; ne pas annoncer une certification réglementaire indépendante de toutes ces doses. |
| Fraction flavonoïque, dobésilate, oxérutines, vigne/marronnier (`I83_pop4.html:1–18,30–46`) | Mécanismes généralement distingués d’hypothèses ; preuves, limites, effets indésirables et grossesse séparés. Dobésilate : arrêt/hémogramme devant fièvre/angine, interférence créatinine et insuffisance rénale correctement conditionnés dans le texte. Effervescent oxérutines : apport K/Na et alternative comprimé exposés. Concordance interne lue ; chiffre et fréquence de chaque essai/monographie non certifiés par une nouvelle lecture primaire. |
| Antithrombotiques et interactions (`I83_d.html:56–67`) | Prophylaxie individualisée, distinction du traitement anticoagulant de fond, risques AINS/anticoagulant et anesthésiques additifs présents. Le renvoi à I80 — Thrombose veineuse profonde et thromboses veineuses (C-01-Cardiologie) ne constitue pas ici une validation indépendante de ses doses. Le délai sclérosant après exérèse chirurgicale n’est pas étendu automatiquement à l’ablation endoveineuse ; la différence de périmètre est indiquée. Point d’urgence ci-dessus non certifié. |
| Médicaments et œdème (`I83_d.html:70–85`) | Mécanisme de l’amlodipine, distinction d’une rétention hydrique, risques pioglitazone/prégabaline/AINS et limites des diurétiques explicités. PH-02 demande de retirer l’attribution causale par défaut. |
| Pentoxifylline/sulodexide (`I83_pop4.html:57–63`) | Limites des essais et rôle adjuvant présents. Disponibilité suisse négative déclarée d’après une liste complète par Claude ; aucune preuve exhaustive de cette liste n’a été relue ici. La pression ≥40 mmHg pour ulcère doit se lire avec les conditions artérielles de la fenêtre compression, et ne dispense pas de l’audit Pathologie. |
| Pareto Pharmacologie (`I83_pop4.html:65–67`) | Doses et correction diabète cohérentes avec corps/fenêtres. Recopie aussi la procédure intra-artérielle non contrevérifiée ; à harmoniser après les corrections. |

**OFSP :** les sept bundles FHIR remis soutiennent les sept inscriptions positives, statut remboursé/listé et quote-part 10 %, selon la contrelecture statique de la sentinelle de réception. Un sous-ensemble sélectionné ne prouve pas l’absence de toutes les autres spécialités ni toutes les autorisations Swissmedic. La publication complète est décrite et empreintée par Claude ; cette session ne l’a pas relue. Les affirmations négatives de disponibilité/remboursement à `I83_d.html:31` et dans la fenêtre pentoxifylline restent donc non certifiées extérieurement, distinctement de la preuve positive effectivement présente.

**Cohérence mineure :** `I83_d.html:75` écrit que l’œdème des chevilles « disparaît » puis évoque sa part persistante à gauche. Préciser que la composante bilatérale attribuée à l’amlodipine s’est résolue ; remarque éditoriale non bloquante.

## EHIT : rapprochement limité, sans remplacer l’autre audit

L’ancienne omission du curatif pour **EHIT III** est corrigée dans `I83_b.html:64`, `I83_pop2.html:47` et le Pareto `I83_pop2.html:123` : curatif + échographie hebdomadaire jusqu’à rétraction/résolution ; IV comme TVP provoquée. Cette correction concorde avec la recommandation AVF/SVS **3.4, grade 1B** déjà lue et documentée dans l’audit historique. L’accès PMC actuel a échoué ; aucune nouvelle lecture complète du référentiel n’est prétendue.

`glossary/i83.py:7` mentionne encore le curatif IV sans rappeler III. Il ne dit pas « seulement IV » et ne nie donc pas la correction du cours. **Harmonisation recommandée, non bloquante à elle seule.** La revue intégrale des autres fichiers et de leurs doses reste du ressort du poste Pathologie/Examens.

## Accès primaire, provenance et critères de clôture

Quatre tentatives indépendantes, TLS conservé, `curl --location --head --max-time 25 --silent --show-error`, le 8 octobre 2026 :

- https://www.swissmedicinfo.ch/ShowText.aspx?textType=FI&lang=FR&authNr=20272
- https://compendium.ch/fr/product/80113-aethoxysklerol-sol-inj-0-25
- https://orbi.uliege.be/handle/2268/288479
- https://pmc.ncbi.nlm.nih.gov/articles/PMC7820569/

Toutes donnent **403 CONNECT du proxy, code curl 56**, avant restitution des documents. Aucun contournement ni désactivation de vérification ; aucune répétition sans changement de configuration. Cela ne prouve pas que les publications manquent ou sont fausses. La contrelecture du contenu des extraits reçus est réalisée ; leur authenticité extérieure ne peut pas être nouvellement attestée dans cette session. La redirection Swissmedicinfo annoncée par Claude vers `swissmedicinfo-pro.ch` n’a pas été atteinte par cette tentative.

**Pour la décision suivante :** corriger PH-01 et PH-02 et leurs résumés, confronter la procédure intra-artérielle à sa section primaire exacte lorsque l’accès est disponible, conserver les preuves déjà reçues et préciser celles effectivement vérifiées. Refaire la contrelecture des passages modifiés au SHA final ; compléter avec les audits Pathologie/Examens/Sciences et les contrôles techniques indépendants. Une réussite build/navigateur ne résout pas les conditions de prescription.

**Statut final de ce poste : Pharmacologie entièrement lue ; anciennes corrections documentaires identifiées ; nouvelles corrections nécessaires et limites primaires explicites ; aucune injection ni certification de l’ensemble de I83 — Varices des membres inférieurs (C-01-Cardiologie).**

## Addendum — contrelecture du correctif au SHA `20bee19`

Nouvelle remise figée : `20bee19a6329f0a62126e9180bfc909207055e38`. Delta vérifié depuis `0974d854db292ae0311e435b3daea5fbed187e25` : une seule ligne de cours change, **`I83_pop4.html:50`**, dans la fenêtre `i83-d-tumescence`. Le rapport et deux journaux/contrôles du producteur changent également. La contrelecture porte sur ce delta et sur les passages de cohérence ; elle ne répète pas un audit exhaustif des contenus identiques.

**PH-01 : résolue dans le périmètre de la correction demandée.** La nouvelle ligne :

- identifie le flacon 20 mL comme multidose et nomme ses parahydroxybenzoates ;
- cite la restriction pour les **blocages >15 mL** et les allergies concernées ;
- retire l’équivalence directe du flacon à la recette ESVS nécessitant 50 mL ;
- rappelle que la tumescence n’est pas une indication décrite dans cette information et renvoie à une préparation sans conservateurs selon le protocole de pharmacie hospitalière.

Ces modifications traitent l’omission démontrée. **Aucune nouvelle interdiction générale d’infiltration n’est déduite du mot « blocage »** ; aucune réserve n’est maintenue arbitrairement sur cette différence de vocabulaire. Le correctif ne prétend plus que la correspondance de concentrations prouve la compatibilité de cette présentation. Les calculs de la recette et la distinction de dose/statut restent corrects dans la portée déjà décrite. L’accès officiel extérieur demeure limité comme indiqué ci-dessus ; lever cette réserve de rédaction ne certifie pas une préparation locale précise.

| Objet | État au nouveau SHA |
| --- | --- |
| `chapters/I83/I83_pop4.html` | Nouveau blob `685d2f9a869c4d11b2e69ec039fe77904eddbfda` ; SHA-256 `79ca90654e97fe00619ed3d76ad1847734b41c8f9019af32146b47d18f3d58d9`. |
| `chapters/I83/I83_d.html` | Blob inchangé `32a8094bfc9c052490a31f9fe0391163f75f41be`. |
| `lots/2026-10-08-I83/preuves/rapidocain_extraits.md` | Blob inchangé `5106966c1976119e88615c7e84fad423309a4e82`, preuve corrigée déjà reçue et lue. |

**PH-02 : reste inchangée** à `I83_d.html:82` ; la causalité par chronologie doit rester une hypothèse à vérifier, pas une attribution par défaut. La réserve sur la procédure intra-artérielle chiffrée reste un point de contrevérification primaire non réalisable actuellement ; ce rapport ne la transforme pas en erreur de dose prouvée. L’harmonisation EHIT du glossaire reste non bloquante à elle seule.

**Décision mise à jour : correctif de formulation tumescence accepté ; autres observations et limites explicitement conservées pour la décision coordonnée du chapitre.** Aucun canonique modifié par ce poste, aucune injection, aucun contrôle producteur exécuté ou présenté comme contrôle indépendant.
