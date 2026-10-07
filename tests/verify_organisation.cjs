/* Offline navigation and catalogue integrity for the MEDINA organisation dashboard. */
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const {pathToFileURL} = require('node:url');
const {loadPlaywright, browserOptions} = require('./browser_runtime.cjs');
const {chromium} = loadPlaywright();
const root = path.resolve(__dirname, '..');
const targeted = process.argv.includes('--targeted');
const file = path.resolve(process.argv.slice(2).filter(arg => arg !== '--targeted')[0] || path.join(root, 'organisation/MEDINA_Organisation.html'));
const out = path.resolve(process.env.MEDINA_QA_OUT || path.join(root, 'audits/ORGANISATION_2026-10-07'));
const checks = [], errors = [], requests = [];
fs.mkdirSync(path.join(out, 'captures'), {recursive:true});
const check = (name, ok, detail) => {
  assert.ok(ok, name + (detail === undefined ? '' : ': ' + JSON.stringify(detail)));
  checks.push(name);
};
const source = fs.readFileSync(file, 'utf8');
const scripts = [...source.matchAll(/<script\b[^>]*type=["']application\/json["'][^>]*>([\s\S]*?)<\/script>/g)];
const data = scripts.map(x => JSON.parse(x[1])).find(x => x.catalogue && x.fragments);
assert.ok(data, 'Données du tableau de bord présentes');
const registry = JSON.parse(fs.readFileSync(path.join(root, 'organisation/fragments.json'), 'utf8'));
const canonicalSource = fs.readFileSync(path.join(root, 'shell/medina_front.html'), 'utf8');
const catalogue = JSON.parse(canonicalSource.match(/<script id="medora-data" type="application\/json">([\s\S]*?)<\/script>/)[1]);
const integrated = JSON.parse(fs.readFileSync(path.join(root, 'chapters.json'), 'utf8')).filter(c => c.integrated);
const blockCount = data.fragments.reduce((sum, f) => sum + f.blocks.length, 0);
const byId = Object.fromEntries(data.fragments.map(f => [f.id, f]));
const byCode = Object.fromEntries(catalogue.entries.map(e => [e.code, e]));
check('Les 22 fragments suivent le registre partagé', data.fragments.length === 22 && JSON.stringify(data.fragments.map(f => [f.id, f.label, f.order])) === JSON.stringify(registry.map(f => [f.id, f.label, f.order])));
check('Le catalogue affiche sa version réelle et aucune certification CIM-11', data.catalogue.full_cim11 === false && data.catalogue.version.includes('CIM-10-GM 2024'));
check('Le nombre de cours disponibles correspond aux sources intégrées', data.catalogue.integrated_courses === integrated.length && data.fragments.reduce((sum, f) => sum + f.integrated_count, 0) === integrated.length);
const allCategories = data.fragments.flatMap(f => f.blocks.flatMap(b => b.categories));
check('Toutes les catégories canoniques sont présentes, sans doublon', data.catalogue.total_categories === catalogue.entries.length && allCategories.length === catalogue.entries.length && new Set(allCategories.map(e => e.code)).size === catalogue.entries.length && allCategories.every(e => byCode[e.code] && byCode[e.code].title === e.title));
check('Les trois axes sans rattachement CIM sont explicites', ['T2', 'T5', 'T7'].every(id => byId[id].category_count === 0 && byId[id].blocks.length === 0));
for (const f of data.fragments) {
  const entries = f.blocks.flatMap(b => b.categories);
  check(f.label + ' : rangs uniques et continus', JSON.stringify(entries.map(e => e.order).sort((a, b) => a-b)) === JSON.stringify(entries.map((_, i) => i+1)));
  check(f.label + ' : catégories avec code et intitulé', entries.length === f.category_count && entries.every(e => e.code && e.title && Number.isInteger(e.order) && ['primary','covered','planned'].includes(e.status)));
  check(f.label + ' : blocs CIM avec code et intitulé', f.blocks.every(b => b.code && b.title && b.categories.length > 0));
  check(f.label + ' : liens vers les deux espaces de livraison', f.delivery_codex_url.includes('Livraison%20Codex/') && f.delivery_claude_url.includes('Livraison%20Claude/'));
}
const cross = byId.S10.blocks.flatMap(b => b.categories).find(e => e.code === 'M30');
check('M30 garde son rattachement et renvoie au cours M31 d’immunologie', cross?.status === 'covered' && cross.course?.code === 'M31' && cross.course.fragment_id === 'S07' && cross.course.title && cross.course.url.endsWith('#/entry/M31'));
check('La pneumologie distingue les quatre cours disponibles des leçons à produire', byId.S02.integrated_count === 4 && byId.S02.blocks.flatMap(b => b.categories).filter(e => e.status === 'primary').length === 4 && byId.S02.blocks.flatMap(b => b.categories).some(e => e.status === 'planned'));

async function overflow(page, name) {
  const sizes = await page.evaluate(() => ({width:innerWidth, document:document.documentElement.scrollWidth}));
  check(name, sizes.document <= sizes.width + 1, sizes);
}
async function shot(page, name) {
  await page.screenshot({path:path.join(out, 'captures', name + '.png'), fullPage:false});
}
const escapeAttribute = value => value.replaceAll('\\', '\\\\').replaceAll('"', '\\"');
const fragmentSelector = '[data-fragment-id],button.fragment-button[data-fragment]';
const blockSelector = '[data-block-code],button.block-card[data-block]';
const categorySelector = '[data-category-code],button.lesson-main[data-category]';
const fragmentButton = (page, id) => page.locator('[data-fragment-id="' + escapeAttribute(id) + '"],button.fragment-button[data-fragment="' + escapeAttribute(id) + '"]');
const blockButton = (page, code) => page.locator('[data-block-code="' + escapeAttribute(code) + '"],button.block-card[data-block="' + escapeAttribute(code) + '"]');
const categoryRow = (page, code) => page.locator('[data-category-code="' + escapeAttribute(code) + '"],button.lesson-main[data-category="' + escapeAttribute(code) + '"]');

(async () => {
  const browser = await chromium.launch(browserOptions(chromium));
  try {
    const context = await browser.newContext({viewport:{width:1440, height:1000}, reducedMotion:'reduce'});
    await context.route(/^https?:/, route => {requests.push(route.request().url());return route.abort();});
    const page = await context.newPage();
    page.on('pageerror', e => errors.push(e.message));
    await page.goto(pathToFileURL(file).href);
    await fragmentButton(page, 'S01').waitFor();
    check('Le fichier autonome démarre sans erreur', errors.length === 0, errors);
    check('Les 22 noms de fragments figurent dans la bande latérale', await page.locator(fragmentSelector).count() === 22 && (await page.locator(fragmentSelector).allTextContents()).every((text, i) => text.includes(registry[i].label)));
    check('Le catalogue CIM-10-GM reste visible', (await page.locator('body').innerText()).includes('CIM-10-GM 2024'));
    await overflow(page, 'Accueil bureau sans débordement horizontal');
    if (!targeted) for (const f of data.fragments) {
      await fragmentButton(page, f.id).click();
      await page.waitForFunction(label => document.getElementById('view-title')?.textContent === label, f.label);
      check(f.label + ' : fragment actif', await fragmentButton(page, f.id).getAttribute('aria-current') === 'page');
      const labels = await page.locator(blockSelector).allTextContents();
      check(f.label + ' : tous les blocs CIM accessibles', labels.length === f.blocks.length && f.blocks.every(b => labels.some(text => text.includes(b.code) && text.includes(b.title))), {expected:f.blocks.length, actual:labels.length});
      if (f.blocks.length === 0) {
        check(f.label + ' : absence de catalogue explicitée', (await page.locator('main').innerText()).includes('Aucune catégorie'));
      }
      for (const b of f.blocks) {
        await fragmentButton(page, f.id).click();
        await blockButton(page, b.code).click();
        await categoryRow(page, b.categories[0].code).waitFor();
        const rows = await page.locator('.lesson-row').allTextContents();
        const ranks = await page.locator('.lesson-row .rank strong').allTextContents();
        check(f.label + ' / ' + b.code + ' : titres et ordre de toutes les leçons', rows.length === b.categories.length && b.categories.every((e, i) => rows[i].includes(e.code) && rows[i].includes(e.title) && ranks[i] === String(e.order).padStart(2, '0')), {expected:b.categories.length, actual:rows.length});
      }
    }
    await page.goto(pathToFileURL(file).href + '#fragment=S10&block=M30-M36&category=M30');
    await categoryRow(page, 'M30').waitFor();
    check('Un lien profond retrouve M30 et son cours M31 nommé', (await categoryRow(page, 'M30').innerText()).includes(cross.course.title) && await categoryRow(page, 'M30').locator('..').locator('a[href="' + cross.course.url + '"]').count() === 1);
    await page.reload();
    await categoryRow(page, 'M30').waitFor();
    check('Le fil d’Ariane conserve code et intitulé complet de la leçon', (await page.locator('.breadcrumbs').innerText()).includes(cross.code) && (await page.locator('.breadcrumbs').innerText()).includes(cross.title));
    check('Le lien profond résiste au rechargement du fichier', await fragmentButton(page, 'S10').getAttribute('aria-current') === 'page');
    await fragmentButton(page, 'S02').click();
    await blockButton(page, byId.S02.blocks.find(b => b.categories.some(e => e.code === 'J45')).code).click();
    await categoryRow(page, 'J45').waitFor();
    const pulmonaryHash = await page.evaluate(() => location.hash);
    await fragmentButton(page, 'S01').click();
    await page.goBack();
    await categoryRow(page, 'J45').waitFor();
    check('Précédent restaure fragment et catégorie', await page.evaluate(() => location.hash) === pulmonaryHash);
    await shot(page, 'pneumologie_desktop');
    await fragmentButton(page, 'S01').focus();
    await page.keyboard.press('Enter');
    await page.waitForFunction(() => document.getElementById('view-title')?.textContent === 'C-01-Cardiologie');
    check('Le clavier ouvre un fragment et place le focus sur son titre', await page.locator('#view-title').evaluate(e => e === document.activeElement));
    const firstCard = page.locator(blockSelector).first();
    const firstBlock = await firstCard.getAttribute('data-block-code') || await firstCard.getAttribute('data-block');
    await firstCard.focus();
    await page.keyboard.press('Space');
    await page.waitForFunction(code => new URLSearchParams(location.hash.slice(1)).get('block') === code && document.querySelector('.lesson-main'), firstBlock);
    check('Le clavier ouvre un bloc et ses leçons', await page.locator(categorySelector).count() > 0);
    const firstLesson = page.locator(categorySelector).first();
    const firstCode = await firstLesson.getAttribute('data-category-code') || await firstLesson.getAttribute('data-category');
    await firstLesson.focus();
    await page.keyboard.press('Enter');
    await page.waitForFunction(code => new URLSearchParams(location.hash.slice(1)).get('category') === code && document.getElementById('category-title')?.textContent.includes(code), firstCode);
    check('Le clavier ouvre la fiche et place le focus sur son titre complet', await page.locator('#category-title').evaluate(e => e === document.activeElement) && (await page.locator('#category-title').innerText()).includes(byCode[firstCode].title));
    await fragmentButton(page, 'S02').click();
    await page.locator('#related-title').waitFor();
    const related = await page.locator('[data-related-code]').allTextContents();
    check('Les rattachements pulmonaires à d’autres fragments sont visibles et nommés', related.length === byId.S02.related.length && byId.S02.related.every(e => related.some(text => text.includes(e.code) && text.includes(e.title))));
    const tuberculosis = byId.S02.related.find(e => e.code === 'A15');
    await page.locator('[data-related-code="A15"] a').click();
    await categoryRow(page, 'A15').waitFor();
    check('Le renvoi pulmonaire A15 rejoint l’infectiologie avec sa leçon complète', await fragmentButton(page, 'T1').getAttribute('aria-current') === 'page' && (await page.locator('#category-title').innerText()).includes(tuberculosis.title));
    await page.locator('#lesson-search').fill('Néphrologie');
    await page.waitForFunction(() => document.getElementById('view-title')?.textContent === 'Néphrologie');
    const withAccent = await page.locator(categorySelector).allTextContents();
    await page.locator('#lesson-search').fill('nephrologie');
    await page.waitForFunction(() => document.getElementById('view-title')?.textContent === 'nephrologie');
    check('La recherche ignore les accents et conserve les intitulés', JSON.stringify(withAccent) === JSON.stringify(await page.locator(categorySelector).allTextContents()) && withAccent.length === byId.S04.category_count);
    await page.locator('#lesson-search').fill('Pneumologie');
    await page.waitForFunction(() => document.getElementById('view-title')?.textContent === 'Pneumologie');
    check('La recherche retrouve toutes les catégories pulmonaires', await page.locator(categorySelector).count() === byId.S02.category_count);
    const asthma = byId.S02.blocks.flatMap(b => b.categories).find(e => e.code === 'J45');
    const absentCourse = byId.S02.blocks.flatMap(b => b.categories).find(e => e.status === 'planned');
    check('La recherche distingue cours disponible et leçon à produire', (await categoryRow(page, 'J45').innerText()).includes(asthma.title) && (await categoryRow(page, 'J45').innerText()).includes('Cours propre intégré') && (await categoryRow(page, absentCourse.code).innerText()).includes('À produire'));
    await categoryRow(page, 'J45').click();
    await page.locator('#category-title').waitFor();
    check('Un résultat de recherche rejoint sa fiche nommée', (await page.locator('#category-title').innerText()).includes(asthma.code) && (await page.locator('#category-title').innerText()).includes(asthma.title));
    await page.reload();
    await categoryRow(page, 'J45').waitFor();
    check('Une fiche issue de la recherche garde son lien profond', (await page.locator('#category-title').innerText()).includes(asthma.title));
    await page.setViewportSize({width:390, height:844});
    await overflow(page, 'Pneumologie mobile sans débordement horizontal');
    await shot(page, 'pneumologie_mobile');
    check('La navigation mobile est masquée et inactive avant ouverture', await page.locator('#fragment-sidebar').evaluate(e => e.inert) && await page.locator('#menu-toggle').getAttribute('aria-expanded') === 'false');
    await page.locator('#menu-toggle').click();
    check('La navigation mobile s’ouvre avec ses 22 fragments accessibles', await page.locator('#menu-toggle').getAttribute('aria-expanded') === 'true' && !(await page.locator('#fragment-sidebar').evaluate(e => e.inert)) && await page.locator(fragmentSelector).count() === 22);
    await overflow(page, 'Navigation mobile sans débordement horizontal');
    await shot(page, 'fragments_mobile');
    await page.keyboard.press('Escape');
    check('Échap ferme la navigation et restaure le focus', await page.locator('#menu-toggle').getAttribute('aria-expanded') === 'false' && await page.locator('#menu-toggle').evaluate(e => e === document.activeElement));
    await page.locator('#menu-toggle').click();
    await fragmentButton(page, 'S10').click();
    await page.waitForFunction(() => document.getElementById('view-title')?.textContent === 'R-14-Rhumatologie et orthopédie');
    check('Le choix mobile ouvre le fragment et ferme le menu', await page.locator('#menu-toggle').getAttribute('aria-expanded') === 'false' && (await page.locator('#view-title').innerText()) === byId.S10.label);
    await overflow(page, 'Rhumatologie mobile sans débordement horizontal');
    await page.locator('#menu-toggle').click();
    await page.locator('#close-nav').click();
    check('Le bouton Fermer rend la page mobile interactive', !(await page.locator('#main-content').evaluate(e => e.inert)) && await page.locator('#menu-toggle').getAttribute('aria-expanded') === 'false');
    check('Le fichier autonome ne demande aucune ressource distante', requests.length === 0, requests);
    check('Toutes les interactions restent sans erreur JavaScript', errors.length === 0, errors);
    fs.writeFileSync(path.join(out, targeted ? 'targeted_result.json' : 'result.json'), JSON.stringify({file, scope:targeted ? 'interactions ciblées' : 'navigation exhaustive des ' + blockCount + ' blocs', checks:checks.length, blocks:blockCount, fragments:data.fragments.length, catalogue:catalogue.entries.length, courses:integrated.length, errors, requests}, null, 2) + '\n');
    console.log(JSON.stringify({result:'OK', targeted, checks:checks.length, file, out, categories:catalogue.entries.length, fragments:22, courses:integrated.length}));
  } finally {await browser.close();}
})().catch(error => {console.error(error);process.exitCode=1;});
