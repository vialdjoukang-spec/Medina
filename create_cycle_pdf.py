#!/usr/bin/env python3
"""Journal formel d'un cycle de production MEDINA_Alpha."""
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parent
OUT = ROOT.parent / 'output' / 'MEDINA_Alpha_05_Cycle_1_26-09-2026.pdf'
OUT.parent.mkdir(parents=True, exist_ok=True)
pdfmetrics.registerFont(TTFont('DVS', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DVS-B', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
W, H = A4
c = canvas.Canvas(str(OUT), pagesize=A4)
c.setTitle('MEDINA_Alpha | Vague 1, cycle 1 | 26 septembre 2026')
navy = HexColor('#10261E'); ink = HexColor('#19332B'); muted = HexColor('#5D7468')
green = HexColor('#376D52'); lime = HexColor('#D6FF2E'); pale = HexColor('#F2F7F2')
line = HexColor('#D9E5DB'); red = HexColor('#B42332'); white = HexColor('#FFFFFF')

def rect(x, y, w, h, color, radius=0):
    c.setFillColor(color)
    c.roundRect(x, y, w, h, radius, fill=1, stroke=0)

def txt(x, y, t, size=9, color=ink, bold=False):
    c.setFillColor(color); c.setFont('DVS-B' if bold else 'DVS', size)
    c.drawString(x, y, t)

def wrap(t, width, size=9, bold=False):
    font = 'DVS-B' if bold else 'DVS'; out=[]; row=''
    for word in t.split():
        nextrow=(row+' '+word).strip()
        if row and pdfmetrics.stringWidth(nextrow, font, size)>width:
            out.append(row); row=word
        else: row=nextrow
    if row: out.append(row)
    return out

def para(x, y, t, width, size=8.6, leading=13, color=ink):
    for row in wrap(t,width,size): txt(x,y,row,size,color); y-=leading
    return y

rect(0,H-165,W,165,navy)
txt(39,H-40,'MEDINA  /  ALPHA',12,lime,True)
txt(39,H-77,'Vague 1 · cycle 1',25,white,True)
txt(39,H-102,'26 septembre 2026  /  Deux systèmes travaillés en parallèle',9.4,HexColor('#D4E5D7'))
rect(39,H-150,517,35,HexColor('#244436'),7)
txt(53,H-137,'69 / 574',14,lime,True)
txt(156,H-136,'catégories ayant un cours dans la vague 1',9,white)
txt(495,H-136,'12,0 %',9.5,lime,True)

y=H-190
txt(39,y,'DEUX CHAPITRES INTÉGRÉS',11,navy,True); y-=17
for code,name,system,detail in [
 ('I26','Embolie pulmonaire aiguë','Poumon','4 onglets · 37 fenêtres · 4 quiz · 7 Pareto'),
 ('A41','Sepsis et choc septique','Infectiologie','4 onglets · 30 fenêtres · 4 quiz · 7 Pareto')]:
    rect(39,y-52,517,58,pale,9)
    rect(51,y-37,49,30,green,7)
    txt(59,y-27,code,11,white,True)
    txt(113,y-12,name,10.5,ink,True)
    txt(113,y-29,system+'  /  '+detail,8,muted)
    txt(113,y-44,'Contre-audit ciblé effectué ; validation complète encore ouverte.',7.5,muted)
    y-=68

y-=10; txt(39,y,'COUVERTURE PAR SYSTÈME · VAGUE 1',11,navy,True); y-=27
rows=[('01','Cœur et hémodynamique',56,56),('02','Poumon, plèvre et ventilation',12,64),
      ('03','Microorganismes et infections',1,155),('04','Tube digestif, foie et pancréas',0,102),
      ('05','Système nerveux',0,120),('06','Métabolisme et endocrines',0,77)]
for index,name,n,total in rows:
    rect(39,y-34,517,39,pale,6)
    txt(50,y-11,index,8,red,True);txt(77,y-11,name,8.8,ink,True)
    rect(77,y-24,328,6,line,3)
    if n: rect(77,y-24,max(3,328*n/total),6,green,3)
    txt(435,y-17,f'{n}/{total}',8.2,ink,True)
    txt(499,y-17,f'{100*n/total:.0f} %',8.2,green,True)
    y-=45

y-=8
rect(39,y-105,517,111,navy,9)
txt(54,y-16,'ÉTAT EXACT DU CYCLE',9.7,lime,True)
yy=para(54,y-35,'Les deux chapitres sont intégrés au même HTML utilisable. Les contrôles de structure, de liens, de glossaire et de syntaxe passent. Le test visuel dans un navigateur n’a pas pu être effectué ici.',486,8.4,13,white)
yy=para(54,yy-2,'Le poumon et l’infectiologie ne sont pas terminés. Les 12,0 % mesurent la couverture rédactionnelle des catégories, et non une validation clinique à 100 %.',486,8.4,13,HexColor('#E0EDE2'))
para(54,yy-2,'Navigo et Police Taille sont intégrés ; le rendu visuel reste à vérifier.',486,8.4,13,HexColor('#D6FF2E'))
y-=128
txt(39,y,'Suite prévue : cycle 2 sur le digestif et le système nerveux, puis rotation.',8.3,muted)
y-=15
txt(39,y,'MEDINA_0 (SSP) et le fichier du Drive demeurent séparés.',8.3,muted)

c.setStrokeColor(line);c.line(39,32,556,32)
txt(39,19,'MEDINA_Alpha  /  Journal de production',7.5,muted)
txt(517,19,'01 / 01',7.5,muted)
c.save()
print(OUT)
