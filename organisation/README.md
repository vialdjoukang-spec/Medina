# Référence commune des fragments MEDINA

Ouvrir [MEDINA_Organisation.html](MEDINA_Organisation.html) ou le [tableau de bord publié](https://vialdjoukang-spec.github.io/Medina/organisation.html). Le fichier HTML fonctionne aussi sans connexion : fragments, catégories, titres et ordre théorique sont incorporés au fichier.

`fragments.json` fixe les 22 libellés publics et leurs rangs de production. Les identifiants techniques S01…T7 sont conservés pour les liens et la construction. L'ordre reprend les priorités du plan historique ; les axes transversaux reçoivent une place explicite dans cette séquence.

Chaque fragment présente ses blocs et catégories du catalogue historique MEDINA, leurs intitulés, leurs liens vers les cours existants et leur rang théorique. Les priorités codées viennent en premier, puis les autres catégories dans l'ordre du catalogue. Cette proposition éditoriale se modifie dans le registre ; elle ne constitue pas un ordre officiel de la CIM. Les thèmes rattachés à une autre spécialité restent visibles par des renvois.

Un cours intégré, un regroupement déclaré et une catégorie à produire ont des états distincts. `covers` signale un regroupement prévu par les sources ; il ne prouve pas l'exhaustivité de la leçon correspondante.

Les 1 636 catégories locales portent des codes **CIM-10-GM 2024**. Le catalogue historique n'est pas toute la classification officielle : notamment, les catégories F ne sont pas présentes et certains sous-codes sont partiels. La complétude **CIM-11** n'est établie pour aucun fragment. Médecine des âges de la vie, Diagnostic, Éthique restent sans catégories rattachées.

Pour reconstruire le fichier depuis les sources :

```bash
python3 tools/build_organisation.py
```

Le site reconstruit `organisation.html` à chaque publication depuis `main`. Pour une copie déjà téléchargée, utiliser « Version en ligne » afin de consulter l'état courant. Le protocole commun des deux dossiers est décrit dans [DELIVERY_PROTOCOL.md](../docs/collaboration/DELIVERY_PROTOCOL.md).

## Production partagée

[production_plan.json](production_plan.json) attribue les 21 fragments hors cardiologie : 11 Claude, 10 Codex, avec un seul emplacement de chapitre actif par agent. Les règles, les files et la clôture avant le chapitre suivant sont détaillées dans [FRAGMENTS_RESTANTS.md](../docs/collaboration/FRAGMENTS_RESTANTS.md). Le tableau affiche le responsable et le rang dans sa file ; chaque attribution porte sur le fragment entier, dont toutes les catégories restent regroupées. Dans chaque texte, nommer une catégorie **code — intitulé (libellé complet du fragment)** ; la complétude CIM-11 reste à établir. Exécuter `python3 tools/production_plan.py` pour contrôler la répartition.
