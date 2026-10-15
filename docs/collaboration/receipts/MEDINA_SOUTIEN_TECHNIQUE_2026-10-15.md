# Réparations techniques MEDINA — 15 octobre 2026

État : correctifs préparés et testés en branche Codex ; pas de nouvelle injection
médicale, pas de validation clinique ni de déploiement de ces correctifs annoncé.

## Provenance et concurrence

- Main réconcilié : `75500d40543cadeafe3bcea97ca074c4c6afed3a` (PR99 déjà fusionnée).
- PR99 Claude : `593e79d67cb68d89891ff50cde1f73b2c6d54cab`, session
  `session_01UbEdt1NLCVRTY6pw1YsPBE`. C72 n'est pas réinjecté par Codex.
- Première séquence Claude : base `5569c4375212056bff7cf0696462029c9dd2f19d`,
  puis `ed8b38132155b71e11a692df40406e6fccc913d8`, session
  `session_018toCfLY3F4d6361mEXeZ8d`. Plan, distributeur et dernier filtre
  anti-écho conservés ; reprise adaptée au relevé dynamique et au canal PR.
- Proposition Codex PR98 : `96629b98c1924f4b7ef4313c34c614a84e3c9595`,
  reprise sans rétablir les audits suspendus.
- Snapshot distant : 75 branches, 8 PR ouvertes, secondes pages vides,
  dans `MEDINA_SOUTIEN_INVENTAIRE_2026-10-15.json`. Les autres contributions
  ne sont pas fusionnées à l'aveugle.

## Correctifs et prévention

1. **Reprise** : compteurs locaux calculés, trois pistes séparées, aucun catalogue
   assimilé à une preuve publique. Ancien script reconstruisant main rendu inerte.
2. **Veille CloV_2** : pagination complète, curseurs transactionnels par source,
   recouvrement temporel, dédoublonnage et filtre anti-écho Claude conservé. Une
   erreur reste explicite et ne consomme pas les événements de la source échouée.
3. **Inventaire** : conservation des pages partielles et rapport d'erreur. L'échec
   réseau du relevé informatif ne bloque plus le workflow ; ses tests restent
   bloquants. Aucun droit GitHub n'a été élevé et aucun 403 n'est déclaré réparé.
4. **Novo Tétrade** : option future de douze leçons couvrant trois anciens cycles,
   douze preuves individuelles et déploiement commun possible. Cycle3 inchangé.
5. **Novo Betta** : raccord distinct du plan42–125 reçu dans PR99, transferts
   exclus des anciennes autorisations ; préflight complet du lot et porte de
   vérité avant copie. Sources, manifeste, empreintes et catalogue réconciliés.
   Retour arrière sur erreur d'écriture ordinaire, sans supprimer les modifications
   concurrentes ; pas de garantie d'atomicité après SIGKILL/panne système.
6. **Pages** : ne reconstruire que si la comparaison vérifiée le justifie ; toute
   source ou voie inconnue déclenche le build complet. Cache de téléchargements
   seulement, jamais de contrôles réputés réussis.
7. **Chargeur des glossaires** : suppression centrale des découvertes récursives
   reconnues par AST, sans réécrire les 180 fichiers. Chargement mesuré à0,59s ;
   4488 clés. Priorité explicite : modules ordinaires, puis ajouts conditionnels
   sans écrasement. L'ancien résultat récursif n'aboutissant pas, une identité de
   rendu avec celui-ci ne peut pas être certifiée. Aucun arbitrage clinique.

## Contrôles réellement exécutés

- 357 tests ciblés réussis : gardes d'espace, chaîne historique et Claude,
  Novo Tétrade, Betta/Novo et injecteur, veille, reprise, inventaire, moteur,
  portée Pages, manifeste public et chargeur des glossaires.
- Parmi eux : 45 tests dédiés Betta/Novo ; 15 du chargeur, avec comparaison
  des empreintes de tous les glossaires ; 18 du contrat Novo Tétrade.
- Construction globale et 23 fragments terminés. Le build signale encore
  des termes non couverts dans J44, J96 et I51 : aucune correction médicale
  silencieuse ni relecture exhaustive revendiquée.
- Compilation Python et vérification des espaces effectuées.
- Comparaison avec main : aucun changement de `chapters/`, `glossary/`,
  `chapters.json`, intégrité nosologique, registres médicaux ou attributions.
- Suite complète tentée :584 tests,2 échecs et4 erreurs, liés aux fichiers
  non matérialisés dans le clone partiel (inventaires/archives/aperçu). Ce n'est
  pas une réussite de la suite complète ; exiger son contrôle sur clone complet.

## Réserves et suite

Chromium est absent ; son téléchargement a retourné des archives tronquées.
Aucun contrôle navigateur ordinateur/mobile n'a été exécuté ici. La garde Git
globale et le scanner exhaustif ont été lancés, mais leur résultat final n'est
pas acquis à cette coupure : ne pas les déclarer réussis. Le connecteur a permis
le relevé paginé des têtes et PR consigné séparément.

La CI distante et le déploiement de la branche réparée restent à vérifier.
Ne pas annoncer de mise en production ni forcer une fusion sur cette base.
Les écarts du JSON Novo Betta à la promesse «4×3 partout» sont laissés à Claude :
dix cycles ont cinq agents, des fragments répétés en fin de plan, dernier lot125
de cinq leçons. Le raccord suit les listes déclarées sans redistribution.

Le soutien reste événementiel et activé ; pas de promesse à la milliseconde.
Le rappel demandé par Vial (publication des cours réellement prêts, liens de
contrôle et jauges colorées dans ses chats Claude) est transmis dans
[l'issue97](https://github.com/vialdjoukang-spec/Medina/issues/97#issuecomment-6193265509).
Lecture et exécution par Claude non confirmées.
