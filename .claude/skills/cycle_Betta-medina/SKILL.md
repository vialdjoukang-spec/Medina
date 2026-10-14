---
name: cycle_Betta-medina
description: Chaîne complète d'un cycle Betta MEDINA (cycles 31+, 8 Leçons Examen fédéral, 4 agents × 2 leçons, recherche Opus 5.5 puis rédaction Sonnet 5.5). Usage : /cycle_Betta-medina <n|suite>
---

# Cycle Betta MEDINA — chaîne, cahiers des agents, preuves

**Source de vérité du plan** : `organisation/progression/plan-betta-cycles.json` (PDF/HTML associés, construits par `python3 tools/build_betta_plan.py --pdf`). Cycles 31 → 47, 130 leçons fédérales (étoile SSP/PROFILES) des fragments N-05-Neurologie, E-06-Endocrinologie et métabolisme, N-07-Néphrologie, H-08-Hématologie, non programmées dans les cycles 1–30.
**Registre + jauge** : `organisation/betta_status.json` ; jauge verte permanente `tools/betta_jauge.py` (ligne d'état `.claude/settings.json`, coût nul). États : `A_FAIRE` → `LIVRE` (dépôt sous livraisons) → `INJECTE` (après autorisation de la garde).

## Chaîne d'un cycle `n`
1. Lire le cycle `n` dans le plan : 4 agents (`C<n>-A<k>-<TAG>`), 2 leçons chacun, un seul fragment par agent.
2. Pour chaque agent, en parallèle ; pour chaque leçon, **l'une après l'autre** :
   a. **Recherche — Opus 5.5** (cahier R ci-dessous) → `recherche.md` + `sources.json`.
   b. **Rédaction — Sonnet 5.5** (cahier W) → fichiers du chapitre + `rapport.md`.
3. **Publication du cycle** : registre (`LIVRE` + empreintes), commit, push sur la branche `claude/*` de la session.
4. Jauge cochée automatiquement (lecture du registre). Cycle suivant.
**Pas d'audit** dans cette série : audit différé, jamais déclaré réalisé.

Dossier d'une leçon : `livraisons/Livraison Claude/<libellé du fragment>/betta/CYCLE_<n>_<CODE>/`
contenant `recherche.md`, `sources.json`, `chapters/<CODE>/<CODE>_a.html … _d.html`, `_pop1.html`, `_pop2.html`, `glossary/<code>.py`, `rapport.md`.

## Cahier R — agent de recherche (Opus 5.5)
- Lire `PROMPT_MEDINA.md` §4, §10–11, `docs/STYLE_REDACTION.md`, la ligne de la leçon dans le plan (titre OFS, bloc, sources visées) et la liste des sous-codes CIM-10-GM (`nosology/fragments/<FID>.json`).
- Rechercher et **lire réellement** (WebSearch/WebFetch, PubMed) : sources suisses d'abord (Swiss Medical Forum, sociétés suisses, OFSP, Suva), puis européennes (EAN, ESE, ERA, EHA, ESMO, ESC…) ; **aucune recommandation américaine** comme fondement d'une conduite. Médicaments : information professionnelle Swissmedic (`python3 tools/swissmedic_fi.py`, AIPS, Compendium) lue et datée.
- Produire `recherche.md` : plan monographique (question clinique, définition, classifications, épidémiologie, mécanismes normal → pathologique, causes, anamnèse, examen, diagnostic et différentiel, urgences, prise en charge suisse, suivi, situations particulières, critères formels, paramètres clés), chaque fait suivi de sa référence ; sous-codes couverts ; lacunes explicites.
- `sources.json` : liste {url, titre, éditeur, version/année, date de consultation, section/page, population, limites}.
- Interdit : toute affirmation de mémoire ; une source introuvable reste une lacune.

## Cahier W — agent de rédaction (Sonnet 5.5)
- Modèles structurels : `chapters/N17/` et `chapters/D50/` + `glossary/n17.py`, `glossary/d50.py` ; contrat `CHAPTER_SPEC.md` (§2–3, contrôles pré-livraison) et `PROMPT_MEDINA.md` §4 (classes de la liste fermée, identifiants préfixés par le code en minuscules, clés de fenêtres `<code>-…`, Pareto `pareto-<code>-…`).
- Quatre onglets : Pathologie (pA), Examens (pE), Sciences (pS), Pharmacologie (pP) ; dernier îlot de la pathologie = critères formels (`div.alert`) puis paramètres clés (`div.key`) ; Pareto en fin de grande partie ; fenêtres explicatives sur mots interactifs ; tableaux introduits et commentés.
- Français professionnel, merveilleux à lire, phrases complètes, sans remplissage ni métaphore ; chaque affirmation justifiée (mécanisme → conséquence → décision) et rattachée à une source du dossier ; aucune donnée absente du dossier.
- Glossaire : chaque abréviation définie lettre à lettre (`a(...)`).
- Auto-contrôle : HTML bien formé, identifiants uniques et préfixés, toute clé de fenêtre référencée existe, aucune abréviation hors glossaire. Rapport `rapport.md` : fichiers, tailles, sources utilisées, lacunes, mention « Audit différé — revue IA, distincte d'une validation médicale humaine ».

## Commandes de preuve
```bash
python3 tools/build_betta_plan.py --pdf          # plan, HTML, PDF
echo '{}' | python3 tools/betta_jauge.py          # jauge
sha256sum "livraisons/Livraison Claude/"*/betta/CYCLE_<n>_*/chapters/*/*   # empreintes livrées
python3 -m unittest discover -s tests -p 'test_*.py'
python3 tools/espace.py garde origin/main HEAD    # la garde actuelle refuse toute injection hors cycle 1/plan 1–30
```

## Injection canonique (bloquée tant que Vial n'a pas autorisé la garde)
La garde `tools/espace.py` (via `tools/cycle1_claude.py` et `tools/night_cycle.py`) refuse toute nouvelle ligne `chapters.json` hors Cycle 1 et plan 1–30. L'injection Betta (copie vers `chapters/`, ligne `chapters.json` `integrated: true, production_cycle: n, provisional_injection: true, audit_status: "audit_differe_non_effectue"`, mise à jour de `nosology/integrity.json`, `python3 build_front.py --all-fragments`, push `main` → `pages.yml`) exige une extension de garde explicitement autorisée par Vial. Ne jamais désactiver une garde pour contourner un refus.

## Veille post-limite d'usage
Si la limite d'usage interrompt le flux : relancer le workflow avec `resumeFromRunId` (les agents terminés sont restitués du cache), puis reprogrammer une veille (`send_later`) au prochain réarmement.
