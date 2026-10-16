/* MEDINA — Navigo premium : prise de relais dans les fragments (16.10.2026).
   Le plan de la leçon est désormais entièrement porté par engine/medina_course.js
   (window.MC_NAVIGO_PREMIUM : arbre ARIA, recherche, suivi de lecture, épinglage, ancre d'URL).
   Les couches de fragment antérieures (engine/category_organisation.js, shell/fragment.js)
   redéfinissent MC_navigoMount avant ce script, injecté en dernier : il rétablit le Navigo
   premium et remplace, s'il est déjà monté, l'ancien plan de la leçon ouverte.
   Le contenu des cours n'est jamais modifié. */
(() => {
 'use strict';
 const premium = window.MC_NAVIGO_PREMIUM;
 if (typeof premium !== 'function' || typeof MC_navigoMount !== 'function') return;
 if (MC_navigoMount !== premium) MC_navigoMount = premium;
 const course = document.querySelector('.mc');
 if (course && !document.querySelector('.mc-navigo[data-navigo="2"]')) {
  MC_navigoDestroy();
  premium(course);
 }
})();
