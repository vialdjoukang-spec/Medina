# Audit linguistique G83 — Autres syndromes paralytiques (S08)

Mission ALPHA1-CLAUDE-G83-LANG, tour 1, génération 1. Branche `claude/alpha1/g83-lang-g1`, base `103745ba` (le manifeste cite la base `523832d9` ; les sept fichiers sont identiques entre les deux commits, empreintes conformes). Audit IA : revue distincte d'une validation médicale humaine ; aucune source canonique modifiée.

## Synthèse

Les sept fichiers de la leçon (quatre onglets, deux fenêtres, glossaire) ont été lus en entier ; leurs empreintes SHA-256 sont conformes au manifeste. Le français est globalement correct et sobre ; les défauts relevés sont de quatre ordres : (1) des **phrases nominales et des infinitifs injonctifs** dans les encadrés « À retenir », les pièges et l'alerte « À ne pas faire », que le guide de rédaction proscrit ; (2) des **répétitions fautives** (« racines 2e à 5e racines sacrées », « rapports de cotes rapportés », « revue… revue ») ; (3) des **calques de l'anglais** (« elle manque les patients », « ne réalise pas le tableau », « locked-in like », « gold standard ») ; (4) des **ambiguïtés** (« le second », « la sensibilité du périnée » dans un cours de sensibilités diagnostiques, « scanner vésical » à côté du scanner tomodensitométrique, « dépasse le seuil de 150 mL »).

- **83 propositions locales** (`propositions.json`), chacune avec un `ancien` unique dans son fichier, `fond_inchange: true`, sans chevauchement ; application simulée en mémoire : multiensembles de balises identiques, `build_medina.audit()` renvoie `{}` sur les six fichiers HTML, le glossaire modifié compile.
- **20 renvois médicaux** : formulations dont la correction créerait, retirerait ou préciserait une causalité, un effectif, une portée ou une source. Ils ne sont pas corrigés ici.
- **Choix différés, non appliqués** : espaces insécables globales (aucun U+00A0 ni U+202F dans les sept fichiers) ; découpage des phrases de plus de 40 mots ; correspondance des lettres « Réponse A/B » des cas cliniques avec les boutons.

## Propositions par catégorie

| Catégorie | Nombre |
|---|---|
| syntaxe | 32 |
| registre | 19 |
| répétition | 10 |
| cohérence | 7 |
| ambiguïté | 7 |
| grammaire | 6 |
| ponctuation | 2 |

## Propositions par fichier

| Fichier | Nombre |
|---|---|
| `chapters/G83/G83_a.html` | 22 |
| `chapters/G83/G83_b.html` | 28 |
| `chapters/G83/G83_c.html` | 14 |
| `chapters/G83/G83_d.html` | 6 |
| `chapters/G83/G83_pop1.html` | 8 |
| `chapters/G83/G83_pop2.html` | 3 |
| `glossary/g83.py` | 2 |

## Renvois médicaux (hors correction linguistique)

Chaque renvoi cite l'extrait exact de la leçon. Les trois plus lourds pour le fond : R-10 (effectifs de la série de 1986 dont les sommes ne correspondent pas à 139), R-02 (« a provoqué » pour deux cas publiés que la fenêtre associée dit ne pas démontrer un mécanisme) et R-16 (encadré « au plus tard dans les 48 heures » contre piège « en général dans les 24 heures »).

- **R-01** (ambiguïté de sens, `G83_a.html`) : « dont l’examen peut s’inspirer ». « Deux causes iatrogènes dont l’examen peut s’inspirer » : le sens de « s’inspirer » est indéterminable (l’examen clinique doit-il rechercher ces causes ? l’anamnèse doit-elle les relever ? comme le dit la phrase suivante). Toute reformulation suppose de trancher l’intention médicale.
- **R-02** (causalité, `G83_a.html`) : « a provoqué un syndrome de la queue de cheval avec arachnoïdite ». « A provoqué » affirme un lien causal pour deux cas publiés, alors que la fenêtre g83-iatrogene précise que ces cas isolés « ne démontrent pas un mécanisme ». Remplacer par « a précédé » ou « a été suivie de » modifie la force de l’affirmation : à trancher par l’audit médical.
- **R-03** (ambiguïté de référence et de fond, `G83_a.html`) : « ne sont pas deux maladies, mais deux moments d’une même évolution ; elle a une valeur pronostique ». Le pronom « elle » peut reprendre la classification de Gleave et MacFarlane ou l’évolution ; l’énoncé « deux moments d’une même évolution » (le CESR succède-t-il toujours au CESI ?) n’est étayé par aucune fenêtre. Corriger la référence revient à choisir le sens : renvoi.
- **R-04** (portée de la mention géographique, `G83_a.html`) : « En Suisse, la prévalence est évaluée à environ 0,04 % parmi les patients qui consultent pour une lombalgie,… ». Le complément « En Suisse » porte-t-il sur les deux chiffres ? La fenêtre g83-incidence attribue 0,04 % à la Revue Médicale Suisse 2010 et 2 % à Kögl 2024 (source allemande). Séparer les deux propositions revient à décider de la portée géographique : à confirmer par l’audit médical.
- **R-05** (recommandation non sourcée, `G83_a.html`) : « <td>Guider par imagerie</td> ». Infinitif injonctif qui énonce une recommandation (guider les injections par imagerie) ; la leçon ne rapporte que des cas où l’injection n’était pas guidée. Reformuler en phrase complète exige de décider si c’est une recommandation, un constat ou une hypothèse.
- **R-06** (ambiguïté de sens, `G83_a.html`) : « Rapporter la complication au geste (cas publiés) ». « Rapporter la complication au geste » peut signifier la rattacher causalement au geste ou la déclarer. Le sens retenu détermine la reformulation : à trancher par l’audit médical.
- **R-07** (exactitude terminologique, `G83_a.html`) : « c’est la coquille du texte source, conservée ici telle quelle ». La graphie « déefférentation » (G83.5) est présentée comme une coquille. Le terme « déefférentation » (privation d’efférences) est régulièrement formé et employé dans la littérature neurologique française pour le locked-in syndrome. La qualification de « coquille » est donc à vérifier contre le libellé de l’OFS ; aucune correction linguistique n’est proposée sans cette vérification.
- **R-08** (cohérence interne, `G83_pop1.html`) : « ou si elle est ancienne, de longue date et de cause non précisée ». La fenêtre énumère trois attributs (« ancienne, de longue date et de cause non précisée ») alors que G83_a, G83_b et G83_pop2 n’en citent que deux (« ancienne et de cause non précisée »). « Ancienne » et « de longue date » sont redondants en français, mais la note de la source (BfArM) peut en comporter trois : supprimer l’un risquerait de retirer une information sourcée.
- **R-09** (généralisation, `G83_b.html`) : « Le retard est d’abord médical ». Généralisation à partir d’une série de 24 patients opérés après 48 heures (imputable au médecin dans 20 cas) : « d’abord médical » fait d’une répartition observée une règle. À nuancer ou sourcer par l’audit médical.
- **R-10** (cohérence numérique, `G83_b.html`) : « 85 hommes pour 52 femmes ». 85 + 52 = 137 patients pour une série de 139 ; 89 + 46 + 3 = 138 formes pour 139 cas. Les effectifs peuvent tenir à des données manquantes dans la source de 1986, mais la leçon ne le dit pas. Vérification dans la source nécessaire ; non corrigé ici.
- **R-11** (référence du pronom, `G83_b.html`) : « peut les précéder ». Dans « Un pontine warning syndrome peut les précéder », « les » reprend « l’infarctus et l’hémorragie » ; or la fenêtre g83-warning ne rattache le syndrome d’alerte qu’à l’infarctus basilaire. Corriger revient à restreindre une affirmation médicale.
- **R-12** (causalité, `G83_b.html`) : « elle améliore le devenir fonctionnel et réduit la mortalité ». Double effet de la réadaptation précoce (devenir fonctionnel, mortalité) affirmé sans source ni nuance dans la phrase ni dans les fenêtres associées (g83-communication ne traite pas de réadaptation). À sourcer ou nuancer.
- **R-13** (fréquence, `G83_b.html`) : « La spasticité justifie souvent le ». « Justifie souvent le baclofène intrathécal » contredit la restriction de G83_d (spasticité chronique grave, réfractaire aux antispastiques oraux) : l’indication est étroite. À nuancer par l’audit médical.
- **R-14** (généralisation, `G83_b.html`) : « Les soignants sous-estiment le bien-être ». Généralisation à tous les soignants à partir d’un pourcentage (9 %) d’une enquête européenne. À nuancer.
- **R-15** (causalité, `G83_b.html`) : « comme le montrent les deux cas suisses cités plus haut, qui gardaient des séquelles à deux ans ». Deux cas isolés « montrent » la nécessité du bilan neuro-urologique ; ils illustrent des séquelles persistantes, ils ne démontrent pas l’intérêt du bilan. À reformuler par l’audit médical (comparer G83_c, e-4 : « illustre l’intérêt d’un suivi organisé »).
- **R-16** (cohérence de fond, `G83_b.html`) : « Décompression urgente, au plus tard dans les 48 heures ». L’encadré fixe « au plus tard dans les 48 heures », alors que le piège de la même section écrit que « le seuil est un repère statistique, non une permission » et que la décompression est urgente « en général dans les 24 heures ». La proposition syntaxique ne tranche pas ce qui reste une tension de fond.
- **R-17** (attribution de source, `G83_c.html`) : « série suisse (8 cas sur 24 patients opérés après 48 heures) ». La série de 24 patients opérés après 48 heures n’est pas qualifiée de suisse dans G83_b ni dans les fenêtres (revue de 2025, JBJS Reviews). L’adjectif « suisse » est à vérifier ou à retirer.
- **R-18** (non-séquitur, `G83_c.html`) : « la récupération distale est plus probable que la proximale ». Dans l’encadré « Science → traitement » consacré à la reperfusion basilaire, l’énoncé sur la récupération distale ne découle pas du traitement et provient de la fenêtre g83-communication (enquête). Le lien avec la reperfusion est à justifier ou à retirer.
- **R-19** (renvoi à une autre leçon, `G83_c.html`) : « le cours renvoie au dossier de la leçon G82 ». La leçon renvoie à G82 pour les modalités du bilan neuro-urologique ; le contenu de G82 n’est pas dans le périmètre de cet audit et le renvoi n’est pas vérifiable ici.
- **R-20** (cohérence numérique, `G83_d.html`) : « Test de 25 à 50 µg, paliers de 25 µg à au moins 24 heures ». L’encadré « À retenir » de cette leçon et le paragraphe des paramètres clés (section 13 de G83_b : « test de 25 à 50 µg ») évoquent une plage, alors que le tableau p-2 et la fenêtre g83-test-baclofene écrivent « 25 ou 50 µg » (deux doses initiales possibles). La plage laisse entendre que toute dose intermédiaire est possible : à harmoniser par l’audit médical, avec l’information professionnelle.

## Tableau de bord

| Élément | Valeur |
|---|---|
| Fichiers lus en entier | 7 / 7 |
| Empreintes conformes au manifeste | oui |
| Propositions | 83 |
| Renvois médicaux | 20 |
| Unicité de tous les `ancien` | oui |
| Chevauchements | aucun |
| Balises HTML après application | identiques |
| Abréviations non couvertes après application | aucune |

## Lacunes

- Libellés officiels de l’OFS et note d’usage du BfArM non relus dans cet audit (périmètre linguistique) : la graphie « déefférentation » et la triple formule « ancienne, de longue date et de cause non précisée » sont donc seulement signalées (R-07, R-08).
- Les sources médicales citées n’ont pas été relues : aucune affirmation de fond n’a été vérifiée ni modifiée.
- Aucun rendu navigateur des propositions n’a été effectué : la vérification est textuelle (unicité, balises, abréviations).

Mention : Audit IA — revue distincte d'une validation médicale humaine ; aucune source canonique modifiée.
