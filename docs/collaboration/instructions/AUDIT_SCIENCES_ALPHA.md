# Contrôle technique des sciences Alpha

Mission `ALPHA77-CODEX-OUTIL-SCIENCES`, génération 1. Aucun contenu médical ni ancien système n’est modifié par ce correctif.

Exécuter dans le worktree source réservé, avec le **SHA40 exact approuvé de comparaison**, transmis par Starter dans son prompt :

```sh
python3 tests/audit_sciences.py --base SHA40_EXACT --codes I63 --out work/sciences.json
```

Remplacer `SHA40_EXACT` et les codes par les valeurs réelles. Branche, `HEAD`, SHA abrégé et objet Git autre qu’un commit sont refusés. Le rapport conserve cette base et mesure les octets de chaque `_c.html` réellement lus dans ce commit. Il ne remplace jamais une source absente par une ancienne base ni par une exemption de code. Une comparaison impossible reste un échec et `before: null`, sans inventer une valeur zéro.

Une absence n’est recevable que pour une nouvelle production déjà approuvée dans `.medina/7-starter-codex.json` **à cette base** : entrée `mode: production`, mission `PRODUCE` active d’intégration du même code/acteur à cette base, reçu au chemin configuré portant `complete: true`, la même mission et les empreintes exactes des sept fichiers courants obligatoires. Seuls les assets propres `assets/img/code/alpha/codex/` peuvent compléter cet inventaire. Les anciennes listes d’exemption sont supprimées. Ce reçu explique une absence historique ; il ne constitue aucune validation médicale ni clôture.

Chaque discipline conserve au moins 280 mots, une figure avec une légende non vide et un média accessible : SVG `role="img"` nommé par `aria-label` ou `aria-labelledby` résolu, **ou** image originale `<img src="…" alt="…">` avec valeurs non vides. Les boutons `data-s` doivent correspondre aux disciplines locales sans cible absente ni doublon. Les quatre liens didactiques demeurent obligatoires : « Science → clinique. », « Science → examen. », « Science → traitement. », « À retenir. ».

Ces vérifications de structure ne prouvent ni la qualité pédagogique, ni la licence, ni la provenance humaine, ni la justesse d’une figure. Les structures anatomiques générées/dessinées par IA restent interdites, SVG compris. La sémiologie clinique et le premier sous-onglet « Sémiologie fondamentale et analytique » suivent leur contrat distinct ; leur présence seule ne valide aucun fait médical. Ne pas produire de remplissage pour franchir le seuil technique.

Vérification isolée, sans lancement d’IA ni réaudit des cours :

```sh
python3 -m unittest discover -s tests -p test_audit_sciences.py -v
python3 -m unittest discover -s tests -p test_starter_codex.py -v
```
