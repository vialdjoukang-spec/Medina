/* ===== MEDINA — couche d'embellissement et modules ===== */
(()=>{const P=document.createElement('div');P.id='mdn-progress';document.body.appendChild(P);
const c=document.getElementById('content');if(c)new MutationObserver(m=>{if(m.some(x=>x.target===c)){c.classList.remove('mdn-enter');void c.offsetWidth;c.classList.add('mdn-enter')}}).observe(c,{childList:true});
const D=window.MDN_DATA||{},ECG=window.MDN_ECG||[];const esc=s=>String(s??'').replace(/[&<>"']/g,x=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[x]));
/* insignes des systèmes achevés */
function sysBadges(){(D.doneNames||[]).forEach(n=>{document.querySelectorAll('#content a,#content h1,#content h2,#content h3,.sidebar a').forEach(el=>{if(el.querySelector('.fluo'))return;const t=(el.childNodes[0]&&el.childNodes[0].textContent||el.textContent).trim();if(t===n||el.textContent.trim()===n){el.insertAdjacentHTML('beforeend','<span class="fluo">100 % rédigé</span>')}})})}
/* atlas ECG */
const CAT=D.ecgCat||{};let dlg=null;
function openECG(f){f=f||'Tous';if(!dlg){dlg=document.createElement('dialog');dlg.className='mdn-ecg';document.body.appendChild(dlg);dlg.addEventListener('click',e=>{if(e.target===dlg)dlg.close()})}
 const cats=['Tous','Rythme','Conduction','Ischémie et repolarisation','Arythmies ventriculaires'];const L=ECG.filter(x=>f==='Tous'||CAT[x.k]===f);
 dlg.innerHTML=`<header><h2>Atlas ECG</h2><button type="button" data-x>Fermer ✕</button></header><div class="scale"><b>Lecture du papier</b> : 25 mm/s et 10 mm/mV. Petit carré = 40 ms et 0,1 mV ; grand carré = 200 ms et 0,5 mV. Fréquence ≈ 300 / nombre de grands carrés entre deux QRS. Tracés schématiques ; dérivation indiquée.</div><div class="chips">${cats.map(x=>`<button type="button" data-f="${x}" aria-pressed="${x===f}">${x}</button>`).join('')}</div><div class="grid">${L.map(x=>`<article><h3>${esc(x.t)}</h3><small>Dérivation ${esc(x.lead)}</small><div class="sv">${x.svg}</div><ul>${x.crit.map(c=>`<li>${c}</li>`).join('')}</ul>${(window.MEDINA_ALIAS||{})[x.course]?`<p><a href="#/entry/${x.course}" data-close>Cours ${x.course} →</a></p>`:''}</article>`).join('')}</div>`;
 dlg.querySelector('[data-x]').onclick=()=>dlg.close();dlg.querySelectorAll('[data-f]').forEach(b=>b.onclick=()=>openECG(b.dataset.f));dlg.querySelectorAll('[data-close]').forEach(a=>a.onclick=()=>dlg.close());
 if(!dlg.open)dlg.showModal();dlg.scrollTop=0}
window.MDN_openECG=openECG;
function ecgButton(){const tb=document.querySelector('.top-actions');if(tb&&!tb.querySelector('.mdn-ecgbtn')){const b=document.createElement('button');b.className='mdn-ecgbtn';b.type='button';b.innerHTML='<svg viewBox="0 0 24 24"><path d="M3 12h4l2-6 4 12 2-6h6"/></svg>Atlas ECG';b.onclick=()=>openECG();tb.prepend(b)}
 const nm=document.querySelector('.sidebar .nav-main');if(nm&&!nm.querySelector('.mdn-ecglink')){const a=document.createElement('a');a.href='javascript:void 0';a.className='mdn-ecglink';a.innerHTML='<svg class="icon" viewBox="0 0 24 24"><path d="M3 12h4l2-6 4 12 2-6h6"/></svg><span>Atlas ECG</span>';a.onclick=e=>{e.preventDefault();openECG()};nm.appendChild(a)}}
/* À l'accueil, un directeur relie les systèmes réellement rédigés à leur parcours. */
function director(){
 if(typeof readRoute!=='function'||readRoute().type!=='home')return;
 const home=document.querySelector('#content .hero');
 if(!home||document.querySelector('#content .mdn-director'))return;
 const systems=(D.systems||[]).filter(s=>(s.courses||[]).length);if(!systems.length)return;
 const ongoing=systems.filter(s=>!s.done).length;
 const cards=systems.map(s=>{
  const first=s.courses?.[0],e=first&&typeof EM!=='undefined'?EM[first.code]:null;
  const href=e?url('specialty',e.primary,{system:e.organ}):first?url('entry',first.code):'#/home';
  const pct=Math.round(100*s.covered/Math.max(1,s.total));
  return `<article class="mdn-director-card ${s.done?'is-done':''}">
   <a class="mdn-director-system" href="${h(href)}" aria-label="Ouvrir ${esc(s.title)}, ${pct} % des catégories couvertes">
    <span class="mdn-director-top"><span class="mdn-director-index">${String(s.n).padStart(2,'0')}</span><span class="mdn-director-state">${s.done?'Rédaction achevée':'En cours'}</span></span>
    <strong>${esc(s.title)}</strong>
    <span class="mdn-director-measure"><span>${s.covered} / ${s.total} catégories couvertes</span><b>${pct} %</b></span>
    <span class="mdn-director-track" role="progressbar" aria-label="Couverture rédactionnelle de ${esc(s.title)}" aria-valuemin="0" aria-valuemax="100" aria-valuenow="${pct}"><i style="width:${pct}%"></i></span>
    <span class="mdn-director-open">Ouvrir le système <span aria-hidden="true">↗</span></span>
   </a><div class="mdn-director-courses" aria-label="Cours intégrés à ${esc(s.title)}">${(s.courses||[]).map(c=>`<a href="${h(url('entry',c.code))}" title="${esc(c.title)}${c.complete?' · 100 % rédigé':' · en révision'}"${c.complete?' class="is-complete"':''}>${esc(c.code)}</a>`).join('')}<button type="button" class="mdn-director-plan" data-n="${s.n}">Plan de rédaction</button></div>
  </article>`;
 }).join('');
 const box=document.createElement('details');box.className='mdn-director';
 box.innerHTML=`<summary><span class="mdn-director-symbol" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="m14.8 9.2-2 5.6-3.6 1.2 2-5.6z"/></svg></span><span class="mdn-director-heading"><strong>Directeur des systèmes</strong><small>${systems.length} systèmes accessibles · ${ongoing} en cours de rédaction</small></span><span class="mdn-director-action">Explorer <span aria-hidden="true">⌄</span></span></summary><div class="mdn-director-body"><p>Progression = catégories couvertes par les cours et renvois éditoriaux ; une jauge à 100 % ne vaut pas validation clinique.</p><div class="mdn-director-grid">${cards}</div></div>`;
 home.insertAdjacentElement('afterend',box);
 box.querySelectorAll('.mdn-director-plan').forEach(b=>b.onclick=()=>window.MDN_openSystems&&window.MDN_openSystems(b.dataset.n));
}
/* notification des nouveaux cours */
function toast(){const N=(D.news||[]);if(!N.length)return;let seen=null;try{seen=localStorage.getItem('medina.seen')}catch(e){}if(seen===D.build)return;
 const t=document.createElement('div');t.className='mdn-toast';t.setAttribute('role','status');t.innerHTML=`<h3>Nouveaux cours livrés</h3><ul>${N.map(c=>`<li><a href="#/entry/${c.code}">${esc(c.code)} · ${esc(c.title)}</a>${c.complete?' <span class="fluo">100 % rédigé</span>':' <span class="mc-badge-draft">en révision</span>'}</li>`).join('')}</ul><button type="button">Fermer</button>`;
 document.body.appendChild(t);requestAnimationFrame(()=>t.classList.add('on'));const close=()=>{t.classList.remove('on');setTimeout(()=>t.remove(),400);try{localStorage.setItem('medina.seen',D.build)}catch(e){}};t.querySelector('button').onclick=close;t.querySelectorAll('a').forEach(a=>a.addEventListener('click',close))}
const run=()=>{sysBadges();ecgButton();director()};let tm=null;new MutationObserver(()=>{clearTimeout(tm);tm=setTimeout(run,80)}).observe(document.body,{childList:true,subtree:true});
setTimeout(run,300);setTimeout(toast,1200);})();
/* ===== Bouton directeur de l'accueil : systèmes en cours, jauges, ouverture du système ===== */
(()=>{const D=window.MDN_DATA||{};const S=D.systems||[];if(!S.length)return;
const esc=s=>String(s??'').replace(/[&<>"']/g,x=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[x]));
const norm=s=>String(s).toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'').replace(/[^a-z0-9 ]/g,' ');
let dlg=null;
function ring(p,cls=''){return `<span class="ring" style="--p:${p}"><b>${p} %</b></span>`}
function list(){const act=S.filter(s=>s.prio).sort((a,b)=>(b.pct>0)-(a.pct>0)||b.pct-a.pct);
 return `<div class="grid">${act.map(s=>`<button type="button" class="sc ${s.done?'done':''} ${s.pct?'':'off'}" data-n="${s.n}">${ring(s.pct)}<span><h3>${esc(s.t)}</h3><small>${s.ch.length} cours intégré${s.ch.length>1?'s':''} · ${s.done?'système achevé':s.pct?'en cours de création':'en préparation'}</small>${s.done?'<br><span class="fluo">100 % rédigé</span>':''}<span class="bar"><i style="width:${s.pct}%"></i></span></span></button>`).join('')}</div>`}
function detail(n){const s=S.find(x=>x.n==n);const done=s.ch.map(c=>c.title);
 const doneN=new Set(done.map(norm));
 const planned=s.plan.filter(p=>![...doneN].some(d=>d.includes(norm(p).split(' ')[0])&&norm(p).split(' ').some(w=>w.length>4&&d.includes(w))));
 return `<div class="detail"><button type="button" class="back">← Tous les systèmes</button><div class="big">${ring(s.pct)}<div><h3>${esc(s.t)}</h3><small>${s.cat} catégories CIM · ${s.ch.length} cours rédigés</small></div></div>
 <ol>${s.ch.map(c=>`<li><a href="#/entry/${c.code}" data-close>${esc(c.code)} · ${esc(c.title)}</a>${c.complete?'<span class="fluo">100 % rédigé</span>':'<span class="mc-badge-draft">en révision</span>'}</li>`).join('')}${planned.map(p=>`<li class="todo">${esc(p)}<span class="st">à rédiger</span></li>`).join('')}</ol></div>`}
function open(n){if(!dlg){dlg=document.createElement('dialog');dlg.className='mdn-sys';document.body.appendChild(dlg);dlg.addEventListener('click',e=>{if(e.target===dlg)dlg.close()})}
 const tot=S.filter(s=>s.prio);const cat=tot.reduce((a,s)=>a+s.cat,0),cov=tot.reduce((a,s)=>a+Math.round(s.cat*s.pct/100),0);
 dlg.innerHTML=`<header><div><h2>Systèmes en cours de création</h2><p>Examen fédéral · ${Math.round(100*cov/cat)} % des catégories prioritaires traitées</p></div><button type="button" data-x>Fermer ✕</button></header>${n?detail(n):list()}`;
 dlg.querySelector('[data-x]').onclick=()=>dlg.close();
 dlg.querySelectorAll('.sc').forEach(b=>b.onclick=()=>open(b.dataset.n));
 const bk=dlg.querySelector('.back');if(bk)bk.onclick=()=>open();
 dlg.querySelectorAll('[data-close]').forEach(a=>a.onclick=()=>dlg.close());
 if(!dlg.open)dlg.showModal();dlg.scrollTop=0}
window.MDN_openSystems=open;
const btn=document.createElement('button');btn.type='button';btn.className='mdn-dir';btn.setAttribute('aria-label','Systèmes en cours de création');
btn.innerHTML='<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 12l4-6M7 16.5A6 6 0 0 1 17.5 9"/></svg><span class="lbl">Systèmes en cours</span>';btn.onclick=()=>open();
const isHome=()=>{const h=location.hash;return h===''||h==='#'||h==='#/'||/^#\/(home|accueil)?\/?$/.test(h)};
const sync=()=>{if(isHome()){if(!btn.isConnected)document.body.appendChild(btn)}else btn.remove()};
addEventListener('hashchange',sync);setTimeout(sync,200);})();
/* ===== MEDINA — modernisation du front-end (phase 2) : hauteur de la barre, mode sombre, messages, insignes ===== */
(()=>{const root=document.documentElement;
/* Hauteur réelle de la barre supérieure : sert aux onglets collants du cours et aux ancres. */
const top=document.querySelector('.topbar');const setTop=()=>{if(top)root.style.setProperty('--mdn-top',top.offsetHeight+'px')};setTop();
/* Hauteur des onglets du cours quand ils sont collants (0 sinon) : marge des ancres et du focus clavier. */
const setTabs=()=>{const m=document.querySelector('.mc'),t=m&&m.querySelector('.mc-tabs');if(t)m.classList.toggle('mdn-tabs-tall',t.offsetHeight>96);root.style.setProperty('--mdn-tabs',(t&&getComputedStyle(t).position==='sticky'?t.offsetHeight+8:0)+'px')};addEventListener('resize',setTabs);
/* À l'ouverture d'un cours, la coque repositionne la page à 200 px : la barre d'outils du cours est alors gardée sous la barre collante. */
(()=>{const f=window.scrollTo;window.scrollTo=function(a,b){const tb=document.querySelector('.mc .mc-toolbar');if(tb&&a===0&&b===200&&top){const y=scrollY+tb.getBoundingClientRect().top-top.offsetHeight-8;return f.call(window,{top:Math.max(0,y),behavior:'instant'})}return f.apply(window,arguments)}})();
/* Mouvement réduit : les défilements « smooth » demandés par le moteur deviennent instantanés. */
(()=>{const rm=matchMedia('(prefers-reduced-motion: reduce)');const s=o=>(rm.matches&&o&&typeof o==='object'&&o.behavior==='smooth')?{...o,behavior:'auto'}:o;
 for(const P of [Element.prototype,window])for(const k of ['scrollTo','scrollBy','scrollIntoView']){const f=P[k];if(typeof f==='function')P[k]=function(o,...r){return f.call(this,s(o),...r)}}})();

if(top&&'ResizeObserver' in window)new ResizeObserver(setTop).observe(top);

/* Mode sombre : la coque d'origine contient de nombreuses couleurs claires codées en dur. Quand le mode sombre est actif,
   chaque surface claire et chaque texte sombre réellement calculés sont convertis (figures, tracés et insignes exclus).
   Lecture de tous les styles d'abord, écriture ensuite : pas de recalcul de mise en page en cascade. */
const rgb=s=>{s=String(s);let m=s.match(/rgba?\(([\d.]+)[ ,]+([\d.]+)[ ,]+([\d.]+)(?:[ ,/]+([\d.]+))?/);if(m)return{r:+m[1],g:+m[2],b:+m[3],a:m[4]===undefined?1:+m[4]};
 m=s.match(/color\(srgb ([\d.e-]+) ([\d.e-]+) ([\d.e-]+)(?: \/ ([\d.]+))?/);return m?{r:255*m[1],g:255*m[2],b:255*m[3],a:m[4]===undefined?1:+m[4]}:null};
const lum=c=>{const f=v=>{v/=255;return v<=.03928?v/12.92:Math.pow((v+.055)/1.055,2.4)};return .2126*f(c.r)+.7152*f(c.g)+.0722*f(c.b)};
const sat=c=>{const mx=Math.max(c.r,c.g,c.b),mn=Math.min(c.r,c.g,c.b);return mx?(mx-mn)/mx:0};
const SKIP='svg,figure,.mdn-ecg .sv,.mc-pareto-btn,.fluo,.mc-badge,.mdn-keep,.sidebar,.ring,.mdn-director-track i,.mdn-director-courses a.is-complete,.swatches,.theme-dotset';
let seen=new WeakSet();
function autoDark(){if(!root.classList.contains('mdn-dark'))return;const todo=[];
 document.querySelectorAll('#content,.topbar,dialog[open],.mc-navigo,.mdn-toast').forEach(scope=>{if(scope.closest(SKIP))return;const w=document.createTreeWalker(scope,1,{acceptNode:n=>n.matches(SKIP)||n.matches('.mc-panel[hidden]')?2:1});const els=[];for(let n=w.nextNode();n;n=w.nextNode())if(!seen.has(n))els.push(n);els.forEach(el=>{
  seen.add(el);const cs=getComputedStyle(el);
  const bw=parseFloat(cs.borderTopWidth)+parseFloat(cs.borderBottomWidth);if(bw>0){const bc=rgb(cs.borderTopColor);if(bc&&bc.a>=.5&&lum(bc)>.6)todo.push([el,'mdn-dk-line'])}
  if(cs.backgroundImage==='none'&&cs.backgroundColor==='rgba(0, 0, 0, 0)'){const c=rgb(cs.color);if(c&&lum(c)<.3)todo.push(sat(c)<.35||lum(c)<.02?[el,'mdn-dk-ink']:[el,'mdn-dk-tint',cs.color]);return}
  const bg=rgb(cs.backgroundColor);let light=bg&&bg.a>=.5&&lum(bg)>.5;
  if(!light&&cs.backgroundImage.includes('gradient'))light=(cs.backgroundImage.match(/(rgba?|color)\([^)]*\)/g)||[]).some(x=>{const c=rgb(x);return c&&c.a>=.5&&lum(c)>.5});
  if(light)todo.push([el,'mdn-dk-bg']);
  const c=rgb(cs.color);if(c&&lum(c)<.3)todo.push(sat(c)<.35||lum(c)<.02?[el,'mdn-dk-ink']:[el,'mdn-dk-tint',cs.color]);
 })});
 todo.forEach(([el,k,c])=>{el.classList.add(k);if(c)el.style.setProperty('--mdn-c',c)})}
function autoLight(){document.querySelectorAll('.mdn-dk-bg,.mdn-dk-ink,.mdn-dk-tint,.mdn-dk-line').forEach(el=>{el.classList.remove('mdn-dk-bg','mdn-dk-ink','mdn-dk-tint','mdn-dk-line');el.style.removeProperty('--mdn-c')});seen=new WeakSet()}

/* Mode sombre facultatif : bouton dans la barre supérieure, choix mémorisé dans ce navigateur. */
const KEY='medina.dark';let on=false;try{on=localStorage.getItem(KEY)==='1'}catch(e){}
const apply=v=>{['--t1','--t2'].forEach(k=>{const o=root.style.getPropertyValue(k);if(o)root.style.setProperty('--mdn-'+k.slice(2)+'o',o)});root.classList.toggle('mdn-dark',v);if(v)requestAnimationFrame(autoDark);else autoLight();
 document.querySelectorAll('.mdn-darkbtn').forEach(b=>{b.setAttribute('aria-pressed',String(v));b.title=v?'Revenir au mode clair':'Passer au mode sombre'})};
apply(on);
new MutationObserver(()=>{['--t1','--t2'].forEach(k=>{const v=root.style.getPropertyValue(k),n='--mdn-'+k.slice(2)+'o';if(v&&root.style.getPropertyValue(n)!==v)root.style.setProperty(n,v)})}).observe(root,{attributes:true,attributeFilter:['style']});
function darkButton(){const tb=document.querySelector('.top-actions');if(!tb||tb.querySelector('.mdn-darkbtn'))return;const b=document.createElement('button');b.type='button';b.className='mdn-darkbtn';b.setAttribute('aria-label','Mode sombre');
 b.innerHTML='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5z"/></svg>';
 b.onclick=()=>{on=!on;try{localStorage.setItem(KEY,on?'1':'0')}catch(e){}apply(on)};const th=tb.querySelector('.theme-btn');th?th.after(b):tb.appendChild(b);apply(on)}

/* Le lecteur de leçons historique (lesson-core.js) ne peut pas être chargé depuis un fichier local :
   l'erreur technique brute est remplacée par une explication, sans effet sur les cours MEDINA. */
function techNotes(){document.querySelectorAll('#content .notice,#content [role="status"],#content .empty').forEach(n=>{if(n.dataset.mdnFixed||!/lesson-core\.js|Failed to fetch dynamically imported module/.test(n.textContent))return;n.dataset.mdnFixed='1';n.textContent='Le lecteur de leçons historique n’est pas disponible dans ce fichier autonome. Les cours MEDINA rédigés s’ouvrent normalement depuis les entrées CIM.'})}

/* Insigne des cours intégrés en révision : distinct de l'insigne fluorescent réservé aux cours achevés. */
function draftBadges(){if(typeof MEDINA_hasCourse!=='function')return;const done=window.MEDINA_COMPLETE||[];document.querySelectorAll('#content a[href*="#/entry/"]').forEach(a=>{if(a.closest('.mc-toolbar,.mc,.bottomnav,.breadcrumbs')||a.querySelector('.mc-badge,.mc-badge-draft'))return;const m=a.getAttribute('href').match(/#\/entry\/([A-Z]\d{2}(?:\.\d+)?)/);if(!m||!MEDINA_hasCourse(m[1]))return;const code=(window.MEDINA_ALIAS||{})[m[1]]||m[1];if(done.includes(code))return;const s=document.createElement('span');s.className='mc-badge-draft';s.textContent='cours · en révision';s.title='Cours MEDINA intégré, audit indépendant en attente';a.appendChild(s)})}

/* Plan du cours : même numérotation que les îlots (0 = question clinique). */
function tocStart(){document.querySelectorAll('.mc .mc-panel').forEach(p=>{const ol=p.querySelector('.mc-toc ol'),n=parseInt(p.querySelector('.mc-ilot h2 .mc-n')?.textContent,10);if(ol&&!isNaN(n)&&ol.start!==n&&ol.children.length===p.querySelectorAll(':scope .mc-body>.mc-ilot').length)ol.start=n})}
document.addEventListener('click',e=>{
 /* Changement d'onglet depuis la barre collante : le nouveau panneau commence sous les onglets. */
 const b=e.target.closest('.mc .mc-tabs button');if(b){autoDark();requestAnimationFrame(()=>{setTabs();const p=document.querySelector('.mc-panel:not([hidden])'),t=document.querySelector('.mc .mc-tabs');if(!p||!t)return;const st=getComputedStyle(t).position==='sticky';const y=st?scrollY+p.getBoundingClientRect().top-(t.getBoundingClientRect().bottom+12):scrollY+t.getBoundingClientRect().top-(top?top.offsetHeight:0)-8;if(scrollY>y)scrollTo({top:Math.max(0,y),behavior:'instant'})})}
 /* Navigo en mode livre : le livre est ramené dans la fenêtre après le changement de page. */
 if(e.target.closest('.mc-navigo-item')&&document.querySelector('.mc.book')){const bk=document.querySelector('.mc-panel:not([hidden]) .mc-body');setTimeout(()=>bk&&bk.scrollIntoView({block:'start',behavior:'smooth'}),340)}
});
const run=()=>{darkButton();techNotes();draftBadges();tocStart();setTabs();autoDark()};let tm=null;
/* Le mode sombre convertit avant le rendu (microtâche) : pas d'éclair blanc au changement de page. */
new MutationObserver(()=>{if(root.classList.contains('mdn-dark'))autoDark();clearTimeout(tm);tm=setTimeout(run,90)}).observe(document.body,{childList:true,subtree:true});setTimeout(run,350);
})();

/* Césure française de secours. Le texte des cours est justifié ; sans césure, un navigateur privé de dictionnaire
   (Chromium sous Linux, certaines vues intégrées) étire les espaces entre les mots. Si la césure native fonctionne,
   ce module ne fait rien. Sinon, il insère des traits d'union conditionnels (U+00AD) par l'algorithme de Liang,
   avec les motifs français hyph-fr (Copyright (C) 1994-2002 Daniel Flipo, Bernard Gaulle, 2016 Arthur Reutenauer ;
   licence MIT, https://opensource.org/licenses/MIT). Titres, boutons d'interface, code et figures ne sont jamais touchés. */
(()=>{
const native=()=>{const d=document.createElement('div');d.lang='fr';d.style.cssText='position:absolute;left:-9999px;top:0;visibility:hidden;width:3em;font:16px Georgia,serif;-webkit-hyphens:auto;hyphens:auto';d.textContent='anticonstitutionnellement';document.body.appendChild(d);const a=d.offsetHeight;d.style.webkitHyphens=d.style.hyphens='manual';const b=d.offsetHeight;d.remove();return a>b};
if(!document.body||native())return;
document.documentElement.classList.add('mdn-hy');
const M=new Map();let MAX=0;
'.a4 .â4 ab2h .ab3réa ad2h a1è2dre .ae3s4ch 1alcool a2l1algi .amino1a2c .ana3s4tr 1a2nesthési .anti1a2 .anti1e2 .anti1é2 .anti2enne .anti1s2 .apo2s3ta apo2s3tr archi1é2pis .as2ta a2s3tro 1ba 1bâ .bai2se3main 1be 1bé 1bè 1bê 4be. 4bes. 2bent. 1bi 1bî .bi1a2c .bi1a2t .bi1au .bio1a2 .bi2s1a2 .bi1u2 1b2l 4ble. 4bles. 2blent. 1bo 1bô 1b2r 4bre. 4bres. 2brent. 1bu 1bû 1by 1ç 1ca 1câ ca3ou3t2 1ce 1cé 1cè 1cê 4ce. 4ces. 2cent. ja3cent. ac3cent. é3cent. munifi3cent. réti3cent. privatdo3cent. inno3cent. es3cent. acquies4cent. is3cent. immis4cent. .ch4 1c2h 4ch. 2chb 4che. 4ches. 2chent. .chè2vre3feuille 2chg ch2l 4chle. 4chles. chlo2r3a2c chlo2r3é2t 2chm 2chn 2chp ch2r 4chre. 4chres. 2chs 2cht 2chw 1ci 1cî .ci2s1alp 1c2k 4ck. 2ckb 4cke. 4ckes. 2ckent. 2ckf 2ckg 2ck3h 2ckp 2cks 2ckt 1c2l 4cle. 4cles. 2clent. 1co 1cô co1acc co1acq co1a2d co1ap co1ar co1assoc co1assur co1au co1ax 1cœ co1é2 co1ef co1en co1ex .con4 .cons4 .contre1s2c .contre3maître co2nurb .co1o2 .co2o3lie 1c2r 4cre. 4cres. 2crent. 1cu 1cû 1cy .cul4 1da 1dâ .dacryo1a2 d1d2h 1de 1dé 1dè 1dê 4de. 4des. 2dent. déca3dent. é3dent. cci3dent. inci3dent. confi3dent. tri3dent. dissi3dent. chien3dent. .ar3dent. impu3dent. pru3dent. .dé1a2 .dé1io .dé1o2 .dé2s .dé3s2a3cr .dés2a3m .dé3s2a3tell .dé3s2astr .dé3s2c .dé2s1é2 .dé3s2é3gr .dé3s2ensib .dé3s2ert .dé3s2exu .dé2s1i2 .dé3s2i3d .dé3s2i3gn .dé3s2i3li .dé3s2i3nen .dé3s2invo .dé3s2i3r .dé3s2ist .dé3s2o3dé .dé2s1œ .dé3s2o3l .dé3s2o3pil .dé3s2orm .dé3s2orp .dé3s2oufr .dé3s2p .dé3s2t .dé2s1u2n 3d2hal 3d2houd 1di 1dî di2s3cop .di1a2cé .di1a2cid .di1ald .di1a2mi .di1a2tom .di1e2n .di2s3h 2dlent. 1do 1dô 1d2r 4dre. 4dres. 2drent. d1s2 1du 1dû 1dy .dy2s3 .dy2s1a2 .dy2s1i2 .dy2s1o2 .dy2s1u2 .e4 .ê4 .é4 .è4 éd2hi 1é2drie 1é2drique 1é2lectr 1é2lément .en1a2 1é2nerg e2n1i2vr .en1o2 épi2s3cop épi3s4cope e2s3cop .eu2r1a2 eu1s2tat extra1 extra2c extra2i 1fa 1fâ 1fe 1fé 1fè 1fê 4fe. 4fes. 2fent. 1fi 1fî 1f2l 4fle. 4fles. 2flent. 1fo 1fô 1f2r 4fre. 4fres. 2frent. f1s2 1fu 1fû 1fy 1ga 1gâ 1ge 1gé 1gè 1gê 4ge. 4ges. 2gent. ré3gent. entre3gent. indi3gent. dili3gent. intelli3gent. indul3gent. tan3gent. rin3gent. contin3gent. .ar3gent. ser3gent. ter3gent. résur3gent. 1g2ha 1g2he 1g2hi 1g2ho 1g2hy 1gi 1gî 1g2l 4gle. 4gles. 2glent. 1g2n .a2g3nat a2g3nos co2g3niti .i2g3né .i2g3ni .ma2g3nicide .ma2g3nificat .ma2g3num o2g3nomoni o2g3nosi .pro2g3nath pu2g3nable pu2g3nac .sta2g3n .syn2g3nath wa2g3n 4gne. 4gnes. 2gnent. 1go 1gô 1g2r 4gre. 4gres. 2grent. 1gu 1gû g1s2 4gue. 4gues. 2guent. .on3guent. 1gy 1ha 1hâ 1he 1hé 1hè 1hê hémi1é hémo1p2t 4he. 4hes. 1hi 1hî 1ho 1hô 1hu 1hû 1hy hypera2 hypere2 hyperé2 hyperi2 hypero2 hypers2 hype4r1 hyperu2 hypo1a2 hypo1e2 hypo1é2 hypo1i2 hypo1o2 hypo1s2 hypo1u2 .i4 .î4 i1algi i1arthr i1è2dre il2l cil3l rcil4l ucil4l vacil4l gil3l hil3l lil3l l3lion mil3l mil4let émil4l semil4l rmil4l armil5l capil3l papil3la papil3le papil3li papil3lom pupil3l piril3l thril3l cyril3l ibril3l pusil3l .stil3l distil3l instil3l fritil3l boutil3l vanil3lin vanil3lis vil3l avil4l chevil4l uevil4l uvil4l xil3l 1informat .in1a2 .in2a3nit .in2augur .in1e2 .in1é2 .in2effab .in2é3lucta .in2é3narra .in2ept .in2er .in2exora .in1i2 .in2i3miti .in2i3q .in2i3t .in1o2 .in2o3cul .in2ond .in1s2tab .intera2 .intere2 .interé2 .interi2 .intero2 .inte4r3 .interu2 .inters2 .in1u2 .in2uit .in2u3l io1a2ct i1oxy i1s2tat 1j 2jk 4je. 4jes. 2jent. 1ka 1kâ 1ke 1ké 1kè 1kê 4ke. 4kes. 2kent. 1k2h 4kh. .kh4 1ki 1kî 1ko 1kô 1k2r 1ku 1kû 1ky 1la 1lâ 1là la2w3re 1le 1lé 1lè 1lê 4le. 4les. 2lent. .ta3lent. iva3lent. équiva4lent. monova3lent. polyva3lent. re3lent. .do3lent. indo3lent. inso3lent. turbu3lent. succu3lent. fécu3lent. trucu3lent. opu3lent. corpu3lent. ru3lent. sporu4lent. 1li 1lî 1lo 1lô l1s2t 1lu 1lû 1ly 1ma 1mâ .ma2c3k .macro1s2c .ma2l1a2dres .ma2l1a2dro .ma2l1aisé .ma2l1ap .ma2l1a2v .ma2l1en .ma2l1int .ma2l1oc .ma2l1o2d .ma2r1x 1me 1mé 1mè 1mê .mé2g1oh .mé2sa .mé3san .mé2s1es .mé2s1i .mé2s1u2s .méta1s2ta 4me. 4mes. â2ment. da2ment. fa2ment. amalga2ment. cla2ment. ra2ment. tempéra3ment. ta2ment. testa3ment. qua2ment. è2ment. carê2ment. diaphrag2ment. ryth2ment. ai2ment. rai3ment. abî2ment. éci2ment. vidi2ment. subli2ment. éli2ment. reli2ment. mi2ment. ani2ment. veni2ment. ri2ment. détri3ment. nutri3ment. inti2ment. esti2ment. l2ment. flam2ment. gram2ment. .gem2ment. om2ment. .com3ment. ô2ment. slalo2ment. chro2ment. to2ment. ar2ment. .sar3ment. er2ment. antifer3ment. .ser3ment. fir2ment. or2ment. as2ment. au2ment. écu2ment. fu2ment. hu2ment. fichu3ment. llu2ment. plu2ment. bou2ment. bru2ment. su2ment. tu2ment. 1mi 1mî .milli1am 1m2némo 1m2nès 1m2nési 1mo 1mô 1mœ .mono1a2 .mono1e2 .mono1é2 .mono1i2 .mono1ï2dé .mono1o2 .mono1u2 .mono1s2 mon2t3réal m1s2 1mu 1mû 1my moye2n1â2g 1na 1nâ 1ne 1né 1nè 1nê 4ne. 4nes. 2nent. réma3nent. imma3nent. perma3nent. .émi3nent. préémi3nent. proémi3nent. surémi3nent. immi3nent. conti3nent. perti3nent. absti3nent. 1ni 1nî 1no 1nô 1nœ .no2n1obs 1nu 1nû n3s2at. n3s2ats. n1x 1ny .o4 .ô4 o2b3long 1octet o1d2l o1è2dre o1ioni ombud2s3 omni1s2 o1s2tas o1s2tat o1s2téro o1s2tim o1s2tom o1s2trad o1s2tratu o1s2triction .oua1ou .ovi1s2c oxy1a2 1pa 1pâ paléo1é2 .pa2n1a2f .pa2n1a2mé .pa2n1a2ra .pa2n1is .pa2n1o2ph .pa2n1opt .pa2r1a2che .pa2r1a2chè .para1s2 .pa2r3hé 1pe 1pé 1pè 1pê 4pe. 4pes. 2pent. re3pent. .ar3pent. ser3pent. .pen2ta per3h pé2nul .pe4r .per1a2 .per1e2 .per1é2 .per1i2 .per1o2 .per1u2 pé1r2é2q .péri1os .péri1s2 .péri2s3s .péri2s3ta .péri1u2 1p2h .ph4 4ph. .phalan3s2t 4phe. 4phes. 2phent. ph2l 4phle. 4phles. 2phn photo1s2 ph2r 4phre. 4phres. 2phs 2pht 3ph2talé 3ph2tis 1pi 1pî 1p2l 4ple. 4ples. 2plent. .pluri1a 1p2né 1p2neu 1po 1pô po1astre poly1a2 poly1e2 poly1é2 poly1è2 poly1i2 poly1o2 poly1s2 poly1u2 .pon2tet .pos2t3h .pos2t1in .pos2t1o2 .pos2t3r .post1s2 1p2r 4pre. 4pres. 2prent. .pré1a2 .pré2a3la .pré2au .pré1é2 .pré1e2 .pré1i2 .pré1o2 .pré1u2 .pré1s2 .pro1é2 .pro1s2cé pro2s3tat .prou3d2h 1p2sych .psycho1a2n 1p2tèr 1p2tér 1pu .pud1d2l 1pû 1py 1q 4que. 4ques. 2quent. é3quent. élo3quent. grandilo3quent. 1ra 1râ radio1a2 1re 1ré 1rè 1rê .ré1a2 .ré2a3le .ré2a3lis .ré2a3lit .ré2aux .ré1é2 .ré1e2 .ré2el .ré2er .ré2èr .ré1i2 .ré2i3fi .ré1o2 .re1s2 .re2s3cap .re2s3cisi .re2s3ciso .re2s3cou .re2s3cri .re2s3pect .re2s3pir .re2s3plend .re2s3pons .re2s3quil .re2s3s .re2s3t .re3s4tab .re3s4tag .re3s4tand .re3s4tat .re3s4tén .re3s4tér .re3s4tim .re3s4tip .re3s4toc .re3s4top .re3s4tr .re4s5trein .re4s5trict .re4s5trin .re3s4tu .re3s4ty .réu2 .ré2uss .rétro1a2 4re. 4res. 2rent. .pa3rent. appa3rent. transpa3rent. é3rent. tor3rent. cur3rent. 1r2h 4rhe. 4rhes. 2r3heur 2r3hydr 1ri 1rî 1ro 1rô 1ru 1rû 1ry 1sa 1sâ .sch4 1s2caph 1s2clér 1s2cop 1s2ch e2s3ch i2s3ché i2s3chia i2s3chio 4sch. 4sche. 4sches. 2schs 1se 1sé 1sè 1sê sesqui1a2 4se. 4ses. 2sent. ab3sent. pré3sent. .res3sent. .seu2le .sh4 1s2h 4sh. 4she. 4shes. 2shent. 2shm 2s3hom 2shr 2shs 1si 1sî 1s2lav 1s2lov 1so 1sô 1sœ 1s2patia 1s2perm 1s2por 1s2phèr 1s2phér 1s2piel 1s2piros 1s2tandard 1s2tein stéréo1s2 1s2tigm 1s2tock 1s2tomos 1s2troph 1s2tructu 1s2tyle 1su 1sû .su2b1a2 .su3b2alt .su2b1é2 .su3b2é3r .su2b1in .su2b3limin .su2b3lin .su2b3lu sub1s2 .su2b1ur supero2 supe4r1 supers2 .su2r1a2 su3r2ah .su3r2a3t .su2r1e2 .su3r2eau .su3r2ell .su3r2et .su2r1é2 .su2r3h .su2r1i2m .su2r1inf .su2r1int .su2r1of .su2r1ox 1sy 1ta 1tâ 1tà tachy1a2 tchin3t2 1te 1té 1tè 1tê télé1e2 télé1i2 télé1o2b télé1o2p télé1s2 4te. 4tes. 2tent. .la3tent. .pa3tent. compé3tent. éni3tent. mécon3tent. omnipo3tent. ventripo3tent. équipo3tent. impo3tent. mit3tent. .th4 1t2h 4th. 4the. 4thes. thermo1s2 2t3heur 2thl 2thm 2thn th2r 4thre. 4thres. 2ths 1ti 1tî 1to 1tô 1t2r tran2s1a2 tran3s2act tran3s2ats tran2s3h tran2s1o2 tran2s3p tran2s1u2 4tre. 4tres. 2trent. .tri1a2c .tri1a2n .tri1a2t .tri1o2n t1t2l 1tu 1tû tung2s3 1ty .u4 .û4 uni1o2v uni1a2x u2s3tr 1va 1vâ 1ve 1vé 1vè 1vê vélo1s2ki 4ve. 4ves. 2vent. conni3vent. .sou3vent. 1vi 1vî 1vo 1vô vol2t1amp 1v2r 4vre. 4vres. 2vrent. 1vu 1vû 1vy 1wa 1we 4we. 4wes. 2went. 1wi 1wo 1wu 1w2r 2xent. .y4 y1asth y1s2tom y1algi 1za 1ze 1zé 1zè 4ze. 4zes. 2zent. privatdo3zent. 1zi 1zo 1zu 1zy'.split(' ').forEach(p=>{let l='';const n=[0];for(const c of p){if(c>='0'&&c<='9')n[n.length-1]=+c;else{l+=c;n.push(0)}}M.set(l,n);if(l.length>MAX)MAX=l.length});
const cache=new Map();
/* Points de coupure permis : deux lettres au moins avant, trois au moins après (usage typographique français). */
const cut=w=>{let at=cache.get(w);if(at)return at;const s='.'+w+'.',L=s.length,pt=new Array(L+1).fill(0);
 for(let i=0;i<L;i++)for(let j=i+1,e=Math.min(L,i+MAX);j<=e;j++){const v=M.get(s.slice(i,j));if(v)for(let k=0;k<v.length;k++)if(v[k]>pt[i+k])pt[i+k]=v[k]}
 at=[];for(let i=2;i<=w.length-3;i++)if(pt[i+1]%2)at.push(i);cache.set(w,at);return at};
const WORD=/\p{L}{6,}/gu,UP=/\p{Lu}/u,SKIP='h1,h2,h3,h4,h5,h6,code,pre,kbd,samp,script,style,textarea,svg,.mc-code',TARGET='.mc-ilot,.mc-dlg-b';
const seen=new WeakSet();
const one=t=>{if(seen.has(t))return;seen.add(t);if(t.data.length<6)return;const e=t.parentElement;if(!e||e.closest(SKIP))return;const b=e.closest('button');if(b&&!b.classList.contains('mc-w'))return;
 const s=t.data.replace(WORD,x=>{if(UP.test(x.slice(1)))return x;const at=cut(x.toLowerCase());if(!at.length)return x;let o='',l=0;for(const i of at){o+=x.slice(l,i)+'­';l=i}return o+x.slice(l)});if(s!==t.data)t.data=s};
const hyph=n=>{if(n.nodeType===3){one(n);return}const w=document.createTreeWalker(n,NodeFilter.SHOW_TEXT),a=[];while(w.nextNode())a.push(w.currentNode);a.forEach(one)};
const handle=n=>{const e=n.nodeType===1?n:n.parentElement;if(!e)return;if(e.closest(TARGET))hyph(n);else if(n.nodeType===1)n.querySelectorAll(TARGET).forEach(hyph)};
/* Microtâche : la césure est posée avant le rendu, sans reflux visible. */
new MutationObserver(ms=>{for(const m of ms)m.addedNodes.forEach(handle)}).observe(document.body,{childList:true,subtree:true});
document.querySelectorAll(TARGET).forEach(hyph);
/* Copier un passage ne transporte pas les traits d'union invisibles. */
document.addEventListener('copy',e=>{const s=String(getSelection());if(!s.includes('­')||!e.clipboardData)return;e.clipboardData.setData('text/plain',s.replace(/­/g,''));e.preventDefault()});
})();
