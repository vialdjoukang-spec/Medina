# A04 — revue technique indépendante de l’assemblage

Date : 8 octobre 2026. Sources examinées en lecture seule : `/workspace/work/medina-resume/livraisons/Livraison Codex/I-03-Infectiologie/travail/PRODUCTION_FRAGMENT_2026-10-08/sources/chapters/A04/`, `sources/glossary/a04.py` et `manifest_interne.json`. Aucun fichier du dépôt n’a été modifié par cette revue.

## Résultat

**Aucun défaut bloquant de structure HTML détecté.** Le preview T1 a été construit avec A04 vers `/workspace/work/a04-preview-check/infectiologie-A04.html`, hors dépôt. Le builder a déclaré 7 cours (`A41`, `B24`, `B18`, `A54`, `A53`, `B50`, `A04`) et 518 fenêtres dans le pack ; ce contrôle technique ne vaut pas validation médicale.

| Contrôle | Résultat |
|---|---|
| Fragments concaténés `a+b+c+d` | Balises équilibrées ; un `template id="ch-A04"` fermé. |
| Panneaux | `pA`, `pE`, `pS`, `pP` uniques, avec quatre boutons correspondants. |
| Plan et ancres | 14 îlots du cours, 5 des examens, 6 des sciences et 5 de pharmacologie ; 24 ancres de navigation avec cibles présentes ; aucun identifiant dupliqué. |
| Sous-onglets scientifiques | 6 boutons `data-s` reliés aux 6 `div.sci` : anatomie, histologie, physiologie, microbiologie, immunologie, génétique. |
| Fenêtres A04 | 33 appels `data-k`, 34 définitions `data-pop` ; tous les appels sont résolus, aucune clé dupliquée dans A04 ni collision avec les autres chapitres du paquet. |
| Quiz | 5 quiz dont 3 dans `pE` ; chacun possède une seule option `data-ok="1"`, au moins une option `data-ok="0"` et un retour `p.fb hidden`. |
| Classes et placeholders | Classes limitées au contrat `PROMPT_MEDINA.md` ; aucune marque `⟦…⟧` restante. La formule clinique « à compléter » en `pE` décrit une donnée patient inconnue, pas un emplacement éditorial. |
| Manifeste | A04 est le dernier chapitre, `covers=["A04"]` ; les 7 HTML requis et `glossary/a04.py` sont présents et leurs 8 SHA-256 concordent. Les trois statuts finaux restent `false`. |

## Points à nettoyer

1. **Fenêtre orpheline, non bloquante :** `a04-s-detail` reste dans `A04_pop1.html` mais aucun bouton du chapitre ne l’appelle. La supprimer ou créer un renvoi seulement si son contenu apporte réellement une explication utile. Les huit fichiers du manifeste et le preview doivent alors être recalculés.
2. **Provenance du preview :** le manifeste conserve `source_commit=ab1faa4487b48b132a5a8c7700d51109e80f1150`, antérieur aux nouvelles sources A04 et différent du HEAD actuellement vu (`8a9ca096af01f767e258fadfc8f85763a02dfd9b`). Le champ passe la validation technique parce qu’il exige seulement une chaîne non vide, mais il ne prouve pas le commit des fichiers A04. Actualiser avec le commit contenant le paquet figé avant d’exposer cette provenance comme SHA source.

Le constructeur vérifie le pack et les panneaux, mais ne vérifie pas la justesse des contenus, les doses, les liens externes ni les actions au clic dans un navigateur. La correction clinique et l’aperçu visuel restent des contrôles séparés.
