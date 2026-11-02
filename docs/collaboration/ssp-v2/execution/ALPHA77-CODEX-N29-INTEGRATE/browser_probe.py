"""Native autonomous MEDINA preview exercised at an intercepted HTTP origin.
All network requests except the document are blocked; image pixels are untouched.
This is not a claim of HTTP deployment, remote availability, or medical review.
"""
from pathlib import Path
from urllib.parse import urlparse, unquote
import json, mimetypes
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parents[5]
OUT=Path(__file__).resolve().parent
NATIVE=OUT/'N29-apercu-autonome.html'
CAP=OUT/'captures'; CAP.mkdir(exist_ok=True)
report={'mode':'Chromium intercepted HTTP URL serving native autonomous HTML from disk; all other network requests blocked; incorporated image bytes decoded after scroll; no live deployment claim','viewports':[],'errors':[]}
with sync_playwright() as p:
    browser=p.chromium.launch(headless=True, executable_path="/usr/bin/chromium", args=["--no-sandbox"])
    for width,height in [(1440,900),(390,844)]:
        page=browser.new_page(viewport={'width':width,'height':height},device_scale_factor=1)
        page.on('pageerror',lambda e:report['errors'].append(str(e)))
        def route(req):
            path=unquote(urlparse(req.request.url).path).lstrip('/')
            local=ROOT/path
            if path == 'native.html':
                req.fulfill(body=NATIVE.read_bytes(),content_type='text/html')
            # All requests other than the intercepted native document are blocked.
            # N29 originals must load from their incorporated data URIs.
            else:
                req.abort()
        page.route('**/*',route)
        page.goto('http://medina.local/native.html',wait_until='domcontentloaded',timeout=60000)
        page.evaluate("location.hash='#/entry/N29'")
        page.wait_for_timeout(1500)
        item={'width':width,'course_visible':page.locator('.mc').count()==1,'screenshots':[]}
        if not item['course_visible']:
            item['body_sample']=page.inner_text('body')[:1000];report['viewports'].append(item);continue
        path=CAP/f'N29-{width}-opening.png';page.screenshot(path=str(path));item['screenshots'].append(str(path.relative_to(OUT)))
        page.locator('.mc-tabs button[data-p="pS"]').click()
        page.wait_for_timeout(300)
        item['science_buttons']=page.locator('.mc-sci-bar button').all_text_contents()
        item['semio_visible']=page.locator('[id="n29-s-semio"]').is_visible()
        item['semio_sections']=page.locator('[data-semiology]').count()
        item['images']=[]
        item['annotation_checks']=[]
        path=CAP/f'N29-{width}-semio.png';page.screenshot(path=str(path));item['screenshots'].append(str(path.relative_to(OUT)))
        page.locator('[data-n29-figure]').filter(visible=True).first.scroll_into_view_if_needed()
        page.wait_for_timeout(400)
        path=CAP/f'N29-{width}-figure.png';page.screenshot(path=str(path));item['screenshots'].append(str(path.relative_to(OUT)))
        # Exercise each science discipline, scroll to each original, then await decode.
        item['discipline_states']=[]
        for sid in page.locator('.mc-sci-bar button').evaluate_all('(xs)=>xs.map(x=>x.dataset.s)'):
            page.locator(f'.mc-sci-bar button[data-s="{sid}"]').click()
            page.wait_for_timeout(80)
            item['discipline_states'].append({'id':sid,'visible':page.locator(f'[id="{sid}"]').is_visible()})
            for img in page.locator(f'[id="{sid}"] [data-n29-figure] img').all():
                img.scroll_into_view_if_needed()
                img.evaluate('(x)=>x.decode()')
                item['annotation_checks'].extend(img.locator('xpath=ancestor::figure').locator('[data-n29-marker]').evaluate_all('(xs)=>xs.map(x=>{const r=x.getBoundingClientRect(),im=x.parentElement.querySelector("img").getBoundingClientRect();return {position:getComputedStyle(x).position,inside:r.x+r.width/2>=im.x&&r.x+r.width/2<=im.right&&r.y+r.height/2>=im.y&&r.y+r.height/2<=im.bottom}})'))
                item['images'].append(img.evaluate('(x)=>({figure:x.closest("figure").dataset.n29Figure,loaded:x.complete&&x.naturalWidth>0,width:x.naturalWidth,height:x.naturalHeight,incorporated:x.currentSrc.startsWith("data:image/")})'))
                figure=img.locator('xpath=ancestor::figure')
                index=figure.get_attribute('data-n29-figure')
                if index in ['kidney','nephron','schisto','urinary']:
                    shot=CAP/f'N29-{width}-original-{index}.png'
                    figure.screenshot(path=str(shot));
                    if str(shot.relative_to(OUT)) not in item['screenshots']:item['screenshots'].append(str(shot.relative_to(OUT)))
        page.locator('.mc-sci-bar button[data-s="n29-s-semio"]').click()
        item['horizontal_overflow']=page.evaluate('document.documentElement.scrollWidth-innerWidth')
        item['annotations_visible']=page.locator('[data-n29-marker]').filter(visible=True).count()
        for panel in ['pE','pP','pA','pS']:
            page.locator(f'.mc-tabs button[data-p="{panel}"]').click();page.wait_for_timeout(80)
            if panel in ['pA','pE']:
                for img in page.locator(f'[id="{panel}"] [data-n29-figure] img').all():
                    img.scroll_into_view_if_needed();img.evaluate('(x)=>x.decode()')
                    item['annotation_checks'].extend(img.locator('xpath=ancestor::figure').locator('[data-n29-marker]').evaluate_all('(xs)=>xs.map(x=>{const r=x.getBoundingClientRect(),im=x.parentElement.querySelector("img").getBoundingClientRect();return {position:getComputedStyle(x).position,inside:r.x+r.width/2>=im.x&&r.x+r.width/2<=im.right&&r.y+r.height/2>=im.y&&r.y+r.height/2<=im.bottom}})'))
                    item['images'].append(img.evaluate('(x)=>({figure:x.closest("figure").dataset.n29Figure,loaded:x.complete&&x.naturalWidth>0,width:x.naturalWidth,height:x.naturalHeight,incorporated:x.currentSrc.startsWith("data:image/")})'))
                    if img.locator('xpath=ancestor::figure').get_attribute('data-n29-figure')=='bladder':
                        shot=CAP/f'N29-{width}-original-bladder.png';img.locator('xpath=ancestor::figure').screenshot(path=str(shot));item['screenshots'].append(str(shot.relative_to(OUT)))
        page.locator('.mc-tabs button[data-p="pA"]').click()
        popup=page.locator('.mc-w').filter(visible=True).first
        popup.click();page.wait_for_timeout(150)
        item['popup_visible']=page.locator('.mc-dlg-b').is_visible()
        item['popup_missing']='Fiche absente' in page.inner_text('.mc-dlg-b')
        path=CAP/f'N29-{width}-popup.png';page.screenshot(path=str(path));item['screenshots'].append(str(path.relative_to(OUT)))
        page.keyboard.press('Escape')
        page.locator('.mc-book').click();page.wait_for_timeout(150)
        item['book_active']='book' in page.locator('.mc').get_attribute('class').split()
        page.locator('.mc-size-toggle').click()
        page.evaluate("(()=>{const r=document.querySelector('.mc-size-range');r.value=24;r.dispatchEvent(new Event('input'))})()")
        page.keyboard.press('Escape');page.wait_for_timeout(200)
        item['book_font']=page.evaluate("getComputedStyle(document.querySelector('.mc')).getPropertyValue('--mc-fs').trim()")
        item['book_overflow']=page.evaluate('document.documentElement.scrollWidth-innerWidth')
        item['book_clinical_visible']=page.locator('[id="pA"]').is_visible()
        path=CAP/f'N29-{width}-livre24.png';page.screenshot(path=str(path));item['screenshots'].append(str(path.relative_to(OUT)))
        page.locator('.mc-tabs button[data-p="pS"]').click();page.wait_for_timeout(120)
        page.locator('.mc-sci-bar button[data-s="n29-s-semio"]').click()
        page.locator('[id="n29-semio-normal"]').scroll_into_view_if_needed()
        item['book_semio_visible']=page.locator('[id="n29-s-semio"]').is_visible()
        path=CAP/f'N29-{width}-livre24-semio.png';page.screenshot(path=str(path));item['screenshots'].append(str(path.relative_to(OUT)))
        item['passed']=bool(item['course_visible'] and item['semio_visible'] and item['semio_sections']==9 and len(item['science_buttons'])==6 and all(x['loaded'] and x['incorporated'] for x in item['images']) and item['popup_visible'] and not item['popup_missing'] and item['book_active'] and item['book_font']=='24px' and item['horizontal_overflow']==0 and item['book_overflow']==0 and item['book_semio_visible'] and len(item['images'])==8 and len(item['annotation_checks'])==26 and all(x['position']=='absolute' and x['inside'] for x in item['annotation_checks']))
        report['viewports'].append(item);page.close()
    browser.close()
report['passed']=all(x.get('passed') for x in report['viewports']) and not report['errors']
(OUT/'browser-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
raise SystemExit(not report['passed'])
