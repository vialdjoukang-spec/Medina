# Publication en l’état et parité administrative — 15 octobre 2026

Cette instruction transcrit la demande actuelle de Vial : prendre connaissance des quatre systèmes actifs et publier leurs cours tels qu’ils existent, y compris les cours en cours ; lever les restrictions administratives incompatibles et corriger les problèmes techniques et de branches sans modifier les contenus ; placer Codex et Claude à égalité, avec le pouvoir administratif maximal du projet et le même droit de veto partout.

## Autorité commune sur tout MEDINA

Codex et Claude disposent des mêmes autorisations locales de lecture, organisation, revue, maintenance technique, gestion des branches, intégration et publication dans MEDINA. Aucun des deux n’est supérieur à l’autre. Les mentions historiques « Claude Leader », « Codex arrêté », les affectations exclusives d’injection et les restrictions par préfixe de branche ne confèrent plus un pouvoir administratif supérieur. Les attributions d’auteur décrivent la provenance et la coordination du travail ; elles ne créent aucun privilège administratif. Chaque fichier conserve un seul auteur à la fois pour éviter les conflits.

Cette autorité est une règle du projet. Les rôles du compte propriétaire, des collaborateurs et des installations GitHub Apps demeurent ceux accordés réellement par GitHub. Un fichier du dépôt n’octroie aucun accès API, rôle administrateur ni contournement de protection. Une restriction de plateforme reste un blocage réel à signaler. L’instruction humaine la plus récente prime ; aucun veto IA ne peut annuler une instruction humaine explicite applicable.

## Opération actuelle : quatre systèmes, contenus inchangés

L’opération d’assainissement et de publication couvre Neurologie (S08 / N-05), Endocrinologie et métabolisme (S05 / E-06), Néphrologie (S04 / N-07) et Hématologie (S06 / H-08). Elle autorise la publication de toutes les sources existantes de ces quatre systèmes, même incomplètes, sans réécriture médicale. Elle ne lance aucune production médicale nouvelle ailleurs.

Les anciens STOP, fenêtres horaires expirées, obligations de cycle terminé, audits médicaux préalables, réserves et scellements incompatibles ne bloquent pas cette publication en l’état. Leurs documents, preuves, auteurs et statuts historiques restent conservés. Un cours publié en cours conserve un statut provisoire explicite ; aucun audit, contre-audit, contrôle, clôture de cycle ou validation humaine manquant n’est déclaré accompli. Les contrôles techniques de construction, de liens, d’intégrité et de déploiement restent applicables.

Le chemin contrôlé est `organisation/PUBLICATION_EN_ETAT_2026-10-15.json` et `tools/publication_en_etat.py` : périmètre des quatre fragments, empreinte de chaque source publiée, chemin et SHA du vrai commit de provenance, égalité exacte des octets, catalogue provisoire, préservation des registres historiques. Les contrôles de publication ne transforment pas une preuve historique en preuve renouvelée. Le Prompt médical et les rapports d’audit antérieurs conservent leurs empreintes.

## Veto symétrique et traçable

Codex et Claude peuvent chacun inscrire un veto motivé dans `organisation/governance_events.jsonl`, sur un chemin, un répertoire ou tout le projet (`*`), pour les modifications (`change`), les publications (`publish`) ou les deux. Les règles sont identiques pour les deux IA. Le journal est append-only. Une IA peut lever son propre veto ; elle ne peut lever celui de l’autre. Une instruction humaine explicite applicable permet la levée, avec chemin et empreinte de l’instruction conservés. La levée se fait dans un commit distinct de l’opération concernée.

Exemples : `python3 tools/project_governance.py veto --actor Codex --scope '*' --reason 'Motif précis'` ; `python3 tools/project_governance.py release --actor Codex --veto-id IDENTIFIANT --reason 'Motif résolu'`. Claude utilise exactement les mêmes commandes avec `--actor Claude`.

La garde du dépôt vérifie les veto sur les modifications ; le workflow Pages vérifie ceux sur la publication avec `python3 tools/project_governance.py check --revision HEAD --operation publish`. Le nom d’auteur du journal est déclaratif : il ne prouve pas l’identité d’une session ou d’un compte GitHub. Le journal, les workflows et les contrôles locaux sont modifiables par quiconque possède l’accès d’écriture. Sans protection GitHub imposée et identités distinctes vérifiées, ce veto reste un mécanisme de collaboration contrôlé dans ces chemins, pas une interdiction GitHub inviolable de toute action externe.

## Ordre de lecture et historique

Lire cette instruction avant les anciennes règles de leadership, STOP, injection et cycles. Elle remplace leurs dispositions incompatibles dans les périmètres définis ci-dessus. Les règles médicales et les preuves historiques restent lisibles et ne valent pas ordre de réécriture dans cette mission. Ne pas relancer une veille ou un automate persistant sans demande actuelle correspondante.
