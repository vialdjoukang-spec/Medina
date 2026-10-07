/* Local, dependency-free 3D surface geometry for cardiovascular examination. */
(() => {
 'use strict';
 const storageKey='medina.fragment.S01.cs.practice.v1';
 const point=(id,label,p,description,view='front')=>({id,label,p,description,view});
 const MODELS={
  thorax:{title:'Thorax · Repères de l’examen',caption:'Les zones d’écoute sont des repères de surface. Elles ne sont pas les positions exactes des valves. Les proportions sont simplifiées. Dans la vue de face, le côté droit du patient apparaît à gauche.',points:[
   point('sternal','Angle sternal',[0,.75,.55],'<p>Vous palpez la jonction entre le manubrium et le corps du sternum. La deuxième côte s’articule à ce niveau. Vous comptez les espaces intercostaux à partir de ce repère.</p><p>Le mamelon change de position selon la morphologie. Il ne remplace pas ce repérage osseux.</p>'),
   point('aortic','Foyer aortique',[-.22,.63,.55],'<p>Vous écoutez au deuxième espace intercostal droit, près du sternum. Vous cherchez un souffle d’éjection et son irradiation, notamment vers les carotides.</p><p>Le foyer est une zone de transmission acoustique. La valve aortique se situe plus profondément et dans une autre position.</p>'),
   point('pulmonic','Foyer pulmonaire',[.22,.63,.55],'<p>Vous écoutez au deuxième espace intercostal gauche, près du sternum. Le diaphragme du stéthoscope aide à entendre les composantes du deuxième bruit.</p><p>À l’inspiration, la composante pulmonaire peut se fermer plus tard. Vous comparez une respiration calme et l’expiration.</p>'),
   point('erb','Zone d’Erb',[.22,.40,.58],'<p>Vous complétez l’écoute au troisième espace intercostal gauche. Un souffle diastolique de fuite aortique peut être bien transmis dans cette région ou plus bas au bord sternal.</p><p>Vous recherchez le souffle chez un patient assis, penché en avant, en expiration confortable, lorsque son état le permet.</p>'),
   point('tricuspid','Foyer tricuspide',[.19,.10,.57],'<p>Vous écoutez au bord sternal gauche bas, vers les quatrième et cinquième espaces intercostaux. L’inspiration peut renforcer un souffle tricuspide par augmentation du retour veineux droit.</p><p>Vous décrivez d’abord le temps et le siège. La variation respiratoire oriente sans établir seule l’étiologie.</p>'),
   point('mitral','Foyer mitral',[.64,-.04,.46],'<p>Vous écoutez dans la région de l’apex, habituellement au cinquième espace intercostal gauche près de la ligne médioclaviculaire. Vous recherchez les bruits et les souffles apicaux.</p><p>Le décubitus latéral gauche facilite l’écoute des phénomènes graves. La cloche est posée légèrement. Un souffle holosystolique irradiant vers l’aisselle peut évoquer une fuite mitrale.</p>'),
   point('apex','Choc de pointe',[.64,-.04,.46],'<p>Vous palpez le choc de pointe avec la pulpe des doigts. Vous décrivez son siège, son étendue et sa durée. Il est habituellement situé vers le cinquième espace intercostal gauche.</p><p>Un déplacement peut accompagner une dilatation ou un déplacement médiastinal. Une pointe non palpable ne permet pas de conclure sur la fonction cardiaque.</p>')
  ]},
  neck:{title:'Cou · Onde veineuse et pouls artériel',caption:'La position et la hauteur sont schématiques. La mesure réelle utilise une verticale au-dessus de l’angle sternal chez le patient installé.',points:[
   point('jugular','Jugulaire interne droite',[-.23,.69,.29],'<p>Vous observez l’onde veineuse, sans la confondre avec une artère palpable. Vous ajustez l’inclinaison du patient jusqu’à voir son sommet. La respiration et la position modifient cette onde.</p><p>Vous mesurez sa hauteur verticale au-dessus de l’angle sternal. Si l’onde reste invisible, vous décrivez une jugulaire non visualisée.</p>'),
   point('carotid','Carotide droite',[-.09,.67,.36],'<p>Vous palpez doucement une seule carotide à la fois. Vous appréciez l’amplitude et la montée du pouls. Vous ne comprimez jamais les deux côtés simultanément.</p><p>La carotide donne normalement une impulsion palpable. L’onde jugulaire est surtout observée. Aucun massage du sinus carotidien ne fait partie de cet examen de routine.</p>'),
   point('angle','Angle sternal',[0,.09,.46],'<p>L’angle sternal fournit le repère de hauteur. Vous mesurez une distance verticale et notez l’inclinaison du patient. Le modèle n’est pas une règle calibrée.</p><p>L’ajout conventionnel de cinq centimètres estime la pression en centimètres d’eau. Cette convention possède des limites et ne correspond pas à une mesure invasive.</p>'),
   point('atrium','Oreillette droite · relation',[ -.18,-.26,.16],'<p>La jugulaire communique avec le réseau veineux central et renseigne indirectement sur les pressions droites. La hauteur dépend de la pression, de la respiration et de la position.</p><p>Une estimation élevée ne mesure pas directement le volume sanguin total. Vous la confrontez à la congestion et au contexte clinique.</p>')
  ]},
  pulses:{title:'Artères · Sites de palpation',caption:'Les repères illustrent principalement un côté. L’examen réel compare les deux membres. La position des artères varie avec la morphologie.',points:[
   point('brachial','Pouls brachial',[1.08,.13,.21],'<p>Vous palpez l’artère brachiale sur la face médiale du bras ou dans la région antécubitale selon le geste. Le bras doit être relâché.</p><p>Ce repère aide la mesure auscultatoire de pression. Une pression excessive des doigts peut effacer une faible pulsation.</p>'),
   point('radial','Pouls radial',[1.09,-.78,.23],'<p>Vous palpez le côté radial du poignet avec la pulpe des doigts. Vous appréciez fréquence, régularité et amplitude. Vous comparez les deux côtés selon l’indication.</p><p>Vous comptez pendant une minute si le rythme est irrégulier. Le pouls oriente le rythme ; l’ECG l’identifie.</p>'),
   point('femoral','Pouls fémoral',[.36,-.75,.30],'<p>Vous expliquez le geste et préservez l’intimité. Vous cherchez le pouls sous le ligament inguinal, approximativement à mi-distance entre l’épine iliaque antérosupérieure et la symphyse pubienne.</p><p>Vous comparez les côtés. Un pouls diminué ou non perçu nécessite une interprétation technique et clinique.</p>'),
   point('popliteal','Pouls poplité',[.39,-1.72,-.23],'<p>Vous fléchissez légèrement le genou et palpez profondément le creux poplité. Ce pouls peut être difficile à percevoir même sans occlusion.</p><p>La vue postérieure situe le creux. Vous complétez par un Doppler lorsque la question clinique reste ouverte.</p>','back'),
   point('posterior-tibial','Pouls tibial postérieur',[.23,-2.39,.14],'<p>Vous cherchez la pulsation derrière et légèrement sous la malléole médiale. Vous évitez une pression trop forte et comparez le côté opposé.</p><p>Ce pouls et le pédieux participent à l’examen distal. La perfusion se juge avec les symptômes, la peau et les mesures hémodynamiques.</p>'),
   point('dorsalis','Pouls pédieux',[.41,-2.55,.43],'<p>Vous palpez le dos du pied, habituellement près du tendon de l’extenseur du gros orteil. La position et la perception varient.</p><p>Un pouls non perçu ne prouve pas une occlusion. Vous vérifiez la technique puis utilisez le Doppler et l’index cheville-bras si cela répond à la question.</p>')
  ]},
  heart:{title:'Cœur · Cavités, valves et bruits',caption:'Les cavités et les connexions sont stylisées. Le modèle explique le trajet et le cycle ; il ne représente pas les rapports anatomiques exacts ni une imagerie.',points:[
   point('right-atrium','Oreillette droite',[-.47,.65,.22],'<p>L’oreillette droite reçoit le retour veineux systémique. Elle se vide vers le ventricule droit lorsque la valve tricuspide est ouverte.</p><p>Une augmentation de pression dans ce territoire peut se transmettre à la jugulaire. Vous reliez l’onde veineuse à ce mécanisme.</p>'),
   point('right-ventricle','Ventricule droit',[-.47,-.41,.27],'<p>Le ventricule droit propulse le sang vers l’artère pulmonaire. L’inspiration augmente habituellement le retour veineux droit et peut prolonger son éjection.</p><p>Ce mécanisme participe au retard physiologique de la fermeture pulmonaire et au dédoublement inspiratoire de B2.</p>'),
   point('left-atrium','Oreillette gauche',[.47,.65,.17],'<p>L’oreillette gauche reçoit le sang des veines pulmonaires. Elle se vide vers le ventricule gauche pendant la diastole.</p><p>Une pression élevée peut se transmettre au réseau pulmonaire. Elle aide à comprendre la dyspnée dans une maladie mitrale.</p>'),
   point('left-ventricle','Ventricule gauche',[.47,-.41,.30],'<p>Le ventricule gauche éjecte dans l’aorte pendant la systole. La perfusion systémique dépend de cette fonction et de la charge imposée à l’éjection.</p><p>L’impulsion apicale et les sons transmis fournissent des indices. L’échocardiographie mesure la fonction et les dimensions.</p>'),
   point('tricuspid-valve','Valve tricuspide · B1',[-.47,.14,.35],'<p>La valve tricuspide relie l’oreillette et le ventricule droits. Sa fermeture participe au premier bruit, au début de la systole ventriculaire.</p><p>Une fuite peut produire un souffle systolique. Le foyer d’écoute se situe au bord sternal gauche bas.</p>'),
   point('mitral-valve','Valve mitrale · B1',[.47,.14,.35],'<p>La fermeture mitrale participe au premier bruit. Une sténose gêne le remplissage diastolique. Une fuite permet un retour systolique vers l’oreillette.</p><p>Le temps du souffle découle du gradient de pression. Il aide à comprendre pourquoi une sténose mitrale et une fuite mitrale ne s’entendent pas au même moment.</p>'),
   point('aortic-valve','Valve aortique · B2',[.19,-.04,.47],'<p>La valve aortique s’ouvre pendant l’éjection puis se ferme lorsque le gradient s’inverse. Sa fermeture participe au deuxième bruit.</p><p>Une sténose produit un obstacle systolique. Une fuite permet un retour en diastole. Les foyers sont des zones de transmission, distinctes de cette position schématique.</p>'),
   point('pulmonary-valve','Valve pulmonaire · B2',[-.16,-.04,.49],'<p>La fermeture pulmonaire participe au deuxième bruit. À l’inspiration, elle peut survenir un peu après la fermeture aortique.</p><p>Vous recherchez cette variation au foyer pulmonaire avec une respiration calme. Un dédoublement pathologique doit être interprété dans l’ensemble de l’examen.</p>')
  ]}
 };
 let current=null,dialog=null,opener=null,scene=null,pageCleanup=null;
 const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 const sphere=(center,radii,color,lat=12,lon=20)=>{
  const vertices=[],faces=[];
  for(let i=0;i<=lat;i++){const u=-Math.PI/2+i*Math.PI/lat;for(let j=0;j<=lon;j++){const v=j*2*Math.PI/lon;vertices.push([center[0]+radii[0]*Math.cos(u)*Math.cos(v),center[1]+radii[1]*Math.sin(u),center[2]+radii[2]*Math.cos(u)*Math.sin(v)])}}
  for(let i=0;i<lat;i++)for(let j=0;j<lon;j++){const a=i*(lon+1)+j,b=a+lon+1;for(const indices of [[a,b,a+1],[a+1,b,b+1]]){const v=indices.map(k=>vertices[k]);const mid=v[0].map((_,k)=>(v[0][k]+v[1][k]+v[2][k])/3);const n=mid.map((x,k)=>(x-center[k])/(radii[k]*radii[k]));const length=Math.hypot(...n);faces.push({v,n:n.map(x=>x/length),color})}}
  return faces;
 };
 const line=(v,color='#405d50',width=2)=>({v,color,width});
 function geometry(id){
  const faces=[],lines=[];
  const add=(c,r,color,lat,lon)=>faces.push(...sphere(c,r,color,lat,lon));
  const skin=[218,228,220],bone=[194,209,199],right=[139,181,199],left=[188,118,120];
  let extent=1.7;
  if(id==='thorax'){
   add([0,0,0],[1.04,1.23,.50],skin,18,28);add([0,1.29,0],[.25,.37,.23],skin);
   for(let i=0;i<7;i++){const v=[];for(let j=0;j<=28;j++){const a=-1.24+2.48*j/28;v.push([.96*Math.sin(a),.66-i*.225+.09*Math.cos(a),.51*Math.cos(a)])}lines.push(line(v,'#71857a',1.4))}
   lines.push(line([[0,.87,.535],[0,-.64,.535]],'#61746a',8));
   lines.push(line([[-.88,.96,.26],[-.45,1.04,.42],[0,.97,.48],[.45,1.04,.42],[.88,.96,.26]],'#61746a',3));
  }else if(id==='neck'){
   add([0,-.37,0],[.91,.74,.43],skin,16,26);add([0,.70,0],[.25,.49,.24],skin,14,22);add([0,1.34,-.02],[.39,.43,.34],skin,16,24);
   lines.push(line([[-.38,.07,.36],[-.25,.63,.26],[-.20,1.01,.23]],'#466c87',5));
   lines.push(line([[-.08,.10,.42],[-.09,.66,.36],[-.12,1.00,.25]],'#a45e61',4));
   lines.push(line([[-.55,.10,.33],[-.15,.90,.26]],'#9caea2',3));
   lines.push(line([[-.75,.09,.26],[0,.09,.46],[.75,.09,.26]],'#61746a',3));
   lines.push(line([[.65,.09,.45],[.65,.84,.45]],'#61746a',1));
   lines.push(line([[.59,.09,.45],[.71,.09,.45]],'#61746a',2));lines.push(line([[.59,.84,.45],[.71,.84,.45]],'#61746a',2));
  }else if(id==='pulses'){
   extent=2.75;
   add([0,.35,0],[.78,.93,.37],skin);add([0,1.50,0],[.17,.33,.17],skin);add([0,1.91,0],[.29,.34,.25],skin);
   for(const side of [-1,1]){add([side*.97,.42,0],[.20,.64,.18],skin,10,16);add([side*1.08,-.37,0],[.145,.58,.145],skin,10,16);add([side*1.08,-.91,.06],[.16,.22,.12],skin,10,16);add([side*.39,-1.12,0],[.24,.64,.22],skin,10,18);add([side*.39,-1.95,0],[.18,.63,.18],skin,10,18);add([side*.39,-2.55,.16],[.19,.12,.34],skin,10,18);
    lines.push(line([[side*.28,1.03,.34],[side*.79,.95,.24],[side*1.03,.18,.20],[side*1.08,-.78,.21]],'#9b6462',2));
    lines.push(line([[side*.26,-.51,.33],[side*.36,-.75,.30],[side*.40,-1.49,.24],[side*.40,-2.20,.19],[side*.39,-2.54,.46]],'#9b6462',2));
   }
  }else if(id==='heart'){
   extent=1.5;
   add([-.47,.57,0],[.43,.48,.33],right,16,24);add([.47,.57,0],[.43,.48,.33],left,16,24);
   add([-.47,-.43,0],[.46,.70,.36],right,18,26);add([.47,-.43,0],[.46,.70,.39],left,18,26);
   add([.18,.47,.36],[.11,.65,.11],left,12,18);add([-.18,.43,.40],[.11,.59,.11],right,12,18);
   for(const c of [[-.47,.14,.35],[.47,.14,.35],[.19,-.04,.47],[-.16,-.04,.49]]){const v=[];for(let i=0;i<=36;i++){const a=i*2*Math.PI/36;v.push([c[0]+.12*Math.cos(a),c[1]+.055*Math.sin(a),c[2]+.018])}lines.push(line(v,'#f4ead4',4))}
  }
  return {faces,lines,extent};
 }
 function makeScene(canvas,id){
  const ctx=canvas.getContext('2d');if(!ctx)return null;
  const g=geometry(id);let yaw=0,pitch=0,zoom=1,active=0,frame=0,destroyed=false,drag=null,markers=[];
  const transform=p=>{const cy=Math.cos(yaw),sy=Math.sin(yaw),cp=Math.cos(pitch),sp=Math.sin(pitch);const x=p[0]*cy+p[2]*sy,z=-p[0]*sy+p[2]*cy;return[x,p[1]*cp-z*sp,p[1]*sp+z*cp]};
  function draw(){
   frame=0;if(destroyed)return;
   const rect=canvas.getBoundingClientRect(),w=rect.width,h=rect.height;if(!w||!h)return;
   const dpr=Math.min(devicePixelRatio||1,2);canvas.width=Math.round(w*dpr);canvas.height=Math.round(h*dpr);ctx.setTransform(dpr,0,0,dpr,0,0);
   ctx.fillStyle='#f6f9f7';ctx.fillRect(0,0,w,h);
   const scale=Math.min(w*.37,h*.43/g.extent)*zoom;
   const project=p=>{const factor=5/(5-p[2]);return[w/2+p[0]*scale*factor,h/2-p[1]*scale*factor]};
   const faces=g.faces.map(f=>{const v=f.v.map(transform);return{...f,v,n:transform(f.n),z:(v[0][2]+v[1][2]+v[2][2])/3}}).sort((a,b)=>a.z-b.z);
   for(const f of faces){const shade=.74+.26*Math.max(0,f.n[0]*-.24+f.n[1]*.43+f.n[2]*.77);ctx.fillStyle='rgb('+f.color.map(x=>Math.round(x*shade)).join(',')+')';ctx.beginPath();f.v.forEach((v,i)=>{const p=project(v);i?ctx.lineTo(...p):ctx.moveTo(...p)});ctx.closePath();ctx.fill()}
   for(const l of g.lines){ctx.strokeStyle=l.color;ctx.lineWidth=l.width;ctx.beginPath();l.v.forEach((v,i)=>{const p=project(transform(v));i?ctx.lineTo(...p):ctx.moveTo(...p)});ctx.stroke()}
   markers=MODELS[id].points.map((p,i)=>{const tp=transform(p.p),xy=project(tp);return{xy,i,z:tp[2]}}).sort((a,b)=>a.z-b.z);
   const groups=[];for(const m of markers){const same=groups.find(x=>Math.hypot(x.xy[0]-m.xy[0],x.xy[1]-m.xy[1])<1);if(same)same.indices.push(m.i);else groups.push({...m,indices:[m.i]})}const placed=[];for(const m of groups){const anchor=[...m.xy];const candidates=[[0,0],[30,0],[-30,0],[0,30],[0,-30],[48,0],[-48,0]];for(const [dx,dy] of candidates){const proposed=[anchor[0]+dx,anchor[1]+dy];if(proposed[0]>16&&proposed[0]<w-16&&proposed[1]>30&&proposed[1]<h-16&&placed.every(p=>Math.hypot(p[0]-proposed[0],p[1]-proposed[1])>=29)){m.xy=proposed;break}}placed.push(m.xy);if(Math.hypot(m.xy[0]-anchor[0],m.xy[1]-anchor[1])>1){ctx.strokeStyle='#60786a';ctx.lineWidth=1.3;ctx.beginPath();ctx.moveTo(...anchor);ctx.lineTo(...m.xy);ctx.stroke();ctx.beginPath();ctx.arc(...anchor,2.5,0,Math.PI*2);ctx.fillStyle='#173b32';ctx.fill()}for(const marker of markers){if(m.indices.includes(marker.i))marker.xy=m.xy}const selected=m.indices.includes(active);ctx.beginPath();ctx.arc(...m.xy,selected?14:11,0,Math.PI*2);ctx.fillStyle=selected?'#27654a':'#fff';ctx.fill();ctx.lineWidth=selected?3:2;ctx.strokeStyle=selected?'#173b32':'#60786a';ctx.stroke();ctx.fillStyle=selected?'#fff':'#173b32';ctx.font='bold 12px Tahoma,sans-serif';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(m.indices.map(i=>i+1).join('/'),m.xy[0],m.xy[1])}
   ctx.fillStyle='#50665e';ctx.textAlign='left';ctx.font='12px Tahoma,sans-serif';ctx.fillText(id==='heart'?'Cavités et connexions stylisées':'Repères de surface simplifiés',12,18);
   canvas.dataset.csYaw=yaw.toFixed(3);canvas.dataset.csPitch=pitch.toFixed(3);canvas.dataset.csZoom=zoom.toFixed(2);
  }
  const schedule=()=>{if(!frame&&!destroyed)frame=requestAnimationFrame(draw)};
  const rotate=(dy,dp)=>{yaw+=dy;pitch=Math.max(-.75,Math.min(.75,pitch+dp));schedule()};
  const setView=view=>{yaw=view==='back'?Math.PI:view==='side'?-Math.PI/2:0;pitch=0;schedule()};
  const reset=()=>{yaw=0;pitch=0;zoom=1;schedule()};
  const down=e=>{drag={x:e.clientX,y:e.clientY,startX:e.clientX,startY:e.clientY,moved:false};canvas.setPointerCapture(e.pointerId);canvas.focus({preventScroll:true})};
  const move=e=>{if(!drag)return;const dx=e.clientX-drag.x,dy=e.clientY-drag.y;if(Math.hypot(e.clientX-drag.startX,e.clientY-drag.startY)>5)drag.moved=true;rotate(dx*.010,dy*.009);drag.x=e.clientX;drag.y=e.clientY};
  const up=e=>{if(drag&&!drag.moved){const rect=canvas.getBoundingClientRect(),x=e.clientX-rect.left,y=e.clientY-rect.top;const hit=markers.map(m=>({...m,d:Math.hypot(m.xy[0]-x,m.xy[1]-y)})).sort((a,b)=>a.d-b.d)[0];if(hit?.d<24)selectPoint(hit.i,false)}drag=null;if(canvas.hasPointerCapture(e.pointerId))canvas.releasePointerCapture(e.pointerId)};
  const cancel=()=>{drag=null};
  const key=e=>{const moves={ArrowLeft:[-.16,0],ArrowRight:[.16,0],ArrowUp:[0,-.12],ArrowDown:[0,.12]};if(moves[e.key]){e.preventDefault();rotate(...moves[e.key])}else if(e.key==='Home'){e.preventDefault();reset()}};
  canvas.addEventListener('pointerdown',down);canvas.addEventListener('pointermove',move);canvas.addEventListener('pointerup',up);canvas.addEventListener('pointercancel',cancel);canvas.addEventListener('keydown',key);
  const observer=new ResizeObserver(schedule);observer.observe(canvas);schedule();
  return{rotate,setView,reset,zoom:value=>{zoom=value;schedule()},select:(i,view)=>{active=i;if(view)setView(view);else schedule()},destroy:()=>{destroyed=true;cancelAnimationFrame(frame);observer.disconnect();canvas.removeEventListener('pointerdown',down);canvas.removeEventListener('pointermove',move);canvas.removeEventListener('pointerup',up);canvas.removeEventListener('pointercancel',cancel);canvas.removeEventListener('keydown',key)}};
 }
 function selectPoint(index,changeView=true,reveal=false){
  const p=MODELS[current].points[index];if(!p)return;
  dialog.querySelectorAll('[data-cs-select]').forEach((b,i)=>b.setAttribute('aria-pressed',String(i===index)));
  const detail=dialog.querySelector('.cs-point-detail');detail.innerHTML='<h3>'+esc(p.label)+'</h3>'+p.description;
  detail.dataset.csSelected=p.id;
  scene?.select(index,changeView?p.view:null);
  if(reveal&&matchMedia('(max-width:760px)').matches)detail.scrollIntoView({block:'nearest',behavior:'instant'});
 }
 function ensureDialog(){
  if(dialog)return;
  dialog=document.createElement('dialog');dialog.id='medina-cs-dialog';dialog.className='cs-dialog';dialog.setAttribute('aria-labelledby','cs-dialog-title');
  document.body.append(dialog);
  dialog.addEventListener('keydown',e=>{if(e.key!=='Tab')return;const items=Array.from(dialog.querySelectorAll('button,input,[tabindex]')).filter(x=>!x.disabled&&x.tabIndex>=0&&x.getClientRects().length);const first=items[0],last=items.at(-1);if(e.shiftKey&&document.activeElement===first){e.preventDefault();last?.focus()}else if(!e.shiftKey&&document.activeElement===last){e.preventDefault();first?.focus()}});
  dialog.addEventListener('close',()=>{scene?.destroy();scene=null;current=null;if(opener?.isConnected)opener.focus({preventScroll:true})});
  dialog.addEventListener('click',e=>{if(e.target===dialog){const r=dialog.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)dialog.close()}});
 }
 function open(id,trigger,initialPoint){
  const model=MODELS[id];if(!model)return;
  ensureDialog();scene?.destroy();opener=trigger;current=id;
  dialog.innerHTML='<header class="cs-dialog-header"><h2 id="cs-dialog-title">'+esc(model.title)+'</h2><button type="button" class="cs-dialog-close">Fermer ×</button></header><div class="cs-dialog-body"><div><figure class="cs-scene"><canvas class="cs-canvas" width="760" height="650" tabindex="0" role="img" aria-label="Modèle 3D : '+esc(model.title)+'. Les flèches font tourner le modèle ; la touche Début réinitialise la vue.">Les repères et leurs explications sont disponibles dans les boutons à côté du modèle.</canvas><figcaption>'+esc(model.caption)+'</figcaption></figure><div class="cs-rotate-controls" role="group" aria-label="Orientation du modèle"><button type="button" data-cs-rotate="left">← Tourner</button><button type="button" data-cs-rotate="right">Tourner →</button><button type="button" data-cs-view="front">Face</button><button type="button" data-cs-view="side">Profil</button><button type="button" data-cs-view="back">Dos</button><button type="button" data-cs-reset>Réinitialiser</button></div><label class="cs-zoom">Zoom <input type="range" min="75" max="140" value="100" aria-label="Zoom du modèle 3D"></label><p class="cs-orientation">Vous faites glisser le modèle avec la souris ou un doigt. Au clavier, vous utilisez les flèches lorsque le modèle a le focus. Les boutons numérotés donnent les mêmes explications.</p><p class="cs-canvas-fallback" hidden>Le dessin 3D n’est pas disponible ici. Tous les repères et les techniques restent accessibles avec les boutons numérotés.</p></div><div><div class="cs-points" role="group" aria-label="Repères anatomiques">'+model.points.map((p,i)=>'<button type="button" data-cs-select="'+i+'" aria-pressed="false">'+(i+1)+' · '+esc(p.label)+'</button>').join('')+'</div><section class="cs-point-detail" aria-live="polite" aria-atomic="true"></section></div></div>';
  dialog.querySelector('.cs-dialog-close').onclick=()=>dialog.close();
  dialog.querySelectorAll('[data-cs-select]').forEach(b=>b.onclick=()=>selectPoint(Number(b.dataset.csSelect),true,true));
  dialog.querySelectorAll('[data-cs-rotate]').forEach(b=>b.onclick=()=>scene?.rotate(b.dataset.csRotate==='left'?-.25:.25,0));
  dialog.querySelectorAll('[data-cs-view]').forEach(b=>b.onclick=()=>scene?.setView(b.dataset.csView));
  dialog.querySelector('[data-cs-reset]').onclick=()=>{scene?.reset();dialog.querySelector('input[type="range"]').value='100'};
  dialog.querySelector('input[type="range"]').oninput=e=>scene?.zoom(Number(e.target.value)/100);
  if(!dialog.open)dialog.showModal();
  scene=makeScene(dialog.querySelector('canvas'),id);dialog.querySelector('.cs-canvas-fallback').hidden=!!scene;
  const index=model.points.findIndex(p=>p.id===initialPoint);selectPoint(index>=0?index:0);
  dialog.querySelector('.cs-dialog-close').focus({preventScroll:true});
 }
 function destroy(){if(dialog?.open)dialog.close();scene?.destroy();scene=null;pageCleanup?.();pageCleanup=null}
 function mount(root){
  const page=root.querySelector('.cs-page');if(!page)return;
  let checks={};try{checks=JSON.parse(localStorage.getItem(storageKey)||'{}')||{}}catch{checks={}}
  const boxes=Array.from(page.querySelectorAll('[data-cs-check]'));
  const update=()=>{page.querySelector('.cs-progress').textContent=boxes.filter(b=>b.checked).length+' / '+boxes.length+' étapes cochées';try{localStorage.setItem(storageKey,JSON.stringify(Object.fromEntries(boxes.map(b=>[b.dataset.csCheck,b.checked]))))}catch{}};
  boxes.forEach(b=>{b.checked=checks[b.dataset.csCheck]===true});update();
  const click=e=>{
   const model=e.target.closest('[data-cs-model]');if(model){open(model.dataset.csModel,model,model.dataset.csPoint);return}
   const jump=e.target.closest('[data-cs-jump]');if(jump){e.preventDefault();const target=page.querySelector('#'+jump.dataset.csJump);target?.scrollIntoView({block:'start',behavior:'instant'});const heading=target?.querySelector('h2');heading?.setAttribute('tabindex','-1');heading?.focus({preventScroll:true});return}
   const answer=e.target.closest('[data-cs-choice]');if(answer){const quiz=answer.closest('.cs-quiz');quiz.querySelectorAll('[data-cs-choice]').forEach(b=>{b.removeAttribute('data-result');b.setAttribute('aria-pressed',String(b===answer))});const correct=answer.dataset.csChoice===quiz.dataset.csAnswer;answer.dataset.result=correct?'correct':'incorrect';quiz.querySelector('[data-cs-choice="'+quiz.dataset.csAnswer+'"]').dataset.result='correct';const feedback=quiz.querySelector('.cs-feedback');feedback.hidden=false;feedback.setAttribute('role','status');feedback.setAttribute('aria-live','polite');feedback.dataset.csResult=correct?'correct':'incorrect';return}
   if(e.target.closest('.cs-reset-checklist')){boxes.forEach(b=>b.checked=false);update()}
  };
  const change=e=>{if(e.target.matches('[data-cs-check]'))update()};
  page.addEventListener('click',click);page.addEventListener('change',change);pageCleanup=()=>{page.removeEventListener('click',click);page.removeEventListener('change',change)};
 }
 window.MEDINA_CS={page:()=>document.getElementById('medina-cs-page')?.innerHTML||'',mount,destroy};
})();
