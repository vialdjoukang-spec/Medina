export const meta = {
  name: 'medina-reecriture-pedagogique',
  description: 'Réécriture pédagogique de cours MEDINA selon docs/STYLE_REDACTION.md (annonce, développement, épilogue ; zéro phrase nominale ; tableaux expliqués ; sciences approfondies), avec contre-lecture adverse',
  phases: [
    { title: 'Pathologie', detail: 'onglet 1 : fichiers _a et _b, fenêtres associées' },
    { title: 'Examens et sciences', detail: 'onglets 2 et 3 : fichier _c, fenêtres associées' },
    { title: 'Pharmacologie', detail: 'onglet 4 : fichier _d, fenêtres restantes, cohérence' },
    { title: 'Contre-lecture', detail: 'style, faits, contrat' },
    { title: 'Reprise', detail: 'écarts confirmés' },
  ],
}
const CODES = (args && args.codes) || ['J44', 'J18', 'I26', 'A41']

const CTX = (code) => `Projet MEDINA, dépôt /home/user/Medina : atlas de cours de médecine en français pour l'examen fédéral suisse. Le propriétaire, médecin, trouve le chapitre ${code} trop difficile à suivre : trop de phrases nominales et d'infinitifs injonctifs, des parties qui ne sont ni annoncées ni conclues, des tableaux posés sans explication, des sciences fondamentales superficielles, une densité d'information trop faible par partie. Son exigence tient en une phrase : « le lecteur comprend, il ne devine pas ».
AVANT TOUTE ÉCRITURE, LIS EN ENTIER : /home/user/Medina/docs/STYLE_REDACTION.md (guide obligatoire, il prime sur tes habitudes), puis PROMPT_MEDINA.md § 4 (contrat HTML), § 5 (glossaire), § 10 (contenu par onglet), § 11 (rigueur), § 13 (critères formels), § 14 (Pareto), et CHAPTER_SPEC.md. Lis aussi audits/${code}.md : sa section « Vérification en texte intégral — 26.09.2026 » liste les données déjà vérifiées dans les sources primaires ; tu les conserves exactement (valeur, unité, source, année).
Contrat HTML (non négociable) : classes de la liste fermée seulement (alert card chap chap-body chap-head code fb ilot k key lab maj n next pager panel pareto-btn prev quiz ratio sci sci-bar sci-body src ssp status t tabs toc trap two ui w, plus small dans les fenêtres) ; aucun attribut style ; identifiants et clés de fenêtre préfixés par « ${code.toLowerCase()}- » ; mots verts <button class="w" data-k="${code.toLowerCase()}-cle">libellé (destination annoncée)</button> ; fenêtres <template data-pop="${code.toLowerCase()}-cle" data-title="Titre">…</template> ; sous-parties <h3>n.m Titre</h3> ; épilogue local <div class="key"><b>À retenir.</b> …</div> ; figures <figure><svg viewBox … role="img" aria-label="…">…</svg><figcaption>Figure n — …</figcaption></figure> en noir et blanc (#222), normal avant pathologique. Les îlots gardent leurs identifiants existants (les ancres du plan et les Pareto en dépendent) ; un nouvel îlot reçoit un identifiant nouveau et une entrée dans le plan (nav.toc).
Glossaire : toute abréviation employée doit être une clé du glossaire global ; vérifie le sens d'une clé existante (\`cd /home/user/Medina && python3 -c "import build_medina as B; print(B.G.get('CLÉ'))"\`) ; ajoute les clés manquantes dans glossary/${code.toLowerCase()}.py uniquement (jamais dans zz_fusion.py ni ailleurs) ; en cas de doute, écris le terme en toutes lettres.
Exactitude : tolérance zéro. Toute donnée nouvelle (chiffre, seuil, dose, essai, recommandation) est vérifiée dans la source primaire, accessible en ligne (swissmedicinfo.ch, compendium.ch, sociétés savantes, PubMed ou Europe PMC ; NEJM et JAMA renvoient 403 : passe par PubMed). Consigne chaque donnée nouvelle, avec l'URL et la date, dans audits/${code}.md, section « Réécriture pédagogique — 26.09.2026 ».
Aucune condensation : tu n'enlèves aucune information exacte ; tu la reformules, l'expliques et l'approfondis. La longueur du chapitre augmentera nettement : c'est attendu (à titre indicatif, une partie réécrite compte souvent 1,5 à 2 fois plus de mots, parce qu'elle explique ; la longueur n'est pas un but en soi, la compréhension l'est).
Fenêtres : elles sont aujourd'hui les plus nominales (exemple réel à proscrire : « Conséquences : Perte de surface d'échange (DLCO basse), perte de rétraction élastique… »). Chaque fenêtre que tu touches garde ses intertitres div.lab, mais chaque intertitre est suivi de phrases complètes qui expliquent le pourquoi.
Travail en parallèle : d'autres rédacteurs travaillent en même temps sur d'autres chapitres du même dépôt. Tu ne modifies que les fichiers autorisés ci-dessous. Tu n'emploies AUCUNE commande git qui modifie l'état du dépôt (commit, checkout, switch, stash, reset, restore, clean, merge, rebase) ; les lectures (git show, git diff, git log) sont permises. Tu ne lances pas build_front.py ni pack_v7.py.
Glossaire partagé : tous les fichiers glossary/*.py remplissent un seul dictionnaire, et la dernière définition chargée l'emporte pour tout l'atlas. Tu n'ajoutes donc jamais une clé qui existe déjà (vérifie avec la commande ci-dessus) ; si elle existe avec un autre sens, tu écris le terme en toutes lettres.
Pareto : à la fin de chaque grande partie, la fenêtre Pareto (template data-pop="pareto-${code.toLowerCase()}-…") garde des data-cover valides ; mets à jour sa liste pour qu'elle couvre 100 % des notions utiles de la partie réécrite, en phrases complètes, et vise 5 à 20 % du texte couvert.
Contrôle bloquant après ton travail : \`cd /home/user/Medina && python3 test_v7.py --static ${code}\` doit afficher OK. Relis ensuite ton propre texte une fois, en cherchant chaque phrase nominale et chaque infinitif injonctif restants, et corrige-les.`

const PART = {
  A: (code) => `${CTX(code)}

TA PART : l'onglet 1, « Pathologie et prise en charge » (panneau pA), c'est-à-dire chapters/${code}/${code}_a.html et chapters/${code}/${code}_b.html, ainsi que les fenêtres ouvertes par les mots verts de cet onglet (dans les fichiers chapters/${code}/${code}_pop*.html existants ; crée un fichier chapters/${code}/${code}_pop_pa.html pour les fenêtres nouvelles) et les fenêtres Pareto de cet onglet.
Réécris chaque îlot selon le guide : annonce (2 à 4 phrases), développement dense du normal au pathologique et du mécanisme à la décision, épilogue local « À retenir ». Sois complet et pédagogiquement offensif dans l'anamnèse (antécédents et symptômes cliquables, fréquences chiffrées, formes typiques et atypiques), l'examen clinique (chaque signe cliquable : technique, valeur, piège), le diagnostic (critères officiels, algorithme en figure, différentiels hiérarchisés par gravité et expliqués), les urgences, la thérapeutique (objectifs, moyens, choix justifiés, surveillance), la prévention et le pronostic. Explique toujours POURQUOI. Introduis et commente chaque tableau. Garde le dernier îlot conforme au § 13 (div.alert des critères formels, puis div.key des paramètres clés), rédigé en phrases complètes. Conserve le cas fil rouge et fais-le vivre d'îlot en îlot.
Fichiers autorisés : chapters/${code}/${code}_a.html, chapters/${code}/${code}_b.html, chapters/${code}/${code}_pop*.html (fenêtres de l'onglet 1 et Pareto de l'onglet 1 seulement), chapters/${code}/${code}_pop_pa.html (nouveau), glossary/${code.toLowerCase()}.py, audits/${code}.md.`,
  C: (code) => `${CTX(code)}

TA PART : l'onglet 2, « Examens complémentaires » (panneau pE), et l'onglet 3, « Sciences fondamentales » (panneau pS), c'est-à-dire chapters/${code}/${code}_c.html, ainsi que les fenêtres ouvertes par leurs mots verts (fichiers _pop existants ; crée chapters/${code}/${code}_pop_pc.html pour les fenêtres nouvelles) et les Pareto de ces deux onglets. L'onglet 1 vient d'être réécrit par un autre rédacteur : lis-le d'abord pour rester cohérent (mêmes seuils, même cas fil rouge, pas de redite inutile).
Examens : pour chaque examen, explique la question clinique qu'il tranche, son principe, ses valeurs normales (unité, population), les seuils qui changent la décision, ses limites et ses pièges ; introduis et commente chaque tableau ; garde au moins trois quiz au format de l'examen (au moins trois options, explication rédigée) ; ajoute une figure si une courbe ou un tracé aide à comprendre.
Sciences fondamentales : approfondis chaque discipline au niveau d'un cours universitaire relié à la maladie ; annonce la question clinique éclairée ; explique le normal puis sa perturbation ; au moins un schéma légendé par discipline utile ; aucun tableau sans introduction ni lecture ; termine par des encadrés key de corrélation science → clinique, science → examen, science → traitement, en phrases complètes. C'est la partie que le propriétaire juge la plus faible : elle doit devenir la plus claire.
Fichiers autorisés : chapters/${code}/${code}_c.html, chapters/${code}/${code}_pop*.html (fenêtres des onglets 2 et 3 et leurs Pareto seulement), chapters/${code}/${code}_pop_pc.html (nouveau), glossary/${code.toLowerCase()}.py, audits/${code}.md.`,
  D: (code) => `${CTX(code)}

TA PART : l'onglet 4, « Pharmacologie » (panneau pP), c'est-à-dire chapters/${code}/${code}_d.html, les monographies et fenêtres ouvertes depuis cet onglet (fichiers _pop existants ; crée chapters/${code}/${code}_pop_pd.html pour les fenêtres nouvelles), ses Pareto, puis TOUTES les fenêtres restantes du chapitre qui ne suivraient pas encore le guide. Les onglets 1 à 3 viennent d'être réécrits : lis-les d'abord.
Pharmacologie : annonce la logique thérapeutique (classes, place selon le stade et le phénotype, pourquoi tel choix avant tel autre) ; introduis et commente le tableau des doses (colonnes expliquées, lecture guidée, exemple de patient) ; conserve à l'identique chaque posologie vérifiée ; interactions dangereuses dans un div.alert expliqué ; surveillance et effets indésirables expliqués par leur mécanisme ; monographies en fenêtres (mécanisme, essai nommé avec année et résultat, posologie, effets indésirables, contre-indications, surveillance) rédigées en phrases complètes.
Fin de ta part : vérifie que chaque data-k du chapitre a sa fenêtre, que le plan (nav.toc) correspond aux îlots, que les seuils sont identiques dans les quatre onglets, les fenêtres et les Pareto, et que le test statique affiche OK.
Fichiers autorisés : chapters/${code}/*, glossary/${code.toLowerCase()}.py, audits/${code}.md.`,
}

const RES = { type: 'object', properties: { summary: { type: 'string' }, words_before: { type: 'number' }, words_after: { type: 'number' }, new_windows: { type: 'number' }, new_facts_sourced: { type: 'number' }, static_test: { type: 'string' }, reserves: { type: 'array', items: { type: 'string' } } }, required: ['summary', 'static_test'] }
const VERDICT = { type: 'object', properties: { ok: { type: 'boolean' }, style_score: { type: 'string' }, issues: { type: 'array', items: { type: 'object', properties: { severity: { type: 'string', enum: ['bloquant', 'majeur', 'mineur'] }, where: { type: 'string' }, description: { type: 'string' }, fix: { type: 'string' } }, required: ['severity', 'where', 'description'] } } }, required: ['ok', 'issues'] }

const verify = (code, notes) => `${CTX(code)}

MISSION : CONTRE-LECTURE INDÉPENDANTE ET ADVERSE de la réécriture du chapitre ${code} (trois rédacteurs successifs ; leurs résumés : ${JSON.stringify(notes).slice(0, 2500)}). N'ÉCRIS AUCUN FICHIER.
Compare avec la version antérieure à la réécriture, figée au commit 0a57926 (\`git -C /home/user/Medina show 0a57926:chapters/${code}/<fichier>\`).
Contrôle et rapporte, avec l'emplacement exact :
1. Style (guide docs/STYLE_REDACTION.md) : relève TOUTES les phrases nominales et tous les infinitifs injonctifs restants hors titres et cellules brèves ; chaque îlot et chaque sous-partie a-t-il son annonce et son épilogue « À retenir » ? chaque tableau est-il introduit et commenté ? chaque figure annoncée et lue ? donne une estimation du taux de conformité (style_score).
2. Profondeur : la densité d'information a-t-elle augmenté partie par partie ? les sciences fondamentales atteignent-elles un niveau universitaire relié à la maladie ? l'anamnèse, la clinique, le diagnostic, la thérapeutique, la prévention et le pronostic sont-ils complets, avec des mots verts réels ?
3. Exactitude : AUCUNE donnée vérifiée n'a disparu ni changé (compare au tableau « Vérification en texte intégral » de audits/${code}.md) ; vérifie toi-même dans la source primaire au moins DIX données nouvelles de la section « Réécriture pédagogique » ; cherche toute affirmation nouvelle non sourcée.
4. Contrat et cohérence : classes, identifiants, plan, fenêtres, Pareto, seuils identiques partout ; lance \`python3 test_v7.py --static ${code}\`.
ok=true seulement s'il ne reste aucun écart bloquant ou majeur.`

const refix = (code, issues) => `${CTX(code)}

MISSION : corriger les écarts relevés par la contre-lecture indépendante du chapitre ${code}. Vérifie chacun ; corrige ceux qui sont fondés (réécris les phrases nominales signalées, ajoute annonces, épilogues et lectures de tableaux manquants, rectifie les données) ; explique ceux que tu refuses. Consigne le tout dans audits/${code}.md, sous-section « Réécriture pédagogique — après contre-lecture ». Termine par le test statique (OK).
Écarts : ${JSON.stringify(issues, null, 1)}
Fichiers autorisés : chapters/${code}/*, glossary/${code.toLowerCase()}.py, audits/${code}.md.`

// L'état transporte le code : les étapes ne dépendent pas de la signature des rappels.
const out = await pipeline(CODES,
  code => agent(PART.A(code), { label: `pathologie:${code}`, phase: 'Pathologie', schema: RES }).then(a => ({ code, a })),
  s => agent(PART.C(s.code), { label: `examens-sciences:${s.code}`, phase: 'Examens et sciences', schema: RES }).then(c => ({ ...s, c })),
  s => agent(PART.D(s.code), { label: `pharmacologie:${s.code}`, phase: 'Pharmacologie', schema: RES }).then(d => ({ ...s, d })),
  s => agent(verify(s.code, [s.a && s.a.summary, s.c && s.c.summary, s.d && s.d.summary]), { label: `contre-lecture:${s.code}`, phase: 'Contre-lecture', schema: VERDICT }).then(v => ({ ...s, v })),
  async s => {
    const issues = (s.v && s.v.issues) || []
    if (!s.v || !issues.length) return { ...s, fix: null }
    const fix = await agent(refix(s.code, issues), { label: `reprise:${s.code}`, phase: 'Reprise' })
    return { ...s, fix }
  })
return out
