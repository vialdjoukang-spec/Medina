import math, random, json
random.seed(7)
MM=4.0            # px par mm ; 25 mm/s ; 10 mm/mV
def g(t,c,w,a): return a*math.exp(-((t-c)/w)**2)
def beat(t,t0,pr=0.16,qrs=0.09,qt=0.38,p=0.15,r=1.1,q=-0.1,s=-0.25,T=0.3,st=0.0,wide=False,delta=False,bbd=False,noP=False,peakT=False,flatT=False,U=0,prdep=0.0,coved=False,Pinv=False):
    x=t-t0; y=0
    if not noP: y+=g(x,-pr+0.045,0.028,-p if Pinv else p); y+= g(x,-pr/2+0.03,0.04,prdep) if prdep else 0
    w=qrs/6
    if wide and not bbd:
        y+=g(x,0.00,w*1.4,q)+g(x,0.035,w*1.6,r*0.9)+g(x,0.075,w*1.6,r*0.95)+g(x,qrs,w*1.2,s*0.3)
    elif bbd:
        y+=g(x,0.0,0.009,0.25)+g(x,0.03,0.012,-0.35)+g(x,0.075,0.02,r*0.9)
    else:
        y+=g(x,0.0,w*0.8,q)+g(x,qrs*0.45,w*0.9,r)+g(x,qrs*0.85,w*0.9,s)
    if delta: y+=0.38*min(1,max(0,(x+0.04)/0.04))*(0.5*(1-math.tanh((x-0.012)/0.006)))
    je=qrs+0.02
    if st: 
        y+= (st*(1 if x>je else math.exp(-((x-je)/0.015)**2)) if False else 0)
        span=max(0.0,(qt-0.12)-je)
        if coved: y+= st*(0.5*(1+math.tanh((x-je+0.03)/0.005)))*math.exp(-(max(0,x-je+0.02)/0.11)**2) - 0.32*math.exp(-((x-(je+0.2))/0.06)**2)
        else: y+= st*(0.5*(1+math.tanh((x-je+0.01)/0.008)))*(0.5*(1-math.tanh((x-(qt-0.02))/0.05)))
    if not coved:
        tw=0.03 if peakT else 0.055
        ta=0.03 if flatT else (T*2.6 if peakT else T)
        y+=g(x,qt-0.09,tw,ta)
    if U: y+=g(x,qt+0.09,0.05,U)
    return y
def strip(fn,dur=6.0,h=30,ann=None,title=''):
    W=dur*25*MM; H=h*MM; base=H*0.62
    pts=[]; n=int(dur*250)
    for i in range(n+1):
        t=i/250; y=fn(t); pts.append(f"{t*25*MM:.1f},{base-y*10*MM:.1f}")
    grid=[]
    for i in range(int(dur*25)+1):
        x=i*MM; grid.append(f'<path d="M{x:.1f} 0V{H}" stroke="{"#d7a1a1" if i%5==0 else "#f1d9d9"}" stroke-width="{0.8 if i%5==0 else 0.4}"/>')
    for j in range(h+1):
        y=j*MM; grid.append(f'<path d="M0 {y:.1f}H{W}" stroke="{"#d7a1a1" if j%5==0 else "#f1d9d9"}" stroke-width="{0.8 if j%5==0 else 0.4}"/>')
    a=''.join(ann or [])
    return f'<svg viewBox="0 0 {W:.0f} {H:.0f}" role="img" aria-label="{title}" class="ecg"><rect width="{W:.0f}" height="{H:.0f}" fill="#fffafa"/>{"".join(grid)}<polyline fill="none" stroke="#111" stroke-width="1.4" stroke-linejoin="round" points="{" ".join(pts)}"/>{a}</svg>'
def rr(times,**k):
    return lambda t: sum(beat(t,t0,**k) for t0 in times if -0.5<t-t0<0.9)
def reg(rate,dur=6,start=0.35,**k): return rr([start+i*60/rate for i in range(int(dur*rate/60)+2)],**k)
def lab(x,y,s): return f'<text x="{x}" y="{y}" font-size="11" font-family="Segoe UI,Arial" fill="#17243b">{s}</text>'
T=[]
def add(key,title,lead,crit,course,fn,ann=None,dur=6):
    T.append({'k':key,'t':title,'lead':lead,'crit':crit,'course':course,'svg':strip(fn,dur,ann=ann,title=title)})
x0=0.35*25*MM
add('normal','Rythme sinusal normal','DII',['Fréquence 60–100/min ; onde P positive en DII devant chaque QRS','PR 120–200 ms ; QRS &lt; 120 ms ; QTc &lt; 450 ms (homme), &lt; 460 ms (femme)','Axe du QRS entre −30° et +90°'],'I49',reg(75),
 ann=[lab(92,64,'P'),lab(118,14,'R'),lab(118,92,'S'),lab(140,56,'T'),'<path d="M99 100H115M99 97v6M115 97v6M115 108H153M153 105v6" stroke="#225ea8" stroke-width="1.2"/>',lab(60,104,'PR'),lab(158,113,'QT')])
add('tachy','Tachycardie sinusale','DII',['Rythme sinusal &gt; 100/min','Chercher la cause : fièvre, douleur, hypovolémie, anémie, hyperthyroïdie, embolie pulmonaire'],'I47',reg(125,qt=0.30))
add('brady','Bradycardie sinusale','DII',['Rythme sinusal &lt; 60/min','Physiologique chez le sportif et pendant le sommeil ; sinon médicaments, hypothyroïdie, dysfonction sinusale'],'I44',reg(45,qt=0.42))
def fa(t):
    y=0.04*math.sin(2*math.pi*6.3*t)+0.03*math.sin(2*math.pi*8.7*t+1)
    return y+sum(beat(t,t0,noP=True) for t0 in FA if -0.5<t-t0<0.9)
FA=[0.3];
while FA[-1]<6.5: FA.append(FA[-1]+random.choice([0.42,0.55,0.7,0.48,0.9,0.61,0.38,0.77]))
add('fa','Fibrillation auriculaire','DII',['Absence d’ondes P, trémulations de la ligne de base','Intervalles RR irrégulièrement irréguliers','QRS fins sauf bloc de branche ou préexcitation'],'I48',fa)
def fl(t):
    ph=(t*5.0)%1; y=-0.25*(ph if ph<0.8 else (1-ph)*4)+0.1
    return y+sum(beat(t,t0,noP=True,T=0.15) for t0 in [0.33+i*0.4 for i in range(16)] if -0.5<t-t0<0.9)
add('flutter','Flutter auriculaire typique, conduction 2:1','DII',['Ondes F en dents de scie à 250–350/min, négatives en DII, DIII, aVF','Conduction 2:1 : fréquence ventriculaire régulière proche de 150/min','Toute tachycardie régulière à 150/min fait évoquer un flutter'],'I48',fl)
add('bav1','Bloc auriculoventriculaire du premier degré','DII',['PR &gt; 200 ms, constant','Chaque onde P est suivie d’un QRS'],'I44',reg(65,pr=0.32))
def wk(t):
    y=0;tt=0.35;prs=[0.18,0.26,0.32,None]
    for c in range(4):
        for pr in prs:
            if pr: y+=beat(t,tt+pr,pr=pr) if -0.8<t-tt-pr<0.9 else 0
            else: y+=g(t-tt,0.045,0.028,0.15)
            tt+=0.8
    return y
add('mobitz1','Bloc auriculoventriculaire 2e degré, Mobitz I (Wenckebach)','DII',['Allongement progressif du PR puis une onde P bloquée','Bloc habituellement nodal, souvent bénin (tonus vagal)'],'I44',lambda t:wk(t-0.0))
def m2(t):
    y=0;tt=0.2
    for i in range(10):
        if i in (3,7): y+=g(t-tt,0.045,0.028,0.15)
        else: y+=beat(t,tt+0.18,pr=0.18,wide=True,qrs=0.13) if -0.8<t-tt<1.2 else 0
        tt+=0.72
    return y
add('mobitz2','Bloc auriculoventriculaire 2e degré, Mobitz II','DII',['PR constant, puis onde P bloquée sans allongement préalable','Bloc infranodal, QRS souvent larges : risque de bloc complet, indication d’un stimulateur'],'I44',m2)
def b3(t):
    y=sum(g(t-p0,0.045,0.028,0.15) for p0 in [0.1+i*0.7 for i in range(10)])
    return y+sum(beat(t,q0,noP=True,wide=True,qrs=0.16,T=-0.35) for q0 in [0.6,2.3,4.0,5.7] if -0.5<t-q0<0.9)
add('bav3','Bloc auriculoventriculaire complet (3e degré)','DII',['Ondes P et QRS sans relation (dissociation) ; fréquence auriculaire &gt; ventriculaire','Échappement jonctionnel (QRS fins, 40–60/min) ou ventriculaire (QRS larges, &lt; 40/min)'],'I44',b3)
add('bbg','Bloc de branche gauche','V6',['QRS ≥ 120 ms','Onde R large, crochetée en V5–V6 et DI, sans onde q septale','Aspect QS ou rS en V1 ; troubles secondaires de la repolarisation'],'I44',reg(70,wide=True,qrs=0.15,q=0,T=-0.3))
add('bbd','Bloc de branche droit','V1',['QRS ≥ 120 ms','Aspect rsR′ en V1–V2','Onde S large en DI et V6'],'I44',reg(70,bbd=True,qrs=0.13,T=-0.15))
add('wpw','Préexcitation de Wolff-Parkinson-White','DII',['PR &lt; 120 ms','Onde delta (empâtement initial du QRS), QRS élargi','Fibrillation auriculaire préexcitée : ne pas donner de bloqueur du nœud auriculoventriculaire'],'I47',reg(72,pr=0.10,delta=True,qrs=0.11))
add('stemi','Sus-décalage du segment ST (infarctus en cours)','V3',['Sus-décalage du point J dans au moins 2 dérivations contiguës : ≥ 1 mm ; en V2–V3 ≥ 2 mm (homme ≥ 40 ans), ≥ 2,5 mm (homme &lt; 40 ans), ≥ 1,5 mm (femme) — ESC','Image en miroir dans les dérivations opposées','Reperfusion immédiate'],'I21',reg(80,st=0.35,T=0.45))
add('sousST','Sous-décalage du segment ST','V5',['Sous-décalage horizontal ou descendant ≥ 0,5 mm dans au moins 2 dérivations contiguës','Ischémie sous-endocardique, syndrome coronarien sans sus-décalage ; aussi hypertrophie, digoxine'],'I21',reg(85,st=-0.22,T=0.12))
add('pericard','Péricardite aiguë','DII',['Sus-décalage du ST concave, diffus, sans image en miroir (sauf aVR)','Sous-décalage du segment PR','Évolution en quatre stades'],'I30',reg(90,st=0.28,prdep=-0.1,T=0.32))
add('hyperk','Hyperkaliémie','V3',['Ondes T amples, pointues, étroites et symétriques','Puis allongement du PR, aplatissement de P, élargissement du QRS, aspect sinusoïdal','Urgence : gluconate de calcium'],'N17',reg(75,peakT=True,T=0.45,p=0.08))
add('hypok','Hypokaliémie','V3',['Ondes T aplaties, sous-décalage du ST','Ondes U proéminentes, intervalle QU allongé','Risque d’arythmies et de torsades'],'N17',reg(72,flatT=True,st=-0.05,U=0.12))
add('qtl','Allongement de l’intervalle QT','DII',['QTc corrigé par la formule de Bazett ou de Fridericia','QTc &gt; 500 ms : risque élevé de torsades de pointes','Médicaments (psychotropes, macrolides, antiarythmiques), hypokaliémie, hypomagnésémie'],'I49',reg(65,qt=0.56,T=0.28))
def esv(t):
    y=0;tt=0.3
    for i in range(8):
        if i==3: y+=beat(t,tt-0.35,noP=True,wide=True,qrs=0.16,T=-0.4,r=1.4) ; tt+=0.8+0.4
        else: y+=beat(t,tt) if -0.5<t-tt<0.9 else 0; tt+=0.8
    return y
add('esv','Extrasystole ventriculaire','DII',['QRS prématuré, large (≥ 120 ms), non précédé d’une onde P','Repolarisation discordante ; repos compensateur complet'],'I49',esv)
add('tsv','Tachycardie supraventriculaire par réentrée nodale','DII',['QRS fins, réguliers, 150–250/min','Onde P rétrograde cachée dans le QRS ou juste après','Manœuvres vagales puis adénosine'],'I47',reg(185,noP=True,qt=0.24,T=0.2))
add('tv','Tachycardie ventriculaire monomorphe','DII',['Au moins 3 QRS larges successifs (≥ 120 ms) à &gt; 100/min, réguliers','Dissociation auriculoventriculaire, complexes de capture et de fusion','Toute tachycardie à QRS large est une TV jusqu’à preuve du contraire'],'I47',reg(180,noP=True,wide=True,qrs=0.16,T=-0.45,r=0.95,qt=0.3))
def tdp(t): return math.sin(2*math.pi*4*t)*(0.12+0.75*abs(math.sin(math.pi*t/1.8)))
add('tdp','Torsades de pointes','DII',['Tachycardie ventriculaire polymorphe : QRS dont l’amplitude oscille autour de la ligne de base','Survient sur un QT long ; traitement : sulfate de magnésium, correction du potassium'],'I49',tdp)
def fv(t): return 0.28*math.sin(2*math.pi*5.3*t)+0.25*math.sin(2*math.pi*7.9*t+0.7)+0.15*math.sin(2*math.pi*3.1*t+2)
add('fv','Fibrillation ventriculaire','DII',['Activité électrique chaotique, sans QRS identifiable','Arrêt circulatoire : défibrillation immédiate'],'I46',fv)
add('brugada','Aspect de Brugada de type 1','V1',['Sus-décalage du ST en dôme ≥ 2 mm, suivi d’une onde T négative, en V1–V2','Risque de mort subite ; démasqué par la fièvre et certains médicaments'],'I49',reg(70,bbd=True,st=0.42,coved=True,qrs=0.12,r=0.5))
import os
json.dump(T,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'ecg.json'),'w'),ensure_ascii=False)
print(len(T),sum(len(x['svg']) for x in T))
