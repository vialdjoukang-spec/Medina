import asyncio,json,hashlib,sys,re
from pathlib import Path
from datetime import datetime,timezone
from playwright.async_api import async_playwright
sys.path.insert(0,'/workspace/Medina/tools')
from capture_lecon import click_word,settle
D=Path('/workspace/Medina/livraisons/Livraison Codex/E-06-Endocrinologie et métabolisme/travail/CYCLE_01_E11')
OUT=Path('/workspace/Medina/work/c01_r_endo_resume/browser');OUT.mkdir(parents=True,exist_ok=True)
URL='http://127.0.0.1:8478/fragments/MEDINA_S05_endocrinien-metabolique.html#/entry/E11'
async def run():
 report={'code':'E11','checked_at':datetime.now(timezone.utc).isoformat(),'browser':'/usr/bin/chromium','url':URL,'viewports':{},'errors':[]}
 async with async_playwright() as pw:
  browser=await pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
  for label,width,height in [('desktop',1440,1000),('mobile',390,844)]:
   page=await browser.new_page(viewport={'width':width,'height':height},color_scheme='light',reduced_motion='reduce');page.set_default_timeout(8000)
   errs=[];page.on('pageerror',lambda e:errs.append(str(e)))
   await page.goto(URL,wait_until='domcontentloaded');await page.wait_for_function('()=>window.MDN_READY===true');course=page.locator('.mc[data-code="E11"]');await course.wait_for(state='visible')
   if await course.evaluate("e=>e.classList.contains('book')"):await page.locator('.mc-book').click()
   data={'viewport':{'width':width,'height':height},'panels':[],'windows':{},'abbreviations':{},'quizzes':[],'sciences':[],'captures':[],'figures':[],'keyboard':[]}
   routes=[]
   async def check_figures(container,location):
    for svg in await container.locator('svg').all():
     if not await svg.is_visible():continue
     metrics=await svg.evaluate("e=>({viewBoxWidth:e.viewBox.baseVal.width,renderedWidth:e.getBoundingClientRect().width,labels:Array.from(e.querySelectorAll('text')).map(t=>({text:t.textContent,font:parseFloat(getComputedStyle(t).fontSize),effective:parseFloat(getComputedStyle(t).fontSize)*e.getBoundingClientRect().width/e.viewBox.baseVal.width}))})")
     assert all(x['effective']>=12 for x in metrics['labels']),(label,location,metrics)
     data['figures'].append({'location':location,**metrics})
   async def real_click(trigger):
    if await trigger.evaluate("e=>e.tagName.toLowerCase()==='tspan'"):
     await trigger.evaluate("e=>e.closest('svg').scrollIntoView({block:'center',behavior:'instant'})");await page.wait_for_timeout(100)
     rect=await trigger.bounding_box();assert rect and 0<rect['y']<height,(rect,height)
     await page.mouse.click(rect['x']+rect['width']/2,rect['y']+rect['height']/2)
    else:await click_word(trigger)
   async def check_window(trigger,key):
    if key in data['windows']:return
    await trigger.evaluate("e=>(e.closest('svg')||e).scrollIntoView({block:'center',inline:'center',behavior:'instant'})");await page.wait_for_timeout(80);await real_click(trigger);dlg=page.locator('.mc-dlg[open]');await dlg.wait_for(state='visible');body=await dlg.locator('.mc-dlg-b').inner_text();title=await dlg.locator('#mc-dlg-t').inner_text()
    assert len(body)>40 and 'Fiche absente.' not in body,(key,title,body)
    data['windows'][key]={'title':title,'length':len(body),'pass':True}
    await check_figures(dlg,key)
    for child in await dlg.locator('[data-k]').all():
     ck=await child.get_attribute('data-k')
     if ck not in data['windows']:routes.append({'panel':panel,'science':current_science,'keys':[key,ck]})
    if len(data['captures'])==1:
     fn=OUT/(label+'-2-explication.png');pass;pass
    await page.keyboard.press('Escape')
   async def check_ab(trigger,key):
    if key in data['abbreviations']:return
    await trigger.evaluate("e=>(e.closest('svg')||e).scrollIntoView({block:'center',inline:'center',behavior:'instant'})");await page.wait_for_timeout(80);await real_click(trigger);dlg=page.locator('.mc-dlg[open]');await dlg.wait_for(state='visible');body=await dlg.locator('.mc-dlg-b').inner_text();assert len(body)>40 and 'Fiche absente.' not in body,(key,body)
    data['abbreviations'][key]={'length':len(body),'pass':True};await page.keyboard.press('Escape')
   for panel in ['pA','pE','pS','pP']:
    current_science=None
    await page.locator('.mc-tabs button[data-p="'+panel+'"]').click();active=course.locator('.mc-panel:not([hidden])');assert await active.count()==1
    assert await active.get_attribute('data-p')==panel or await active.get_attribute('id')==panel,(panel,await active.evaluate('e=>e.outerHTML.slice(0,150)'))
    data['panels'].append({'id':panel,'text_length':len(await active.inner_text())})
    if panel=='pA':
     await page.evaluate('scrollTo(0,0)');await settle(page);fn=OUT/(label+'-1-ouverture.png');pass;pass
     data['style']=await active.locator('p').first.evaluate("e=>({body:getComputedStyle(e).color,font:getComputedStyle(e).fontFamily,term:getComputedStyle(document.querySelector('.mc [data-k]')).color})")
    groups=[None]
    if panel=='pS':groups=await active.locator('.mc-sci-bar button[data-s]').evaluate_all('es=>es.map(e=>e.dataset.s)')
    for science in groups:
     if science:
      current_science=science
      await active.locator('button[data-s="'+science+'"]').click();unit=active.locator('#'+science);assert await unit.is_visible();data['sciences'].append({'id':science,'text_length':len(await unit.inner_text())})
     else:unit=active
     await check_figures(unit,science or panel)
     for selector,name,fn in [('[data-k]','windows',check_window),('.mc-ab[data-ab]','abbreviations',check_ab)]:
      items=unit.locator(selector);count=await items.count()
      for i in range(count):
       trigger=items.nth(i);key=await trigger.get_attribute('data-k' if name=='windows' else 'data-ab')
       if key not in data[name] and await trigger.is_visible():
        try:await fn(trigger,key)
        except Exception as exc:
         print('FAILED',label,panel,science,key,await trigger.evaluate("e=>({html:e.outerHTML,rect:e.getBoundingClientRect().toJSON(),hit:document.elementFromPoint(e.getBoundingClientRect().x+3,e.getBoundingClientRect().y+3)?.outerHTML.slice(0,400)})"),flush=True);pass;(OUT/'browser-partial.json').write_text(json.dumps(data,ensure_ascii=False,indent=2));raise
     for q in await unit.locator('.mc-quiz').all():
      opts=q.locator('.mc-opt');n=await opts.count()
      for i in range(n):
       opt=opts.nth(i);await opt.scroll_into_view_if_needed();await opt.click(position={'x':5,'y':5});fb=q.locator('.mc-fb');assert await fb.is_visible()
       assert await q.locator('.mc-opt.ok[data-ok="1"]').count()==1
      data['quizzes'].append({'options':n,'feedback':True})
    for trigger in await active.locator('[data-k]').all():
     key=await trigger.get_attribute('data-k')
     if key not in data['windows'] and await trigger.is_visible():await check_window(trigger,key)
    await page.evaluate('scrollTo(0,0)')
   index=0
   while index<len(routes):
    route=routes[index];index+=1
    if route['keys'][-1] in data['windows']:continue
    await page.locator('.mc-tabs button[data-p="'+route['panel']+'"]').click()
    if route['science']:
     await course.locator('button[data-s="'+route['science']+'"]').click()
    valid=True
    for depth,key in enumerate(route['keys']):
     container=page.locator('.mc-dlg[open]') if depth else course
     candidates=container.locator('[data-k="'+key+'"]')
     candidates=[x for x in await candidates.all() if await x.is_visible()]
     if not candidates: valid=False;break
     await real_click(candidates[0]);dlg=page.locator('.mc-dlg[open]');await dlg.wait_for(state='visible');body=await dlg.locator('.mc-dlg-b').inner_text()
     assert len(body)>40 and 'Fiche absente.' not in body,(key,body)
     data['windows'][key]={'title':await dlg.locator('#mc-dlg-t').inner_text(),'length':len(body),'pass':True,'nested_route':route['keys'][:depth+1]}
    if valid:
     for child in await page.locator('.mc-dlg[open] [data-k]').all():
      ck=await child.get_attribute('data-k')
      if ck not in data['windows']:routes.append({**route,'keys':route['keys']+[ck]})
    if await page.locator('.mc-dlg[open]').count():await page.keyboard.press('Escape')
   data['nested_routes_processed']=index
   await page.locator('.mc-tabs button[data-p="pS"]').click()
   await course.locator('button[data-s="e11-s-histo"]').click()
   for key in ['e11-gl-2','e11-ratios-physio']:
    candidates=[x for x in await course.locator('[data-k="'+key+'"]').all() if await x.is_visible()]
    if not candidates:continue
    await candidates[0].scroll_into_view_if_needed();await candidates[0].focus();await page.keyboard.press('Enter');dlg=page.locator('.mc-dlg[open]');await dlg.wait_for(state='visible');assert len(await dlg.locator('.mc-dlg-b').inner_text())>40;await page.keyboard.press('Escape');data['keyboard'].append({'key':key,'enter':True,'escape':True})
   await page.locator('.mc-tabs button[data-p="pA"]').click()
   await page.locator('.mc-navigo-trigger').click();await page.wait_for_timeout(120)
   navitems=page.locator('.mc-navigo-item');nnav=await navitems.count();assert nnav>0
   await navitems.nth(nnav-1).click();await page.wait_for_timeout(200)
   assert await page.evaluate("!!document.activeElement&&/^H[234]$/.test(document.activeElement.tagName)")
   if await page.locator('.mc-navigo-panel:not([hidden])').count():await page.keyboard.press('Escape')
   await page.locator('.mc-size-toggle').click()
   await page.evaluate("(()=>{const r=document.querySelector('.mc-size-range');r.value=21;r.dispatchEvent(new Event('input'))})()")
   assert await course.evaluate("e=>getComputedStyle(e).getPropertyValue('--mc-fs').trim()")=='21px'
   await page.locator('.mc-size-reset').click()
   assert await course.evaluate("e=>getComputedStyle(e).getPropertyValue('--mc-fs').trim()")=='17px'
   await page.keyboard.press('Escape')
   await page.locator('.mc-book').click();assert await course.evaluate("e=>e.classList.contains('book')")
   for panel in ['pA','pE','pS','pP']:
    await page.locator('.mc-tabs button[data-p="'+panel+'"]').click()
    assert await course.locator('.mc-panel:not([hidden])').count()==1
   await page.locator('.mc-book').click();assert not await course.evaluate("e=>e.classList.contains('book')")
   data['reader_controls']={'navigo_entries':nnav,'focus_heading':True,'font_size_21px_reset_17px':True,'book_mode_four_tabs':True}
   # Chaque template doit avoir été atteint par un vrai déclencheur dans le cours.
   allkeys=await page.locator('template[data-pop]').evaluate_all('es=>es.map(e=>e.dataset.pop)')
   data['unopened_templates']=[k for k in allkeys if k.startswith(('e11-','pareto-e11-')) and k not in data['windows']]
   data['overflow']=await page.evaluate('({document:document.documentElement.scrollWidth,viewport:innerWidth})')
   data['gauges']=await page.locator('.nosology-progress[data-mcg-filter] progress').evaluate_all("es=>es.map(e=>({border:getComputedStyle(e).borderColor,appearance:getComputedStyle(e).appearance,track:getComputedStyle(e,'::-webkit-progress-bar').backgroundColor,value:e.value,max:e.max}))")
   data['javascript_errors']=errs
   data['passed']=not data['unopened_templates'] and not errs and data['overflow']['document']<=width
   report['viewports'][label]=data;print(label,len(data['windows']),'windows',len(data['abbreviations']),'abbreviations',len(data['quizzes']),'quizzes',data['unopened_templates'],data['overflow'],flush=True)
   await page.close()
  await browser.close()
 report['passed']=all(x['passed'] for x in report['viewports'].values());(OUT/'browser.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print('passed',report['passed'])
asyncio.run(run())
