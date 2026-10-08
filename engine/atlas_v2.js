/* MEDINA — couleur vive par catégorie (contraste du blanc ≥ 4,5:1 vérifié pour chaque teinte). */
(() => {
 'use strict';
 const P=['#C2185B','#1565C0','#2E7D32','#BF360C','#6A1B9A','#00796B','#C62828','#283593','#8E5A00','#AD1457','#0277BD','#1B5E20','#7B1FA2','#9E2A2B','#00695C','#5D4037','#4527A0','#00777F','#B23C0E','#37602B'];
 const colour=i=>i<P.length?P[i]:`hsl(${Math.round((i*137.508)%360)} 72% 27%)`;
 function paint(){
  const O=window.MEDINA_CATEGORY_ORGANISATION;if(!O)return;
  const rank=new Map(O.blocks.map((b,i)=>[b.code,i]));
  document.querySelectorAll('[data-mcg-category],[data-mcg-block],[data-mcg-sidebar-category]').forEach(el=>{
   const code=el.dataset.mcgCategory||el.dataset.mcgBlock||el.dataset.mcgSidebarCategory;
   if(rank.has(code))el.style.setProperty('--cat',colour(rank.get(code)));
  });
  const lesson=document.querySelector('.mcg-planned-panel'),item=lesson&&document.querySelector('[data-mcg-block]');
  if(lesson&&item)lesson.style.setProperty('--cat',item.style.getPropertyValue('--cat'));
 }
 // Conserver le repère du moteur de thèmes ; la surface Atlas impose le clair.
 new MutationObserver(paint).observe(document.body,{childList:true,subtree:true});
 paint();
})();
