MEDINA — SSP, Audit Alpha, production et prévention des conflits — V2
15 octobre 2026. Instruction actuelle de Vial. Périmètre : S08/S05/S04/S06.

1. CE QUI FAIT FOI

Le plan V2 remplace les nombres et attributions de planification Alpha V1 pour
les quatre systèmes actuels. Il remplace l'obligation d'audit croisé dans ce
chantier Alpha. Les anciens documents, validations et empreintes restent des
preuves historiques de leurs versions. Aucun système antérieur n'est réécrit.
Codex et Claude ont les mêmes règles et possibilités locales ; les droits réels
de GitHub relèvent des comptes et applications connectés. Aucune instruction
ancienne de leadership ne permet d'écraser un travail concurrent.

Le plan et ses 270 fiches sont préparés, non lancés. Une fiche dans
missions-planifiees n'est pas une mission active dans .medina/missions.
Une attribution n'atteste ni audit clinique effectué ni production terminée.
La diffusion existante en l'état reste distincte de l'audit médical à venir.

2. COMPTAGE REPRODUCTIBLE, SANS FAUSSE CERTITUDE

PROFILES 2017 contient exactement 265 SSP pour l'ensemble des 23 fragments.
Une SSP est une présentation ou situation de consultation, pas un diagnostic.
Le résultat recherché est : présentation -> hypothèses/différentiels pertinents
-> critères discriminants et source -> concept clinique -> CIM-10-GM -> leçon
mère et propriétaire actuel. La CIM classe, elle ne prouve pas la pertinence à
l'examen fédéral. Il n'existe pas ici de correspondance officielle SSP/CIM.

Une catégorie à trois caractères compte pour une leçon mère dans ce plan.
Ses sous-codes constituent un périmètre à couvrir dans cette leçon, jamais un
nombre automatique de cours. Un syndrome ou code de symptôme ne devient pas
une étiologie par simple rattachement. Les codes astérisque, exclusions,
inclusions et étiologies associées sont vérifiés avant attribution.

Les 247 cibles historiques sont conservées par prudence, sans prétendre les
avoir toutes revalidées. Onze catégories auparavant en réserve disposent de
liens documentés et rejoignent le périmètre éditorial :
S08 D32/G10/G12 ; S05 D34/E15/E16/E80/E83/E88/E89 ; S06 D47.

S08 Neurologie : 107 cibles = 57 existantes + 50 à produire ; réserve 9.
S05 Endocrinologie : 75 = 26 + 49 ; réserve 2.
S04 Néphrologie : 33 = 6 + 27 ; réserve 0.
S06 Hématologie : 43 = 15 + 28 ; réserve 1.
Total conservatoire : 258 = 104 + 154 ; 12 réserves non exclues.
Ce nombre est un périmètre de travail provisoire, pas « 258 maladies fédérales
certifiées ». Chaque preuve porte seulement sur l'entité et le lien examinés.
Une catégorie documentée n'a pas tous ses sous-codes automatiquement validés.

Les anciens 1967 éléments vides étaient 143 catégories racines et 1824
sous-codes. Ce nombre V1 n'est ni celui des leçons nouvelles ni une preuve
d'exhaustivité des différentiels. L'annexe globale affichant 291 est historique :
le même algorithme de couverture appliqué à l'état actuel produit 398. Aucun
de ces deux résultats gloutons ne démontre un besoin clinique ou pédagogique.

Les sept libellés SSP tronqués ont leur version complète dans
ssp-labels-corriges.json ; la source PROFILES et les pages sont tracées.
Les annexes globales des autres systèmes ne sont pas régénérées.

3. RÉPARTITION SANS DOUBLER UNE LEÇON

Audit existant : Codex/Claude = 52/52.
Par système S08 29/28 ; S05 13/13 ; S04 3/3 ; S06 7/8.
Production : 77/77. S08 25/25 ; S05 25/24 ; S04 13/14 ; S06 14/14.
Réserve : 6/6. S08 4/5 ; S05 1/1 ; S06 1/0.
Chaque chapitre CIM conserve un écart d'au plus une leçon par mode.
Le volume sert de proxy de charge, pas de certification de difficulté médicale.
Une leçon entière reste sous un seul responsable ; aucune moitié de fichier
partagée. Les sous-agents sont comptés dans leur responsable Codex ou Claude.

Pilote prévu : quatre leçons, puis au plus deux missions source simultanées
par responsable au départ. Les lots sont logistiques : une leçon prête peut
être livrée sans attendre un fragment complet ou toutes les autres missions.
Les lecteurs libres peuvent préparer des notes hors dépôt sans réservation ;
toute mutation d'une source, d'un rapport réservé ou d'un fichier partagé suit
le chemin contrôlé. Il n'est pas nécessaire de demander à Vial chaque tâche :
le coordinateur applique les attributions et trace les transferts.

4. ENTRÉE OBLIGATOIRE DE TOUTE IA, MÊME UNE NOUVELLE CONVERSATION

main est l'unique référence d'intégration. Aucun second main indépendant :
deux historiques durables ne font que déplacer les divergences. Une branche
et un worktree propres sont créés par mission depuis un SHA précis de main.
Un clone indépendant est possible ; il doit utiliser le même registre distant.
Le gestionnaire local conversation_workspace.py ne constitue pas ce registre,
et son nom de branche généré n'est pas automatiquement celui du manifeste.

1) Lire ce document, prompt-commun-ia.yaml, AGENTS.md et CLAUDE.md actualisés.
2) Examiner les branches, PR, livraisons et réservations actives, avec pagination.
3) Faire approuver la mission dans main par un coordinateur de gouvernance.
   Champs : ID, acteur, conversation, responsable, rôle, code(s), base SHA40,
   génération positive, branche exacte, chemins. Jamais d'auto-approbation par
   ajout de son propre manifeste dans la PR de cours.
4) Lire le SHA courant, acquérir au registre distant, conserver son reçu.
5) Créer le worktree et la branche exacts ; vérifier start avant toute écriture.

MODÈLE DE COMMANDES — remplacer les valeurs par celles du manifeste approuvé.
Les tests d'intégration de l'outil exécutent les scénarios ; ces exemples ne
prétendent pas démarrer les 270 missions planifiées.

git fetch origin '+refs/heads/*:refs/remotes/origin/*'
MEDINA_BASE=$(git rev-parse origin/main)
MEDINA_MISSION='ID_APPROUVE'
MEDINA_TASK_BRANCH='BRANCHE_EXACTE_DU_MANIFESTE'
MEDINA_TASK_DIR='../medina-taches/ID_APPROUVE-GENERATION'
python3 tools/ai_session_guard.py status --base "$MEDINA_BASE"
python3 tools/ai_session_guard.py acquire "$MEDINA_MISSION" --base "$MEDINA_BASE"
git worktree add -b "$MEDINA_TASK_BRANCH" "$MEDINA_TASK_DIR" "$MEDINA_BASE"
python3 tools/ai_session_guard.py start "$MEDINA_MISSION" --base "$MEDINA_BASE" --actor IA_DECLAREE --conversation CONVERSATION_EXACTE --worktree "$MEDINA_TASK_DIR"

L'outil refuse une base non exacte, une mission absente/inactive, une collision
de code source ou chemin, une génération périmée et un worktree incorrect.
Deux audits peuvent lire un même code, mais leurs rapports ont des chemins
distincts. Le rôle audit ne permet aucune écriture de source canonique.
Deux conversations de Codex sont aussi concurrentes que Codex et Claude.

Si acquire réussit mais la création du worktree échoue, conserver le reçu et
libérer explicitement la réservation après constat ; ne pas inventer une
autre branche ou reprendre un dossier appartenant déjà à une conversation.

5. ATTRIBUTION CENTRALE, GÉNÉRATIONS ET RELAIS

Le registre réel est la branche medina/session-registry. Chaque écriture crée
un commit enfant du SHA lu, puis utilise un push normal sans force. Deux
enfants concurrents ne peuvent pas tous deux avancer cette référence. Le
perdant relit les réservations et recalcule sa demande ; aucun retry aveugle.
Le reçu pointe vers le commit accepté. Le registre conserve les libérations,
les générations et leurs motifs ; aucune expiration ne rend un cours libre.

La CI confronte le manifeste de la base de confiance à la réservation active
du registre. Une ancienne génération ne peut pas fournir une livraison
recevable dans ce chemin contrôlé. Une identité --actor reste déclarative.

Le mandat initial SSPV2-GOUVERNANCE-INITIALISATION ne réserve que .medina : il
n'autorise aucun cours. Avant de fermer le dernier mandat de gouvernance,
faire approuver son relais avec un ID, une branche et une conversation propres.
Le relais peut fermer le précédent et préparer le suivant ; aucune mission
ne modifie sa propre approbation. Les réservations de gouvernance seules ne
consomment pas le verrou de génération des sources médicales.

Transfert : sauvegarder SHA/diff/preuves ; libérer avec motif ; le coordinateur
approuve une nouvelle génération et ses chemins dans une PR distincte ; le
nouvel intervenant acquiert depuis main frais. Un ancien auteur hors ligne
peut encore calculer localement, mais son ancienne génération est refusée.
Si tout accès réseau est indisponible : poursuivre les lectures et calculs
locaux déjà exclusifs ; aucune nouvelle attribution ou intégration partagée.

6. SORTIES, PREUVES ET CHARGE EN TOKENS

Chaque mission a son dossier de rapport réservé :
docs/collaboration/ssp-v2/execution/<ID>/
L'auteur a aussi ses chemins chapters/<CODE> et glossary/<code>.py. Toute
figure partagée, clé de glossaire globale, dépendance commune, catalogue,
nosologie ou workflow exige une mutation d'intégration distincte et attribuée.
Utiliser un MEDINA_OUT et un dossier de captures uniques ; ne jamais partager
dist, _site, un cache mutable ou un index Git entre conversations actives.

Conserver : recherche ciblée, source/URL/éditeur/version/date/page, constat
localisé, proposition appliquée, diff et empreintes, résultat réel du contrôle,
réserves et captures. Un cache de preuves inclut contenu/empreinte et lecteur,
passage et population ; sa réutilisation est attribuée sans inventer une
nouvelle lecture. Invalider si contenu, population, décision ou dépendance
change. Charger le socle une fois, puis les deltas et passages utiles.

7. AUDIT MÉDICAL ET FRANÇAIS

Audit exigeant de toutes les surfaces du cours : onglets, fenêtres, tableaux,
figures, quiz, résumé, glossaire, sous-codes explicitement couverts. Chaque
rubrique du canevas des 20 reçoit couvert avec preuve, sans objet motivé ou
LACUNE. Les sources suisses applicables précèdent les européennes. Aucune
affirmation médicale n'est validée par mémoire du modèle ou par un lien URL
non ouvert. Pour les médicaments : information professionnelle suisse du
produit exact et version, forme, dose, voie, fréquence, durée, maximum,
adaptations et contre-indications applicables, sans élargir une indication.

La rédaction conduit du normal au mécanisme, à la conséquence puis à la
décision. Elle reste précise, élégante et attrayante ; les phrases complètes
et les transitions servent la compréhension. Conserver chiffres, négations,
conditions, exceptions et degrés d'incertitude lors des reformulations.
Chaque différentiel possède un contexte et un discriminant sourcé ; une
énumération de toutes les maladies connues n'est pas une bonne démarche.

Alpha ne comporte pas d'audit croisé systématique. L'IA responsable reste
responsable de la relecture et des corrections de ses leçons. Une auto-relecture
n'est jamais appelée audit indépendant. Une vérification ciblée finale reste
proportionnée au risque ; aucun score de perfection ou audit final nul promis.

8. INTÉGRATION, PUBLICATION ET ÉTATS HONNÊTES

Livrer une PR portant un diff ciblé, base/final SHA40, mission/génération,
empreintes et preuves. Rafraîchir main avant la livraison. Si main a avancé,
intégrer sa nouvelle tête dans sa propre branche ou créer un nouveau candidat
et rejouer les seuls commits utiles ; ne jamais réécrire une branche tierce.
Les opérations partagées suivent une file versionnée et un intégrateur à la
fois. Préserver une demande tant que son reçu manque. Actions concurrency
seul peut supprimer une exécution pending et ne remplace pas cette file.

Avant fusion : exécuter le contrôle de mission sur le candidat final et le main
courant, les contrôles structurels et de contenu réellement concernés, puis
les workflows obligatoires sur le SHA exact. L'intégrateur reconstruit les
catalogues depuis les sources actuelles, sans copier une ancienne version
entière. Un push non-fast-forward échoue et entraîne une nouvelle comparaison.

Les anciennes sources publiées en l'état restent liées à leur reçu initial.
Une correction médicale future n'utilise jamais ce reçu comme autorisation
d'écraser ses octets. Avant la première correction canonique : créer et tester
le reçu de version Alpha borné au cours, avant/après, preuves, statuts réels et
instruction actuelle ; adapter les gardes de publication dans une mission
technique distincte. Ce chemin n'est pas prétendu réalisé par ce dossier.
Les missions d'audit peuvent livrer leurs constats sans modifier les sources.

Après fusion : distinguer « intégré » de « construit » puis « publié ».
Vérifier le commit construit, publication.json, audit/sources.json, les routes
et empreintes publiques. Un build réussi ou une branche distante ne prouve
aucune validation médicale. Ne pas promouvoir les statuts historiques.

Après intégration vérifiée, sauvegarder la livraison puis libérer :
python3 tools/ai_session_guard.py release "$MEDINA_MISSION" --base "$MEDINA_BASE" --generation GENERATION --reason 'Livraison conservee, integration verifiee'

9. STRATÉGIE DE RÉCUPÉRATION PAR INCIDENT

Collision d'acquisition : garder sa branche intacte, relire registre, prendre
un autre cours libre ou demander un transfert tracé. Ne jamais voler le bail.
Conflit de texte : fixer base/livraison/main, créer branche depuis main frais,
rejouer le petit diff, résoudre seulement les lignes concernées avec preuves.
Conflit sémantique sans conflit Git : comparer code mère/covers/alias/sous-code,
propriétaire et liens partagés ; suspendre seulement la publication affectée.
Catalogue : recalculer l'ajout depuis main courant ; préserver exactement les
lignes hors mission ; tester routes/doublons et reconstruire les dépendances.
Source médicale contradictoire : appliquer la source primaire applicable,
documenter population/version et désaccord ; ciblage du veto, pas arrêt global.
Génération ancienne : conserver son travail comme proposition, pas livraison
active ; propriétaire actuel reprend le diff utile et renouvelle les preuves.
Build ou lien cassé : corriger dans la mission propriétaire de la dépendance ;
les autres cours peuvent poursuivre leurs lectures et leurs livraisons isolées.
Mauvais déploiement : conserver le dernier site publié ; corriger un candidat
neuf, vérifier ses sources puis publier avec un nouveau reçu. Ne pas effacer
un historique ou un audit pour donner l'apparence d'une progression parfaite.

Interdits : force/force-with-lease sur main, reset destructeur du travail tiers,
suppression d'une branche tierce, ours/theirs aveugle, fusion globale d'un
ancien arbre, libération silencieuse et validation clinique inventée.

10. APPLICATION RÉELLE ET LIMITE DES POUVOIRS

Implémenté : outils de réservation/start/check/release/status, contrôle CI
pull_request_target exécutant le script de la base et lisant le candidat comme
données Git, tests multiprocessus, refus de chemins/générations et altérations
de catalogue hors cours. Le contrôle après push main est diagnostique : un
refus après écriture ne peut pas empêcher cette écriture.

À imposer côté GitHub : PR obligatoire vers main, contrôle requis strict
« MEDINA / mission et périmètre », source de contrôle protégée, actualisation
avant fusion, interdiction force/suppression et contournements, gouvernance
des workflows et de la branche registre. Ce dépôt public personnel ne possède
pas la merge queue réservée aux dépôts d'organisation éligibles. Le séquencement
par intégrateur et la vérification de main frais restent nécessaires.

L'application connectée n'a pas le droit Administration : la lecture et la
tentative de configuration sont conservées dans le reçu GitHub. Un code403
n'est pas une preuve qu'aucune ancienne protection n'existe. Les rulesets
publics ont été lus vides au moment du contrôle. Les pages de réglage et
manœuvres sont dans AUTORISATIONS_GITHUB.csv et le PDF de protocole.

Un required check Actions peut être usurpé par un autre workflow du même nom
si les workflows ne sont pas protégés. --actor n'authentifie personne et un
compte partagé ne sépare pas Codex et Claude. Aucune garantie zéro collision,
zéro blocage ou contrainte absolue sur un administrateur ayant un droit de
contournement ne découle de ce prompt. Les règles réduisent les collisions
accidentelles, rendent les livraisons contrôlables et conservent une reprise.

11. FICHIERS À CONSULTER SELON LE BESOIN

prompt-commun-ia.yaml : contrat compact destiné à toute IA.
plan-v2.json et attributions-*.csv : responsabilité par cours/chapitre/fragment.
missions-planifiees/ : 270 fiches, non actives, génération zéro.
preuves-S08/S05/S04/S06.json : sources, sections lues et limites originales.
graphe-ssp-diagnostics.json/csv : arêtes normalisées et provenance de chaque lien.
couverture-265-ssp.json/csv : SSP avec liens et absences documentées.
methodologie.json : référentiel primaire, limites du calcul historique et GitHub.
validation-independante.json : contrôles réels de répartition et d'intégrité.
recu-registre.json, recu-github.json, tests-garde.log : preuves d'installation.
Les trois PDF : audit, production par fragment et protocole détaillé.
