# Audit linguistique G98 — Autres affections du système nerveux, non classées ailleurs : l’arthropathie de Charcot (S08)

Mission ALPHA1-CLAUDE-G98-LANG, tour 1, génération 1. Branche `claude/alpha1/g98-lang-g1`, base de la mission `523832d9` (sources figées ; empreintes SHA-256 des sept fichiers conformes au manifeste). Audit IA : revue distincte d’une validation médicale humaine ; aucune source canonique modifiée.

## Synthèse

Les sept fichiers de la leçon (quatre onglets, deux fenêtres, glossaire) ont été lus en entier. Le français est globalement correct : un contrôle orthographique automatisé ne trouve aucune faute, et le glossaire est exact. Les défauts tiennent à quatre familles :

- des **mentions de la fabrication du cours** dans le texte (« le cours ne les invente pas », « de mémoire », « ce dossier », « la fenêtre précédente »), que `STYLE_REDACTION` § 3 proscrit : quatorze occurrences réécrites sans retirer la limite de source qu’elles signalent ;
- des **phrases nominales et énumérations de mots-clés**, surtout dans les fenêtres, que `STYLE_REDACTION` § 2 interdit : seize réécritures qui conservent chaque élément et leur ordre ;
- des **constructions fautives** : « chez une neuropathie diabétique », « Coder G98† un Charcot », « jusqu’à 3 à 5 semaines », « Eichenholtz … elle ignore », coordination d’un infinitif et d’un nom (« de traiter … et une prophylaxie ») ;
- des **incohérences terminologiques** : G99 dit « bloc voisin » alors qu’il appartient au même bloc que G98, « cellulite » (faux ami) à côté de « dermo-hypodermite », « guérison » contre « rémission », « sérielle » contre « sériée », « inamovible » contre « non amovible », numérotation des cas pédagogiques hors séquence (1, 2, 3, 5, 6, 4).

- **95 propositions locales** (`propositions.json`), chacune avec un `ancien` unique dans son fichier, `fond_inchange: true`, sans chevauchement ; application simulée en mémoire : suite des balises HTML inchangée et `build_medina.audit()` renvoie `{}` sur les six fichiers.
- **21 renvois médicaux** : formulations où une correction fixerait un fait (provenance d’une série, chiffre, seuil, définition, conduite). Ils ne sont pas corrigés ici.
- **6 choix différés** (espaces insécables globales, `ml/min`, infinitifs des encadrés « Piège », listes Pareto, `inamovible`, cellulite/PET) et **1 constat hors périmètre** (libellés « Îlot » du pager, générés par le moteur).

## Propositions par catégorie

| Catégorie | Nombre |
|---|---|
| registre | 30 |
| syntaxe | 28 |
| cohérence | 16 |
| répétition | 6 |
| ambiguité | 5 |
| grammaire | 5 |
| ponctuation | 3 |
| conjugaison | 2 |

| Fichier | Propositions |
|---|---|
| G98_a.html | 23 |
| G98_b.html | 25 |
| G98_c.html | 11 |
| G98_d.html | 12 |
| G98_pop1.html | 17 |
| G98_pop2.html | 7 |

## Les constats les plus graves

1. **Provenance de la série de 71 cas (R-01).** La même série est « documentée en Suisse », « suisse-allemande » et « de la Swiss Medical Weekly (clinique de Düsseldorf) » selon les sections. Düsseldorf n’est pas en Suisse. Fait de provenance, à trancher à la source par l’audit médical.
2. **Classement de A52.1 (R-04).** La section 1 dit que A52.1 « exclut expressément l’arthropathie de Charcot (G98†, M14.6-*) » tout en codant le Charcot tabétique A52.1† dans son tableau ; la conclusion « les deux codes ne se recouvrent donc pas » ne lève pas l’ambiguïté. À trancher à la source (BfArM, OFS). Le glossaire développe en outre SAI en « sans autre indication » alors que le texte écrit « sans autre précision » (R-03).
3. **Renvoi interne faux et faute de construction.** « L’avant-dernière ligne rappelle que la démarche … concerne la CNO à peau intacte » vise en réalité la ligne « Plaie présente » (P-42) ; le cas pédagogique 2 écrit « chez une neuropathie diabétique » (faute de construction, P-54).

## Renvois médicaux (hors correction linguistique)

- **R-01** (provenance/chronologie, `G98_a.html`) : « Le risque de l’oublier est documenté en Suisse ». La série de 71 cas est présentée comme « documenté[e] en Suisse » (section 0), « suisse-allemande » (sections 8, 10, e-5, Pareto) et « de la Swiss Medical Weekly (clinique de Düsseldorf) » (section 4). Düsseldorf n’est pas en Suisse et « suisse-allemande » désigne ambiguëment une origine alémanique ; la revue est suisse, la série ne l’est vraisemblablement pas. Toute reformulation fixe un fait de provenance : à trancher par l’audit médical (Chantelau et Richter, Swiss Med Wkly 2013).
- **R-02** (chronologie, `G98_a.html`) : « avaient retardé l’adressage à cinq mois ». « Retarder l’adressage à cinq mois » est ambigu : retard de cinq mois, ou adressage tardif au cinquième mois de l’évolution. La formule se répète (sections 0, 8, e-3, e-5, Pareto Examens). Seule la source primaire tranche ; la reformulation est un choix de fond.
- **R-03** (terminologie, `G98_a.html`) : « l’« affection du système nerveux sans autre précision » (SAI) ». Le libellé cité est « sans autre précision », l’abréviation SAI est développée dans le glossaire en « Sans autre indication » (g98.py). Les deux ne coïncident pas ; seul le libellé officiel de l’OFS 2024 permet de choisir entre « précision » et « indication » (et de corriger le texte ou le glossaire).
- **R-04** (classification, `G98_a.html`) : « exclut expressément l’arthropathie de Charcot (G98†, M14.6-*) ». La phrase dit que A52.1 inclut l’arthropathie syphilitique (tabétique) et exclut « l’arthropathie de Charcot », alors que le tableau de la même section code le Charcot tabétique A52.1† + M14.6-*. « Arthropathie de Charcot » désigne dans l’exclusion le Charcot non syphilitique, mais le texte ne le dit pas ; la conclusion « les deux codes ne se recouvrent donc pas » reste obscure. Fait de classification : à trancher à la source (BfArM, OFS).
- **R-05** (ambiguïté de fond, `G98_a.html`) : « la récidive 13,6 % ». « La récidive 13,6 % » n’indique pas ce qui récidive (ulcère, Charcot, déformation). La phrase suivante parle de « récidive d’ulcère » pour le diabète ; l’identification relève de la source (Gratwohl et al. 2022).
- **R-06** (définition, `G98_a.html`) : « c’est-à-dire une baisse de la sensibilité douloureuse et de la proprioception ». « C’est-à-dire » pose l’équivalence entre polyneuropathie et perte de deux modalités sensitives ; une polyneuropathie ne s’y réduit pas. Une reformulation (« qui se traduit par ») change la portée de la définition : à décider par l’audit médical.
- **R-07** (métaphore/terme, `G98_a.html`) : « des ostéoclastes très agressifs sont recrutés ». « Agressifs » est une métaphore qui revient dans la section 5, la biologie osseuse, les fenêtres et le Pareto. Le terme technique (hyperactifs, suractivés) n’est pas synonyme : choisir exige de relire la source (Rosskopf et al. 2019).
- **R-08** (unité, `G98_b.html`) : « (4 °F) est utilisée comme seuil d’activité ». L’équivalent en degrés Fahrenheit n’a pas d’usage en Suisse et n’est pas une unité SI ; de plus 2 °C d’écart correspondent à 3,6 °F, non à 4 °F (arrondi dans la source ?). Retirer ou corriger la valeur revient à modifier un chiffre : décision médicale. Même formulation dans la fenêtre g98-thermometrie.
- **R-09** (logique de l’énoncé, `G98_b.html`) : « CRP souvent normale ou élevée sans spécificité ». « Souvent normale ou élevée » couvre toutes les valeurs possibles et ne dit rien ; la source n’a pas été relue dans cet audit linguistique et l’énoncé reste tautologique tel quel. Même énoncé dans e-1 et e-4 (« souvent normaux ou élevés »). À reprendre à la source.
- **R-10** (ambiguïté de fond, `G98_b.html`) : « Il n’y a pas de fixation interne en cas d’infection ou d’ulcère, et pas de chirurgie en l’absence d’ulcération et d’instabilité. ». « Il n’y a pas de » peut vouloir dire « il ne faut pas » (contre-indication) ou « il n’existe pas d’indication ». La seconde proposition, « en l’absence d’ulcération et d’instabilité », signifie-t-elle l’absence des deux ou de l’une ? Les deux lectures ont des conséquences cliniques différentes : renvoi à l’audit médical.
- **R-11** (omission, `G98_b.html`) : « le Charcot non diabétique (prise en charge spécifique) ». La parenthèse suggère qu’une prise en charge spécifique existe, alors que la phrase conclut que les sources ne donnent aucune conduite. Reformuler (« dont la prise en charge peut être spécifique », ou retrait de la parenthèse) revient à trancher un fait.
- **R-12** (généralisation, `G98_c.html`) : « Pourquoi la CNO prend-elle toujours le même visage ? ». « Toujours » et « le même visage » sont imagés et absolus ; la section 3 décrit cinq zones anatomiques, quatre classes de Chantelau et plusieurs stades. La question fait une prémisse non sourcée ; la reformuler fixe une proposition de fond.
- **R-13** (stade/grade, `G98_c.html`) : « Cette lecture a une portée pronostique ». La phrase passe du « grade 0 / grade 1 » de l’IRM (Chantelau et Grützner 2014) aux chiffres 69 % et 7 % « au stade 0 / stade 1 » de la série de 2013, qui n’est pas fondée sur ce grade. Le lien « cette lecture » → 69 %/7 % peut être un amalgame de deux classifications ; à vérifier aux sources.
- **R-14** (cohérence interne, `G98_b.html`) : « Le document suisse concorde : les données sont insuffisantes ». La section 11 écrit que le document suisse « concorde » avec une recommandation forte de ne pas utiliser les antirésorptifs ; la section p-1 écrit qu’il « ne contredit pas » mais « nuance la force ». Deux caractérisations différentes de la même relation ; l’accord ou la nuance relève de la source.
- **R-15** (causalité, `G98_a.html`) : « Cet écart chiffre ce que coûte une radiographie normale prise pour une preuve d’absence de maladie. ». L’écart 69 %/7 % compare des patients selon le stade à la prise en charge ; il n’isole pas l’effet d’une radiographie normale mal interprétée. Le « coût » est une inférence de l’auteur. À sourcer ou à retirer par l’audit médical.
- **R-16** (cohérence interne, `G98_c.html`) : « La thermométrie sérielle des deux pieds sert au suivi, non au diagnostic initial. ». Contredit la section 7 (la thermométrie y fournit le seuil d’activité qui oriente le diagnostic) et la fenêtre g98-thermometrie (« recommandations conditionnelles, de faible certitude, pour le diagnostic et le suivi »). L’énoncé dépend de ce que l’IWGDF recommande réellement : fond.
- **R-17** (seuil, `G98_b.html`) : « la température dépasse de plus de 2 °C celle du pied sain ». Le seuil est dit « supérieur à 2 °C » (section 7), « de 2 °C » (même section et fenêtre), « ≥ 2 °C » (paramètres clés), « inférieure à 2 °C » pour le pied chronique. Inclusif ou exclusif ? Un chiffre ne se corrige pas par l’audit linguistique.
- **R-18** (logique de l’énoncé, `G98_a.html`) : « Le pronostic dépend de l’évolution des lésions cutanées. ». La phrase ouvre un paragraphe qui commence par la mortalité à cinq ans (29 %), l’amputation et la survie, sans lien établi avec les « lésions cutanées ». Soit la phrase résume un propos de la source, soit elle doit être reliée ou retirée ; fond.
- **R-19** (terminologie anatomique, `G98_b.html`) : « un dispositif sur mesure monté sous le genou est recommandé ». « Monté sous le genou » est ambigu (jusqu’au genou ? en dessous du genou ?) et contraste avec « jusqu’au genou » pour la décharge. À préciser d’après le consensus IWGDF.
- **R-20** (chiffre répété, `G98_b.html`) : « la guérison clinique précédait la guérison à l’IRM de 3 à 6 mois chez 23 % des patients ». Le chiffre 23 % revient pour la réactivation (« environ 23 % des patients, en moyenne à 27 mois ») avec un autre dénominateur. Coïncidence ou erreur de report : à vérifier dans Rosskopf et al. 2019 ; le linguistique ne peut ni corriger ni confirmer.
- **R-21** (conduite non sourcée, `G98_d.html`) : « justifie une discussion avec le prescripteur ». « Justifie une discussion avec le prescripteur » est une conduite, immédiatement suivie de « les sources lues ne donnent pas de conduite pour ce cas ». Contradiction à lever par l’audit médical (retirer la conduite ou la sourcer).

## Constat hors périmètre

- **H-01** : les libellés « Îlot précédent / Îlot suivant » du pager sont générés par le gabarit des onglets ; ils ne se corrigent pas dans les sept fichiers.

## Choix différés

- **D-01 — Espaces insécables.** Aucun U+00A0 ni U+202F dans les sept fichiers. Devraient en recevoir : environ 193 « : », 187 « ; », 21 « ? », 19 paires de guillemets « », 57 « % », 14 « °C » (hors textes de liens) et les milliers (« 160 000 »). Correction globale mécanique à confier à l’intégration ; non proposée ligne par ligne pour ne pas créer des centaines d’anciens.
- **D-02 — Unité ml/min.** « ml/min » (4 occurrences) : écriture « mL/min » préférée par l’ISO ; la graphie « ml/min » est celle de l’information professionnelle suisse. Choix de l’intégration.
- **D-03 — Encadrés « Piège » à l’infinitif.** Huit encadrés « Piège » (sections 1, 6, 8 ×2, 13, anatomie, p-2, p-4) s’ouvrent par un infinitif nominalisé (« Coder… », « Écarter… »). STYLE_REDACTION § 2 proscrit l’infinitif injonctif ; l’infinitif est ici descriptif de l’erreur. Seule la construction agrammaticale de « Coder G98† » est proposée (P-23, P-45). Choix de style à trancher.
- **D-04 — Listes Pareto.** Les sept fenêtres Pareto sont des listes de formules nominales (fonction « fraction contractée »). Non réécrites.
- **D-05 — Inamovible / non amovible.** « botte plâtrée inamovible » (section 10, fenêtre QualiCCare) est conservé : terme du document suisse. « Dispositif inamovible » est harmonisé en « dispositif non amovible » (sept occurrences), terme dominant de la leçon.
- **D-06 — Mentions « cellulite » et « PET-CT ».** « Cellulite » est conservé entre parenthèses en section 8 (« dermo-hypodermite (cellulite) ») ; « PET/PET-CT » (glossaire) est conservé : le sigle francophone TEP n’est pas défini dans la leçon.

## Lacunes

- Aucune source médicale n’a été relue : l’audit est linguistique et ne vérifie aucun fait. Les 21 renvois ne sont pas tranchés.
- Le libellé officiel « SAI » de la CIM-10-GM 2024 (OFS/BfArM) n’a pas été consulté (R-03, R-04).
- Aucune figure ni image dans la leçon : sans objet pour les légendes.
- Rendu navigateur non vérifié : l’audit porte sur le source HTML.

## Tableau de bord

| Indicateur | Valeur |
|---|---|
| Fichiers lus en entier | 7 / 7 |
| Empreintes conformes | oui |
| Propositions | 95 (toutes uniques, sans chevauchement) |
| Renvois médicaux | 21 |
| Choix différés | 6 |
| Audit des abréviations après application | `{}` sur six fichiers |
| Fond modifié | non |

*Audit IA — revue distincte d’une validation médicale humaine ; aucune source canonique modifiée.*
