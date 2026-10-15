---
name: image-clo-finder
description: Chercher des images médicales réelles, sourcées et licenciées (Wikimedia Commons, Europe PMC) pour remplacer une figure anatomique dessinée par IA dans une leçon MEDINA S08/S05/S04/S06, via le moteur commun Image_Codex_Finder (courtier, cache et budget partagés). Usage /image-clo-finder <CODE> [requête].
---

# Image_Clo_finder (Claude)

Règle de Vial (15.10.2026) : un schéma de structure anatomique dessiné par IA, SVG compris, n'est **pas recevable** (constat MAJEUR) ; on le remplace par un **original existant** sourcé. Jamais de génération, de redessin ni d'import automatique. Lire `docs/collaboration/instructions/FIGURES_ANATOMIQUES_IA_2026-10-15.md`.

1. **Inventaire hors ligne** : `python3 tools/image_clo_finder.py inventory <CODE>`. Ouvrir chaque figure ; classer `ANATOMIQUE_IA`, `SCHEMA_NON_ANATOMIQUE` ou `IMAGE_SOURCEE`. Une origine inconnue reste une réserve.
2. **Recherche sobre** : toujours par le courtier unique de la machine.
   - Le coordinateur lance une seule fois : `python3 tools/image_codex_finder.py --daily-budget 60 serve` (127.0.0.1:8765).
   - Chaque agent : `python3 tools/image_clo_finder.py candidates "<anatomie en anglais> Gray" --broker http://127.0.0.1:8765`, puis `--provider europepmc` pour découvrir des articles.
   - Une requête précise par figure ; aucune boucle ; une erreur (délai d'attente, budget, courtier absent) ⇒ autre fournisseur ou lacune déclarée, jamais de contournement direct.
   - `python3 tools/image_clo_finder.py status` montre délais d'attente et budget.
3. **Contrôle humain requis** : ouvrir page et original, vérifier anatomie et légende, origine humaine, licence propre à la figure (pas celle de l'article), attribution. `publication_ready` reste `false`.
4. **Écriture** : seul un rôle autorisé par une mission approuvée dans `main` peut modifier `chapters/` ; l'audit écrit seulement son rapport (clé `figures`, avec candidats et attribution proposée).
