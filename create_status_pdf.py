from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, Color
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
from pathlib import Path
import os
pdfmetrics.registerFont(TTFont('DV','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DVB','/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
P=Path(__file__).resolve().parent.parent/'output/pdf/MEDINA_Alpha_04_Progression_26-09-2026.pdf';P.parent.mkdir(parents=True,exist_ok=True)
W,H=A4;c=canvas.Canvas(str(P),pagesize=A4)
navy=HexColor('#101C2C');ink=HexColor('#15243A');muted=HexColor('#68768A');line=HexColor('#DDE5EC');lime=HexColor('#D6FF2E');pale=HexColor('#F4F7FA');teal=HexColor('#247F82')
def txt(x,y,s,size=10,color=ink,bold=False):
 c.setFont('DVB' if bold else 'DV',size);c.setFillColor(color);c.drawString(x,y,s)
def box(x,y,w,h,col,r=10):c.setFillColor(col);c.roundRect(x,y,w,h,r,fill=1,stroke=0)
def wrap(s,maxw,size=9,bold=False):
 f='DVB' if bold else 'DV';a=[];row=''
 for word in s.split():
  candidate=(row+' '+word).strip()
  if pdfmetrics.stringWidth(candidate,f,size)>maxw and row:a.append(row);row=word
  else:row=candidate
 if row:a.append(row)
 return a
def para(x,y,s,maxw,size=9,leading=14,color=ink,bold=False):
 for l in wrap(s,maxw,size,bold):txt(x,y,l,size,color,bold);y-=leading
 return y
box(0,H-160,W,160,navy,0)
txt(39,H-44,'MEDINA  /  ALPHA',13,lime,True)
txt(39,H-81,'Progression vérifiée',24,HexColor('#FFFFFF'),True)
txt(39,H-104,'Point du 26 septembre 2026 · production par systèmes',9.5,HexColor('#C9D3DD'))
box(39,H-156,516,35,HexColor('#203145'),7)
txt(53,H-143,'67 / 574',15,lime,True);txt(150,H-142,'catégories de la vague 1 dotées d’un cours',9,HexColor('#FFFFFF'))
txt(480,H-143,'11,7 %',11,lime,True)
y=H-184;txt(39,y,'VAGUE 1  ·  SIX SYSTÈMES',11,navy,True);y-=22
rows=[('01','Cœur et hémodynamique',56,56,'Cours historiques intégrés ; contrôle global à reprendre'),('02','Poumon, plèvre et ventilation',11,64,'J45, J44 et J18 en révision'),('03','Microorganismes et infections',0,155,'À produire'),('04','Tube digestif, foie, pancréas',0,102,'À produire'),('05','Système nerveux',0,120,'À produire'),('06','Métabolisme et endocrines',0,77,'À produire')]
for idx,name,n,total,note in rows:
 box(39,y-44,516,48,pale,7);txt(50,y-15,idx,8.5,teal,True);txt(77,y-15,name,9.5,ink,True)
 txt(77,y-31,note,7.5,muted)
 box(427,y-19,97,6,line,3)
 if n:box(427,y-19,max(3,97*n/total),6,lime,3)
 txt(454,y-38,f'{n}/{total}  ({round(100*n/total)} %)',8,ink,True)
 y-=54
y-=9;txt(39,y,'COURS DU POUMON : ÉTAT RÉEL',11,navy,True);y-=21
for title,detail in [('J45  Asthme','Cours intégré ; auto-audit ; contrôle indépendant et navigateur attendus.'),('J44  BPCO','9 599 mots, 50 fiches ; trois formulations cliniques corrigées.'),('J18  Pneumonies','6 274 mots, 35 fiches, 3 cas ; cours intégré en édition de travail.')]:
 box(39,y-30,516,34,HexColor('#EDF3F4'),6);txt(50,y-12,title,9,teal,True);txt(167,y-12,detail,7.7,ink);y-=38
y-=5;box(39,y-76,516,80,navy,8)
txt(54,y-19,'CRITÈRE DE LIVRAISON',9.5,lime,True)
para(54,y-37,'Aucun des trois cours pulmonaires n’est déclaré à 100 %. L’assemblage et les liens passent le contrôle statique ; le rendu mobile, les interactions et la revue clinique indépendante restent à vérifier.',488,8.8,15,HexColor('#FFFFFF'))
y-=88;txt(39,y,'Suite immédiate : terminer les contrôles de J45/J44/J18, puis les autres cours du poumon.',8.2,muted)
y-=14;txt(39,y,'MEDINA_0 (79 Mo, avec SSP) reste séparé et n’a pas été modifié.',8.2,muted)
c.setStrokeColor(line);c.line(39,32,555,32);txt(39,19,'MEDINA_Alpha  ·  Suivi de production',7.5,muted);txt(503,19,'01 / 01',7.5,muted)
c.save();print(P)
