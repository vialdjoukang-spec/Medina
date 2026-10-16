/* MEDINA — encre de lecture des cours (Vial, 16.10.2026).
   Ajoute « Encre : Noir | Bleu » à côté de « Police / Police Taille » dans la barre d’outils de chaque leçon.
   Le choix est porté par html[data-medina-encre] ; engine/couleurs_premium.css en déduit --ink-cours
   (Noir #111111 ou Bleu marine, ≥ 12:1 sur le blanc immaculé des cours). Mémorisé dans localStorage
   (try/catch : navigation privée, stockage bloqué) ; la page reste correcte sans stockage. */
(function () {
  'use strict';
  var CLE = 'medina.encre', DEFAUT = 'noir', ENCRES = { noir: 'Noir', bleu: 'Bleu' };
  var racine = document.documentElement;

  function lire() {
    try { var v = window.localStorage.getItem(CLE); return ENCRES[v] ? v : DEFAUT; } catch (e) { return DEFAUT; }
  }
  function ecrire(v) {
    try { window.localStorage.setItem(CLE, v); } catch (e) { /* stockage indisponible : choix limité à la page */ }
  }
  function synchroniser(v) {
    var boutons = document.querySelectorAll('.mc-encre button[data-encre]');
    for (var i = 0; i < boutons.length; i++) {
      boutons[i].setAttribute('aria-pressed', String(boutons[i].getAttribute('data-encre') === v));
    }
  }
  function appliquer(v, memoriser) {
    if (!ENCRES[v]) v = DEFAUT;
    racine.setAttribute('data-medina-encre', v);
    if (memoriser) ecrire(v);
    synchroniser(v);
  }

  function controle() {
    var groupe = document.createElement('div');
    groupe.className = 'mc-encre';
    groupe.setAttribute('role', 'group');
    groupe.setAttribute('aria-label', 'Encre du texte du cours');
    var lib = document.createElement('span');
    lib.className = 'mc-encre-l';
    lib.setAttribute('aria-hidden', 'true');
    lib.textContent = 'Encre :';
    groupe.appendChild(lib);
    Object.keys(ENCRES).forEach(function (v) {
      var b = document.createElement('button');
      b.type = 'button';
      b.setAttribute('data-encre', v);
      b.setAttribute('aria-pressed', String(racine.getAttribute('data-medina-encre') === v));
      b.title = 'Texte principal du cours en ' + ENCRES[v].toLowerCase();
      var p = document.createElement('i');
      p.className = 'mc-encre-pastille';
      p.setAttribute('aria-hidden', 'true');
      b.appendChild(p);
      b.appendChild(document.createTextNode(ENCRES[v]));
      b.addEventListener('click', function () { appliquer(v, true); });
      groupe.appendChild(b);
    });
    return groupe;
  }

  function equiper() {
    var barres = document.querySelectorAll('.mc-toolbar:not([data-mc-encre])');
    for (var i = 0; i < barres.length; i++) {
      var barre = barres[i];
      barre.setAttribute('data-mc-encre', '1');
      var apres = barre.querySelector('.mc-size-wrap') || barre.querySelector('.mc-font');
      var c = controle();
      if (apres && apres.closest('label') && !apres.classList.contains('mc-size-wrap')) apres = apres.closest('label');
      if (apres && apres.parentNode === barre) barre.insertBefore(c, apres.nextSibling);
      else barre.appendChild(c);
    }
  }

  appliquer(lire(), false);
  var prevu = false;
  function planifier() {
    if (prevu) return;
    prevu = true;
    (window.requestAnimationFrame || setTimeout)(function () { prevu = false; equiper(); });
  }
  function demarrer() {
    equiper();
    new MutationObserver(planifier).observe(document.body, { childList: true, subtree: true });
  }
  if (document.body) demarrer(); else document.addEventListener('DOMContentLoaded', demarrer);
  window.addEventListener('storage', function (e) { if (e.key === CLE) appliquer(e.newValue, false); });
})();
