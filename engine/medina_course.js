
/* ===== MEDINA — moteur de cours ===== */
const MC_GLOSS=JSON.parse(document.getElementById('medina-glossary').textContent);
const MC={store:{get(k,d){try{const v=localStorage.getItem('medina.course.'+k);return v===null?d:JSON.parse(v)}catch(e){return d}},set(k,v){try{localStorage.setItem('medina.course.'+k,JSON.stringify(v))}catch(e){}}}};
function MC_code(code){return (window.MEDINA_ALIAS||{})[code]||code}
function MEDINA_hasCourse(code){return !!document.getElementById('ch-'+MC_code(code))}
function MEDINA_coursePage(e){
 pageTitle(`${e.code} — ${e.title}`);
 const sid=SM[route.q.get('specialty')]?route.q.get('specialty'):e.primary;const s=SM[sid];context={sid,e};
 const tpl=document.getElementById('ch-'+MC_code(e.code));
 const fonts=[["'Anthropic Serif',Georgia,serif",'Anthropic Serif'],["Georgia,'Times New Roman',serif",'Georgia'],["system-ui,sans-serif",'Système'],["'Segoe UI',Arial,sans-serif",'Segoe UI'],["'Literata',Georgia,serif",'Literata'],["'Source Serif 4',Georgia,serif",'Source Serif'],["'EB Garamond',Georgia,serif",'Garamond'],["'Atkinson Hyperlegible','Segoe UI',sans-serif",'Atkinson'],["'Inter','Segoe UI',sans-serif",'Inter']];
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
let MC_NAV_CLEANUP=null,MC_SIZE_CLEANUP=null;
function MC_navigoDestroy(){if(MC_NAV_CLEANUP){MC_NAV_CLEANUP();MC_NAV_CLEANUP=null}}
/* Libellé Navigo : le numéro (span.mc-n ou .mc-subn) est séparé du titre par une espace. */
function MC_navLabel(h){const t=h.textContent.replace(/\s+/g,' ').trim(),n=h.querySelector('.mc-n,.mc-subn');if(!n)return t;const k=n.textContent.trim();return k&&t.startsWith(k)?k+' '+t.slice(k.length).trim():t}
function MC_navigoMount(m){
 const host=document.createElement('div');host.className='mc-navigo';host.innerHTML='<button type="button" class="mc-navigo-trigger" aria-controls="mc-navigo-panel" aria-expanded="false">Navigo <span aria-hidden="true">▤</span></button><aside id="mc-navigo-panel" class="mc-navigo-panel" aria-label="Plan de la leçon active" hidden><div class="mc-navigo-head"><div><small>PLAN DE LA LEÇON</small><strong class="mc-navigo-title"></strong></div><button type="button" class="mc-navigo-close" aria-label="Fermer Navigo">×</button></div><div class="mc-navigo-tabs" role="group" aria-label="Onglets du cours"></div><label class="mc-navigo-search-label">Rechercher une partie<input class="mc-navigo-search" type="search" placeholder="Titre ou numéro…"></label><nav class="mc-navigo-list" aria-label="Parties et sous-parties du cours"></nav><div class="mc-navigo-foot"></div></aside>';
 document.body.appendChild(host);const trigger=host.querySelector('.mc-navigo-trigger'),drawer=host.querySelector('.mc-navigo-panel'),list=host.querySelector('.mc-navigo-list'),search=host.querySelector('.mc-navigo-search');
 let headings=[],buttons=[];
 const open=(on)=>{drawer.hidden=!on;trigger.setAttribute('aria-expanded',String(on));if(on){refresh();search.focus()}else trigger.focus({preventScroll:true})};
 trigger.onclick=()=>open(drawer.hidden);host.querySelector('.mc-navigo-close').onclick=()=>open(false);
 function move(h){const science=h.closest('.mc-sci');if(science?.hidden){const tab=Array.from(m.querySelectorAll('.mc-sci-bar button[data-s]')).find(x=>x.dataset.s===science.id);if(tab){tab.click();requestAnimationFrame(()=>move(h));return}}
 const b=h.closest('.mc-body');if(m.classList.contains('book')&&b){const page=Array.from(b.children).find(x=>x.contains(h));if(page){b.scrollTo({left:b.scrollLeft+page.getBoundingClientRect().left-b.getBoundingClientRect().left,behavior:'smooth'});setTimeout(()=>{page.scrollTo({top:page.scrollTop+h.getBoundingClientRect().top-page.getBoundingClientRect().top-14,behavior:'smooth'});h.setAttribute('tabindex','-1');h.focus({preventScroll:true})},320);return}}
 h.scrollIntoView({block:'start',behavior:'smooth'});h.setAttribute('tabindex','-1');h.focus({preventScroll:true})}
 function filter(){const q=search.value.trim().toLocaleLowerCase('fr');let n=0;buttons.forEach(b=>{const match=!q||b.textContent.toLocaleLowerCase('fr').includes(q);b.hidden=!match;if(match)n++});host.querySelector('.mc-navigo-foot').textContent=n+' partie'+(n>1?'s':'')+' affichée'+(n>1?'s':'')}
 search.oninput=filter;
 function refresh(){if(!m.isConnected)return;const panel=m.querySelector('.mc-panel:not([hidden])');if(!panel)return;
  host.style.setProperty('--mc-font',m.style.getPropertyValue('--mc-font'));host.style.setProperty('--mc-scale',m.style.getPropertyValue('--mc-scale'));
  host.querySelector('.mc-navigo-title').textContent=m.querySelector('.mc-chap-head h1')?.textContent.trim()||'Cours';
  const tabs=host.querySelector('.mc-navigo-tabs');tabs.replaceChildren();m.querySelectorAll('.mc-tabs [data-p]').forEach(tab=>{const b=document.createElement('button');b.type='button';b.textContent=tab.textContent.trim();b.className=tab.getAttribute('aria-selected')==='true'?'is-active':'';b.onclick=()=>{tab.click();refresh()};tabs.appendChild(b)});
  headings=Array.from(panel.querySelectorAll('.mc-ilot h2,.mc-ilot h3,.mc-ilot h4,.mc-sci>h2'));
  list.replaceChildren();buttons=[];headings.forEach(h=>{const b=document.createElement('button');b.type='button';b.className='mc-navigo-item mc-navigo-'+h.tagName.toLowerCase();b.textContent=MC_navLabel(h);b.onclick=()=>{buttons.forEach(x=>x.removeAttribute('aria-current'));b.setAttribute('aria-current','location');open(false);move(h)};list.appendChild(b);buttons.push(b)});filter();
 }
 const onKey=e=>{if(e.key==='Escape'&&!drawer.hidden){e.preventDefault();open(false)}};
 const outside=e=>{if(!drawer.hidden&&!host.contains(e.target))open(false)};
 document.addEventListener('keydown',onKey);document.addEventListener('pointerdown',outside);
 const observer=new MutationObserver(()=>{if(!m.isConnected)MC_navigoDestroy()});const content=document.getElementById('content');if(content)observer.observe(content,{childList:true});
 MC_NAV_CLEANUP=()=>{observer.disconnect();document.removeEventListener('keydown',onKey);document.removeEventListener('pointerdown',outside);host.remove()};
 return refresh;
}
function MEDINA_mount(){MC_badges();MC_navigoDestroy();if(MC_SIZE_CLEANUP){MC_SIZE_CLEANUP();MC_SIZE_CLEANUP=null}
 const m=document.querySelector('.mc');if(!m)return;const code=m.dataset.code;
 let navRefresh=()=>{};
 const applyFont=()=>{const f=MC.store.get('font.'+code,MC.store.get('font.default',"'Anthropic Serif',Georgia,serif"));const s=Math.min(24,Math.max(14,Number(MC.store.get('fs.'+code,17))||17));m.style.setProperty('--mc-font',f);m.style.setProperty('--mc-fs',s+'px');m.style.setProperty('--mc-scale',(s/17).toFixed(3));m.querySelector('.mc-font').value=f;m.querySelector('.mc-size-range').value=s;m.querySelector('.mc-size-value').textContent=s+' px';document.documentElement.style.setProperty('--mc-font',f);document.documentElement.style.setProperty('--mc-scale',(s/17).toFixed(3));navRefresh()};
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
 const bookBtn=m.querySelector('.mc-book');const setBook=on=>{m.classList.toggle('book',on);bookBtn.setAttribute('aria-pressed',on);MC.store.set('book',on);pager()};
 bookBtn.onclick=()=>setBook(!m.classList.contains('book'));
 const body=()=>m.querySelector('.mc-panel:not([hidden]) .mc-body');
 function pager(){const b=body();const pg=m.querySelector('.mc-panel:not([hidden]) .mc-pager');if(!b||!pg)return;const n=b.children.length;
  const step=()=>{const child=b.children[0];const gap=parseFloat(getComputedStyle(b).columnGap)||0;return child?child.getBoundingClientRect().width+gap:b.clientWidth};
  const upd=()=>{pg.querySelector('span').textContent=(Math.min(n,Math.max(1,Math.round(b.scrollLeft/Math.max(1,step()))+1)))+' / '+n};b.onscroll=upd;upd();
  pg.querySelector('.mc-prev').onclick=()=>b.scrollBy({left:-step(),behavior:'smooth'});pg.querySelector('.mc-next').onclick=()=>b.scrollBy({left:step(),behavior:'smooth'})}
 const tabs=m.querySelectorAll('.mc-tabs button');tabs.forEach(b=>b.onclick=()=>{tabs.forEach(x=>x.setAttribute('aria-selected',x===b));m.querySelectorAll('.mc-panel').forEach(p=>p.hidden=p.id!==b.dataset.p);MC.store.set('tab.'+code,b.dataset.p);pager();navRefresh()});
 const lt=MC.store.get('tab.'+code,null);const tb=lt&&m.querySelector(`.mc-tabs button[data-p="${lt}"]`);if(tb)tb.click();
 const sb=m.querySelectorAll('.mc-sci-bar button');sb.forEach(b=>b.onclick=()=>{sb.forEach(x=>x.setAttribute('aria-selected',x===b));m.querySelectorAll('.mc-sci').forEach(p=>p.hidden=p.id!==b.dataset.s);
  const sbody=m.querySelector('.mc-sci-body'),target=m.querySelector('#'+b.dataset.s);if(m.classList.contains('book')&&sbody&&target){sbody.scrollTo({left:sbody.scrollLeft+target.getBoundingClientRect().left-sbody.getBoundingClientRect().left})}navRefresh()});
 if(sb[0])sb[0].click();
 applyFont();setBook(MC.store.get('book',false));MC_quiz(m);navRefresh=MC_navigoMount(m);navRefresh();
}
function MC_quiz(root){root.querySelectorAll('.mc-quiz').forEach(q=>q.querySelectorAll('.mc-opt').forEach(o=>o.onclick=ev=>{if(ev.target.closest('[data-ab]'))return;q.querySelectorAll('.mc-opt').forEach(x=>x.classList.toggle('ok',x.dataset.ok==='1'));if(o.dataset.ok!=='1')o.classList.add('ko');const fb=q.querySelector('.mc-fb');if(fb)fb.hidden=false}))}
/* fenêtres */
const MC_DLG=(()=>{const d=document.createElement('dialog');d.className='mc-dlg';d.setAttribute('aria-labelledby','mc-dlg-t');
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
document.addEventListener('click',ev=>{const go=ev.target.closest('.mc [data-go]');if(go){ev.preventDefault();const tg=document.getElementById(go.dataset.go);if(tg){const m=document.querySelector('.mc');const b=tg.parentElement;if(m&&m.classList.contains('book')&&b.classList.contains('mc-body'))b.scrollTo({left:b.scrollLeft+tg.getBoundingClientRect().left-b.getBoundingClientRect().left,behavior:'smooth'});else tg.scrollIntoView({behavior:'smooth',block:'start'})}return}
 const el=ev.target.closest('.mc-w[data-k]')||ev.target.closest('[data-ab],[data-k]');if(!el||!(el.closest('.mc')||el.closest('.mc-dlg')))return;ev.preventDefault();ev.stopPropagation();MC_act(el)},true);
document.addEventListener('keydown',ev=>{const el=ev.target.closest&&(ev.target.closest('.mc-w[data-k]')||ev.target.closest('.mc-ab'));if(el&&(ev.key==='Enter'||ev.key===' ')){ev.preventDefault();MC_act(el);return}
 const m=document.querySelector('.mc.book');if(!m||MC_DLG.open||ev.target.closest?.('input,textarea,select,button,[contenteditable="true"],.mc-navigo'))return;const b=m.querySelector('.mc-panel:not([hidden]) .mc-body');if(!b)return;
 const step=(b.children[0]?.getBoundingClientRect().width||b.clientWidth)+(parseFloat(getComputedStyle(b).columnGap)||0);
 if(ev.key==='ArrowRight')b.scrollBy({left:step,behavior:'smooth'});if(ev.key==='ArrowLeft')b.scrollBy({left:-step,behavior:'smooth'})});
MC_DLG.querySelector('.mc-back').onclick=()=>{MC_stack.pop();MC_open(MC_stack[MC_stack.length-1],false)};
MC_DLG.querySelector('.mc-x').onclick=()=>MC_DLG.close();
MC_DLG.addEventListener('close',()=>{MC_stack=[];if(MC_trigger&&MC_trigger.isConnected)MC_trigger.focus()});
MC_DLG.addEventListener('click',ev=>{if(ev.target===MC_DLG)MC_DLG.close()});
const MC_basePage=entryPage;entryPage=function(){const e=EM[route.id];if(e&&MEDINA_hasCourse(e.code)&&route.q.get('view')!=='plan')return MEDINA_coursePage(e);return MC_basePage()};
if(typeof render==='function'&&location.hash.startsWith('#/entry/'))render();
(()=>{const c=document.getElementById('content');if(!c)return;let t=null;new MutationObserver(()=>{clearTimeout(t);t=setTimeout(MC_badges,60)}).observe(c,{childList:true,subtree:true})})();
setTimeout(MC_badges,300);
