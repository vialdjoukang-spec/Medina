/* Real browser checks for the opt-in S01 surface; build the fragment first. */
const fs = require('node:fs');
const http = require('node:http');
const path = require('node:path');
const assert = require('node:assert/strict');
const {pathToFileURL} = require('node:url');
const {chromium} = require(process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES
  ? process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES + '/playwright' : 'playwright');
const file = path.resolve(process.env.MEDINA_S01_FILE || 'dist/fragments/MEDINA_S01_cardiovasculaire.html');
const out = path.resolve(process.env.MEDINA_QA_OUT || 'audits/S01_2026-10-05');
const checks = [], errors = [];
fs.mkdirSync(path.join(out, 'captures'), {recursive:true});
const check = (name, condition, detail) => {assert.ok(condition, name + (detail ? ': ' + JSON.stringify(detail) : '')); checks.push(name)};

(async () => {
  const server = http.createServer((req,res) => {
    if(req.url.split('?')[0] !== '/S01.html') {res.writeHead(404);res.end();return}
    res.setHeader('Content-Type','text/html; charset=utf-8');res.end(fs.readFileSync(file));
  });
  await new Promise(r => server.listen(0,'127.0.0.1',r));
  const base = 'http://127.0.0.1:' + server.address().port + '/S01.html';
  const browser = await chromium.launch({
    ...(process.env.MEDINA_CHROMIUM_PATH ? {executablePath:process.env.MEDINA_CHROMIUM_PATH} : {}),
    args:['--no-sandbox','--disable-dev-shm-usage','--no-zygote','--disable-gpu']
  });
  try {
    const context = await browser.newContext({viewport:{width:1360,height:900}, reducedMotion:'reduce'});
    await context.addInitScript(() => localStorage.setItem('medora.atlas.v3', JSON.stringify({bookmarks:['J45'],notes:{J45:'Repère respiratoire'}})));
    const page = await context.newPage();
    page.on('pageerror', e => errors.push(e.message));
    page.on('console', m => {if(m.type()==='error')errors.push(m.text())});
    const ready = async () => {await page.waitForFunction(() => window.MDN_READY === true);await page.waitForTimeout(550)};
    const shot = async name => {await page.waitForTimeout(550);await page.screenshot({path:path.join(out,'captures',name+'.jpg'),type:'jpeg',quality:82})};
    const go = async route => {await page.evaluate(r => {location.hash=r}, route);await page.waitForTimeout(120)};
    const noOverflow = async name => {const sizes=await page.evaluate(() => ({window:innerWidth,document:document.documentElement.scrollWidth}));check(name,sizes.document<=sizes.window+1,sizes)};
    await page.goto(base);await ready();
    const data = await page.evaluate(() => ({specialties:DATA.specialties.map(s=>s.id),codes:DATA.fragment.courses.map(c=>c.code)}));
    check('Une seule spécialité : cardiologie',JSON.stringify(data.specialties)==='["cardiologie"]');
    check('Accueil : 20 cours uniques',await page.locator('[data-s01-course]').count()===20 && new Set(data.codes).size===20);
    check('Accueil : huit catégories',await page.locator('.s01-category').count()===8);
    check('Navigation sans catalogue global',!await page.locator('.nav-main a[href="#/intelligence"],.nav-main a[href="#/federal"]').count());
    check('Accueil lisible sans filtre de flou',await page.locator('.s01-home').evaluate(e=>getComputedStyle(e).filter)==='none');
    await noOverflow('Accueil PC : aucun débordement');await shot('accueil_pc');
    await page.locator('[data-s01-category="vaisseaux"]').click();await page.waitForTimeout(180);
    const categoryBox=await page.locator('#s01-category-vaisseaux').boundingBox();
    check('Lien de catégorie : défilement vers les vaisseaux',categoryBox.y>=0 && categoryBox.y<800 && await page.evaluate(()=>scrollY>0),categoryBox);
    await go('#/home');
    await page.locator('[data-s01-course="I21"]').click();await page.locator('.mc[data-code="I21"]').waitFor();
    check('Premier cours : contenu écrit',await page.locator('.mc-ilot').count()>5);
    check('Navigo PC : panneau visible',await page.locator('.mc-navigo-panel').isVisible());
    check('Navigo PC : bouton mobile masqué',!await page.locator('.mc-navigo-trigger').isVisible());
    const desktopBox = await page.locator('.mc-navigo-panel').boundingBox();
    const contentBox = await page.locator('.mc').boundingBox();
    check('Navigo PC : espace séparé du texte',contentBox.x+contentBox.width<desktopBox.x,{contentBox,desktopBox});
    await shot('cours_pc');
    await page.locator('.mc-navigo-search').fill('diagnostic');
    const filtered = await page.locator('.mc-navigo-item:visible').allTextContents();
    check('Navigo : recherche des titres',filtered.length>0 && filtered.every(t=>t.toLowerCase().includes('diagnostic')),filtered);
    await page.locator('.mc-navigo-item:visible').first().click();
    check('Navigo : focus sur la partie demandée',await page.evaluate(()=>/^H[234]$/.test(document.activeElement.tagName)));
    check('Navigo PC reste ouvert après un saut',await page.locator('.mc-navigo-panel').isVisible());
    const movedBox = await page.locator('.mc-navigo-panel').boundingBox();
    check('Navigo PC reste fixe pendant le défilement',Math.abs(desktopBox.y-movedBox.y)<1);
    await page.locator('.mc-navigo-search').fill('');
    for(let i=0;i<4;i++) {
      await page.locator('.mc-navigo-tabs button').nth(i).click();
      const selected = await page.locator('.mc-tabs [aria-selected="true"]').getAttribute('data-p');
      check('Navigo : onglet '+(i+1),await page.locator('#'+selected).isVisible() && await page.locator('.mc-navigo-tabs .is-active').count()===1);
    }
    await page.locator('.mc-navigo-tabs button').first().click();
    await page.evaluate(()=>scrollTo(0,0));
    const windowLink = page.locator('.mc-panel:not([hidden]) .mc-w[data-k]').first();
    await windowLink.click();
    check('Fenêtre d’approfondissement : ouverture',await page.locator('.mc-dlg[open]').isVisible());
    await page.locator('.mc-dlg .mc-x').click();
    check('Fenêtre d’approfondissement : fermeture',!await page.locator('.mc-dlg[open]').count());
    await page.locator('.mc-tabs button').nth(1).click();
    const quiz = page.locator('.mc-panel:not([hidden]) .mc-quiz').first();
    await quiz.locator('.mc-opt').first().click();
    check('QCM : correction affichée',await quiz.locator('.mc-fb').isVisible() && await quiz.locator('.mc-opt.ok').count()>0);
    await page.locator('.mc-navigo-tabs button').first().click();
    await page.evaluate(()=>scrollTo(0,0));
    await page.locator('.mc-size-toggle').click();
    await page.locator('.mc-size-range').evaluate(e=>{e.value='24';e.dispatchEvent(new Event('input',{bubbles:true}))});
    check('Lecture : taille de police 24 px',await page.locator('.mc').evaluate(e=>e.style.getPropertyValue('--mc-fs'))==='24px');
    await page.keyboard.press('Escape');await noOverflow('Cours PC 24 px : aucun débordement');
    await page.locator('.mc-book').click();
    check('Lecture : mode Livre',await page.locator('.mc.book').count()===1);
    await page.locator('.mc-navigo-item').nth(5).click();
    check('Navigo fonctionne en mode Livre',await page.evaluate(()=>/^H[234]$/.test(document.activeElement.tagName)));
    await page.evaluate(()=>scrollTo(0,0));await page.locator('.mc-book').click();
    await page.locator('.mc-size-toggle').click();await page.locator('.mc-size-reset').click();await page.keyboard.press('Escape');
    for(const code of data.codes) {
      await go('#/entry/'+code);await page.locator('.mc[data-code="'+code+'"]').waitFor();
      check('Cours '+code+' : ouverture et Navigo',await page.locator('.mc-ilot').count()>0 && await page.locator('.mc-navigo-item').count()>0 && await page.locator('.mc-navigo').count()===1);
    }
    for(const [alias,code] of [['I22','I21'],['Q20','Q21']]) {
      await go('#/entry/'+alias);check('Alias '+alias+' ouvre '+code,await page.locator('.mc[data-code="'+code+'"]').count()===1);
    }
    for(const route of ['#/entry/J45','#/specialty/pediatrie-generale','#/federal','#/intelligence']) {
      await go(route);check('Route hors fragment '+route+' renvoie à l’accueil',await page.locator('.s01-home [data-s01-course]').count()===20);
    }
    await page.locator('#global-search').fill('I50');await page.locator('#global-search-form button[type="submit"]').click();
    await page.locator('.s01-search').waitFor();
    check('Recherche : résultats limités aux cours écrits',await page.locator('[data-s01-course]').count()===1 && await page.locator('[data-s01-course="I50"]').count()===1);
    check('Carnet de l’atlas conservé',await page.evaluate(()=>JSON.parse(localStorage.getItem('medora.atlas.v3')).notes.J45)==='Repère respiratoire');
    check('État du fragment sans entrée étrangère',await page.evaluate(()=>!state.bookmarks.includes('J45')&&!state.notes.J45));
    await go('#/entry/I21');
    for(const width of [1024,1100,1440]) {
      await page.setViewportSize({width,height:900});await noOverflow('Cours : largeur '+width);
      check('Navigo adaptatif à '+width,await page.locator('.mc-navigo-trigger').isVisible()=== (width<1100));
    }
    await page.setViewportSize({width:390,height:844});await go('#/home');await shot('accueil_mobile');await noOverflow('Accueil mobile : aucun débordement');
    await page.locator('[data-s01-course="I21"]').click();await page.locator('.mc').waitFor();await shot('cours_mobile');
    check('Navigo mobile : bouton rectangulaire visible',await page.locator('.mc-navigo-trigger').isVisible());
    check('Navigo mobile : panneau fermé au départ',!await page.locator('.mc-navigo-panel').isVisible());
    await noOverflow('Cours mobile : aucun débordement');
    await page.locator('.mc-navigo-trigger').click();await shot('navigo_mobile');
    check('Navigo mobile : ouverture du panneau',await page.locator('.mc-navigo-panel').isVisible());
    await page.locator('.mc-navigo-search').fill('diagnostic');await page.locator('.mc-navigo-item:visible').first().click();
    check('Navigo mobile : saut et fermeture',!await page.locator('.mc-navigo-panel').isVisible() && await page.evaluate(()=>/^H[234]$/.test(document.activeElement.tagName)));
    await page.locator('.mc-navigo-trigger').click();await page.keyboard.press('Escape');
    check('Navigo mobile : Échap referme le panneau',!await page.locator('.mc-navigo-panel').isVisible());
    await go('#/home');check('Retour à l’accueil détruit le Navigo',await page.locator('.mc-navigo').count()===0);
    check('Aucune erreur JavaScript ou console',errors.length===0,errors);
    const portable = await browser.newPage();
    portable.on('pageerror',e=>errors.push(e.message));
    await portable.goto(pathToFileURL(file).href);await portable.waitForFunction(()=>window.MDN_READY===true);
    await portable.locator('[data-s01-course="I21"]').click();await portable.locator('.mc[data-code="I21"]').waitFor();
    check('HTML autonome : lecture depuis file://',await portable.locator('.mc-navigo-panel').isVisible() && errors.length===0);
    const report={browser:await browser.version(),file,checks,errors,result:'passed'};
    fs.writeFileSync(path.join(out,'browser-results.json'),JSON.stringify(report,null,2)+'\n');
    console.log(JSON.stringify({result:'passed',checks:checks.length,captures:5,errors},null,2));
  } catch(e) {
    fs.writeFileSync(path.join(out,'browser-results.json'),JSON.stringify({checks,errors,result:'failed',failure:e.message},null,2)+'\n');
    throw e;
  } finally {await browser.close();server.close()}
})().catch(e=>{console.error(e);process.exitCode=1});
