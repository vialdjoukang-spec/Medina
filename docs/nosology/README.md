# Complétion nosologique CIM-10-GM 2024

Cette mission ajoute uniquement un inventaire et des coquilles vides. Elle ne rédige aucun cours. `QUEUE.md` suit les 22 fragments dans l'ordre du registre public ; chaque fragment possède sa branche, son commit et sa PR. L'état « fait » atteste le remplissage nosologique et les contrôles, pas l'achèvement des cours.

## Référentiel et couverture

Les archives françaises CSV et ClaML de l'OFS du 31 octobre 2024 sont conservées dans `nosology/sources/`. Les URL et empreintes SHA-256 sont dans `nosology/reference.json`. Le CSV contient les codes générés par les modificateurs, au-delà des seules classes explicites du ClaML. L'import conserve les libellés, chapitres, blocs, codes terminaux et marques de codage (`!`, `*`, `†`). Ces marques sont distinctes de l'Étoile d'Or pédagogique.

L'OFS fournit 1 636 catégories actives à trois caractères hors psychisme, déjà présentes dans MEDINA. Elles correspondent à 15 835 codes actifs à trois, quatre et cinq caractères. Tous les codes source, y compris ceux exclus, sont inventoriés. Les codes du chapitre V et U63 sont exclus du psychisme ; les codes `Content=N` sont non affectés, sans coquille de maladie. Les 22 chapitres et 250 blocs sont conservés dans le référentiel, même sans code actif dans le périmètre.

## Intégrité, sous-leçons et versions

`nosology/integrity.json` contient les empreintes de tous les fichiers préexistants sous `chapters/`, `glossary/` et `livraisons/`, ainsi que les manifestes et la coque documentaire. Aucun de ces fichiers n'est modifié. Les sous-leçons et versions préexistantes restent intactes. Le moteur conserve aussi les titres et variantes détaillées existantes : il ajoute les codes manquants, sans remplacer les entrées déjà présentes. Chaque cours canonique conserve son groupe de catégories `covers`. Une catégorie regroupée n'est pas une seconde leçon. Les versions sont enregistrées comme références à leurs fichiers existants ; elles ne sont ni fusionnées ni supprimées.

Chaque code détaillé manquant reçoit une coquille JSON avec le plan monographique adaptatif et des contenus de sections vides. Un code détaillé peut être consulté et recherché directement. La présence d'un cours principal ne signifie pas que toutes ses variantes détaillées sont rédigées. Une relance conserve les sections ou notes déjà remplies d'une coquille.

## Mapping

`reference.json.mapping` attribue chaque catégorie active à un fragment principal et, au besoin, à des fragments secondaires. Les tumeurs localisées, malformations, symptômes, traumatismes et facteurs de santé suivent le système concerné. Les cours préexistants et leurs catégories regroupées conservent leur propriétaire. Les fragments secondaires sont des renvois vers le propriétaire, sans duplication de cours ou de progression. Les codes contextuels composites gardent un propriétaire principal ; les rattachements transversaux proposés sont listés dans `docs/nosology/<fragment>.json` pour arbitrage.

## Étoiles d'Or et limites du référentiel d'examen

La source examinée est PROFILES 2017, avec ses 265 SSP, cadre applicable à l'examen 2026. La SMIFK annonce l'utilisation du nouveau PROFILES à partir de 2028 : https://smifk-cims.ch/projects. La CIM reste exclusivement la CIM-10-GM 2024 française OFS.

PROFILES décrit des situations et compétences : il ne publie pas une liste officielle de maladies exigibles avec codes CIM. `exam_mapping` établit des correspondances pédagogiques explicites entre catégories et SSP ; les entités héritent du lien de leur catégorie. Une Étoile d'Or fixe, sans commande utilisateur ni stockage local modifiable, signale ce lien. `official_icd_crosswalk=false` évite de présenter cette correspondance comme une certification officielle. Les codes sans lien établi sont listés sous `exam_unresolved` pour arbitrage ; ils ne sont jamais déclarés « non exigibles ». L'exhaustivité des étoiles au sens d'une liste officielle de maladies d'examen ne peut pas être certifiée par ce référentiel seul.

## Jauges

Le dénominateur inclut les cours canoniques dédoublonnés et chaque coquille détaillée. Le numérateur compte un cours préexistant avec ses quatre fichiers non vides, ou une coquille dont toutes les sections ont été explicitement remplies. Un regroupement de catégories ou un renvoi n'augmente pas le numérateur. `nosology/progress.json` recalcule les jauges des 22 fragments et la jauge globale à chaque invocation ; la file de traitement reste distincte de la rédaction des cours.

## Reprise et contrôles

```bash
python3 tools/fill_nosology.py --fragment S01
python3 -m unittest discover -s tests -p test_nosology_engine.py
python3 build_front.py --fragment S01
python3 tools/fill_nosology.py --fragment S01 --complete
```

Reprendre au premier fragment non coché de `QUEUE.md`. L'outil refuse d'avancer hors ordre. Un contrôle échoué interdit de marquer le fragment terminé. Chaque livraison indique codes, coquilles, cours préservés, étoiles, jauge, codes non rattachés et cas d'arbitrage.
