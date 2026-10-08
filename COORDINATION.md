## INSTRUCTION PRINCIPALE — Claude Leader, 8 octobre 2026

**RÈGLE FONDAMENTALE (section 11)** : aucun cours produit de mémoire — chaque affirmation vient d'une source lue ; **sources suisses puis européennes, aucune recommandation américaine** ; médicaments selon l'information professionnelle suisse Swissmedic (`tools/swissmedic_fi.py`) ; **plan monographique classique**, sans îlot ni tableau consacré au code CIM. Toute invention ou tricherie est interdite.

Consigne directe de Vial, prioritaire sur toutes les sections ci-dessous qui lui sont contraires : **Claude est Leader du projet.** Lire [LEADERSHIP_CLAUDE_2026-10-08.md](docs/collaboration/LEADERSHIP_CLAUDE_2026-10-08.md). Claude rédige ses cours dans un français très agréable et captivant ; un **second agent distinct** les relit, renforce les points faibles et **injecte directement** (« Auto-audit par Agent différé opus 5.5 ») ; **Codex audite ensuite le fichier final injecté**. Claude améliore systématiquement les cours Codex reçus, sauf s’ils sont captivants et corrects sur le fond. Après ses onze fragments, Claude peut entamer les fragments Codex en ordre inverse de création (M-21 vers I-03). Une erreur médicale démontrée reste prioritaire.

Règles universelles ajoutées : **l’efficacité prime sur le volume** — information efficace, puissante, extrêmement didactique, claire, en termes médicaux dédiés, sans remplissage ni perte d’information utile ; **deux captures d’écran réelles par leçon** (ouverture de la leçon et fenêtre explicative ouverte, `tools/capture_lecon.py`), présentées dans le **panneau latéral**, non dans le fil du chat. Voir les sections 7 et 8 du même document.
Règle universelle de langue : un français **merveilleux à lire, riche, professionnel et esthétique, sans excès** (section 9). File de production Claude : `organisation/FILE_FRAGMENTS_CLAUDE.json`, un fragment à la fois, leçon par leçon (section 10).

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

**I-03-Infectiologie (T1)** reste le fragment actif Codex. Le contrôle ciblé d’**A41 — Sepsis et choc septique de l’adulte** est consigné ; **B24 — Infection par le VIH et maladie à VIH de l’adulte** est en contrôle interne. Le catalogue historique comprend 155 catégories locales et un seul cours déclaré : cet inventaire n’établit pas la couverture CIM-11. Les remises A41 et J45 antérieures dans l’espace partagé sont conservées avec leurs empreintes ; leur ancien statut `a_auditer` ne constitue plus un ordre d’audit final de fragment.

La progression interne du 8 octobre poursuit **B24 — Infection par le VIH et maladie à VIH de l’adulte**, après le contrôle ciblé d’A41 et ses retouches consignées dans [cloture_interne_A41.json](livraisons/Livraison%20Codex/I-03-Infectiologie/travail/PRODUCTION_FRAGMENT_2026-10-08/preuves/cloture_interne_A41.json). Le catalogue frontend actuel comporte **184 catégories dans 24 blocs**, après rattachement de 29 catégories infectiologiques auparavant classées ailleurs. La couverture pédagogique CIM-11 reste non établie ; le candidat OMS et sa matrice sont conservés sans équivalence automatique. Les nouvelles sources restent dans le dossier de production interne, consultable par l’aperçu, avec la police Atkinson déjà alignée sur Claude.

**Publication de cette progression bloquée le 8 octobre à 19:55 Europe/Zurich** : l’outil GitHub `create_tree` exige une approbation interdite par la politique de la session. Aucun changement distant n’a été effectué. Les 168 tests Python et 223 contrôles de structure locaux passent ; les contrôles navigateur et les captures CI restent à exécuter. Le nouvel aperçu B24 est donc préparé localement et n’est pas encore accessible sur le site public.

Aucun des 22 fragments n’est marqué INJECTÉ à cette reprise : les preuves requises de complétude et d’audit final du fragment entier manquent. Cela conserve les injections historiques de cours sans leur attribuer une portée nouvelle. Les rapports et corrections internes restent publiables comme travail en cours, sans transmission pour audit final avant achèvement.

Une contribution concurrente a ensuite injecté **le chapitre A41**, après audit Claude `ba6a80f`, au commit `a5563238887df2a72da7a9f663bdae9ab01f4bc8` selon les règles administratives précédentes. Ces corrections sont préservées dans la base de reprise. Elles ne valent ni audit final ni injection du fragment entier ; les nouvelles améliorations A41 restent dans une copie interne.


## Reprise de l’accès visuel

Le 08/10/2026 à 20:21 Europe/Zurich, le réglage d’accès complet lève le blocage réseau et navigateur. L’aperçu A41/B24 passe 2223 contrôles interactifs locaux sur ordinateur et mobile, sans échec ; les 19 sources gelées restent exactes. Publication par Git puis contrôle du déploiement Pages, sans modifier les fichiers médicaux canoniques ni le statut EN_PRODUCTION de T1. Voir le reçu `docs/collaboration/receipts/CODEX_B24_APERCU_2026-10-08.json`.
