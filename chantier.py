import json,sys,html,os
ROOT=os.environ.get('MEDINA_ROOT',os.path.dirname(os.path.abspath(__file__)))
OUT=os.environ.get('MEDINA_OUT','/mnt/user-data/outputs' if os.path.isdir('/mnt/user-data') else ROOT+'/dist')
os.makedirs(OUT,exist_ok=True)
sys.path.insert(0,ROOT+'/shell')
from data import WAVES,PRIO,DONE_SYS,RENVOIS,NOTES
chap=[c for c in json.load(open(ROOT+'/chapters.json')) if c.get('integrated')]
cov={}
for c in chap: cov[c.get('wave',1)]=cov.get(c.get('wave',1),0)+len(c['covers'])
tot=sum(k for _,_,k in WAVES);pc=sum(k for n,_,k in WAVES if n in PRIO);done=sum(k for n,_,k in WAVES if n in DONE_SYS)+sum(v for w,v in cov.items() if w not in DONE_SYS)
cells=[];k=0
for n,t,cat in WAVES:
    for i in range(cat):
        if n in DONE_SYS: cl='d' if i<cov.get(n,0) else 'r'
        elif i<cov.get(n,0): cl='d'
        else: cl='p' if n in PRIO else ''
        cells.append(f'<i class="{cl}" title="{html.escape(t)}"></i>')
rows=''.join(f'<tr><td>{n}</td><td>{html.escape(t)}{" <span class=f>100 % rédigé</span>" if n in DONE_SYS else ""}</td><td>{"Examen fédéral" if n in PRIO else "En pause"}</td><td>{cat}</td><td>{len([c for c in chap if c.get("wave",1)==n])}</td><td><div class=bar><i style="width:{100 if n in DONE_SYS else round(100*cov.get(n,0)/cat)}%"></i></div></td></tr>' for n,t,cat in WAVES)
crs=''.join(f'<tr><td>{c["code"]}</td><td>{html.escape(c["title"])}</td><td>{", ".join(c["covers"])}</td><td>{c.get("wave",1)}</td><td>{NOTES.get(c["code"],"20/20" if c.get("wave",1)==1 else "auto-audit, audit indépendant à faire")}</td></tr>' for c in chap)
page=f'''<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>MEDINA · État des lieux du chantier</title><style>
body{{margin:0;background:#f4f7fb;color:#243247;font:15px/1.6 'Segoe UI',Arial,sans-serif}}main{{max-width:1180px;margin:auto;padding:28px 20px 60px}}h1{{font-size:2rem;letter-spacing:-.03em;margin:0 0 6px}}h2{{font-size:1.25rem;margin:30px 0 10px}}.m{{color:#65738a}}
.card{{background:#fff;border:1px solid #dce4f0;border-radius:17px;padding:18px;box-shadow:0 8px 28px #2336590f}}.g{{display:grid;grid-template-columns:repeat(auto-fill,minmax(8px,1fr));gap:2px}}.g i{{aspect-ratio:1;border-radius:2px;background:#dfe6ef}}.g i.p{{background:#b9c9e4}}.g i.d{{background:#D6FF2E;box-shadow:0 0 5px #c8ff28}}.g i.r{{background:#ecf7b0}}
.facts{{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:12px;margin:18px 0}}.facts div{{background:#fff;border:1px solid #dce4f0;border-radius:14px;padding:14px}}.facts b{{display:block;font-size:1.5rem}}
table{{width:100%;border-collapse:collapse;background:#fff;border:1px solid #dce4f0;font-size:14px}}th,td{{padding:8px 12px;border-bottom:1px solid #dce4f0;text-align:left}}th{{background:#eef3fa;font-size:12.5px;color:#65738a}}.tw{{overflow-x:auto}}
.bar{{height:6px;border-radius:3px;background:#dfe6ef;min-width:80px}}.bar i{{display:block;height:100%;background:#D6FF2E;border-radius:3px}}.f{{font:700 11px 'Segoe UI';background:#D6FF2E;color:#132200;border-radius:99px;padding:3px 8px;margin-left:6px}}
.lg span{{margin-right:16px;font-size:13px;color:#65738a}}.lg span:before{{content:"";display:inline-block;width:10px;height:10px;border-radius:2px;margin-right:6px;background:var(--c)}}</style></head><body><main>
<h1>État des lieux du chantier MEDINA</h1><p class="m">Plan d’élaboration — document de travail séparé du produit. Chaque case est une catégorie CIM-10-GM.</p>
<div class="card"><div class="g">{"".join(cells)}</div><p class="lg" style="margin:12px 0 0"><span style="--c:#D6FF2E">Couverte par un cours</span><span style="--c:#ecf7b0">Système achevé, renvoi</span><span style="--c:#b9c9e4">Prioritaire, à produire</span><span style="--c:#dfe6ef">En pause</span></p></div>
<div class="facts"><div><b>{len(DONE_SYS)} / {len(WAVES)}</b>systèmes achevés</div><div><b>{len(chap)}</b>cours rédigés</div><div><b>{done} / {pc}</b>catégories prioritaires traitées ({round(100*done/pc)} %)</div><div><b>24</b>tracés dans l’atlas ECG</div></div>
<h2>Systèmes</h2><div class="tw"><table><tr><th>Vague</th><th>Système</th><th>Statut</th><th>Catégories</th><th>Cours</th><th>Avancement</th></tr>{rows}</table></div>
<h2>Cours</h2><div class="tw"><table><tr><th>Code</th><th>Cours</th><th>Codes couverts</th><th>Vague</th><th>Audit</th></tr>{crs}</table></div>
<h2>Réserves et point suivant</h2><div class="card"><p>Aucune revue humaine indépendante (pas de PASS_VIAL). J45 : auto-audit, deuxième passe indépendante à réaliser. Production parallèle multisystème : dans Cowork, selon le prompt maître 2.0.</p><p><b>Suivant</b> : vague 2 — J44 BPCO, J18 pneumonies, I26 embolie pulmonaire ; puis vagues 3 et 4 en parallèle.</p></div>
</main></body></html>'''
open(OUT+'/MEDINA_Etat_des_lieux.html','w').write(page)
print('ok',done,pc)
