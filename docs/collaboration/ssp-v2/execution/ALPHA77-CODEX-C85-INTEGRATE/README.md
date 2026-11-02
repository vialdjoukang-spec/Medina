# C85 — version révisée du 2 novembre 2026

Ouvrir `C85-apercu-autonome.html` : leçon native avec deux images originales CC BY 4.0, quatre occurrences et légendes françaises reliées aux repères du scanner et aux panneaux histologiques. Aucun pixel original modifié.

Le plan monographique à 14 points et les 20 rubriques ont une auto-revue attribuée, avec quarante lectures ciblées documentées. Six disciplines scientifiques, neuf sections de sémiologie, 56 fenêtres et cinq quiz. Les limites L1–L6 restent explicites ; aucune validation médicale humaine n’est revendiquée.

`verification.json` et `source-binding.json` rattachent les six étapes réelles (statique, sciences, Betta, construction, assemblage autonome, navigateur) aux octets des sources et de l’aperçu. Les captures finales ont été inspectées. Le test G2 distingue le repère pédagogique de la catégorie rénale du glossaire ; les césures visuelles sont normalisées dans l’assertion, sans retirer ce contrôle.

`reserves.json` garde les sept réserves de la première version et leur résolution documentée. `limitations.json` conserve notamment l’unité hépatique Endoxan inutilisable, la borne doxorubicine, l’absence d’incidence suisse isolée et la portée du codage 2024. Aucun nombre douteux n’est transformé en règle posologique.

## Reproduction

Exécuter `verify_c85.py` depuis ce worktree avec les dépendances de construction Medina, Playwright et Chromium. Dans cet environnement, les dépendances isolées disponibles sont `/tmp/medina-n29-pydeps` (via PYTHONPATH). Le script utilise le moteur natif et le constructeur autonome du harness. Il ne modifie pas les sources médicales, ne pousse pas de branche et ne ferme pas de mission.

Les scripts de migration et d’enregistrement décrivent les décisions de cette reprise. Ne pas rejouer une ancienne migration ou `record_evidence.py` sur une version plus récente : ils ne remplacent pas les sources canoniques ni une nouvelle relecture. `package_revision2.py` vérifie les empreintes avant d’assembler cette revue précise ; il ne génère pas un avis médical.

## Revue et publication

La branche demeure une version de travail pour présentation à Vial. Aucune PR, fusion ou écriture sur main n’a été effectuée. Le reçu `harness-completion.json`, lorsqu’il existe, décrit l’achèvement de projet ; il ne vaut ni publication sur main ni certification clinique. Les compteurs et bandeaux historiques du frontend natif restent ceux de la base et ne remplacent pas l’état du harness.
