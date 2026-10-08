# Isolation des 22 frontends — 8 octobre 2026

Auteur unique de `fragment_surface.py`, `tests/audit_fragments.py` et `tests/test_fragment_surface_isolation.py`. Aucun changement de source médicale canonique, registre documentaire, `build_front.py`, `build_index.py` ou fichier `engine/category_organisation.*` par cet agent. Le coordinateur adapte le constructeur et le moteur d'accueil ; l'autre agent adapte le portail.

## Résultat

Les 22 frontends disposent d'une identité de spécialité et d'un périmètre exclusif, y compris les fragments historiques sans `surface: courses-v1`. Leurs catégories, cours, variantes, compteurs, alias et fenêtres ne réintroduisent pas le cours d'un autre fragment.

Les données de l'accueil sont exposées dans `#medina-category-organisation-data` :

- `fragment.id`, `label`, `specialty`, `order` : identité et provenance documentaire.
- `fragment.display_name` : nom de spécialité sans identifiant technique.
- `fragment.accent` : couleur hexadécimale fixe propre au fragment.
- `fragment.description` : phrase éditoriale courte sans nouvelle assertion clinique.
- `blocks` : catégories et chapitres exclusivement propres ; chaque leçon porte `source_fragment_id` égal au fragment courant et une URL locale `#/entry/<code>`.
- `courses` : cours canoniques propres, avec leurs titres, variantes et URL locales.
- `integrated_count` : nombre de cours canoniques propres, dédupliqués entre blocs.
- `category_count` : nombre de catégories locales.

Un cours propre partagé entre deux blocs peut conserver `reference: true` : cette valeur indique le regroupement documentaire des variantes, sans constituer un renvoi vers une autre spécialité. Sa propriété et son URL restent locales.

## Propriété centralisée

Les helpers `frontend_entries(fragment, entries, root)` et `fragment_chapters(fragment, entries, root)` sont partagés par la construction et l'audit. `SPECIALTY_BY_FRAGMENT` attribue une seule identité frontend aux 22 fragments, même lorsqu'un descripteur historique ne possède pas de champ `specialty`.

Le classement donne priorité aux rattachements explicites des cours. La spécialité médicale primaire corrige ensuite les classifications reposant seulement sur l'ancien organe ; les catégories génériques de médecine interne conservent leur rattachement anatomique. Les variantes d'un cours intégré restent avec ce cours canonique.

Ainsi, **A43 — Nocardiose**, **B18 — Hépatite virale chronique** et **A04 — Autres infections intestinales bactériennes** appartiennent au frontend d'infectiologie. A43 n'est plus présenté en cardiologie, et B18/A04 ne sont plus présentés dans le frontend de gastroentérologie. Les données historiques d'origine restent intactes dans le dépôt. Les 1 636 catégories sont réparties sans perte ni doublon.

Les cours intégrés existants se répartissent en 21 de cardiologie, 5 de pneumologie, 4 d'immunologie, 1 de rhumatologie et 1 d'infectiologie : **32 cours propres**, sans nouvelle déclaration d'audit médical ou de complétude de fragment.

## Frontière finale et fenêtres

`finish_surface` impose de nouveau le périmètre avant la sortie HTML. Il refuse un template de cours absent de la spécialité, un template propre manquant ou une fenêtre portant le préfixe d'un autre cours. Il supprime les anciens catalogues globaux, familles, plans cliniques génériques, profils, références de spécialités, SSP et données GLOBALITY embarquées.

L'API structurelle de l'ancien générateur reste disponible avec un plan vide, afin de préserver la coque sans embarquer ses développements génériques. Les vrais cours restent leurs templates canoniques, inchangés. Les titres du navigateur et de la marque affichent le nom de spécialité ; les identifiants techniques restent internes.

Le glossaire embarqué conserve les clés effectivement utilisées par les cours et fenêtres locaux, puis les dépendances de leurs définitions. Une référence d'approfondissement n'est conservée que lorsque sa fenêtre existe dans ce frontend. Les définitions et fenêtres propres restent disponibles ; le glossaire complet de l'atlas n'est plus embarqué dans les fragments sans cours.

## Vérification

- `python3 -m unittest discover -s tests -p test_fragment_surface_isolation.py` : **6 tests réussis**, comprenant la finition des 22 frontends, la partition exhaustive des catégories, le transfert A43/B18/A04, les refus de templates et fenêtres étrangers, le retrait des alias étrangers et la conservation des définitions/fenêtres locales.
- Construction réelle de T1 puis des **22 fragments réussie** dans `/workspace/work/fragment-isolation-build/fragments`.
- `MEDINA_FRAGMENTS=/workspace/work/fragment-isolation-build/fragments python3 tests/audit_fragments.py` : **22 fragments conformes, JavaScript valide, construction reproductible**.
- L'audit vérifie aussi les compteurs propres, l'identité de spécialité, l'absence d'anciens catalogues et de fenêtres étrangères, et la présence de toutes les définitions utilisées.

Le coordinateur exécute séparément les tests d'interface et les captures sur sa construction finale `/workspace/work/medina-redesign/fragments`. Les publications, commits et contrôles finaux sont gérés par lui.
