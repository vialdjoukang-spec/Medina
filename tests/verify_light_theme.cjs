/* Vérifie les HTML globaux et fragmentés avec une ancienne préférence sombre. */
const fs = require('node:fs');
const http = require('node:http');
const path = require('node:path');
const assert = require('node:assert/strict');
const crypto = require('node:crypto');
const {loadPlaywright, browserOptions} = require('./browser_runtime.cjs');
const {chromium} = loadPlaywright();
const directory = path.resolve(process.env.MEDINA_OUT || 'dist');
const out = path.resolve(process.env.MEDINA_QA_OUT || 'audits/THEME_CLAIR_2026-10-08');
const fragments = JSON.parse(fs.readFileSync('fragments.json', 'utf8'));
const files = new Map([
  ['/MEDINA.html', path.join(directory, 'MEDINA.html')],
  ...fragments.map(f => [`/${f.id}.html`, path.join(directory, 'fragments', `MEDINA_${f.id}_${f.slug}.html`)])
]);
const checks = [], errors = [], knownLimitations = [], sha256 = {};
const check = (name, ok, detail) => {assert.ok(ok, name + (detail ? ': ' + JSON.stringify(detail) : ''));checks.push(name)};
fs.mkdirSync(out, {recursive:true});

async function light(page, name) {
  const result = await page.evaluate(() => {
    const root = document.documentElement, scheme = getComputedStyle(root).colorScheme;
    const canvas = document.createElement('canvas'), ctx = canvas.getContext('2d');
    const luminance = color => {
      ctx.clearRect(0, 0, 1, 1);ctx.fillStyle = color;ctx.fillRect(0, 0, 1, 1);
      const rgba = ctx.getImageData(0, 0, 1, 1).data;
      const rgb = [...rgba].slice(0, 3).map(v => {v /= 255;return v <= .04045 ? v / 12.92 : ((v + .055) / 1.055) ** 2.4});
      return .2126 * rgb[0] + .7152 * rgb[1] + .0722 * rgb[2];
    };
    const body = getComputedStyle(document.body).backgroundColor;
    const dialogs = [...document.querySelectorAll('dialog[open]')].map(dialog => ({class:dialog.className,
      luminance:luminance(getComputedStyle(dialog).backgroundColor)}));
    return {scheme, body, luminance:luminance(body), dialogs, oldPreference:localStorage.getItem('medina.dark'),
      controls:document.querySelectorAll('.mdn-darkbtn,[aria-label="Mode sombre"]').length,
      oldClasses:document.querySelectorAll('.mdn-dark,.mdn-dk-bg,.mdn-dk-ink,.mdn-dk-tint,.mdn-dk-line').length};
  });
  check(name + ' : schéma clair exclusif', result.scheme.includes('light') && result.scheme.includes('only') && !result.scheme.includes('dark'), result);
  check(name + ' : surface claire', result.luminance > .6, result);
  if (result.dialogs.length) check(name + ' : fenêtres sur papier clair', result.dialogs.every(dialog => dialog.luminance > .6), result.dialogs);
  check(name + ' : ancien choix supprimé', result.oldPreference === null);
  check(name + ' : aucun contrôle ni classe sombre', result.controls === 0 && result.oldClasses === 0);
}

(async () => {
  for (const [url, file] of files) {
    const html = fs.readFileSync(file, 'utf8');
    sha256[url] = crypto.createHash('sha256').update(html).digest('hex');
    check(url + ' : HTML sans moteur ni styles sombres', !/mdn-dark|autoDark|mdn-dk-/.test(html));
  }
  const server = http.createServer((req, res) => {
    const file = files.get(req.url.split('?')[0]);
    if (!file) {res.writeHead(404);res.end();return}
    res.setHeader('Content-Type', 'text/html; charset=utf-8');res.end(fs.readFileSync(file));
  });
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  let browser;
  try {
    browser = await chromium.launch(browserOptions(chromium));
    const context = await browser.newContext({colorScheme:'dark', reducedMotion:'reduce', viewport:{width:1360,height:900}});
    await context.addInitScript(() => {
      localStorage.setItem('medina.dark', '1');
      localStorage.setItem('medora.atlas.v3', JSON.stringify({theme:'night', notes:{J45:'Carnet à conserver'}}));
    });
    const page = await context.newPage();page.on('pageerror', e => {
      // La coque globale importe ce lecteur historique absent du dépôt, avant toute navigation.
      if (/^Failed to fetch dynamically imported module: http:\/\/127\.0\.0\.1:\d+\/lesson-core\.js$/.test(e.message)) {
        knownLimitations.push({page:page.url(),message:e.message});
      } else errors.push(e.message);
    });
    for (const [url] of files) {
      await page.goto('http://127.0.0.1:' + server.address().port + url);
      await page.waitForFunction(() => !!document.documentElement.dataset.theme);
      await page.waitForTimeout(450);
      await light(page, url + ' au chargement');
      const paletteResults = await page.evaluate(() => {
        const original = state.theme, failures = [], canvas = document.createElement('canvas'), ctx = canvas.getContext('2d');
        for (const theme of V4_THEMES) {
          state.theme = theme.id;applyTheme();
          ctx.fillStyle = getComputedStyle(document.body).backgroundColor;ctx.fillRect(0, 0, 1, 1);
          const rgb = [...ctx.getImageData(0, 0, 1, 1).data].slice(0, 3).map(v => {v /= 255;return v <= .04045 ? v / 12.92 : ((v + .055) / 1.055) ** 2.4});
          const luminance = .2126 * rgb[0] + .7152 * rgb[1] + .0722 * rgb[2];
          if (luminance <= .6) failures.push({theme:theme.id,luminance});
        }
        state.theme = original;applyTheme();return {count:V4_THEMES.length,failures};
      });
      check(url + ' : 100 palettes conservent une surface claire', paletteResults.count === 100 && paletteResults.failures.length === 0, paletteResults);
      await page.evaluate(() => showThemeStudio());
      check(url + ' : sélecteur chromatique conservé', await page.locator('.theme-card').count() === 100);
      await page.locator('.theme-card').last().click();
      check(url + ' : choix chromatique effectif', await page.evaluate(() => document.documentElement.dataset.theme === 'theme-100'));
      await page.evaluate(() => closeModal());
      await light(page, url + ' après choix chromatique');
      if (url === '/MEDINA.html' || url === '/S01.html') {
        await page.setViewportSize({width:390,height:844});await light(page, url + ' mobile');
        await page.screenshot({path:path.join(out, url === '/MEDINA.html' ? 'global-clair-mobile.png' : 's01-clair-mobile.png')});
        await page.setViewportSize({width:1360,height:900});
      }
      if (url === '/S01.html') {
        await page.evaluate(() => location.hash = '#/clinical-skills');
        await page.locator('[data-cs-model="thorax"]').first().click();
        await page.locator('.cs-dialog[open]').waitFor();await light(page, 'S01 : scène thorax');
        await page.keyboard.press('Escape');
        await page.evaluate(() => location.hash = '#/entry/I83');
        await page.locator('.mc[data-code="I83"]').waitFor();
        const tabs = page.locator('.mc-tabs button');
        check('I83 : quatre onglets de cours disponibles', await tabs.count() === 4);
        for (let i = 0; i < 4; i++) {await tabs.nth(i).click();await light(page, 'I83 : onglet ' + (i + 1))}
        await tabs.first().click();
        await page.locator('.mc-panel:not([hidden]) .mc-w[data-k]').first().click();
        await page.locator('.mc-dlg[open]').waitFor();await light(page, 'I83 : fenêtre explicative');
        await page.keyboard.press('Escape');
      }
    }
    check('Carnet historique conservé', await page.evaluate(() => JSON.parse(localStorage.getItem('medora.atlas.v3')).notes.J45 === 'Carnet à conserver'));
    check('Aucune erreur JavaScript inattendue', errors.length === 0, errors);
    check('HTML inchangés pendant le contrôle', [...files].every(([url, file]) => crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex') === sha256[url]));
    fs.writeFileSync(path.join(out, 'light-theme-browser-results.json'), JSON.stringify({result:'passed',browser:await browser.version(),files:Object.fromEntries(files),sha256,checks,errors,knownLimitations,scope:'Contrôle technique du thème clair ; aucune validation médicale.'}, null, 2) + '\n');
    console.log(JSON.stringify({result:'passed',files:files.size,palettes_per_file:100,checks:checks.length,errors,knownLimitations}, null, 2));
  } catch (error) {
    fs.writeFileSync(path.join(out, 'light-theme-browser-results.json'), JSON.stringify({result:'failed',checks,errors,knownLimitations,failure:error.message}, null, 2) + '\n');
    throw error;
  } finally {if (browser) await browser.close();server.close()}
})().catch(error => {console.error(error);process.exitCode = 1});
