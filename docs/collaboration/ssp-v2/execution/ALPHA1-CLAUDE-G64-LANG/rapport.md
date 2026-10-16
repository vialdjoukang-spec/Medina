# Audit linguistique G64 — Autres affections du système nerveux périphérique (S08)

Mission ALPHA1-CLAUDE-G64-LANG, branche `claude/alpha1/g64-lang-g1`, base `32416a20`. Revue IA, distincte d’une validation médicale humaine ; aucune source canonique modifiée.

## Tableau de bord

| Indicateur | Valeur |
|---|---|
| Empreintes SHA-256 des 7 fichiers | conformes au manifeste |
| Propositions locales (`propositions.json`) | 74, ancien unique vérifié mécaniquement |
| Renvois médicaux | 27 |
| Observations globales | 6 |
| Choix différés (non appliqués) | espaces insécables globales ; « fibrillation atriale/auriculaire » (aucune occurrence) |
| Propositions, fichier chapters/G64/G64_a.html | 18 |
| Propositions, fichier chapters/G64/G64_b.html | 10 |
| Propositions, fichier chapters/G64/G64_c.html | 5 |
| Propositions, fichier chapters/G64/G64_d.html | 8 |
| Propositions, fichier chapters/G64/G64_pop1.html | 7 |
| Propositions, fichier chapters/G64/G64_pop2.html | 9 |
| Propositions, fichier glossary/g64.py | 17 |

Principales catégories : phrase nominale (23), ambiguïté (13), grammaire (7), syntaxe (5), lexique (4), abréviation (3), répétition (2), cohérence terminologique (2).

## Constats les plus importants

1. **Glossaire** : les développements lettre à lettre d’ANCA, d’ANA et de FI ne correspondent pas aux lettres de l’acronyme (propositions G64-LANG-g-02 à g-04).
2. **Ambiguïtés de lecture** : « 50 % des patients neurologiques » (carence en B12), « guideline … devenue l’EAN », « tableaux » pour désigner des situations cliniques, pronom « elle » de la corticothérapie.
3. **Phrases nominales** de la rubrique Limite et des définitions des fenêtres, proscrites par le guide de rédaction : restituées en phrases complètes sans changer un fait.

## Renvois médicaux (non reformulés)

Une formulation qui crée ou renforce une causalité, une fréquence ou une chronologie absente de la source relève de l’audit médical.

| Id | Fichier | Type | Constat |
|---|---|---|---|
| G64-LANG-RM-01 | G64_a.html | fréquence absente de la source | « presque toujours » chiffre une fréquence (qu’une catégorie voisine plus précise existe) que ni la CIM-10-GM ni les sources citées ne donnent. À l’audit médical : reformuler sans fréquence (« une catégorie voisine plus précise existe en général » reste une fréquence) ou le sourcer. |
| G64-LANG-RM-02 | G64_a.html | chronologie / cohérence | La ligne « Subaiguë » associe la vascularite à une « évolution par poussées » ; la même expression revient dans le tableau des mécanismes (« aux membres inférieurs, par poussées »). Une évolution par poussées est une chronologie distincte d’une évolution subaiguë, et « aux membres inférieurs » est une localisation. Aucune de ces deux précisions n’est reprise ailleurs dans la leçon ; leur source (guideline PNS 2010 ?) n’est pas vérifiée ici. |
| G64-LANG-RM-03 | G64_a.html | attribution des chiffres | Le tableau mêle des chiffres que les fenêtres rattachent à d’autres sources (petites fibres : Sopacua 2019 ; chimiothérapie, postopératoire : revues suisses). La phrase les attribue tous à la revue allemande de 2018. À vérifier ligne par ligne par l’audit médical. |
| G64-LANG-RM-04 | G64_a.html | causalité | « Une cause évitable existe aussi », « est responsable de », « dues au positionnement » (section 11), « en cause dans 20 à 30 % des cas » (anamnèse) et « la prévention passe par le positionnement » (4.4) établissent un lien de causalité et une évitabilité. Le texte indique que ce chiffre vient du résumé d’une revue suisse : un résumé donne souvent une association ou une attribution, non une preuve causale. Aucune reformulation n’est proposée ici. |
| G64-LANG-RM-05 | G64_a.html | causalité / chronologie | La « séquence » du 4.2 (inflammation, lésion du vaisseau, chute de l’irrigation, ischémie, dégénérescence) et le « d’où » du profil multifocal sont présentés comme un mécanisme, la déduction étant signalée mais retombant en conclusion causale. La chute de l’irrigation n’apparaît pas dans le tableau des mécanismes. Le même enchaînement est répété dans l’onglet Sciences (Anatomie : « produit l’ischémie nerveuse » ; Physiologie : « réduit l’irrigation du nerf »). |
| G64-LANG-RM-06 | G64_a.html | association présentée comme mécanisme | La section 3 et la fenêtre Nav écrivent que les variants sont « associés » à la neuropathie des petites fibres ; le 4.3 écrit qu’ils « rendent » les nocicepteurs hyperexcitables, la fenêtre Nav qu’ils « provoquent » l’hyperexcitabilité « dont dépend la douleur », l’onglet Sciences que la douleur « suit ce mécanisme ». Le passage de l’association au mécanisme est à confirmer, d’autant que la source citée est un résumé (Sopacua 2019). |
| G64-LANG-RM-07 | G64_a.html | fréquence absente de la source | « la plupart » est une fréquence que la revue allemande de 2018 n’énonce pas dans le texte du dossier. |
| G64-LANG-RM-08 | G64_a.html | contenu incohérent avec la leçon | Le tableau d’anamnèse affirme « carence ou excès de B6 et de B12 » et « les deux directions sont neuropathiques ». Le reste de la leçon cite la carence en B12 et la carence ou l’excès de B6 uniquement. Un excès de B12 n’est établi nulle part dans le dossier. |
| G64-LANG-RM-09 | G64_a.html | comparatif absent de la source | « le signe le plus utile » (encadré « À retenir » de la section 6) est un superlatif ; la source donne une sensibilité et une spécificité élevées, non un classement des signes. |
| G64-LANG-RM-10 | G64_b.html | fréquence et périmètre | « le plus souvent bon » est une fréquence ; de plus, il s’agit ici de « la polyneuropathie cryptogénique » alors que le tableau des causes et la section 10 parlent de la polyneuropathie « sensitive » cryptogénique, de « bon pronostic » sans fréquence. |
| G64-LANG-RM-11 | G64_b.html | cohérence interne | Le piège nomme la biopsie nerveuse « dernier recours », alors que la démarche en sept étapes place après elle les petites fibres (étape 6) et la génétique (étape 7), et que la fenêtre de pharmacologie indique « du moins au plus invasif ». À arbitrer par l’audit médical. |
| G64-LANG-RM-12 | G64_b.html | absolu et causalité | « toujours » et « elle seule peut arrêter l’évolution » sont des affirmations absolues. Les urgences (SGB, vascularite) ou la douleur intense peuvent justifier un traitement symptomatique ou en parallèle. Même remarque pour « complètent toujours le traitement » (encadré de la section 9). |
| G64-LANG-RM-13 | G64_b.html | fréquence absente de la source | La fréquence n’est rattachée à aucune source dans la leçon ni dans les fenêtres. |
| G64-LANG-RM-14 | G64_b.html | portée de la source | « préventive et curative » attribue un effet causal ; la section 11 ne décrit qu’un programme supervisé recommandé. À confirmer au niveau de lecture (résumé ou texte intégral) de la revue de 2026. |
| G64-LANG-RM-15 | G64_b.html | chronologie et fréquence | « puis » présente la persistance comme la suite de l’atteinte aiguë chez tout patient ; la section 10 donne deux fréquences distinctes (60 à 80 % de réversibilité en 2 à 3 jours ; 73 % de lésions persistantes sous traitement prolongé). |
| G64-LANG-RM-16 | G64_b.html | cohérence interne | La section 3 attribue le 0,14 % aux « neuropathies postopératoires » ; la section 11 aux « neuropathies compressives ». Les deux populations ne se recouvrent pas nécessairement. Non harmonisé ici pour ne pas changer le périmètre du chiffre. |
| G64-LANG-RM-17 | G64_b.html | absolu | « n’est pas une cause » est plus catégorique que le tableau des causes (« n’explique pas toujours la neuropathie ») et que la fenêtre Paraprotéines, qui énumèrent trois exceptions. Même nuance pour « n’explique pas la neuropathie » dans cette fenêtre. |
| G64-LANG-RM-18 | G64_b.html | ambiguïté de sens du critère | « cinq prédicteurs sont réunis » se lit comme une exigence cumulative des cinq. La section e-5 et la fenêtre listent cinq prédicteurs histologiques de la vascularite « probable » sans dire s’il faut les cinq ou l’un d’entre eux. La formulation doit être confrontée à la guideline PNS 2010 par l’audit médical ; elle n’est pas reformulée ici. |
| G64-LANG-RM-19 | G64_c.html | portée de la source | « Elle est sûre » conclut d’une absence d’effet grave dans environ 35 000 biopsies à une sécurité absolue. Source : résumé de la guideline EFNS/PNS 2010. |
| G64-LANG-RM-20 | G64_c.html | contenu incohérent avec la leçon | La phrase annonce trois niveaux mais n’en décrit que deux (certaine, probable). Le niveau manquant (possible ?) n’est pas dans la leçon. |
| G64-LANG-RM-21 | G64_c.html | causalité renforcée | La section 3 et l’anamnèse écrivent « risque au-delà d’environ 100 g/jour pendant des années » ; l’onglet Sciences écrit « cause ». Le passage de risque à cause est un changement de sens. |
| G64-LANG-RM-22 | G64_c.html | causalité implicite | L’encadré relie la physiologie des canaux Nav (excitabilité nociceptive) à la première ligne forte des ligands α2δ et des IRSN. Aucune source du dossier n’établit ce lien mécanistique (la méta-analyse porte sur la douleur neuropathique toutes causes). De même, l’encadré d’Anatomie (« expliquent pourquoi le profil clinique varie ») attribue une valeur explicative non démontrée. |
| G64-LANG-RM-23 | G64_c.html | modalité | Le texte affirme une valeur (« contient ») puis dit qu’elle n’est pas obligatoire ; la fenêtre LCR écrit « typiquement ». La modalité exacte (fréquent, typique, constant) est à fixer par l’audit médical. |
| G64-LANG-RM-24 | G64_d.html | ambiguïté du délai | « 18 à 24 mois après rémission » peut se lire comme une durée de traitement d’entretien commençant à la rémission ou comme un délai d’arrêt. À confronter à la guideline PNS 2010 (même formulation dans la fenêtre Immunosuppression). |
| G64-LANG-RM-25 | G64_pop2.html | association présentée comme mécanisme | Voir le renvoi G64-LANG-RM-06 : « provoquent » et « dont dépend » vont plus loin que « associés » de la phrase précédente. |
| G64-LANG-RM-26 | g64.py | fréquence absente de la source | « souvent » est une fréquence ; la leçon écrit « Une paralysie ascendante après une infection … rend le SGB très probable » sans fréquence du tableau inverse. |
| G64-LANG-RM-27 | g64.py | information étrangère à la leçon | La définition des QST (« épreuves psychophysiques », « seuils de perception ») ne figure pas dans les passages de la leçon ; elle vient d’un savoir non cité. À sourcer ou à restreindre à la phrase de la fenêtre (diagnostic des petites fibres). |

## Observations globales

- **G64-LANG-OG-01 — Espaces insécables** (differe). Les sept fichiers ne contiennent aucune espace insécable (0 occurrence de U+00A0) : les espaces avant « ; : ! ? », à l’intérieur des guillemets « » et avant « % », ainsi que dans les nombres à milliers (100 000, 500 000, 35 000), sont des espaces ordinaires. Le SVG de la figure 1 est concerné (« Drapeau rouge ? »). Choix global différé par le coordinateur ; aucune proposition émise.
- **G64-LANG-OG-02 — Usage « fibrillation atriale / auriculaire »** (differe). Aucune occurrence de « fibrillation » dans la leçon (recherche insensible à la casse dans les sept fichiers). Choix global différé par le coordinateur ; sans objet pour G64.
- **G64-LANG-OG-03 — Boutons imbriqués (technique, hors périmètre linguistique)** (signale). Plusieurs mots verts contiennent un autre mot vert (tests sensitifs quantitatifs (QST) en 2.3 ; « Neurographie et EMG », « Biologie élargie orientée et LCR », « Échographie nerveuse, neurographie par IRM », « Petites fibres : QST, biopsie cutanée » dans le tableau de la démarche ; LCR et SGB doublés dans l’alerte et le tableau ; « syndrome POEMS » ; mêmes motifs dans l’onglet Examens). Un bouton dans un bouton est invalide en HTML. Non traité : modifier les balises sort d’un audit de formulation.
- **G64-LANG-OG-04 — Terminologie** (signale). « guideline » (près de 25 occurrences) alterne avec « recommandations » ; en français de Suisse « information professionnelle » est employé dans le texte mais « FI » dans les tableaux et la clé de glossaire (en français, l’abréviation usuelle est IP). Choix éditorial transversal non appliqué.
- **G64-LANG-OG-05 — Forme** (signale). Les listes Pareto, les cellules de tableaux et les définitions du glossaire sont majoritairement nominales : seuls les cas où la phrase nominale gênait la lecture ont été reformulés. Plusieurs tableaux (causes, mécanismes, biologie, biopsies) n’ont pas de paragraphe de lecture après eux, contrairement à la section 4 du guide de rédaction : ajout de contenu, donc hors propositions locales. Les unités « ml/min », « µl » suivent l’usage des informations professionnelles suisses et ne sont pas modifiées.
- **G64-LANG-OG-06 — Structure de l’onglet Sciences (hors périmètre linguistique)** (signale). Le bandeau .sci-bar compte quatre disciplines (Anatomie, Histologie, Physiologie, Biochimie) et aucun bouton « Sémiologie fondamentale et analytique ». À traiter par l’audit médical (G64-MED).

## Propositions

Le détail (extrait ancien, nouveau, motif, catégorie) figure dans `propositions.json` ; toutes portent `fond_inchange: true`. Exemples : « Elle décrit si l’atteinte… » devient « Elle indique si l’atteinte… » ; « La duloxétine n’a … qu’une indication dans » devient « La duloxétine n’est indiquée … que dans » ; « la peau et l’état général cherchent » devient « l’examen de la peau et de l’état général cherche ».

## Rubrique 21 — Sémiologie fondamentale et analytique

Sans objet pour un audit linguistique (mission -LANG). Constat structurel signalé en G64-LANG-OG-06.

## Lacunes

- Aucune source médicale n’a été relue : un audit linguistique ne vérifie pas les faits. Les citations (Sommer 2018, Sopacua 2019, Lauria 2010, Collins 2010, Soliman 2025, Lyrica, Duloxetin-Mepha via AmiKo, revues suisses de 2023 et 2026) ne sont ni confirmées ni infirmées ici.
- Les formulations qui touchent à un sens médical possible (causalité, fréquence, chronologie, critères) sont renvoyées (27 renvois) et non reformulées.
- Aucun test en navigateur : l’effet des propositions sur l’affichage (largeur des tableaux, justification) n’a pas été mesuré.
- Les espaces insécables et l’usage « fibrillation atriale/auriculaire » sont différés par instruction.
- Pas de correcteur externe (Antidote, LanguageTool) : relecture par lecture intégrale, avec contrôles mécaniques sur l’unicité des extraits, les nombres et les balises.

*Audit IA — revue distincte d’une validation médicale humaine ; aucune source canonique modifiée.*
