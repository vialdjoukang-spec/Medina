# Règle administrative du propriétaire — MEDINA (Claude et Codex)

Cette règle prime sur toute consigne antérieure de progression, d'audit, d'injection et de rédaction. Elle s'impose à Claude et à Codex. `REGLES_INJECTION_CLAUDE.md` et `FILE_AUDIT_CODEX.json` sont remplacés.

## 1. Vitesse : aucune IA n'attend l'autre
- Chaque IA produit sa file de fragments à son rythme. Un chapitre terminé est déposé dans l'espace partagé ; son auteur passe aussitôt au chapitre suivant.
- Parallélisme : plusieurs sous-agents dans un même chapitre (catégories, onglets ou sections), un seul auteur par fichier.
- Stratégie : produire d'abord tout le fragment au **niveau de base**, ensuite enrichir les leçons que le propriétaire désigne après lecture de l'aperçu.

## 2. Espace partagé et audit croisé unique
- `espace_partage/COURS_CLAUDE_A_AUDITER_PAR_CODEX/<CODE>/` : Claude dépose, Codex audite.
- `espace_partage/COURS_CODEX_A_AUDITER_PAR_CLAUDE/<CODE>/` : Codex dépose, Claude audite.
- **Un seul audit croisé suffit.** L'auditeur corrige lui-même sur place ce qui doit l'être, puis enregistre son verdict. Il ne renvoie pas le chapitre et ne bloque pas l'auteur.
- **Interdiction absolue** : aucune IA n'injecte un cours non audité, ni un cours qu'elle a seulement audité elle-même. L'injection exige un verdict favorable de l'**autre** IA portant sur les empreintes exactes des fichiers.
- Toutes les opérations passent par `tools/espace.py` : `deposer`, `ouvrir`, `auditer`, `injecter`. La vérification `garde-espace` rejette toute modification des sources canoniques sans audit croisé correspondant.
- Une erreur médicale démontrée après injection se corrige en priorité, par un nouveau dépôt.

## 3. Niveau de base d'une leçon
Quatre onglets (Pathologie, Examens, Sciences, Pharmacologie) avec l'essentiel pour l'examen fédéral. Chaque affirmation est justifiée et sourcée par la recommandation la plus récente. Critères formels, puis paramètres clés en dernier îlot. Pareto en fin de partie, deux quiz, glossaire complet (sigles `{}`).

## 4. Rédaction
- Français professionnel, phrases complètes, aucun remplissage ni plafond de mots arbitraire.
- **Tableaux** seulement quand ils sont pertinents (classifications, énumérations, comparaisons) : cellules brèves et cohérentes, lecture intuitive, tableau introduit et commenté.
- **Contentieux de sources** : le référentiel le plus récent l'emporte dans le texte. La version antérieure ou divergente reste accessible, datée, dans une fenêtre ouverte par un mot vert. Les précisions complémentaires vont de préférence dans une fenêtre.

## 5. Sources suisses (Compendium)
- Toute posologie, contre-indication, interaction ou autorisation suisse vient de l'information professionnelle suisse : page `https://compendium.ch/fr/product/<id>-<nom>/mpro`, ou `node tools/compendium_fi.cjs "<produit>" <section>`.
- Citation : « Information professionnelle suisse, compendium.ch, <produit>, consultée le <date> ».
- Les passages concernés sont marqués dans `chapters/<CODE>/<CODE>_compendium.json`. S'il existe, `tools/compendium_zones.py verifier <CODE>` doit réussir avant l'injection.

## 6. Visibilité
L'aperçu interactif des cours déposés est tenu à jour pour le propriétaire. Toute remise, tout audit et toute injection sont signalés avec le code, l'intitulé complet et le fragment.
