# Instruction principale — Claude Leader, 8 octobre 2026

> **Consigne directe de Vial, prioritaire sur toutes les instructions antérieures incompatibles** (y compris `PROTOCOLE_FRAGMENTS_2026-10-08.md`, `REGLES_INJECTION_CLAUDE.md`, `FRAGMENTS_RESTANTS.md` et les sections historiques de `CLAUDE.md`, `AGENTS.md` et `COORDINATION.md`). Les travaux, preuves, commits et injections antérieurs sont conservés.

## 1. Motif et principe

Devant la lenteur de la production Codex, Vial confie à **Claude le rôle de Leader** du projet MEDINA. Le principe est simple : la qualité ne dépend plus d’un aller-retour lent entre deux IA avant chaque injection. Elle est garantie par une **chaîne interne à deux agents distincts** chez Claude, puis contrôlée a posteriori par Codex sur le fichier final.

## 2. Production des cours par Claude

1. **Rédaction.** Chaque leçon est rédigée selon toutes les règles en vigueur (`PROMPT_MEDINA.md`, `docs/STYLE_REDACTION.md`, `CONSIGNES_INTERACTION_DENSITE_SOURCES.md`, justification causale de chaque affirmation, sources primaires datées), dans **un français très agréable à lire et captivant** : phrases complètes, progression logique du normal au pathologique, mécanisme avant conduite, exemples chiffrés, aucun remplissage.
2. **« Auto-audit par Agent différé opus 5.5 ».** L’agent rédacteur transmet la leçon complète à **un second agent distinct**, qui n’a pas rédigé le texte. Ce relecteur :
   - relit intégralement le fond médical, les mécanismes, les sources et le français ;
   - **renforce les points faibles** (erreur, imprécision, lacune, passage terne ou confus) ;
   - exécute les contrôles techniques (glossaire `audit() == {}`, contrat HTML, tests navigateur) ;
   - **injecte directement** la version finale.
3. **Audit Codex sur le fichier final.** Après injection, Claude demande à Codex d’auditer le fichier injecté (signal dans `SIGNAUX_CODEX.json` et file `FILE_AUDIT_CODEX.json`). Les constats Codex reviennent à Claude, qui tranche ; **une erreur médicale démontrée est corrigée en priorité**, y compris sur un contenu injecté.
4. Un auteur par fichier reste la règle ; le rédacteur et le relecteur sont toujours deux agents différents.

## 3. Cours produits par Codex

Claude reçoit les cours produits par Codex et **les améliore systématiquement**, sauf s’il constate que le cours est **à la fois captivant et correct sur le fond**. Dans ce cas, il le consigne dans un reçu (`docs/collaboration/receipts/`) sans le réécrire. Toute amélioration conserve les travaux et l’empreinte de la version Codex reçue.

## 4. Droit de reprise des fragments Codex (veto de Vial)

Lorsque Claude a achevé ses onze fragments, il **peut entamer les fragments attribués à Codex**, en progressant **en sens inverse de leur rang de création** :

| Ordre de reprise | Fragment |
| --- | --- |
| 1 | M-21-Médecine de premier recours et santé publique |
| 2 | D-20-Diagnostic clinique et examens complémentaires |
| 3 | D-16-Dermatologie |
| 4 | U-15-Urologie et andrologie |
| 5 | I-13-Immunologie et allergologie |
| 6 | O-11-Obstétrique et néonatologie |
| 7 | O-09-Oncologie, génétique médicale et soins palliatifs |
| 8 | N-07-Néphrologie |
| 9 | N-05-Neurologie |
| 10 | I-03-Infectiologie |

Les deux IA convergent ainsi par les extrémités opposées de la file Codex. Avant d’entamer un fragment, Claude publie un signal de prise en charge ; Codex ne commence plus ce fragment et lui transmet ses travaux éventuels, qui sont conservés.

## 5. Ce qui ne change pas

Nomenclature (`code — intitulé (libellé du fragment)`), quatre onglets, glossaire, typographie et police Atkinson Hyperlegible Next, thème clair, séparation des spécialités, sources suisses d’abord, distinction entre revue IA, tests et validation par un médecin. Aucun fragment n’est déclaré complet en CIM-11 sans inventaire versionné.

## 6. Pour Codex — à lire à chaque reprise

- **Claude est Leader.** Ses arbitrages priment en cas de désaccord non résolu, hors erreur médicale démontrée.
- Continuer la production de la file Codex à partir du rang le plus bas (I-03-Infectiologie, puis N-05, N-07…).
- **Auditer les fichiers finaux injectés par Claude** dans l’ordre de `FILE_AUDIT_CODEX.json`, puis publier les constats dans `SIGNAUX_CODEX.json` ; ne pas corriger soi-même un fichier Claude injecté.
- Vérifier les signaux de prise en charge de Claude avant d’ouvrir un fragment de sa file.
