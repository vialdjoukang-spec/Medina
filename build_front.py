#!/usr/bin/env python3
"""Construit MEDINA.html sur le front-end d'origine (shell/medina_front.html) + cours + moteur + glossaire + embellissement + atlas ECG."""
import os,sys,json,glob,argparse,re,tempfile
ROOT=os.environ.get('MEDINA_ROOT',os.path.dirname(os.path.abspath(__file__)))
OUT=os.environ.get('MEDINA_OUT','/mnt/user-data/outputs' if os.path.isdir('/mnt/user-data') else ROOT+'/dist')
os.environ['MEDINA_V6']=ROOT+'/shell/medina_front.html'
sys.path.insert(0,ROOT);sys.path.insert(0,ROOT+'/shell')
import build_medina as B
from fragment_surface import isolate_specialty, finish_surface
from tools.atomic_output import atomic_output
from data import WAVES,DONE_SYS,DONE_COURSES,PRIO,PLAN
parser=argparse.ArgumentParser()
group=parser.add_mutually_exclusive_group()
group.add_argument('--fragment',metavar='ID')
group.add_argument('--all-fragments',action='store_true')
args=parser.parse_args()
cfg=json.load(open(ROOT+'/chapters.json'))
fragments=json.load(open(ROOT+'/fragments.json')) if args.fragment or args.all_fragments else []
if fragments:
    public_names={f['id']:f for f in json.load(open(ROOT+'/organisation/fragments.json'))}
    for f in fragments:
        f['nom']=public_names[f['id']]['label']
        f['production_order']=public_names[f['id']]['order']
explicit={x:f['id'] for f in fragments for x in f['rattachements'] if re.fullmatch(r'[A-Z][0-9]{2}',x)}

def fragment_chapters(fragment,entries):
    attached=set(fragment['rattachements'])
    systems={e['code']:e.get('system') for e in entries}
    return [c for c in cfg if c.get('integrated') and
            (c['code'] in attached or (c['code'] not in explicit and systems.get(c['code']) in attached))]

def fragment_shell(fragment):
    s=open(ROOT+'/shell/medina_front.html',encoding='utf-8').read()
    pattern=r'(<script id="medora-data" type="application/json">)(.*?)(</script>)'
    match=re.search(pattern,s,re.S)
    assert match
    data=json.loads(match.group(2));attached=set(fragment['rattachements'])
    data['entries']=[e for e in data['entries'] if e['code'] in attached or
                     (e['code'] not in explicit and e.get('system') in attached)]
    codes={e['code'] for e in data['entries']};systems={e.get('system') for e in data['entries']}
    specialties={x for e in data['entries'] for x in e.get('specialties',[])}
    data['specialties']=[x for x in data['specialties'] if x['id'] in specialties]
    for specialty in data['specialties']:
        specialty['entries']=[x for x in specialty.get('entries',[]) if x in codes]
    data['profiles']={k:v for k,v in data['profiles'].items()
                      if any(e.get('organ')==k or e.get('profile')==k for e in data['entries'])}
    data['focus']={k:v for k,v in data['focus'].items() if k in codes}
    linked={x for e in data['entries'] for x in e.get('links',[])}
    data['ssps']=[x for x in data['ssps'] if x['code'] in linked]
    data['legacy']['specialties']=[x for x in data['legacy']['specialties'] if x['id'] in specialties]
    data['legacy']['meta']['specialties']=len(data['specialties'])
    data['legacy']['meta']['systems']=len(systems)
    data['legacy']['meta']['chapters']=len(data['entries'])
    data['legacy']['meta']['fullCourses']=len(fragment_chapters(fragment,data['entries']))
    data['meta']['entries']=len(data['entries'])
    data['meta']['sspVisible']=len(data['ssps'])
    data['fragment']={'id':fragment['id'],'name':fragment['nom'],'systems':sorted(systems)}
    if fragment.get('surface') == 'courses-v1':
        isolate_specialty(data, fragment, fragment_chapters(fragment, data['entries']), DONE_COURSES)
    payload=json.dumps(data,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')
    s=s[:match.start()]+match.group(1)+payload+match.group(3)+s[match.end():]
    name=fragment['nom']
    s=s.replace('<title>Medina · Atlas médical</title>','<title>Medina · '+name+'</title>',1)
    s=s.replace('<span><strong>Medina</strong><small>ATLAS DE MÉDECINE</small></span>',
                '<span><strong>'+name+'</strong><small>FRAGMENT '+fragment['id']+'</small></span>',1)
    chapter_by_code={c['code']:c for c in fragment_chapters(fragment,data['entries'])}
    groups={}
    for entry in sorted(data['entries'],key=lambda x:x['code']):
        axis=entry.get('system') or 'Autres'
        category=(entry.get('block')+' · '+entry.get('blockTitle','')).strip(' ·')
        key=(axis,category) if fragment['id'].startswith('T') else ('',category)
        groups.setdefault(key,[]).append(entry)
    sidebar=[]
    for (axis,category),items in groups.items():
        if axis and (not sidebar or sidebar[-1].get('axis')!=axis): sidebar.append({'axis':axis})
        sidebar.append({'category':category,'items':[{'code':e['code'],'title':chapter_by_code.get(e['code'],e).get('title',e['title']),
                                                       'written':e['code'] in chapter_by_code} for e in items]})
    if not chapter_by_code: sidebar=[{'empty':"Aucun chapitre rédigé pour l'instant"}]
    fragment_script='<script>window.MEDINA_FRAGMENT_SIDEBAR='+json.dumps(sidebar,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')+';</script>'
    s=s.replace('</head>',fragment_script+'</head>',1)
    s=s.replace('<div class="nav-title">Spécialités · priorité intuitive</div>',
                '<div class="nav-title">Chapitres par catégories</div>',1)
    note=f"{len(data['entries']):n} catégories CIM intégrées.<br>{len(chapter_by_code)} cours rédigés.<br>Périmètre exclusif {fragment['id']}.".replace(',', ' ')
    s=re.sub(r'<div class="sidebar-note">.*?</div>', '<div class="sidebar-note">'+note+'</div>',s,count=1)
    old="$('#spec-nav').innerHTML=ordered.map(s=>`<a href=\"${url('specialty',s.id)}\" class=\"${context?.sid===s.id?'active':''}\"><span class=\"nav-num\">${String(s.rank).padStart(2,'0')}</span><span class=\"nav-label\">${h(s.title)}</span></a>`).join('');"
    new="const fs=window.MEDINA_FRAGMENT_SIDEBAR;if(fs){$('#spec-nav').innerHTML=fs.map(g=>g.empty?`<div class=\"sidebar-note\">${h(g.empty)}</div>`:g.axis?`<div class=\"nav-title\">${h(g.axis)}</div>`:`<details open data-fragment-category=\"${h(g.category)}\"><summary>${h(g.category)} · ${g.items.length}</summary>${g.items.map(x=>x.written?`<a href=\"#/entry/${x.code}\" data-fragment-chapter=\"${x.code}\"><span class=\"nav-num\">${x.code}</span><span class=\"nav-label\">${h(x.title)}</span></a>`:`<span class=\"nav-planned\" data-fragment-planned=\"${x.code}\"><span class=\"nav-num\">${x.code}</span><span class=\"nav-label\">${h(x.title)} · à venir</span></span>`).join('')}</details>`).join('')}else "+old
    assert old in s
    s=s.replace(old,new,1)
    s=s.replace('</head>','<style>.nav-list details>summary{cursor:pointer;color:#94a8c7;font-size:10px;font-weight:700;padding:8px}.nav-planned{display:flex;gap:9px;color:#8392aa;font-size:11px;padding:6px 9px;opacity:.72}.nav-list details .nav-num{width:32px}</style></head>',1)
    if not fragment_chapters(fragment,data['entries']):
        notice='<div class="empty" id="medina-fragment-empty">Aucun chapitre rédigé pour l\'instant</div>'
        s=s.replace('</main>',notice+'</main>',1)
    f=tempfile.NamedTemporaryFile('w',encoding='utf-8',suffix='.html',delete=False)
    f.write(s);f.close();return f.name,data['entries']

selected=[]
if args.fragment:
    selected=[f for f in fragments if f['id'].upper()==args.fragment.upper()]
    if not selected: parser.error('fragment inconnu : '+args.fragment)
elif args.all_fragments:selected=fragments

chap=[c for c in cfg if c.get('integrated')]
shell_tmp=None
if selected:
    # Le corps historique ci-dessous est exécuté une fois par fragment par runpy.
    if len(selected)>1:
        import subprocess
        for fragment in selected:
            subprocess.run([sys.executable,__file__,'--fragment',fragment['id']],check=True,env=os.environ)
        raise SystemExit
    fragment=selected[0];shell_tmp,entries=fragment_shell(fragment)
    chap=fragment_chapters(fragment,entries)
    os.environ['MEDINA_V6']=shell_tmp
for c in cfg: B.COVERS[c['code']]=c.get('covers',[c['code']])
chapters=[(c['code'],sorted(glob.glob(f"{ROOT}/chapters/{c['code']}/*.html"))) for c in chap]
os.makedirs(OUT,exist_ok=True)
out=(OUT+'/fragments/MEDINA_'+fragment['id']+'_'+fragment['slug']+'.html') if selected else OUT+'/MEDINA.html'
if selected: os.makedirs(os.path.dirname(out),exist_ok=True)
final_out=out
try:
    with atomic_output(final_out) as out:
        rep,size=B.build(chapters,out)
        build=max((c.get('added','') or '' for c in chap),default='')
        CAT={}
        for k in 'normal tachy brady fa flutter tsv'.split():CAT[k]='Rythme'
        for k in 'bav1 mobitz1 mobitz2 bav3 bbg bbd wpw'.split():CAT[k]='Conduction'
        for k in 'stemi sousST pericard hyperk hypok qtl brugada'.split():CAT[k]='Ischémie et repolarisation'
        for k in 'esv tv tdp fv'.split():CAT[k]='Arythmies ventriculaires'
        # Couverture : catégories CIM distinctes (union des covers), 100 % pour un système achevé (cours + renvois).
        sysd=[]
        for n,t,k in WAVES:
            courses=[c for c in chap if c.get('wave',1)==n]
            if selected and not courses: continue
            covered=k if n in DONE_SYS else min(k,len({x for c in courses for x in c.get('covers',[c['code']])}))
            ch=[{'code':c['code'],'title':c['title'],'complete':c['code'] in DONE_COURSES} for c in courses]
            sysd.append({'n':n,'t':t,'title':t,'cat':k,'total':k,'covered':covered,'prio':n in PRIO,'done':n in DONE_SYS,
                         'pct':round(100*covered/k),'ch':ch,'courses':ch,'plan':[] if selected else PLAN.get(n,[])})
        completed=[c['code'] for c in chap if c['code'] in DONE_COURSES]
        data={'systems':sysd,'build':build,'news':[{'code':c['code'],'title':c['title'],'complete':c['code'] in DONE_COURSES} for c in chap if c.get('added')==build],
              'doneNames':[t for n,t,_ in WAVES if n in DONE_SYS],'ecgCat':CAT,'complete':completed}
        s=open(out,encoding='utf-8').read()
        # Icône « stomach » de la coque : chemin SVG incomplet (erreur de console au premier rendu) ; source intacte.
        s=s.replace("1-5 1-7V3z'","1-5 1-7 0V3z'",1)
        # Insigne « 100 % rédigé » : seuls les chapitres de DONE_COURSES (audités), distincts des chapitres intégrés.
        assert '<script>window.MEDINA_ALIAS=' in s
        s=s.replace('<script>window.MEDINA_ALIAS=','<script>window.MEDINA_COMPLETE='+json.dumps(completed)+';</script><script>window.MEDINA_ALIAS=',1)
        s=s.replace('</head>','<style id="medina-polish">'+open(ROOT+'/shell/polish.css').read()+'</style></head>',1)
        ecg=open(ROOT+'/modules/ecg.json').read() if not selected or fragment['id']=='S01' else '[]'
        polish=open(ROOT+'/shell/polish.js').read()
        if selected and fragment['id']!='S01': polish=polish.replace('function ecgButton(){','function ecgButton(){return;',1)
        tail='<script>window.MDN_DATA='+json.dumps(data,ensure_ascii=False)+';window.MDN_ECG='+ecg+'</script><script>'+polish+'</script>'
        i=s.rindex('</body>');s=s[:i]+tail+s[i:]
        if selected:
            s=finish_surface(s, fragment, ROOT)
        if selected:
            present={c['code'] for c in chap}
            absent={c['code'] for c in cfg}-present
            # Les renvois littéraux des cours ne doivent pas ouvrir une route retirée.
            link=re.compile(r'<a\b([^>]*\bhref=["\']#/entry/('+'|'.join(map(re.escape,absent))+r')["\'][^>]*)>(.*?)</a>',re.S)
            s=link.sub(lambda m:'<span'+re.sub(r'\s*href=["\'][^"\']+["\']','',m.group(1))+'>'+m.group(3)+'</span>',s)
        open(out,'w',encoding='utf-8').write(s)
        if shell_tmp: os.unlink(shell_tmp)
        print('fichier',final_out,'taille',len(s.encode()))
        for c,m in rep.items():
            if m: print(c,'non couvertes',len(m))

        # ===== Compression des cours (gzip + base64), décompressés à l'ouverture par DecompressionStream =====
        import re,gzip,base64
        s=open(out,encoding='utf-8').read()
        tpls=[]
        def grab(m):
            tpls.append(m.group(0));return ''
        s2=re.sub(r'<template (?:id="ch-[^"]+"|data-pop="[^"]+")[\s\S]*?</template>',grab,s)
        if tpls:
            pack=base64.b64encode(gzip.compress(''.join(tpls).encode('utf-8'),9,mtime=0)).decode()  # mtime=0 : construction reproductible
            loader=('<div id="mdn-tpl" hidden></div><script id="mdn-pack" type="application/octet-stream">'+pack+'</script>'
             '<script>(async()=>{try{const b=Uint8Array.from(atob(document.getElementById("mdn-pack").textContent),c=>c.charCodeAt(0));'
             'const t=await new Response(new Blob([b]).stream().pipeThrough(new DecompressionStream("gzip"))).text();'
             'document.getElementById("mdn-tpl").innerHTML=t;window.MDN_READY=true;if(typeof render==="function")render();}catch(e){console.error("MEDINA décompression",e)}})()</script>')
            i=s2.rindex('<script id="medina-glossary"') if '<script id="medina-glossary"' in s2 else s2.rindex('</body>')
            s2=s2[:i]+loader+s2[i:]
            open(out,'w',encoding='utf-8').write(s2)
            print('compression :',len(s.encode()),'→',len(s2.encode()),'octets ;',len(tpls),'gabarits')
finally:
    if shell_tmp and os.path.exists(shell_tmp):
        os.unlink(shell_tmp)
