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
/* notification des nouveaux cours */
function toast(){const N=(D.news||[]);if(!N.length)return;let seen=null;try{seen=localStorage.getItem('medina.seen')}catch(e){}if(seen===D.build)return;
 const t=document.createElement('div');t.className='mdn-toast';t.setAttribute('role','status');t.innerHTML=`<h3>Nouveaux cours livrés</h3><ul>${N.map(c=>`<li><a href="#/entry/${c.code}">${esc(c.code)} · ${esc(c.title)}</a></li>`).join('')}</ul><button type="button">Fermer</button>`;
 document.body.appendChild(t);requestAnimationFrame(()=>t.classList.add('on'));const close=()=>{t.classList.remove('on');setTimeout(()=>t.remove(),400);try{localStorage.setItem('medina.seen',D.build)}catch(e){}};t.querySelector('button').onclick=close;t.querySelectorAll('a').forEach(a=>a.addEventListener('click',close))}
const run=()=>{sysBadges();ecgButton()};let tm=null;new MutationObserver(()=>{clearTimeout(tm);tm=setTimeout(run,80)}).observe(document.body,{childList:true,subtree:true});
setTimeout(run,300);setTimeout(toast,1200);})();
/* ===== Bouton directeur de l'accueil : systèmes en cours, jauges, ouverture du système ===== */
(()=>{const D=window.MDN_DATA||{};const S=D.systems||[];if(!S.length)return;
const esc=s=>String(s??'').replace(/[&<>"']/g,x=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[x]));
const norm=s=>String(s).toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'').replace(/[^a-z0-9 ]/g,' ');
let dlg=null;
function ring(p,cls=''){return `<span class="ring" style="--p:${p}"><b>${p} %</b></span>`}
function list(){const act=S.filter(s=>s.prio).sort((a,b)=>(b.pct>0)-(a.pct>0)||b.pct-a.pct);
 return `<div class="grid">${act.map(s=>`<button type="button" class="sc ${s.done?'done':''} ${s.pct?'':'off'}" data-n="${s.n}">${ring(s.pct)}<span><h3>${esc(s.t)}</h3><small>${s.ch.length} cours rédigé${s.ch.length>1?'s':''} · ${s.done?'système achevé':s.pct?'en cours de création':'en préparation'}</small>${s.done?'<br><span class="fluo">100 % rédigé</span>':''}<span class="bar"><i style="width:${s.pct}%"></i></span></span></button>`).join('')}</div>`}
function detail(n){const s=S.find(x=>x.n==n);const done=s.ch.map(c=>c.title);
 const doneN=new Set(done.map(norm));
 const planned=s.plan.filter(p=>![...doneN].some(d=>d.includes(norm(p).split(' ')[0])&&norm(p).split(' ').some(w=>w.length>4&&d.includes(w))));
 return `<div class="detail"><button type="button" class="back">← Tous les systèmes</button><div class="big">${ring(s.pct)}<div><h3>${esc(s.t)}</h3><small>${s.cat} catégories CIM · ${s.ch.length} cours rédigés</small></div></div>
 <ol>${s.ch.map(c=>`<li><a href="#/entry/${c.code}" data-close>${esc(c.code)} · ${esc(c.title)}</a><span class="fluo">100 % rédigé</span></li>`).join('')}${planned.map(p=>`<li class="todo">${esc(p)}<span class="st">à rédiger</span></li>`).join('')}</ol></div>`}
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
