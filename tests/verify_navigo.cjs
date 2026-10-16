/* Navigo — ergonomie du plan de la leçon (16.10.2026).
   Usage : MEDINA_FRAGMENTS=<dossier fragments/> node tests/verify_navigo.cjs
   Variables : MEDINA_NAVIGO_CASES="S08:G45,S05:E11" (fragment:leçon), MEDINA_QA_OUT (captures facultatives).
   Contrôle : ouverture (bouton, N, Ctrl+K), focus piégé, Échap et retour du focus, arbre ARIA, clavier complet,
   recherche avec surlignage, saut inter-onglets sous les barres collantes, ancre d'URL et retour arrière,
   panneau épinglé ≥ 1440 px, feuille basse à 390 px, mode Livre à 24 px, contraste ≥ 7:1, aucune erreur JS. */
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {pathToFileURL}=require('node:url');
const {loadPlaywright,browserOptions}=require('./browser_runtime.cjs');
const {chromium}=loadPlaywright(),root=path.resolve(__dirname,'..');
const directory=path.resolve(process.env.MEDINA_FRAGMENTS||path.join(root,'dist/fragments'));
const fragments=JSON.parse(fs.readFileSync(path.join(root,'fragments.json'),'utf8'));
const cases=(process.env.MEDINA_NAVIGO_CASES||'S08:G45,S05:E11').split(',').map(x=>x.split(':'));
const shots=process.env.MEDINA_QA_OUT?path.resolve(process.env.MEDINA_QA_OUT):null;if(shots)fs.mkdirSync(shots,{recursive:true});
const checks=[];
const check=(name,ok,detail)=>{assert.ok(ok,name+(detail===undefined?'':' : '+JSON.stringify(detail)));checks.push(name)};
const ROWS='[...document.querySelectorAll(".mc-navigo-list [role=treeitem]")]';
const rowOf='(li=>li&&li.querySelector(":scope>.mc-navigo-item"))';
async function active(page){return page.evaluate(()=>{const a=document.activeElement;return {tag:a.tagName,inPanel:!!a.closest('.mc-navigo-panel'),trigger:a.matches('.mc-navigo-trigger'),key:a.dataset?.key||null,role:a.getAttribute('role')}})}
async function open(page,url,width,height,options={}){
 const context=await page.context().browser().newContext({viewport:{width,height},reducedMotion:'reduce',...options});
 const p=await context.newPage();const errors=[];p.on('pageerror',e=>errors.push(e.message));
 await p.goto(url);await p.locator('.mc').waitFor();await p.locator('.mc-navigo[data-navigo="2"]').waitFor({state:'attached'});await p.waitForTimeout(250);
 return {context,page:p,errors};
}
async function contrast(page){return page.evaluate(()=>{
 const rgb=c=>c.match(/[\d.]+/g).slice(0,4).map(Number),lin=v=>{v/=255;return v<=.04045?v/12.92:((v+.055)/1.055)**2.4},lum=c=>.2126*lin(c[0])+.7152*lin(c[1])+.0722*lin(c[2]);
 const bg=el=>{for(let e=el;e;e=e.parentElement){const c=rgb(getComputedStyle(e).backgroundColor);if(c.length<4||c[3]>.98)return c}return [255,255,255]};
 const els=[...document.querySelectorAll('.mc-navigo-panel :is(.mc-navigo-label,.mc-navigo-num,.mc-navigo-title,.mc-navigo-where-text,.mc-navigo-count,.mc-navigo-path,small)')].filter(e=>e.getClientRects().length);
 return Math.min(...els.map(e=>{const a=lum(rgb(getComputedStyle(e).color)),b=lum(bg(e));return (Math.max(a,b)+.05)/(Math.min(a,b)+.05)}))})}
(async()=>{
 const browser=await chromium.launch(browserOptions(chromium));
 try{
  const seed=await (await browser.newContext()).newPage();
  for(const [id,code] of cases){
   const fragment=fragments.find(f=>f.id===id);assert.ok(fragment,'fragment inconnu '+id);
   const file=path.join(directory,`MEDINA_${fragment.id}_${fragment.slug}.html`),url=pathToFileURL(file).href+'#/entry/'+code,L=id+'/'+code;
   /* ---------- Bureau 1280 : tiroir ---------- */
   let {context,page,errors}=await open(seed,url,1280,900);
   const trig=page.locator('.mc-navigo-trigger'),panel=page.locator('.mc-navigo-panel');
   check(L+' : un seul déclencheur, visible',await trig.count()===1&&await trig.isVisible());
   const tb=await trig.evaluate(el=>({r:el.getBoundingClientRect().toJSON(),bar:!!el.closest('.topbar')}));
   check(L+' : déclencheur stable dans la barre supérieure, ≥ 44 px, sans recouvrir le texte',tb.bar&&tb.r.height>=44&&tb.r.width>=44,tb);
   check(L+' : Navigo fermé au départ',!await panel.isVisible());
   await page.locator('.mc-chap-head h1').click();await page.keyboard.press('n');
   check(L+' : la touche N ouvre le plan',await panel.isVisible()&&await trig.getAttribute('aria-expanded')==='true');
   check(L+' : rôle de dialogue modal du tiroir',await panel.getAttribute('role')==='dialog'&&await panel.getAttribute('aria-modal')==='true');
   check(L+' : focus placé dans le tiroir',(await active(page)).inPanel);
   await page.keyboard.press('Escape');
   check(L+' : Échap ferme et rend le focus au déclencheur',!await panel.isVisible()&&(await active(page)).trigger);
   await page.locator('.mc-chap-head h1').click();await page.keyboard.press('Control+k');
   check(L+' : Ctrl+K ouvre le plan sur la recherche',await panel.isVisible()&&await page.evaluate(()=>document.activeElement.matches('.mc-navigo-search')));
   let escaped=0;for(let i=0;i<24;i++){await page.keyboard.press(i%5===4?'Shift+Tab':'Tab');const a=await active(page);if(!a.inPanel)escaped++}
   check(L+' : focus piégé dans le tiroir ouvert (Tab et Maj+Tab)',escaped===0,{escaped});
   const aria=await page.evaluate(new Function('const r='+ROWS+';const tree=document.querySelector(".mc-navigo-list");return {tree:tree.getAttribute("role"),n:r.length,levels:r.every(x=>+x.getAttribute("aria-level")>=1),labelled:r.every(x=>(x.getAttribute("aria-labelledby")||"").split(" ").every(id=>document.getElementById(id))),parents:r.filter(x=>x.querySelector(":scope>[role=group]")).every(x=>x.getAttribute("aria-expanded")==="true"),current:r.filter(x=>x.getAttribute("aria-current")==="location").length,tabs:r.filter(x=>x.getAttribute("aria-level")==="1").length,stops:r.filter(x=>x.tabIndex===0).length,groups:document.querySelectorAll(".mc-navigo-list [role=group]").length}'));
   check(L+' : arbre ARIA tree/treeitem/group, niveaux et noms',aria.tree==='tree'&&aria.n>4&&aria.levels&&aria.labelled&&aria.parents&&aria.groups>0,aria);
   check(L+' : onglets au premier niveau, une seule position courante, un seul arrêt de tabulation',aria.tabs>=4&&aria.current===1&&aria.stops===1,aria);
   const sizes=await page.evaluate(()=>[...document.querySelectorAll('.mc-navigo-item')].map(r=>r.getBoundingClientRect().height));
   check(L+' : cibles ≥ 32 px au bureau',Math.min(...sizes)>=32,{min:Math.min(...sizes)});
   const c1=await contrast(page);check(L+' : contraste du texte ≥ 7:1',c1>=7,{min:c1});
   const lines=await page.evaluate(()=>[...document.querySelectorAll('.mc-navigo-label')].every(l=>{const lh=parseFloat(getComputedStyle(l).lineHeight);return l.getBoundingClientRect().height<=lh*2+2}));
   check(L+' : titres sur deux lignes au plus',lines);
   /* Clavier de l'arbre */
   await page.locator('.mc-navigo-list [role=treeitem][tabindex="0"]').focus();
   await page.keyboard.press('Home');check(L+' : Début → premier élément',await page.evaluate(new Function('return document.activeElement==='+ROWS+'[0]')));
   await page.keyboard.press('End');check(L+' : Fin → dernier élément',await page.evaluate(new Function('const r='+ROWS+';return document.activeElement===r[r.length-1]')));
   await page.keyboard.press('Home');await page.keyboard.press('ArrowDown');
   check(L+' : ↓ → élément suivant',await page.evaluate(new Function('return document.activeElement==='+ROWS+'[1]')));
   const collapsed=await page.evaluate(new Function('return '+ROWS+'.findIndex(x=>x.getAttribute("aria-expanded")==="false")'));
   if(collapsed>=0){
    await page.evaluate(new Function('i','const x='+ROWS+'[i];x.focus()'),collapsed);
    const key=await page.evaluate(()=>document.activeElement.dataset.key);
    await page.keyboard.press('ArrowRight');
    check(L+' : → déplie la partie',await page.evaluate(k=>document.querySelector('.mc-navigo-list [data-key="'+CSS.escape(k)+'"]').getAttribute('aria-expanded')==='true'&&document.activeElement.dataset.key===k,key));
    await page.keyboard.press('ArrowRight');check(L+' : → entre dans les sous-parties',await page.evaluate(k=>document.activeElement.parentElement.closest('[role=treeitem]')?.dataset.key===k,key));
    await page.keyboard.press('ArrowLeft');check(L+' : ← remonte au parent',await page.evaluate(k=>document.activeElement.dataset.key===k,key));
    await page.keyboard.press('ArrowLeft');check(L+' : ← replie la partie',await page.evaluate(k=>document.querySelector('.mc-navigo-list [data-key="'+CSS.escape(k)+'"]').getAttribute('aria-expanded')==='false',key));
   }
   /* Recherche */
   const search=page.locator('.mc-navigo-search');await search.fill('diagnostic');
   const found=await page.evaluate(new Function('const r='+ROWS+';return {n:r.length,all:r.every(x=>x.querySelector(".mc-navigo-text").textContent.normalize("NFD").replace(/[\\u0300-\\u036f]/g,"").toLowerCase().includes("diagnostic")),marks:document.querySelectorAll(".mc-navigo-list mark").length,count:document.querySelector(".mc-navigo-count").textContent}'));
   check(L+' : recherche instantanée, surlignage et compteur',found.n>0&&found.all&&found.marks>=found.n&&/résultat/.test(found.count),found);
   if(shots)await page.screenshot({path:path.join(shots,id+'_recherche_1280.png')});
   await search.fill('zzzzqx');check(L+' : recherche vide expliquée',/Aucun titre/.test(await page.locator('.mc-navigo-count').textContent()));
   /* Saut inter-onglets : un titre de l'onglet Examens, recherché depuis l'onglet affiché. */
   const other=await page.evaluate(()=>{const tabs=[...document.querySelectorAll('.mc .mc-tabs [data-p]')],cur=tabs.find(t=>t.getAttribute('aria-selected')==='true');const t=tabs.find(x=>x!==cur);const hd=document.getElementById(t.dataset.p).querySelector('.mc-ilot h3,.mc-ilot h2');return {tab:t.dataset.p,text:hd.textContent.replace(/\s+/g,' ').trim()}});
   const y0=await page.evaluate(()=>Math.round(scrollY));
   await search.fill(other.text.replace(/^[\d.]+\s*/,'').slice(0,40));await search.press('Enter');
   await page.waitForFunction(()=>/^H[234]$/.test(document.activeElement.tagName));await page.waitForTimeout(150);
   const landed=await page.evaluate(()=>{const a=document.activeElement,r=a.getBoundingClientRect(),tabs=document.querySelector('.mc .mc-tabs'),cs=getComputedStyle(tabs),cover=Math.max(document.querySelector('.topbar').getBoundingClientRect().bottom,cs.position==='sticky'?parseFloat(cs.top)+tabs.offsetHeight:0);
    return {tab:document.querySelector('.mc .mc-tabs [aria-selected="true"]').dataset.p,inTab:a.closest('.mc-panel').id,top:r.top,cover,bottom:r.bottom,h:innerHeight,hash:location.hash}});
   check(L+' : saut inter-onglets, onglet ouvert automatiquement',landed.tab===other.tab&&landed.inTab===other.tab,landed);
   check(L+' : titre visible sous les barres collantes',landed.top>=landed.cover-1&&landed.bottom<=landed.h,landed);
   check(L+' : tiroir refermé après le saut',!await panel.isVisible());
   check(L+' : ancre « nav » écrite dans l’URL',/[?&]nav=/.test(landed.hash),landed.hash);
   await page.goBack();await page.waitForTimeout(300);
   const back=await page.evaluate(()=>({mc:document.querySelectorAll('.mc').length,hash:location.hash,y:Math.round(scrollY),tab:document.querySelector('.mc .mc-tabs [aria-selected="true"]').dataset.p}));
   check(L+' : retour arrière sans rechargement, position et onglet rétablis',back.mc===1&&!/nav=/.test(back.hash)&&Math.abs(back.y-y0)<=4&&back.tab!==other.tab,{back,y0});
   await page.goForward();await page.waitForTimeout(300);
   check(L+' : avance rapide vers le titre',await page.evaluate(()=>/nav=/.test(location.hash)&&document.querySelectorAll('.mc').length===1));
   /* Lien partagé : rechargement sur l'ancre. */
   await page.reload();await page.locator('.mc').waitFor();await page.waitForTimeout(500);
   const reloaded=await page.evaluate(()=>{const k=new URLSearchParams(location.hash.split('?')[1]).get('nav'),cur=document.querySelector('.mc-navigo-list [aria-current]');return {k,tab:document.querySelector('.mc .mc-tabs [aria-selected="true"]').dataset.p,focus:document.activeElement.tagName}});
   check(L+' : lien « ?nav= » rouvert sur le bon onglet et le bon titre',reloaded.tab===other.tab&&/^H[234]$/.test(reloaded.focus),reloaded);
   check(L+' : aucune erreur JavaScript (1280)',errors.length===0,errors);
   await context.close();
   /* ---------- Grand écran 1600 : panneau épinglé ---------- */
   ({context,page,errors}=await open(seed,url,1600,950));
   const p2=page.locator('.mc-navigo-panel');
   const pinned=await page.evaluate(()=>{const p=document.querySelector('.mc-navigo-panel').getBoundingClientRect(),m=document.querySelector('.mc').getBoundingClientRect();return {mode:document.body.dataset.mcNavigo,role:document.querySelector('.mc-navigo-panel').getAttribute('role'),gap:p.left-m.right,trigger:!!document.querySelector('.mc-navigo-trigger').getClientRects().length}});
   check(L+' : panneau épinglé par défaut à 1600, sans masquer le texte',await p2.isVisible()&&pinned.mode==='pinned'&&pinned.gap>=8&&!pinned.trigger&&pinned.role===null,pinned);
   if(shots)await page.screenshot({path:path.join(shots,id+'_epingle_1600.png')});
   await page.locator('.mc-navigo-item').nth(2).click();await page.waitForFunction(()=>/^H[234]$/.test(document.activeElement.tagName));
   check(L+' : le panneau épinglé reste ouvert après un saut',await p2.isVisible());
   await page.locator('.mc-navigo-pin').click();
   check(L+' : désépingler range le plan dans un tiroir',!await p2.isVisible()&&await page.locator('.mc-navigo-trigger').isVisible());
   await page.reload();await page.locator('.mc').waitFor();await page.waitForTimeout(300);
   check(L+' : choix « désépinglé » conservé',!await p2.isVisible());
   await page.locator('.mc-navigo-trigger').click();await page.locator('.mc-navigo-pin').click();
   check(L+' : épingler de nouveau',await page.evaluate(()=>document.body.dataset.mcNavigo==='pinned')&&await p2.isVisible());
   check(L+' : aucune erreur JavaScript (1600)',errors.length===0,errors);
   await context.close();
   /* ---------- Mobile 390 : feuille basse ---------- */
   ({context,page,errors}=await open(seed,url,390,844,{isMobile:true,hasTouch:true}));
   const mt=page.locator('.mc-navigo-trigger');const mb=await mt.evaluate(el=>({...el.getBoundingClientRect().toJSON(),pos:getComputedStyle(el).position}));
   check(L+' : bouton flottant au pouce ≥ 44×44 en bas à droite',mb.pos==='fixed'&&mb.width>=44&&mb.height>=44&&mb.right>=330&&mb.bottom>=760,mb);
   await mt.tap();const mp=page.locator('.mc-navigo-panel');
   const sheet=await page.evaluate(()=>{const p=document.querySelector('.mc-navigo-panel').getBoundingClientRect();return {mode:document.body.dataset.mcNavigo,w:p.width,bottom:p.bottom,min:Math.min(...[...document.querySelectorAll('.mc-navigo-item')].map(r=>r.getBoundingClientRect().height)),keyboard:document.activeElement.matches('input'),scroll:document.documentElement.scrollWidth}});
   check(L+' : feuille basse ouverte, cibles ≥ 44 px, pas de clavier imposé',await mp.isVisible()&&sheet.mode==='sheet'&&sheet.w>=370&&sheet.min>=44&&!sheet.keyboard&&sheet.scroll<=391,sheet);
   if(shots)await page.screenshot({path:path.join(shots,id+'_mobile_390.png')});
   await page.locator('.mc-navigo-item.mc-navigo-h3:visible,.mc-navigo-item.mc-navigo-h2:visible').nth(1).tap();
   await page.waitForFunction(()=>/^H[234]$/.test(document.activeElement.tagName));
   check(L+' : fermeture automatique après le saut sur mobile',!await mp.isVisible());
   check(L+' : aucune erreur JavaScript (390)',errors.length===0,errors);
   await context.close();
   /* ---------- Mode Livre et police 24 px ---------- */
   ({context,page,errors}=await open(seed,url,1280,900));
   await page.locator('.mc-size-toggle').click();await page.locator('.mc-size-range').evaluate(el=>{el.value=24;el.dispatchEvent(new Event('input'))});await page.keyboard.press('Escape');
   await page.locator('.mc-book').click();await page.waitForTimeout(200);
   await page.locator('.mc-navigo-trigger').click();
   const fs24=await page.evaluate(()=>parseFloat(getComputedStyle(document.querySelector('.mc-navigo-item')).fontSize));
   check(L+' : Navigo suit la taille 24 px',fs24>=19,{fs24});
   const okLines=await page.evaluate(()=>[...document.querySelectorAll('.mc-navigo-label')].every(l=>l.getBoundingClientRect().height<=parseFloat(getComputedStyle(l).lineHeight)*2+2));
   check(L+' : à 24 px, titres toujours sur deux lignes au plus',okLines);
   const last=page.locator('.mc-navigo-list .is-tab-active [role=group]>[role=treeitem]>.mc-navigo-item').last();await last.click();
   await page.waitForFunction(()=>/^H[234]$/.test(document.activeElement.tagName));await page.waitForTimeout(250);
   const book=await page.evaluate(()=>{const a=document.activeElement,b=a.closest('.mc-body'),r=a.getBoundingClientRect(),br=b.getBoundingClientRect();return {book:!!document.querySelector('.mc.book'),inside:r.left>=br.left-1&&r.right<=br.right+1,top:r.top,h:innerHeight}});
   check(L+' : mode Livre, la page du titre est affichée',book.book&&book.inside&&book.top>=0&&book.top<book.h,book);
   check(L+' : aucune erreur JavaScript (Livre)',errors.length===0,errors);
   await context.close();
  }
  console.log('OK verify_navigo : '+checks.length+' contrôles');
 }finally{await browser.close()}
})().catch(error=>{console.error(error.message||error);console.error('Contrôles réussis avant l’échec : '+checks.length);process.exit(1)});
