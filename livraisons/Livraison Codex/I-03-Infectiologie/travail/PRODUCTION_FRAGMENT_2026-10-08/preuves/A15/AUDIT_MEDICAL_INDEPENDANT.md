# A15 — revue médicale indépendante, 8 octobre 2026

## Verdict

**Les deux bloquants initiaux et la précision de suivi visuel sont corrigés dans le réassemblage.** Le noyau clinique est cohérent avec les sources suisses lues directement. Le conflit sur l’allaitement apparaît désormais dans `A15_d.html` §3 et `A15_pop2.html` ; A15.8 avec ses sites apparaît dans `A15_a.html` §4 et `A15_pop_pa.html`, avec référence à l’OFS 2024 p. 8 ; `A15_d.html` §3 mentionne maintenant l’examen visuel avant traitement puis toutes les quatre semaines. Les sections ci-dessous conservent le constat initial pour la traçabilité.

## Bloquant 1 — conflit sur l’allaitement omis, corrigé

**Fichiers :** `A15_d.html`, §3 « Contre-indications et interactions » ; `A15_pop2.html`, tableau ligne « Grossesse ».

Le guide OFSP–Ligue pulmonaire *Tuberculose en Suisse* V1.2024, §7.3, p. 40, dit textuellement : « Grossesse et allaitement : le schéma thérapeutique standard (2HRZE / 4HR) est recommandé. » Le cours cite cette phrase et explique correctement le conflit **grossesse** avec les FI, mais n’explicite pas le conflit **allaitement**. Les FI suisses exactes, directement lues le 08.10.2026, disent :

- Rimstar n°56768, FI avril 2026, « Allaitement » : « la préparation ne doit donc pas être utilisée pendant l’allaitement » ; si traitement absolument nécessaire, « il faut arrêter l’allaitement ».
- Rimactazid n°56769, FI avril 2026, même restriction et arrêt de l’allaitement en cas de nécessité absolue.
- Myambutol n°33153, FI août 2024 : « Il faut arrêter l’allaitement avant et pendant un traitement par éthambutol. »

**Correction demandée :** dans le texte pharmacologique et la fenêtre de comparaison, séparer grossesse et allaitement et citer les restrictions FI de **chaque produit**. Expliquer que le schéma recommandé par le guide ne valide pas automatiquement ces spécialités pendant l’allaitement ; décision spécialisée et information de la personne, sans inventer une alternative ni retarder le soin d’une tuberculose active.

Sources : [guide national, §7.3](https://www.bag.admin.ch/dam/fr/sd-web/fPW7HAdyOiZ0/tuberkulose-handbuch.pdf) ; [FI Rimstar](https://www.swissmedicinfo.ch/ShowText.aspx?textType=FI&lang=FR&authNr=56768) ; [FI Rimactazid](https://www.swissmedicinfo.ch/ShowText.aspx?textType=FI&lang=FR&authNr=56769) ; [FI Myambutol](https://www.swissmedicinfo.ch/ShowText.aspx?textType=FI&lang=FR&authNr=33153).

## Bloquant 2 — catégorie A15.8 non couverte explicitement, corrigé

**Fichiers :** `A15_a.html`, §1/§4 ; `A15_b.html`, §7/§13 ; `A15_pop_pa.html`/`A15_pop1.html` ; inventaire local `docs/collaboration/reviews/2026-10-08/REPRISE_FRAGMENTS/INVENTAIRE_I03.json`.

L’[OFS, CIM-10-GM **2024**, index systématique français, p. 8/PDF 18](https://dam-api.bfs.admin.ch/hub/api/dam/assets/32686249/master) contient **A15.8**, « autres formes de tuberculose de l’appareil respiratoire », avec exemples *médiastinale, nasale, rhinopharyngée et des sinus de la face*. Le [BfArM allemand 2024](https://klassifikationen.bfarm.de/icd-10-gm/kode-suche/htmlgm2024/block-a15-a19.htm#A15) concorde sur l’existence du sous-code et ces sites. L’inventaire local saute A15.8. Le cours au titre A15 entier donne le poumon, les voies aériennes, les ganglions et la plèvre, mais ne décrit pas explicitement cette branche anatomique. Une simple mention sourcée dans la présentation et le bilan de site suffit ; aucun tableau thérapeutique inventé n’est nécessaire. Corriger l’inventaire historique via son propriétaire si l’édition directe relève d’un autre flux.

**Nuance de nomenclature :** l’OFS français 2024 écrit « **et** histologique » dans le seul libellé A15.9, tandis que l’intitulé A15.- officiel écrit « **ou** » et le BfArM allemand A15.9 écrit « oder ». Ne pas présenter le « et » de l’inventaire comme une simple erreur de transcription ni en déduire qu’il faudrait toutes les modalités pour classer A15.9. Le PDF OFS 2024 est une source suisse officielle du **périmètre historique 2024**, sans preuve à lui seul du millésime de facturation 2026.

## Précision utile — examen visuel de l’éthambutol, corrigée

`A15_d.html`, §3 dit que la FI Myambutol demande un examen visuel et une surveillance ; c’est exact, mais trop peu concret pour une section de prescription. Sa FI §« Mises en garde et précautions » précise acuité visuelle, champ et couleurs **avant traitement puis à intervalles réguliers de quatre semaines**. Ajouter cet intervalle avec l’attribution FI et rappeler la conduite devant nouveau trouble visuel. Le texte actuel ne prétend pas que l’absence de suivi est acceptable : c’est une précision, pas une contradiction.

## Vérifications qui passent

| Sujet | Constat direct |
|---|---|
| Schéma de référence | Guide 2024 §7.1, p. 36–37 : 2 mois HRZE quotidiens puis 4 mois HR ; doses adultes tableau 7-1 H 5, R 10, Z 25, E 15 mg/kg/j. Le cours conditionne correctement le schéma à l’espèce, la sensibilité et au patient. |
| FI et poids | FI Rimstar 56768 et Rimactazid 56769 d’avril 2026 : 2/3/4/5 comprimés selon 30–37/38–54/55–70/≥71 kg ; avertissement de dépassement des plafonds usuels à 5 comprimés. Le cours ne calcule pas de dose pour la vignette sans poids. FI Myambutol 33153 : jusqu’à 25 mg/kg/j en phase initiale, distinct du repère national standard 15 mg/kg/j. |
| Grossesse | Guide 2024 §7.3 recommande schéma standard ; FI Rimstar et Myambutol contre-indiquent la grossesse ; Rimactazid seulement si nécessité absolue. Conflit présenté correctement. |
| Déclaration | [OFSP 2026, fiche 58, p. 116–117](https://www.bag.admin.ch/dam/fr/sd-web/MDjbgfEN6jEf/250321_BAS_Meldeleitfaden_FR.pdf) : médecin **1 semaine au médecin cantonal**, laboratoire **24 h à l’OFSP** ; déclencheurs et exclusion de la seule infection immunologique retranscrits correctement. La différence entre surveillance OFSP et nomenclature A15/A16 est expliquée. |
| Diagnostic et isolement | Guide 2024 §§6.1–6.3 et 7.5 : prélèvement direct puis culture/sensibilité ; IGRA/TCT ne prouvent pas maladie active ; premier PCR négatif à recontrôler si forte probabilité, isolement selon contexte ; PCR positive après traitement n’est pas test de guérison. Pas de confirmation ni contagiosité inventée dans la vignette. |
| Suivi et résistance | Guide 2024 §§7.2, 7.4 : consultation environ tous les quinze jours en phase intensive puis au moins mensuelle ; frottis/culture fin du 2e mois et avant fin du 5e si culture initiale positive ; résistance rifampicine en branche spécialisée ; seuils ALAT ≥3× symptomatique et ≥5× asymptomatique correctement repris. |

## Remarque éditoriale

Dans `A15_a.html`, §2, les doubles astérisques autour de « données de 2024 » semblent être du Markdown littéral dans l’HTML. Les retirer au profit de `<strong>` ou du texte simple. Le code est largement répété dans les fenêtres et la synthèse ; il est exact, mais le souhait de l’utilisateur est de garder la nomenclature discrète par rapport au fond clinique.

## Limite de cette revue

Relecture médicale et confrontation des textes cités ; pas de test du rendu interactif ni de certification du codage suisse actuel. Aucun fichier du dépôt édité par cet audit.
