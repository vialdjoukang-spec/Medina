/* Visible provisional I51 reservations in the original consuming fragment.
 * Real Chromium clicks and captures; no medical certification or content edits.
 */
const fs = require('node:fs'), path = require('node:path'), assert = require('node:assert/strict'), crypto = require('node:crypto');
const {pathToFileURL} = require('node:url');
const {loadPlaywright, browserOptions} = require('./browser_runtime.cjs');
const root = path.resolve(__dirname, '..');
const input = path.join(root, 'dist/fragments/MEDINA_S01_cardiovasculaire.html');
const output = path.resolve(process.env.MEDINA_QA_OUT || path.join(root, 'docs/collaboration/reviews/2026-10-08/C01_PROVISOIRE/reserves'));
const pageUrl = process.env.MEDINA_RESERVE_URL || pathToFileURL(input).href;
const digest = bytes => crypto.createHash('sha256').update(bytes).digest('hex');
async function visibleText(locator) { return (await locator.innerText()).replace(/\u00ad/g, ''); }
const report = {scope: 'I51 visible clinical reservations, course tabs, native popup, glossary return, contrast, mobile touch viewport, light appearance and screenshots. Not medical certification.', result: 'running', url: pageUrl, checks: [], viewports: [], captures: [], errors: []};
const reservations = [
  {id: 'i51-reserve-choc', key: 'C01-I51-CHOC', panel: 'pA'},
  {id: 'i51-reserve-aod', key: 'C01-I51-AOD-DOSE', panel: 'pP'},
  {id: 'i51-reserve-levo', key: 'C01-I51-LEVOSIMENDAN-STATUT', panel: 'pP'}
];
function check(label, ok, details) { assert.ok(ok, label + ': ' + JSON.stringify(details)); report.checks.push({label, details}); }
async function settle(page) { await page.evaluate(() => document.fonts.ready); await page.evaluate(() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)))); }
async function overflow(page, label) {
  const width = await page.evaluate(() => ({viewport: innerWidth, document: document.documentElement.scrollWidth}));
  check(label + ' no page horizontal overflow', width.document <= width.viewport + 1, width);
}
async function capture(page, name, label) {
  await settle(page); const file = name + '.png'; await page.screenshot({path: path.join(output, file), fullPage: false});
  report.captures.push({file, label, sha256: digest(fs.readFileSync(path.join(output, file)))});
}
function contrast(fg, bg) {
  const rgb = value => value.match(/[\d.]+/g).slice(0, 3).map(Number).map(v => v / 255).map(v => v <= .04045 ? v / 12.92 : ((v + .055) / 1.055) ** 2.4);
  const light = value => {const [r,g,b] = rgb(value); return .2126*r+.7152*g+.0722*b;};
  const a=light(fg),b=light(bg);return (Math.max(a,b)+.05)/(Math.min(a,b)+.05);
}
(async () => {
  fs.mkdirSync(output, {recursive: true});
  report.input = {path: path.relative(root, input), sha256_before: digest(fs.readFileSync(input))};
  const {chromium} = loadPlaywright(), browser = await chromium.launch(browserOptions(chromium));
  report.browser_version = browser.version();
  try {
    for (const viewport of [{width:1440,height:900,isMobile:false,hasTouch:false},{width:390,height:844,isMobile:true,hasTouch:true}]) {
      const context = await browser.newContext({viewport:{width:viewport.width,height:viewport.height}, isMobile:viewport.isMobile, hasTouch:viewport.hasTouch, deviceScaleFactor:1, colorScheme:'light', reducedMotion:'reduce'});
      await context.route(/^https?:/, route => new URL(pageUrl).protocol === 'https:' && new URL(route.request().url()).origin === new URL(pageUrl).origin ? route.continue() : route.abort());
      const page = await context.newPage(); page.setDefaultTimeout(15000); page.on('pageerror', error => report.errors.push(error.message));
      await page.goto(pageUrl.split('#')[0]+'#/entry/I51'); await page.waitForFunction(() => window.MDN_READY === true);
      const course = page.locator('.mc[data-code="I51"]'); await course.waitFor({state:'visible'});
      if (await course.evaluate(el=>el.classList.contains('book'))) await course.locator('.mc-book').click();
      const detail = {viewport, reservations:[], tabs:[], glossary:[]}; report.viewports.push(detail);
      for (const panel of ['pA','pE','pS','pP']) {
        await course.locator('.mc-tabs button[data-p="'+panel+'"]').click();
        const active = course.locator('.mc-panel:not([hidden])');
        check(viewport.width+' correct tab '+panel, await active.getAttribute('id') === panel);
        check(viewport.width+' tab content '+panel, (await active.innerText()).trim().length > 100);
        await overflow(page, viewport.width+' '+panel); detail.tabs.push(panel);
      }
      for (const reservation of reservations) {
        await course.locator('.mc-tabs button[data-p="'+reservation.panel+'"]').click();
        const marker = course.locator('#'+reservation.id); await marker.scrollIntoViewIfNeeded(); await marker.waitFor({state:'visible'});
        const observed = await marker.evaluate(el => {const css=getComputedStyle(el),rect=el.getBoundingClientRect();return {id:el.id,key:el.dataset.claudeReservation,status:el.dataset.reservationStatus,owner:el.dataset.reviewOwner,text:el.innerText.replace(/\u00ad/g,''),color:css.color,background:css.backgroundColor,border:css.borderColor,rect:{x:rect.x,width:rect.width},viewport:innerWidth};});
        check(viewport.width+' correct machine-detectable reservation '+reservation.id, observed.key===reservation.key && observed.status==='open' && observed.owner==='Claude', observed);
        check(viewport.width+' visible clinical reservation '+reservation.id, /Réserve clinique/.test(observed.text) && /reprendre par Claude/.test(observed.text));
        check(viewport.width+' red visual marker '+reservation.id, observed.color==='rgb(139, 16, 27)' && observed.background==='rgb(255, 241, 242)', observed);
        const ratio=contrast(observed.color, observed.background);check(viewport.width+' readable reservation contrast '+reservation.id, ratio>=4.5, ratio);
        check(viewport.width+' reservation fits viewport '+reservation.id, observed.rect.x>=-1 && observed.rect.x+observed.rect.width<=observed.viewport+1, observed);
        detail.reservations.push({...observed,contrast:ratio}); await overflow(page, viewport.width+' '+reservation.id);
        await capture(page,'i51-'+viewport.width+'-'+reservation.id,reservation.key);
      }
      await course.locator('.mc-tabs button[data-p="pP"]').click();
      const trigger = course.locator('.mc-panel:not([hidden]) [data-k="i51-levosimendan"]').first(); await trigger.scrollIntoViewIfNeeded(); await trigger.click();
      const dialog=page.locator('.mc-dlg[open]'); await dialog.waitFor({state:'visible'});
      check(viewport.width+' native levo explanation', /lévosimendan/i.test(await visibleText(dialog)) || /levosimendan/i.test(await visibleText(dialog)));
      check(viewport.width+' no absent popup', !(await visibleText(dialog)).includes('Fiche absente.'));
      await capture(page,'i51-'+viewport.width+'-explication','Real native popup opened from a green word');
      await page.keyboard.press('Escape'); await dialog.waitFor({state:'hidden'});
      check(viewport.width+' Escape focus return', await trigger.evaluate(el=>el===document.activeElement));
      await course.locator('.mc-tabs button[data-p="pA"]').click();
      for (const ab of ['GEIST','HR']) {
        const button=course.locator('.mc-panel:not([hidden]) [data-ab="'+ab+'"]').first(); await button.scrollIntoViewIfNeeded(); await button.click(); await dialog.waitFor({state:'visible'});
        check(viewport.width+' glossary '+ab, (await visibleText(dialog)).includes(ab+' — ') && !(await visibleText(dialog)).includes('Fiche absente.'));
        const expandedText = await visibleText(dialog);
        check(viewport.width+' existing glossary deepening '+ab, /Approfondissement/i.test(expandedText) && /GEIST 2025/i.test(expandedText), expandedText);
        const nested=dialog.locator('[data-ab]').first(); check(viewport.width+' nested glossary child '+ab, await nested.count() === 1);
        await nested.click(); await page.locator('.mc-back:not([hidden])').waitFor({state:'visible'});
        check(viewport.width+' nested glossary not absent '+ab, !(await visibleText(dialog)).includes('Fiche absente.'));
        await page.locator('.mc-back').click(); check(viewport.width+' glossary return '+ab, (await visibleText(dialog)).includes(ab+' — '));
        await page.keyboard.press('Escape'); await dialog.waitFor({state:'hidden'}); detail.glossary.push(ab);
      }
      await overflow(page, viewport.width+' final'); await context.close();
    }
    check('No JavaScript error', report.errors.length===0, report.errors);
  } finally { await browser.close(); }
  report.input.sha256_after=digest(fs.readFileSync(input));check('Compiled input stable',report.input.sha256_before===report.input.sha256_after);
  report.result='passed';
})().catch(error => { report.result='failed'; report.failure=String(error.stack || error); process.exitCode=1; }).finally(() => {
  report.completed_at=new Date().toISOString();fs.mkdirSync(output,{recursive:true});fs.writeFileSync(path.join(output,'i51_reservations_results.json'),JSON.stringify(report,null,2)+'\n');
  console.log(JSON.stringify({result:report.result,checks:report.checks.length,failure:report.failure,report:path.relative(root,path.join(output,'i51_reservations_results.json'))}));
});
