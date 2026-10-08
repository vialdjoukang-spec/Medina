# Déploiement E2 — I83 — Varices des membres inférieurs (C-01-Cardiologie)

Vérification terminée le 8 octobre 2026 à `2026-10-08T10:25:22.499583+00:00`. **La qualification canonique E2 est publiée au SHA `8d6deeeec54a5557fe93dcea6f6c6e6543e09d83`. Le workflow Pages et son déploiement ont réussi ; le global et S01 publics contiennent exactement la nouvelle phrase.** Les fichiers historiques [DEPLOIEMENT.md](DEPLOIEMENT.md) et [DEPLOIEMENT.json](DEPLOIEMENT.json), relatifs à `72ccab4e`, sont conservés. [Preuves E2 détaillées](DEPLOIEMENT_E2.json).

## Provenance et exécution GitHub

- [Commit E2](https://github.com/vialdjoukang-spec/Medina/commit/8d6deeeec54a5557fe93dcea6f6c6e6543e09d83) : `8d6deeeec54a5557fe93dcea6f6c6e6543e09d83` ; `main` à la dernière lecture API : `8d6deeeec54a5557fe93dcea6f6c6e6543e09d83`.
- Depuis `72ccab4e`, seule la source `chapters/I83/I83_d.html` change dans le périmètre du chapitre. Son SHA-256 est `72a6ddb28a8379f9ab54323d3323220e3f4f102129f1f948d5ccf8c58c5b0e06`. Les neuf autres sources et `chapters.json` sont inchangés.
- [Workflow Pages 37762436051](https://github.com/vialdjoukang-spec/Medina/actions/runs/37762436051) : `completed / success`, SHA exact `8d6deeeec54a5557fe93dcea6f6c6e6543e09d83`, mise à jour terminale `2026-10-08T10:18:22Z`. Le statut terminal a été lu sur [l’API directe du run](https://api.github.com/repos/vialdjoukang-spec/Medina/actions/runs/37762436051) ; la première liste des runs conservait encore un état `queued`.
- [Build](https://github.com/vialdjoukang-spec/Medina/actions/runs/37762436051/job/113261861513) et [deploy](https://github.com/vialdjoukang-spec/Medina/actions/runs/37762436051/job/113262229283) : tous deux terminés avec succès. [Statut exact du déploiement 6932927658](https://api.github.com/repos/vialdjoukang-spec/Medina/deployments/6932927658/statuses/19453439289) : `success`, enregistré à `2026-10-08T10:18:22Z` pour le même SHA.

## Vérification du site public et de son artefact

L’index, [MEDINA global](https://vialdjoukang-spec.github.io/Medina/MEDINA.html) et [C-01-Cardiologie](https://vialdjoukang-spec.github.io/Medina/fragments/MEDINA_S01_cardiovasculaire.html) répondent HTTP 200. Les trois documents téléchargés sont identiques octet pour octet aux fichiers correspondants de [l’artefact Pages 11542618469](https://api.github.com/repos/vialdjoukang-spec/Medina/actions/artifacts/11542618469), rattaché au run et au SHA E2. Le ZIP fait `13665194` octets ; son SHA-256 `3be476e90e3eef1acc67301432e2e56fecbf1c86fc6864b3ee6f2fee81b2174a` correspond au digest annoncé par GitHub.

| Document public | SHA-256 réel |
| --- | --- |
| MEDINA global | `dec7e38f8ed85e4db0d882ec264f0df68682410ca846b72fe83fa8f56e97fd1f` |
| C-01-Cardiologie | `129337ae3058e959dd2b5fb089107aa820d7b4e763ca38f0ed05b2067b95bcab` |

Le payload `mdn-pack` des documents publics a été décodé par `base64` et `gzip` de la bibliothèque standard, puis le texte du template `ch-I83` a été lu par `HTMLParser`, sans exécuter son code. **La phrase exacte suivante est présente dans le cours I83 du global et de S01 réellement servis :**

> Cette conduite est l’instruction propre à ces deux produits, non une recommandation fondée sur des essais : l’avis immédiat du chirurgien vasculaire et le protocole local d’urgence ischémique priment.

Cette lecture confirme que le public reçoit la qualification E2, au-delà de la seule présence du commit sur GitHub.

## Portée des contrôles

Les routes publiques restent [I83 — Varices des membres inférieurs (C-01-Cardiologie)](https://vialdjoukang-spec.github.io/Medina/fragments/MEDINA_S01_cardiovasculaire.html#/entry/I83) et [I87 — Autres atteintes veineuses (C-01-Cardiologie)](https://vialdjoukang-spec.github.io/Medina/fragments/MEDINA_S01_cardiovasculaire.html#/entry/I87), alias du cours primaire I83. Les 41 interactions ne sont pas rejouées dans ce contrôle de publication. Le coordinateur rapporte pour la copie E2 1 923 contrôles natifs et 41 contrôles de routes réussis ; cette attribution est séparée de nos preuves indépendantes GitHub, artefact et HTTP.

La limite de navigation HTTPS directe de Chromium, `ERR_CERT_AUTHORITY_INVALID`, est documentée dans le rapport précédent ; elle n’a été ni contournée ni retestée ici. Ce rapport atteste la version et les octets publiés, ainsi que le texte du cours décodé. Il ne constitue pas une nouvelle relecture médicale ou une déclaration de complétude du fragment. Aucune mutation Git ni canonique : seuls les deux rapports E2 ont été écrits dans le dépôt.
