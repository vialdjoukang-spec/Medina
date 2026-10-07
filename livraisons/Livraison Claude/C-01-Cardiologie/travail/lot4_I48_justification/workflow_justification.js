export const meta = {
  name: 'medina-lot4-justification-i48',
  description: 'MEDINA lot 4 pilote : rédiger et vérifier la justification mécanistique de 505 affirmations de I48 (fenêtres + textes)',
  phases: [
    { title: 'Plan', detail: 'par fichier : textes courts, cellules, thèmes de fenêtres' },
    { title: 'Fusion', detail: 'regroupe les thèmes en fenêtres uniques' },
    { title: 'Fenêtres', detail: 'rédaction, vérification médicale, révision' },
    { title: 'Textes', detail: 'vérification des insertions dans le texte' },
  ],
}
const IDX = '/tmp/claude-0/lot4/fenetres_existantes.json'
const ESC = '/tmp/claude-0/esc_pdf/esc2024.txt'
const RULE = `Contexte : cours MEDINA I48 — Fibrillation et flutter auriculaires, examen fédéral suisse. Exigence du propriétaire (docs/collaboration/MISSION_JUSTIFICATION_2026-10-07.md, à lire) : chaque affirmation porte son POURQUOI, le mécanisme physiopathologique précis, de préférence dans une fenêtre interactive (mot vert). Pas de cellule de tableau laconique.
Règles de rédaction : français médical professionnel, phrases complètes, ordre normal → mécanisme → conséquence → décision ; aucune métaphore, aucun métadiscours (« le lecteur », « cette partie ») ; aucune abréviation nouvelle (n'emploie que les sigles déjà présents dans le cours I48, sinon écris en toutes lettres) ; typographie ’ et « ». Exactitude : tout chiffre, seuil, classe de recommandation ou dose doit provenir d'une source identifiée. La recommandation ESC 2024 sur la FA est disponible en texte intégral dans ${ESC} (cherche avec Grep) ; cite « ESC 2024, section/tableau ». Pour une physiologie classique, cite un manuel (Guyton & Hall, Braunwald) ou une revue identifiée. Un mécanisme débattu est présenté comme tel. Ne modifie aucun fichier : sortie structurée uniquement.`

const INLINE = { type: 'object', properties: { id: { type: 'string' }, old: { type: 'string' }, new: { type: 'string' }, motif: { type: 'string' }, source: { type: 'string' } }, required: ['id', 'old', 'new', 'motif', 'source'] }
const ANCRE = { type: 'object', properties: { file: { type: 'string' }, id: { type: 'string' }, old: { type: 'string' }, label: { type: 'string', description: 'sous-chaîne exacte de old qui deviendra le mot vert ; vide si le bouton doit être ajouté après old' } }, required: ['file', 'id', 'old', 'label'] }
const THEME = { type: 'object', properties: { theme: { type: 'string' }, titre: { type: 'string' }, existante: { type: 'string' }, contenu_attendu: { type: 'string' }, ancres: { type: 'array', items: ANCRE } }, required: ['theme', 'titre', 'existante', 'contenu_attendu', 'ancres'] }
const PLAN = { type: 'object', properties: { inline: { type: 'array', items: INLINE }, themes: { type: 'array', items: THEME } }, required: ['inline', 'themes'] }
const WIN = { type: 'object', properties: { cle: { type: 'string' }, titre: { type: 'string' }, action: { type: 'string', enum: ['creer', 'completer'] }, fichier_cible: { type: 'string', enum: ['I48_pop1', 'I48_pop2', 'I48_pop3', 'I48_pop4'] }, contenu_attendu: { type: 'string' }, ancres: { type: 'array', items: ANCRE } }, required: ['cle', 'titre', 'action', 'fichier_cible', 'contenu_attendu', 'ancres'] }
const FUS = { type: 'object', properties: { fenetres: { type: 'array', items: WIN } }, required: ['fenetres'] }
const HTMLW = { type: 'object', properties: { html: { type: 'string', description: 'creer : <template data-pop="CLE" data-title="TITRE">…</template> ; completer : rubriques <div class="lab">…</div><p>…</p> à ajouter à la fin de la fenêtre existante' }, sources: { type: 'array', items: { type: 'string' } } }, required: ['html', 'sources'] }
const VER = { type: 'object', properties: { ok: { type: 'boolean' }, problemes: { type: 'array', items: { type: 'string' } } }, required: ['ok', 'problemes'] }
const VERI = { type: 'object', properties: { verdicts: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' }, ok: { type: 'boolean' }, probleme: { type: 'string' }, new_corrige: { type: 'string' } }, required: ['id', 'ok', 'probleme', 'new_corrige'] } } }, required: ['verdicts'] }

const FILES = args
phase('Plan')
const plans = await parallel(FILES.map(f => () => agent(
  `${RULE}\n\nFichier : ${f.path} (${f.name}). Liste des ${f.n} affirmations sans mécanisme relevées par l'inventaire : ${f.items} (JSON, champs id, old, affirmation, manque, forme, fenetre_existante, explication brouillon, source_a_verifier). Index des fenêtres existantes : ${IDX}.\n` +
  `Pour CHAQUE affirmation, choisis :\n- "inline" si un complément de une à trois phrases suffit (ou pour une cellule de tableau : cause puis conséquence en phrase complète) : donne old (copie exacte, l'id l'indique) et new (old réécrit avec l'explication intégrée, mêmes balises), motif, source ;\n- sinon un thème de fenêtre : regroupe les affirmations qui relèvent du même mécanisme dans un seul thème ; indique "existante" = clé d'une fenêtre existante qui couvre déjà le sujet (le mot vert y renverra et la fenêtre sera complétée si besoin), sinon vide ; "contenu_attendu" = ce que la fenêtre doit expliquer précisément ; chaque ancre = {file:"${f.name}", id, old, label} où label est une courte sous-chaîne exacte de old (2 à 6 mots) qui deviendra le mot vert, et ne contient pas déjà un bouton.\nTraite toutes les affirmations ; ne relève pas de faux positifs (si l'affirmation est déjà expliquée, ignore-la).`,
  { label: `plan:${f.name}`, phase: 'Plan', schema: PLAN })))
const okPlans = plans.map((p, i) => p ? { ...p, file: FILES[i].name } : null).filter(Boolean)
log(`plans : ${okPlans.length}/${FILES.length} ; inline ${okPlans.reduce((n, p) => n + p.inline.length, 0)} ; thèmes ${okPlans.reduce((n, p) => n + p.themes.length, 0)}`)

phase('Fusion')
const fusion = await agent(
  `${RULE}\n\nVoici les thèmes de fenêtres proposés pour les huit fichiers du cours I48 :\n${JSON.stringify(okPlans.map(p => ({ file: p.file, themes: p.themes })))}\n\nIndex des fenêtres existantes : ${IDX}.\nFusionne les thèmes qui relèvent du même mécanisme en UNE fenêtre ; rattache aux fenêtres existantes quand elles couvrent le sujet (action "completer", cle = clé existante) ; sinon action "creer" avec une clé nouvelle "i48-…" unique (minuscules, tirets, absente de l'index). Chaque fenêtre garde toutes ses ancres. Choisis fichier_cible : pour completer, le fichier de la fenêtre existante ; pour creer, le pop le plus cohérent (pop1 notions fondamentales, pop2 clinique/examens, pop3 traitement/gestes/examens, pop4 pharmacologie). Ne perds aucune ancre.`,
  { label: 'fusion', phase: 'Fusion', schema: FUS, effort: 'high' })
const wins = (fusion && fusion.fenetres) || []
log(`${wins.length} fenêtres à créer ou compléter`)

const inlineAll = okPlans.map(p => ({ file: p.file, inline: p.inline }))
const [winRes, inlRes] = await parallel([
  () => pipeline(wins,
    (w) => agent(`${RULE}\n\nRédige la fenêtre « ${w.titre} » (clé ${w.cle}, action ${w.action}, fichier ${w.fichier_cible}). Contenu attendu : ${w.contenu_attendu}\nAffirmations qu'elle doit justifier (ancres) : ${JSON.stringify(w.ancres.map(a => a.old))}\n` +
      (w.action === 'completer' ? `La fenêtre existe déjà : lis-la dans /home/user/Medina/livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I48/${w.fichier_cible}.html et n'écris que les rubriques MANQUANTES (<div class="lab">…</div><p>…</p>), sans répéter l'existant, terminées par une rubrique Source.` :
        `Écris le template complet <template data-pop="${w.cle}" data-title="${w.titre}"> avec des rubriques <div class="lab">…</div><p>…</p> : Physiologie normale, Mécanisme, Conséquence clinique, Ce qui change la décision, Source. Pas d'autres balises que div.lab, p, b, i, sub, sup.`) +
      ` Chaque paragraphe : phrases complètes, mécanisme précis, chiffres sourcés.`,
      { label: `fenêtre:${w.cle}`, phase: 'Fenêtres', schema: HTMLW }),
    async (h, w) => {
      if (!h) return null
      const v = await agent(`${RULE}\n\nVÉRIFICATEUR MÉDICAL SCEPTIQUE. Fenêtre ${w.cle} « ${w.titre} » proposée :\n${h.html}\nSources citées : ${JSON.stringify(h.sources)}\nVérifie chaque affirmation : exactitude physiopathologique, chiffres et classes (contrôle dans ${ESC} pour l'ESC 2024), absence de surcertitude, cohérence avec le reste du cours I48, absence de sigle nouveau, format HTML. ok=false au moindre défaut, avec la liste précise.`,
        { label: `vérif:${w.cle}`, phase: 'Fenêtres', schema: VER, effort: 'high' })
      if (!v || v.ok) return { ...w, html: h.html, sources: h.sources, verif: 'ok' }
      const r = await agent(`${RULE}\n\nCorrige la fenêtre ${w.cle} en tenant compte des problèmes relevés par le vérificateur (rejette ceux qui sont infondés et explique-le dans sources).\nFenêtre :\n${h.html}\nProblèmes :\n${JSON.stringify(v.problemes)}`,
        { label: `révision:${w.cle}`, phase: 'Fenêtres', schema: HTMLW, effort: 'high' })
      return { ...w, html: (r && r.html) || h.html, sources: (r && r.sources) || h.sources, verif: r ? 'révisée' : 'non révisée', problemes: v.problemes }
    }),
  () => parallel(inlineAll.map(x => () => agent(
    `${RULE}\n\nVÉRIFICATEUR MÉDICAL ET STYLISTIQUE SCEPTIQUE des compléments intégrés au texte du fichier ${x.file}. Pour chaque édition, vérifie : exactitude du mécanisme et des chiffres (ESC 2024 dans ${ESC}), fidélité au sens de old, phrases complètes, absence de sigle nouveau, balises HTML de old conservées, longueur raisonnable. ok=false au moindre défaut, et donne new_corrige complet ; sinon new_corrige vide.\n${JSON.stringify(x.inline)}`,
    { label: `vérif-textes:${x.file}`, phase: 'Textes', schema: VERI, effort: 'high' })
    .then(v => ({ ...x, verdicts: v ? v.verdicts : [] })))),
])
return { plans: okPlans, fenetres: winRes.filter(Boolean), textes: inlRes.filter(Boolean) }