const fs = require('node:fs'), http = require('node:http'), path = require('node:path');
const {fileURLToPath} = require('node:url');
const crypto = require('node:crypto');
const assets = new Map();
const servedAssets = [];
function indexAssets(file) {
 const html = fs.readFileSync(file, 'utf8');
 const match = html.match(/<script\b[^>]*id="medina-portable-resources"[^>]*>([\s\S]*?)<\/script>/);
 if (!match) return;
 const records = JSON.parse(match[1]);
 for (const [key, record] of Object.entries(records)) {
  const data=Buffer.from(record.base64,'base64');
  const digest=crypto.createHash('sha256').update(data).digest('hex');
  if (digest!==record.sha256) throw new Error('Embedded asset hash mismatch '+key);
  const names=[key,path.basename(key)];
  for(const name of names) assets.set(path.relative(output,path.resolve(path.dirname(file),name)).split(path.sep).join('/'),{data,type:record.type,sha256:digest,key});
 }
}

const {chromium} = require('playwright');
const output = fs.realpathSync(process.env.A41_CONTROL_OUT);
let server, ready, origin;
function start() {
  if (!ready) ready = new Promise((resolve, reject) => {
    server = http.createServer((request, response) => {
      try {
        const relative = decodeURIComponent(new URL(request.url, 'http://local').pathname).slice(1);
        const file = fs.realpathSync(path.resolve(output, relative));
        const inside = path.relative(output, file);
        if (inside === '..' || inside.startsWith('..' + path.sep) || path.isAbsolute(inside)) {
          response.writeHead(403); response.end(); return;
        }
        response.setHeader('Content-Type', 'text/html; charset=utf-8');
        response.end(fs.readFileSync(file));
      } catch (error) {
 const relative=decodeURIComponent(new URL(request.url,'http://local').pathname).slice(1);
 const asset=assets.get(relative);
 if(asset){response.setHeader('Content-Type',asset.type);response.end(asset.data);servedAssets.push({request:relative,key:asset.key,sha256:asset.sha256});}
 else{response.writeHead(404);response.end();}
 }
    });
    server.once('error', reject);
    server.listen(0, '127.0.0.1', () => {
      origin = 'http://127.0.0.1:' + server.address().port;
      resolve();
    });
  });
  return ready;
}
function wrapPage(page) {
  const goto = page.goto.bind(page);
  page.goto = async (value, options) => {
    let parsed = new URL(value);
    if (parsed.protocol === 'http:' && parsed.hostname === '127.0.0.1' && parsed.pathname === '/S01.html' && process.env.MEDINA_S01_FILE) {
      parsed = new URL(require('node:url').pathToFileURL(process.env.MEDINA_S01_FILE).href + parsed.search + parsed.hash);
    }
    if (parsed.protocol === 'file:') {
      const file = fs.realpathSync(fileURLToPath(parsed));
      indexAssets(file);
      const relative = path.relative(output, file);
      if (relative === '..' || relative.startsWith('..' + path.sep) || path.isAbsolute(relative)) {
        throw new Error('HTML demandé hors du répertoire de construction');
      }
      await start();
      value = origin + '/' + relative.split(path.sep).map(encodeURIComponent).join('/') + parsed.search + parsed.hash;
    }
    return goto(value, options);
  };
  return page;
}
function wrapContext(context) {
  const route = context.route.bind(context);
  route(/^https?:/, requestRoute => {
    if (new URL(requestRoute.request().url()).hostname === '127.0.0.1') return requestRoute.continue();
    return requestRoute.abort();
  });
  context.route = (pattern, handler, options) => route(pattern, async (requestRoute, ...args) => {
    if (origin && new URL(requestRoute.request().url()).origin === origin) return requestRoute.continue();
    return handler(requestRoute, ...args);
  }, options);
  const newPage = context.newPage.bind(context);
  context.newPage = async (...args) => wrapPage(await newPage(...args));
  return context;
}
const launch = chromium.launch.bind(chromium);
chromium.launch = async (...args) => {
  const browser = await launch(...args);
  const newContext = browser.newContext.bind(browser);
  browser.newContext = async (...values) => wrapContext(await newContext(...values));
  const newPage = browser.newPage.bind(browser);
  browser.newPage = async (...values) => wrapPage(await newPage(...values));
  const close = browser.close.bind(browser);
  browser.close = async (...values) => {
    try { return await close(...values); }
    finally {
      if (server) await new Promise(resolve => server.close(resolve));
      if(process.env.MEDINA_QA_OUT){fs.mkdirSync(process.env.MEDINA_QA_OUT,{recursive:true});fs.writeFileSync(path.join(process.env.MEDINA_QA_OUT,'transport.json'),JSON.stringify({transport:'HTTP loopback; unchanged assertions; embedded assets verified before serving',served_assets:servedAssets},null,2)+'\n');}
    }
  };
  return browser;
};
