# Navigation des versions prouvées

Index de liens seulement. Aucune consigne n’est réécrite, aucun texte hors de `main` n’est importé, et aucun plan ni format de leçon n’est modifié. Pour un même objet, la version retenue est le dernier commit qui touche le fichier, recoupé avec la date écrite dans le document. La date de pointe d’une branche ne sert pas de preuve.

Contrôle reproductible : `python3 -m unittest tests.test_references_navigation`.

## Contrôles techniques

| Objet | Statut | Preuve |
| --- | --- | --- |
| Contrôle courant des chapitres | `test_v7.py` | Commit [`a1c47783e8b1ed8fb8a1e3998e02419a5e6a9eab`](https://github.com/vialdjoukang-spec/Medina/commit/a1c47783e8b1ed8fb8a1e3998e02419a5e6a9eab) du 11 octobre 2026, 19:12 UTC. Pas de date interne. Blob `9f23427c3a99122e463d2b5dae9b03693e226cc6`. [Fichier à ce commit](https://github.com/vialdjoukang-spec/Medina/blob/a1c47783e8b1ed8fb8a1e3998e02419a5e6a9eab/test_v7.py). |
| Aperçu legacy | `test_preview.py` | Commit [`0f38d9aab4ef051eaa9013c4aebfdcb9d5105070`](https://github.com/vialdjoukang-spec/Medina/commit/0f38d9aab4ef051eaa9013c4aebfdcb9d5105070) du 28 septembre 2026, 02:30 Europe/Zurich. Blob `a0d2e09178398b1317b9f8f2cefed0467e5f0735`. [Fichier à ce commit](https://github.com/vialdjoukang-spec/Medina/blob/0f38d9aab4ef051eaa9013c4aebfdcb9d5105070/test_preview.py). `pack.py` l’empaquette encore : cette dépendance reste. Ce n’est pas le contrôle des chapitres. |

## Instructions dont la dernière version est dans `main`

| Sujet | Dernier commit qui touche le fichier | Lien stable |
| --- | --- | --- |
| Parité du 15 octobre 2026 | [`e986a31987d8e983a20b8211497faa69d779873d`](https://github.com/vialdjoukang-spec/Medina/commit/e986a31987d8e983a20b8211497faa69d779873d), en-tête 15 octobre 2026 | [PARITE_LEVEE_BLOCAGES_2026-10-15.txt](https://github.com/vialdjoukang-spec/Medina/blob/e986a31987d8e983a20b8211497faa69d779873d/docs/collaboration/instructions/PARITE_LEVEE_BLOCAGES_2026-10-15.txt) |
| Sémiologie fondamentale et analytique | [`8f5710c0cbd52ec82e2a5fbd8114fd5952beb294`](https://github.com/vialdjoukang-spec/Medina/commit/8f5710c0cbd52ec82e2a5fbd8114fd5952beb294), autorité 15 octobre 2026 | [YAML](https://github.com/vialdjoukang-spec/Medina/blob/8f5710c0cbd52ec82e2a5fbd8114fd5952beb294/docs/collaboration/instructions/SEMIOLOGIE_FONDAMENTALE_ANALYTIQUE_2026-10-15.yaml) |
| Contrat HTML des leçons (onglets, fenêtres, ancres) | [`2673735a07e05b7198e31ca01df98426f660332a`](https://github.com/vialdjoukang-spec/Medina/commit/2673735a07e05b7198e31ca01df98426f660332a), en-tête 8 octobre 2026 | [CHAPTER_SPEC.md](https://github.com/vialdjoukang-spec/Medina/blob/2673735a07e05b7198e31ca01df98426f660332a/CHAPTER_SPEC.md) |
| Style de rédaction, même commit | [`2673735a07e05b7198e31ca01df98426f660332a`](https://github.com/vialdjoukang-spec/Medina/commit/2673735a07e05b7198e31ca01df98426f660332a) | [STYLE_REDACTION.md](https://github.com/vialdjoukang-spec/Medina/blob/2673735a07e05b7198e31ca01df98426f660332a/docs/STYLE_REDACTION.md) |
| Prompt de vérité | [`60bb210048ebb80407bc1814dce54bc71ab843b4`](https://github.com/vialdjoukang-spec/Medina/commit/60bb210048ebb80407bc1814dce54bc71ab843b4), en-tête 15 octobre 2026 | [PROMPT_VERITE.md](https://github.com/vialdjoukang-spec/Medina/blob/60bb210048ebb80407bc1814dce54bc71ab843b4/docs/collaboration/betta/PROMPT_VERITE.md) |
| Prompt maître | [`e64c813f02212415f86bd71de6bf0886a943e7fa`](https://github.com/vialdjoukang-spec/Medina/commit/e64c813f02212415f86bd71de6bf0886a943e7fa), en-tête jusqu’au 13 octobre 2026 | [PROMPT_MEDINA.md](https://github.com/vialdjoukang-spec/Medina/blob/e64c813f02212415f86bd71de6bf0886a943e7fa/PROMPT_MEDINA.md) |
| Contrat SSP V2 et prompt commun | [`d40aaf7c845226429f662b710b0711ea5297d472`](https://github.com/vialdjoukang-spec/Medina/commit/d40aaf7c845226429f662b710b0711ea5297d472), autorité 15 octobre 2026 | [README-V2.txt](https://github.com/vialdjoukang-spec/Medina/blob/d40aaf7c845226429f662b710b0711ea5297d472/docs/collaboration/ssp-v2/2026-10-15/README-V2.txt), [prompt-commun-ia.yaml](https://github.com/vialdjoukang-spec/Medina/blob/d40aaf7c845226429f662b710b0711ea5297d472/docs/collaboration/ssp-v2/2026-10-15/prompt-commun-ia.yaml) |

Les chemins relatifs de ces fichiers dans `main` portent le même blob. Les copies plus anciennes sur d’autres branches sont historiques.

## Délégation — lien épinglé, sans fusion

Le dernier commit qui **écrit** encore le fichier est [`34840aac8123079578cbe0966144b00e0f28e986`](https://github.com/vialdjoukang-spec/Medina/commit/34840aac8123079578cbe0966144b00e0f28e986), le 15 octobre 2026 à 14:29 Europe/Zurich. Blob `e1c8bdea849d0c7d20b12a168b8017f67722f386`. Il n’est pas dans `main`. Il est contenu dans les pull requests ouvertes [98](https://github.com/vialdjoukang-spec/Medina/pull/98) et [100](https://github.com/vialdjoukang-spec/Medina/pull/100).

Texte à lire : [DELEGATION_VIAL_2026-10-15.md à 34840aac](https://github.com/vialdjoukang-spec/Medina/blob/34840aac8123079578cbe0966144b00e0f28e986/docs/collaboration/instructions/DELEGATION_VIAL_2026-10-15.md).

Le fichier du même chemin dans cet arbre est l’état antérieur, commit [`9e07092eccd14b410eb0273579f9f88cde78ccba`](https://github.com/vialdjoukang-spec/Medina/commit/9e07092eccd14b410eb0273579f9f88cde78ccba) du 15 octobre 2026 à 14:07 Europe/Zurich, blob `e37960f8afb53c6c1a651d7e0a690cdafb040d9d` : [copie de l’arbre](instructions/DELEGATION_VIAL_2026-10-15.md). Elle est conservée. Elle n’est pas réimportée ici.

Le commit [`77f194bef28bdd4874835bff5b684fe483ebb3ed`](https://github.com/vialdjoukang-spec/Medina/commit/77f194bef28bdd4874835bff5b684fe483ebb3ed) du 15 octobre 2026 à 21:53 Europe/Zurich, sur `medina/7-starter-codex`, **retire** le fichier de cet arbre-là. Le blob retiré est `e37960f8afb53c6c1a651d7e0a690cdafb040d9d`, l’état de 14:07. Cette suppression n’est pas une version plus récente du texte de 14:29.

## Documents seuls sur une histoire séparée

La branche `medina/alpha77-chainage` n’a pas d’ancêtre commun avec `main`. Son commit [`e8a79c57dc51643a1c9df21d871a92e9dafe111f`](https://github.com/vialdjoukang-spec/Medina/commit/e8a79c57dc51643a1c9df21d871a92e9dafe111f) du 16 octobre 2026 à 18:02 UTC porte des textes datés du 16 octobre qui ne sont pas dans `main` et ne sont pas copiés ici :

- [AGENT_LECON.md](https://github.com/vialdjoukang-spec/Medina/blob/e8a79c57dc51643a1c9df21d871a92e9dafe111f/AGENT_LECON.md), blob `9e6920e066ec07ef9e88d7bf870a33e5cb894783`
- [EXIGENCE_CALCULS.md](https://github.com/vialdjoukang-spec/Medina/blob/e8a79c57dc51643a1c9df21d871a92e9dafe111f/EXIGENCE_CALCULS.md), blob `7183d40cafe362fae7e8b5ce06b88ae7e5de0f5c`
- [EXIGENCE_SEMIOLOGIE.md](https://github.com/vialdjoukang-spec/Medina/blob/e8a79c57dc51643a1c9df21d871a92e9dafe111f/EXIGENCE_SEMIOLOGIE.md), blob `1d19c5bc9491543d9c8fc3c4fe6af9ac28ca332d` — diagnostic du 15 octobre, distinct du YAML de sémiologie ci-dessus

## Références anciennes encore présentes

`docs/alpha/PROMPT_MEDINA_Alpha.md` s’arrête au commit [`aa01220a337a7f59e0d7c7a428c840825f8b6256`](https://github.com/vialdjoukang-spec/Medina/commit/aa01220a337a7f59e0d7c7a428c840825f8b6256) du 26 septembre 2026. Le prompt maître en vigueur est celui du 13 octobre. Les rapports de livraison qui citent `test_preview.py` comme contrôle de navigateur décrivent l’outil legacy, pas `test_v7.py`.
