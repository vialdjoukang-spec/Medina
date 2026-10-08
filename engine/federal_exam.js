/* MEDINA — bouton « Isolate Federal – CH Exam » : les catégories restent ; les chapitres de pratique quotidienne et d'examen fédéral passent en poudre d'or. */
(() => {
 'use strict';
 const node = document.getElementById('medina-federal-data');
 if (!node) return;
 const F = JSON.parse(node.textContent), codes = new Set(Object.keys(F.codes || {}));
 const key = 'medina.fragment.' + F.fragment + '.federal';
 const read = () => {try {return localStorage.getItem(key) === '1';} catch (e) {return false;}};
 const write = on => {try {localStorage.setItem(key, on ? '1' : '0');} catch (e) {}};
 let golden = new Set(), byCategory = new Map();
 function index() {
  const O = window.MEDINA_CATEGORY_ORGANISATION; golden = new Set(); byCategory = new Map();
  if (!O) return;
  for (const block of O.blocks) {
   let n = 0;
   for (const lesson of block.lessons) {
    const covered = [lesson.code].concat((lesson.covers || []).map(c => c.code));
    if (covered.some(c => codes.has(c))) {golden.add(lesson.code); n++;}
   }
   byCategory.set(block.code, n);
  }
 }
 function paint() {
  if (!golden.size) index();
  document.querySelectorAll('[data-mcg-lesson],a.mcg-sidebar-lesson').forEach(el => {
   const code = el.dataset.mcgLesson || el.dataset.mcgSidebarLesson || el.dataset.fragmentChapter || (el.getAttribute('href') || '').match(/[A-Z][0-9]{2}/)?.[0];
   const on = golden.has(code);
   if (el.classList.contains('mfx-gold') !== on) el.classList.toggle('mfx-gold', on);
  });
  document.querySelectorAll('[data-mcg-category]').forEach(el => {
   const n = byCategory.get(el.dataset.mcgCategory) || 0;
   if (n && !el.querySelector('.mfx-count')) (el.querySelector('h2') || el).insertAdjacentHTML('beforeend', '<span class="mfx-count" title="Chapitres d’examen fédéral">★ ' + n + '</span>');
  });
 }
 function set(on) {
  document.documentElement.classList.toggle('medina-federal-on', on);
  const b = document.getElementById('medina-federal-toggle');
  if (b) {b.setAttribute('aria-pressed', String(on)); b.title = on ? 'Revenir à l’affichage normal' : 'Mettre en surbrillance les chapitres de pratique quotidienne et d’examen fédéral';}
  write(on); paint();
 }
 const topbar = document.querySelector('.topbar');
 if (topbar && !document.getElementById('medina-federal-toggle')) {
  topbar.insertAdjacentHTML('beforeend', '<button type="button" id="medina-federal-toggle" aria-pressed="false"><span class="mfx-star" aria-hidden="true">★</span><span>Isolate Federal<span class="mfx-label-long"> – CH Exam</span></span></button>');
  document.getElementById('medina-federal-toggle').addEventListener('click', () => set(!document.documentElement.classList.contains('medina-federal-on')));
 }
 let queued = false;
 new MutationObserver(() => {if (!queued) {queued = true; requestAnimationFrame(() => {queued = false; paint();});}}).observe(document.body, {childList: true, subtree: true});
 set(read());
})();
