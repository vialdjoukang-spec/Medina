# MEDINA — coordination des 22 fragments

Instruction reçue le **8 octobre 2026** : Vial demande de lire `Prompt_Codex.pdf` et de continuer. Le [protocole actif](docs/collaboration/PROTOCOLE_FRAGMENTS_2026-10-08.md) remplace les règles incompatibles de progression par remise d’un chapitre, d’audit après injection et de réouverture après injection. L’arrêt Codex antérieur est levé par cette demande de reprise. Les veilles automatiques restent en pause.

**Unité de remise : fragment entier achevé et auto-revu. Audit croisé : un tour, puis corrections et injection par l’autre IA. Statut INJECTÉ : immuable. Sortie : HTML clair uniquement. Arrêt définitif après les 22 fragments rédigés, auto-revus, audités et injectés.**

Les attributions existantes restent conservées. Le registre technique est [production_plan.json](organisation/production_plan.json) ; les états et preuves finaux sont [fragment_status.json](organisation/fragment_status.json). La cardiologie conserve son partage historique : l’injection d’I83 isolé ne vaut pas injection définitive de C-01-Cardiologie.

| Rang | Fragment | Producteur | Auditeur final |
| --- | --- | --- | --- |
| 01 | C-01-Cardiologie | Partage historique Codex / Claude | À fixer pour la remise finale historique |
| 02 | P-02-Pneumologie | Claude | Codex |
| 03 | I-03-Infectiologie | Codex | Claude Code |
| 04 | G-04-Gastroentérologie et hépatologie | Claude | Codex |
| 05 | N-05-Neurologie | Codex | Claude Code |
| 06 | E-06-Endocrinologie et métabolisme | Claude | Codex |
| 07 | N-07-Néphrologie | Codex | Claude Code |
| 08 | H-08-Hématologie | Claude | Codex |
| 09 | O-09-Oncologie, génétique médicale et soins palliatifs | Codex | Claude Code |
| 10 | G-10-Gynécologie et sénologie | Claude | Codex |
| 11 | O-11-Obstétrique et néonatologie | Codex | Claude Code |
| 12 | M-12-Médecine des âges de la vie | Claude | Codex |
| 13 | I-13-Immunologie et allergologie | Codex | Claude Code |
| 14 | R-14-Rhumatologie et orthopédie | Claude | Codex |
| 15 | U-15-Urologie et andrologie | Codex | Claude Code |
| 16 | D-16-Dermatologie | Codex | Claude Code |
| 17 | O-17-Oto-rhino-laryngologie et médecine bucco-dentaire | Claude | Codex |
| 18 | O-18-Ophtalmologie | Claude | Codex |
| 19 | M-19-Médecine d’urgence, traumatologie et toxicologie | Claude | Codex |
| 20 | D-20-Diagnostic clinique et examens complémentaires | Codex | Claude Code |
| 21 | M-21-Médecine de premier recours et santé publique | Codex | Claude Code |
| 22 | E-22-Éthique médicale, droit et communication | Claude | Codex |

## Reprise effective

**I-03-Infectiologie (T1)** reste le fragment actif Codex, avec **A41 — Sepsis et choc septique de l’adulte (I-03-Infectiologie)** en reprise interne. Le catalogue historique comprend 155 catégories locales et un seul cours déclaré : cet inventaire n’établit pas la couverture CIM-11. Les remises A41 et J45 antérieures dans l’espace partagé sont conservées avec leurs empreintes ; leur ancien statut `a_auditer` ne constitue plus un ordre d’audit final de fragment.

Aucun des 22 fragments n’est marqué INJECTÉ à cette reprise : les preuves requises de complétude et d’audit final du fragment entier manquent. Cela conserve les injections historiques de cours sans leur attribuer une portée nouvelle. Les rapports et corrections internes restent publiables comme travail en cours, sans transmission pour audit final avant achèvement.

Une contribution concurrente a ensuite injecté **le chapitre A41**, après audit Claude `ba6a80f`, au commit `a5563238887df2a72da7a9f663bdae9ab01f4bc8` selon les règles administratives précédentes. Ces corrections sont préservées dans la base de reprise. Elles ne valent ni audit final ni injection du fragment entier ; les nouvelles améliorations A41 restent dans une copie interne.
