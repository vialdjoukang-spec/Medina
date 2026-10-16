/* MEDINA — sélecteur de thème de lecture (16.10.2026).
   Injecté dans <head>, juste après engine/themes_medina.css : le thème mémorisé est posé sur
   <html data-medina-theme="…"> avant le premier rendu (aucun flash). Le bouton « Thème » est
   ajouté ensuite dans la barre supérieure (fragments : .top-actions ; portail : nav de l'en-tête).
   Mémoire : localStorage « medina.theme » (try/catch), partagée par le portail et les fragments ;
   un changement dans un autre onglet est appliqué à la volée (événement storage).
   Le contenu des cours n'est jamais modifié. */
(() => {
 'use strict';
 const KEY = 'medina.theme', DEF = 'defaut';
 const CATALOGUE = /* <catalogue> */[{"id": "geo-rouge", "famille": "geo", "nom": "Rouge · losanges", "motif": "losanges"}, {"id": "geo-orange", "famille": "geo", "nom": "Orange · cercles concentriques", "motif": "cercles"}, {"id": "geo-jaune", "famille": "geo", "nom": "Jaune · hexagones", "motif": "hexagones"}, {"id": "geo-vert", "famille": "geo", "nom": "Vert · triangles", "motif": "triangles"}, {"id": "geo-cyan", "famille": "geo", "nom": "Cyan · ondes", "motif": "ondes"}, {"id": "geo-bleu", "famille": "geo", "nom": "Bleu · grille fine", "motif": "grille"}, {"id": "geo-violet", "famille": "geo", "nom": "Violet · chevrons", "motif": "chevrons"}, {"id": "geo-magenta", "famille": "geo", "nom": "Magenta · points", "motif": "points"}, {"id": "multi-vitrail", "famille": "multi", "nom": "Vitrail", "humeur": "Rubis, saphir, émeraude, ambre et améthyste : la lumière d’un vitrail, pièce par pièce."}, {"id": "multi-bauhaus", "famille": "multi", "nom": "Bauhaus", "humeur": "Les trois primaires de l’atelier : bleu, jaune et rouge, posés en aplats francs."}, {"id": "multi-mineral", "famille": "multi", "nom": "Minéral", "humeur": "Glacier, argile, ardoise, lichen et quartz rose : la palette d’un éboulis alpin."}, {"id": "multi-aurore", "famille": "multi", "nom": "Aurore boréale", "humeur": "Vert, violet, cyan, magenta et bleu : le voile d’une aurore qui glisse d’une teinte à l’autre."}, {"id": "multi-agrumes", "famille": "multi", "nom": "Agrumes et lagon", "humeur": "Orange, menthe, corail, lagon et citron vert : un marché d’été au bord de l’eau."}]/* </catalogue> */;
 const root = document.documentElement;
 const ids = new Set(CATALOGUE.map(t => t.id));
 let current = DEF, defaults = null, built = null, frame = 0;

 function read() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }
 function write(id) {
  try { if (id === DEF) localStorage.removeItem(KEY); else localStorage.setItem(KEY, id); } catch (e) { /* stockage indisponible : choix limité à la page */ }
 }
 function apply(id) {
  current = ids.has(id) ? id : DEF;
  if (current === DEF) root.removeAttribute('data-medina-theme');
  else root.setAttribute('data-medina-theme', current);
  if (built) built.swatches.forEach(s => s.setAttribute('aria-pressed', String(s.dataset.mthSwatch === current)));
 }
 apply(read());

 // Valeurs du thème par défaut, lues sans attribut, pour l'aperçu « Par défaut ».
 const PROBE = ['--n-paper', '--n-surface', '--n-line', '--n-line-soft', '--accent', '--accent-ink', '--ink-1'];
 function captureDefaults() {
  if (defaults) return defaults;
  const had = root.getAttribute('data-medina-theme');
  if (had) root.removeAttribute('data-medina-theme');
  const cs = getComputedStyle(root);
  defaults = {};
  PROBE.forEach(p => { defaults[p] = cs.getPropertyValue(p).trim(); });
  if (had) root.setAttribute('data-medina-theme', had);
  return defaults;
 }

 const SVG = 'http://www.w3.org/2000/svg';
 function el(tag, attrs, text) {
  const node = document.createElement(tag);
  if (attrs) Object.entries(attrs).forEach(([k, v]) => node.setAttribute(k, v));
  if (text) node.textContent = text;
  return node;
 }
 function icon(markup, cls) {
  const s = document.createElementNS(SVG, 'svg');
  s.setAttribute('viewBox', '0 0 24 24'); s.setAttribute('aria-hidden', 'true'); s.setAttribute('focusable', 'false');
  if (cls) s.setAttribute('class', cls);
  s.innerHTML = markup;
  return s;
 }
 const PALETTE = '<path d="M12 3a9 9 0 1 0 0 18c1.2 0 1.8-.8 1.8-1.7 0-.5-.2-.9-.5-1.3-.3-.3-.5-.7-.5-1.2 0-1 .8-1.8 1.8-1.8H17a4 4 0 0 0 4-4C21 6.6 17 3 12 3Z" fill="none" stroke="currentColor" stroke-width="1.6"/>'
  + '<circle class="mth-btn-dot" cx="7.5" cy="11" r="1.5"/><circle cx="10.5" cy="7" r="1.5" fill="currentColor"/><circle cx="15.5" cy="7.5" r="1.5" fill="currentColor"/>';
 const CHECK = '<path d="M5 12.5 10 17l9-10" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>';

 function swatch(id, name) {
  const b = el('button', { type: 'button', class: 'mth-swatch', 'data-mth-swatch': id, 'aria-pressed': String(id === current) });
  const prev = el('span', { class: 'mth-prev', 'aria-hidden': 'true' });
  prev.append(el('span', { class: 'mth-prev-bar' }), el('span', { class: 'mth-prev-card' }), el('span', { class: 'mth-prev-card' }));
  const label = el('span', { class: 'mth-name' });
  label.append(el('span', null, name), icon(CHECK));
  b.append(prev, label);
  if (id === DEF) {
   const d = captureDefaults();
   Object.entries(d).forEach(([k, v]) => { if (v) b.style.setProperty(k, v); });
   b.style.setProperty('--mth-page', 'none');
  }
  return b;
 }

 function group(title, note, items) {
  const box = el('div', { class: 'mth-group', role: 'group' });
  const h = el('p', { class: 'mth-group-title', id: 'mth-g-' + Math.random().toString(36).slice(2, 8) }, title);
  box.setAttribute('aria-labelledby', h.id);
  const grid = el('div', { class: 'mth-grid' });
  items.forEach(([id, name]) => grid.append(swatch(id, name)));
  box.append(h);
  if (note) box.append(el('p', { class: 'mth-group-note' }, note));
  box.append(grid);
  return box;
 }

 function build(host, before) {
  const wrap = el('div', { class: 'mth-root' });
  const btn = el('button', { type: 'button', class: 'mth-btn', id: 'mth-btn', 'aria-haspopup': 'dialog', 'aria-expanded': 'false', 'aria-controls': 'mth-panel', title: 'Choisir un thème de lecture' });
  btn.append(icon(PALETTE), el('span', { class: 'mth-btn-label' }, 'Thème'));
  const panel = el('div', { class: 'mth-panel', id: 'mth-panel', role: 'dialog', 'aria-modal': 'false', 'aria-labelledby': 'mth-title', hidden: '' });
  const head = el('div', { class: 'mth-head' });
  const copy = el('div');
  copy.append(el('p', { class: 'mth-title', id: 'mth-title' }, 'Thème de lecture'),
   el('p', { class: 'mth-note' }, 'Le choix est mémorisé sur cet appareil, pour l’accueil et toutes les spécialités. Les cours ne changent pas.'));
  const close = el('button', { type: 'button', class: 'mth-close', 'aria-label': 'Fermer le choix du thème' }, '×');
  head.append(copy, close);
  const geo = CATALOGUE.filter(t => t.famille === 'geo').map(t => [t.id, t.nom]);
  const multi = CATALOGUE.filter(t => t.famille === 'multi').map(t => [t.id, t.nom]);
  const live = el('p', { class: 'mth-live', role: 'status', 'aria-live': 'polite' });
  panel.append(head,
   group('Thème actuel', null, [[DEF, 'Par défaut']]),
   group('Géométrique pâle', 'Un fond extrêmement pâle de la couleur, un motif géométrique discret ; les cartes restent claires.', geo),
   group('Multicolore iconique', 'Une teinte par région ; à chaque frontière, une couleur s’efface là où l’autre naît.', multi),
   live);
  wrap.append(btn, panel);
  if (before && before.parentNode === host) host.insertBefore(wrap, before); else host.append(wrap);
  const swatches = Array.from(panel.querySelectorAll('.mth-swatch'));
  built = { wrap, btn, panel, swatches, live };

  function open() {
   panel.hidden = false; panel.classList.add('is-entering');
   requestAnimationFrame(() => requestAnimationFrame(() => panel.classList.remove('is-entering')));
   btn.setAttribute('aria-expanded', 'true');
   (swatches.find(s => s.getAttribute('aria-pressed') === 'true') || swatches[0]).focus();
  }
  function shut(focusButton) {
   if (panel.hidden) return;
   panel.hidden = true; btn.setAttribute('aria-expanded', 'false');
   if (focusButton) btn.focus();
  }
  btn.addEventListener('click', () => (panel.hidden ? open() : shut(false)));
  close.addEventListener('click', () => shut(true));
  panel.addEventListener('click', event => {
   const s = event.target.closest('.mth-swatch');
   if (!s) return;
   apply(s.dataset.mthSwatch); write(current);
   live.textContent = 'Thème « ' + s.querySelector('.mth-name span').textContent + ' » appliqué.';
  });
  wrap.addEventListener('keydown', event => {
   if (event.key === 'Escape' && !panel.hidden) { event.preventDefault(); event.stopPropagation(); shut(true); return; }
   const i = swatches.indexOf(document.activeElement);
   if (i < 0) return;
   const step = { ArrowRight: 1, ArrowDown: 1, ArrowLeft: -1, ArrowUp: -1 }[event.key];
   let j = null;
   if (step) j = (i + step + swatches.length) % swatches.length;
   if (event.key === 'Home') j = 0;
   if (event.key === 'End') j = swatches.length - 1;
   if (j !== null) { event.preventDefault(); swatches[j].focus(); }
  });
  wrap.addEventListener('focusout', event => { if (!panel.hidden && event.relatedTarget && !wrap.contains(event.relatedTarget)) shut(false); });
  document.addEventListener('pointerdown', event => { if (!panel.hidden && !wrap.contains(event.target)) shut(false); });
 }

 function mount() {
  if (document.getElementById('mth-btn')) return;
  // Fragments : enfant direct de la barre, juste avant .top-actions (masqué sous 700 px) ; une 4e colonne lui est réservée en mobile.
  const bar = document.querySelector('.topbar');
  if (bar) { build(bar, bar.querySelector(':scope > .top-actions')); return; }
  const nav = document.querySelector('.masthead nav');
  if (nav) build(nav, null);
 }

 // Fondu des cartes : chaque carte reçoit la teinte de la suivante (--mth-next).
 function tagCards() {
  frame = 0;
  document.querySelectorAll('.mcg-category-grid,.specialties').forEach(grid => {
   const cards = Array.from(grid.children).filter(c => c.matches('.mcg-category-card,.specialty-card'));
   const sig = cards.length + ':' + (cards[0] ? cards[0].getAttribute('data-mcg-category') || cards[0].getAttribute('data-fragment-id') || '' : '');
   if (cards.length < 2 || grid.dataset.mthTagged === sig) return;
   const hues = cards.map(c => getComputedStyle(c).getPropertyValue(c.classList.contains('specialty-card') ? '--card-accent' : '--mp-cat').trim());
   cards.forEach((c, k) => { const next = hues[(k + 1) % cards.length]; if (next) c.style.setProperty('--mth-next', next); });
   grid.dataset.mthTagged = sig;
  });
 }
 function schedule() { if (!frame) frame = requestAnimationFrame(tagCards); }

 function ready() {
  mount(); schedule();
  if (document.body) new MutationObserver(() => { schedule(); if (!document.getElementById('mth-btn')) mount(); }).observe(document.body, { childList: true, subtree: true });
 }
 if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', ready, { once: true }); else ready();
 window.addEventListener('storage', event => { if (event.key === KEY) apply(event.newValue); });
 window.MEDINA_THEMES = { list: () => [DEF].concat(CATALOGUE.map(t => t.id)), get: () => current, set: id => { apply(id); write(current); } };
})();
