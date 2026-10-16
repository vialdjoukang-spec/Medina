import json, sys, os
from playwright.sync_api import sync_playwright
URL='http://127.0.0.1:8793/MEDINA_S08_nerveux.html'; CAP=sys.argv[1]; OUTJ=sys.argv[2]
SCI=['c72-s-semio','c72-s-anat','c72-s-histo','c72-s-gen','c72-s-radio','c72-s-physio']
res={'url':'http://127.0.0.1:8793/MEDINA_S08_nerveux.html#/entry/C72 (construction hors dépôt)','navigateur':'/opt/pw-browsers/chromium-1194/chrome-linux/chrome','controles':{},'erreurs_js':[],'erreurs_console':[],'captures':[]}
def shot(pg,name,el=None):
    p=os.path.join(CAP,name); (el.screenshot(path=p) if el else pg.screenshot(path=p)); res['captures'].append('captures/'+name)
def ok(lab,k,v,detail=None):
    res['controles'][lab+'.'+k]={'ok':bool(v)}|({'detail':detail} if detail is not None else {})
with sync_playwright() as p:
    b=p.chromium.launch(executable_path=res['navigateur'])
    for lab,vp,pre in [('bureau',(1300,900),'C72_0'),('mobile390',(390,844),'C72_1')]:
        pg=b.new_page(viewport={'width':vp[0],'height':vp[1]})
        pg.on('pageerror',lambda e: res['erreurs_js'].append(str(e)))
        pg.on('console',lambda m: res['erreurs_console'].append(m.text) if m.type=='error' else None)
        pg.goto(URL); pg.wait_for_timeout(1000); pg.goto(URL+'#/entry/C72'); pg.wait_for_timeout(1500)
        ok(lab,'cours_affiche',pg.locator('.mc').count()==1)
        shot(pg,f'{pre}1_ouverture_{lab}.png')
        clin=pg.locator('[data-semiology-clinical="C72"]')
        ok(lab,'bloc_clinique_present',clin.count()==1)
        clin.scroll_into_view_if_needed(); pg.wait_for_timeout(300)
        ok(lab,'bloc_clinique_visible',clin.is_visible())
        shot(pg,f'{pre}2_bloc_clinique_{lab}.png')
        pg.evaluate("window.scrollTo(0,0)")
        pg.locator('.mc-tabs button[data-p="pS"]').click(); pg.wait_for_timeout(500)
        first=pg.evaluate("()=>{const b=document.querySelector('#pS .mc-sci-bar button, #pS .sci-bar button');return b?[b.id,b.textContent.trim()]:null}")
        ok(lab,'premier_bouton_semio',first and first[0]=='c72-tab-semio' and first[1]=='Sémiologie fondamentale et analytique',first)
        ar=pg.evaluate("()=>[...document.querySelectorAll('#pS [data-s]')].map(b=>[b.dataset.s,b.getAttribute('aria-selected')])")
        ok(lab,'aria_selected',ar and ar[0]==['c72-s-semio','true'] and all(x[1]=='false' for x in ar[1:]) and len(ar)==6,ar)
        vis=[[i,pg.locator('#'+i).is_visible()] for i in SCI]
        ok(lab,'semio_seul_visible',vis[0][1] and not any(v for _,v in vis[1:]),vis)
        ok(lab,'titre_exact',pg.locator('#c72-s-semio h3').first.inner_text().strip()=='Pour la leçon : quelle est la sémiologie fondamentale et analytique ?')
        secs=pg.evaluate("()=>[...document.querySelectorAll('#c72-s-semio [data-semiology]')].map(s=>[s.dataset.semiology,s.innerText.split(/\\s+/).length])")
        ok(lab,'neuf_sections',[s[0] for s in secs]==['normal','signs','mechanisms','examination','interpretation','differentials','urgency','limits','sources'],secs)
        ok(lab,'pas_de_defilement_horizontal',pg.evaluate("document.documentElement.scrollWidth<=window.innerWidth+1"),pg.evaluate("document.documentElement.scrollWidth"))
        shot(pg,f'{pre}3_sous_onglet_semiologie_{lab}.png')
        fig=pg.locator('#c72-s-semio figure').first; fig.scroll_into_view_if_needed(); pg.wait_for_timeout(300)
        fs=pg.evaluate("()=>{const t=document.querySelector('#c72-s-semio figure svg text');return t?t.getBoundingClientRect().height:0}")
        ok(lab,'figure8_texte_lisible',fs>=12,round(fs,1))
        shot(pg,f'{pre}4_figure8_semiologie_{lab}.png',fig)
        w=pg.locator('#c72-s-semio .mc-w[data-k="c72-sm-residu"]').first; w.scroll_into_view_if_needed(); w.click(); pg.wait_for_timeout(400)
        body=pg.inner_text('.mc-dlg-b'); ok(lab,'fenetre_c72-sm-residu','Fiche absente' not in body and '200 ml' in body, body[:120])
        shot(pg,f'{pre}5_fenetre_semiologie_{lab}.png'); pg.keyboard.press('Escape'); pg.wait_for_timeout(200)
        for i in SCI[1:]:
            pg.locator(f'#pS [data-s="{i}"]').click(); pg.wait_for_timeout(300)
            ok(lab,'bascule_'+i,pg.locator('#'+i).is_visible() and not pg.locator('#c72-s-semio').is_visible())
            for fg in range(pg.locator(f'#{i} figure').count()):
                f=pg.locator(f'#{i} figure').nth(fg); f.scroll_into_view_if_needed(); pg.wait_for_timeout(200)
                h=pg.evaluate(f"()=>{{const t=document.querySelectorAll('#{i} figure')[{fg}].querySelector('svg text');return t?t.getBoundingClientRect().height:0}}")
                ok(lab,f'texte_figure_{i}_{fg}',h>=12,round(h,1))
                shot(pg,f'{pre}6_figure_{i}_{lab}.png',f)
            ok(lab,'pas_de_defilement_'+i,pg.evaluate("document.documentElement.scrollWidth<=window.innerWidth+1"))
        pg.locator('#pS [data-s="c72-s-semio"]').click(); pg.wait_for_timeout(300)
        ok(lab,'retour_semio',pg.locator('#c72-s-semio').is_visible())
        if lab=='bureau':
            bad=[]; n=0
            for t,subs in [('pA',[None]),('pE',[None]),('pS',SCI),('pP',[None])]:
                pg.locator(f'.mc-tabs button[data-p="{t}"]').click(); pg.wait_for_timeout(200)
                for s in subs:
                    if s: pg.locator(f'#pS [data-s="{s}"]').click(); pg.wait_for_timeout(200)
                    els=pg.locator('.mc .mc-w')
                    for k in range(els.count()):
                        el=els.nth(k)
                        if not el.is_visible(): continue
                        el.scroll_into_view_if_needed(); el.click(); pg.wait_for_timeout(40); n+=1
                        bd=pg.inner_text('.mc-dlg-b')
                        if 'Fiche absente' in bd or len(bd.strip())<20: bad.append(el.get_attribute('data-k'))
                        pg.keyboard.press('Escape')
            ok(lab,'toutes_fenetres_ouvertes',not bad,{'ouvertures':n,'echecs':bad})
        pg.close()
    b.close()
res['resultat']='passed' if not res['erreurs_js'] and all(v['ok'] for v in res['controles'].values()) else 'failed'
json.dump(res,open(OUTJ,'w'),ensure_ascii=False,indent=1)
print(res['resultat']); print([k for k,v in res['controles'].items() if not v['ok']], res['erreurs_js'][:3])
