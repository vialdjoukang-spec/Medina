# Clôture du delta — I83 — Varices des membres inférieurs (C-01-Cardiologie)

**Décision au SHA `6d5797c6a902e430cd9d3e9dd5159ec507a1476a` : avis favorable à l’injection sélective maintenu pour le périmètre Pharmacologie relu. Aucun défaut médical avéré n’est introduit par ce delta. PH-01 et PH-02 restent résolues ; la procédure d’urgence et sa preuve sont inchangées.** Les autres audits et contrôles techniques restent du ressort du coordinateur. Aucune injection par ce poste.

Date : 8 octobre 2026. Comparaison réellement lue : `20c67c011e57eccd25b105b15f465becf7df7f2e` → `6d5797c6a902e430cd9d3e9dd5159ec507a1476a`. Les décisions précédentes sont conservées dans [l’audit historique](AUDIT_PHARMACOLOGIE.md) et [la contrelecture précédente](DELTA_20C67C0_PHARMACOLOGIE.md).

## Changement effectivement relu

Le diff complet comporte quatre chemins : une seule ligne de cours change, **`chapters/I83/I83_pop4.html:50`**, avec 36 lignes ajoutées à la preuve Rapidocain, un addendum au rapport et un journal de simulation du producteur. Le journal n’est pas exécuté et ne constitue pas une validation médicale.

La nouvelle ligne distingue désormais :

- la recette ESVS et ses calculs, inchangés ;
- le Rapidocain avec épinéphrine, contenant des conservateurs, qui ne sert pas d’équivalent direct au mélange de grand volume ;
- les présentations de Rapidocain 10 mg/mL sans conservateurs et sans adrénaline : ampoules de 5 ou 10 mL, flacon de 20 mL à usage unique ;
- une préparation diluée réalisée sur place, avec ajout d’adrénaline et de bicarbonate suivant les règles de l’établissement, que l’information professionnelle ne décrit pas.

Le texte ne présente donc pas une ampoule de lidocaïne seule comme contenant déjà l’adrénaline de la recette. Il n’invente pas une spécialité combinée sans conservateur ni une autorisation suisse de tumescence. La restriction des blocages >15 mL, les allergies aux conservateurs et le statut hors information professionnelle restent visibles.

## Concordance documentaire vérifiée

La preuve nouvelle `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83/preuves/rapidocain_extraits.md` a été lue, notamment ses ajouts **lignes 178–212**. Elle déclare l’information professionnelle suisse Rapidocain/Rapidocain avec épinéphrine, Swissmedic **20272/32381**, juillet 2024.

| Point du cours | Passage effectivement lu | Résultat |
| --- | --- | --- |
| Conservateurs des formes concernées | Preuve nouvelle : lignes 181–193, sources 35–47 ; E216/E218 explicitement présents | Concordant. La forme avec épinéphrine comporte également E223 ; sa précaution est conservée dans la fenêtre. |
| 10 mg/mL, ampoules 5 et 10 mL, flacon 20 mL à usage unique | Preuve nouvelle : lignes 194–199, sources **503–508**, sous « Préparations à usage unique » | Présentations et volumes concordants. Les sources 513–518 distinguent ensuite les formes à usage multiple avec conservateurs. |
| Forme simple sans adrénaline ni conservateurs | Composition réellement relue dans la preuve antérieure archivée, **lignes 11–18** : lidocaïne seule ; chlorure de sodium, hydroxyde de sodium et eau pour injection ; volumes correspondants | Concordant. L’absence de conservateurs n’est pas déduite du seul conditionnement à usage unique. |
| Préparation locale et statut réglementaire | `I83_pop4.html:50,54` : les ajouts ne sont pas décrits par l’information professionnelle et la tumescence reste hors information | Limite explicitée ; aucune préparation locale particulière n’est certifiée par ce rapport. |

La preuve de composition antérieure est l’objet lu au SHA main de référence `ea105ace0046c71492cc6a69ff4c61698ef2ce34`, chemin exact :

`livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_PR12_D94B11F_I83_MAIN31B_PROOFS/livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83/preuves/rapidocain_extraits.md`.

Ses anciens titres découpaient mal le document, comme déjà consigné ; le passage de **composition**, présent dans son contenu, est réellement lu et identifié comme tel. Il n’est pas utilisé comme preuve de posologie. Aucune nouvelle pièce identique n’est demandée alors que ce passage est déjà disponible.

## Empreintes et maintien des décisions

| Objet au SHA `6d5797c` | Blob Git vérifié | SHA-256 recalculé |
| --- | --- | --- |
| `chapters/I83/I83_pop4.html` | `5b0ed67c99a57fc22d567a03a5b0c955a290d90e` | `dede4bdcf1974bbff6c2b2874410b64ac1e15003371fc9d78b3436c4999174f4` |
| Nouvelle preuve Rapidocain | `fc2c831e53546d471d50d6b28766bc246e42f830` | `0e147d7710cca673ba4ef3212d23f1de3f89af961681da3b5ec789235a9ca1a7` |
| `chapters/I83/I83_d.html`, inchangé | `e006eace6f7eac73897d0d5418ae9b495067f6cf` | `d6a339fea23ae2ffb8aa16268972ec0e9708b997fbd44403b3a2478387bbc88f` |
| Preuve d’urgence intra-artérielle, inchangée | `3ff96ae7f11e017be24febabd711bf24396ef31e` | `fce2515bdf985f5ecf22f56fd7dbbab116058974b992707a4ef196fefb205f25` |

Les **sept autres HTML du chapitre** ont des blobs identiques à `20c67c0` : `I83_a.html`, `I83_b.html`, `I83_c.html`, `I83_d.html`, `I83_pop1.html`, `I83_pop2.html`, `I83_pop3.html`. Ce contrôle d’identité ne constitue pas un nouvel audit médical intégral de leurs contenus.

**PH-01 reste fermée** : la distinction entre formulation commerciale et préparation de tumescence est précisée sans rétablir l’ancienne équivalence pratique. **PH-02 reste fermée** : `I83_d.html:82` n’a pas changé. **La réserve documentaire ciblée sur l’urgence reste fermée** : `I83_d.html:61`, le Pareto à `I83_pop4.html:67` et les deux extraits suisses sont inchangés depuis la décision précédente.

## Limite de provenance et avis final

La fidélité aux **passages effectivement livrés** est contrevérifiée. La copie complète de l’information professionnelle, son empreinte déclarée `7b24cf1d5f2d91b8fa986c412d0ca6778a1633c4887b4f9ea19a144d4a628268`, et le téléchargement officiel indépendant restent distincts : ce téléchargement n’est pas effectué ici. Les limites primaires déjà consignées sont maintenues sans être transformées en nouveaux défauts prouvés ni en demandes répétées de pièces déjà présentes.

**Reste bloquant médical prouvé dans ce delta et dans les réserves Pharmacologie suivies : aucun. Avis de clôture favorable pour la remise figée `6d5797c`, en vue de son injection sélective.** Cette contrelecture ne certifie pas à elle seule l’ensemble de I83 — Varices des membres inférieurs (C-01-Cardiologie), toutes ses sources externes ou un protocole local de préparation.

Objets Git consultés en lecture seule ; aucun code entrant exécuté, aucun fichier canonique, index, référence ou commit modifié. Seul ce nouveau rapport est écrit.
