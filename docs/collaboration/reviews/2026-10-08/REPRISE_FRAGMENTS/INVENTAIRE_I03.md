# Inventaire de reprise — I-03-Infectiologie (T1)

Relevé local du 8 octobre 2026, lecture seule des sources canoniques et suivis au SHA `61a841b3c96b3bd4f3ad58ec5870d06945e63292`. Ce rapport ne vérifie pas les têtes distantes, les références primaires en ligne, l’affichage du site ni l’exactitude médicale complète. Aucune branche ni source du projet modifiée ; seuls les rapports de travail Markdown et JSON sont écrits.

Complément lu sur les blobs exacts de main `a6f82b6e359a5087b3271f66d590ac02f46d23bf` signalé par le coordinateur : le STOP ancien, les règles administratives d’espace partagé et le dossier A41 sont conservés. Le PDF adopté par la demande actuelle autorise la reprise et fixe désormais le fragment entier comme unité de transmission. Aucun changement dans les cinq sources de périmètre (`organisation/fragments.json`, `fragments.json`, `chapters.json`, `shell/medina_front.html`, `docs/COMPLETUDE_CIM11.md`) entre le checkout 61a841b et a6f82b6 ; les 155 catégories demeurent identiques.


**Actualisation concurrente :** main `a5563238887df2a72da7a9f663bdae9ab01f4bc8` injecte le **chapitre** A41 après audit Claude `ba6a80fbbe901b52085f3b8f992e2e49fe592e4d`, verdict enregistré « favorable sous réserves mineures ». Les dix fichiers canoniques correspondent aux dix empreintes de l’espace partagé et de son état `injecte` ; contrôle effectué sur les blobs Git. Les mentions « non injecté » ci-dessous décrivent le relevé historique a6f82b6, conservé. Cette injection d’un chapitre ne requalifie pas le fragment entier I-03-Infectiologie en INJECTÉ. Aucun déploiement ni audit médical reproduit ici. Les cinq sources de périmètre demeurent inchangées.

Une extraction officielle candidate du chapitre OMS 01 est désormais disponible ; voir `/workspace/work/cim11-i03-sources.md` et `/workspace/work/cim11-officiel/chapter01_mms_2026-01_fr.json`. Elle ne valide pas encore le périmètre pédagogique complet T1.

## Consigne nouvellement adoptée et distinction des états

La demande utilisateur adopte les nouvelles consignes de `Prompt_Codex.pdf`, dont la transcription lue est `/workspace/work/Prompt_Codex.txt`. Le document décrit le travail ; son adoption est donnée par la demande utilisateur et la mission du coordinateur. Pour la nouvelle production : achever et auto-revoir le fragment entier avant transmission ; audit croisé final en un seul tour puis injection ; état INJECTÉ immuable ; HTML clair uniquement. Les règles antérieures de remise/audit/injection chapitre par chapitre figurent encore dans AGENTS.md, le plan et les suivis : elles ne doivent pas recréer une transmission prématurée du nouveau fragment. Conserver les remises et preuves historiques, sans requalifier rétroactivement leur validation.

Le verrou du PDF est défini au niveau du fragment. `integrated: true` pour un cours ancien ou un manifeste de sources ne suffit pas à établir que I-03-Infectiologie est INJECTÉ au sens de cette nouvelle règle. Le fragment est explicitement déclaré partiel et sa couverture CIM-11 non établie.

## Périmètre actuel exactement inventorié

- Registre public `organisation/fragments.json` : T1 = **I-03-Infectiologie**, rang 03.
- Structure technique `fragments.json` : slug `agents-therapeutique`, nom historique « Agents et thérapeutique », spécialité `infectiologie`, surface `courses-v1`.
- Axe de catalogue rattaché : **Microorganismes, hôte et sites infectieux** ; une seule catégorie pédagogique de cours actuelle « Infections systémiques et réponse de l’hôte », contenant A41.
- Le catalogue natif se trouve dans `shell/medina_front.html`, script JSON `medora-data`. Métadonnées : CIM-10-GM 2024, catalogue v3.0 du 18 septembre 2026, 1 636 catégories globales.
- Recalcul du rattachement par le même mécanisme que `tools/build_organisation.py` : **155 catégories locales T1, réparties sur 22 blocs**, avec **450 sous-codes locaux**. Les sous-codes locaux et extraits ne sont pas garantis exhaustifs. Extrait tronqué pour : U99.
- `chapters.json` comporte 32 cours globaux et **1 cours T1 intégré** : **A41 — Sepsis et choc septique de l’adulte (I-03-Infectiologie)**, `covers: [A41]`, ajouté le 26 septembre 2026.
- Les **154 autres catégories locales** n’ont pas de cours déclaré ni de `covers` dans `chapters.json`. Il ne s’agit pas d’un décompte CIM-11 ni d’une preuve d’absence de toute mention textuelle.

### Priorités et renvois du registre

| Rang déclaré | Catégorie et fragment propriétaire | Situation locale |
| --- | --- | --- |
| 1 | A41 — Autres septicémies (I-03-Infectiologie) | Cours primaire disponible ; reprise A41 proposée, non injectée |
| 2 | B24 — Immunodéficience humaine virale [VIH], sans précision (I-03-Infectiologie) | À produire dans T1 |
| 3 | B18 — Hépatite virale chronique (G-04-Gastroentérologie et hépatologie) | Renvoi planned vers G-04-Gastroentérologie et hépatologie ; aucun cours cible déclaré |
| 4 | A54 — Infection gonococcique (I-03-Infectiologie) | À produire dans T1 |
| 5 | A53 — Syphilis, autres et sans précision (I-03-Infectiologie) | À produire dans T1 |
| 6 | B50 — Paludisme à Plasmodium falciparum (I-03-Infectiologie) | À produire dans T1 |
| 7 | A04 — Autres infections intestinales bactériennes (G-04-Gastroentérologie et hépatologie) | Renvoi planned vers G-04-Gastroentérologie et hépatologie ; aucun cours cible déclaré |
| 8 | A69 — Autres infections à spirochètes (I-03-Infectiologie) | À produire dans T1 |
| 9 | A15 — Tuberculose de l’appareil respiratoire, avec confirmation bactériologique, par biologie moléculaire ou histologique (I-03-Infectiologie) | À produire dans T1 |
| 10 | A16 — Tuberculose de l’appareil respiratoire, sans confirmation bactériologique, par biologie moléculaire ou histologique (I-03-Infectiologie) | À produire dans T1 |

B18 et A04 restent attachés à G-04-Gastroentérologie et hépatologie (S03) par l’organisation actuelle. Leur présence dans les priorités T1 n’en fait pas des cours T1 disponibles. La matrice CIM-11 devra établir les rattachements multiples pertinents et les passages spécifiques accessibles dans le fragment autonome.

### Blocs locaux

| Bloc de catalogue historique | Nombre de catégories | Enseignement déclaré |
| --- | ---: | --- |
| A15-A19 — Tuberculose | 4 | Aucun cours déclaré |
| A20-A28 — Certaines anthropozoonoses bactériennes | 9 | Aucun cours déclaré |
| A30-A49 — Autres maladies bactériennes | 16 | A41 uniquement ; autres absents du registre |
| A50-A64 — Infections dont le mode de transmission est essentiellement sexuel | 13 | Aucun cours déclaré |
| A65-A69 — Autres maladies à spirochètes | 5 | Aucun cours déclaré |
| A70-A74 — Autres maladies à Chlamydia | 3 | Aucun cours déclaré |
| A75-A79 — Rickettsioses | 4 | Aucun cours déclaré |
| A80-A89 — Infections virales du système nerveux central | 2 | Aucun cours déclaré |
| A92-A99 — Fièvres virales transmises par des arthropodes et fièvres virales hémorragiques | 8 | Aucun cours déclaré |
| B00-B09 — Infections virales caractérisées par des lésions cutanéo-muqueuses | 8 | Aucun cours déclaré |
| B20-B24 — Maladies dues au virus de l’immunodéficience humaine [VIH] | 5 | Aucun cours déclaré |
| B25-B34 — Autres maladies virales | 6 | Aucun cours déclaré |
| B35-B49 — Mycoses | 15 | Aucun cours déclaré |
| B50-B64 — Maladies dues à des protozoaires | 11 | Aucun cours déclaré |
| B65-B83 — Helminthiases | 19 | Aucun cours déclaré |
| B85-B89 — Pédiculose, acariase et autres infestations | 4 | Aucun cours déclaré |
| B90-B94 — Séquelles de maladies infectieuses et parasitaires | 4 | Aucun cours déclaré |
| B95-B98 — Agents d’infections bactériennes, virales et autres classées dans d’autres chapitres | 4 | Aucun cours déclaré |
| B99-B99 — Autres maladies infectieuses | 1 | Aucun cours déclaré |
| U00-U49 — Classement provisoire d’affections d’étiologie incertaine, codes affectés et non affectés | 7 | Aucun cours déclaré |
| U80-U85 — Agents infectieux résistants aux antibiotiques ou aux thérapies chimiques précisés | 6 | Aucun cours déclaré |
| U98-U99 — Codes affectés et non affectés | 1 | Aucun cours déclaré |

## Sources A41 réellement présentes

Sources canoniques : `chapters/A41/` avec les neuf fichiers `A41_a.html`, `A41_b.html`, `A41_c.html`, `A41_d.html`, `A41_pop1.html`, `A41_pop2.html`, `A41_pop_pa.html`, `A41_pop_sciences_revision.html`, `A41_justifications.json` ; glossaire supplémentaire `glossary/a41.py`. Les fichiers `a` et `b` forment ensemble l’onglet Pathologie ; `c` contient Examens **et** Sciences ; `d` Pharmacologie. Pour les reprises, attribuer les fichiers réels afin d’éviter deux auteurs sur `A41_c.html`.

Le paquet `livraisons/Livraison Codex/I-03-Infectiologie/livraison.json` se déclare « partiel ; complétude CIM-11 non établie », référentiel CIM-10-GM 2024, source commit `f149128357ce6cdc7bb9d7c77a837e545facc814`, aucune vérification listée dans `checks`. Les neuf copies de son dossier `sources/chapters/A41/` sont actuellement identiques octet pour octet aux fichiers canoniques et leurs neuf empreintes SHA-256 concordent avec le manifeste : ce contrôle de provenance a été refait durant cette mission.

Le relevé historique `travail/A41-2026-10-08/INVENTAIRE_BASE.md` documente la structure (63 fenêtres natives, 8 quiz, 7 SVG, glossaire et fenêtres de justifications), les anciennes bases et limites. Ces nombres sont ses constats historiques, sans contrôle navigateur ou revue médicale refaits ici.

### Reprise A41 déjà remise, distincte du canonique

Reçu `docs/collaboration/receipts/CODEX_A41_E330776_REMIS_CLAUDE_2026-10-08.json` : candidat source `e3307768ff4c3a6c3af2e790859ff36947c0279d`, branche `codex/a41-corrections-20261008`, PR #15. Dix fichiers proposés, 75 observations d’origine (10 majeures, 46 mineures, 19 éditoriales), 68 propositions complètes, 2 partielles, 5 déléguées, **0 closes par audit externe Claude**. `canonical_sources_unchanged: true`, `injected: false`, `external_Claude_ack_received: false`.

Réserves explicites du reçu : **ESP-03 majeure** (bicarbonate actuel/calculé artériel et matrices), **ESP-07 mineure** (protocole de contraste). Les contrôles 4 350 assertions / 0 échec et 49 parcours T1 sont les résultats enregistrés pour ce candidat, pas une validation médicale ni des contrôles reproduits ici. Les propositions du lot `lots/2026-10-08-A41/` ne sont pas présentes dans le checkout 61a841b. Elles sont désormais aussi conservées dans main a6f82b6e359a5087b3271f66d590ac02f46d23bf sous `espace_partage/COURS_CODEX_A_AUDITER_PAR_CLAUDE/A41/` : `ETAT.json` déclare `statut: a_auditer`, `audits: []`. Les dix empreintes des fichiers de ce dossier ont été vérifiées sur ses blobs Git : toutes conformes ; leurs dix empreintes de base concordent avec les fichiers canoniques main. Aucun audit favorable ni injection ne peut être déduit de ce dépôt.

## CIM-11 : preuve recherchée et manquante

`docs/COMPLETUDE_CIM11.md` impose la CIM-11 MMS **2026-01 en français** et une matrice par entité : code, identifiant OMS, intitulé officiel, parent, version, URL, tous les rattachements pédagogiques justifiés, fichier/cours/onglet/ancre du passage propre, variantes et limites, accès vérifié dans le fragment autonome, relecture indépendante et SHA relu, état sans confusion. Blocs organisateurs, entités résiduelles et codes de précision doivent rester documentés ; correspondances CIM-10→CIM-11 à contrôler officiellement.

Aucun inventaire CIM-11 T1 versionné et validé n’a été trouvé dans les fichiers ciblés ni parmi les chemins locaux d’inventaire/classification. Le catalogue native ne possède aucun champ CIM-11 ni identifiant d’entité OMS : ses clés sont `code`, `title`, `block`, `subcodes`, etc. `organisation/README.md`, `audits/COMPLETUDE_2026-10-07/README.md`, `livraison.json` et la règle de complétude confirment cette absence. La couverture reste donc **non établie**, et le dénominateur CIM-11 est **inconnu**.

Le chiffre historique 1/155 (0,65 %) dans `audits/COMPLETUDE_2026-10-07/catalogue-coverage.json` décrit seulement une déclaration de couverture CIM-10-GM par `covers`. Il n’est pas une mesure de couverture CIM-11 ou de validation clinique. Les priorités du registre ne sont pas un périmètre exhaustif.

### Entités transversales et lacunes de rattachement à examiner

29 catégories du catalogue hors T1 portent déjà le tag de spécialité `infectiologie` (15 S03, 10 S08, 3 S11, 1 S01). Ce relevé est un signal de rapprochement documentaire, pas l’inventaire complet de toutes les infections. Exemple concret : A43 — Nocardiose (C-01-Cardiologie) reste propriétaire S01 selon les rattachements actuels, alors que `shell/data.py` la renvoie à une future production en infectiologie ; aucun cours déclaré n’en prouve la disponibilité. Ne pas silencieusement déplacer cette catégorie ; ajouter la justification et l’accès spécifique dans la matrice de rattachements.

Le plan pédagogique historique `shell/data.py`, `PLAN[7]`, prévoit aussi : infections urinaires, peau/tissus mous, méningites/encéphalites, VIH, hépatites, IST, retour de voyage/paludisme, ostéo-articulaire, Clostridioides difficile, borréliose/encéphalite à tiques, fièvre chez l’immunodéprimé, vaccinations adultes, antibiothérapie raisonnée. Ces thèmes recoupent plusieurs fragments : la règle CIM-11 exige leur visibilité appropriée et un passage réellement enseigné, sans accepter un renvoi vers un cours futur.

## Obstacles concrets et suite faisable

1. **Coordination antérieure incompatible avec la nouvelle unité de transmission** : le plan et les instructions locales prévoient encore un chapitre remis avant le suivant. Le coordinateur peut tracer la nouvelle règle « fragment entier avant audit final », conserver le reçu historique A41 et continuer la production interne de T1 ; aucune nouvelle transmission de fragment incomplet.
2. **Dénominateur CIM-11 absent** : établir une extraction officielle MMS 2026-01 française, avec provenance, empreinte et date, puis la hiérarchie entière T1 et les rattachements transversaux ; construire une matrice vérifiable, sans inventer un total d’entités. Tant que ce travail n’est pas contrôlé, aucune clôture T1.
3. **Sources officielles précédemment inaccessibles** : le rapport A41 existant consigne `CONNECT 403` pour SCCM et WHO. C’est un incident antérieur, pas un test de ce tour. Vérifier maintenant l’accès officiel, ou télécharger une exportation officielle accessible par une voie autorisée ; consigner accès intégral/résumé/indisponible.
4. **Réserves A41 non closes et candidat non injecté** : préserver et rapprocher les propositions e330776 avec la tête canonique avant tout remplacement. Continuer la résolution interne des réserves dans le fragment en travail. Le nombre de contrôles techniques ne ferme aucune réserve médicale.
5. **Travail clinique immédiatement utile dans T1** : après conservation de l’état A41, le prochain code prioritaire propriétaire T1 sans enseignement est **B24 — Immunodéficience humaine virale [VIH], sans précision (I-03-Infectiologie)**. Préparer un dossier HIV/VIH adulte couvrant les distinctions B20–B24 et les entités CIM-11 vérifiées, avec quatre onglets, fenêtres sourcées, accès, diagnostic, dépistage, infection aiguë, critères/complications, traitement, suivi et prévention. Lire les recommandations primaires suisses/EACS/OMS effectivement applicables avant seuils ou posologies ; une architecture ou un plan n’est pas un enseignement livré. Cette rédaction reste interne jusqu’à achèvement et auto-revue du fragment entier.
6. **HTML clair** : vérifier la construction, le shell et les styles du fragment lors de la future production ; cette mission n’a pas modifié le thème ni contrôlé l’affichage.

## Annexe — 155 catégories locales exactes T1

Liste calculée depuis le catalogue natif et le rattachement canonique. Chaque état décrit seulement le registre des cours. Le nombre de sous-codes est celui du catalogue historique partiel.

| Catégorie (I-03-Infectiologie) | Bloc | Sous-codes locaux | État des cours |
| --- | --- | ---: | --- |
| A15 — Tuberculose de l’appareil respiratoire, avec confirmation bactériologique, par biologie moléculaire ou histologique (I-03-Infectiologie) | A15-A19 | 9 | Aucun cours déclaré |
| A16 — Tuberculose de l’appareil respiratoire, sans confirmation bactériologique, par biologie moléculaire ou histologique (I-03-Infectiologie) | A15-A19 | 9 | Aucun cours déclaré |
| A18 — Tuberculose d’autres organes (I-03-Infectiologie) | A15-A19 | 9 | Aucun cours déclaré |
| A19 — Tuberculose miliaire (I-03-Infectiologie) | A15-A19 | 1 | Aucun cours déclaré |
| A20 — Peste (I-03-Infectiologie) | A20-A28 | 2 | Aucun cours déclaré |
| A21 — Tularémie (I-03-Infectiologie) | A20-A28 | 2 | Aucun cours déclaré |
| A22 — Charbon (I-03-Infectiologie) | A20-A28 | 4 | Aucun cours déclaré |
| A23 — Brucellose (I-03-Infectiologie) | A20-A28 | 4 | Aucun cours déclaré |
| A24 — Morve et mélioïdose (I-03-Infectiologie) | A20-A28 | 3 | Aucun cours déclaré |
| A25 — Fièvres causées par morsure de rat (I-03-Infectiologie) | A20-A28 | 3 | Aucun cours déclaré |
| A26 — Érysipéloïde (I-03-Infectiologie) | A20-A28 | 3 | Aucun cours déclaré |
| A27 — Leptospirose (I-03-Infectiologie) | A20-A28 | 2 | Aucun cours déclaré |
| A28 — Autres anthropozoonoses bactériennes, non classées ailleurs (I-03-Infectiologie) | A20-A28 | 2 | Aucun cours déclaré |
| A30 — Lèpre [maladie de Hansen] (I-03-Infectiologie) | A30-A49 | 7 | Aucun cours déclaré |
| A31 — Infections dues à d’autres mycobactéries (I-03-Infectiologie) | A30-A49 | 6 | Aucun cours déclaré |
| A32 — Listériose (I-03-Infectiologie) | A30-A49 | 4 | Aucun cours déclaré |
| A33 — Tétanos néonatal (I-03-Infectiologie) | A30-A49 | 0 | Aucun cours déclaré |
| A34 — Tétanos obstétrical (I-03-Infectiologie) | A30-A49 | 0 | Aucun cours déclaré |
| A35 — Autres formes de tétanos (I-03-Infectiologie) | A30-A49 | 0 | Aucun cours déclaré |
| A36 — Diphtérie (I-03-Infectiologie) | A30-A49 | 6 | Aucun cours déclaré |
| A37 — Coqueluche (I-03-Infectiologie) | A30-A49 | 1 | Aucun cours déclaré |
| A38 — Scarlatine (I-03-Infectiologie) | A30-A49 | 0 | Aucun cours déclaré |
| A40 — Septicémie à streptocoques (I-03-Infectiologie) | A30-A49 | 2 | Aucun cours déclaré |
| A41 — Autres septicémies (I-03-Infectiologie) | A30-A49 | 5 | A41 intégré ancien ; révision proposée non injectée |
| A42 — Actinomycose (I-03-Infectiologie) | A30-A49 | 2 | Aucun cours déclaré |
| A44 — Bartonellose (I-03-Infectiologie) | A30-A49 | 3 | Aucun cours déclaré |
| A46 — Érysipèle (I-03-Infectiologie) | A30-A49 | 0 | Aucun cours déclaré |
| A48 — Autres maladies bactériennes, non classées ailleurs (I-03-Infectiologie) | A30-A49 | 6 | Aucun cours déclaré |
| A49 — Infection bactérienne, siège non précisé (I-03-Infectiologie) | A30-A49 | 1 | Aucun cours déclaré |
| A50 — Syphilis congénitale (I-03-Infectiologie) | A50-A64 | 9 | Aucun cours déclaré |
| A51 — Syphilis précoce (I-03-Infectiologie) | A50-A64 | 5 | Aucun cours déclaré |
| A52 — Syphilis tardive (I-03-Infectiologie) | A50-A64 | 6 | Aucun cours déclaré |
| A53 — Syphilis, autres et sans précision (I-03-Infectiologie) | A50-A64 | 2 | Aucun cours déclaré |
| A54 — Infection gonococcique (I-03-Infectiologie) | A50-A64 | 8 | Aucun cours déclaré |
| A55 — Lymphogranulomatose vénérienne à Chlamydia (I-03-Infectiologie) | A50-A64 | 0 | Aucun cours déclaré |
| A56 — Autres infections à Chlamydia transmises par voie sexuelle (I-03-Infectiologie) | A50-A64 | 3 | Aucun cours déclaré |
| A57 — Chancre mou (I-03-Infectiologie) | A50-A64 | 0 | Aucun cours déclaré |
| A58 — Granulome inguinal (I-03-Infectiologie) | A50-A64 | 0 | Aucun cours déclaré |
| A59 — Trichomonase (I-03-Infectiologie) | A50-A64 | 2 | Aucun cours déclaré |
| A60 — Infection ano-génitale par le virus de l’herpès [herpes simplex] (I-03-Infectiologie) | A50-A64 | 2 | Aucun cours déclaré |
| A63 — Autres maladies dont le mode de transmission est essentiellement sexuel, non classées ailleurs (I-03-Infectiologie) | A50-A64 | 1 | Aucun cours déclaré |
| A64 — Maladie sexuellement transmise, sans précision (I-03-Infectiologie) | A50-A64 | 0 | Aucun cours déclaré |
| A65 — Syphilis non vénérienne (I-03-Infectiologie) | A65-A69 | 0 | Aucun cours déclaré |
| A66 — Pian (I-03-Infectiologie) | A65-A69 | 10 | Aucun cours déclaré |
| A67 — Pinta [caraté] (I-03-Infectiologie) | A65-A69 | 5 | Aucun cours déclaré |
| A68 — Fièvres récurrentes [borrélioses] (I-03-Infectiologie) | A65-A69 | 3 | Aucun cours déclaré |
| A69 — Autres infections à spirochètes (I-03-Infectiologie) | A65-A69 | 4 | Aucun cours déclaré |
| A70 — Infection à Chlamydia psittaci (I-03-Infectiologie) | A70-A74 | 0 | Aucun cours déclaré |
| A71 — Trachome (I-03-Infectiologie) | A70-A74 | 3 | Aucun cours déclaré |
| A74 — Autres infections à Chlamydia (I-03-Infectiologie) | A70-A74 | 3 | Aucun cours déclaré |
| A75 — Typhus (I-03-Infectiologie) | A75-A79 | 5 | Aucun cours déclaré |
| A77 — Fièvre pourprée [rickettsioses à tiques] (I-03-Infectiologie) | A75-A79 | 5 | Aucun cours déclaré |
| A78 — Fièvre Q (I-03-Infectiologie) | A75-A79 | 0 | Aucun cours déclaré |
| A79 — Autres rickettsioses (I-03-Infectiologie) | A75-A79 | 4 | Aucun cours déclaré |
| A80 — Poliomyélite aiguë (I-03-Infectiologie) | A80-A89 | 2 | Aucun cours déclaré |
| A82 — Rage (I-03-Infectiologie) | A80-A89 | 1 | Aucun cours déclaré |
| A92 — Autres fièvres virales transmises par des moustiques (I-03-Infectiologie) | A92-A99 | 5 | Aucun cours déclaré |
| A93 — Autres fièvres virales transmises par des arthropodes, non classées ailleurs (I-03-Infectiologie) | A92-A99 | 2 | Aucun cours déclaré |
| A94 — Fièvre virale transmise par des arthropodes, sans précision (I-03-Infectiologie) | A92-A99 | 0 | Aucun cours déclaré |
| A95 — Fièvre jaune (I-03-Infectiologie) | A92-A99 | 2 | Aucun cours déclaré |
| A96 — Fièvre hémorragique à arénavirus (I-03-Infectiologie) | A92-A99 | 4 | Aucun cours déclaré |
| A97 — Dengue (I-03-Infectiologie) | A92-A99 | 4 | Aucun cours déclaré |
| A98 — Autres fièvres hémorragiques virales, non classées ailleurs (I-03-Infectiologie) | A92-A99 | 4 | Aucun cours déclaré |
| A99 — Fièvre hémorragique virale, sans précision (I-03-Infectiologie) | A92-A99 | 0 | Aucun cours déclaré |
| B00 — Infections par le virus de l’herpès [herpes simplex] (I-03-Infectiologie) | B00-B09 | 9 | Aucun cours déclaré |
| B01 — Varicelle (I-03-Infectiologie) | B00-B09 | 3 | Aucun cours déclaré |
| B02 — Zona [herpes zoster] (I-03-Infectiologie) | B00-B09 | 5 | Aucun cours déclaré |
| B03 — Variole (I-03-Infectiologie) | B00-B09 | 0 | Aucun cours déclaré |
| B04 — Monkeypox (I-03-Infectiologie) | B00-B09 | 0 | Aucun cours déclaré |
| B05 — Rougeole (I-03-Infectiologie) | B00-B09 | 6 | Aucun cours déclaré |
| B06 — Rubéole (I-03-Infectiologie) | B00-B09 | 3 | Aucun cours déclaré |
| B07 — Verrues d’origine virale (I-03-Infectiologie) | B00-B09 | 0 | Aucun cours déclaré |
| B20 — Immunodéficience humaine virale [VIH], à l’origine de maladies infectieuses et parasitaires (I-03-Infectiologie) | B20-B24 | 0 | Aucun cours déclaré |
| B21 — Immunodéficience humaine virale [VIH], à l’origine de tumeurs malignes (I-03-Infectiologie) | B20-B24 | 0 | Aucun cours déclaré |
| B22 — Immunodéficience humaine virale [VIH], à l’origine d’autres affections précisées (I-03-Infectiologie) | B20-B24 | 0 | Aucun cours déclaré |
| B23 — Immunodéficience humaine virale [VIH], à l’origine d’autres maladies (I-03-Infectiologie) | B20-B24 | 1 | Aucun cours déclaré |
| B24 — Immunodéficience humaine virale [VIH], sans précision (I-03-Infectiologie) | B20-B24 | 0 | Aucun cours déclaré |
| B25 — Maladie à cytomégalovirus (I-03-Infectiologie) | B25-B34 | 3 | Aucun cours déclaré |
| B26 — Oreillons (I-03-Infectiologie) | B25-B34 | 2 | Aucun cours déclaré |
| B27 — Mononucléose infectieuse (I-03-Infectiologie) | B25-B34 | 2 | Aucun cours déclaré |
| B30 — Conjonctivite virale (I-03-Infectiologie) | B25-B34 | 6 | Aucun cours déclaré |
| B33 — Autres maladies à virus, non classées ailleurs (I-03-Infectiologie) | B25-B34 | 5 | Aucun cours déclaré |
| B34 — Infection virale, siège non précisé (I-03-Infectiologie) | B25-B34 | 6 | Aucun cours déclaré |
| B35 — Dermatophytose [Tinea] (I-03-Infectiologie) | B35-B49 | 9 | Aucun cours déclaré |
| B36 — Autres mycoses superficielles (I-03-Infectiologie) | B35-B49 | 4 | Aucun cours déclaré |
| B37 — Candidose (I-03-Infectiologie) | B35-B49 | 9 | Aucun cours déclaré |
| B38 — Coccidioïdomycose (I-03-Infectiologie) | B35-B49 | 3 | Aucun cours déclaré |
| B39 — Histoplasmose (I-03-Infectiologie) | B35-B49 | 5 | Aucun cours déclaré |
| B40 — Blastomycose (I-03-Infectiologie) | B35-B49 | 3 | Aucun cours déclaré |
| B41 — Paracoccidioïdomycose (I-03-Infectiologie) | B35-B49 | 3 | Aucun cours déclaré |
| B42 — Sporotrichose (I-03-Infectiologie) | B35-B49 | 3 | Aucun cours déclaré |
| B43 — Chromomycose [chromoblastomycose] et abcès phaeohyphomycosique (I-03-Infectiologie) | B35-B49 | 3 | Aucun cours déclaré |
| B44 — Aspergillose (I-03-Infectiologie) | B35-B49 | 4 | Aucun cours déclaré |
| B45 — Cryptococcose (I-03-Infectiologie) | B35-B49 | 4 | Aucun cours déclaré |
| B46 — Zygomycose (I-03-Infectiologie) | B35-B49 | 5 | Aucun cours déclaré |
| B47 — Mycétome (I-03-Infectiologie) | B35-B49 | 2 | Aucun cours déclaré |
| B48 — Autres mycoses, non classées ailleurs (I-03-Infectiologie) | B35-B49 | 8 | Aucun cours déclaré |
| B49 — Mycose, sans précision (I-03-Infectiologie) | B35-B49 | 0 | Aucun cours déclaré |
| B50 — Paludisme à Plasmodium falciparum (I-03-Infectiologie) | B50-B64 | 3 | Aucun cours déclaré |
| B51 — Paludisme à Plasmodium vivax (I-03-Infectiologie) | B50-B64 | 1 | Aucun cours déclaré |
| B52 — Paludisme à Plasmodium malariae (I-03-Infectiologie) | B50-B64 | 1 | Aucun cours déclaré |
| B53 — Autres paludismes confirmés par examen parasitologique (I-03-Infectiologie) | B50-B64 | 3 | Aucun cours déclaré |
| B54 — Paludisme, sans précision (I-03-Infectiologie) | B50-B64 | 0 | Aucun cours déclaré |
| B55 — Leishmaniose (I-03-Infectiologie) | B50-B64 | 4 | Aucun cours déclaré |
| B56 — Trypanosomiase africaine (I-03-Infectiologie) | B50-B64 | 3 | Aucun cours déclaré |
| B57 — Maladie de Chagas (I-03-Infectiologie) | B50-B64 | 4 | Aucun cours déclaré |
| B58 — Toxoplasmose (I-03-Infectiologie) | B50-B64 | 4 | Aucun cours déclaré |
| B60 — Autres maladies dues à des protozoaires, non classées ailleurs (I-03-Infectiologie) | B50-B64 | 6 | Aucun cours déclaré |
| B64 — Maladie due à des protozoaires, sans précision (I-03-Infectiologie) | B50-B64 | 0 | Aucun cours déclaré |
| B65 — Schistosomiase [bilharziose] (I-03-Infectiologie) | B65-B83 | 6 | Aucun cours déclaré |
| B66 — Autres infections par douves [distomatoses] (I-03-Infectiologie) | B65-B83 | 8 | Aucun cours déclaré |
| B67 — Echinococcose (I-03-Infectiologie) | B65-B83 | 2 | Aucun cours déclaré |
| B68 — Infection à Taenia [téniase] (I-03-Infectiologie) | B65-B83 | 3 | Aucun cours déclaré |
| B69 — Cysticercose (I-03-Infectiologie) | B65-B83 | 2 | Aucun cours déclaré |
| B70 — Diphyllobothriase et sparganose (I-03-Infectiologie) | B65-B83 | 2 | Aucun cours déclaré |
| B71 — Autres infections à cestodes (I-03-Infectiologie) | B65-B83 | 4 | Aucun cours déclaré |
| B72 — Dracunculose (I-03-Infectiologie) | B65-B83 | 0 | Aucun cours déclaré |
| B73 — Onchocercose (I-03-Infectiologie) | B65-B83 | 0 | Aucun cours déclaré |
| B74 — Filariose (I-03-Infectiologie) | B65-B83 | 5 | Aucun cours déclaré |
| B75 — Trichinose (I-03-Infectiologie) | B65-B83 | 0 | Aucun cours déclaré |
| B76 — Ankylostomiase (I-03-Infectiologie) | B65-B83 | 3 | Aucun cours déclaré |
| B77 — Ascaridiase (I-03-Infectiologie) | B65-B83 | 1 | Aucun cours déclaré |
| B78 — Anguillulose [strongyloïdose] (I-03-Infectiologie) | B65-B83 | 1 | Aucun cours déclaré |
| B79 — Infection à Trichuris trichiuria (I-03-Infectiologie) | B65-B83 | 0 | Aucun cours déclaré |
| B80 — Oxyurose (I-03-Infectiologie) | B65-B83 | 0 | Aucun cours déclaré |
| B81 — Autres helminthiases intestinales, non classées ailleurs (I-03-Infectiologie) | B65-B83 | 5 | Aucun cours déclaré |
| B82 — Parasitose intestinale, sans précision (I-03-Infectiologie) | B65-B83 | 1 | Aucun cours déclaré |
| B83 — Autres helminthiases (I-03-Infectiologie) | B65-B83 | 6 | Aucun cours déclaré |
| B85 — Pédiculose et phtiriase (I-03-Infectiologie) | B85-B89 | 4 | Aucun cours déclaré |
| B86 — Gale (I-03-Infectiologie) | B85-B89 | 0 | Aucun cours déclaré |
| B87 — Myiase (I-03-Infectiologie) | B85-B89 | 5 | Aucun cours déclaré |
| B89 — Parasitose, sans précision (I-03-Infectiologie) | B85-B89 | 0 | Aucun cours déclaré |
| B90 — Séquelles de tuberculose (I-03-Infectiologie) | B90-B94 | 1 | Aucun cours déclaré |
| B91 — Séquelles de poliomyélite (I-03-Infectiologie) | B90-B94 | 0 | Aucun cours déclaré |
| B92 — Séquelles de lèpre (I-03-Infectiologie) | B90-B94 | 0 | Aucun cours déclaré |
| B94 — Séquelles de maladies infectieuses et parasitaires, autres et non précisées (I-03-Infectiologie) | B90-B94 | 1 | Aucun cours déclaré |
| B95 — Streptocoques et staphylocoques, cause de maladies classées dans d’autres chapitres (I-03-Infectiologie) | B95-B98 | 4 | Aucun cours déclaré |
| B96 — Autres agents bactériens précisés, cause de maladies classées dans d’autres chapitres (I-03-Infectiologie) | B95-B98 | 5 | Aucun cours déclaré |
| B97 — Virus, cause de maladies classées dans d’autres chapitres (I-03-Infectiologie) | B95-B98 | 3 | Aucun cours déclaré |
| B98 — Autres micro-organismes infectieux précisés, cause de maladies classées dans d’autres chapitres (I-03-Infectiologie) | B95-B98 | 1 | Aucun cours déclaré |
| B99 — Maladies infectieuses, autres et non précisées (I-03-Infectiologie) | B99-B99 | 0 | Aucun cours déclaré |
| U04 — Syndrome respiratoire aigu sévère [SRAS] (I-03-Infectiologie) | U00-U49 | 1 | Aucun cours déclaré |
| U07 — Maladies d’étiologie incertaine, codes U07.- affectés et non affectés (I-03-Infectiologie) | U00-U49 | 4 | Aucun cours déclaré |
| U08 — Antécédents personnels de COVID-19 (I-03-Infectiologie) | U00-U49 | 1 | Aucun cours déclaré |
| U09 — État post-COVID-19 (I-03-Infectiologie) | U00-U49 | 1 | Aucun cours déclaré |
| U10 — Syndrome inflammatoire multisystémique associé au COVID-19 (I-03-Infectiologie) | U00-U49 | 1 | Aucun cours déclaré |
| U11 — Nécessité d’une vaccination contre le COVID-19 (I-03-Infectiologie) | U00-U49 | 1 | Aucun cours déclaré |
| U12 — Effets secondaires indésirables de l’utilisation de vaccins contre le COVID-19 (I-03-Infectiologie) | U00-U49 | 1 | Aucun cours déclaré |
| U80 — Micro-organismes Gram positifs résistants à certains antibiotiques et nécessitant des mesures thérapeutiques ou hygiéniques spéciales (I-03-Infectiologie) | U80-U85 | 5 | Aucun cours déclaré |
| U81 — Micro-organismes Gram négatifs résistants à certains antibiotiques et nécessitant des mesures thérapeutiques ou hygiéniques spéciales (I-03-Infectiologie) | U80-U85 | 9 | Aucun cours déclaré |
| U82 — Mycobactéries résistantes aux antituberculeux (de première ligne) (I-03-Infectiologie) | U80-U85 | 3 | Aucun cours déclaré |
| U83 — Champignons pathogènes pour l’homme avec résistance aux antifongiques (I-03-Infectiologie) | U80-U85 | 4 | Aucun cours déclaré |
| U84 — Virus de l’Herpès résistants aux virostatiques (I-03-Infectiologie) | U80-U85 | 0 | Aucun cours déclaré |
| U85 — Virus de l’immunodéficience humaine résistant aux virostatiques ou aux inhibiteurs de protéases (I-03-Infectiologie) | U80-U85 | 0 | Aucun cours déclaré |
| U99 — Codes U99.-! affectés et non affectés (I-03-Infectiologie) | U98-U99 | 1 | Aucun cours déclaré |

## Références locales consultées

- `AGENTS.md`
- `organisation/fragments.json`
- `organisation/production_plan.json`
- `organisation/README.md`
- `fragments.json`
- `chapters.json`
- `shell/medina_front.html`
- `shell/data.py`
- `tools/build_organisation.py`
- `docs/COMPLETUDE_CIM11.md`
- `docs/collaboration/SOURCES_CANONIQUES.md`
- `docs/collaboration/FRAGMENTS_RESTANTS.md`
- `docs/collaboration/CODEX_CHAINE_FRAGMENTS.md`
- `docs/collaboration/DELIVERIES_LATEST.md`
- `docs/collaboration/receipts/CODEX_A41_E330776_REMIS_CLAUDE_2026-10-08.json`
- `audits/COMPLETUDE_2026-10-07/catalogue-coverage.json`
- `audits/COMPLETUDE_2026-10-07/README.md`
- `audits/A41.md`
- `livraisons/Livraison Codex/I-03-Infectiologie/livraison.json`
- `livraisons/Livraison Codex/I-03-Infectiologie/travail/A41-2026-10-08/INVENTAIRE_BASE.md`
- `livraisons/Livraison Codex/I-03-Infectiologie/travail/A41-2026-10-08/rapport.md`

## Inventaire JSON compagnon

`/workspace/work/inventaire-i03.json` contient les 155 catégories avec titres et blocs, 450 sous-codes locaux, cours et chemins seulement quand déclarés, 29 rapprochements transversaux, 10 priorités, 17 preuves de sources au SHA exact main a6f82b6e359a5087b3271f66d590ac02f46d23bf, 10 contrôles d’empreintes du dépôt A41 partagé et 9 copies canoniques vérifiées. Aucun mapping ni dénominateur CIM-11 inventé.
