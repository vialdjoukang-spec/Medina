"""Mesure de la mise en page du texte des cours : largeur utile, caractères par ligne,
écarts de justification (rapport à l'espace normale), mots par écran.
Usage : python3 mesure_texte.py <fichier.html> [CODE ...]"""
import sys, json
from playwright.sync_api import sync_playwright
F = sys.argv[1]; CODES = sys.argv[2:] or ['J45', 'I26']
JS = r"""
() => {
  const vis = e => e.offsetParent && e.getClientRects().length;
  const ps = [...document.querySelectorAll('.mc .mc-panel:not([hidden]) .mc-ilot p')].filter(vis).slice(0, 60);
  const cv = document.createElement('canvas').getContext('2d');
  let lines = 0, chars = 0, gaps = [], wide = 0, jl = 0, hyph = 0;
  for (const p of ps) {
    const cs = getComputedStyle(p); const lh = parseFloat(cs.lineHeight) || parseFloat(cs.fontSize) * 1.6;
    const n = Math.max(1, Math.round(p.getBoundingClientRect().height / lh)); lines += n; chars += p.textContent.replace(/\u00AD/g, '').length;
    hyph += (p.textContent.match(/­/g) || []).length;
    if (cs.textAlign !== 'justify') continue;
    cv.font = `${cs.fontStyle} ${cs.fontWeight} ${cs.fontSize} ${cs.fontFamily}`; const sp = cv.measureText(' ').width;
    const w = document.createTreeWalker(p, NodeFilter.SHOW_TEXT); let tn = 0; const words = [];
    while (w.nextNode()) { const node = w.currentNode; tn++; if (node.parentElement !== p) continue; const re = /\S+/g; let m;
      while ((m = re.exec(node.data))) { const r = document.createRange(); r.setStart(node, m.index); r.setEnd(node, m.index + m[0].length);
        const rs = [...r.getClientRects()]; if (!rs.length) continue; words.push({ tn, l: rs[0].left, r: rs[rs.length - 1].right, t: Math.round(rs[rs.length - 1].top), t0: Math.round(rs[0].top) }); } }
    const byLine = {}; for (let i = 0; i + 1 < words.length; i++) { const a = words[i], b = words[i + 1]; if (a.tn !== b.tn || Math.abs(a.t - b.t0) > 3) continue; (byLine[a.t] = byLine[a.t] || []).push((b.l - a.r) / sp); }
    const tops = Object.keys(byLine).map(Number).sort((x, y) => x - y); tops.pop(); // dernière ligne non justifiée
    for (const t of tops) { const g = byLine[t]; jl++; gaps.push(...g); if (Math.max(...g) > 2) wide++; }
  }
  gaps.sort((a, b) => a - b); const q = x => gaps.length ? +gaps[Math.floor(x * (gaps.length - 1))].toFixed(2) : null;
  const p0 = ps[0], il = p0 && p0.closest('.mc-ilot'); const r = p0 ? p0.getBoundingClientRect() : {}; const ri = il ? il.getBoundingClientRect() : {};
  // mots par écran : mots des paragraphes visibles ramenés à la hauteur de la fenêtre
  const body = document.querySelector('.mc .mc-panel:not([hidden])'); const words = body ? body.innerText.split(/\s+/).length : 0; const h = body ? body.getBoundingClientRect().height : 1;
  return { vw: innerWidth, textLeft: Math.round(r.left), textRight: Math.round(innerWidth - r.right), textWidth: Math.round(r.width), ilotLeft: Math.round(ri.left), ilotPad: il && getComputedStyle(il).paddingLeft,
    fs: p0 && getComputedStyle(p0).fontSize, lh: p0 && getComputedStyle(p0).lineHeight, cpl: lines ? Math.round(chars / lines) : null,
    gapMedian: q(.5), gapP90: q(.9), gapP99: q(.99), linesWithGap2x: jl ? Math.round(100 * wide / jl) + ' %' : null, justifiedLines: jl, softHyphens: hyph,
    wordsPerScreen: Math.round(words * innerHeight / h) };
}
"""
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
    for vw in [(1360, 900), (1024, 800), (390, 844)]:
        pg = b.new_page(viewport={'width': vw[0], 'height': vw[1]})
        pg.goto('file://' + F); pg.wait_for_timeout(700)
        for code in CODES:
            pg.goto('file://' + F + '#/entry/' + code); pg.wait_for_timeout(1500)
            print(code, json.dumps(pg.evaluate(JS), ensure_ascii=False))
        pg.close()
    b.close()
