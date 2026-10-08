# Consignes à transmettre à Codex — 8 octobre 2026

Texte à copier tel quel dans la session Codex. Il met en force les exigences de Vial consignées dans [EXIGENCES_VIAL_2026-10-08.md](EXIGENCES_VIAL_2026-10-08.md).

---

Codex — consignes de Vial au 8 octobre 2026. Elles priment sur toute consigne antérieure de style, de typographie et de couleurs. Lis d'abord `docs/collaboration/EXIGENCES_VIAL_2026-10-08.md`, `COORDINATION.md` et `docs/collaboration/PROTOCOLE_FRAGMENTS_2026-10-08.md`.

**1. Périmètre.** Tes fragments, et eux seuls : I-03-Infectiologie, N-05-Neurologie, N-07-Néphrologie, O-09-Oncologie, génétique médicale et soins palliatifs, O-11-Obstétrique et néonatologie, I-13-Immunologie et allergologie, U-15-Urologie et andrologie, D-16-Dermatologie, D-20-Diagnostic clinique et examens complémentaires, M-21-Médecine de premier recours et santé publique. Tu ne produis ni ne modifies un chapitre des fragments de Claude.

**2. Espaces.** Tu déposes dans `espace_partage/COURS_CODEX_A_AUDITER_PAR_CLAUDE/`. Tu audites ce que Claude dépose dans `espace_partage/COURS_CLAUDE_A_AUDITER_PAR_CODEX/`. Toute opération passe par `tools/espace.py`. Unité de remise : le fragment entier, achevé et revu par toi. Un seul tour d'audit croisé : l'autre IA corrige sur place, puis injecte. Un fragment INJECTÉ est immuable.

**3. Rédaction.** Niveau maximal de ton moteur, sans version allégée, à la rédaction comme à la revue finale de chaque chapitre. Français direct, précis, concis, professionnel, en phrases complètes et agréables à lire. Aucune évidence, aucune annonce creuse, aucune redite entre le texte et ses fenêtres, aucune phrase lourde. Densité maximale d'information avec le moins de mots possible. Compte environ 30 % de mots en moins qu'une rédaction ordinaire, sans perdre une notion, un chiffre ou une source.

**4. Fenêtres et sources.** Le texte principal porte les décisions et les faits clés ; mécanismes, preuves, nuances et contentieux vont dans les fenêtres cliquables. Chaque affirmation est justifiée et sourcée par la source primaire applicable la plus récente, réellement lue et datée ; la version antérieure reste accessible dans une fenêtre. Posologies, contre-indications et interactions suisses : information professionnelle de compendium.ch.

**5. Reprise.** Relis et réécris à ce niveau chaque chapitre que tu as produit depuis le 8 octobre, A41 — Sepsis et choc septique de l'adulte compris, avant de remettre le fragment.

**6. Intitulés.** Les mots « autre », « autres », « sans précision », « non classé ailleurs » et « non précisé » sont interdits dans tout intitulé affiché de catégorie ou de chapitre. Les codes CIM-10-GM ne changent pas ; seul l'intitulé lisible est reformulé. Le nom d'une catégorie tient sur une ligne, deux au plus, et annonce ce qu'elle développe. Utilise `tools/libelles.py` et complète `organisation/libelles_clairs.json` pour tes fragments.

**7. Interface.** Conserve la charte haute lisibilité : police Atkinson Hyperlegible Next imposée partout, cours compris ; contraste élevé ; fonds francs, jamais ivoire, beige ni crème ; une couleur vive par spécialité et par catégorie ; quatre à cinq colonnes de catégories ; page de catégorie titrée avec ses chapitres sur deux colonnes ; couleur de la catégorie reprise dans l'environnement du cours et ses icônes ; thème clair uniquement. Fichiers : `engine/atlas_v2.css`, `engine/atlas_v2.js`, `engine/portal_v2.css`, `tools/libelles.py`. Ne les remplace pas par une palette pâle ni par une police à faible contraste.

**8. Preuves.** Montre ton avancement par des captures d'écran. Avant toute remise : `build_medina.py <CODE>` (0 abréviation non couverte), `test_v7.py --static <CODE>` puis `test_v7.py <CODE>`, `build_front.py --all-fragments`, `tests/audit_fragments.py`, `node tests/verify_fragment_frontends.cjs`, et les tests unitaires. Une revue par IA ne vaut pas validation par un médecin.
