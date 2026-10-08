# Décision Codex — I83 — Varices des membres inférieurs (C-01-Cardiologie)

**Injection sélective autorisée au SHA Claude `6d5797c6a902e430cd9d3e9dd5159ec507a1476a`. Les réserves bloquantes PH-01, PH-02 et le passage primaire d’urgence sont fermés ; les contrôles après injection locale réussissent.** Les remarques mineures sont conservées dans les rapports, sans les transformer en anciens défauts de prescription. Aucun score 20/20 ou certificat CIM-11 n’est inventé.

La décision d’attente intermédiaire adressée à Claude à 09:36 UTC a reçu des corrections effectives aux commits 20c67c0 et 6d5797c. Le [commentaire de référence pour injection](https://github.com/vialdjoukang-spec/Medina/pull/12#issuecomment-6057237825) est publié à 09:50:23 UTC. Les historiques de réception restent conservés ; ils ne décrivent pas les contrôles indépendants maintenant exécutés.

## Audit croisé et fermetures

| Poste et point | État final et preuve |
| --- | --- |
| Réception/provenance | Dix sources inspectées, empreintes conformes, seule entrée I83/I87 ajoutée, aucun conflit de glossaire/catalogue |
| Pathologie et Examens | [Lecture intégrale](AUDIT_PATHOLOGIE_EXAMENS.md) ; EHIT III corrigée, avis favorable avec remarques mineures |
| Sciences | [Lecture intégrale](AUDIT_SCIENCES.md) ; mécanismes et calculs relus, avis favorable avec qualifications mineures |
| Pharmacologie PH-01 | Formulation Rapidocain et restrictions conservateurs clarifiées ; [avis final 6d5797c](DELTA_6D5797C_PHARMACOLOGIE.md) favorable |
| Pharmacologie PH-02 | Chronologie désormais indice à confronter aux causes concurrentes ; [clôture 20c67c0](DELTA_20C67C0_PHARMACOLOGIE.md) |
| Injection intra-artérielle | Deux passages suisses exacts livrés et réellement lus ; 500 UI et autres conditions concordent, aucun changement de dose supposé |
| Inspection technique | AST des nouveaux glossaires sûr, liens/clés/structure conformes ; [delta final](DELTA_6D5797C_TECHNIQUE.json) |
| Contrôles après injection locale | [Tous réussis](CONTROLES_CANONIQUES_6D5797C.md) : 118 unités, statique/global, 1 923 natifs, 72 S01, 41 routes |

Six sous-agents spécialisés ont été mobilisés, avec un auteur par fichier et le coordinateur seul responsable des opérations Git. Les quatre panneaux, 47 fenêtres, figures, quiz, Pareto et glossaires associés sont couverts par les périmètres de lecture consignés. Les nouveaux deltas sont contrôlés séparément, sans refaire passer un ancien constat pour une erreur actuelle.

## Périmètre d’injection

Huit fichiers `chapters/I83/I83_{a,b,c,d,pop1,pop2,pop3,pop4}.html`, deux ajouts `glossary/i83.py` et `glossary/fragments_medina.py`, et seul objet I83 dans `chapters.json`, couvrant I83/I87. Pas de fusion globale de la PR #12. La fixture S01 passe de 20 à 21 cours ; le reste du test conserve ses assertions.

Les tests canoniques sont reconstruits dans des sorties externes depuis le checkout effectivement injecté, pas simplement repris des résultats du producteur. Les séries 0974d85, 20bee19 et 20c67c0 restent archivées à leurs propres SHA. Le reçu final précisera le commit d’injection, les contrôles, la publication distante et le déploiement vérifié.

## Qualifications conservées et progression

Remarques mineures : notation CEAP du cas, portée anatomique des résumés de reflux profond, précision C4a/c du cas de perforante, endpoints des pansements, existence/recherche du reflux debout, hypothèses de randomisation mendélienne, limites du modèle inflammatoire, harmonisation du glossaire EHIT et du cas d’œdème. Voir les localisations et propositions dans les rapports. Ces remarques sont à reprendre dans le même chapitre avant sa clôture complète ; I89 — Lymphœdème et adénopathies (C-01-Cardiologie) reste en attente.

Les sources primaires externes ont renvoyé CONNECT 403 : la fidélité aux extraits livrés est contrevérifiée, leur transcription depuis l’ensemble des sites officiels et certaines affirmations négatives OFSP ne sont pas certifiées par un téléchargement indépendant. Les domaines nécessaires sont ajoutés au brouillon cloud ; activation après enregistrement et publication de l’environnement. Cette limite est explicitée, pas utilisée comme veto automatique après remise des passages demandés. La portabilité directe `file://` n’est pas établie par les contrôles HTTP.

Les réserves ESC d’autres chapitres et la cartographie CIM-11 sont conservées dans leurs dossiers ; aucun fragment n’est déclaré achevé. La répartition 11 fragments Claude / 10 fragments Codex et la reprise active A41 — Sepsis et choc septique de l’adulte (I-03-Infectiologie) sont préservées. Le propriétaire n’a pas à confirmer une publication déjà autorisée.
