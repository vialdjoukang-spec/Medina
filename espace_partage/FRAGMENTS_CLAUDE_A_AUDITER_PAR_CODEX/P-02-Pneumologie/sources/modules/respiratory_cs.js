/* MEDINA · Sémiologie CS S02 · Examen respiratoire.
   Géométrie 3D locale, sans dépendance : projection de surface des lobes, scissures,
   culs-de-sac pleuraux, arbre aérien, doigt et muscles respiratoires. */
(() => {
 'use strict';
 const storageKey='medina.fragment.S02.cs.practice.v1';
 const FONT='"Atkinson Hyperlegible Next","Atkinson Hyperlegible",system-ui,sans-serif';
 /* Tronc : ellipsoïde de rayons A, B, C. Un repère se place par son angle autour du tronc
    (0 = face, ±π/2 = ligne axillaire moyenne, ±π = dos ; négatif = côté droit du patient)
    et par sa hauteur y. */
 const A=1.04,B=1.23,C=.55,PI=Math.PI;
 const surf=(t,y,lift=1.012)=>{const s=Math.sqrt(Math.max(0,1-(y/B)**2));return[A*s*Math.sin(t)*lift,y,C*s*Math.cos(t)*lift]};
 const surfNormal=p=>{const n=[p[0]/(A*A),p[1]/(B*B),p[2]/(C*C)],l=Math.hypot(...n);return n.map(x=>x/l)};
 const lerp=(pts,t)=>{t=Math.abs(t);for(let i=1;i<pts.length;i++){if(t<=pts[i][0]){const[a,ya]=pts[i-1],[b,yb]=pts[i];return ya+(yb-ya)*(t-a)/(b-a)}}return pts.at(-1)[1]};
 /* Projections de surface simplifiées (adulte, respiration calme). */
 const LUNG=[[0,-.10],[.5,-.14],[PI/2,-.37],[PI,-.59]];          // 6e côte LMC, 8e LAM, T10
 const PLEURA=[[0,-.40],[.5,-.48],[PI/2,-.77],[PI,-.99]];        // 8e côte LMC, 10e LAM, T12
 const OBLIQUE=[[0,-.11],[.3,-.11],[PI/2,.235],[PI,.62]];        // T3 → 5e côte latérale → 6e jonction chondrocostale
 const HORIZONTAL=[[0,.26],[PI/2,.235]];                         // 4e cartilage costal droit
 const TOP=1.06;
 const ribY=(n,t)=>.86-(n-1)*.2+Math.abs(t)/PI*.35;
 const COL={skin:[222,229,226],upper:[143,186,214],middle:[150,204,168],lower:[232,190,146],recess:[238,226,186],medi:[211,219,216]};
 function lobeColor(m){
  const s=Math.sqrt(Math.max(1e-6,1-(m[1]/B)**2)),t=Math.atan2(m[0]/(A*s),m[2]/(C*s)),at=Math.abs(t),y=m[1],right=t<0;
  if(y>TOP-.12*(at>2.2?1:0))return COL.skin;
  if(at<.1&&y<.95)return COL.medi;
  if(at>PI-.13)return COL.medi;
  if(!right&&at<.34&&y>-.14&&y<.22)return COL.medi;              // encoche cardiaque
  const yl=lerp(LUNG,at);
  if(y<yl)return y>lerp(PLEURA,at)?COL.recess:COL.skin;
  if(y<=lerp(OBLIQUE,at)&&at>=.3)return COL.lower;
  if(right&&at<=PI/2&&y<lerp(HORIZONTAL,at))return COL.middle;
  return COL.upper;
 }
 const P=(id,label,where,description,view='front')=>({id,label,where:Array.isArray(where[0])?where:[where],description,view});
 const T=(t,y)=>surf(t,y,1.03);
 const MODELS={
  lobes:{title:'Thorax · Lobes, scissures et culs-de-sac',legend:[['upper','Lobes supérieurs'],['middle','Lobe moyen (droit)'],['lower','Lobes inférieurs'],['recess','Cul-de-sac pleural sans poumon']],caption:'Projection de surface simplifiée chez l’adulte en respiration calme. Le côté droit du patient apparaît à gauche en vue de face. Les niveaux varient avec la morphologie et la respiration ; la radiographie et l’échographie localisent réellement une lésion.',points:[
   P('apex','Sommet pulmonaire',T(-.42,1.0),'<p>Le sommet du poumon dépasse la clavicule de deux à trois centimètres, derrière son tiers médial. Vous l’explorez en percutant et en auscultant le creux sus-claviculaire.</p><p>Une lésion apicale, par exemple une tuberculose ou une tumeur de l’apex, peut rester silencieuse à l’auscultation antérieure basse. Vous comparez donc toujours les deux sommets.</p>'),
   P('angle','Angle sternal · 2e côte',T(0,.66),'<p>L’angle sternal marque l’articulation de la deuxième côte. Vous comptez les côtes et les espaces intercostaux à partir de ce repère osseux, et non à partir du mamelon.</p><p>La bifurcation trachéale se projette habituellement à ce niveau en arrière. Les bruits trachéobronchiques s’entendent donc normalement près du sternum, sous l’angle.</p>'),
   P('hfiss','Scissure horizontale (droite)',T(-.38,.26),'<p>La petite scissure suit le quatrième cartilage costal droit, du sternum jusqu’à la ligne axillaire moyenne. Elle sépare le lobe supérieur du lobe moyen.</p><p>Au-dessous et en avant, vous auscultez donc surtout le lobe moyen. Une pneumonie du lobe moyen s’entend en avant et peut échapper à un examen limité au dos.</p>'),
   P('middle','Lobe moyen',T(-.6,.07),'<p>Le lobe moyen n’existe qu’à droite. Il se projette en avant et latéralement entre la quatrième et la sixième côte.</p><p>Il est presque absent de la face postérieure. Une matité ou des crépitants du lobe moyen se recherchent en avant et dans l’aisselle droite.</p>'),
   P('lingula','Lingula (lobe supérieur gauche)',T(.62,.04),'<p>À gauche, la lingula occupe la même région antérieure que le lobe moyen droit. Elle appartient pourtant au lobe supérieur gauche.</p><p>L’encoche cardiaque réduit la surface pulmonaire antérieure gauche. Une matité précordiale normale ne doit pas être prise pour une condensation.</p>'),
   P('base-ant','Bord inférieur antérieur · 6e côte',T(-.5,-.14),'<p>En respiration calme, le bord inférieur du poumon croise la sixième côte sur la ligne médioclaviculaire. Au-dessous, la percussion à droite rencontre la matité hépatique.</p><p>Une hypersonorité qui descend plus bas suggère une distension. Une matité qui remonte suggère un épanchement, une ascension diaphragmatique ou une condensation basale.</p>'),
   P('recess-ant','Cul-de-sac pleural · 8e côte',T(-.5,-.48),'<p>La plèvre pariétale descend environ deux côtes plus bas que le poumon : huitième côte sur la ligne médioclaviculaire. Cet espace sans poumon s’appelle le récessus costodiaphragmatique.</p><p>Le liquide pleural s’y accumule d’abord en position debout. Une matité basse et déclive est donc le premier signe d’épanchement à l’examen.</p>'),
   P('junction','Jonction des scissures · ligne axillaire',T(-PI/2,.235),'<p>Sur la ligne axillaire moyenne droite, la grande scissure croise la cinquième côte et reçoit la petite scissure. Les trois lobes droits se rencontrent dans l’aisselle.</p><p>L’auscultation axillaire explore donc plusieurs lobes à la fois. Elle complète utilement l’examen chez un patient alité qui ne peut pas s’asseoir.</p>','right'),
   P('recess-lat','Cul-de-sac latéral · 10e côte',T(-PI/2,-.77),'<p>Sur la ligne axillaire moyenne, le poumon s’arrête vers la huitième côte et la plèvre vers la dixième. Le récessus latéral est le plus profond.</p><p>Chez un patient couché, le liquide se déplace vers le dos. La matité devient alors postérieure et l’examen latéral seul la sous-estime.</p>','right'),
   P('oblique','Grande scissure · origine vers T3',T(PI-.32,.62),'<p>La grande scissure naît en arrière vers l’apophyse épineuse de T3. Elle descend en avant jusqu’à la sixième jonction chondrocostale.</p><p>Elle explique un piège fréquent : le dos explore surtout les lobes inférieurs. Les lobes supérieurs se projettent en avant et seulement au sommet du dos.</p>','back'),
   P('lower','Lobe inférieur',T(PI-.6,-.15),'<p>Les lobes inférieurs occupent la majeure partie de la face postérieure. Les pneumonies d’inhalation et les atélectasies de décubitus y siègent souvent.</p><p>Vous auscultez donc le dos de haut en bas jusqu’aux bases, en comparant chaque niveau au côté opposé.</p>','back'),
   P('base-post','Bord inférieur postérieur · T10',T(PI-.35,-.59),'<p>En arrière, le bord inférieur du poumon se situe vers T10 en expiration calme. Vous le repérez par la transition entre sonorité et matité.</p><p>L’excursion diaphragmatique se mesure entre ce niveau en expiration et en inspiration profonde. Elle atteint habituellement plusieurs centimètres chez l’adulte.</p>','back'),
   P('recess-post','Cul-de-sac postérieur · T12',T(PI-.35,-.97),'<p>La plèvre pariétale postérieure descend jusqu’à la douzième côte. Ce récessus postérieur est le point le plus déclive chez le patient assis.</p><p>Un petit épanchement y siège avant de devenir audible ou percutable plus haut. L’échographie pleurale le détecte avant l’examen physique.</p>','back')
  ]},
  auscultation:{title:'Thorax · Parcours d’auscultation et de percussion',legend:[['upper','Lobes supérieurs'],['middle','Lobe moyen'],['lower','Lobes inférieurs'],['recess','Cul-de-sac pleural']],caption:'Chaque numéro désigne une paire symétrique. Vous écoutez un cycle respiratoire complet d’un côté, puis au même niveau de l’autre côté. La position exacte des sites varie ; le principe de comparaison ne varie pas.',points:[
   P('a1','Creux sus-claviculaires',[T(-.42,1.0),T(.42,1.0)],'<p>Vous écoutez les sommets au-dessus du tiers médial des clavicules. Le patient respire bouche ouverte, un peu plus profondément que d’habitude.</p><p>Cette paire explore les sommets, siège classique de la tuberculose et des tumeurs apicales.</p>'),
   P('a2','2e espace, ligne médioclaviculaire',[T(-.5,.52),T(.5,.52)],'<p>Vous explorez les lobes supérieurs en avant. Près du sternum, le murmure peut devenir plus rude à cause de la proximité des grosses bronches.</p><p>Une respiration bronchique franche loin du sternum reste anormale.</p>'),
   P('a3','4e espace, ligne médioclaviculaire',[T(-.55,.12),T(.62,.12)],'<p>À droite, vous écoutez le lobe moyen ; à gauche, la lingula. Chez une femme, vous demandez de soulever le sein ou vous écoutez juste en dehors.</p><p>Le cœur gêne l’écoute à gauche. Vous écoutez en dehors de la zone de matité cardiaque.</p>'),
   P('a4','Aisselles, 6e espace',[T(-PI/2,-.1),T(PI/2,-.1)],'<p>Vous écoutez sur la ligne axillaire moyenne, bras levés. Cette zone explore les lobes inférieurs et, à droite, le lobe moyen.</p><p>Les crépitants de fibrose pulmonaire débutent souvent aux bases latérales et postérieures.</p>','right'),
   P('a5','Sus-épineuses',[T(-(PI-.42),.82),T(PI-.42,.82)],'<p>Au-dessus des épines des omoplates, vous explorez la partie postérieure des sommets.</p><p>Vous demandez au patient de croiser les bras devant lui. Les omoplates s’écartent et libèrent la paroi.</p>','back'),
   P('a6','Interscapulaires',[T(-(PI-.25),.38),T(PI-.25,.38)],'<p>Entre les omoplates, près de la colonne, vous entendez normalement un bruit un peu plus bronchique. Les bronches souches se projettent à ce niveau.</p><p>Cette rudesse normale ne doit pas être interprétée isolément.</p>','back'),
   P('a7','Sous-scapulaires',[T(-(PI-.5),.0),T(PI-.5,.0)],'<p>Sous la pointe des omoplates, vous explorez la partie moyenne des lobes inférieurs.</p><p>Vous vérifiez à ce niveau la symétrie des vibrations vocales et de la percussion.</p>','back'),
   P('a8','Bases postérieures',[T(-(PI-.5),-.45),T(PI-.5,-.45)],'<p>Vous finissez par les bases, juste au-dessus du bord inférieur du poumon. Les crépitants de congestion, de fibrose et d’atélectasie s’y entendent d’abord.</p><p>Vous demandez une toux puis réécoutez : des crépitants d’atélectasie peuvent disparaître, alors que ceux d’une fibrose persistent.</p>','back')
  ]},
  airways:{title:'Arbre respiratoire · Où naissent les bruits',caption:'Le schéma est stylisé. Il relie chaque bruit à son étage anatomique : larynx et trachée, bronches, alvéoles et plèvre. Les dimensions et les rapports ne sont pas réels.',points:[
   P('larynx','Larynx · stridor',[0,1.42,.17],'<p>Le stridor est un bruit musical, aigu, surtout inspiratoire. Il naît d’un rétrécissement des voies aériennes extrathoraciques : larynx ou trachée cervicale.</p><p>À l’inspiration, la pression intraluminale devient inférieure à la pression atmosphérique et la zone extrathoracique se collabe. Un stridor chez l’adulte impose une évaluation urgente des voies aériennes supérieures.</p>'),
   P('trachea','Trachée · bruit trachéal',[0,.98,.12],'<p>Au-dessus de la trachée, le bruit est fort, creux, avec une expiration aussi longue que l’inspiration. Il est normal à cet endroit.</p><p>Le même bruit entendu sur un champ pulmonaire périphérique devient un souffle tubaire. Il signifie que le parenchyme transmet anormalement bien le son trachéobronchique.</p>'),
   P('bronchi','Grosses bronches · ronchi',[-.27,.48,.2],'<p>Les ronchi sont des bruits continus graves, souvent ronflants. Ils naissent de sécrétions et de la vibration des parois des grosses bronches.</p><p>Ils se modifient souvent après une toux, ce qui les distingue d’un sibilant fixe. La nomenclature européenne les classe parmi les bruits continus de basse tonalité.</p>'),
   P('small','Petites bronches · sibilants',[.56,.15,.44],'<p>Les sibilants sont des bruits continus, musicaux, aigus, surtout expiratoires. Ils naissent quand une bronche rétrécie vibre au passage de l’air, comme une anche.</p><p>Leur absence ne prouve pas l’absence d’obstruction. Dans un asthme très grave, le débit peut devenir trop faible pour produire un son : c’est le silence auscultatoire.</p>'),
   P('alveoli','Alvéoles · crépitants',[-.62,-.5,.38],'<p>Les crépitants sont des bruits discontinus, brefs, non musicaux. Les crépitants fins correspondent surtout à la réouverture brutale de petites voies aériennes fermées en fin d’inspiration.</p><p>Les crépitants grossiers évoquent plutôt des bulles de liquide ou de sécrétions dans des voies plus larges. Vous précisez leur temps, leur siège et leur modification par la toux.</p>'),
   P('pleura','Plèvre · frottement pleural',[.92,-.3,.2],'<p>Le frottement pleural est un bruit superficiel, rugueux, entendu aux deux temps respiratoires. Il naît du frottement de feuillets pleuraux inflammatoires.</p><p>Il disparaît en apnée, contrairement à un frottement péricardique qui persiste avec le cœur. Il peut s’effacer quand un épanchement sépare les feuillets.</p>'),
   P('consolidation','Condensation · égophonie',[-.78,.08,.28],'<p>Dans une condensation, les alvéoles sont remplies mais les bronches restent ouvertes. Le parenchyme solide transmet mieux les fréquences de la voix et des bruits bronchiques.</p><p>Vous entendez alors un souffle tubaire, une bronchophonie et parfois une égophonie : le « i » prononcé par le patient devient « é ».</p>')
  ]},
  finger:{title:'Doigt · Hippocratisme digital',caption:'En haut, un doigt normal ; en bas, un doigt hippocratique. La vue de profil montre l’angle entre l’ongle et la peau du repli unguéal. Les proportions sont simplifiées.',points:[
   P('profile','Angle de profil',[.35,.71,.34],'<p>Vous regardez le doigt de profil. Vous estimez l’angle entre la lame unguéale et la peau du repli proximal.</p><p>Chez une personne sans hippocratisme, cet angle ne dépasse pas 176° selon la revue de Myers et Farquhar. Une valeur au-delà de 180° justifie une recherche de cause.</p>','front'),
   P('pdr','Rapport de profondeur phalangienne',[.5,-.88,.34],'<p>Vous comparez l’épaisseur du doigt au niveau du lit unguéal et au niveau de l’articulation interphalangienne distale. Normalement, la phalange distale est la moins épaisse.</p><p>Un rapport supérieur à 1 signe un hippocratisme. Il s’accompagne d’un rapport de vraisemblance de 3,9 pour un cancer pulmonaire dans l’étude rapportée par cette revue.</p>','front'),
   P('schamroth','Signe de Schamroth',[.3,-.26,.34],'<p>Le patient accole les faces dorsales des deux mêmes doigts, ongle contre ongle. Normalement, une petite fenêtre en losange apparaît entre les deux bases unguéales.</p><p>L’hippocratisme comble cette fenêtre. Le signe est simple et rapide, mais il reste une aide qualitative.</p>','front'),
   P('bed','Lit unguéal · mobilité',[.72,-.25,.34],'<p>Vous appuyez doucement sur la base de l’ongle. Une sensation d’ongle qui « flotte » traduit l’hypertrophie du tissu conjonctif sous-unguéal.</p><p>Ce signe dépend fortement de l’examinateur. Vous le combinez avec l’angle de profil.</p>','front'),
   P('causes','Causes à chercher',[-.5,-.55,.3],'<p>L’hippocratisme acquis accompagne surtout le cancer bronchique, les suppurations chroniques comme les bronchectasies, la mucoviscidose et la fibrose pulmonaire. Il accompagne aussi des cardiopathies cyanogènes, l’endocardite, les maladies inflammatoires de l’intestin et la cirrhose.</p><p>La BPCO isolée ne donne habituellement pas d’hippocratisme. Chez un fumeur atteint de BPCO, son apparition oriente vers une autre cause, notamment un cancer.</p>','front')
  ]},
  muscles:{title:'Respiration · Travail respiratoire et ampliation',caption:'Les muscles et les mains de l’examinateur sont schématiques. Le modèle relie les signes de lutte à leur mécanisme ; il ne représente pas l’anatomie musculaire exacte.',points:[
   P('nose','Ailes du nez et lèvres',[0,1.86,.35],'<p>Le battement des ailes du nez réduit la résistance nasale à chaque inspiration. Il signe une lutte respiratoire, surtout chez l’enfant.</p><p>La respiration à lèvres pincées freine l’expiration. Elle maintient les petites bronches ouvertes plus longtemps chez un patient atteint de BPCO.</p>'),
   P('scm','Sterno-cléido-mastoïdiens',[-.17,1.32,.2],'<p>Les sterno-cléido-mastoïdiens et les scalènes soulèvent le thorax quand le diaphragme ne suffit plus. Vous les voyez se contracter à chaque inspiration.</p><p>Leur recrutement au repos indique une charge respiratoire élevée ou un diaphragme désavantagé par une distension.</p>'),
   P('trachea','Trachée · position et hauteur',[0,1.08,.25],'<p>Vous palpez la trachée dans la fourchette sternale avec un doigt. Elle doit être médiane.</p><p>Une déviation vers le côté opposé suggère une poussée, par exemple un pneumothorax compressif ou un gros épanchement. Une déviation vers le côté atteint suggère une traction : atélectasie ou fibrose. Une hauteur laryngée, du sommet du cartilage thyroïde à la fourchette sternale, de 4 cm ou moins s’associait à une obstruction bronchique avec un rapport de vraisemblance de 2,8 dans l’étude CARE-COAD1.</p>'),
   P('supraclav','Creux sus-claviculaire · tirage',[.42,1.0,.3],'<p>Le tirage est une dépression inspiratoire des parties molles. La pression pleurale devient très négative et attire la peau vers l’intérieur.</p><p>Un tirage sus-claviculaire ou intercostal témoigne d’un effort inspiratoire important.</p>'),
   P('intercostal','Espaces intercostaux',[.82,.12,.33],'<p>Vous observez les espaces intercostaux latéraux pendant l’inspiration. Un tirage intercostal traduit une pression pleurale très négative.</p><p>Un bombement expiratoire peut se voir lors d’une expiration forcée contre une obstruction.</p>'),
   P('hoover','Marges costales · signe de Hoover',[.46,-.44,.48],'<p>Normalement, les marges costales s’écartent à l’inspiration. Dans le signe de Hoover, elles se rapprochent : le diaphragme aplati tire les côtes inférieures vers l’intérieur.</p><p>Chez des patients hospitalisés pour dyspnée, le signe avait une sensibilité de 76 % et une spécificité de 94 % pour la BPCO.</p>'),
   P('abdomen','Abdomen · respiration paradoxale',[0,-1.0,.55],'<p>Normalement, l’abdomen se soulève à l’inspiration parce que le diaphragme descend. Quand il se creuse à l’inspiration, le diaphragme est faible ou épuisé et il est aspiré vers le thorax.</p><p>Cette respiration paradoxale est un signe de fatigue respiratoire. Elle annonce un risque d’arrêt respiratoire et impose une aide immédiate.</p>'),
   P('hands','Ampliation · mains de l’examinateur',[-.0,-.45,-.55],'<p>Vous placez les mains à plat sur la partie basse du dos, pouces vers la colonne vers le dixième niveau costal. Vous demandez une inspiration profonde et regardez s’écarter les pouces.</p><p>Une ampliation diminuée d’un seul côté oriente vers la lésion de ce côté : épanchement, condensation, pneumothorax ou atélectasie.</p>','back')
  ]}
 };
 let current=null,dialog=null,opener=null,scene=null,pageCleanup=null;
 const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 const sphere=(center,radii,color,lat=12,lon=20)=>{
  const vertices=[],faces=[];
  for(let i=0;i<=lat;i++){const u=-PI/2+i*PI/lat;for(let j=0;j<=lon;j++){const v=j*2*PI/lon;vertices.push([center[0]+radii[0]*Math.cos(u)*Math.cos(v),center[1]+radii[1]*Math.sin(u),center[2]+radii[2]*Math.cos(u)*Math.sin(v)])}}
  for(let i=0;i<lat;i++)for(let j=0;j<lon;j++){const a=i*(lon+1)+j,b=a+lon+1;for(const indices of [[a,b,a+1],[a+1,b,b+1]]){const v=indices.map(k=>vertices[k]);const mid=v[0].map((_,k)=>(v[0][k]+v[1][k]+v[2][k])/3);const n=mid.map((x,k)=>(x-center[k])/(radii[k]*radii[k]));const length=Math.hypot(...n)||1;faces.push({v,n:n.map(x=>x/length),color:typeof color==='function'?color(mid):color})}}
  return faces;
 };
 const line=(v,color='#3f5961',width=2,opts={})=>({v,color,width,...opts});
 const surfLine=(f,t0,t1,color,width,opts={},steps=48)=>{const v=[];for(let i=0;i<=steps;i++){const t=t0+(t1-t0)*i/steps;v.push(surf(t,f(t)))}return line(v,color,width,{...opts,n:v.map(surfNormal)})};
 function torso(faces,lines,colorFn,detail=true){
  faces.push(...sphere([0,0,0],[A,B,C],colorFn,detail?40:20,detail?64:30));
 }
 function geometry(id){
  const faces=[],lines=[],labels=[];
  const add=(c,r,color,lat,lon)=>faces.push(...sphere(c,r,color,lat,lon));
  const skin=COL.skin;let extent=1.5,cy=.24,xext=1.15;
  if(id==='lobes'||id==='auscultation'){
   torso(faces,lines,lobeColor);add([0,1.36,0],[.26,.34,.24],skin,12,20);
   for(const n of [2,4,6,8,10])for(const sgn of [-1,1])lines.push(surfLine(t=>ribY(n,t),sgn*.12,sgn*(PI-.14),'#7f9097',1,{dash:[3,4]}));
   for(const sgn of [-1,1]){
    lines.push(surfLine(t=>lerp(OBLIQUE,t),sgn*.3,sgn*(PI-.13),'#1d3d4a',2.6));
    lines.push(surfLine(t=>lerp(LUNG,t),sgn*.1,sgn*(PI-.13),'#24414c',1.6,{dash:[7,4]}));
    lines.push(surfLine(t=>lerp(PLEURA,t),sgn*.1,sgn*(PI-.13),'#8a6d1f',1.6,{dash:[2,3]}));
    lines.push(line([[sgn*.08,.98,.5],[sgn*.45,1.03,.43],[sgn*.86,.96,.27]],'#5b6d72',3.2,{n:[[0,.3,1],[0,.3,1],[sgn*.5,.3,.8]]}));
    const sc=[[sgn*.3,.78],[sgn*.72,.70],[sgn*.42,-.05],[sgn*.3,.78]].map(([x,y])=>{const s=Math.sqrt(1-(y/B)**2),xx=Math.min(.98,Math.abs(x)/(A*s))*Math.sign(x);return surf(Math.sign(x)*(PI-Math.asin(Math.abs(xx))),y,1.02)});
    lines.push(line(sc,'#7a8a8f',1.6,{n:sc.map(surfNormal)}));
   }
   lines.push(surfLine(t=>lerp(HORIZONTAL,t),-.1,-PI/2,'#1d3d4a',2.6));
   lines.push(line([[0,.87,.56],[0,-.6,.56]],'#6c7c80',7,{n:[[0,0,1],[0,0,1]]}));
   for(const n of [2,4,6,8,10]){const p=surf(.98,ribY(n,.98)+.03,1.05);labels.push({p,text:'côte '+n,n:surfNormal(p)})}
   for(const [n,y] of [['T3',.62],['T10',-.59],['T12',-.99]]){const p=surf(PI-.02,y,1.05);labels.push({p,text:n,n:surfNormal(p)})}
  }else if(id==='airways'){
   extent=1.4;cy=.2;
   const lungR=[214,170,168],lungL=[206,176,176];
   add([-.55,-.05,0],[.45,.92,.42],lungR,18,26);add([.56,-.08,0],[.42,.88,.40],lungL,18,26);
   add([0,1.42,.02],[.17,.12,.15],[196,210,214],10,16);
   lines.push(line([[0,1.34,.1],[0,.62,.1]],'#5f8796',11));
   lines.push(line([[0,.62,.1],[-.34,.4,.16],[-.48,.2,.2]],'#5f8796',8));lines.push(line([[0,.62,.1],[.36,.38,.16],[.52,.18,.2]],'#5f8796',8));
   const branch=(o,dirs,w)=>dirs.forEach(d=>lines.push(line([o,[o[0]+d[0],o[1]+d[1],o[2]+d[2]]],'#7da3b1',w)));
   branch([-.48,.2,.2],[[-.12,.38,.12],[-.2,-.05,.16],[-.06,-.42,.16]],5);branch([.52,.18,.2],[[.1,.36,.14],[.16,-.1,.18],[.04,-.42,.16]],5);
   for(const [o,s] of [[[-.6,.58,.32],-1],[[-.68,.13,.36],-1],[[-.54,-.24,.36],-1],[[.62,.54,.34],1],[[.68,.08,.38],1],[[.56,-.24,.36],1]])branch(o,[[s*.12,.1,.05],[s*.14,-.06,.05],[s*.03,-.14,.05]],2.5);
   lines.push(line([[-.15,.46,.39],[-.6,.25,.42],[-1.0,.32,.0]],'#2b4a55',2,{dash:[5,3]}));
   lines.push(line([[-.97,.6,.0],[-.52,.4,.4],[-.15,-.6,.39],[-.35,-.92,.0]],'#2b4a55',2,{dash:[5,3]}));
   lines.push(line([[.95,.55,.0],[.52,.36,.38],[.16,-.62,.36],[.3,-.92,.0]],'#2b4a55',2,{dash:[5,3]}));
   lines.push(line([[-1.15,-1.02,0],[-.6,-1.1,.2],[0,-.92,.3],[.6,-1.1,.2],[1.15,-1.02,0]],'#8a6d1f',3));
  }else if(id==='finger'){
   extent=1.05;cy=0;xext=1.45;
   const tone=[228,198,180],club=[224,190,174];
   for(const [yc,clubbed] of [[.55,false],[-.55,true]]){
    add([-.85,yc,0],[.5,.22,.23],tone,10,18);add([-.15,yc,0],[.34,.205,.215],tone,10,18);
    if(clubbed)add([.55,yc-.03,0],[.43,.30,.29],club,16,24);else add([.55,yc,0],[.42,.19,.2],tone,14,22);
    const skinL=clubbed?[[-.2,yc+.21,.32],[.3,yc+.29,.32]]:[[-.2,yc+.215,.32],[.35,yc+.16,.32]];
    const nailL=clubbed?[[.3,yc+.29,.32],[.7,yc+.30,.32],[.93,yc+.17,.32]]:[[.35,yc+.16,.32],[.75,yc+.205,.32],[.96,yc+.13,.32]];
    lines.push(line(skinL,'#7a4a3a',2.4),line(nailL,'#c47f8a',6));
    const ext=(a,b,k)=>[b[0]+(b[0]-a[0])*k,b[1]+(b[1]-a[1])*k,.32];
    lines.push(line([skinL[1],ext(skinL[0],skinL[1],.55)],clubbed?'#a33a2e':'#2d5f72',1.4,{dash:[4,3]}));
    const top=clubbed?yc+.27:yc+.19,bot=clubbed?yc-.33:yc-.19;
    lines.push(line([[-.02,yc+.205,.33],[-.02,yc-.205,.33]],'#2d5f72',2,{dash:[3,3]}),line([[.5,top,.33],[.5,bot,.33]],clubbed?'#a33a2e':'#2d5f72',2,{dash:[3,3]}));
    labels.push({p:[.6,yc+(clubbed?.46:.36),.3],text:clubbed?'angle > 180°':'angle ≈ 165°'});
    labels.push({p:[-.02,yc-.33,.3],text:'IPD'},{p:[.42,bot-.1,.3],text:clubbed?'lit unguéal > IPD':'lit unguéal < IPD'});
   }
   lines.push(line([[-1.4,0,0],[1.35,0,0]],'#b9c4c7',1,{dash:[4,5]}));
   labels.push({p:[-1.32,.93,.25],text:'Doigt normal'},{p:[-1.32,-.17,.25],text:'Hippocratisme'});
  }else if(id==='muscles'){
   extent=1.9;cy=.43;
   add([0,-.18,0],[A,B,C],m=>m[2]>0&&m[1]<-.23-.8*Math.abs(m[0])?[210,224,230]:skin,22,34);add([0,1.25,0],[.24,.42,.22],skin,12,20);add([0,1.85,-.02],[.36,.42,.33],skin,14,22);
   for(const s of [-1,1]){
    lines.push(line([[s*.2,1.62,.05],[s*.17,1.35,.2],[s*.07,1.05,.27]],'#a2524e',4));
    lines.push(line([[s*.25,1.5,.0],[s*.32,1.15,.12]],'#b36d68',2.4));
    lines.push(line([[s*.08,1.02,.48],[s*.45,1.06,.42],[s*.86,.98,.27]],'#5b6d72',3,{n:[[0,.3,1],[0,.3,1],[s*.5,.3,.8]]}));
    lines.push(line([[s*.05,-.05,.55],[s*.36,-.38,.5],[s*.72,-.66,.38],[s*.92,-.78,.18]],'#2d5f72',3,{n:[[0,0,1],[s*.2,0,1],[s*.5,0,.8],[s*.8,0,.5]]}));
    for(let i=0;i<4;i++){const y=.5-i*.22;lines.push(line([[s*.72,y,.36],[s*.98,y-.04,.06]],'#8d9da2',1.2,{n:[[s*.6,0,.8],[s,0,.1]]}))}
    lines.push(line([[s*.62,-.2,-.47],[s*.12,-.42,-.55]],'#2d5f72',5,{n:[[s*.4,0,-1],[0,0,-1]]}));
    lines.push(line([[s*.12,-.42,-.55],[s*.04,-.36,-.56]],'#a33a2e',4,{n:[[0,0,-1],[0,0,-1]]}));
   }
   lines.push(line([[0,1.68,.33],[0,1.82,.36]],'#7a5b52',2));
   lines.push(line([[-.08,1.62,.31],[.08,1.62,.31]],'#a2524e',2.4));
   lines.push(line([[0,.62,-.56],[0,-1.0,-.56]],'#9aa7aa',3,{n:[[0,0,-1],[0,0,-1]]}));
  }
  return {faces,lines,labels,extent,cy,xext};
 }
 function makeScene(canvas,id){
  const ctx=canvas.getContext('2d');if(!ctx)return null;
  const g=geometry(id),model=MODELS[id];let yaw=0,pitch=0,zoom=1,active=0,frame=0,destroyed=false,drag=null,markers=[];
  const transform=p=>{const cy=Math.cos(yaw),sy=Math.sin(yaw),cp=Math.cos(pitch),sp=Math.sin(pitch);const x=p[0]*cy+p[2]*sy,z=-p[0]*sy+p[2]*cy;return[x,p[1]*cp-z*sp,p[1]*sp+z*cp]};
  const facing=n=>!n||transform(n)[2]>-.02;
  function draw(){
   frame=0;if(destroyed)return;
   const rect=canvas.getBoundingClientRect(),w=rect.width,h=rect.height;if(!w||!h)return;
   const dpr=Math.min(devicePixelRatio||1,2);canvas.width=Math.round(w*dpr);canvas.height=Math.round(h*dpr);ctx.setTransform(dpr,0,0,dpr,0,0);
   ctx.fillStyle='#f5f9fa';ctx.fillRect(0,0,w,h);
   const scale=Math.min(w*.46/g.xext,h*.47/g.extent)*zoom;
   const project=p=>{const factor=5/(5-p[2]);return[w/2+p[0]*scale*factor,h/2-(p[1]-g.cy*Math.cos(pitch))*scale*factor]};
   const faces=g.faces.map(f=>{const v=f.v.map(transform);return{...f,v,n:transform(f.n),z:(v[0][2]+v[1][2]+v[2][2])/3}}).sort((a,b)=>a.z-b.z);
   for(const f of faces){const shade=.78+.22*Math.max(0,f.n[0]*-.24+f.n[1]*.43+f.n[2]*.77);ctx.fillStyle='rgb('+f.color.map(x=>Math.round(x*shade)).join(',')+')';ctx.beginPath();f.v.forEach((v,i)=>{const p=project(v);i?ctx.lineTo(...p):ctx.moveTo(...p)});ctx.closePath();ctx.fill();ctx.strokeStyle=ctx.fillStyle;ctx.lineWidth=.6;ctx.stroke()}
   for(const l of g.lines){ctx.strokeStyle=l.color;ctx.lineWidth=l.width;ctx.setLineDash(l.dash||[]);ctx.lineCap='round';ctx.beginPath();let pen=false;l.v.forEach((v,i)=>{const ok=!l.n||facing(l.n[i]);if(!ok){pen=false;return}const p=project(transform(v));pen?ctx.lineTo(...p):ctx.moveTo(...p);pen=true});ctx.stroke()}
   ctx.setLineDash([]);
   ctx.font='600 11px '+FONT;ctx.textAlign='left';ctx.textBaseline='middle';
   for(const lb of g.labels){if(!facing(lb.n))continue;const p=project(transform(lb.p));ctx.fillStyle='#ffffffcc';const tw=ctx.measureText(lb.text).width;ctx.fillRect(p[0]-2,p[1]-8,tw+4,16);ctx.fillStyle='#22343a';ctx.fillText(lb.text,p[0],p[1])}
   markers=[];model.points.forEach((pt,i)=>pt.where.forEach(pos=>{const tp=transform(pos),xy=project(tp);const n=id==='lobes'||id==='auscultation'?transform(surfNormal(pos))[2]:tp[2]+.25;markers.push({xy,i,z:tp[2],back:n<-.02})}));
   markers.sort((a,b)=>a.z-b.z);
   const groups=[];for(const m of markers){const same=groups.find(x=>Math.hypot(x.xy[0]-m.xy[0],x.xy[1]-m.xy[1])<1&&x.back===m.back);if(same)same.indices.push(m.i);else groups.push({...m,xy:[...m.xy],indices:[m.i]})}
   const placed=[];
   for(const m of groups){
    const anchor=[...m.xy];
    if(!m.back){for(const [dx,dy] of [[0,0],[26,0],[-26,0],[0,26],[0,-26],[40,0],[-40,0]]){const q=[anchor[0]+dx,anchor[1]+dy];if(q[0]>14&&q[0]<w-14&&q[1]>30&&q[1]<h-14&&placed.every(p=>Math.hypot(p[0]-q[0],p[1]-q[1])>=26)){m.xy=q;break}}placed.push(m.xy)}
    m.screen=m.xy;
    if(Math.hypot(m.xy[0]-anchor[0],m.xy[1]-anchor[1])>1){ctx.strokeStyle='#4d6870';ctx.lineWidth=1.3;ctx.beginPath();ctx.moveTo(...anchor);ctx.lineTo(...m.xy);ctx.stroke();ctx.beginPath();ctx.arc(...anchor,2.5,0,PI*2);ctx.fillStyle='#10323d';ctx.fill()}
    const selected=m.indices.includes(active);ctx.globalAlpha=m.back?.32:1;
    ctx.beginPath();ctx.arc(...m.xy,selected?13:10.5,0,PI*2);ctx.fillStyle=selected?'#2a6577':'#fff';ctx.fill();ctx.lineWidth=selected?3:2;ctx.strokeStyle=selected?'#0f2f3a':'#4d6870';ctx.stroke();
    ctx.fillStyle=selected?'#fff':'#0f2f3a';ctx.font='700 12px '+FONT;ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(m.indices.map(i=>i+1).join('/'),m.xy[0],m.xy[1]+.5);ctx.globalAlpha=1;
   }
   markers=groups;
   ctx.fillStyle='#3d555c';ctx.textAlign='left';ctx.textBaseline='alphabetic';ctx.font='12px '+FONT;ctx.fillText(id==='airways'||id==='muscles'?'Schéma stylisé':id==='finger'?'Vue de profil simplifiée':'Projection de surface simplifiée',12,18);
   canvas.dataset.rcsYaw=yaw.toFixed(3);canvas.dataset.rcsPitch=pitch.toFixed(3);canvas.dataset.rcsZoom=zoom.toFixed(2);
  }
  const schedule=()=>{if(!frame&&!destroyed)frame=requestAnimationFrame(draw)};
  const rotate=(dy,dp)=>{yaw+=dy;pitch=Math.max(-.75,Math.min(.75,pitch+dp));schedule()};
  const setView=view=>{yaw=view==='back'?PI:view==='right'?PI/2:view==='left'?-PI/2:0;pitch=0;schedule()};
  const reset=()=>{yaw=0;pitch=0;zoom=1;schedule()};
  const down=e=>{drag={x:e.clientX,y:e.clientY,startX:e.clientX,startY:e.clientY,moved:false};canvas.setPointerCapture(e.pointerId);canvas.focus({preventScroll:true})};
  const move=e=>{if(!drag)return;const dx=e.clientX-drag.x,dy=e.clientY-drag.y;if(Math.hypot(e.clientX-drag.startX,e.clientY-drag.startY)>5)drag.moved=true;rotate(dx*.010,dy*.009);drag.x=e.clientX;drag.y=e.clientY};
  const up=e=>{if(drag&&!drag.moved){const rect=canvas.getBoundingClientRect(),x=e.clientX-rect.left,y=e.clientY-rect.top;const hit=markers.filter(m=>!m.back).map(m=>({...m,d:Math.hypot(m.screen[0]-x,m.screen[1]-y)})).sort((a,b)=>a.d-b.d)[0];if(hit?.d<22)selectPoint(hit.indices[0],false)}drag=null;if(canvas.hasPointerCapture(e.pointerId))canvas.releasePointerCapture(e.pointerId)};
  const cancel=()=>{drag=null};
  const key=e=>{const moves={ArrowLeft:[-.16,0],ArrowRight:[.16,0],ArrowUp:[0,-.12],ArrowDown:[0,.12]};if(moves[e.key]){e.preventDefault();rotate(...moves[e.key])}else if(e.key==='Home'){e.preventDefault();reset()}};
  canvas.addEventListener('pointerdown',down);canvas.addEventListener('pointermove',move);canvas.addEventListener('pointerup',up);canvas.addEventListener('pointercancel',cancel);canvas.addEventListener('keydown',key);
  const observer=new ResizeObserver(schedule);observer.observe(canvas);schedule();
  return{rotate,setView,reset,zoom:value=>{zoom=value;schedule()},select:(i,view)=>{active=i;if(view)setView(view);else schedule()},destroy:()=>{destroyed=true;cancelAnimationFrame(frame);observer.disconnect();canvas.removeEventListener('pointerdown',down);canvas.removeEventListener('pointermove',move);canvas.removeEventListener('pointerup',up);canvas.removeEventListener('pointercancel',cancel);canvas.removeEventListener('keydown',key)}};
 }
 function selectPoint(index,changeView=true,reveal=false){
  const p=MODELS[current]?.points[index];if(!p)return;
  dialog.querySelectorAll('[data-rcs-select]').forEach((b,i)=>b.setAttribute('aria-pressed',String(i===index)));
  const detail=dialog.querySelector('.rcs-point-detail');detail.innerHTML='<h3>'+esc((index+1)+' · '+p.label)+'</h3>'+p.description;
  detail.dataset.rcsSelected=p.id;
  scene?.select(index,changeView?p.view:null);
  if(reveal&&matchMedia('(max-width:760px)').matches)detail.scrollIntoView({block:'nearest',behavior:'instant'});
 }
 function ensureDialog(){
  if(dialog)return;
  dialog=document.createElement('dialog');dialog.id='medina-rcs-dialog';dialog.className='rcs-dialog';dialog.setAttribute('aria-labelledby','rcs-dialog-title');
  document.body.append(dialog);
  dialog.addEventListener('keydown',e=>{if(e.key!=='Tab')return;const items=Array.from(dialog.querySelectorAll('button,input,[tabindex]')).filter(x=>!x.disabled&&x.tabIndex>=0&&x.getClientRects().length);const first=items[0],last=items.at(-1);if(e.shiftKey&&document.activeElement===first){e.preventDefault();last?.focus()}else if(!e.shiftKey&&document.activeElement===last){e.preventDefault();first?.focus()}});
  dialog.addEventListener('close',()=>{scene?.destroy();scene=null;current=null;if(opener?.isConnected)opener.focus({preventScroll:true})});
  dialog.addEventListener('click',e=>{if(e.target===dialog){const r=dialog.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)dialog.close()}});
 }
 function open(id,trigger,initialPoint){
  const model=MODELS[id];if(!model)return;
  ensureDialog();scene?.destroy();opener=trigger;current=id;
  const views=id==='finger'?[['front','Profil']]:[['front','Face'],['right','Côté droit'],['left','Côté gauche'],['back','Dos']];
  const legend=model.legend?'<ul class="rcs-legend" aria-label="Légende des couleurs">'+model.legend.map(([k,t])=>'<li><span style="background:rgb('+COL[k].join(',')+')"></span>'+esc(t)+'</li>').join('')+'<li><span class="rcs-legend-line"></span>Scissures</li><li><span class="rcs-legend-dash"></span>Bord inférieur du poumon</li><li><span class="rcs-legend-dot"></span>Limite pleurale</li></ul>':'';
  dialog.innerHTML='<header class="rcs-dialog-header"><h2 id="rcs-dialog-title">'+esc(model.title)+'</h2><button type="button" class="rcs-dialog-close">Fermer ×</button></header><div class="rcs-dialog-body"><div><figure class="rcs-scene"><canvas class="rcs-canvas" width="760" height="650" tabindex="0" role="img" aria-label="Modèle 3D : '+esc(model.title)+'. Les flèches font tourner le modèle ; la touche Début réinitialise la vue.">Les repères et leurs explications sont disponibles dans les boutons à côté du modèle.</canvas><figcaption>'+esc(model.caption)+'</figcaption></figure>'+legend+'<div class="rcs-rotate-controls" role="group" aria-label="Orientation du modèle"><button type="button" data-rcs-rotate="left">← Tourner</button><button type="button" data-rcs-rotate="right">Tourner →</button>'+views.map(([v,t])=>'<button type="button" data-rcs-view="'+v+'">'+t+'</button>').join('')+'<button type="button" data-rcs-reset>Réinitialiser</button></div><label class="rcs-zoom">Zoom <input type="range" min="75" max="150" value="100" aria-label="Zoom du modèle 3D"></label><p class="rcs-orientation">Vous faites glisser le modèle avec la souris ou un doigt. Au clavier, les flèches le font tourner lorsque le modèle a le focus. Les repères estompés se trouvent sur la face cachée.</p><p class="rcs-canvas-fallback" hidden>Le dessin 3D n’est pas disponible ici. Tous les repères et leurs explications restent accessibles avec les boutons numérotés.</p></div><div><div class="rcs-points" role="group" aria-label="Repères">'+model.points.map((p,i)=>'<button type="button" data-rcs-select="'+i+'" aria-pressed="false">'+(i+1)+' · '+esc(p.label)+'</button>').join('')+'</div><section class="rcs-point-detail" aria-live="polite" aria-atomic="true"></section></div></div>';
  dialog.querySelector('.rcs-dialog-close').onclick=()=>dialog.close();
  dialog.querySelectorAll('[data-rcs-select]').forEach(b=>b.onclick=()=>selectPoint(Number(b.dataset.rcsSelect),true,true));
  dialog.querySelectorAll('[data-rcs-rotate]').forEach(b=>b.onclick=()=>scene?.rotate(b.dataset.rcsRotate==='left'?-.25:.25,0));
  dialog.querySelectorAll('[data-rcs-view]').forEach(b=>b.onclick=()=>scene?.setView(b.dataset.rcsView));
  dialog.querySelector('[data-rcs-reset]').onclick=()=>{scene?.reset();dialog.querySelector('input[type="range"]').value='100'};
  dialog.querySelector('input[type="range"]').oninput=e=>scene?.zoom(Number(e.target.value)/100);
  if(!dialog.open)dialog.showModal();
  scene=makeScene(dialog.querySelector('canvas'),id);dialog.querySelector('.rcs-canvas-fallback').hidden=!!scene;
  const index=model.points.findIndex(p=>p.id===initialPoint);selectPoint(index>=0?index:0);
  dialog.querySelector('.rcs-dialog-close').focus({preventScroll:true});dialog.scrollTop=0;
 }
 function destroy(){if(dialog?.open)dialog.close();scene?.destroy();scene=null;pageCleanup?.();pageCleanup=null}
 function mount(root){
  const page=root.querySelector('.rcs-page');if(!page)return;
  let checks={};try{checks=JSON.parse(localStorage.getItem(storageKey)||'{}')||{}}catch{checks={}}
  const boxes=Array.from(page.querySelectorAll('[data-rcs-check]'));
  const update=()=>{const out=page.querySelector('.rcs-progress');if(out)out.textContent=boxes.filter(b=>b.checked).length+' / '+boxes.length+' étapes cochées';try{localStorage.setItem(storageKey,JSON.stringify(Object.fromEntries(boxes.map(b=>[b.dataset.rcsCheck,b.checked]))))}catch{}};
  boxes.forEach(b=>{b.checked=checks[b.dataset.rcsCheck]===true});update();
  const click=e=>{
   const model=e.target.closest('[data-rcs-model]');if(model){open(model.dataset.rcsModel,model,model.dataset.rcsPoint);return}
   const jump=e.target.closest('[data-rcs-jump]');if(jump){e.preventDefault();const target=page.querySelector('#'+jump.dataset.rcsJump);target?.scrollIntoView({block:'start',behavior:'instant'});const heading=target?.querySelector('h2');heading?.setAttribute('tabindex','-1');heading?.focus({preventScroll:true});return}
   const answer=e.target.closest('[data-rcs-choice]');if(answer){const quiz=answer.closest('.rcs-quiz');quiz.querySelectorAll('[data-rcs-choice]').forEach(b=>{b.removeAttribute('data-result');b.setAttribute('aria-pressed',String(b===answer))});const correct=answer.dataset.rcsChoice===quiz.dataset.rcsAnswer;answer.dataset.result=correct?'correct':'incorrect';quiz.querySelector('[data-rcs-choice="'+quiz.dataset.rcsAnswer+'"]').dataset.result='correct';const feedback=quiz.querySelector('.rcs-feedback');feedback.hidden=false;feedback.setAttribute('role','status');feedback.dataset.rcsResult=correct?'correct':'incorrect';return}
   if(e.target.closest('.rcs-reset-checklist')){boxes.forEach(b=>b.checked=false);update()}
  };
  const change=e=>{if(e.target.matches('[data-rcs-check]'))update()};
  page.addEventListener('click',click);page.addEventListener('change',change);pageCleanup=()=>{page.removeEventListener('click',click);page.removeEventListener('change',change)};
 }
 window.MEDINA_CS={page:()=>document.getElementById('medina-rcs-page')?.innerHTML||'',mount,destroy};
})();
