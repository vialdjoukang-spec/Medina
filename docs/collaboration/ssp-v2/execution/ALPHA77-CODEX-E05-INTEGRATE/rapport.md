# E05 — intégration médicale, langue et sémiologie Alpha77

Candidat d’auteur Codex, mission `ALPHA77-CODEX-E05-INTEGRATE`, génération 1, branche `codex/alpha77/e05-integrate-g1`, base de travail `3131a5cbf6cc003ead358e25152073959c53c4d9`. Le coordinateur a obtenu acquire/start ; aucune nouvelle acquisition ni clôture n’a été exécutée ici. Ce rapport décrit une intégration avec réserves, pas un audit final favorable ni une validation médicale humaine.

## Corrections réalisées

Les rapports MED/LANG Alpha1 ont été adoptés et les propositions relues avant application. `adoption.json` conserve les changements et leur origine. Les sept fichiers sources E05 sont seuls modifiés hors assets et preuves réservés.

- MED M01–M09 et E01 : seuil d’agranulocytose corrigé à 500/µL (0,5 × 10⁹/L), dénominateur de l’hyperglycémie Tepezza corrigé, taux chirurgical correctement attribué, prudence bêtabloquant/asthme, allaitement par produit, pancréatite liée aux thionamides, exceptions de TSH, calcul population/individu et quiz de grossesse.
- 31 propositions LANG adoptées ; lorsqu’une formulation médicale a ensuite changé, sa correction finale remplace la proposition littérale. Aucune promotion des anciens rapports au rang d’audits finaux de ce candidat.
- Lecture du nouveau consensus européen de crise ETA/BTA/SfE/WEDS 2026 : jugement clinique et limites des scores, délai d’au moins une heure avant l’iodure, prudence circulatoire des bêtabloquants, réévaluation en 24–48 h. Les doses spécialisées qui dépassent les FI sont explicitement distinguées ; aucune formulation iodée locale n’est inventée.
- Grossesse : répétition des TRAK à 18–22 semaines conditionnée par leur élévation initiale. Radioprotection : exception OFSP individuelle ajoutée aux résumés. Nodule chaud : exception de forte suspicion de malignité. Méthylprednisolone : 1 g/j n’est pas une frontière d’innocuité. EUGOGO : association méthylprednisolone/mycophénolate pour la plupart des formes actives modérées à sévères ; FI Myfortic consultée et usage orbitaire hors indication clairement attribué.

## Sémiologie ajoutée

Dans `E05_c.html`, le premier bouton local est « Sémiologie fondamentale et analytique », ID `e05-tab-semio`, cible `e05-s-semio`. Les neuf sections sont substantielles, avec le premier h3 exact demandé. Les autres panneaux sont cachés initialement. La clinique est marquée dans A05 à l’intérieur du panneau pA. Un sixième panneau traite les mécanismes de décompensation, avec leurs incertitudes explicites.

Les sources se rattachent aux passages et populations dans `recherche_E05/sources.json` et `claim-mapping.json`. Le test réflexe SSCC/SSED est limité à l’adulte hors grossesse ; les fréquences et performances de gestes cliniques non fournies ne sont pas inventées. Les nouvelles affirmations ne reposent pas sur un transfert de faits cardiologiques.

## Figures

Huit originaux exacts ont été téléchargés manuellement et conservés sans transformation sous `assets/img/e05/alpha/codex`. `figures.json` fournit, pour chacun, les URL, l’auteur, la licence, les octets SHA256, les pages de droits conservées et la revue visuelle. Les sept rastres ont été ouverts dans un montage de contrôle ; l’original SVG de l’axe a été rendu dans Chromium et ouvert séparément. Les observations et limites figurent dans les huit rapports visuels. Aucun dessin anatomique n’a été créé ou modifié par IA.

La provenance de l’axe et de la synthèse repose sur l’auteur nommé, ses déclarations de travail/source, les pages propres aux fichiers, les licences et l’historique, avec inspection ; la date seule n’est pas une certification. L’image scintigraphique possède une déclaration Commons BY-SA3 et une référence PLoS donnée comme CC-BY ; ces deux niveaux sont conservés, sans inventer une nouvelle licence. Les SVG locaux ne font qu’afficher les originaux au moyen de `<image>` accessibles. Le schéma diagnostique existant est causal, non anatomique ; il n’est pas présenté comme une recommandation officielle.

## Vérifications réelles

- Porte `tools/betta_verite.py` : VÉRITÉ OK avant rédaction sur la matrice héritée avec lacunes, puis après enrichissement. Ce résultat ne constitue pas une validation clinique.
- `test_v7.py --static E05` : OK, 90 fenêtres, quatre quiz et quatre Pareto.
- Construction réelle `build_front.py --fragment S05` dans une sortie temporaire propre : réussie. Aucun fichier partagé ou résultat généré n’est committé.
- `tests/audit_sciences.py` directement : impossible sur sa base historique `c50a…`, où E05 n’existe pas. Le même module a ensuite été exécuté avec la seule constante de comparaison remplacée en mémoire par la base trusted `3131…`. Aucun test partagé modifié et aucune exigence affaiblie : six panneaux, six figures accessibles, minimum 280 mots et quatre corrélations vérifiés. Résultat `sciences.json`.
- Chromium réel 1365 × 950 et 390 × 844 : sélection initiale et alternée des six panneaux, Entrée/Espace natifs, popup du calcul, police 24 px, mode Livre et Navigo. Les onze références d’images présentes dans le cours décodent leurs originaux ; aucune erreur JavaScript et aucun débordement horizontal du document. Le panneau Livre est défilable verticalement ; l’accès à la fin est contrôlé. Captures et JSON joints. Aucune gestion de flèches/Home/End des onglets n’est revendiquée.
- Huit preuves `figure_rights` passent les assertions du vérificateur Alpha ; aucune attestation MED/LANG/SEMIO finale ni reçu de clôture n’est créée.

## Réserves exactes à transmettre aux audits finaux

1. La relecture est celle d’un auteur/intégrateur. Les audits MED, LANG et SEMIO finaux indépendants sur ces empreintes restent à réaliser par le coordinateur. Aucun certificat global de conformité suisse n’est émis.
2. Risch Ribook a livré une coque applicative, sans catalogue exploitable dans cette tentative. Les intervalles, méthodes, références de grossesse et seuil TRAK hérités ne sont pas revendiqués comme nouvellement relus ; ils doivent être confirmés sur le catalogue applicable. La sémiologie nouvelle ne les traite pas comme universels.
3. Le consensus européen 2026 décrit des doses hospitalières dépassant les FI et reprend un algorithme référant aussi à l’ATA. Le texte distingue ces origines, le cadre européen et les limites suisses. Aucun protocole hospitalier suisse local ni préparation iodée exacte n’a été obtenu ; validation locale spécialisée reste nécessaire pour une prescription. Les barèmes complets anciens BWPS/JTA doivent être revérifiés sur leurs originaux, sans mélanger les tables divergentes de versions différentes.
4. Les FI des options immunomodulatrices secondaires citées dans le cours (notamment ciclosporine, azathioprine, rituximab et tocilizumab) ne sont pas toutes documentées par produit exact dans cette reprise. Leur mention EUGOGO ne vaut pas ordonnance suisse. La FI Myfortic et les principaux produits de dose ont été consultés, sans créer une FI fictive d’orbitopathie.
5. L’édition OFS effectivement applicable et les codes de grossesse/post-partum, le remboursement actuel, les détails biochimiques hérités et leurs références primaires ne sont pas certifiés par cette reprise ciblée. La matrice de vingt rubriques conserve ces lacunes. Les FI Euthyrox/Cordarone obtenues sans nouvelle lecture ciblée ne sont pas présentées comme décisions nouvellement vérifiées.
6. Les contrôles de droits et d’imagerie sont des revues IA documentées, pas une validation médicale humaine ni une garantie juridique. Les droits de personnalité d’anciens clichés sont limités à ce qui est documenté par les pages publiques ; aucune nouvelle autorisation individuelle n’est prétendue.

Les empreintes de la base et du candidat source sont dans `empreintes.json`. Publication, audits finaux et clôture restent des étapes distinctes.

## Audit final MED et SEMIO distinct — reprise du 15 octobre 2026

Un auditeur médical IA distinct de l’auteur/intégrateur a repris les réserves Alpha1, la sémiologie complète et les passages primaires ciblés. `MED.json` et `SEMIO.json` attestent cette revue avec le statut **provisional**, les sept empreintes de base exacte `3131a5cb…` et les quinze empreintes finales. Aucun avis favorable exhaustif, clôture Alpha ou validation médicale humaine n’est attribué.

La réserve Risch est résolue. Une navigation Chromium sur la page initiale a encore fourni une coque sans catalogue. Le client public Ribook indique cependant le service public de données : les quatre fiches TSH/FT4/FT3/TRAK ont été obtenues et réellement lues. Elles confirment les intervalles adultes, pédiatriques et de grossesse du cours, la méthode ECLIA/Roche, le seuil TRAK <1,22UI/l et la version du30juillet2026. Les liens directs sont désormais visibles dans E01. Il ne s’agit pas de valeurs universelles.

Des discordances ont été corrigées sur les surfaces héritées : A10 désignait encore la méthylprednisolone seule ou associée sans distinguer la première ligne EUGOGO ; l’association avec mycophénolate est désormais le choix pour la plupart des formes concernées, avec l’alternative de monothérapie explicitée. A12 exige maintenant des T4 et T3 normales pour la forme infraclinique. Les formulations absolues des scores de crise sont remplacées par leur rôle d’aide au jugement. A07 et sa fenêtre utilisent exclusivement les paliers du tableau1 du consensus européen2026, explicitement nommé ; l’exemple 39,5°C prend15points et totalise75, sans mélanger les paliers thermiques de la présentation historique. La catégorie japonaise TS2 sans dosage disponible conserve ses conditions supplémentaires. Le tableau pharmacologique distingue FI et schémas européens spécialisés ; l’hydrocortisone est harmonisée avec le consensus actuel et la quantité de charge d’esmolol est exprimée sans ambiguïté. Les FI exactes lues restent les références suisses pour leurs produits ; les doses hospitalières hors FI ne deviennent pas des prescriptions suisses validées.

L’extraction EUGOGO perd la barre du glyphe≥. La page53 du PDF (tableau2) a été rendue et ouverte : le seuil d’activité est bien CAS≥3/7, conservé dans le cours ; le rendu probant est joint. Les huit figures ont été revues dans le montage original et l’axe rendu séparément. Cela ne crée ni nouvelle autorisation de personne photographiée ni expertise juridique ; aucune garantie au-delà des documents d’origine n’est ajoutée.

Les réserves encore ouvertes sont le protocole hospitalier suisse local de crise et la préparation iodée exacte, les produits FI secondaires non exhaustivement revus, OFS et codes de grossesse applicables, remboursement actuel, et la revalidation exhaustive des mécanismes biochimiques hérités. Ces limites remplacent les mentions d’audits finaux «à réaliser» pour MED/SEMIO et la réserve Risch du rapport d’auteur. Le détail figure dans `findings`; `unresolved_blockers` conserve le texte exact de l’avis visible du cours. La sémiologie est substantielle et ses contrôles passent, mais aucune clôture n’est déduite de la seule présence des balises.

Sur les octets finaux : test statique **OK**,34508 mots,90fenêtres,4quiz,4Pareto ; reconstruction S05 propre ; Chromium1365×950 et390×844 avec les six sélections réellement cliquées, neuf sections, Entrée/Espace, popup, police24px, Livre et Navigo. Les15copies sous `delivery/`, le manifeste et les attestations sont actualisés. Le test partagé `audit_sciences.py` reste inchangé ; sa base historique manquante n’est pas convertie en réussite par cet audit.

Checkpoint de transition demandé par Vial : arrêt de tout nouveau travail après cette sauvegarde. La revue médicale ciblée et les attestations MED/SEMIO ci-jointes sont provisoires ; l’audit LANG final sur ces octets, le reçu Alpha, la PR, la CI et la publication restent à réaliser par le coordinateur. Aucune clôture ni validation humaine. La reprise doit conserver les réserves ci-dessus et partir de `final-hashset.json` ; ne pas promouvoir les rapports d’auteur historiques.
