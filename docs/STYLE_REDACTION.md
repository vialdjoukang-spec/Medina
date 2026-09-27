# Guide de rédaction MEDINA — « Le lecteur comprend, il ne devine pas »

> Exigence du propriétaire (26.09.2026). Ce guide s’applique à chaque phrase d’un cours : îlots, tableaux, encadrés, fenêtres, quiz, Pareto. Il complète PROMPT_MEDINA.md (§ 4 contrat HTML, § 10 contenu, § 11 rigueur) sans rien en retirer.

## 1. La règle d’or

L’obsession du rédacteur est que le lecteur **comprenne**. Il ne doit jamais deviner un lien, un chiffre ou une raison. Chaque affirmation dit **quoi**, puis **pourquoi**, puis **ce que cela change** pour le patient. Rien n’est écrit gratuitement : une phrase qui n’explique, ne prouve ou ne sert pas une décision est supprimée.

## 2. Des phrases courtes et complètes, jamais nominales

Une phrase complète possède un sujet et un verbe conjugué. Elle reste courte : une idée par phrase, une vingtaine de mots au plus.

Sont interdits partout, y compris dans les listes, les encadrés, les cellules d’explication et les fenêtres :
- la phrase nominale (« Hypoxémie sévère. », « Surveillance clinique rapprochée. ») ;
- l’infinitif injonctif (« Rechercher une chirurgie récente. », « Prélever deux hémocultures. ») ;
- l’énumération de mots-clés à la place d’une explication ;
- la parenthèse qui remplace une phrase (« (cf. supra) », « (voir îlot 7) » sans explication).

| Écrit à proscrire | Écrit attendu |
|---|---|
| « Rechercher une chirurgie récente, une immobilisation, un cancer actif. » | « Le médecin recherche d’abord une chirurgie récente, une immobilisation ou un cancer actif. Ces trois situations ralentissent le retour veineux ou activent la coagulation : elles multiplient le risque de thrombose. » |
| « Tachypnée : signe de gravité. » | « Une fréquence respiratoire supérieure à 30 par minute signale une pneumonie grave. Elle traduit un travail respiratoire que le patient ne pourra pas soutenir longtemps. » |
| « Hémocultures avant antibiotiques si possible. » | « Le médecin prélève deux paires d’hémocultures avant la première dose d’antibiotique. Il le fait parce qu’une seule dose peut stériliser les cultures et priver l’équipe de l’identification du germe. Il ne retarde pas l’antibiotique pour autant chez un patient en choc. » |

Les **titres** restent des groupes nominaux courts : c’est leur fonction. Les **cellules de tableau** peuvent être brèves, à la condition expresse que le tableau soit introduit et commenté (§ 4).

## 3. Chaque partie suit trois temps : annonce, développement, épilogue local

Chaque îlot, chaque sous-partie (h3) et chaque discipline des sciences suit le même mouvement.

1. **L’annonce** ouvre la partie en deux à quatre phrases. Elle dit ce que la partie va établir, pourquoi le lecteur en a besoin et comment elle se relie à la partie précédente.
2. **Le développement** progresse du normal au pathologique, du mécanisme à la décision. Il donne un exemple chiffré ou un patient pour chaque notion nouvelle. Il place un **mot vert cliquable** sur chaque notion qui mérite un approfondissement (§ 5).
3. **L’épilogue local** ferme la partie dans un encadré `<div class="key"><b>À retenir.</b> …</div>`. Il résume en phrases complètes ce que le lecteur doit savoir faire après cette partie, puis annonce le lien avec la partie suivante.

La densité informationnelle compte autant que la clarté. Une partie qui tient en un paragraphe n’est pas développée : elle doit contenir le mécanisme, les chiffres utiles, les situations particulières, les pièges et la conséquence pratique.

## 4. Aucun tableau sans introduction ni lecture

Un tableau n’apparaît jamais seul. Il suit toujours ce schéma :
1. **Avant le tableau**, un paragraphe explique la question à laquelle le tableau répond, les paramètres comparés et la logique de ses colonnes (« La première colonne donne le paramètre mesuré ; la deuxième donne la valeur normale de l’adulte ; la troisième indique le seuil qui change la décision. »).
2. **Le tableau** porte des en-têtes explicites.
3. **Après le tableau**, un paragraphe de lecture enseigne comment s’en servir : ce qu’il faut regarder d’abord, l’erreur fréquente, et un exemple de patient lu à travers le tableau.

La même règle vaut pour les figures : la figure est annoncée, puis sa lecture est expliquée.

## 5. Les termes cliquables sont un devoir, pas une option

Dans l’anamnèse, l’examen clinique, le diagnostic, la thérapeutique, la prévention et le pronostic, chaque antécédent, symptôme, signe, examen, score, critère, médicament et essai important est un mot vert : `<button class="w" data-k="<code>-cle">libellé (destination annoncée)</button>`. Chaque mot vert ouvre une fenêtre réelle (`<template data-pop="<code>-cle" data-title="…">`) qui suit elle aussi ce guide : définition, mécanisme, technique ou mode d’emploi, valeur et limites, piège, conséquence pratique.

## 6. Les sciences fondamentales expliquent le « pourquoi » du cours

Chaque discipline (anatomie, histologie, physiologie, biochimie ou immunologie, génétique ou microbiologie) :
- s’ouvre par une annonce qui dit quelle question clinique cette science éclaire ;
- expose le fonctionnement normal, puis sa perturbation dans la maladie ;
- contient au moins un schéma légendé ou un tableau introduit et commenté ;
- se termine par des encadrés `key` de corrélation (science → clinique, science → examen, science → traitement), rédigés en phrases complètes ;
- atteint la profondeur d’un cours universitaire, sans jamais s’éloigner de la maladie étudiée.

## 7. Exactitude

Réécrire ne veut pas dire inventer. Chaque chiffre, seuil, posologie et essai déjà vérifié en texte intégral (voir la section « Vérification en texte intégral » de `audits/<CODE>.md`) est conservé tel quel. Toute donnée nouvelle est vérifiée dans la source primaire (information professionnelle suisse, recommandation, PubMed) et datée. Aucune métaphore, aucun jeu de mots, aucune formule de chantier.

## 8. Mise en page

Le texte est justifié par le moteur. Le rédacteur n’ajoute aucun style en ligne. Il écrit des paragraphes courts (trois à six phrases), séparés, et laisse la mise en forme au moteur et à la couche `polish`.
