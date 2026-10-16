/* MEDINA — Navigo premium (15.10.2026).
   Ajoute au plan du cours, sans modifier ses boutons ni leur ordre :
   - parties (h2) dépliables : survol, focus clavier ou premier toucher déplient leurs sous-parties ;
     flèches droite/gauche déplient ou replient ; la recherche déplie tout ;
   - suivi de lecture : partie et titre courants mis en évidence, barre de progression douce.
   Le contenu des cours n'est jamais modifié. */
(() => {
 'use strict';
 const SELECTOR = '.mc-ilot h2,.mc-ilot h3,.mc-ilot h4,.mc-sci:not([hidden])>h2';
 const reduce = matchMedia('(prefers-reduced-motion: reduce)');
 let pointer = 'mouse', frame = 0;

 function headings() {
  const panel = document.querySelector('.mc .mc-panel:not([hidden])');
  if (!panel) return [];
  return Array.from(panel.querySelectorAll(SELECTOR)).filter(h => !h.closest('.mc-sci[hidden]'));
 }

 function enhance(host) {
  const list = host.querySelector('.mc-navigo-list');
  if (!list) return;
  const items = Array.from(list.querySelectorAll('.mc-navigo-item'));
  if (!items.length || items.every(item => item.dataset.mpSeen)) return;
  items.forEach(item => { item.dataset.mpSeen = '1'; });
  let part = -1, sub = 0;
  items.forEach(item => {
   if (item.classList.contains('mc-navigo-h2')) {
    part += 1; sub = 0;
    item.classList.add('mp-part'); item.dataset.mpPart = String(part);
   } else if (part >= 0) {
    item.classList.add('mp-sub'); item.dataset.mpParent = String(part); item.style.setProperty('--mp-i', String(Math.min(sub++, 3)));
   }
  });
  items.filter(item => item.classList.contains('mp-part')).forEach(item => {
   const has = items.some(other => other.dataset.mpParent === item.dataset.mpPart);
   if (has) { item.dataset.mpHasSub = ''; item.setAttribute('aria-expanded', 'false'); }
  });
  if (!host.querySelector('.mp-progress')) {
   const bar = document.createElement('div');
   bar.className = 'mp-reading';
   bar.innerHTML = '<span class="mp-progress-label" aria-live="off">Position de lecture : 0 %</span><div class="mp-progress" role="progressbar" aria-label="Position de lecture dans l’onglet" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0"><i></i></div>';
   list.before(bar);
  }
  if (!list.dataset.mpBound) bind(host, list);
  host.mpState = host.mpState || {hover: null, focus: null, pinned: new Set(), active: null};
  apply(host);
  track();
 }

 function apply(host) {
  const list = host.querySelector('.mc-navigo-list'), state = host.mpState;
  if (!list || !state) return;
  const search = host.querySelector('.mc-navigo-search');
  const searching = !!(search && search.value.trim());
  const open = new Set([state.hover, state.focus, state.active, ...state.pinned].filter(v => v !== null && v !== undefined).map(String));
  list.querySelectorAll('.mp-sub').forEach(item => item.classList.toggle('mp-collapsed', !searching && !open.has(item.dataset.mpParent)));
  list.querySelectorAll('.mp-part[data-mp-has-sub]').forEach(item => item.setAttribute('aria-expanded', String(searching || open.has(item.dataset.mpPart))));
  list.querySelectorAll('.mp-part').forEach(item => item.classList.toggle('mp-active-part', item.dataset.mpPart === String(state.active)));
 }

 function partOf(item) {
  if (!item) return null;
  return item.dataset.mpPart !== undefined ? item.dataset.mpPart : (item.dataset.mpParent !== undefined ? item.dataset.mpParent : null);
 }

 function bind(host, list) {
  list.dataset.mpBound = '1';
  const state = () => host.mpState;
  list.addEventListener('pointerover', event => {
   pointer = event.pointerType || 'mouse';
   if (pointer !== 'mouse') return;
   const part = partOf(event.target.closest('.mc-navigo-item'));
   if (part !== null && state().hover !== part) { state().hover = part; apply(host); }
  });
  list.addEventListener('pointerleave', () => { if (state().hover !== null) { state().hover = null; apply(host); } });
  list.addEventListener('pointerdown', event => { pointer = event.pointerType || 'mouse'; }, true);
  list.addEventListener('focusin', event => { const part = partOf(event.target.closest('.mc-navigo-item')); if (part !== null) { state().focus = part; apply(host); } });
  list.addEventListener('focusout', event => { if (!list.contains(event.relatedTarget)) { state().focus = null; apply(host); } });
  // Tactile : le premier toucher d'une partie repliée la déplie ; le second ouvre la partie.
  list.addEventListener('click', event => {
   const item = event.target.closest('.mp-part[data-mp-has-sub]');
   if (!item || pointer === 'mouse' || item.getAttribute('aria-expanded') === 'true') return;
   const search = host.querySelector('.mc-navigo-search');
   if (search && search.value.trim()) return;
   event.preventDefault(); event.stopPropagation();
   state().pinned = new Set([item.dataset.mpPart]); apply(host);
  }, true);
  list.addEventListener('keydown', event => {
   const item = event.target.closest('.mc-navigo-item');
   if (!item) return;
   const part = partOf(item);
   if (event.key === 'ArrowRight' && item.dataset.mpHasSub !== undefined) { event.preventDefault(); state().pinned.add(part); apply(host); const next = item.nextElementSibling; if (next && next.dataset.mpParent === part) next.focus(); }
   else if (event.key === 'ArrowLeft' && part !== null) { event.preventDefault(); state().pinned.delete(part); const head = list.querySelector('.mp-part[data-mp-part="' + part + '"]'); if (head) head.focus(); apply(host); }
   else if (event.key === 'ArrowDown' || event.key === 'ArrowUp') {
    const visible = Array.from(list.querySelectorAll('.mc-navigo-item')).filter(b => !b.hidden && !b.classList.contains('mp-collapsed'));
    const i = visible.indexOf(item), next = visible[i + (event.key === 'ArrowDown' ? 1 : -1)];
    if (next) { event.preventDefault(); next.focus(); }
   }
  });
  const search = host.querySelector('.mc-navigo-search');
  if (search) search.addEventListener('input', () => apply(host));
 }

 function progressOf(mc) {
  const book = mc.classList.contains('book');
  const body = book && mc.querySelector('.mc-panel:not([hidden]) .mc-body');
  if (body && body.scrollWidth > body.clientWidth + 2) return body.scrollLeft / Math.max(1, body.scrollWidth - body.clientWidth);
  const panel = mc.querySelector('.mc-panel:not([hidden])') || mc;
  const rect = panel.getBoundingClientRect(), span = rect.height - innerHeight * .6;
  return Math.min(1, Math.max(0, (innerHeight * .3 - rect.top) / Math.max(1, span)));
 }

 function update() {
  frame = 0;
  const host = document.querySelector('.mc-navigo'), mc = document.querySelector('.mc');
  if (!host || !mc || !host.mpState) return;
  const list = host.querySelector('.mc-navigo-list');
  const items = Array.from(list.querySelectorAll('.mc-navigo-item')), hs = headings();
  if (!items.length || items.length !== hs.length) return;
  const bar = document.querySelector('.topbar');
  const limit = (bar ? bar.getBoundingClientRect().bottom : 0) + 28;
  let current = -1;
  hs.forEach((h, i) => { const r = h.getBoundingClientRect(); if (r.width && r.top <= limit && r.left < innerWidth && r.right > 0) current = i; });
  if (current < 0) current = 0;
  const item = items[current];
  if (!item.hasAttribute('aria-current')) {
   items.forEach(b => b.removeAttribute('aria-current'));
   item.setAttribute('aria-current', 'location');
   const listRect = list.getBoundingClientRect(), r = item.getBoundingClientRect();
   if (!host.matches(':hover') && (r.top < listRect.top || r.bottom > listRect.bottom)) list.scrollTo({top: list.scrollTop + r.top - listRect.top - listRect.height / 3, behavior: reduce.matches ? 'auto' : 'smooth'});
  }
  const part = partOf(item);
  if (host.mpState.active !== part) { host.mpState.active = part; apply(host); }
  const value = Math.round(progressOf(mc) * 100);
  const progress = host.querySelector('.mp-progress');
  if (progress && progress.getAttribute('aria-valuenow') !== String(value)) {
   progress.setAttribute('aria-valuenow', String(value));
   progress.style.setProperty('--mp-read', String(value / 100));
   const label = host.querySelector('.mp-progress-label');
   if (label) label.textContent = 'Position de lecture : ' + value + ' %';
  }
 }

 function track() { if (!frame) frame = requestAnimationFrame(update); }

 const observer = new MutationObserver(() => {
  const host = document.querySelector('.mc-navigo');
  if (host) enhance(host);
 });
 function centre() {
  const list = document.querySelector('.mc-navigo .mc-navigo-list'), current = list && list.querySelector('[aria-current]');
  if (!current) return;
  const box = list.getBoundingClientRect(), r = current.getBoundingClientRect();
  list.scrollTop += r.top - box.top - (list.clientHeight - r.height) / 2;
 }
 document.addEventListener('click', event => { if (event.target.closest('.mc-navigo-trigger')) { setTimeout(update, 60); setTimeout(centre, reduce.matches ? 80 : 320); } });
 function start() {
  observer.observe(document.body, {childList: true, subtree: true});
  addEventListener('scroll', track, {passive: true, capture: true});
  addEventListener('resize', track, {passive: true});
  const host = document.querySelector('.mc-navigo');
  if (host) enhance(host);
 }
 if (document.body) start(); else document.addEventListener('DOMContentLoaded', start);
})();
