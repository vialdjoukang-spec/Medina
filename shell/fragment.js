/* S01 course surface. Loaded only when a fragment explicitly enables it. */
(() => {
 'use strict';
 const F=DATA.fragment;
 if(F?.surface!=='courses-v1')return;
 const byCode=new Map(F.courses.map(c=>[c.code,c]));
 const aliases=new Set(F.courses.flatMap(c=>c.covers||[c.code]));
 const categoryByCode=new Map(F.categories.flatMap(g=>g.chapters.map(code=>[code,g])));
 const card=c=>`<a class="s01-course" href="#/entry/${h(c.code)}" data-s01-course="${h(c.code)}"><span class="s01-course-code">${h(c.code)}</span><span class="s01-course-copy"><span class="s01-course-title">${h(c.title)}</span><small class="s01-course-status">${c.complete?'✓ Déclaré achevé et audité':'Cours intégré · audit à compléter'}</small></span><span class="s01-course-arrow" aria-hidden="true">↗</span></a>`;
 const rule=()=>'<details class="s01-rule"><summary>Règle d’or</summary><p>Le lecteur comprend, il ne devine pas. Chaque notion relie le mécanisme, les manifestations et la décision clinique.</p></details>';
 const baseRead=readRoute;
 readRoute=function(){
  const r=baseRead();
  if(r.type==='pathology'&&aliases.has(r.id.toUpperCase())){r.type='entry';r.id=r.id.toUpperCase()}
  if(r.type==='entry'){
   r.id=r.id.toUpperCase();
   if(!aliases.has(r.id))return{type:'home',id:'',q:new URLSearchParams()};
   r.q.delete('specialty');r.q.delete('view');
  }
  if(r.type==='specialty'&&r.id!==F.specialty)return{type:'home',id:'',q:new URLSearchParams()};
  if(!['home','entry','specialty','search','notebook','method'].includes(r.type))return{type:'home',id:'',q:new URLSearchParams()};
  return r;
 };
 homePage=function(){
  pageTitle(F.name+' · Cours');
  const done=F.courses.filter(c=>c.complete).length;
  return `<div class="s01-home"><header class="s01-cover"><div><small>MEDINA · S01</small><h1>${h(F.name)}</h1></div><div class="s01-counts"><span><b>${F.courses.length}</b>cours intégrés</span><span><b>${F.categories.length}</b>catégories</span><span><b>${done}</b>déclarés achevés</span></div></header><nav class="s01-category-index" aria-label="Catégories de cours">${F.categories.map((g,i)=>`<a href="#/home?category=${h(g.id)}" data-s01-category="${h(g.id)}">${i+1}. ${h(g.nom)}</a>`).join('')}</nav>${F.categories.map((g,i)=>`<section class="s01-category" id="s01-category-${h(g.id)}" aria-labelledby="s01-heading-${h(g.id)}"><header class="s01-category-heading"><span class="s01-category-number">${i+1}</span><h2 id="s01-heading-${h(g.id)}">${h(g.nom)}</h2><small>${g.chapters.length} cours</small></header><div class="s01-courses">${g.chapters.map(code=>card(byCode.get(code))).join('')}</div></section>`).join('')}${rule()}</div>`;
 };
 specialtyPage=function(){context={sid:F.specialty};return homePage()};
 searchPageView=function(){
  pageTitle('Recherche · '+F.name);const query=route.q.get('q')||'',nq=norm(query);
  const matches=F.courses.filter(c=>norm([c.code,...(c.covers||[]),c.title,categoryByCode.get(c.code).nom].join(' ')).includes(nq));
  return `<div class="s01-search"><div class="breadcrumbs"><a href="#/home">${h(F.name)}</a><span>›</span><span>Recherche</span></div><header class="s01-cover"><div><small>RECHERCHE DANS LES COURS</small><h1>${query?'« '+h(query)+' »':F.name}</h1></div><span>${matches.length} cours</span></header><div class="s01-courses">${matches.map(card).join('')||'<p class="s01-rule">Aucun cours intégré ne correspond à cette recherche.</p>'}</div></div>`;
 };
 crumbs=function(items){
  const c=byCode.get(MC_code(route.id)),g=c&&categoryByCode.get(c.code);
  return `<div class="breadcrumbs"><a href="#/home">${h(F.name)}</a>${g?`<span>›</span><a href="#/home?category=${h(g.id)}">${h(g.nom)}</a>`:''}<span>›</span><span>${h(c?.code||items.at(-1)?.[0]||'Cours')}</span></div>`;
 };
 nextPrevious=function(e){
  const i=F.courses.findIndex(c=>c.code===MC_code(e.code)),prev=F.courses[i-1],next=F.courses[i+1];
  return `<nav class="bottomnav" aria-label="Navigation entre les cours">${prev?`<a class="btn" href="#/entry/${h(prev.code)}">← ${h(prev.code)} · Précédent</a>`:'<span></span>'}<a class="btn tiny" href="#/home">Tous les cours</a>${next?`<a class="btn" href="#/entry/${h(next.code)}">${h(next.code)} · Suivant →</a>`:'<span></span>'}</nav>`;
 };
 footer=function(){const done=F.courses.filter(c=>c.complete).length;return `<footer class="s01-footer">Medina · ${h(F.name)} · CIM-10-GM 2024<br>${done} cours déclarés achevés · ${F.courses.length-done} cours à auditer.</footer>`};
 methodPage=function(){pageTitle('Règle d’or et sources');return `<div class="s01-home"><header class="s01-cover"><h1>Règle d’or et sources</h1></header>${rule()}<section class="s01-rule"><h2>Statut des cours</h2><p>Le statut d’audit est celui enregistré dans les sources de Medina. La présence d’un cours ne constitue pas une nouvelle validation médicale.</p><p>Les références figurent dans chaque cours. Le classement clinique de l’accueil conserve les codes CIM de chaque chapitre.</p><p><a href="#/home">Revenir aux cours cardiovasculaires</a></p></section></div>`};
 showCommandPalette=function(){openModal(F.name,`<div class="command-links"><a data-close-modal class="command-link" href="#/home">Tous les cours</a><a data-close-modal class="command-link" href="#/search">Rechercher un cours</a><a data-close-modal class="command-link" href="#/notebook">Carnet du fragment</a></div><div class="s01-category-index">${F.categories.map(g=>`<a data-close-modal href="#/home?category=${h(g.id)}">${h(g.nom)}</a>`).join('')}</div>`)};
 document.getElementById('command-btn').onclick=showCommandPalette;
 document.getElementById('medora-intelligence-link')?.remove();
 const oldSanitize=sanitizeState;
 sanitizeState=function(raw){
  const s=oldSanitize(raw);
  for(const k of ['bookmarks','read','deepen','recent'])s[k]=s[k].filter(code=>aliases.has(code));
  for(const k of ['notes','checks','gaps'])s[k]=Object.fromEntries(Object.entries(s[k]).filter(([code])=>aliases.has(code)));
  if(!aliases.has(s.last))s.last=null;
  return s;
 };
 state=sanitizeState(state);
 const coursePage=MEDINA_coursePage;
 MEDINA_coursePage=function(e){return coursePage(e).replace(/<a class="btn tiny"[^>]*>Plan de révision détaillé<\/a>/,'<a class="btn tiny" href="#/home">← Tous les cours</a>')};
 const entry=entryPage;
 entryPage=function(){
  if(!window.MDN_READY){pageTitle('Ouverture du cours');return '<p role="status">Ouverture du cours…</p>'}
  return entry();
 };
 const baseBind=bindPage;
 bindPage=function(){baseBind();const category=route.q.get('category');if(category)requestAnimationFrame(()=>document.getElementById('s01-category-'+category)?.scrollIntoView({block:'start',behavior:'instant'}))};
 drawSidebar=function(){
  document.getElementById('spec-nav').innerHTML=F.categories.map((g,i)=>`<details open><summary>${i+1}. ${h(g.nom)}</summary>${g.chapters.map(code=>`<a href="#/entry/${h(code)}" data-fragment-chapter="${h(code)}" class="${MC_code(route.id)===code?'active':''}"><span class="nav-num">${h(code)}</span><span class="nav-label">${h(byCode.get(code).title)}</span></a>`).join('')}</details>`).join('');
  document.querySelectorAll('.nav-main a').forEach(a=>a.classList.toggle('active',a.getAttribute('href')==='#/'+route.type));
 };

 // Fixed rectangular plan: permanently open on desktop, explicit drawer on mobile.
 MC_navigoMount=function(m){
  const host=document.createElement('div');host.className='mc-navigo';
  host.innerHTML='<button type="button" class="mc-navigo-trigger" aria-controls="mc-navigo-panel" aria-expanded="false"><span aria-hidden="true">▤</span> Navigo · Plan</button><aside id="mc-navigo-panel" class="mc-navigo-panel" aria-label="Navigo : plan du cours" hidden><div class="mc-navigo-head"><div><small>Navigo · Plan du cours</small><strong class="mc-navigo-title"></strong></div><button type="button" class="mc-navigo-close" aria-label="Fermer Navigo">×</button></div><div class="mc-navigo-tabs" role="group" aria-label="Onglets du cours"></div><label class="mc-navigo-search-label">Rechercher une partie<input class="mc-navigo-search" type="search" placeholder="Titre ou numéro…"></label><nav class="mc-navigo-list" aria-label="Parties et sous-parties"></nav><div class="mc-navigo-foot"></div></aside>';
  document.body.append(host);
  const desktop=matchMedia('(min-width:1100px)'),trigger=host.querySelector('.mc-navigo-trigger'),drawer=host.querySelector('.mc-navigo-panel'),list=host.querySelector('.mc-navigo-list'),search=host.querySelector('.mc-navigo-search');
  let buttons=[];
  function open(on,focus=true){drawer.hidden=desktop.matches?false:!on;trigger.setAttribute('aria-expanded',String(!drawer.hidden));if(focus&&!desktop.matches)(on?search:trigger).focus({preventScroll:true})}
  function move(heading){
   const body=heading.closest('.mc-body');
   if(m.classList.contains('book')&&body){const page=Array.from(body.children).find(x=>x.contains(heading));if(page){body.scrollTo({left:body.scrollLeft+page.getBoundingClientRect().left-body.getBoundingClientRect().left,behavior:'instant'});page.scrollTo({top:page.scrollTop+heading.getBoundingClientRect().top-page.getBoundingClientRect().top-14,behavior:'instant'});heading.setAttribute('tabindex','-1');heading.focus({preventScroll:true});return}}
   heading.scrollIntoView({block:'start',behavior:'instant'});heading.setAttribute('tabindex','-1');heading.focus({preventScroll:true});
  }
  function filter(){const query=norm(search.value);let count=0;buttons.forEach(b=>{b.hidden=!norm(b.textContent).includes(query);if(!b.hidden)count++});host.querySelector('.mc-navigo-foot').textContent=count+' parties affichées'}
  function refresh(){
   if(!m.isConnected)return;
   const panel=m.querySelector('.mc-panel:not([hidden])');if(!panel)return;
   host.querySelector('.mc-navigo-title').textContent=m.querySelector('h1')?.textContent.trim()||'Cours';
   const tabs=host.querySelector('.mc-navigo-tabs');tabs.replaceChildren();
   m.querySelectorAll('.mc-tabs [data-p]').forEach(tab=>{const b=document.createElement('button');b.type='button';b.textContent=tab.textContent;b.className=tab.getAttribute('aria-selected')==='true'?'is-active':'';b.onclick=()=>tab.click();tabs.append(b)});
   list.replaceChildren();buttons=[];
   panel.querySelectorAll('.mc-ilot h2,.mc-ilot h3,.mc-ilot h4,.mc-sci:not([hidden])>h2').forEach(heading=>{
    if(heading.closest('.mc-sci[hidden]'))return;
    const b=document.createElement('button');b.type='button';b.className='mc-navigo-item mc-navigo-'+heading.tagName.toLowerCase();b.textContent=MC_navLabel(heading);
    b.onclick=()=>{buttons.forEach(x=>x.removeAttribute('aria-current'));b.setAttribute('aria-current','location');open(false,false);move(heading)};list.append(b);buttons.push(b);
   });filter();
  }
  trigger.onclick=()=>{refresh();open(drawer.hidden)};host.querySelector('.mc-navigo-close').onclick=()=>open(false);
  search.oninput=filter;
  const onKey=e=>{if(e.key==='Escape'&&!desktop.matches&&!drawer.hidden){e.preventDefault();open(false)}};
  const outside=e=>{if(!desktop.matches&&!drawer.hidden&&!host.contains(e.target))open(false,false)};
  const resize=()=>open(false,false);
  document.addEventListener('keydown',onKey);document.addEventListener('pointerdown',outside);desktop.addEventListener('change',resize);
  const observer=new MutationObserver(()=>{if(!m.isConnected)MC_navigoDestroy()});observer.observe(document.getElementById('content'),{childList:true});
  MC_NAV_CLEANUP=()=>{observer.disconnect();desktop.removeEventListener('change',resize);document.removeEventListener('keydown',onKey);document.removeEventListener('pointerdown',outside);host.remove()};
  open(desktop.matches,false);return refresh;
 };
 render();
})();
