/* One independent learning space per specialty. Medical course engines stay local. */
(() => {
 'use strict';
 const element = document.getElementById('medina-category-organisation-data');
 if (!element) return;
 const O = JSON.parse(element.textContent), F = O.fragment;
 const blocks = new Map(O.blocks.map(block => [block.code, block])), aliases = new Map();
 const title = F.display_name || F.label.replace(/^[^-]+-\d+-/, '');
 const accent = F.accent || '#317765';
 document.documentElement.style.setProperty('--atlas-accent', accent);
 document.documentElement.dataset.atlasSpecialty = F.id;
 O.blocks.forEach(block => block.lessons.forEach(lesson => {
  lesson.variants.forEach(variant => aliases.set(variant.code, {block, lesson, variant}));
  if (!aliases.has(lesson.code)) aliases.set(lesson.code, {block, lesson, variant: lesson.variants[0]});
 }));
 if (O.nosology) O.nosology.lessons.forEach(lesson => {
  if (aliases.has(lesson.code)) return;
  const block = blocks.get(lesson.block);
  if (block) aliases.set(lesson.code, {block, lesson:{...lesson, integrated:false, source_fragment_id:F.id,
   variants:[{code:lesson.code,title:lesson.title,subcodes:[]}],entities:[]}, variant:lesson});
 });
 const own = lesson => lesson.integrated && lesson.source_fragment_id === F.id;
 const available = [...new Map(O.blocks.flatMap(block => block.lessons.filter(own).map(lesson => [lesson.code, {block, lesson}]))).values()];
 const filterNames = {frequent:'Pathologies fréquentes', federal_exam:'Examen Fédéral'};
 const filterCodes = new Map(Object.entries(O.nosology?.filters || {}).map(([key, codes]) => [key, new Set(codes)]));
 const activeFilter = () => filterCodes.has(route?.q.get('filter')) ? route.q.get('filter') : '';
 const included = lesson => !activeFilter() || filterCodes.get(activeFilter()).has(lesson.code);
 // Each view numbers its categories 1..n. Global keeps the embedded order; a filtered view
 // ranks by the number of its own lessons shown in the category, then by the global order.
 // Codes, lessons and course bodies never change: only the displayed rank does.
 const viewOrders = {
  frequent:{label:'Ordre : leçons fréquentes d’abord, puis ordre global', unit:['pathologie fréquente','pathologies fréquentes'],
   reason:'Dans ce filtre, les catégories qui réunissent le plus de pathologies fréquentes viennent d’abord ; à égalité, l’ordre global de la spécialité est conservé. Les numéros sont recalculés de 1 à n pour cette vue ; le code CIM de chaque catégorie ne change pas.'},
  federal_exam:{label:'Ordre : leçons fédérales d’abord, puis ordre global', unit:['pathologie de l’Examen fédéral','pathologies de l’Examen fédéral'],
   reason:'Dans ce filtre, les catégories qui réunissent le plus de leçons étoilées (correspondances PROFILES 2017 / SSP) viennent d’abord ; à égalité, l’ordre global de la spécialité est conservé. Les numéros sont recalculés de 1 à n pour cette vue ; le code CIM de chaque catégorie ne change pas.'}
 };
 const views = new Map();
 const visibleBlocks = () => {
  const filter = activeFilter();
  if (!views.has(filter)) {
   const codes = filterCodes.get(filter);
   const blocks = filter ? O.blocks.map(block => ({...block, lessons:block.lessons.filter(included)})).filter(block => block.lessons.length)
    .map(block => ({...block, view_weight:new Set(block.lessons.filter(lesson => codes.has(lesson.code)).map(lesson => lesson.code)).size}))
    .sort((a, b) => b.view_weight - a.view_weight || a.order - b.order) : O.blocks.map(block => ({...block}));
   blocks.forEach((block, index) => {block.rank = index + 1;});
   views.set(filter, blocks);
  }
  return views.get(filter);
 };
 const displayRank = block => block.rank || block.order;
 const visibleAvailable = () => available.filter(item => included(item.lesson));
 const filteredUrl = value => {
  const [path, query = ''] = value.split('?'), params = new URLSearchParams(query);
  if (activeFilter()) params.set('filter', activeFilter());
  return path + (params.size ? '?' + params.toString() : '');
 };
 const filterNotice = () => activeFilter() ? '<div class="mcg-filter-notice" role="status"><strong>Filtre : ' + h(filterNames[activeFilter()]) + '</strong><a class="mcg-back" href="#/home">← Toutes les leçons</a></div>' : '';
 const pad = value => String(value).padStart(2, '0');
 const rank = value => String(value) + '.';
 const orderNote = () => {
  const view = activeFilter(), order = view ? viewOrders[view] : O.category_order;
  return order ? '<p class="mcg-order-note" data-mcg-order-view="' + (view || 'global') + '" title="' + h(order.reason) + '">' + h(order.label) + '</p>' : '';
 };
 const ordinal = value => value + '<sup>' + (value === 1 ? 're' : 'e') + '</sup>';
 const weightNote = block => activeFilter() && typeof block.view_weight === 'number' ? '<span class="mcg-order-weight" data-mcg-view-weight="' + block.view_weight + '">' + block.view_weight + ' ' + viewOrders[activeFilter()].unit[block.view_weight > 1 ? 1 : 0] + (block.order !== block.rank ? ' · ' + ordinal(block.order) + ' en vue globale' : '') + '</span>' : typeof block.federal_weight === 'number' ? '<span class="mcg-order-weight">' + (block.federal_weight ? block.federal_weight + ' pathologie' + (block.federal_weight > 1 ? 's' : '') + ' de l’Examen fédéral' : 'Hors Examen fédéral') + '</span>' : '';
 const rankLabel = block => 'Catégorie ' + displayRank(block) + (activeFilter() ? ' sur ' + visibleBlocks().length + ' · ' + filterNames[activeFilter()] : '');
 // Concise display name on screen; the official CIM label (when present) for tooltips, aria-labels and search.
 const officialTitle = block => block.official_title || block.title;
 // WCAG 2.5.3 : le nom accessible reprend le nom affiché ; le libellé officiel reste en info-bulle.
 const officialHint = block => block.official_title && block.official_title !== block.title ? ' title="' + h(block.official_title) + '"' : '';
 const name = lesson => lesson.code + ' — ' + lesson.title;
 let goldIconIndex = 0;
 const gold = lesson => {
  if (!lesson.gold_star?.enabled) return '';
  const id = 'mcg-gold-' + (++goldIconIndex);
  return '<sup class="nosology-gold" role="img" aria-label="Étoile d’Or permanente · PROFILES SSP ' + h((Array.isArray(lesson.gold_star.ssp) ? lesson.gold_star.ssp : []).join(', ')) + '" title="Lien pédagogique PROFILES 2017 · SSP ' + h((Array.isArray(lesson.gold_star.ssp) ? lesson.gold_star.ssp : []).join(', ')) + '"><svg class="mcg-gold-symbol" viewBox="0 0 80 84" aria-hidden="true" focusable="false"><defs>'
   + '<linearGradient id="'+id+'-metal" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#fff3a6"/><stop offset=".2" stop-color="#efc34e"/><stop offset=".43" stop-color="#b97908"/><stop offset=".57" stop-color="#ffdf70"/><stop offset=".8" stop-color="#f5c64a"/><stop offset="1" stop-color="#8f5700"/></linearGradient>'
   + '<radialGradient id="'+id+'-shadow"><stop stop-color="#76500a" stop-opacity=".28"/><stop offset="1" stop-color="#76500a" stop-opacity="0"/></radialGradient></defs>'
   + '<ellipse cx="41" cy="79" rx="30" ry="4" fill="url(#'+id+'-shadow)"/>'
   + '<path d="M40 5L50 28L76 31L56 48L61 74L40 61L19 74L24 48L4 31L30 28Z" fill="url(#'+id+'-metal)" stroke="#9b6305" stroke-width="1"/>'
   + '<path d="M40 5L40 41L30 28Z" fill="#fff5b5"/><path d="M76 31L40 41L50 28Z" fill="#ffeb94"/><path d="M61 74L40 41L56 48Z" fill="#ad6b03"/><path d="M19 74L40 41L40 61Z" fill="#ffe899"/><path d="M4 31L40 41L24 48Z" fill="#cc8f18"/>'
   + '<path d="M40 8L31 29L8 32M41 42L58 70" fill="none" stroke="#fff5c2" stroke-width="1.25" stroke-linecap="round" stroke-opacity=".9"/>'
   + '<path d="M50 29L72 32L55 47M40 60L20 72" fill="none" stroke="#805009" stroke-width=".9" stroke-opacity=".5"/>'
   + '</svg></sup>';
 };
 const markedTitle = (lesson, label = lesson.title) => {
  const star = gold(lesson);
  if (!star) return h(label);
  const glyphs = Array.from(label.trimEnd()), last = glyphs.pop() || '';
  return h(glyphs.join('')) + '<span class="mcg-star-tail">' + h(last) + star + '</span>';
 };
 const pct = v => (v.total ? Math.round(1000*v.filled/v.total)/10 : 0).toLocaleString('fr-CH') + ' %';
 const categoryProgress = block => {
  if (!block.progress) return '';
  return '<div class="mcg-category-progress" data-mcg-category-progress="' + h(block.code) + '" aria-label="Avancement de cette catégorie">' + [['federal_exam','Leçons fédérales'],['global','Avancement global de la catégorie']].map(([key,label]) => {
   const value = block.progress[key];
   if (!value) return '';
   const percentage = value.percent.toLocaleString('fr-CH', {maximumFractionDigits:2}) + ' %';
   return '<div class="mcg-category-gauge" data-mcg-progress-kind="' + key + '"><span class="mcg-category-gauge-copy"><span>' + h(label) + '</span><b data-mcg-progress-count>' + value.filled + ' / ' + value.total + '</b></span><progress max="' + Math.max(1,value.total) + '" value="' + value.filled + '" aria-label="' + h(label + ' : ' + value.filled + ' sur ' + value.total) + '"></progress><b data-mcg-progress-percent>' + h(percentage) + '</b></div>';
  }).join('') + '</div>';
 };
 const gauge = (label, value, note='', filter='') => {
  if (!value) return '';
  const global = filter === 'global', linked = global || filterCodes.has(filter), tag = linked ? 'a' : 'div';
  const navigation = global ? ' href="#/home" data-mcg-global aria-label="Afficher toutes les catégories et tous les chapitres du fragment"' : linked ? ' href="#/home?filter=' + filter + '" data-mcg-filter="' + filter + '" aria-label="Filtrer les leçons : ' + h(filterNames[filter]) + '"' + (activeFilter() === filter ? ' aria-current="page"' : '') : '';
  return '<' + tag + ' class="nosology-progress" title="' + h(note) + '"' + navigation + '><span class="gauge-copy"><span class="gauge-label">' + h(label) + '</span> <b class="gauge-abs">(' + value.filled + ' / ' + value.total + ')</b>' + (value.total ? '' : ' · non applicable') + '</span><progress max="' + Math.max(1,value.total) + '" value="' + value.filled + '" aria-label="' + h(label + ' : ' + value.filled + ' sur ' + value.total) + '"></progress><b>(' + pct(value) + ')</b></' + tag + '>';
 };
 let filterIconIndex = 0;
 const filterHeading = () => {
  const id = 'mcg-funnel-' + (++filterIconIndex);
  return '<div class="mcg-filter-heading"><svg class="mcg-filter-symbol" viewBox="0 0 80 80" aria-hidden="true" focusable="false"><defs>'
   + '<linearGradient id="'+id+'-metal" x1="0" x2="1"><stop offset="0" stop-color="#476476"/><stop offset=".18" stop-color="#aecbd8"/><stop offset=".35" stop-color="#f6fdff"/><stop offset=".48" stop-color="#98b6c8"/><stop offset=".69" stop-color="#d9eef7"/><stop offset="1" stop-color="#3b5d76"/></linearGradient>'
   + '<linearGradient id="'+id+'-inside" x1=".15" y1="0" x2=".8" y2="1"><stop stop-color="#24445c"/><stop offset=".46" stop-color="#698da3"/><stop offset="1" stop-color="#d9eff7"/></linearGradient>'
   + '<linearGradient id="'+id+'-rim" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#f8feff"/><stop offset=".36" stop-color="#bdd8e5"/><stop offset=".65" stop-color="#456a82"/><stop offset="1" stop-color="#e5f5fa"/></linearGradient>'
   + '<radialGradient id="'+id+'-shadow"><stop stop-color="#163b55" stop-opacity=".3"/><stop offset="1" stop-color="#163b55" stop-opacity="0"/></radialGradient></defs>'
   + '<ellipse cx="42" cy="72" rx="25" ry="5" fill="url(#'+id+'-shadow)"/>'
   + '<path d="M10 21Q40 37 70 21L47 48V65Q44 70 36 71V49Z" fill="url(#'+id+'-metal)" stroke="#496c81" stroke-width=".8"/>'
   + '<path d="M36 49V69Q42 69 47 65V48" fill="url(#'+id+'-metal)" stroke="#476c83" stroke-width=".7"/>'
   + '<path d="M14 25L38 49V66" fill="none" stroke="#f3fcff" stroke-opacity=".85" stroke-width="1.5"/>'
   + '<path d="M65 26L45 49V63" fill="none" stroke="#1b405d" stroke-opacity=".38" stroke-width="1.4"/>'
   + '<ellipse cx="40" cy="20" rx="30" ry="11" fill="url(#'+id+'-rim)" stroke="#52748a" stroke-width=".8"/>'
   + '<ellipse cx="40" cy="20" rx="26" ry="7.5" fill="url(#'+id+'-inside)" stroke="#e4f6fc" stroke-width="1"/>'
   + '<path d="M17 18Q40 9 63 18" fill="none" stroke="#f9feff" stroke-opacity=".9" stroke-width="1.3"/>'
   + '<path d="M19 23Q40 29 61 23" fill="none" stroke="#1c405c" stroke-opacity=".5" stroke-width="1"/>'
   + '<path d="M38 70Q42 70 47 66" fill="none" stroke="#eefaff" stroke-width="1"/>'
   + '</svg><span class="mcg-filter-label">Filtre</span></div>';
 };
 const fragmentGauges = () => O.nosology ? filterHeading()+'<div class="nosology-gauges">'+gauge('Pathologies fréquentes',O.nosology.gauges.frequent,'Afficher les leçons sélectionnées dans leurs catégories.','frequent')+gauge('Examen Fédéral',O.nosology.gauges.federal_exam,'Afficher les leçons liées aux SSP PROFILES 2017 dans leurs catégories.','federal_exam')+gauge('Avancement global du fragment',O.nosology.gauges.global,'Afficher toutes les catégories et tous les chapitres du fragment.','global')+'</div>' : '';
 const categoryUrl = block => filteredUrl('#/home?category=' + encodeURIComponent(block.code));
 const status = lesson => own(lesson) ? (lesson.work_in_progress ? 'Lire la version de travail' : 'Lire le cours') : 'En préparation';
 const lessonUrl = (block, lesson) => own(lesson) ? filteredUrl(lesson.url) : lesson.code.includes('.') ? filteredUrl('#/entry/' + encodeURIComponent(lesson.code)) : categoryUrl(block) + '&lesson=' + encodeURIComponent(lesson.code);
 const arrow = '<span class="mcg-arrow" aria-hidden="true">↗</span>';
 const book = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5c-3-2-6-2-9-1v15c3-1 6-1 9 1m0-15c3-2 6-2 9-1v15c-3-1-6-1-9 1V5Z"/></svg>';
 const rule = () => '<details class="mcg-rule"><summary>Un mot souligné ? Explorez son explication.</summary><p>Dans les cours, les mots interactifs ouvrent les mécanismes, les précisions et leurs sources. Les quatre onglets vous accompagnent du raisonnement à la prise en charge.</p></details>';
 function categoryCard(block) {
  const count = block.lessons.filter(own).length;
  return '<a class="mcg-category-card" href="' + h(categoryUrl(block)) + '" data-mcg-category="' + h(block.code) + '" data-mcg-rank="' + displayRank(block) + '" title="' + h(officialTitle(block)) + '" aria-label="' + h(rankLabel(block)) + ' : ' + h(block.title) + ' — ' + h(block.code) + '"><div class="mcg-category-top"><span class="mcg-category-number" data-mcg-rank-value>' + rank(displayRank(block)) + '</span><span class="mcg-code">' + h(block.code) + '</span></div><h2>' + h(block.title) + '</h2>' + weightNote(block) + categoryProgress(block) + '<span class="mcg-category-foot"><span>' + block.lessons.length + ' chapitre' + (block.lessons.length > 1 ? 's' : '') + (count ? '<i class="mcg-available-dot"></i>' + count + ' disponible' + (count > 1 ? 's' : '') : '') + '</span>' + arrow + '</span></a>';
 }
 function variants(lesson) {
  const listed = lesson.searchVariants || lesson.variants;
  const entities = lesson.entities || [];
  const nested = entities.length ? '<details class="mcg-variants"><summary>Entités détaillées · ' + entities.length + '</summary><ul>' + entities.map(entity => '<li><a href="' + h(filteredUrl('#/entry/' + encodeURIComponent(entity.code))) + '">' + markedTitle(entity, entity.code + ' — ' + entity.title) + '</a></li>').join('') + '</ul></details>' : '';
  if (listed.length === 1 && listed[0].code === lesson.code && listed[0].title === lesson.title) return nested;
  return '<details class="mcg-variants"><summary>Voir les catégories regroupées</summary><ul>' + listed.map(variant => '<li data-mcg-variant="' + h(variant.code) + '"><b>' + h(variant.code) + '</b> — ' + h(variant.title) + '</li>').join('') + '</ul></details>' + nested;
 }
 function lessonCard(block, lesson, featured = false) {
  return '<article class="mcg-lesson' + (featured ? ' mcg-featured-lesson' : '') + '" data-mcg-lesson="' + h(lesson.code) + '" data-mcg-reference="false"><a class="mcg-lesson-main" href="' + h(lessonUrl(block, lesson)) + '" aria-label="' + h(name(lesson)) + ' · ' + status(lesson) + '"><span class="mcg-lesson-icon">' + book + '</span><span class="mcg-course-copy"><span class="mcg-code">' + h(lesson.code) + '</span><span class="mcg-lesson-title">' + markedTitle(lesson) + '</span><span class="mcg-lesson-state ' + (own(lesson) ? 'is-available' : 'is-planned') + '">' + status(lesson) + ' <span aria-hidden="true">→</span></span></span></a>' + (!featured ? variants(lesson) : '') + '</article>';
 }
 function blockSection(block) {
  return '<section class="mcg-block" data-mcg-block="' + h(block.code) + '" data-mcg-rank="' + displayRank(block) + '"><header class="mcg-block-heading"><div><span class="mcg-eyebrow">Catégorie <span data-mcg-rank-value>' + displayRank(block) + '</span> · ' + h(block.code) + '</span><h2' + officialHint(block) + '>' + h(block.title) + '</h2></div><span class="mcg-section-count">' + block.lessons.length + ' chapitre' + (block.lessons.length > 1 ? 's' : '') + '</span></header>' + categoryProgress(block) + '<div class="mcg-lessons">' + block.lessons.map(lesson => lessonCard(block, lesson)).join('') + '</div></section>';
 }
 function cover(compact = false) {
  const count = visibleAvailable().length, categories = visibleBlocks().length;
  return '<header class="mcg-cover' + (compact ? ' is-compact' : '') + '"><div class="mcg-cover-copy"><span class="mcg-eyebrow">MEDINA · Votre bibliothèque médicale</span><h1>' + h(title) + '</h1><p>' + h(F.description || 'Retrouvez les cours de votre spécialité, organisés par catégories.') + '</p><div class="mcg-cover-actions">' + (count ? '<a class="mcg-primary-action" href="' + h(filteredUrl('#/search?available=1')) + '">Lire les cours <span aria-hidden="true">→</span></a>' : '') + '<button class="mcg-explore-action" type="button" data-mcg-explore>Les catégories <span aria-hidden="true">↓</span></button></div></div><div class="mcg-counts" aria-label="Contenu de la bibliothèque"><span><b>' + count + '</b> cours disponible' + (count > 1 ? 's' : '') + '</span><span><b>' + categories + '</b> catégorie' + (categories > 1 ? 's' : '') + '</span></div></header>';
 }
 function trail(block, lesson) {
  return '<nav class="mcg-breadcrumbs" aria-label="Fil d’Ariane"><a href="' + h(filteredUrl('#/home')) + '">' + h(title) + '</a>' + (block ? '<span aria-hidden="true">/</span><a href="' + h(categoryUrl(block)) + '">' + h(block.title) + '</a>' : '') + (lesson ? '<span aria-hidden="true">/</span><span>' + h(name(lesson)) + '</span>' : '') + '</nav>';
 }
 function planned(block, lesson) {
  if (lesson.plan?.length) return '<section class="mcg-planned-panel" aria-labelledby="mcg-planned-title"><span class="mcg-eyebrow">' + h(lesson.code) + ' · En préparation · plan prévu</span><h2 id="mcg-planned-title" tabindex="-1">' + markedTitle(lesson) + '</h2>' + (lesson.gold_star?.enabled ? '<p>PROFILES 2017 · SSP ' + h(lesson.gold_star.ssp.join(', ')) + ' · correspondance pédagogique</p>' : '') + '<div class="nosology-plan">' + lesson.plan.map(section => '<section><h3>' + h(section.title) + '</h3>' + (section.content ? '<p>' + h(section.content) + '</p>' : '') + '</section>').join('') + '</div>' + variants(lesson) + '</section>';
  return '<section class="mcg-planned-panel" aria-labelledby="mcg-planned-title"><span class="mcg-eyebrow">' + h(lesson.code) + ' · En préparation</span><h2 id="mcg-planned-title" tabindex="-1">' + markedTitle(lesson) + '</h2><p>Le contenu de ce chapitre est en cours de préparation. Vous pouvez déjà consulter les catégories qui lui sont rattachées.</p><ul>' + lesson.variants.map(variant => '<li><strong>' + h(variant.code) + ' — ' + h(variant.title) + '</strong>' + (variant.subcodes.length ? '<details><summary>Sous-catégories</summary><ul>' + variant.subcodes.map(subcode => '<li>' + h(subcode.code) + ' — ' + h(subcode.title) + '</li>').join('') + '</ul></details>' : '') + '</li>').join('') + '</ul></section>';
 }
 readRoute = function() {
  const raw = location.hash.slice(2) || 'home', [head, query = ''] = raw.split('?'), parts = head.split('/').map(decodeURIComponent);
  const result = {type:parts[0] || 'home', id:parts[1] || '', extra:parts[2] || '', q:new URLSearchParams(query)};
  if (!filterCodes.has(result.q.get('filter'))) result.q.delete('filter');
  if (result.type === 'category') {result.q.set('category', result.id); result.type = 'home'; result.id = '';}
  if (result.type === 'pathology') result.type = 'entry';
  if (result.type === 'entry') {
   result.id = result.id.toUpperCase(); const item = aliases.get(result.id);
   if (!item) return {type:'home', id:'', q:new URLSearchParams()};
   const selectedCodes = filterCodes.get(result.q.get('filter'));
   if (selectedCodes && !selectedCodes.has(item.lesson.code) && !O.blocks.some(block => block.lessons.some(lesson => selectedCodes.has(lesson.code) && lesson.entities?.some(entity => entity.code === result.id)))) return {type:'home', id:'', q:new URLSearchParams({filter:result.q.get('filter')})};
   if (own(item.lesson)) result.id = item.lesson.code;
   result.q.delete('specialty'); result.q.delete('view');
  }
  if (result.type === 'specialty') {result.type = 'home'; result.id = '';}
  if (result.type === 'clinical-skills' && F.id !== 'S01') result.type = 'home';
  if (!['home','entry','search','notebook','method','clinical-skills'].includes(result.type)) return {type:'home', id:'', q:new URLSearchParams()};
  return result;
 };
 homePage = function() {
  const viewBlocks = visibleBlocks(), viewAvailable = visibleAvailable();
  const block = viewBlocks.find(item => item.code === route.q.get('category')), selected = block?.lessons.find(lesson => lesson.code === route.q.get('lesson'));
  pageTitle((block ? block.title + ' · ' : '') + (activeFilter() ? filterNames[activeFilter()] + ' · ' : '') + title);
  if (block) return '<div class="mcg-home">' + trail(block, selected) + filterNotice() + '<a class="mcg-back" href="' + h(filteredUrl('#/home')) + '">← Toutes les catégories</a>' + (selected ? planned(block, selected) : '') + blockSection(block) + rule() + '</div>';
  const filtered = route.q.get('available') === '1', shown = filtered ? viewBlocks.filter(b => b.lessons.some(own)) : viewBlocks;
  const last = viewAvailable.find(item => item.lesson.code === (typeof state !== 'undefined' ? state.last : null));
  const resume = last ? '<a class="mcg-resume" href="' + h(lessonUrl(last.block,last.lesson)) + '"><span><small>Votre dernière lecture</small><strong>' + h(name(last.lesson)) + '</strong></span><span>Reprendre <span aria-hidden="true">→</span></span></a>' : '';
  const courses = viewAvailable.length ? '<section class="mcg-start" aria-labelledby="mcg-start-title"><div class="mcg-page-actions"><div><span class="mcg-eyebrow">Pour commencer</span><h2 id="mcg-start-title">Les cours à explorer</h2></div><a class="mcg-text-link" href="' + h(filteredUrl('#/search?available=1')) + '">Voir les ' + viewAvailable.length + ' cours <span aria-hidden="true">→</span></a></div><div class="mcg-featured-grid">' + viewAvailable.slice(0,3).map(item => lessonCard(item.block, item.lesson, true)).join('') + '</div></section>' : '<section class="mcg-empty"><h2>' + (activeFilter() ? 'Aucun cours disponible dans ce filtre.' : 'Les cours se préparent.') + '</h2><p>Explorez les catégories de cette spécialité pour retrouver les chapitres prévus.</p></section>';
  const searchForm = '<form class="mcg-home-search" role="search" aria-label="Recherche dans cette spécialité"><label for="mcg-home-query">Trouver un chapitre</label><div><input id="mcg-home-query" name="q" type="search" placeholder="Un intitulé, une maladie ou un code CIM…" autocomplete="off"><button type="submit">Rechercher <span aria-hidden="true">→</span></button></div></form>';
  return '<div class="mcg-home">' + cover() + fragmentGauges() + filterNotice() + resume + searchForm + courses + (!activeFilter() && F.id === 'T1' ? '<a class="mcg-draft-access" href="../apercus/infectiologie.html#/entry/A41"><span><span class="mcg-eyebrow">Version de travail</span><strong>A41 — Sepsis et choc septique de l’adulte</strong></span><span class="mcg-text-link">Consulter l’aperçu ↗</span></a>' : '') + (!activeFilter() && F.id === 'S01' ? '<a class="s01-cs-gateway" href="#/clinical-skills"><span><span class="mcg-eyebrow">Pratique clinique</span><strong>Sémiologie · Examen cardiovasculaire</strong></span><span class="mcg-text-link">Explorer le parcours →</span></a>' : '') + '<section aria-labelledby="mcg-categories-title"><div class="mcg-page-actions mcg-categories-heading"><div><span class="mcg-eyebrow">Toute la spécialité</span><h2 id="mcg-categories-title" tabindex="-1">Les catégories</h2>' + orderNote() + '</div>' + (viewBlocks.length ? '<div class="mcg-filters" aria-label="Filtrer les catégories"><a href="' + h(filteredUrl('#/home')) + '"' + (!filtered ? ' aria-current="true"' : '') + '>Toutes <span>' + viewBlocks.length + '</span></a><a href="' + h(filteredUrl('#/home?available=1')) + '"' + (filtered ? ' aria-current="true"' : '') + '>Avec un cours</a></div>' : '') + '</div><div class="mcg-category-grid">' + (shown.map(categoryCard).join('') || '<p class="mcg-empty">' + (activeFilter() ? 'Aucune leçon ne correspond à ce filtre dans cette spécialité.' : 'Les catégories de cette spécialité seront ajoutées au fil de la rédaction.') + '</p>') + '</div></section>' + rule() + '</div>';
 };
 specialtyPage = homePage;
 searchPageView = function() {
  const query = route.q.get('q') || '', needle = norm(query), onlyAvailable = route.q.get('available') === '1', matches = new Map();
  visibleBlocks().forEach(block => block.lessons.forEach(lesson => {
   if (onlyAvailable && !own(lesson)) return;
   const text = [block.code, block.title, block.official_title || '', lesson.code, lesson.title, ...lesson.variants.flatMap(v => [v.code, v.title, ...v.subcodes.flatMap(s => [s.code, s.title])])].join(' ');
   if (!needle || norm(text).includes(needle)) {
    const previous = matches.get(lesson.code), merged = new Map((previous?.lesson.searchVariants || []).map(v => [v.code, v]));
    lesson.variants.forEach(v => merged.set(v.code, v));
    const preferred = previous || {block, lesson};
    matches.set(lesson.code, {block:preferred.block, lesson:{...preferred.lesson, searchVariants:[...merged.values()]}});
   }
  }));
  if(needle && !onlyAvailable && !activeFilter()) aliases.forEach(item=>{
   if(item.lesson.code.includes('.') && norm(item.lesson.code+' '+item.lesson.title).includes(needle)) matches.set(item.lesson.code,item);
  });
  pageTitle('Recherche · ' + title);
  return '<div class="mcg-home">' + trail() + filterNotice() + '<div class="mcg-search-heading"><span class="mcg-eyebrow">' + h(title) + '</span><h1>' + (query ? '« ' + h(query) + ' »' : onlyAvailable ? 'Les cours disponibles.' : 'Tous les chapitres.') + '</h1><p>' + matches.size + ' résultat' + (matches.size > 1 ? 's' : '') + '</p></div><div class="mcg-filters"><a href="' + h(filteredUrl('#/search?q=' + encodeURIComponent(query))) + '"' + (!onlyAvailable ? ' aria-current="true"' : '') + '>Tous les chapitres</a><a href="' + h(filteredUrl('#/search?available=1&q=' + encodeURIComponent(query))) + '"' + (onlyAvailable ? ' aria-current="true"' : '') + '>Cours disponibles</a></div><div class="mcg-lessons">' + ([...matches.values()].map(item => lessonCard(item.block, item.lesson)).join('') || '<p class="mcg-empty">Aucun chapitre ne correspond à cette recherche. Essayez un intitulé ou un code CIM.</p>') + '</div></div>';
 };
 methodPage = function() {
  pageTitle('Lecture et sources · ' + title);
  return '<div class="mcg-home">' + trail() + '<div class="mcg-search-heading"><span class="mcg-eyebrow">' + h(title) + '</span><h1>Lire, comprendre, explorer.</h1><p>Quelques repères pour parcourir votre espace d’étude.</p></div><section class="mcg-planned-panel"><h2>Votre bibliothèque</h2><p>Retrouvez les cours de ' + h(title) + ' dans leurs catégories. Les chapitres annoncés « En préparation » ne contiennent pas encore de cours disponible.</p><h2>Les quatre onglets du cours</h2><p>Passez de la pathologie et de la prise en charge aux examens, aux sciences fondamentales et à la pharmacologie. Cliquez sur les mots soulignés pour ouvrir leurs explications et leurs références.</p><h2>Votre confort de lecture</h2><p>La barre du cours permet de régler la police, la taille et le mode livre. Navigo donne accès aux parties du cours. Le carnet conserve vos notes dans cet espace.</p><h2>Les sources</h2><p>Les références sont citées dans les cours et leurs fenêtres. L’organisation actuelle utilise ' + h(O.version) + ' ; une catégorie de nomenclature ne constitue pas une recommandation clinique.</p><a class="mcg-back" href="#/home">← Retrouver les catégories de ' + h(title) + '</a></section></div>';
 };
 const originalEntry = entryPage;
 const originalCoursePage = MEDINA_coursePage;
 MEDINA_coursePage = function(entry) {
  const html = originalCoursePage(entry);
  if (!activeFilter()) return html;
  const item = aliases.get(entry.code);
  // Change only the reader's navigation control; embedded course content is untouched.
  return html.replace(/(<div class="mc-toolbar mc-ui">)<a class="btn tiny"[^>]*>(?:Plan de révision détaillé|← Tous les cours)<\/a>/, '$1<a class="btn tiny" href="' + h(item ? categoryUrl(item.block) : filteredUrl('#/home')) + '">← Les chapitres</a>');
 };
 entryPage = function() {
  const item = aliases.get(route.id);
  if (item && !own(item.lesson)) {pageTitle(name(item.lesson) + ' · ' + title); return '<div class="mcg-home">' + trail(item.block, item.lesson) + planned(item.block, item.lesson) + '<a class="mcg-back" href="' + h(categoryUrl(item.block)) + '">← Les chapitres de cette catégorie</a></div>';}
  const content = originalEntry();
  if (item) pageTitle(name(item.lesson) + ' · ' + title);
  return item?.lesson.gold_star?.enabled ? '<div class="nosology-course-star">' + gold(item.lesson) + ' PROFILES 2017 · SSP ' + h(item.lesson.gold_star.ssp.join(', ')) + '</div>' + content : content;
 };
 crumbs = function() {const item = aliases.get(route?.id) || aliases.get(typeof MC_code === 'function' ? MC_code(route?.id) : route?.id); return item ? trail(item.block, item.lesson) : trail();};
 nextPrevious = function(entry) {
  const item = aliases.get(entry.code), lessons = item?.block.lessons.filter(lesson => own(lesson) && included(lesson)) || [], index = lessons.findIndex(l => l.code === item?.lesson.code), previous = lessons[index-1], next = lessons[index+1];
  return '<nav class="bottomnav mcg-bottomnav" aria-label="Navigation entre les chapitres">' + (previous ? '<a class="btn" href="' + h(lessonUrl(item.block,previous)) + '">← ' + h(name(previous)) + '</a>' : '<span></span>') + '<a class="btn tiny" href="' + h(item ? categoryUrl(item.block) : '#/home') + '">Les chapitres</a>' + (next ? '<a class="btn" href="' + h(lessonUrl(item.block,next)) + '">' + h(name(next)) + ' →</a>' : '<span></span>') + '</nav>';
 };
 footer = () => (!activeFilter() && O.nosology?.secondary_references?.length ? '<details class="mcg-variants"><summary>Renvois associés à cette spécialité · ' + O.nosology.secondary_references.length + '</summary><ul>' + O.nosology.secondary_references.map(link=>'<li><a href="'+h(link.url)+'">'+h(link.code)+' · '+h(link.fragment)+'</a></li>').join('')+'</ul></details>' : '') + '<footer class="mcg-footer"><span>MEDINA <span aria-hidden="true">/</span> ' + h(title) + '</span><span>' + h(O.version) + ' <span aria-hidden="true">·</span> <a href="../index.html">Toutes les spécialités ↗</a></span></footer>';
 drawSidebar = function() {
  const active = aliases.get(route?.id), category = route?.q.get('category') || active?.block.code;
  document.getElementById('spec-nav').innerHTML = visibleBlocks().map(block => '<details class="mcg-sidebar-block" ' + (category === block.code ? 'open' : '') + ' data-mcg-sidebar-category="' + h(block.code) + '" data-mcg-rank="' + displayRank(block) + '"><summary><span data-mcg-rank-value>' + rank(displayRank(block)) + '</span><b>' + h(block.title) + '</b></summary><a class="mcg-sidebar-all" href="' + h(categoryUrl(block)) + '">Tous les chapitres <span aria-hidden="true">→</span></a>' + block.lessons.map(lesson => '<a class="mcg-sidebar-lesson ' + (active?.lesson.code === lesson.code ? 'active' : '') + '" href="' + h(lessonUrl(block, lesson)) + '" aria-label="' + h(name(lesson)) + '" data-fragment-chapter="' + (own(lesson) ? h(lesson.code) : '') + '" data-mcg-sidebar-lesson="' + h(lesson.code) + '"><span>' + '<span class="mcg-sidebar-title">' + markedTitle(lesson) + '</span><small>' + h(lesson.code) + ' · ' + (own(lesson) ? 'Disponible' : 'En préparation') + '</small></span></a>').join('') + '</details>').join('') || '<p class="mcg-sidebar-empty">Aucune catégorie à afficher.</p>';
  document.querySelectorAll('.nav-main a').forEach(link => {
   const base = link.dataset.mcgBaseHref || link.getAttribute('href');
   link.dataset.mcgBaseHref = base;
   if (base === '#/search') link.setAttribute('href', filteredUrl(base));
   link.classList.toggle('active', base === '#/' + route?.type);
  });
  if(O.nosology){
   const note=document.querySelector('.sidebar-note');
   if(note)note.innerHTML=fragmentGauges()+gauge('MEDINA · avancement global',O.nosology.global_progress);
  }
 };
 showCommandPalette = function() {openModal(title, '<div class="command-links"><a data-close-modal class="command-link" href="' + h(filteredUrl('#/home')) + '">L’accueil et les catégories</a><a data-close-modal class="command-link" href="' + h(filteredUrl('#/search?available=1')) + '">Les cours disponibles</a><a data-close-modal class="command-link" href="' + h(filteredUrl('#/search')) + '">Rechercher un chapitre</a></div><div class="mcg-category-grid">' + visibleBlocks().map(block => categoryCard(block).replace('<a ', '<a data-close-modal ')).join('') + '</div>');};
 document.getElementById('global-search-form').onsubmit = event => {event.preventDefault();location.hash=filteredUrl('#/search?q='+encodeURIComponent(document.getElementById('global-search').value.trim()));};
 document.getElementById('command-btn').onclick = showCommandPalette;
 const previousBind = bindPage;
 bindPage = function() {
  previousBind(); document.getElementById('mcg-planned-title')?.focus({preventScroll:true});
  const readerLesson = aliases.get(route?.id)?.lesson, readerTitle = document.querySelector('.mc-chap-head h1');
  if (readerLesson?.gold_star?.enabled && readerTitle && !readerTitle.querySelector('.nosology-gold')) {
   const walker = document.createTreeWalker(readerTitle, NodeFilter.SHOW_TEXT);
   let lastText = null, node;
   while ((node = walker.nextNode())) if (node.textContent.trim()) lastText = node;
   if (lastText) {
    // Decorate the reader heading only. Existing heading elements and course panels stay intact.
    const index = lastText.data.search(/\S\s*$/u), finalGlyph = lastText.splitText(index);
    const glyphLength = Array.from(finalGlyph.data)[0].length;
    if (finalGlyph.length > glyphLength) finalGlyph.splitText(glyphLength);
    const tail = document.createElement('span'); tail.className = 'mcg-star-tail';
    finalGlyph.before(tail); tail.append(finalGlyph); tail.insertAdjacentHTML('beforeend', gold(readerLesson));
   }
  }
  document.querySelectorAll('.mc .mc-toc:not(details)').forEach(toc=>{
   const details=document.createElement('details'),summary=document.createElement('summary');
   details.className=toc.className;summary.textContent='Sommaire de cet onglet';
   const list=toc.querySelector('ol');if(!list)return;
   details.open=matchMedia('(min-width:1100px)').matches;
   details.append(summary,list);toc.replaceWith(details);
  });
  const form=document.querySelector('.mcg-home-search');
  if(form)form.onsubmit=event=>{event.preventDefault();const query=form.elements.q.value.trim();location.hash=filteredUrl('#/search?q='+encodeURIComponent(query));};
  document.querySelector('[data-mcg-explore]')?.addEventListener('click',()=>{const heading=document.getElementById('mcg-categories-title');heading?.scrollIntoView({block:'start',behavior:matchMedia('(prefers-reduced-motion:reduce)').matches?'instant':'smooth'});heading?.focus({preventScroll:true});});
 };
 document.getElementById('medora-intelligence-link')?.remove();
 document.getElementById('medina-fragment-empty')?.remove();
 const brand = document.querySelector('.brand');
 if (brand) brand.innerHTML = '<span class="brandmark">' + book + '</span><span><strong>MEDINA</strong><small>' + h(title) + '</small></span>';
 const version = document.querySelector('.sidebar .version');
 if (version) version.innerHTML = '<a href="../index.html">← Toutes les spécialités</a>';
 document.querySelector('.sidebar .sidebar-note')?.replaceChildren(document.createTextNode(available.length + ' cours à explorer · ' + title));
 const navTitle = document.querySelector('.sidebar .nav-title'); if (navTitle) navTitle.textContent = 'Les catégories';
 const search = document.getElementById('global-search');
 search.placeholder = 'Rechercher en ' + title.toLocaleLowerCase('fr') + '…';
 search.setAttribute('aria-label', 'Rechercher dans les cours de ' + title);
 const topbar = document.querySelector('.topbar');
 topbar.insertAdjacentHTML('afterbegin', '<a class="mcg-top-title" href="#/home">' + h(title) + '</a>');
 document.getElementById('command-btn').setAttribute('aria-label', 'Ouvrir les catégories de ' + title);
 // One responsive course plan for every specialty. Leave room for reading on laptops.
 MC_navigoMount = function(m) {
  const host=document.createElement('div');host.className='mc-navigo';
  host.innerHTML='<button type="button" class="mc-navigo-trigger" aria-controls="mc-navigo-panel" aria-expanded="false"><span aria-hidden="true">▤</span> Plan du cours</button><aside id="mc-navigo-panel" class="mc-navigo-panel" aria-label="Navigo : plan du cours" hidden><div class="mc-navigo-head"><div><small>Plan du cours</small><strong class="mc-navigo-title"></strong></div><button type="button" class="mc-navigo-close" aria-label="Fermer le plan du cours">×</button></div><div class="mc-navigo-tabs" role="group" aria-label="Onglets du cours"></div><label class="mc-navigo-search-label">Rechercher une partie<input class="mc-navigo-search" type="search" placeholder="Titre ou numéro…"></label><nav class="mc-navigo-list" aria-label="Parties et sous-parties"></nav><div class="mc-navigo-foot"></div></aside>';
  document.body.append(host);
  const desktop=matchMedia('(min-width:1480px)'),trigger=host.querySelector('.mc-navigo-trigger'),drawer=host.querySelector('.mc-navigo-panel'),list=host.querySelector('.mc-navigo-list'),search=host.querySelector('.mc-navigo-search');
  let buttons=[],headings=[];
  function open(on,focus=true){drawer.hidden=desktop.matches?false:!on;trigger.setAttribute('aria-expanded',String(!drawer.hidden));if(focus&&!desktop.matches)(on?search:trigger).focus({preventScroll:true});}
  function move(heading){
   const body=heading.closest('.mc-body');
   if(m.classList.contains('book')&&body){
    const page=Array.from(body.children).find(child=>child.contains(heading));
    if(page){body.scrollTo({left:body.scrollLeft+page.getBoundingClientRect().left-body.getBoundingClientRect().left,behavior:'instant'});page.scrollTo({top:page.scrollTop+heading.getBoundingClientRect().top-page.getBoundingClientRect().top-16,behavior:'instant'});heading.setAttribute('tabindex','-1');heading.focus({preventScroll:true});return;}
   }
   heading.scrollIntoView({block:'start',behavior:'instant'});heading.setAttribute('tabindex','-1');heading.focus({preventScroll:true});
  }
  function filter(){const query=norm(search.value);let count=0;buttons.forEach(button=>{button.hidden=!norm(button.textContent).includes(query);if(!button.hidden)count++;});host.querySelector('.mc-navigo-foot').textContent=count+' partie'+(count>1?'s':'')+' affichée'+(count>1?'s':'');}
  function refresh(){
   if(!m.isConnected)return;
   const panel=m.querySelector('.mc-panel:not([hidden])');if(!panel)return;
   host.style.setProperty('--mc-font',m.style.getPropertyValue('--mc-font'));host.style.setProperty('--mc-scale',m.style.getPropertyValue('--mc-scale'));
   host.querySelector('.mc-navigo-title').textContent=m.querySelector('h1')?.textContent.trim()||'Cours';
   const tabs=host.querySelector('.mc-navigo-tabs');tabs.replaceChildren();
   m.querySelectorAll('.mc-tabs [data-p]').forEach(tab=>{const button=document.createElement('button');button.type='button';button.textContent=tab.textContent;button.className=tab.getAttribute('aria-selected')==='true'?'is-active':'';button.setAttribute('aria-pressed',String(tab.getAttribute('aria-selected')==='true'));button.onclick=()=>tab.click();tabs.append(button);});
   list.replaceChildren();buttons=[];
   headings=Array.from(panel.querySelectorAll('.mc-ilot h2,.mc-ilot h3,.mc-ilot h4,.mc-sci:not([hidden])>h2')).filter(heading=>!heading.closest('.mc-sci[hidden]'));
   headings.forEach(heading=>{const button=document.createElement('button');button.type='button';button.className='mc-navigo-item mc-navigo-'+heading.tagName.toLowerCase();button.textContent=MC_navLabel(heading);button.onclick=()=>{buttons.forEach(item=>item.removeAttribute('aria-current'));button.setAttribute('aria-current','location');open(false,false);move(heading);};list.append(button);buttons.push(button);});filter();
  }
  trigger.onclick=()=>{refresh();open(drawer.hidden);};host.querySelector('.mc-navigo-close').onclick=()=>open(false);search.oninput=filter;
  const onKey=event=>{if(event.key==='Escape'&&!desktop.matches&&!drawer.hidden){event.preventDefault();open(false);}};
  const outside=event=>{if(!desktop.matches&&!drawer.hidden&&!host.contains(event.target))open(false,false);};
  const resize=()=>open(false,false);
  document.addEventListener('keydown',onKey);document.addEventListener('pointerdown',outside);desktop.addEventListener('change',resize);
  const observer=new MutationObserver(()=>{if(!m.isConnected)MC_navigoDestroy();});observer.observe(document.getElementById('content'),{childList:true});
  MC_NAV_CLEANUP=()=>{observer.disconnect();desktop.removeEventListener('change',resize);document.removeEventListener('keydown',onKey);document.removeEventListener('pointerdown',outside);host.remove();};
  open(desktop.matches,false);return refresh;
 };
 // FLIP transition between views: cards and side entries glide to their new place and a
 // changed number rolls in. Positions are measured relative to their own container, so the
 // scroll reset of render() does not distort them. Reduced motion: no animation at all.
 const motionAllowed = () => typeof Element.prototype.animate === 'function' && !matchMedia('(prefers-reduced-motion: reduce)').matches;
 const flipEasing = 'cubic-bezier(.2,.7,.2,1)', flipDuration = 200, rankDuration = 220;
 const offset = (element, origin) => {const a = element.getBoundingClientRect(), b = origin.getBoundingClientRect(); return {x:a.left - b.left, y:a.top - b.top};};
 const flipGroups = () => [['cards', document.querySelector('#content .mcg-category-grid'), '[data-mcg-category]', 'mcgCategory'], ['side', document.getElementById('spec-nav'), '[data-mcg-sidebar-category]', 'mcgSidebarCategory']]
  .filter(([, container]) => container && container.getClientRects().length);
 let shownRanks = null;
 function layoutSnapshot() {
  return new Map(flipGroups().map(([group, container, selector, key]) => [group, new Map([...container.querySelectorAll(selector)].map(item => [item.dataset[key], offset(item, container)]))]));
 }
 function playTransition(before, previousRanks) {
  flipGroups().forEach(([group, container, selector, key]) => {
   const previous = before.get(group);
   if (!previous?.size) return;
   const limit = Math.max(innerHeight, 600) * 1.5;
   container.querySelectorAll(selector).forEach(item => {
    const from = previous.get(item.dataset[key]), to = offset(item, container);
    if (from && Math.abs(from.y - to.y) <= limit) {
     const dx = from.x - to.x, dy = from.y - to.y;
     if (Math.abs(dx) >= 1 || Math.abs(dy) >= 1) item.animate([{translate:dx + 'px ' + dy + 'px'}, {translate:'0 0'}], {duration:flipDuration, easing:flipEasing});
    } else item.animate([{opacity:0, scale:'.96'}, {opacity:1, scale:'1'}], {duration:flipDuration, easing:flipEasing});
   });
  });
  document.querySelectorAll('#content [data-mcg-rank], #spec-nav [data-mcg-rank]').forEach(holder => {
   const code = holder.dataset.mcgCategory || holder.dataset.mcgBlock || holder.dataset.mcgSidebarCategory, from = previousRanks.get(code);
   const value = holder.querySelector('[data-mcg-rank-value]');
   if (!value || !from || String(from) === holder.dataset.mcgRank) return;
   value.dataset.mcgRankFrom = from;
   value.animate([{opacity:0, translate:'0 -.65em', scale:'1.3'}, {opacity:1, translate:'0 0', scale:'1'}], {duration:rankDuration, easing:flipEasing});
  });
 }
 const renderView = render;
 render = function() {
  const animate = shownRanks && motionAllowed(), before = animate ? layoutSnapshot() : null, previousRanks = shownRanks;
  renderView.apply(this, arguments);
  shownRanks = new Map(visibleBlocks().map(block => [block.code, displayRank(block)]));
  if (before) playTransition(before, previousRanks);
 };
 window.MEDINA_CATEGORY_ORGANISATION = O;
 render();
})();
