/* First painted fragment content must never come from an earlier atlas surface. */
const fs = require('node:fs');
const path = require('node:path');
const http = require('node:http');
const assert = require('node:assert/strict');
const {loadPlaywright, browserOptions} = require('./browser_runtime.cjs');
const {chromium} = loadPlaywright();
const root = path.resolve(__dirname, '..');
const directory = path.resolve(process.env.MEDINA_OUT || path.join(root, 'dist'));
const out = path.resolve(process.env.MEDINA_QA_OUT || path.join(root, 'work/frontend-bootstrap-audit'));
const registry = JSON.parse(fs.readFileSync(path.join(root, 'fragments.json'))).filter(fragment => !process.env.MEDINA_QA_FRAGMENTS || process.env.MEDINA_QA_FRAGMENTS.split(',').includes(fragment.id));
const results = [], cache = new Map();
fs.mkdirSync(out, {recursive:true});
function source(file) {
 if (!cache.has(file)) cache.set(file, fs.readFileSync(file));
 return cache.get(file);
}
const server = http.createServer((req, res) => {
 const file = path.resolve(directory, '.' + decodeURIComponent(new URL(req.url, 'http://local').pathname));
 if (!file.startsWith(directory + path.sep) || !fs.existsSync(file)) {res.writeHead(404);res.end();return;}
 const bytes = source(file), marker = bytes.indexOf('<script id="medina-fragment-runtime">');
 assert.ok(marker >= 0, 'Missing local runtime marker in ' + file);
 res.setHeader('Content-Type', 'text/html;charset=utf-8');
 // Deliberately pause after the historical atlas has executed and before the local
 // fragment overrides arrive. A check that only waits for DOMContentLoaded misses this bug.
 res.write(bytes.subarray(0, marker));
 setTimeout(() => res.end(bytes.subarray(marker)), 300);
});
(async () => {
 await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
 const origin = 'http://127.0.0.1:' + server.address().port;
 const browser = await chromium.launch(browserOptions(chromium));
 try {
  for (const fragment of registry) {
   const name = '/fragments/MEDINA_' + fragment.id + '_' + fragment.slug + '.html';
   const raw = source(path.join(directory, name)).toString();
   const organisation = JSON.parse(raw.match(/<script id="medina-category-organisation-data" type="application\/json">([\s\S]*?)<\/script>/)[1]);
   const lesson = organisation.blocks.flatMap(block => block.lessons).find(item => item.integrated);
   const category = organisation.blocks[0];
   const routes = ['', '#/home', '#/entry/ZZZ_FOREIGN', '#/specialty/foreign'];
   if (category) routes.push('#/home?category=' + encodeURIComponent(category.code));
   if (lesson) routes.push('#/entry/' + lesson.code, '#/pathology/' + lesson.code.toLowerCase());
   if (fragment.id === 'S01') routes.push('#/clinical-skills');
   for (const hash of routes) {
    const context = await browser.newContext({viewport:{width:1440,height:1000}, reducedMotion:'reduce'});
    await context.addInitScript(({id, delayTemplates}) => {
     if (delayTemplates) {
      const nativeText = Response.prototype.text;
      Response.prototype.text = function(...args) {return nativeText.apply(this, args).then(value => new Promise(resolve => setTimeout(() => resolve(value), 350)));};
     }
     localStorage.setItem('medina.fragment.' + id + '.atlas', JSON.stringify({last:'ZZZ_FOREIGN', recent:['ZZZ_FOREIGN']}));
     window.__bootstrapPaints = [];
     const record = () => {
      const content = document.getElementById('content');
      if (content) {
       const oldSurface = content.querySelector('.hero,.s01-home,.s01-search,.sys-shell,.sys-loading,.empty');
       const ready = content.querySelector('.mcg-home,.mc,.nosology-course-star,.cs-page');
       const loading = content.querySelector('.loading,[role="status"]');
       const item = {at:Math.round(performance.now()), title:content.querySelector('h1,h2')?.textContent || '',
        oldSurface:oldSurface?.className || '', ready:!!ready, bootstrapped:!!window.MEDINA_FRAGMENT_READY, loading:!!loading, text:content.innerText.slice(0,170)};
       const last = window.__bootstrapPaints.at(-1);
       if (!last || last.text !== item.text || last.oldSurface !== item.oldSurface) window.__bootstrapPaints.push(item);
      }
      requestAnimationFrame(record);
     };
     requestAnimationFrame(record);
    }, {id:fragment.id, delayTemplates:hash.startsWith('#/entry/') || hash.startsWith('#/pathology/')});
    const page = await context.newPage(), errors = [];
    page.on('pageerror', error => errors.push(error.message));
    await page.goto(origin + name + hash);
    await page.waitForFunction(() => window.MEDINA_CATEGORY_ORGANISATION && (!document.querySelector('#mdn-pack') || window.MDN_READY));
    await page.waitForTimeout(100);
    const paints = await page.evaluate(() => window.__bootstrapPaints);
    const result = {fragment:fragment.id, hash, paints, errors, finalHash:await page.evaluate(() => location.hash)};
    results.push(result);
    assert.equal(errors.length, 0, fragment.id + hash + ': JavaScript errors ' + errors.join('; '));
    assert.ok(paints.length && paints.some(paint => paint.ready), fragment.id + hash + ': no final local surface painted');
    assert.ok(paints.every(paint => !paint.oldSurface), fragment.id + hash + ': obsolete surface painted ' + JSON.stringify(paints));
    assert.ok(paints.every(paint => !paint.ready || paint.bootstrapped), fragment.id + hash + ': local surface painted before the final routing engine');
    assert.ok(paints.every(paint => paint.ready || paint.loading), fragment.id + hash + ': unexpected intermediary ' + JSON.stringify(paints));
    // None of these direct routes should trigger a legacy pilot redirection.
    assert.equal(result.finalHash, hash, fragment.id + hash + ': unexpected hash redirect');
    const isHome = !hash || hash === '#/home' || hash.includes('FOREIGN') || hash.includes('specialty');
    if (isHome) assert.equal((await page.locator('.mcg-cover h1').innerText()).replace(/\.$/, ''), organisation.fragment.display_name);
    if (hash.startsWith('#/entry/') && lesson && hash.endsWith(lesson.code)) assert.equal(await page.locator('.mc').getAttribute('data-code'), lesson.code);
    // Verify a second navigation while gzip has finished: route changes must remain local.
    await page.evaluate(() => {location.hash = '#/home';});
    await page.locator('.mcg-cover').waitFor();
    await page.evaluate(() => {location.hash = '#/entry/ZZZ_FOREIGN';});
    await page.waitForFunction(() => location.hash === '#/entry/ZZZ_FOREIGN' && document.querySelector('.mcg-cover'));
    assert.equal(await page.locator('html').getAttribute('data-medina-fragment'), fragment.id);
    await context.close();
   }
   console.log(fragment.id + ': ' + routes.length + ' direct routes passed');
  }
 } finally {
  fs.writeFileSync(path.join(out, 'bootstrap-browser.json'), JSON.stringify({checks:results.length,results},null,2));
  await browser.close();server.close();
 }
 console.log(results.length + ' cold streamed routes passed, across ' + registry.length + ' fragments.');
})().catch(error => {console.error(error);process.exitCode=1;server.close();});
