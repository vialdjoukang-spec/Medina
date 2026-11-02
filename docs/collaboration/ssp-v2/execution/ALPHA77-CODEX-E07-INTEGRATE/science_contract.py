from pathlib import Path
import re
p=Path('chapters/E07/E07_c.html');s=p.read_text()
links={
'semio':('Un même chiffre total peut résulter d’une anomalie de transport ou d’une maladie générale ; la plainte et la chronologie changent sa signification.','Confronter FT4, TSH et méthode ; examiner d’abord les voies aériennes devant une tuméfaction rapide.','L’hypothyroïdie congénitale confirmée se traite sans attendre le gène ; T3 basse isolée en réanimation ne suffit pas à substituer.','Décrire le signe, comprendre son mécanisme et tester l’hypothèse avant de traiter le chiffre.'),
'anat':('L’effet de masse cervical peut menacer la respiration indépendamment de la fonction hormonale.','L’observation respiratoire précède la palpation ; imagerie et audiologie répondent ensuite à une question anatomique précise.','Une obstruction demande une prise en charge urgente des voies aériennes ; une substitution ne remplace pas ce geste.','Une image de goitre compressif adulte ne démontre ni la cause ni un syndrome néonatal.'),
'histo':('Cellules folliculaires et cellules C assurent des fonctions différentes ; un résultat sanguin ne remplace pas l’architecture tissulaire.','Confronter cytologie, histologie, immunohistochimie et histoire de ponction ; rechercher les zones viables après nécrose.','L’infarctus d’un nodule n’autorise pas à déclarer une guérison oncologique ; la décision conserve l’information cytologique initiale.','La figure normale situe follicule et colloïde, sans représenter une hyperplasie C.'),
'physio':('Une réserve liée abaissée peut réduire la T4 totale sans insuffisance hormonale ; la maladie critique ajoute des variations tissulaires.','Total, libre et TSH répondent à des questions distinctes ; les normes dépendent de l’âge et la méthode.','Traiter la synthèse insuffisante démontrée ; ne pas corriger mécaniquement la réserve liée ou un profil NTIS.','Le résultat sérique ne mesure pas directement l’action hormonale de chaque organe.'),
'bioch':('Une interférence peut produire une discordance sans modifier la sécrétion réelle ; précurseurs et hormone mature ne sont pas interchangeables.','Discuter dilution, méthode alternative ou recherche d’interférence avec le laboratoire selon la plateforme.','Le test au calcium est une procédure spécialisée hors indication du produit décrit, pas un traitement de l’hypercalcitoninémie.','Un seuil de série doit garder son immunodosage, sa population et ses limites.'),
'gene':('Le même gène peut donner des phénotypes variables ; le risque dépend du variant et de la transmission.','Phénotype et fiabilité du dosage orientent les tests ; un variant incertain ne prouve pas une maladie.','La génétique guide conseil et surveillance mais ne retarde pas la substitution d’une hypothyroïdie congénitale confirmée.','25 % est le risque du modèle récessif décrit ; il ne s’applique pas à tout goitre familial.')}
for code,vals in links.items():
 anchor=f'<section class="ilot" id="e07-s-{code}-cours">';start=s.index(anchor);end=s.index('</section>',start)
 add=''.join(f'<p class="key"><b>{label}</b> {val}</p>' for label,val in zip(['Science → clinique.','Science → examen.','Science → traitement.','À retenir.'],vals))
 if code in ['semio','physio']:
  texts=['Signe ou résultat inattendu','Contexte + méthode + examen','Hypothèse clinique confrontée','Décision et suivi individualisés'] if code=='semio' else ['Synthèse glandulaire','Transport lié et fraction libre','Entrée et métabolisme tissulaires','Action hormonale selon le tissu']
  svg='<figure><svg role="img" aria-label="'+('Démarche sémiologique' if code=='semio' else 'Niveaux fonctionnels hormonaux')+' : schéma logique non anatomique" viewBox="0 0 460 335" style="width:100%;max-width:600px;height:auto;display:block;margin:auto">'
  for i,t in enumerate(texts):
   y=8+i*80;svg+=f'<rect x="10" y="{y}" width="440" height="54" rx="8" fill="#eef3fa" stroke="#254568"/><text x="230" y="{y+33}" text-anchor="middle" font-size="18" fill="#153653">{t}</text>'
   if i<3:svg+=f'<text x="230" y="{y+76}" text-anchor="middle" font-size="22" fill="#153653">↓</text>'
  svg+='</svg><figcaption>Schéma logique, non anatomique. '+('Les étapes représentent une démarche d’interprétation, pas un score validé. Sources [S3, S5, S16, S32, S33].' if code=='semio' else 'Ces niveaux participent à la fonction ; leur état ne se déduit pas d’un seul dosage sérique. Sources [S3, S16, S17, S36].')+'</figcaption></figure>'
  add=svg+add
 s=s[:end]+add+s[end:]
p.write_text(s)
p=Path('docs/collaboration/ssp-v2/execution/ALPHA77-CODEX-E07-INTEGRATE/browser_check.py');s=p.read_text().replace("'thyroperoxydase' in txt.lower()", "'peroxydase thyroïdienne' in txt.lower()");p.write_text(s)
