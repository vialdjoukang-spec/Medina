
/* ===== MEDINA — moteur de cours ===== */
const MC_GLOSS=JSON.parse(document.getElementById('medina-glossary').textContent);
const MC={store:{get(k,d){try{const v=localStorage.getItem('medina.course.'+k);return v===null?d:JSON.parse(v)}catch(e){return d}},set(k,v){try{localStorage.setItem('medina.course.'+k,JSON.stringify(v))}catch(e){}}}};
function MC_code(code){return (window.MEDINA_ALIAS||{})[code]||code}
function MEDINA_hasCourse(code){return !!document.getElementById('ch-'+MC_code(code))}
function MEDINA_coursePage(e){
 pageTitle(`${e.code} — ${e.title}`);
 const sid=SM[route.q.get('specialty')]?route.q.get('specialty'):e.primary;const s=SM[sid];context={sid,e};
 const tpl=document.getElementById('ch-'+MC_code(e.code));
 const fonts=[["'Atkinson Hyperlegible Next','Atkinson Hyperlegible',system-ui,sans-serif",'Atkinson Hyperlegible (lisibilité)'],["'Anthropic Serif',Georgia,serif",'Anthropic Serif'],["Georgia,'Times New Roman',serif",'Georgia'],["system-ui,sans-serif",'Système'],["'Segoe UI',Arial,sans-serif",'Segoe UI'],["'Literata',Georgia,serif",'Literata'],["'Source Serif 4',Georgia,serif",'Source Serif'],["'EB Garamond',Georgia,serif",'Garamond'],["'Atkinson Hyperlegible','Segoe UI',sans-serif",'Atkinson'],["'Inter','Segoe UI',sans-serif",'Inter']];
 return `${crumbs([[s.title,url('specialty',s.id)],[e.system,url('specialty',s.id,{system:e.organ})],[e.code]])}
 <div class="mc" data-code="${h(MC_code(e.code))}">
 <div class="mc-toolbar mc-ui"><a class="btn tiny" href="${h(url('entry',e.code,{view:'plan'}))}">Plan de révision détaillé</a>
 <label>Police <select class="mc-font">${fonts.map(f=>`<option value="${h(f[0])}">${f[1]}</option>`).join('')}</select></label>
 <div class="mc-size-wrap"><button type="button" class="mc-size-toggle" aria-expanded="false" aria-controls="mc-size-pop">Police Taille <output class="mc-size-value">17 px</output></button>
 <div id="mc-size-pop" class="mc-size-pop" hidden><label for="mc-size-range">Taille des caractères</label><div class="mc-size-row"><button type="button" class="mc-fsdn" aria-label="Diminuer la taille des caractères">A−</button><input id="mc-size-range" class="mc-size-range" type="range" min="14" max="24" step="1" value="17"><button type="button" class="mc-fsup" aria-label="Augmenter la taille des caractères">A+</button></div><button type="button" class="mc-size-reset">Réinitialiser à 17 px</button></div></div>
 <button class="mc-book" aria-pressed="false" title="Îlots verticaux ou pages horizontales">⇆ Livre</button></div>
 ${tpl.innerHTML}</div>${nextPrevious(e,sid)}`;
}
function MC_badges(){document.querySelectorAll('#content a[href*="#/entry/"]').forEach(a=>{const m=a.getAttribute('href').match(/#\/entry\/([A-Z]\d{2}(?:\.\d+)?)/);if(!m||a.closest('.mc-toolbar')||a.querySelector('.mc-badge'))return;if(MEDINA_hasCourse(m[1])&&(window.MEDINA_COMPLETE||[]).includes(MC_code(m[1]))){const b=document.createElement('span');b.className='mc-badge';b.textContent='100 % rédigé';a.appendChild(b)}})}
let MC_NAV_CLEANUP=null,MC_SIZE_CLEANUP=null,MC_NAV_API=null,MC_NAV_JUMP=false;
function MC_navigoDestroy(){if(MC_NAV_CLEANUP){MC_NAV_CLEANUP();MC_NAV_CLEANUP=null}}
/* Libellé Navigo : le numéro (span.mc-n ou .mc-subn) est séparé du titre par une espace. */
function MC_navLabel(h){const t=h.textContent.replace(/\s+/g,' ').trim(),n=h.querySelector('.mc-n,.mc-subn');if(!n)return t;const k=n.textContent.trim();return k&&t.startsWith(k)?k+' '+t.slice(k.length).trim():t}
/* ===== Navigo : plan de la leçon (16.10.2026) =====
   Arbre ARIA onglets → (sections Sciences) → parties → sous-parties, recherche instantanée sans accents,
   suivi de la position de lecture, saut avec décalage sous les barres collantes, ancre « ?nav= » dans l'URL
   et retour arrière. Modes : tiroir (bureau), feuille basse (≤ 760 px), panneau épinglé (≥ 1440 px, par défaut
   dès 1480 px). Raccourcis : N ou Ctrl+K. Le contenu des cours n'est jamais modifié. */
const MC_NAV_PIN_MIN=1440,MC_NAV_PIN_DEFAULT=1480,MC_NAV_SHEET_MAX=760;
const MC_navNorm=s=>String(s||'').normalize('NFD').replace(/[\u0300-\u036f]/g,'').replace(/[’']/g,' ').toLocaleLowerCase('fr');
const MC_navReduce=()=>matchMedia('(prefers-reduced-motion: reduce)').matches;
const MC_navClean=s=>String(s||'').replace(/^[^\p{L}\p{N}]+/u,'').replace(/\s+/g,' ').trim();
function MC_navSplit(h){const t=h.textContent.replace(/\s+/g,' ').trim(),n=h.querySelector('.mc-n,.mc-subn');
 if(n){const k=n.textContent.replace(/\s+/g,' ').trim();if(k&&t.startsWith(k))return {num:k.replace(/\.$/,''),label:t.slice(k.length).trim()||t}}
 const x=t.match(/^(\d+(?:\.\d+)*)\.?\s+(\S.*)$/);return x?{num:x[1],label:x[2]}:{num:'',label:t}}
/* Hauteur masquée par la barre supérieure et les onglets collants : cible du saut et de la position de lecture. */
function MC_navOffset(m){const bar=document.querySelector('.topbar');let y=bar?Math.max(0,bar.getBoundingClientRect().bottom):0;
 const tabs=m&&m.querySelector('.mc-tabs');if(tabs){const cs=getComputedStyle(tabs);if(cs.position==='sticky'||cs.position==='fixed')y=Math.max(y,(parseFloat(cs.top)||0)+tabs.offsetHeight)}
 return Math.round(y+14)}
/* Surlignage des termes recherchés, insensible aux accents et à la casse. */
function MC_navMark(text,terms){const chars=Array.from(String(text));if(!terms||!terms.length)return h(text);
 let norm='';const map=[];chars.forEach((c,i)=>{for(const x of MC_navNorm(c)){norm+=x;map.push(i)}});
 const hit=new Array(chars.length).fill(false);terms.forEach(t=>{let p=norm.indexOf(t);while(t&&p>=0){for(let k=p;k<p+t.length;k++)hit[map[k]]=true;p=norm.indexOf(t,p+t.length)}});
 let out='',open=false;chars.forEach((c,i)=>{if(hit[i]&&!open){out+='<mark>';open=true}else if(!hit[i]&&open){out+='</mark>';open=false}out+=h(c)});return out+(open?'</mark>':'')}
/* Modèle du plan : un nœud par onglet, section Sciences et titre h2/h3/h4, dans l'ordre du document. */
function MC_navModel(m){
 const roots=[],nodes=[],byKey=new Map();let uid=0;
 const add=(n,parent)=>{if(byKey.has(n.key))n.key+='~'+uid;n.id='mcnav-'+(uid++);n.parent=parent||null;n.children=[];n.level=parent?parent.level+1:1;
  (parent?parent.children:roots).push(n);nodes.push(n);byKey.set(n.key,n);n.norm=MC_navNorm((n.num?n.num+' ':'')+n.label);return n};
 m.querySelectorAll('.mc-tabs [data-p]').forEach(tab=>{
  const panel=document.getElementById(tab.dataset.p);if(!panel||!m.contains(panel))return;const p=tab.dataset.p;
  const tn=add({key:p,kind:'tab',num:'',label:MC_navClean(tab.textContent),tab:p,btn:tab,el:panel});
  const sciBtns=new Map(Array.from(panel.querySelectorAll('.mc-sci-bar [data-s]')).map(b=>[b.dataset.s,b]));
  let base=tn,sciEl=null,last=[],i=0;
  panel.querySelectorAll('.mc-ilot h2,.mc-ilot h3,.mc-ilot h4,.mc-sci>h2').forEach(hd=>{
   i++;const sci=sciBtns.size?hd.closest('.mc-sci'):null;
   if(sci&&sci!==sciEl){sciEl=sci;last=[];const own=sci.querySelector(':scope>h2'),s=own?MC_navSplit(own):null,b=sciBtns.get(sci.id);
    base=add({key:p+'~'+(sci.id||i),kind:'sci',num:s?s.num:'',label:s?s.label:MC_navClean(b?b.textContent:'Section'),tab:p,sci:sci.id,el:own||sci,heading:own||null,btn:b||null},tn)}
   else if(!sci&&sciEl){sciEl=null;base=tn;last=[]}
   if(base.heading===hd)return;
   const d={H2:0,H3:1,H4:2}[hd.tagName];let parent=base;for(let k=d-1;k>=0;k--)if(last[k]){parent=last[k];break}
   const s=MC_navSplit(hd);last[d]=add({key:hd.id||p+'-'+i,kind:'h',tag:hd.tagName.toLowerCase(),num:s.num,label:s.label,tab:p,sci:sci?sci.id:null,el:hd,heading:hd},parent);last.length=d+1;
  });
 });
 return {roots,nodes,byKey};
}
const MC_NAV_ICON={plan:'<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 6h2M9 6h11M4 12h2M9 12h11M4 18h2M9 18h11"/></svg>',
 pin:'<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M9 4h6l-1 6 3 3H7l3-3-1-6zM12 13v7"/></svg>',
 close:'<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6L6 18"/></svg>',
 find:'<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.5"/><path d="M16 16l4.5 4.5"/></svg>'};
function MC_navigoMount(m){
 const code=m.dataset.code,model=MC_navModel(m),reduce=MC_navReduce;
 const host=document.createElement('div');host.className='mc-navigo';host.dataset.navigo='2';
 host.innerHTML='<div class="mc-navigo-scrim" hidden></div><aside id="mc-navigo-panel" class="mc-navigo-panel" aria-labelledby="mc-navigo-heading" hidden>'+
  '<div class="mc-navigo-head"><div class="mc-navigo-headtext"><small id="mc-navigo-heading">Plan de la leçon</small><strong class="mc-navigo-title"></strong></div>'+
  '<button type="button" class="mc-navigo-pin" aria-pressed="false">'+MC_NAV_ICON.pin+'<span class="mc-navigo-sr">Épingler le plan à côté du texte</span></button>'+
  '<button type="button" class="mc-navigo-close" aria-label="Fermer le plan (Échap)">'+MC_NAV_ICON.close+'</button></div>'+
  '<div class="mc-navigo-reading"><div class="mc-navigo-where"><span class="mc-navigo-where-label">Position de lecture</span><span class="mc-navigo-where-text"></span><span class="mc-navigo-pct">0 %</span></div>'+
  '<div class="mc-navigo-progress" role="progressbar" aria-label="Position de lecture dans l’onglet" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0"><i></i></div></div>'+
  '<div class="mc-navigo-searchbox">'+MC_NAV_ICON.find+'<label class="mc-navigo-sr" for="mc-navigo-search">Rechercher une partie dans les quatre onglets</label>'+
  '<input id="mc-navigo-search" class="mc-navigo-search" type="search" placeholder="Rechercher un titre ou un numéro…" autocomplete="off" spellcheck="false" enterkeyhint="go" aria-controls="mc-navigo-tree" aria-describedby="mc-navigo-count"></div>'+
  '<ul id="mc-navigo-tree" class="mc-navigo-list" role="tree" aria-label="Plan : onglets, parties et sous-parties"></ul>'+
  '<div class="mc-navigo-foot"><span id="mc-navigo-count" class="mc-navigo-count" role="status"></span><span class="mc-navigo-keys" aria-hidden="true"><kbd>↑</kbd><kbd>↓</kbd> parcourir · <kbd>←</kbd><kbd>→</kbd> replier, déplier · <kbd>Entrée</kbd> aller</span></div></aside>';
 document.body.appendChild(host);
 const trigger=document.createElement('button');trigger.type='button';trigger.className='mc-navigo-trigger';trigger.dataset.navigo='2';
 trigger.setAttribute('aria-controls','mc-navigo-panel');trigger.setAttribute('aria-expanded','false');trigger.setAttribute('aria-keyshortcuts','N Control+K');
 trigger.setAttribute('aria-label','Navigo : plan de la leçon');trigger.title='Plan de la leçon (touche N ou Ctrl+K)';
 trigger.innerHTML=MC_NAV_ICON.plan+'<span class="mc-navigo-trigger-label" aria-hidden="true">Plan</span><span class="mc-navigo-trigger-pct" aria-hidden="true"></span>';
 const $=s=>host.querySelector(s),panel=$('.mc-navigo-panel'),scrim=$('.mc-navigo-scrim'),tree=$('.mc-navigo-list'),search=$('.mc-navigo-search'),
  pin=$('.mc-navigo-pin'),close=$('.mc-navigo-close'),count=$('.mc-navigo-count'),whereText=$('.mc-navigo-where-text'),pct=$('.mc-navigo-pct'),bar=$('.mc-navigo-progress');
 const st={mode:'',open:false,current:null,manual:new Map(),focusKey:null,pending:false,terms:[],hold:null,hover:false,last:''};
 const path=new Set();
 const tabNow=()=>{const t=m.querySelector('.mc-tabs [data-p][aria-selected="true"]');return t?t.dataset.p:(model.roots[0]||{}).key};
 const setPath=()=>{path.clear();for(let n=st.current&&model.byKey.get(st.current);n;n=n.parent)path.add(n.key)};
 const isOpen=n=>n.children.length>0&&(st.manual.has(n.key)?st.manual.get(n.key):(n.kind==='tab'?n.key===tabNow():path.has(n.key)));
 const rows=()=>Array.from(tree.querySelectorAll('[role="treeitem"]'));
 const findLi=k=>k?tree.querySelector('[role="treeitem"][data-key="'+CSS.escape(k)+'"]'):null;
 const firstHeading=n=>{if(n.heading)return n;for(const c of n.children){const x=firstHeading(c);if(x)return x}return null};
 const target=n=>firstHeading(n)||n;
 const partsOf=n=>{let a=0,b=0;const walk=x=>x.children.forEach(c=>{if(c.kind==='h'){if(c.tag==='h2')a++;else b++}walk(c)});walk(n);return {a,b}};
 const trail=n=>{const t=[];for(let x=n.parent;x;x=x.parent)t.unshift((x.num?x.num+' ':'')+x.label);return t.join(' › ')};
 const engaged=()=>st.hover||(tree.contains(document.activeElement));
 function item(n,o){
  const li=document.createElement('li');li.setAttribute('role','treeitem');li.className='mc-navigo-node';li.dataset.key=n.key;li.id=n.id;li.tabIndex=-1;
  li.setAttribute('aria-level',o.flat?'1':String(n.level));li.setAttribute('aria-setsize',String(o.size));li.setAttribute('aria-posinset',String(o.pos));
  li.setAttribute('aria-labelledby',(n.num?n.id+'-n ':'')+n.id+'-l');if(o.flat)li.setAttribute('aria-describedby',n.id+'-p');
  if(!o.flat&&n.children.length)li.setAttribute('aria-expanded',String(isOpen(n)));
  if(n.key===st.current)li.setAttribute('aria-current','location');else if(!o.flat&&path.has(n.key))li.classList.add('is-path');
  if(n.kind==='tab'&&n.key===tabNow())li.classList.add('is-tab-active');
  const r=document.createElement('div');r.className='mc-navigo-item mc-navigo-'+(n.kind==='h'?n.tag:n.kind);r.dataset.key=n.key;
  let html=o.flat?'':'<span class="mc-navigo-twisty"'+(n.children.length?' data-toggle title="'+(isOpen(n)?'Replier':'Déplier')+'"':'')+' aria-hidden="true"></span>';
  if(n.num)html+='<span class="mc-navigo-num" id="'+n.id+'-n">'+MC_navMark(n.num,o.terms)+'</span>';
  html+='<span class="mc-navigo-text"><span class="mc-navigo-label" id="'+n.id+'-l">'+MC_navMark(n.label,o.terms)+'</span>'+(o.flat?'<span class="mc-navigo-path" id="'+n.id+'-p">'+h(trail(n))+'</span>':'')+'</span>';
  if(n.kind==='tab'){const c=partsOf(n);html+='<span class="mc-navigo-badge" aria-hidden="true" title="'+c.a+' parties">'+c.a+'</span>'}
  r.innerHTML=html;li.appendChild(r);return li}
 function roving(){const list=rows();const k=findLi(st.focusKey)||tree.querySelector('[aria-current]')||tree.querySelector('.is-path:not(.is-tab-active)')||list[0];list.forEach(li=>{li.tabIndex=li===k?0:-1})}
 function clamp(){tree.querySelectorAll('.mc-navigo-item').forEach(r=>{const l=r.querySelector('.mc-navigo-label');if(!l)return;const n=model.byKey.get(r.dataset.key);
  if(l.scrollHeight>l.clientHeight+1||l.scrollWidth>l.clientWidth+1)r.title=(n.num?n.num+' ':'')+n.label;else r.removeAttribute('title')})}
 function render(){
  st.pending=false;const had=tree.contains(document.activeElement)?document.activeElement.closest('[role="treeitem"]'):null,hadKey=had&&had.dataset.key;
  st.terms=MC_navNorm(search.value).split(/\s+/).filter(Boolean);const frag=document.createDocumentFragment();
  if(st.terms.length){
   const hits=model.nodes.filter(n=>n.kind!=='tab'&&st.terms.every(t=>n.norm.includes(t)));
   hits.forEach((n,i)=>frag.appendChild(item(n,{flat:true,pos:i+1,size:hits.length,terms:st.terms})));
   const total=model.nodes.length-model.roots.length;
   count.textContent=hits.length?hits.length+' résultat'+(hits.length>1?'s':'')+' sur '+total+' titres, dans les quatre onglets':'Aucun titre ne correspond. Essayez un autre mot ou un numéro, par exemple « 2.1 ».';
   tree.classList.add('is-search');
  }else{
   const build=(list,el)=>list.forEach((n,i)=>{const li=item(n,{pos:i+1,size:list.length});el.appendChild(li);
    if(isOpen(n)){const g=document.createElement('ul');g.setAttribute('role','group');g.className='mc-navigo-group';build(n.children,g);li.appendChild(g)}});
   build(model.roots,frag);tree.classList.remove('is-search');
   const t=model.byKey.get(tabNow());if(t){const c=partsOf(t);count.textContent=t.label+' : '+c.a+' partie'+(c.a>1?'s':'')+(c.b?', '+c.b+' sous-partie'+(c.b>1?'s':''):'')}
  }
  tree.classList.toggle('is-empty',!frag.childNodes.length);tree.replaceChildren(frag);roving();
  if(hadKey){let li=findLi(hadKey);for(let n=model.byKey.get(hadKey);!li&&n;n=n.parent)li=findLi(n.key);(li||rows()[0]||search).focus({preventScroll:true})}
  requestAnimationFrame(clamp);
 }
 function showRow(li,mid){if(!li)return;const r=(li.querySelector('.mc-navigo-item')||li).getBoundingClientRect(),box=tree.getBoundingClientRect();if(!box.height)return;
  if(mid||r.top<box.top+6||r.bottom>box.bottom-6)tree.scrollTop+=mid?r.top-box.top-(box.height-r.height)/2:(r.top<box.top+6?r.top-box.top-6:r.bottom-box.bottom+6)}
 const reveal=mid=>showRow(tree.querySelector('[aria-current]')||tree.querySelector('.is-path:not(.is-tab-active)'),mid);
 function focusEl(el){if(!el)return;if(!el.hasAttribute('tabindex'))el.setAttribute('tabindex','-1');MC_NAV_JUMP=true;try{el.focus({preventScroll:true})}finally{MC_NAV_JUMP=false}}
 const body=()=>m.querySelector('.mc-panel:not([hidden]) .mc-body');
 const hashWith=key=>{const raw=location.hash||'#/entry/'+code,i=raw.indexOf('?'),head=i<0?raw:raw.slice(0,i),q=new URLSearchParams(i<0?'':raw.slice(i+1));if(key)q.set('nav',key);else q.delete('nav');const s=q.toString();return head+(s?'?'+s:'')};
 function pushUrl(key,before){try{const old=history.state&&typeof history.state==='object'?history.state:{};history.replaceState(Object.assign({},old,{mcNav:{code,y:before.y,left:before.left,tab:before.tab,key:old.mcNav?old.mcNav.key:null}}),'');
  const next=hashWith(key);if(next!==location.hash)history.pushState({mcNav:{code,key}},'',next)}catch(e){}}
 /* Saut : onglet et section Sciences ouverts si besoin, page du mode Livre, puis défilement vertical sous les barres. */
 function jump(n,o={}){
  const t=target(n),el=t.heading||t.el,smooth=!o.instant&&!reduce();if(!el)return;
  const before={y:Math.round(scrollY),tab:tabNow(),left:body()?Math.round(body().scrollLeft):0};
  const tab=model.byKey.get(n.tab);if(tab&&tab.btn.getAttribute('aria-selected')!=='true')tab.btn.click();
  const sci=el.closest('.mc-sci');if(sci&&sci.hidden){const b=m.querySelector('.mc-sci-bar [data-s="'+CSS.escape(sci.id)+'"]');if(b)b.click()}
  st.current=t.key;setPath();st.hold={key:t.key,until:performance.now()+(smooth?1100:250)};setTimeout(track,smooth?1150:300);
  focusEl(el);
  const vertical=()=>{const y=scrollY+el.getBoundingClientRect().top-MC_navOffset(m);scrollTo({top:Math.max(0,Math.round(y)),behavior:smooth?'smooth':'auto'});focusEl(el)};
  const land=()=>{const b=el.closest('.mc-body');
   if(m.classList.contains('book')&&b&&b.scrollWidth>b.clientWidth+2){const page=Array.from(b.children).find(x=>x.contains(el));
    if(page){const dx=page.getBoundingClientRect().left-b.getBoundingClientRect().left;if(Math.abs(dx)>2){let tm=0;const done=()=>{b.removeEventListener('scrollend',done);clearTimeout(tm);if(m._mcPagerUpdate)m._mcPagerUpdate();requestAnimationFrame(vertical)};
     b.addEventListener('scrollend',done);tm=setTimeout(done,smooth?700:80);b.scrollTo({left:b.scrollLeft+dx,behavior:smooth?'smooth':'auto'});return}}}
   vertical()};
  requestAnimationFrame(()=>requestAnimationFrame(land));
  if(o.push!==false)pushUrl(t.key,before);
  if(!panel.hidden&&!engaged())render();else st.pending=true;
 }
 function activate(n){st.focusKey=n.key;if(st.mode!=='pinned'&&st.open)setOpen(false,{restore:false});jump(n)}
 function setOpen(on,o={}){
  if(st.mode==='pinned'){panel.hidden=false;return}
  st.open=on;panel.hidden=!on;scrim.hidden=!on;trigger.setAttribute('aria-expanded',String(on));
  if(on)document.body.setAttribute('data-mc-navigo-open','');else document.body.removeAttribute('data-mc-navigo-open');
  if(on){search.value='';st.focusKey=null;render();update();requestAnimationFrame(()=>{reveal(true);
    const touch=st.mode==='sheet'||matchMedia('(pointer: coarse)').matches;
    if(o.focus==='search'||(!touch&&o.focus!=='tree'))search.focus({preventScroll:true});else (tree.querySelector('[tabindex="0"]')||search).focus({preventScroll:true})})}
  else if(o.restore!==false&&trigger.isConnected)trigger.focus({preventScroll:true});
 }
 const focusables=()=>[pin,close,search,tree.querySelector('[role="treeitem"][tabindex="0"]')].filter(x=>x&&x.getClientRects().length&&!x.disabled);
 function applyMode(){
  const w=innerWidth,pref=MC.store.get('navigo.pin',null);
  const mode=w>=MC_NAV_PIN_MIN&&(pref===null?w>=MC_NAV_PIN_DEFAULT:!!pref)?'pinned':(w<=MC_NAV_SHEET_MAX?'sheet':'drawer');
  const slot=mode==='sheet'?null:document.querySelector('.topbar .top-actions');
  if(slot&&slot.getClientRects().length){if(trigger.parentElement!==slot)slot.prepend(trigger);trigger.classList.add('is-docked')}
  else{if(trigger.parentElement!==host)host.prepend(trigger);trigger.classList.remove('is-docked')}
  const was=st.mode;st.mode=mode;document.body.dataset.mcNavigo=mode;
  const pinned=mode==='pinned',label=pinned?'Détacher le plan : le ranger dans un tiroir':'Épingler le plan à côté du texte';
  pin.setAttribute('aria-pressed',String(pinned));pin.title=label;pin.querySelector('.mc-navigo-sr').textContent=label;
  if(pinned){panel.hidden=false;scrim.hidden=true;panel.removeAttribute('role');panel.removeAttribute('aria-modal');st.open=true;trigger.setAttribute('aria-expanded','true');document.body.removeAttribute('data-mc-navigo-open');
   if(was!=='pinned'){render();update();requestAnimationFrame(()=>reveal(true))}}
  else{panel.setAttribute('role','dialog');panel.setAttribute('aria-modal','true');
   if(was==='pinned'||!was){st.open=false;panel.hidden=true;scrim.hidden=true;trigger.setAttribute('aria-expanded','false');document.body.removeAttribute('data-mc-navigo-open')}}
 }
 /* Suivi de lecture : titre courant = dernier titre passé sous les barres collantes. */
 let raf=0;const track=()=>{if(!raf)raf=requestAnimationFrame(update)};
 function update(){raf=0;if(!m.isConnected)return;const t=tabNow(),off=MC_navOffset(m);if(st.off!==off){st.off=off;document.documentElement.style.setProperty('--mc-nav-offset',off+'px')}
  const b=m.classList.contains('book')?body():null,bl=b&&b.scrollWidth>b.clientWidth+2?b.getBoundingClientRect():null;
  const atEnd=innerHeight+scrollY>=document.documentElement.scrollHeight-4;let cur=null,first=null;
  for(const n of model.nodes){if(n.tab!==t||!n.heading)continue;const r=n.heading.getBoundingClientRect();if(!r.height)continue;
   if(bl&&(r.right<=bl.left+1||r.left>=bl.right-1))continue;if(!first)first=n;
   if(r.top<=off+8||(atEnd&&r.top<innerHeight*.55))cur=n;else if(!bl&&!atEnd)break}
  cur=cur||first;
  if(st.hold){const now=performance.now(),pos=Math.round(scrollY)+':'+(b?Math.round(b.scrollLeft):0),held=model.byKey.get(st.hold.key);
   if(now<st.hold.until)cur=held||cur;else if(st.hold.pos===undefined){st.hold.pos=pos;cur=held||cur}else if(st.hold.pos===pos)cur=held||cur;else st.hold=null}
  const key=cur?cur.key:null;
  if(key!==st.current){st.current=key;setPath();if(!panel.hidden){if(engaged()||st.terms.length){tree.querySelectorAll('[aria-current]').forEach(x=>x.removeAttribute('aria-current'));const li=findLi(key);if(li)li.setAttribute('aria-current','location');st.pending=!st.terms.length}else{render();reveal(false)}}}
  let p=0;if(bl)p=b.scrollLeft/Math.max(1,b.scrollWidth-b.clientWidth);else{const pn=m.querySelector('.mc-panel:not([hidden])');if(pn){const r=pn.getBoundingClientRect();p=(off-r.top)/Math.max(1,r.height-(innerHeight-off))}}
  const v=Math.round(Math.min(1,Math.max(0,p))*100);
  let where='';if(cur){let top=cur;while(top.parent&&top.parent.kind==='h')top=top.parent;const sibs=top.parent?top.parent.children.filter(x=>x.kind==='h'):[];const tl=model.byKey.get(t);
   where=(tl?tl.label:'')+(top.parent&&top.parent.kind==='sci'?' · '+top.parent.label:'')+(sibs.length?' · partie '+(sibs.indexOf(top)+1)+' sur '+sibs.length:'')}
  const sig=v+'|'+where;if(sig!==st.last){st.last=sig;bar.setAttribute('aria-valuenow',String(v));bar.setAttribute('aria-valuetext',v+' %'+(where?', '+where:''));bar.style.setProperty('--mc-nav-read',String(v/100));
   pct.textContent=v+' %';whereText.textContent=where;trigger.querySelector('.mc-navigo-trigger-pct').textContent=v+' %'}
 }
 /* Clavier de l'arbre : ↑ ↓ Début Fin, → déplie ou entre, ← replie ou remonte, Entrée et Espace sautent, lettre = recherche rapide. */
 tree.addEventListener('keydown',ev=>{const li=ev.target.closest('[role="treeitem"]');if(!li||ev.altKey||ev.ctrlKey||ev.metaKey)return;const n=model.byKey.get(li.dataset.key);if(!n)return;
  const list=rows(),i=list.indexOf(li),flat=st.terms.length>0;
  const go=x=>{ev.preventDefault();if(!x)return;st.focusKey=x.dataset.key;list.forEach(y=>{y.tabIndex=y===x?0:-1});x.focus({preventScroll:true});showRow(x)};
  switch(ev.key){
   case 'ArrowDown':go(list[i+1]);break;
   case 'ArrowUp':if(i===0){ev.preventDefault();search.focus()}else go(list[i-1]);break;
   case 'Home':go(list[0]);break;
   case 'End':go(list[list.length-1]);break;
   case 'ArrowRight':ev.preventDefault();if(flat||!n.children.length)break;if(!isOpen(n)){st.manual.set(n.key,true);st.focusKey=n.key;render()}else go(findLi(n.children[0].key));break;
   case 'ArrowLeft':ev.preventDefault();if(flat)break;if(n.children.length&&isOpen(n)){st.manual.set(n.key,false);st.focusKey=n.key;render()}else if(n.parent)go(findLi(n.parent.key));break;
   case 'Enter':case ' ':ev.preventDefault();activate(n);break;
   default:if(ev.key.length===1&&/\S/.test(ev.key)){const c=MC_navNorm(ev.key),order=list.slice(i+1).concat(list.slice(0,i+1));
    const x=order.find(y=>{const k=model.byKey.get(y.dataset.key);return k&&(MC_navNorm(k.label).startsWith(c)||k.num.startsWith(c))});if(x)go(x)}}
 });
 tree.addEventListener('click',ev=>{const r=ev.target.closest('.mc-navigo-item');if(!r)return;ev.stopPropagation();const n=model.byKey.get(r.dataset.key);if(!n)return;
  if(ev.target.closest('[data-toggle]')){st.manual.set(n.key,!isOpen(n));st.focusKey=n.key;render();const li=findLi(n.key);if(li)li.focus({preventScroll:true});return}
  activate(n)});
 tree.addEventListener('focusin',ev=>{const li=ev.target.closest('[role="treeitem"]');if(li)st.focusKey=li.dataset.key});
 panel.addEventListener('pointerenter',ev=>{if(ev.pointerType==='mouse')st.hover=true});
 panel.addEventListener('pointerleave',()=>{st.hover=false;if(st.pending&&!engaged()){render();reveal(false)}});
 panel.addEventListener('focusout',ev=>{if(!panel.contains(ev.relatedTarget)&&st.pending&&!st.hover)setTimeout(()=>{if(st.pending&&!engaged())render()},0)});
 panel.addEventListener('keydown',ev=>{if(ev.key!=='Tab'||st.mode==='pinned')return;const f=focusables();if(!f.length)return;const i=f.indexOf(document.activeElement);
  if(ev.shiftKey&&i<=0){ev.preventDefault();f[f.length-1].focus()}else if(!ev.shiftKey&&i===f.length-1){ev.preventDefault();f[0].focus()}});
 search.addEventListener('input',()=>{st.focusKey=null;render();tree.scrollTop=0});
 search.addEventListener('keydown',ev=>{const f=rows()[0];if(!f)return;if(ev.key==='ArrowDown'){ev.preventDefault();rows().forEach(y=>{y.tabIndex=y===f?0:-1});f.focus()}else if(ev.key==='Enter'){ev.preventDefault();activate(model.byKey.get(f.dataset.key))}});
 trigger.addEventListener('click',()=>{if(st.mode==='pinned'){render();(tree.querySelector('[tabindex="0"]')||search).focus({preventScroll:true});return}setOpen(!st.open)});
 close.addEventListener('click',()=>setOpen(false));
 pin.addEventListener('click',()=>{const was=st.mode==='pinned';MC.store.set('navigo.pin',!was);applyMode();if(was&&st.mode!=='pinned')trigger.focus({preventScroll:true});else pin.focus({preventScroll:true})});
 const onKey=ev=>{
  if(ev.key==='Escape'){
   if(ev.target===search&&search.value){ev.preventDefault();search.value='';render();return}
   if(st.mode!=='pinned'&&st.open){ev.preventDefault();setOpen(false);return}
   if(st.mode==='pinned'&&panel.contains(ev.target)){ev.preventDefault();const n=model.byKey.get(st.current);focusEl(n&&(n.heading||n.el))}
   return}
  if(ev.defaultPrevented||ev.altKey||document.querySelector('dialog[open]'))return;
  const k=ev.key.toLowerCase(),editable=ev.target.closest&&ev.target.closest('input,textarea,select,[contenteditable]:not([contenteditable="false"])');
  if((ev.ctrlKey||ev.metaKey)&&!ev.shiftKey&&k==='k'){ev.preventDefault();if(st.mode==='pinned'){render();search.focus()}else if(!st.open)setOpen(true,{focus:'search'});else search.focus();return}
  if(k==='n'&&!ev.ctrlKey&&!ev.metaKey&&!editable&&!host.contains(ev.target)){ev.preventDefault();if(st.mode==='pinned'){render();(tree.querySelector('[tabindex="0"]')||search).focus({preventScroll:true})}else setOpen(!st.open)}
 };
 const outside=ev=>{if(st.mode==='pinned'||!st.open||panel.contains(ev.target)||trigger.contains(ev.target))return;setOpen(false,{restore:false})};
 const trapIn=ev=>{if(st.mode==='pinned'||!st.open||panel.contains(ev.target)||ev.target===trigger||(ev.target.closest&&ev.target.closest('dialog')))return;const f=focusables();if(f[0])f[0].focus({preventScroll:true})};
 document.addEventListener('keydown',onKey,true);document.addEventListener('pointerdown',outside,true);document.addEventListener('focusin',trapIn);
 addEventListener('scroll',track,{passive:true,capture:true});addEventListener('resize',track,{passive:true});
 const mqs=['(min-width:761px)','(min-width:'+MC_NAV_PIN_MIN+'px)','(min-width:'+MC_NAV_PIN_DEFAULT+'px)'].map(q=>matchMedia(q));mqs.forEach(q=>q.addEventListener('change',applyMode));
 const syncFont=()=>{host.style.setProperty('--mc-font',m.style.getPropertyValue('--mc-font'));host.style.setProperty('--mc-scale',m.style.getPropertyValue('--mc-scale')||'1');requestAnimationFrame(clamp)};
 const moSelf=new MutationObserver(()=>{syncFont();st.hold=null;track()});moSelf.observe(m,{attributes:true,attributeFilter:['class','style']});
 const moTabs=new MutationObserver(list=>{if(!list.some(r=>r.target.matches&&r.target.matches('.mc-panel,.mc-sci')))return;if(!st.hold)st.current=null;if(!st.terms.length&&!engaged())render();else st.pending=true;track()});
 moTabs.observe(m,{attributes:true,subtree:true,attributeFilter:['hidden']});
 const content=document.getElementById('content'),moContent=new MutationObserver(()=>{if(!m.isConnected)MC_navigoDestroy()});if(content)moContent.observe(content,{childList:true});
 /* Retour arrière : un changement limité à « ?nav= » dans la même leçon ne reconstruit pas la page. */
 const own=ev=>{try{const split=u=>{const s=new URL(u).hash,i=s.indexOf('?'),q=new URLSearchParams(i<0?'':s.slice(i+1));q.delete('nav');q.sort();return [i<0?s:s.slice(0,i),q.toString()]};
  const a=split(ev.oldURL),b=split(ev.newURL),mm=b[0].match(/^#\/entry\/([^/?]+)$/);return a[0]===b[0]&&a[1]===b[1]&&!!mm&&MC_code(decodeURIComponent(mm[1]))===code}catch(e){return false}};
 const restore=()=>{const s=history.state&&history.state.mcNav,key=new URLSearchParams((location.hash.split('?')[1])||'').get('nav');
  if(s&&s.code===code&&typeof s.y==='number'){const tab=s.tab&&model.byKey.get(s.tab);if(tab&&tab.btn.getAttribute('aria-selected')!=='true')tab.btn.click();st.hold=null;
   requestAnimationFrame(()=>requestAnimationFrame(()=>{const b=body();if(b&&m.classList.contains('book'))b.scrollLeft=s.left||0;scrollTo({top:s.y,behavior:'auto'});track()}))}
  else if(key&&model.byKey.get(key))jump(model.byKey.get(key),{push:false,instant:true});
  else{st.hold=null;scrollTo({top:0,behavior:'auto'});track()}};
 const api={code,own,restore,open:on=>setOpen(on)};MC_NAV_API=api;
 MC_NAV_CLEANUP=()=>{moSelf.disconnect();moTabs.disconnect();moContent.disconnect();mqs.forEach(q=>q.removeEventListener('change',applyMode));
  document.removeEventListener('keydown',onKey,true);document.removeEventListener('pointerdown',outside,true);document.removeEventListener('focusin',trapIn);
  removeEventListener('scroll',track,{capture:true});removeEventListener('resize',track);if(raf)cancelAnimationFrame(raf);
  trigger.remove();host.remove();delete document.body.dataset.mcNavigo;document.body.removeAttribute('data-mc-navigo-open');if(MC_NAV_API===api)MC_NAV_API=null};
 host.querySelector('.mc-navigo-title').textContent=(m.querySelector('.mc-chap-head h1')||{}).textContent?.replace(/\s+/g,' ').trim()||'Cours';
 syncFont();applyMode();render();update();
 /* Lien partagé ou rechargement : « ?nav= » ramène au titre demandé. */
 const initial=new URLSearchParams((location.hash.split('?')[1])||'').get('nav');
 if(initial&&model.byKey.get(initial))setTimeout(()=>{if(m.isConnected)jump(model.byKey.get(initial),{push:false,instant:true})},60);
 return ()=>{syncFont();if(!st.terms.length&&!engaged())render();track()};
}
window.MC_NAVIGO_PREMIUM=MC_navigoMount;
addEventListener('hashchange',ev=>{if(MC_NAV_API&&MC_NAV_API.own(ev)){ev.stopImmediatePropagation();MC_NAV_API.restore()}},true);
function MEDINA_mount(){MC_badges();MC_navigoDestroy();if(MC_SIZE_CLEANUP){MC_SIZE_CLEANUP();MC_SIZE_CLEANUP=null}
 const m=document.querySelector('.mc');document.documentElement.dataset.medinaActiveCycle=(window.MEDINA_CYCLE_COURSES||[]).includes(m?.dataset.code)?'1':'';if(!m)return;const code=m.dataset.code;
 let navRefresh=()=>{};
 const applyFont=()=>{const f=MC.store.get('font.'+code,MC.store.get('font.default',"'Atkinson Hyperlegible Next','Atkinson Hyperlegible',system-ui,sans-serif"));const s=Math.min(24,Math.max(14,Number(MC.store.get('fs.'+code,17))||17));m.style.setProperty('--mc-font',f);m.style.setProperty('--mc-fs',s+'px');m.style.setProperty('--mc-scale',(s/17).toFixed(3));m.querySelector('.mc-font').value=f;m.querySelector('.mc-size-range').value=s;m.querySelector('.mc-size-value').textContent=s+' px';document.documentElement.style.setProperty('--mc-font',f);document.documentElement.style.setProperty('--mc-scale',(s/17).toFixed(3));navRefresh()};
 m.querySelector('.mc-font').onchange=ev=>{MC.store.set('font.'+code,ev.target.value);MC.store.set('font.default',ev.target.value);applyFont()};
 m.querySelector('.mc-fsdn').onclick=()=>{MC.store.set('fs.'+code,Math.max(14,MC.store.get('fs.'+code,17)-1));applyFont()};
 m.querySelector('.mc-fsup').onclick=()=>{MC.store.set('fs.'+code,Math.min(24,MC.store.get('fs.'+code,17)+1));applyFont()};
 m.querySelector('.mc-size-range').oninput=ev=>{MC.store.set('fs.'+code,Number(ev.target.value));applyFont()};
 m.querySelector('.mc-size-reset').onclick=()=>{MC.store.set('fs.'+code,17);applyFont()};
 const sizeButton=m.querySelector('.mc-size-toggle'),sizePop=m.querySelector('.mc-size-pop');sizeButton.onclick=()=>{sizePop.hidden=!sizePop.hidden;sizeButton.setAttribute('aria-expanded',String(!sizePop.hidden));if(!sizePop.hidden)m.querySelector('.mc-size-range').focus()};
 const closeSize=()=>{sizePop.hidden=true;sizeButton.setAttribute('aria-expanded','false')};
 const sizeOutside=e=>{if(!m.isConnected||!m.querySelector('.mc-size-wrap').contains(e.target))closeSize()};
 const sizeEscape=e=>{if(e.key==='Escape'&&!sizePop.hidden){closeSize();sizeButton.focus({preventScroll:true})}};
 document.addEventListener('pointerdown',sizeOutside);document.addEventListener('keydown',sizeEscape);
 MC_SIZE_CLEANUP=()=>{document.removeEventListener('pointerdown',sizeOutside);document.removeEventListener('keydown',sizeEscape)};
 /* Panneau sans pagination (onglet Sciences de certains cours) : le moteur ajoute la sienne, visible en mode Livre seulement. */
 m.querySelectorAll('.mc-panel').forEach(p=>{if(p.querySelector('.mc-body')&&!p.querySelector('.mc-pager')){const d=document.createElement('div');d.className='mc-pager mc-ui';d.innerHTML='<button type="button" class="mc-prev">← Îlot précédent</button><span></span><button type="button" class="mc-next">Îlot suivant →</button>';p.appendChild(d)}});
 const bookBtn=m.querySelector('.mc-book');const setBook=on=>{m.classList.toggle('book',on);bookBtn.setAttribute('aria-pressed',on);MC.store.set('book',on);MC_bookAnnex(m,on);pager()};
 bookBtn.onclick=()=>setBook(!m.classList.contains('book'));
 const body=()=>m.querySelector('.mc-panel:not([hidden]) .mc-body');
 /* Mode Livre : le document reste la seule zone de défilement vertical ; la hauteur du livre suit la page affichée. */
 let fitObs=null;
 function pager(){if(fitObs){fitObs.disconnect();fitObs=null}m.querySelectorAll('.mc-body').forEach(x=>x.style.height='');
  const b=body();const pg=m.querySelector('.mc-panel:not([hidden]) .mc-pager');if(!b||!pg)return;
  const book=m.classList.contains('book'),sci=b.classList.contains('mc-sci-body');
  const pages=()=>Array.from(b.children).filter(c=>c.matches('.mc-ilot,.mc-sci')&&!c.hidden);
  const sciBtns=()=>Array.from(b.parentElement.querySelectorAll('.mc-sci-bar button[data-s]'));
  const step=()=>{const child=pages()[0];const gap=parseFloat(getComputedStyle(b).columnGap)||0;return child?child.getBoundingClientRect().width+gap:b.clientWidth};
  const tabList=Array.from(m.querySelectorAll('.mc-tabs button[data-p]'));const tabIdx=tabList.findIndex(t=>t.getAttribute('aria-selected')==='true');
  const prev=pg.querySelector('.mc-prev'),next=pg.querySelector('.mc-next'),out=pg.querySelector('span');
  [prev,next].forEach(x=>{if(!x.dataset.label)x.dataset.label=x.textContent;x.type='button'});
  const state=()=>{if(sci){const l=sciBtns();return {n:l.length,i:Math.max(0,l.findIndex(x=>x.getAttribute('aria-selected')==='true'))}}
   const n=pages().length,max=b.scrollWidth-b.clientWidth;const i=b.scrollLeft>=max-2?n-1:Math.min(n-1,Math.max(0,Math.round(b.scrollLeft/Math.max(1,step()))));return {n,i}};
  const fit=()=>{if(!book||sci)return;const bl=b.getBoundingClientRect().left,w=b.clientWidth;let h=0;
   pages().forEach(p=>{const r=p.getBoundingClientRect();if(r.right>bl+1&&r.left<bl+w-1)h=Math.max(h,p.offsetHeight)});
   if(h){const cs=getComputedStyle(b);b.style.height=(cs.boxSizing==='border-box'?h+parseFloat(cs.paddingTop)+parseFloat(cs.paddingBottom):h)+'px'}};
  const setBtn=(x,tab,dir)=>{const end=x.dataset.edge==='1';x.classList.toggle('mc-pager-tab',!!tab);
   if(tab){const name=tab.textContent.replace(/^[^\p{L}\p{N}]+/u,'').trim();x.textContent=dir<0?'← Onglet précédent':'Onglet suivant →';x.title=(dir<0?'Onglet précédent : ':'Onglet suivant : ')+name;x.setAttribute('aria-label',x.title);x.disabled=false;x.removeAttribute('aria-disabled')}
   else{x.textContent=x.dataset.label;x.removeAttribute('title');x.removeAttribute('aria-label');x.disabled=end;if(end)x.setAttribute('aria-disabled','true');else x.removeAttribute('aria-disabled')}};
  const upd=()=>{const {n,i}=state();out.textContent=n?(i+1)+' / '+n:'';
   const atStart=i<=0,atEnd=i>=n-1;prev.dataset.edge=atStart?'1':'';next.dataset.edge=atEnd?'1':'';
   setBtn(prev,atStart&&tabIdx>0?tabList[tabIdx-1]:null,-1);setBtn(next,atEnd&&tabIdx<tabList.length-1?tabList[tabIdx+1]:null,1);fit()};
  const reveal=()=>{if(b.getBoundingClientRect().top<0)b.scrollIntoView({block:'start',behavior:'smooth'})};
  const go=dir=>{const btn=dir<0?prev:next;if(btn.disabled)return;
   if(btn.classList.contains('mc-pager-tab')){const t=tabList[tabIdx+dir];t.click();const nb=body();if(nb){const l=Array.from(nb.parentElement.querySelectorAll('.mc-sci-bar button[data-s]'));if(nb.classList.contains('mc-sci-body'))(dir<0?l[l.length-1]:l[0])?.click();else nb.scrollLeft=dir<0?nb.scrollWidth:0;m._mcPagerUpdate?.();if(nb.getBoundingClientRect().top<0||nb.getBoundingClientRect().top>innerHeight*.6)nb.scrollIntoView({block:'start'})}(dir<0?m.querySelector('.mc-panel:not([hidden]) .mc-prev'):m.querySelector('.mc-panel:not([hidden]) .mc-next'))?.focus({preventScroll:true});return}
   if(sci){const l=sciBtns(),{i}=state();l[i+dir]?.click();upd();reveal();return}
   b.scrollBy({left:dir*step(),behavior:'smooth'});reveal()};
  m._mcPagerGo=go;m._mcPagerUpdate=upd;
  b.onscroll=upd;b.onscrollend=()=>{upd();fit()};prev.onclick=()=>go(-1);next.onclick=()=>go(1);
  if(book&&!sci&&'ResizeObserver' in window){fitObs=new ResizeObserver(()=>fit());pages().forEach(p=>fitObs.observe(p))}
  upd()}
 const tabs=m.querySelectorAll('.mc-tabs button');tabs.forEach(b=>b.onclick=()=>{tabs.forEach(x=>x.setAttribute('aria-selected',x===b));m.querySelectorAll('.mc-panel').forEach(p=>p.hidden=p.id!==b.dataset.p);MC.store.set('tab.'+code,b.dataset.p);pager();navRefresh()});
 const lt=MC.store.get('tab.'+code,null);const tb=lt&&m.querySelector(`.mc-tabs button[data-p="${lt}"]`);if(tb)tb.click();
 const sb=m.querySelectorAll('.mc-sci-bar button');sb.forEach(b=>b.onclick=()=>{sb.forEach(x=>x.setAttribute('aria-selected',x===b));m.querySelectorAll('.mc-sci').forEach(p=>p.hidden=p.id!==b.dataset.s);
  const sbody=m.querySelector('.mc-sci-body'),target=m.querySelector('#'+b.dataset.s);if(m.classList.contains('book')&&sbody&&target){sbody.scrollTo({left:sbody.scrollLeft+target.getBoundingClientRect().left-sbody.getBoundingClientRect().left})}m._mcPagerUpdate?.();navRefresh()});
 if(sb[0])sb[0].click();
 applyFont();setBook(MC.store.get('book',false));MC_quiz(m);navRefresh=MC_navigoMount(m);navRefresh();
}
/* Mode Livre : la touche Pareto et les sources de fin de partie rejoignent la dernière page au lieu de former des colonnes écrasées. */
function MC_bookAnnex(m,on){m.querySelectorAll('.mc-body').forEach(b=>{
 if(on){const all=Array.from(b.children),pages=all.filter(c=>c.matches('.mc-ilot,.mc-sci')),extra=all.filter(c=>!pages.includes(c));if(!extra.length||!pages.length)return;
  const sci=b.classList.contains('mc-sci-body');let host;if(sci){host=document.createElement('div');host.className='mc-book-annex';b.after(host)}else host=pages[pages.length-1];
  b._mcAnnex=extra;extra.forEach(x=>{x.dataset.mcAnnex='1';host.appendChild(x)});b._mcAnnexHost=sci?host:null}
 else if(b._mcAnnex){b._mcAnnex.forEach(x=>{delete x.dataset.mcAnnex;b.appendChild(x)});b._mcAnnexHost?.remove();b._mcAnnex=null;b._mcAnnexHost=null}})}
/* Mode Livre : un titre ciblé (Navigo, renvoi) est amené dans la vue par le défilement unique du document. */
document.addEventListener('focusin',ev=>{const t=ev.target;if(MC_NAV_JUMP||!t.matches?.('h2,h3,h4')||!t.closest('.mc.book .mc-body'))return;
 requestAnimationFrame(()=>{t.closest('.mc')?._mcPagerUpdate?.();requestAnimationFrame(()=>t.scrollIntoView({block:'start',inline:'nearest',behavior:MC_navReduce()?'auto':'smooth'}))})});
function MC_quiz(root){root.querySelectorAll('.mc-quiz').forEach(q=>q.querySelectorAll('.mc-opt').forEach(o=>o.onclick=ev=>{if(ev.target.closest('[data-ab]'))return;q.querySelectorAll('.mc-opt').forEach(x=>x.classList.toggle('ok',x.dataset.ok==='1'));if(o.dataset.ok!=='1')o.classList.add('ko');const fb=q.querySelector('.mc-fb');if(fb)fb.hidden=false}))}
/* fenêtres */
const MC_DLG=(()=>{const d=document.createElement('dialog');d.id='mc-dialog';d.className='mc-dlg';d.setAttribute('aria-labelledby','mc-dlg-t');
 d.innerHTML='<div class="mc-dlg-h"><h3 id="mc-dlg-t"></h3><button class="mc-back" hidden>← Retour</button><button class="mc-x" aria-label="Fermer">Fermer ✕</button></div><div class="mc-dlg-b"></div>';document.body.appendChild(d);return d})();
let MC_stack=[],MC_trigger=null;
const MC_KEYS=Object.keys(MC_GLOSS).sort((a,b)=>b.length-a.length).map(k=>k.replace(/[.*+?^${}()|[\]\\]/g,'\\$&'));
const MC_RE=new RegExp('(?<![A-Za-zÀ-ÿ0-9₀-₉⁺′])('+MC_KEYS.join('|')+')(?![A-Za-zÀ-ÿ0-9₀-₉⁺′])','g');
let MC_self=null;
function MC_wrapNode(root){const w=document.createTreeWalker(root,NodeFilter.SHOW_TEXT,{acceptNode:n=>n.parentElement.closest('.mc-ab,button,a,[data-k],script,style,svg,[data-justification-sources]')?NodeFilter.FILTER_REJECT:(MC_RE.test(n.nodeValue)?(MC_RE.lastIndex=0,NodeFilter.FILTER_ACCEPT):(MC_RE.lastIndex=0,NodeFilter.FILTER_REJECT))});
 const ns=[];while(w.nextNode())ns.push(w.currentNode);ns.forEach(n=>{const s=document.createElement('span');s.innerHTML=MC_wrap(n.nodeValue);n.replaceWith(...s.childNodes)})}
function MC_wrap(s){return h(s).replace(MC_RE,k=>k===MC_self?k:`<span class="mc-ab" role="button" tabindex="0" data-ab="${k}">${k}</span>`)}
function MC_open(item,push){MC_self=item.ab||null;const b=MC_DLG.querySelector('.mc-dlg-b'),t=MC_DLG.querySelector('#mc-dlg-t');
 if(item.ab){const g=MC_GLOSS[item.ab];t.innerHTML=h(item.ab)+' — '+MC_wrap(g?g.full:'définition');
  let html='<div class="mc-lab">Définition littérale</div><div class="mc-lit">'+(g?g.lit.map(x=>`<b>${h(x[0])}</b><span>${x[1]}</span>`).join(''):'')+'</div>';
  if(g&&g.full)html+=`<p class="mc-full">${h(item.ab)} = ${MC_wrap(g.full)}</p>`;if(g&&g.def)html+=g.def;
  b.innerHTML=html;if(g&&g.ref){const tp=document.querySelector(`template[data-pop="${g.ref}"]`);if(tp){const l=document.createElement('div');l.className='mc-lab';l.textContent='Approfondissement — '+tp.dataset.title;b.appendChild(l);b.appendChild(tp.content.cloneNode(true))}}}
 else{const tp=document.querySelector(`template[data-pop="${item.k}"]`);if(tp){t.innerHTML=MC_wrap(tp.dataset.title);b.innerHTML='';b.appendChild(tp.content.cloneNode(true))}else{t.textContent='Fiche';b.innerHTML='<p>Fiche absente.</p>'}}
 MC_wrapNode(b);if(push)MC_stack.push(item);MC_DLG.querySelector('.mc-back').hidden=MC_stack.length<2;if(!MC_DLG.open)MC_DLG.showModal();b.scrollTop=0;MC_quiz(b)}
function MC_act(el){if(!MC_DLG.open){MC_trigger=el;MC_stack=[]}MC_open(el.dataset.ab?{ab:el.dataset.ab}:{k:el.dataset.k},true)}
document.addEventListener('click',ev=>{const go=ev.target.closest('.mc [data-go]');if(go){ev.preventDefault();const tg=document.getElementById(go.dataset.go);if(tg){const m=document.querySelector('.mc');const b=tg.parentElement;if(m&&m.classList.contains('book')&&b.classList.contains('mc-body')){b.scrollTo({left:b.scrollLeft+tg.getBoundingClientRect().left-b.getBoundingClientRect().left,behavior:'smooth'});if(b.getBoundingClientRect().top<0)b.scrollIntoView({block:'start',behavior:'smooth'})}else tg.scrollIntoView({behavior:'smooth',block:'start'})}return}
 const el=ev.target.closest('.mc-w[data-k]')||ev.target.closest('[data-ab],[data-k]');if(!el||!(el.closest('.mc')||el.closest('.mc-dlg')))return;ev.preventDefault();ev.stopPropagation();MC_act(el)},true);
document.addEventListener('keydown',ev=>{const el=ev.target.closest&&(ev.target.closest('.mc-w[data-k]')||ev.target.closest('.mc-ab'));if(el&&(ev.key==='Enter'||ev.key===' ')){ev.preventDefault();MC_act(el);return}
 const m=document.querySelector('.mc.book');if(!m||MC_DLG.open||ev.altKey||ev.ctrlKey||ev.metaKey||ev.target.closest?.('input,textarea,select,[contenteditable="true"],.mc-navigo,.mc-dlg')||(ev.target.closest?.('button,summary,a')&&!ev.target.closest('.mc-book,.mc-pager')))return;const b=m.querySelector('.mc-panel:not([hidden]) .mc-body');if(!b)return;
 if(ev.key==='ArrowRight'||ev.key==='ArrowLeft'){ev.preventDefault();m._mcPagerGo?.(ev.key==='ArrowRight'?1:-1)}});
MC_DLG.querySelector('.mc-back').onclick=()=>{MC_stack.pop();MC_open(MC_stack[MC_stack.length-1],false)};
MC_DLG.querySelector('.mc-x').onclick=()=>MC_DLG.close();
MC_DLG.addEventListener('close',()=>{MC_stack=[];if(MC_trigger&&MC_trigger.isConnected)MC_trigger.focus()});
MC_DLG.addEventListener('click',ev=>{if(ev.target===MC_DLG)MC_DLG.close()});
const MC_basePage=entryPage;entryPage=function(){const e=EM[route.id];if(e&&MEDINA_hasCourse(e.code)&&route.q.get('view')!=='plan')return MEDINA_coursePage(e);return MC_basePage()};
if(typeof render==='function'&&location.hash.startsWith('#/entry/'))render();
(()=>{const c=document.getElementById('content');if(!c)return;let t=null;new MutationObserver(()=>{clearTimeout(t);t=setTimeout(MC_badges,60)}).observe(c,{childList:true,subtree:true})})();
setTimeout(MC_badges,300);
