# C-01-Cardiologie — intégration provisoire avec réserves

Instruction directe de Vial, le 8 octobre 2026 :

> Ecoute, corrige les zones à corriger et injecte moi cela de manière immédiate. On doit progresser.

> Si une Partie est bloquée, introduit là quand même, mais met là en rouge détectable par claude... quand on aura la possibilité, lui même interviendra... et ceci n'est valable pour des cas délicat. On doit progresser.

Cette décision autorise une exception ciblée pour les apports C-01 de la PR #16. Elle permet des tranches provisoires contrôlées. Elle ne transforme pas une contrelecture ciblée en audit final du fragment. Les autres fragments, les attributions, les chapitres actifs et les verrous des fragments INJECTE restent inchangés.

## Application

- Corriger les erreurs établies dans les copies adaptées. Conserver les originaux Claude et leurs empreintes.
- Rendre les réserves délicates visibles en rouge, avec un motif précis, un identifiant stable et l'action attendue de Claude.
- Ne pas laisser une posologie non vérifiée ou une conduite dangereuse comme recommandation applicable. Expliquer la limite et la décision spécialisée nécessaire ; la couleur ne valide pas le contenu.
- Réconcilier les sources avec la tête de main. Vérifier chemins, propriété et empreintes. Préserver les contre-corrections existantes.
- Exécuter les tests, l'audit statique, la reconstruction et les contrôles interactifs sur ordinateur et mobile avant publication d'une tranche.
- Enregistrer la provenance, les adaptations et les preuves réelles dans `organisation/provisional_integrations.json`. Ce registre reste append-only.
- L'état est `PROVISOIRE_AVEC_RESERVES`, jamais `INJECTE`. Il ne clôture ni le fragment ni l'audit final et ne certifie pas la CIM-11.

## Première tranche

I51 — Complications des cardiopathies et atteintes cardiaques au cours d’autres maladies (C-01-Cardiologie).

Les huit autres nouveaux cours de la remise restent reçus et archivés ; ils ne sont pas injectés automatiquement avec I51. Les originaux sont dans `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-PR16-95F921F/`.

Claude retrouve les points ouverts par `data-claude-reservation`, `data-reservation-status="open"`, `data-review-owner="Claude"` et les identifiants du registre. Leur levée exige une correction sourcée, l'actualisation des adaptations, de nouvelles preuves et une nouvelle entrée traçable ; aucune suppression silencieuse du reçu historique.

La campagne historique de trente cours 15/15, le backlog cardiologique de vingt cours 10/10 et les attributions des 21 fragments 11 Claude/10 Codex restent distincts et inchangés. J40 — Bronchite conserve son regroupement J20/J40/J41/J42. Le lot ESC2026 n'est pas injecté par cette exception ; ses réserves MED-01, MED-02 et MED-03 ne sont pas réputées levées.
