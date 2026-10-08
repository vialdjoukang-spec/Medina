# Aperçu interne A41 — I-03-Infectiologie

Fichier auteur unique dans le dépôt : `tools/build_work_preview.py`. Aucun changement de workflow, de source canonique, du registre d’audit ni de l’interface partagée écrit par cet agent.

## Résultat

`/workspace/work/medina-redesign/apercus/infectiologie.html` : 1637654 octets ; SHA-256 `27c1d3a09a3b6f7df09dc4641a16af3692c05fef9f83e615d94fdf3b8f263db9` ; permissions 0644. Un seul cours A41, quatre onglets et 86 fenêtres. HTML avec moteur, styles et Anthropic Serif embarqués ; aucune requête externe nécessaire lors des essais.

Dix sources internes vérifiées par SHA-256 à partir de `livraisons/Livraison Codex/I-03-Infectiologie/travail/FRAGMENT_COMPLET_2026-10-08/sources/` et de son manifeste. Leur base documentaire figée reste `a5563238887df2a72da7a9f663bdae9ab01f4bc8`. Frontend actuel du worktree au-dessus de `baa69c5a96cc7189319b720ad318e62fcdc8a7ee` ; son commit final est coordonné par root.

Le générateur copie un instantané des dix fichiers vérifiés dans un overlay temporaire et réutilise `build_front.py --fragment T1` avec `MEDINA_ROOT` et `MEDINA_OUT`. Les autres fichiers du frontend sont accessibles par liens symboliques en lecture. Les certificats historiques sont désactivés dans le seul `shell/data.py` temporaire. Le carnet d’aperçu possède un espace de stockage distinct. Les temporaires sont nettoyés et la sortie est remplacée atomiquement après contrôles.

Bandeau persistant : « Version de travail · cours en rédaction », intitulé complet et retour `#/home`. Titre navigateur conserve « Version de travail » après changement de route. `window.MEDINA_WORK_PREVIEW` garde les dix empreintes, la base documentaire et `final_validation=false`, `fragment_complete=false`. Le cours interne est ouvrable sans devenir un cours déclaré achevé : `MEDINA_COMPLETE=[]`.

## Contrôles

`functional_check.py` / `functional_check.json` : Chromium système, ordinateur 1440 × 1000 et mobile 390 × 844, préférence système sombre et anciennes clés sombres. Quatre onglets réellement cliqués. Fenêtres `a41-j-gazometrie`, `a41-gaz-read` et `a41-contraste-rein` réellement ouvertes ; valeurs suisses 21,2–27,0 et 22,2–28,3 et source ESUR 2025 accessibles. Police système et taille 21 px appliquées puis retour Anthropic Serif / 17 px. Retour aux catégories par le bandeau. Fonte Anthropic Serif chargée, thème clair, aucun débordement horizontal à l’accueil, zéro erreur JavaScript et zéro demande externe.

Captures : `desktop-reader.png`, `desktop-home.png`, `mobile-reader.png`, `mobile-home.png` dans `/workspace/work/work-preview/`.

`nonmutation.json` : 317 empreintes de sources canoniques et registres comparées avant/après, zéro modification. `rejection_checks.json` : empreinte altérée refusée en conservant la sortie précédente ; sortie dans le dossier canonique `chapters/` refusée. Aucun overlay laissé dans le dossier de sortie.

Ces contrôles portent sur construction et consultation technique. Ils ne constituent pas une nouvelle auto-revue clinique exhaustive, une validation médicale humaine ni l’audit final du fragment entier ; celui-ci reste en production interne.

## Commandes

```sh
python3 tools/build_work_preview.py --output /workspace/work/medina-redesign/apercus/infectiologie.html
python3 /workspace/work/work-preview/functional_check.py
```

Pour CI, après la construction des fragments :

```sh
python3 tools/build_work_preview.py --output dist/apercus/infectiologie.html
```

Route utilisateur proposée : `apercus/infectiologie.html#/entry/A41` ; accueil local de la spécialité `apercus/infectiologie.html#/home`. Aucun workflow modifié par cet agent, aucune transmission pour audit final. Le serveur local de preuve est une aide de test ; il n’entre pas dans le HTML et n’est pas requis pour le site publié.
