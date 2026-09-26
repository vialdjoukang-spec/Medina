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
const setTabs=()=>{const t=document.querySelector('.mc .mc-tabs');root.style.setProperty('--mdn-tabs',(t&&getComputedStyle(t).position==='sticky'?t.offsetHeight+8:0)+'px')};addEventListener('resize',setTabs);
/* Mouvement réduit : les défilements « smooth » demandés par le moteur deviennent instantanés. */
(()=>{const rm=matchMedia('(prefers-reduced-motion: reduce)');const s=o=>(rm.matches&&o&&typeof o==='object'&&o.behavior==='smooth')?{...o,behavior:'auto'}:o;
 for(const P of [Element.prototype,window])for(const k of ['scrollTo','scrollBy','scrollIntoView']){const f=P[k];if(typeof f==='function')P[k]=function(o,...r){return f.call(this,s(o),...r)}}})();
/* Icône « stomach » de la coque : chemin SVG incomplet (erreur de console préexistante). */
try{if(typeof PATHS==='object'&&PATHS.stomach&&PATHS.stomach.endsWith('1-5 1-7V3z'))PATHS.stomach=PATHS.stomach.replace('1-5 1-7V3z','1-5 1-7 0V3z')}catch(e){}
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
 document.querySelectorAll('#content,.topbar,dialog[open]').forEach(scope=>scope.querySelectorAll('*').forEach(el=>{
  if(seen.has(el))return;seen.add(el);if(el.closest(SKIP))return;const cs=getComputedStyle(el);
  const bw=parseFloat(cs.borderTopWidth)+parseFloat(cs.borderBottomWidth);if(bw>0){const bc=rgb(cs.borderTopColor);if(bc&&bc.a>=.5&&lum(bc)>.6)todo.push([el,'mdn-dk-line'])}
  if(cs.backgroundImage==='none'&&cs.backgroundColor==='rgba(0, 0, 0, 0)'){const c=rgb(cs.color);if(c&&lum(c)<.3)todo.push(sat(c)<.35||lum(c)<.02?[el,'mdn-dk-ink']:[el,'mdn-dk-tint',cs.color]);return}
  const bg=rgb(cs.backgroundColor);let light=bg&&bg.a>=.5&&lum(bg)>.5;
  if(!light&&cs.backgroundImage.includes('gradient'))light=(cs.backgroundImage.match(/(rgba?|color)\([^)]*\)/g)||[]).some(x=>{const c=rgb(x);return c&&c.a>=.5&&lum(c)>.5});
  if(light)todo.push([el,'mdn-dk-bg']);
  const c=rgb(cs.color);if(c&&lum(c)<.3)todo.push(sat(c)<.35||lum(c)<.02?[el,'mdn-dk-ink']:[el,'mdn-dk-tint',cs.color]);
 }));
 todo.forEach(([el,k,c])=>{el.classList.add(k);if(c)el.style.setProperty('--mdn-c',c)})}
function autoLight(){document.querySelectorAll('.mdn-dk-bg,.mdn-dk-ink,.mdn-dk-tint,.mdn-dk-line').forEach(el=>{el.classList.remove('mdn-dk-bg','mdn-dk-ink','mdn-dk-tint','mdn-dk-line');el.style.removeProperty('--mdn-c')});seen=new WeakSet()}

/* Mode sombre facultatif : bouton dans la barre supérieure, choix mémorisé dans ce navigateur. */
const KEY='medina.dark';let on=false;try{on=localStorage.getItem(KEY)==='1'}catch(e){}
const apply=v=>{['--t1','--t2'].forEach(k=>{const o=root.style.getPropertyValue(k);if(o)root.style.setProperty('--mdn-'+k.slice(2)+'o',o)});root.classList.toggle('mdn-dark',v);if(v)requestAnimationFrame(autoDark);else autoLight();
 document.querySelectorAll('.mdn-darkbtn').forEach(b=>{b.setAttribute('aria-pressed',String(v));b.title=v?'Revenir au mode clair':'Passer au mode sombre'})};
apply(on);
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
/* À l'ouverture d'un cours, la coque défile de 200 px : la barre d'outils du cours est ramenée sous la barre collante. */
let lastRoute='';function revealToolbar(){if(location.hash===lastRoute)return;lastRoute=location.hash;const t=document.querySelector('.mc-toolbar');if(!t||!top)return;requestAnimationFrame(()=>{const y=t.getBoundingClientRect().top,H=top.offsetHeight;if(y<H+4&&y>-400)scrollBy({top:y-H-8,behavior:'instant'})})}
document.addEventListener('click',e=>{
 /* Changement d'onglet depuis la barre collante : le nouveau panneau commence sous les onglets. */
 const b=e.target.closest('.mc .mc-tabs button');if(b)requestAnimationFrame(()=>{setTabs();const p=document.querySelector('.mc-panel:not([hidden])'),t=document.querySelector('.mc .mc-tabs');if(!p||!t)return;const y=scrollY+p.getBoundingClientRect().top-(t.getBoundingClientRect().bottom+12);if(scrollY>y)scrollTo({top:Math.max(0,y),behavior:'instant'})});
 /* Navigo en mode livre : le livre est ramené dans la fenêtre après le changement de page. */
 if(e.target.closest('.mc-navigo-item')&&document.querySelector('.mc.book')){const bk=document.querySelector('.mc-panel:not([hidden]) .mc-body');setTimeout(()=>bk&&bk.scrollIntoView({block:'start',behavior:'smooth'}),340)}
});
const run=()=>{darkButton();techNotes();draftBadges();tocStart();setTabs();revealToolbar();autoDark()};let tm=null;
/* Le mode sombre convertit avant le rendu (microtâche) : pas d'éclair blanc au changement de page. */
new MutationObserver(()=>{if(root.classList.contains('mdn-dark'))autoDark();clearTimeout(tm);tm=setTimeout(run,90)}).observe(document.body,{childList:true,subtree:true});setTimeout(run,350);
})();
