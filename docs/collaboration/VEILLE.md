# Veille croisée Claude ↔ Codex

Consigne de Vial du 8 octobre 2026 : chaque agent détecte sans délai le travail de l'autre, pour l'auditer et le recevoir.

## Mécanisme

1. **Commande commune** : `python3 tools/veille_collaboration.py --agent <Claude|Codex> --attendre 300`. Toutes les cinq minutes, elle récupère les branches distantes. Elle s'arrête avec le code 10 dès qu'une branche de l'autre agent (`codex/…` ou `claude/…`), `main` ou la branche d'intégration change. Elle liste alors les commits et les fichiers modifiés, classés en livraisons, reçus, chapitres, consignes, organisation et glossaire. Lancée en arrière-plan, elle réveille la session. Elle ne fusionne, n'injecte et ne publie rien.
2. **Signal de remise** : chaque agent tient à jour, sur sa branche, `docs/collaboration/SIGNAUX_<AGENT>.json`. Ce fichier liste ses lots prêts pour l'audit croisé, avec le code et l'intitulé du chapitre, le dossier de remise, le commit exact et l'état (`pret_audit`, `corrige`, `recu`, `injecte`). Un changement de ce fichier déclenche la veille de l'autre agent.
3. **Événements GitHub** : Claude est abonné à l'activité des PR #12 (ses remises) et #13 (intégration Codex). Un commentaire, une revue ou une poussée le réveille.

## Conduite à la détection

- **Remise de l'autre agent** : auditer au commit exact les quatre onglets, les fenêtres, les sources et le glossaire, puis publier le rapport d'audit sur sa propre branche et mettre son fichier de signaux à jour.
- **Reçu ou injection** : relire le reçu, intégrer la branche d'intégration et refaire les contrôles du chapitre.
- **Consigne** : la lire avant toute autre action.

Le cahier des charges du 8 octobre réserve à Codex l'injection dans la branche d'intégration : Claude ne pousse jamais sur une branche Codex.
