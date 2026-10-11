import asyncio,json,re,hashlib,base64,gzip,urllib.request
from pathlib import Path
from playwright.async_api import async_playwright
from datetime import datetime,timezone
P=Path('/workspace/work/cycle1-audit-N17'); URL='http://127.0.0.1:8491/fragments/MEDINA_S04_renal-voies-urinaires.html'
async def run():
 r={'code':'N17','checked_at':datetime.now(timezone.utc).isoformat(),'url':URL,'captures':[]}
 body=urllib.request.urlopen(URL).read(); local=(P/'dist/fragments/MEDINA_S04_renal-voies-urinaires.html').read_bytes(); assert body==local
 pack=re.search(rb'<script id="mdn-pack"[^>]*>(.*?)</script>',body,re.S).group(1); payload=gzip.decompress(base64.b64decode(pack)).decode();
 r['served_html_sha256']=hashlib.sha256(body).hexdigest(); r['payload_sha256']=hashlib.sha256(payload.encode()).hexdigest(); r['templates_count']=payload.count('<template '); r['contains_current_core']=all(x in payload for x in ['N17-C0159','N17-C0432','30 mL','660']); assert r['templates_count']==57 and r['contains_current_core']
 async with async_playwright() as pw:
  b=await pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
  for label,w,h in [('desktop',1440,1000),('mobile',390,844)]:
   page=await b.new_page(viewport={'width':w,'height':h},reduced_motion="reduce");await page.goto(URL+'#/entry/N17');await page.wait_for_function('window.MDN_READY===true');await page.locator('.mc[data-code="N17"]').wait_for(state='visible');
   if await page.locator('.mc').evaluate('e=>e.classList.contains("book")'):await page.locator('.mc-book').click()
   await page.locator('.mc-tabs [data-p="pP"]').click();a=page.locator('.mc-panel:not([hidden]) .mc-ab[data-ab="FI"]').first;await a.scroll_into_view_if_needed();await a.click();await page.locator('.mc-dlg[open]').wait_for(state='visible');p=P/'captures'/f'{label}-3-FI-contexte.png';await page.wait_for_timeout(600);await page.screenshot(path=str(p));r['captures'].append({'path':str(p),'purpose':'FI globale approbation Swissmedic dans le cours utilisant une FI allemande'});await page.keyboard.press('Escape')
   await page.locator('.mc-tabs [data-p="pS"]').click();await page.locator('.mc-sci-bar [data-s="n17-s-histo"]').click();u=page.locator('#n17-s-histo');await u.scroll_into_view_if_needed();p=P/'captures'/f'{label}-4-histologie.png';await page.wait_for_timeout(600);await page.screenshot(path=str(p));r['captures'].append({'path':str(p),'purpose':'Tableau histologique présent ; schéma absent'});
   await page.locator('.mc-sci-bar [data-s="n17-s-bioch"]').click();a=page.locator('#n17-s-bioch .mc-ab[data-ab="K⁺"]').first;await a.scroll_into_view_if_needed();await a.click();await page.locator('.mc-dlg[open]').wait_for(state='visible');p=P/'captures'/f'{label}-5-K-cible.png';await page.wait_for_timeout(600);await page.screenshot(path=str(p));r['captures'].append({'path':str(p),'purpose':'Cible cardiologique 4–5 mmol/L transposée par glossaire partagé'});await page.keyboard.press('Escape');await page.close()
  await b.close()
 for c in r['captures']:c['sha256']=hashlib.sha256(Path(c['path']).read_bytes()).hexdigest()
 (P/'verification_payload_captures.json').write_text(json.dumps(r,ensure_ascii=False,indent=2));print(json.dumps({k:v for k,v in r.items() if k!='captures'},ensure_ascii=False))
asyncio.run(run())
