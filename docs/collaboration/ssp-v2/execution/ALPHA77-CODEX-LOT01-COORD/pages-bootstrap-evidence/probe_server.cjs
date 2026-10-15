const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const crypto = require('node:crypto');
const {createRequire} = require('node:module');
const candidate = path.resolve(process.argv[2]);
const built = '/workspace/work/pages-bootstrap-site';
const directory = '/workspace/work/sciences-bootstrap-fix/http-site';
const originalDirectory = path.join(built, 'fragments');
const htmlName = fs.readdirSync(originalDirectory).find(name => /^MEDINA_S06_.*\.html$/.test(name));
assert.ok(htmlName, 'Real built S06 document required');
const svgName = 'fragments/assets/img/c77/alpha/claude/lymph_node_regions_seer.svg';
const files = new Map([
 ['fragments/' + htmlName, fs.readFileSync(path.join(originalDirectory, htmlName))],
 [svgName, fs.readFileSync(path.join(built, svgName))],
 ['templates/fixture.html', Buffer.from('<p>Non-fragment HTML without runtime marker.</p>')],
 ['assets/fixture.js', Buffer.from('const value = \'<script id="medina-fragment-runtime">\';')],
 ['assets/fixture.png', Buffer.from([0, 255, 1, 128, 2])],
 ['assets/fixture.bin', Buffer.from([255, 0, 128, 10])]
]);
for (const [relative, bytes] of files) {
 const target = path.join(directory, relative);
 fs.mkdirSync(path.dirname(target), {recursive:true});
 fs.writeFileSync(target, bytes);
}
process.env.MEDINA_OUT = directory;
process.env.MEDINA_QA_FRAGMENTS = 'S06';
process.env.MEDINA_QA_OUT = '/workspace/work/sciences-bootstrap-fix/http-audit';
const code = fs.readFileSync(candidate, 'utf8');
const cut = code.indexOf('\n(async () => {');
assert.ok(cut > 0, 'Isolate the real server before the browser entrypoint');
const context = {require:createRequire(candidate), __dirname:path.dirname(candidate), process, console, Buffer, URL, setTimeout, clearTimeout};
vm.runInNewContext(code.slice(0, cut) + '\nglobalThis.probedServer = server;', context, {filename:candidate});
const server = context.probedServer;
(async () => {
 await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
 const origin = 'http://127.0.0.1:' + server.address().port;
 const rows = [];
 try {
  for (const [relative, original] of files) {
   const began = performance.now();
   const response = await fetch(origin + '/' + relative);
   const bytes = Buffer.from(await response.arrayBuffer());
   const elapsed = performance.now() - began;
   assert.equal(response.status, 200, relative);
   assert.deepEqual(bytes, original, 'Exact response bytes: ' + relative);
   const expected = relative.endsWith('.svg') ? 'image/svg+xml' : relative.endsWith('.html') ? 'text/html' : relative.endsWith('.js') ? 'text/javascript' : relative.endsWith('.png') ? 'image/png' : 'application/octet-stream';
   assert.equal(response.headers.get('content-type').split(';')[0], expected, relative);
   if (relative === 'fragments/' + htmlName) assert.ok(elapsed >= 250, 'Real fragment still streamed with the 300ms pause');
   rows.push({path:relative, status:response.status, mime:response.headers.get('content-type'), bytes:bytes.length, sha256:crypto.createHash('sha256').update(bytes).digest('hex'), elapsed_ms:Math.round(elapsed)});
  }
  fs.writeFileSync('/workspace/work/sciences-bootstrap-fix/http-report.json', JSON.stringify({result:'passed', source_commit:'50de4ee524bada80bad6766fd4da62df6dca5091', results:rows}, null, 2) + '\n');
  console.log(JSON.stringify(rows, null, 2));
 } finally { await new Promise(resolve => server.close(resolve)); }
})().catch(error => {console.error(error); process.exitCode = 1; server.close();});
