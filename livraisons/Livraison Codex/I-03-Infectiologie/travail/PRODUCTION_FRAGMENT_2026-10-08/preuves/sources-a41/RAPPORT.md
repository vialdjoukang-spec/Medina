# A41 — Sepsis et choc septique de l’adulte (I-03-Infectiologie)

Relecture documentaire ciblée du **8 octobre 2026**, sur `2f4a7dbffba7c43ec791fb6dcea4be7d553ff5a9`. Les six fichiers recensés dans `BASE_SHA256.tsv` étaient identiques au commit. Aucun fichier du dépôt n’a été modifié.

Le rapport Claude conservé dans `espace_partage/COURS_CODEX_A_AUDITER_PAR_CLAUDE/A41/rapport_audit_claude.md` réserve **Leone 2026**, concernant le choc réfractaire. **Leone 2014** concerne la désescalade et ne remplace pas cette référence. Les deux ont été distingués ci-dessous.

## SSC 2026 : cotations confirmées, précision de population

La [page officielle SCCM](https://www.sccm.org/clinical-resources/guidelines/guidelines/surviving-sepsis-campaign-international-guidelines-for-management-of-sepsis-and-septic-shock-2026), publiée le **23 mars 2026**, a été ouverte. Énoncés lus : *Mechanical ventilation*, *Sodium bicarbonate*, *Antimicrobial therapy*.

- Décubitus ventral **> 12 h/j**, sepsis et SDRA modéré–sévère : **conditionnelle, modérée**. `A41_b.html:108` et `a41-sdra` concordent.
- Bicarbonate pour améliorer l’hémodynamique/réduire les vasopresseurs dans l’acidémie lactique d’hypoperfusion : défavorable **conditionnelle, faible**. En **choc septique**, acidémie métabolique sévère **pH ≤ 7,2**, atteinte rénale **AKIN 2–3** : favorable **conditionnelle, très faible**. `A41_d.html:52` concorde.
- Désescalade, agent/sensibilité connus : **forte, très faible** ; cultures finales sans agent : **conditionnelle, très faible**. Grades conformes.

**Précision proposée :** ligne « Rein » de `A41_b.html:108` et `a41-mesures` (`A41_pop_pa.html:27`) : remplacer « bicarbonate seulement si… » par « bicarbonate suggéré en choc septique avec acidémie métabolique sévère, pH ≤ 7,2, et atteinte rénale AKIN 2–3 (conditionnelle, très faible) ». Restituer la population évite une restriction générale.

**Accès :** [aperçu éditeur](https://link.springer.com/article/10.1007/s00134-026-08361-1) sous abonnement, PDF indisponible. Rationales et tous les numéros 2026 non vérifiés.

## ANDROMEDA-SHOCK-2 : résumé actuel exact

[Article primaire JAMA](https://jamanetwork.com/journals/jama/fullarticle/2840823), publié en ligne le **29 octobre 2025**, texte intégral ouvert : méthodes, résultats, tableau 3 et limites. L’essai porte sur le choc septique précoce, dans 86 centres de 19 pays : **1 501 randomisés, 1 467 analysés**. Le critère hiérarchique à 28 jours combine décès, durée des suppléances et séjour ; rapport de victoires **1,16 [1,02–1,33]**, p = 0,04, principalement porté par les suppléances. La mortalité à 28 jours ne diffère pas : **26,5 % contre 26,6 %**, HR **0,99 [0,81–1,21]**, p = 0,91. Essai ouvert ; décisions d’arrêt des suppléances selon les pratiques locales.

`a41-sign-perfusion` (`A41_pop1.html:13`) et la clé du glossaire ne présentent pas le critère principal comme une baisse de mortalité : aucune erreur démontrée. **Ajout utile :** expliciter dans la fenêtre l’absence de différence significative sur la mortalité et proposer le lien JAMA intégral à côté du résumé PubMed déjà référencé.

## Leone 2014 : éviter une efficacité garantie de la désescalade

[Résumé primaire éditeur](https://link.springer.com/article/10.1007/s00134-014-3411-8), publié le **5 août 2014**, sections *Methods*, *Results*, *Conclusion* réellement lues. Essai ouvert, 116 adultes, neuf réanimations françaises. Mortalité similaire, mais davantage de surinfections (**27 % contre 11 %**) et de jours d’antibiotiques (médianes **9 contre 7,5**). Une mortalité similaire dans ce petit essai ne prouve pas une équivalence générale de l’efficacité. Le texte intégral et le contenu de l’[erratum du 7 octobre 2014](https://link.springer.com/article/10.1007/s00134-014-3507-1) restent sous abonnement ; aucune adjudication du calcul de non-infériorité n’est revendiquée.

**Correction proposée :** dans `A41_d.html:54`, remplacer « La désescalade conserve l’efficacité tout en réduisant les risques » par « La désescalade adapte le spectre à la microbiologie et à l’évolution clinique, avec une réévaluation de l’efficacité et de la tolérance ». Dans `a41-desescalade` (`A41_pop_pa.html:28`), préférer « vise à limiter » à « limite » pour les risques annoncés. Conserver la recommandation SSC actuelle ; cet essai ancien ne la renverse pas.

## Leone 2026 : limite importante retrouvée dans le texte intégral

[PDF primaire éditeur](https://link.springer.com/content/pdf/10.1007/s00134-026-08344-2.pdf), publié le **24 mars 2026**, 17 pages : résultats, figure 3, limites et conclusion lus. La population de 56 experts, les cinq tours, 13 critères retenus, la persistance de l’hypoperfusion, l’absence de réponse au remplissage et le seuil d’équivalent noradrénaline base **> 0,5 µg/kg/min** concordent avec `a41-refractaire` (`A41_pop_pa.html:20`).

À la **page 997, page PDF 14**, les auteurs demandent une validation externe avant usage clinique ou inclusion dans les recommandations. Ils n’ont pas obtenu de consensus sur la durée minimale de persistance. **Ajout nécessaire dans cette fenêtre :** « Ces critères de consensus restent à valider extérieurement avant leur adoption clinique ; ils ne constituent pas à eux seuls un seuil validé de décision thérapeutique. » La phrase actuelle « définit le stade réfractaire » gagnerait à devenir « caractérise le phénotype proposé par ce consensus ».

## BICARICU-2 : complément pertinent, sans modifier arbitrairement SSC

[Article primaire JAMA](https://jamanetwork.com/journals/jama/fullarticle/2840824), publié en ligne le **29 octobre 2025**, texte intégral ouvert : critères d’inclusion, tableau 2, résultats et discussion. Essai ouvert : 640 randomisés, 627 dans l’analyse principale, acidémie pH ≤ 7,20 et atteinte rénale **KDIGO 2–3**, population de réanimation non exclusivement septique. Mortalité à 90 jours : **195/314 contre 193/313**, sans différence démontrée ; recours à l’épuration **35 % contre 50 %**, critère secondaire. L’acidémie intervient elle-même dans les critères de début d’épuration, ce qui limite une interprétation comme récupération rénale prouvée.

**Complément proposé près de `A41_d.html:52` ou dans une fenêtre liée :** présenter l’absence de bénéfice démontré sur la mortalité et la diminution du recours à l’épuration, sans convertir la suggestion SSC 2026 en bénéfice de survie établi. Ne pas confondre le stade KDIGO de l’essai avec la formulation AKIN de l’énoncé SCCM.

Ces constats sont limités aux passages et sources indiqués. Ils ne requalifient aucun rapport historique et ne donnent aucun état au fragment.
