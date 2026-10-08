# Alignement Codex sur le cumul transmis par Claude Code

Lecture du 8 octobre 2026. Claude Code a remplacé son premier cumul de 99 lignes, lu au commit `44856ce0f48823455cd7accdf0c1591750d5ccb0`, par une **version exhaustive de 403 lignes**, lue en entier sur la [PR #16](https://github.com/vialdjoukang-spec/Medina/pull/16) au commit `5cebdcc97cc0699dbb7ab9470a613922ce3eecdc`. Le fichier `docs/collaboration/instructions/CUMUL_INSTRUCTIONS_CLAUDE_CODEX.md` possède le blob `9e600398f13642118c54ccb50a42535894dfac92` ; son PDF possède le blob `a8a0fe7dc054bb6586926015a8d88b6620db0830`. Les sections 0 à 21 et les annexes A à C sont inventoriées ci-dessous. Le PDF directement fourni par Vial, `Prompt_Codex.pdf` (SHA-256 `3f6d594119ae4b180a97a544377ebddb3023bc3b9842aed334b0dcbdc985e0f5`), et ses demandes dans la conversation fondent les priorités ; le cumul de Claude est une transmission du projet, et ses affirmations de statut sont vérifiées séparément.

Le contrôle distant a paginé les **20 branches et 15 PR** accessibles, pages suivantes vides. La branche Claude `claude/affectionate-fermi-xpf9yz` au commit `6be5e247e98f3104cb58f6184e409dab3eb1e624` fournit aussi `CONSIGNES_CODEX_2026-10-08.md` et `EXIGENCES_VIAL_2026-10-08.md`. Leurs règles compatibles de sources, de lisibilité et de titres sont retenues. Atkinson reste la police par défaut, sans annuler le choix de police du lecteur ; les titres officiels du catalogue restent exacts. Les anciennes règles de remise par chapitre ou d’injection autonome avant audit ne remplacent pas le PDF directement fourni par Vial.

| Section du cumul exhaustif | Application à cette progression ou limite constatée |
| --- | --- |
| 0. Préséance | Lu ; les demandes directes de Vial et son PDF guident les conflits, avec priorité à l’exactitude médicale. Les prescriptions que Claude déclare lui-même « obligatoires » ne constituent pas à elles seules une nouvelle demande directe. |
| 1. Gouvernance | Lu ; I-03-Infectiologie reste le fragment actif Codex. Aucun cours de Claude n’est réécrit. La remise C-01 de Claude est archivée sur `main` à `7e5a648535164d64638db9bc5a90b0fe5917ec45`, avec réserves médicales et sans injection. |
| 2. Communication | Lu ; état, sources, contrôles et limites sont annoncés en français professionnel sans attribuer à Codex la validation de Claude. |
| 3. Processus | Lu ; la correction B24 demandée par Vial est prioritaire et la production demeure dans I-03. Aucun STOP nouveau n’a été reçu. |
| 4. Organisation | Lu ; le code B24, son intitulé et le fragment I-03 sont conservés ; les identifiants et routes ne changent pas. |
| 5. Complétude CIM | Lu ; les 184 catégories locales T1 et 24 blocs frontend ne prouvent ni un cours par catégorie ni la complétude CIM-11. T1 reste EN_PRODUCTION. |
| 6. Remise et audit | Lu ; les sources B24 restent hors canonique, sans remise finale. L’audit C-01 n’est pas déclaré favorable ; les blocages de son reçu demeurent. |
| 7. Parallélisme | Lu ; B24_a et B24_b ont chacun un auteur, et le coordinateur seul modifie le manifeste et Git. |
| 8. Contrat HTML | Lu ; quatre panneaux, clés interactives et préfixes restent fonctionnels. L’assemblage historique B24 répartit les fermetures de panneaux autrement que le schéma littéral R-8.3 ; une harmonisation éventuelle appartient à la revue du fragment, pas à cette retouche rédactionnelle. |
| 9. Contenu | Lu ; Examens passe de deux à trois quiz, avec résultat hypothétique explicitement indiqué. Les autres exigences de profondeur restent à vérifier pour le fragment entier. |
| 10. Justifications | Lu ; la distinction stade de surveillance / diagnostic clinique et la priorité des urgences sont maintenues dans le texte principal, avec fenêtres liées. |
| 11. Sources | Lu ; CDC 2014 et BfArM 2024 appuient la retouche. Les limites de textes suisses accessibles sont conservées dans les registres B24, sans dose inventée. |
| 12. Style | Lu ; le passage montré par Vial et six autres phrases du même panneau sont repris en phrases cliniques directes. |
| 13. Glossaire | Lu ; aucun nouveau sigle n’est ajouté au quiz, aucune définition globale n’est écrasée. |
| 14. Frontend | Lu ; aperçu clair et isolé, Atkinson par défaut, réglages du lecteur et captures desktop/mobile vérifiés. |
| 15. Bouton fédéral | Lu ; le code de Claude reste sur sa PR. Sa présence fonctionnelle sur l’aperçu I-03 publié n’est pas attestée et sera intégrée après revue ciblée. |
| 16. Sémiologie CS | Lu ; le module I-03 n’existe pas encore dans le frontend de travail. Il reste une tâche de complétude du fragment, pas un acquis de B24. |
| 17. Construction et tests | Lu ; aperçu reconstruit, 19 empreintes, 168 tests Python et 2 229 contrôles Chromium ordinateur/mobile réussis. Les contrôles du futur fragment entier ne sont pas annoncés comme faits. |
| 18. GitHub et reçus | Lu ; 20 branches et 15 PR paginées, main et PR #16 lues au SHA. Les branches Claude sont préservées. La publication Pages sera vérifiée séparément du push. |
| 19. Visibilité | Lu ; capture spécifique du passage, captures ordinateur/mobile et animation issues du navigateur. La pile Claude est repérée sur PR #16, sans présence présumée sur `main`. |
| 20. Secrets | Lu ; aucun secret ni jeton n’est écrit dans les preuves ou montré au lecteur. |
| 21. Arrêt | Lu ; l’ancien STOP est levé par le PDF direct, les veilles restent en pause, aucun fragment n’est déclaré INJECTÉ. |
| Annexe A | Lue ; les anciennes règles de chapitre par remise, injection autonome, nouvelle passe après injection, police Georgia et mode sombre ne sont pas réactivées. |
| Annexe B | Lue ; les points de désaccord documentés ne sont pas masqués par une affirmation de conformité globale. La correction actuelle reste dans le périmètre où les règles convergent. |

Cet accusé atteste la lecture intégrale du cumul **à son commit précis** et l’application des règles pertinentes à cette progression. Il ne coche pas fictivement l’annexe C comme si les fonctions absentes étaient intégrées : les sections 15–16 et les contrôles finaux du fragment restent ouverts. La réception C-01 ne vaut pas audit favorable. Les étapes futures seront contrôlées au commit réellement publié.
