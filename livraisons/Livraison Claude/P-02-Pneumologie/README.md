# P-02-Pneumologie — Livraison Claude

Fragment : **S02**. Base de contenu : `7fa06329b3369f54ef0831ae9f6cdf90fce5f605`. État : **partiel ; complétude CIM-11 non établie**.

Ce dossier reçoit les corrections de Claude. Une copie préparée par l'outil est un espace de travail ; elle ne constitue pas une livraison relue.

Copier ou préparer `livraison.json`, conserver les empreintes `sha256` des fichiers originaux, puis modifier les fichiers sous `sources/chapters/`. Décrire les corrections et les sources médicales dans un rapport. Les fichiers communs et CS sont corrigés directement sur une branche avec PR.

[Lire le fragment HTML](https://vialdjoukang-spec.github.io/Medina/fragments/MEDINA_S02_respiratoire.html) · [Organisation](https://vialdjoukang-spec.github.io/Medina/organisation.html) · [Toutes les sources](https://github.com/vialdjoukang-spec/Medina/tree/7fa06329b3369f54ef0831ae9f6cdf90fce5f605)

Sources communes : [chapters.json](https://github.com/vialdjoukang-spec/Medina/blob/7fa06329b3369f54ef0831ae9f6cdf90fce5f605/chapters.json) · [fragments.json](https://github.com/vialdjoukang-spec/Medina/blob/7fa06329b3369f54ef0831ae9f6cdf90fce5f605/fragments.json) · [glossary](https://github.com/vialdjoukang-spec/Medina/tree/7fa06329b3369f54ef0831ae9f6cdf90fce5f605/glossary) · [modules](https://github.com/vialdjoukang-spec/Medina/tree/7fa06329b3369f54ef0831ae9f6cdf90fce5f605/modules) · [engine](https://github.com/vialdjoukang-spec/Medina/tree/7fa06329b3369f54ef0831ae9f6cdf90fce5f605/engine) · [shell](https://github.com/vialdjoukang-spec/Medina/tree/7fa06329b3369f54ef0831ae9f6cdf90fce5f605/shell) · [build_front.py](https://github.com/vialdjoukang-spec/Medina/blob/7fa06329b3369f54ef0831ae9f6cdf90fce5f605/build_front.py) · [tests](https://github.com/vialdjoukang-spec/Medina/tree/7fa06329b3369f54ef0831ae9f6cdf90fce5f605/tests) · [organisation/fragments.json](https://github.com/vialdjoukang-spec/Medina/blob/main/organisation/fragments.json).

| Code | Cours |
| --- | --- |
| J45 | Asthme |
| J44 | Bronchopneumopathie chronique obstructive |
| J18 | Pneumonies de l’adulte |
| I26 | Embolie pulmonaire aiguë |

L'existence d'un cours ou de catégories CIM-10 ne certifie pas une couverture CIM-11 complète. Les textes sont intégrés dans les dossiers canoniques, puis les fragments sont reconstruits et contrôlés.

## Réceptions du 8 octobre 2026

- `lots/2026-10-08-PR20-349EFD5-J09/` conserve la relecture Claude de **J09 — Grippe** avec ses neuf sources et son rapport. Statut : reçu, non intégré ; le fragment P-02 reste incomplet sous le protocole actif.
- `lots/2026-10-08-PR20-69E5C11-J96-BROUILLON/` conserve les cinq fichiers présents de **J96 — Insuffisance respiratoire** aux commits `69e5c11` puis `97b7315`. Statut : rédaction en cours archivée, non injectable.
- `lots/2026-10-08-PR20-127FF21-J84-AUTEUR/`, `...-C678326-J86-AUTEUR/`, `...-2876123-J90-AUTEUR/`, `...-445CE2A-J93-AUTEUR/` et `...-2876123-J96-AUTEUR/` conservent les cinq versions d’auteur présentes à la tête PR20 `2876123` : 40 fichiers, 40 empreintes exactes. Les rapports les déclarent non relues par l’agent différé, non injectées et assorties de 41 réserves cumulées. Statut : reçues, non injectables.
- `lots/2026-10-08-PR20-8DBF199-J84-RELECTURE/`, `...-FC993A0-J86-RELECTURE/`, `...-FC993A0-J90-RELECTURE/`, `...-88334D9-J93-RELECTURE/` et `...-F8FD91B-J96-RELECTURE/` conservent les versions relues et injectées uniquement sur la branche Claude : 45 fichiers, 45 empreintes exactes. Pour J86, J90, J93 et J96, les sept sources remises sont identiques aux copies canoniques à leur commit de remise. Pour J84, le dossier de travail préserve le brouillon auteur tandis que les sept fichiers canoniques portent la relecture ; les deux états restent donc distincts. Les rapports maintiennent respectivement 6, 5, 7, 7 et 6 réserves et précisent que la revue par IA ne vaut pas validation médicale. Statut : reçues pour audit croisé, non intégrées dans `main`.
- I27, J47, J80, J81 et J12 restent au minimum incomplets ou sans rapport final reçu. Les instantanés postérieurs de balayage de conformité touchent de nombreux cours hors de ces remises ; `81a5d73` retouche J86/J90, `8666f56` retouche I26/J96, `9e9cd01` balaie I70/I71/I83, `084f7ec` balaie I10/I50/I46/I30/I40 et `da5cd70` balaie I33/I42. `48d412c` ajoute un audit interne transversal, sans nouvelle remise finale. Ils ne sont pas reçus comme livraison médicale exploitable. Le changement transversal de gouvernance proposé à `b718434` n’est pas en vigueur sur `main`.

Ces archives n'altèrent ni les attributions, ni le chapitre actif, ni les sources canoniques.
