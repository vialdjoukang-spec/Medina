from pathlib import Path
import http.server,socketserver,threading,functools,json,hashlib,datetime
from playwright.sync_api import sync_playwright
w=Path('/workspace/work/session3/e05-render');cap=w/'captures';cap.mkdir(exist_ok=True)
class Quiet(http.server.SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
server=socketserver.TCPServer(('127.0.0.1',0),functools.partial(Quiet,directory=str(w/'render/fragments')));threading.Thread(target=server.serve_forever,daemon=True).start();results=[]
try:
 with sync_playwright() as p:
  b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
  for width,height in [(1365,950),(390,844)]:
   pg=b.new_page(viewport={'width':width,'height':height});errors=[];pg.on('pageerror',lambda e:errors.append(str(e)));response=pg.goto(f'http://127.0.0.1:{server.server_address[1]}/MEDINA_S05_endocrinien-metabolique.html#/entry/E05');assert response.status==200;pg.wait_for_selector('.mc[data-code="E05"]');pg.locator('.mc-tabs [data-p="pA"]').click()
   paragraph=pg.locator('#e05-a10 p').filter(has_text='La place de la ciclosporine').first
   paragraph.scroll_into_view_if_needed();assert paragraph.is_visible();t=paragraph.inner_text().replace('\xad','');assert 'sort donc de ces indications autorisées' in t and 'ne détermine pas leur remboursement' in t
   assert pg.locator('#e05-a10 a[href*="compendium.ch/fr/product/"]').count()==4;pg.screenshot(path=str(cap/f'{width}-fi.png'))
   pg.locator('.mc [data-k="e05-contentieux-orbitopathie"]:visible').first.click();dialog=pg.locator('#mc-dialog');assert dialog.is_visible();t=dialog.inner_text().replace('\xad','');assert 'Au 16 octobre 2026' in t and '28 mars 2025' in t and 'ni son admission ni son rejet' in t and 'n’est pas acquise pour un patient donné' in t
   assert dialog.locator('a[href*="bag.admin.ch"]').count()==3;pg.screenshot(path=str(cap/f'{width}-ls.png'));pg.keyboard.press('Escape')
   pg.locator('.mc-book').click();assert pg.locator('.mc').get_attribute('class').split().count('book')==1
   # Scroll to actual A10 and source paragraph while horizontal pages are active; no pager buttons claimed.
   pg.locator('#e05-a10').evaluate("el=>el.scrollIntoView({block:'nearest',inline:'center',behavior:'instant'})");paragraph.scroll_into_view_if_needed();pg.wait_for_timeout(200);assert paragraph.is_visible();pg.screenshot(path=str(cap/f'{width}-book.png'))
   assert not errors,errors;assert pg.evaluate('document.documentElement.scrollWidth <= innerWidth+2')
   results.append({'viewport':[width,height],'A10_new_FI_text_visible':True,'four_primary_links':True,'actual_popup_trigger_clicked':True,'LS_dated_text_visible':True,'three_OFSP_links':True,'book_mode_A10_visible':True,'book_navigation_test':'horizontal scroll to A10, no pager-button test claimed','javascript_errors':errors,'document_overflow':False});pg.close()
  b.close()
finally:server.shutdown();server.server_close()
r=Path('/workspace/medina-alpha77/E05');report={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Rendu réel des deux seuls ajouts FI/LS ; aucune répétition d’audit du contenu inchangé.','source_files_sha256':{str(p.relative_to(r)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [r/'chapters/E05/E05_b.html',r/'chapters/E05/E05_pop2.html']},'built_file_sha256':hashlib.sha256((w/'render/fragments/MEDINA_S05_endocrinien-metabolique.html').read_bytes()).hexdigest(),'passed':True,'results':results,'medical_human_validation':False};(w/'browser.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'passed':True,'cases':len(results),'source_files_sha256':report['source_files_sha256']},ensure_ascii=False))
