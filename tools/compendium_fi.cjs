#!/usr/bin/env node
// Lecture de l'information professionnelle suisse (Compendium) par rendu Chromium.
// Usage : node tools/compendium_fi.cjs "<nom du produit ou URL compendium.ch/.../mpro>" [section…]
// Sortie : JSON { url, produit, date_consultation, sections: {titre: texte} } sur la sortie standard.
// Aucune donnée personnelle n'est transmise ; seule la requête de recherche est envoyée.
const {chromium}=require('playwright');
const SECTIONS=['Composition','Forme pharmaceutique et quantité de principe actif par unité','Indications/Possibilités d’emploi','Posologie/Mode d’emploi','Contre-indications','Mises en garde et précautions','Interactions','Grossesse, allaitement','Grossesse/Allaitement','Effets indésirables','Surdosage','Propriétés/Effets','Pharmacocinétique','Remarques particulières','Numéro d’autorisation','Mise à jour de l’information'];
(async()=>{
  const arg=process.argv[2]; const want=process.argv.slice(3);
  if(!arg){console.error('usage: compendium_fi.cjs <produit|url> [section…]');process.exit(2);}
  const b=await chromium.launch({executablePath:process.env.MEDINA_CHROMIUM_PATH||'/opt/pw-browsers/chromium'});
  const p=await b.newPage();
  let url=arg;
  if(!/^https?:/.test(arg)){
    await p.goto('https://compendium.ch/fr/search?q='+encodeURIComponent(arg),{waitUntil:'networkidle',timeout:60000});
    await p.waitForTimeout(3000);
    const href=await p.evaluate(()=>{const a=[...document.querySelectorAll("a")].find(a=>/\/product\/\d+-/.test(a.href));return a?a.href:null;});
    if(!href){console.error('aucun produit trouvé');await b.close();process.exit(3);}
    url=href.replace(/\/(mpro|pro|pat)\/?$/,"").replace(/\/$/,'')+'/mpro';
  }
  await p.goto(url,{waitUntil:'networkidle',timeout:60000}); await p.waitForTimeout(3000);
  const t=await p.evaluate(()=>document.body.innerText);
  const titre=(await p.title())||'';
  const idx=SECTIONS.map(s=>[s,t.lastIndexOf('\n'+s+'\n')]).filter(x=>x[1]>=0).sort((a,b)=>a[1]-b[1]);
  const sections={};
  idx.forEach(([s,i],k)=>{const end=k+1<idx.length?idx[k+1][1]:Math.min(t.length,i+20000);sections[s]=t.slice(i+s.length+2,end).trim();});
  const out={url,produit:titre,date_consultation:new Date().toISOString().slice(0,10),sections:want.length?Object.fromEntries(Object.entries(sections).filter(([k])=>want.some(w=>k.toLowerCase().includes(w.toLowerCase())))):sections};
  console.log(JSON.stringify(out,null,1)); await b.close();
})().catch(e=>{console.error(e.message);process.exit(1);});
