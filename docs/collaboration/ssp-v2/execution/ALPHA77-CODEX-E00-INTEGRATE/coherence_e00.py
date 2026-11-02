from pathlib import Path
import re,json,html,hashlib
P=Path('chapters/E00');D=Path('docs/collaboration/ssp-v2/execution/ALPHA77-CODEX-E00-INTEGRATE');sources=json.loads((D/'recherche_E00/sources.json').read_text())
def ref(*ids):return '<span class="src">'+', '.join('<button class="w" data-k="e00-sources-2026">['+i+']</button>' for i in ids)+'</span>'
replacements={
 'l’imagerie de la thyroïde (échographie ou scintigraphie) est réalisée après le début du traitement, jamais avant.':'l’imagerie de la thyroïde (échographie ou scintigraphie) est organisée sans retarder le début du traitement.',
 'L’imagerie de la thyroïde (échographie ou scintigraphie) est réalisée après le début du traitement, jamais avant.':'L’imagerie de la thyroïde (échographie ou scintigraphie) est organisée sans retarder le début du traitement.',
 'réaliser une scintigraphie avant d’avoir commencé le traitement':'retarder la substitution pour réaliser une scintigraphie',
 'Réaliser une scintigraphie avant d’avoir commencé le traitement':'Retarder la substitution pour réaliser une scintigraphie',
 'récurrence familiale d’environ 25 %':'récurrence de 25 % pour une transmission autosomique récessive confirmée',
 'la récurrence familiale est d’environ 25 %':'une récurrence de 25 % concerne les formes autosomiques récessives confirmées',
 'la partie Swisspeddose de l’information professionnelle reprend':'l’annexe harmonisée SwissPedDose affichée séparément dans AmiKo propose',
 'Pour la tranche 0-6 mois, le consensus européen donne une dose initiale':'Pour le début du traitement néonatal, le consensus européen donne une dose initiale',
 'TSH supérieure à 20 mU/l même avec une fT4 normale, traitement':'TSH sérique supérieure à 20 mU/l lors de la confirmation vers la deuxième semaine, même avec une fT4 normale, traitement (avis expert)',
 'une TSH supérieure à 20 mU/l impose le traitement même avec une fT4 normale':'une TSH sérique supérieure à 20 mU/l lors de la confirmation vers la deuxième semaine conduit au traitement même si la fT4 est normale (seuil d’avis expert)',
 '<td>TSH supérieure à 20 mU/l, fT4 normale</td>':'<td>TSH sérique supérieure à 20 mU/l à la confirmation vers la deuxième semaine, même si fT4 normale ; seuil d’avis expert</td>',
 '<td>TSH de 6 à 20 mU/l après le 21e jour, fT4 normale</td>':'<td>TSH de 6 à 20 mU/l après le 21e jour, enfant sain, fT4 normale pour l’âge ; bénéfice thérapeutique incertain</td>',
 '<td>Sans laboratoire : TSH sur buvard supérieure à 40 mU/l</td>':'<td>Si confirmation sérique impossible : TSH sur buvard supérieure à 40 mU/l ; recommandation européenne de contexte, pas seuil de rappel suisse</td>',
 'fT4 basse avec TSH élevée, ou TSH supérieure à 20 mU/l.':'fT4 basse pour l’âge avec TSH nettement élevée, ou TSH sérique supérieure à 20 mU/l à la confirmation vers la deuxième semaine (avis expert).',
 'Seuils : TSH supérieure à 20 mU/l, ou fT4 basse avec TSH élevée, traiter.':'Seuils néonatals : traiter si fT4 basse avec TSH nettement élevée ; le seuil sérique de TSH supérieure à 20 mU/l à la confirmation vers la deuxième semaine est un avis expert.',
 '1 à 2 semaines, puis toutes les 2 semaines jusqu’à normalisation':'1 à 2 semaines (au plus tard une semaine si dose initiale proche de 15 µg/kg/jour), puis toutes les 2 semaines jusqu’à normalisation de la TSH',
 'un premier contrôle à 1-2 semaines, puis toutes les 2 semaines jusqu’à normalisation':'un premier contrôle à 1–2 semaines (au plus tard une semaine si dose initiale proche de 15 µg/kg/jour), puis toutes les 2 semaines jusqu’à normalisation de la TSH',
 'au-delà de 300 µg/l chez l’enfant d’âge scolaire et de 500 µg/l pendant la grossesse (iodurie médiane)':'à partir de 300 µg/l chez l’enfant d’âge scolaire et de 500 µg/l pendant la grossesse pour la médiane d’iodurie d’une population ; ce ne sont pas des doses de médicament',
 'L’iode se prescrit pour éviter la carence, pas pour traiter un enfant atteint.':'Corriger l’apport iodé insuffisant reste nécessaire, y compris chez une personne atteinte ; cela ne remplace pas la substitution d’une hypothyroïdie persistante et ne promet pas de réparer une lésion ancienne.',
 'Choisir une multivitamine prénatale contenant de l’iode.':'Discuter le complément avec le gynécologue ; si un multinutriment est pris, vérifier sa teneur en iode.',
 'iode avant la grossesse, 250 µg/jour pendant la grossesse selon le consensus européen':'apport iodé suffisant avant la grossesse, objectif nutritionnel total de 250 µg/jour pendant la grossesse selon le consensus européen',
 'Les autres interactions de la lévothyroxine figurant dans l’information professionnelle n’ont pas été lues en totalité':'Les interactions de la lévothyroxine figurant dans l’information professionnelle ont été relues',
 'Deux cofacteurs ont été proposés pour expliquer pourquoi certains enfants développent le tableau myxœdémateux':'Deux pistes historiques sont évoquées pour le tableau myxœdémateux',
 'Ces hypothèses sont présentées comme telles, car les revues de fond n’ont été lues qu’au niveau du résumé.':'Le thiocyanate est une hypothèse spéculative explicitement décrite dans le résumé de Laurberg. Pour le sélénium, le titre de Dumont évoque ce rôle, mais aucun résumé ni texte intégral n’a été obtenu : ce titre ne permet pas de décrire un mécanisme ni de proposer une intervention.',
 '<td>Hypothèse, résumé seul</td>':'<td>Titre de publication seulement ; mécanisme et bénéfice non vérifiés</td>',
 'Sélénium et thiocyanate : hypothèses seulement.':'Thiocyanate : hypothèse spéculative ; rôle du sélénium non vérifié au-delà d’un titre.',
 'Thiocyanate et sélénium : hypothèses.':'Thiocyanate : hypothèse spéculative ; sélénium : titre seul, aucune conduite clinique.',
 'La première invoque la carence en <button class="w" data-k="e00-cofacteurs">sélénium et les goitrogènes (état des connaissances)</button>.':'La première évoque <button class="w" data-k="e00-cofacteurs">sélénium et goitrogènes</button> dans le titre d’un article de1994 ; son contenu n’a pas été obtenu, et aucun mécanisme précis n’en est déduit.',
 'ses auteurs la qualifient de spéculative.':'l’extrapolation au lait humain et au syndrome myxœdémateux est explicitement spéculative dans ce résumé.',
 'état au 14.10.2026':'reprise documentaire au 02.11.2026',
 'revue par intelligence artificielle, validation médicale humaine en attente':'reprise par intelligence artificielle ; revue indépendante et validation médicale humaine en attente',
 'Références lues le 14 octobre 2026':'Références héritées du dossier du 14 octobre 2026',
}
for p in P.glob('*.html'):
 s=p.read_text()
 for a,b in replacements.items():s=s.replace(a,b)
 p.write_text(s)
# Add adult doses read from the exact product, separated from neonatal urgency.
p=P/'E00_d.html';s=p.read_text();anchor='<p>Chez le nourrisson, la FI demande'
adult='''<p><b>Adulte et adolescent dès 12 ans : hypothyroïdie persistante.</b> Pour cette indication, la FI donne une dose initiale de25–50 µg/jour, avec augmentations de25–50 µg à intervalles de2–4 semaines, puis une dose d’entretien usuelle de100–200 µg/jour. Cette plage d’entretien n’est pas un maximum universel ni une dose à appliquer à tout patient. Chez la personne âgée, ou en cas d’hypothyroïdie ancienne ou sévère ou de comorbidités, la FI décrit un début plus faible à25 µg, une augmentation prudente avec intervalles plus longs et des contrôles fréquents. Les contre-indications cardiaques restent à vérifier : cette titration ne les annule pas.</p><p>Ces modalités adultes ne remplacent pas la conduite néonatale urgente exposée plus haut. La FI indique que le traitement substitutif est le plus souvent à vie, tandis que le consensus recommande une réévaluation spécialisée quand le caractère permanent de l’hypothyroïdie congénitale n’a pas été établi.</p>'''+ref('S101','S102')
assert anchor in s;s=s.replace(anchor,adult+anchor)
s=s.replace('La lévothyroxine est le seul médicament dont la posologie néonatale figure dans l’information professionnelle suisse consultée','La lévothyroxine est le médicament substitutif étudié ici dans sa FI suisse exacte et dans l’annexe néonatale SwissPedDose distincte')
s=s.replace('Les comprimés sécables suisses contiennent25,50,75,100,125,150,175 ou200 µg','Les comprimés sécables suisses contiennent 25, 50, 75, 100, 125, 150, 175 ou 200 µg')
s=s.replace('AntivitaminesK','Antivitamines K').replace('conversionT4–T3','conversion T4–T3')
p.write_text(s)
# Monitoring central hypothyroidism is driven by fT4, not normalization of an uninformative TSH.
p=P/'E00_c.html';s=p.read_text();needle='<section class="ilot" id="e00-e-normes">';start=s.index(needle);end=s.index('</section>',start)
s=s[:end]+'''<p><b>Forme centrale : objectif de suivi différent.</b> Après sécurisation de l’axe surrénalien, le consensus suit principalement la fT4, maintenue au-dessus de la moyenne ou médiane de l’intervalle adapté à l’âge. Si la TSH était basse avant traitement, son dosage répété peut être omis dans ce cadre spécialisé. La normalisation de la TSH utilisée dans l’hypothyroïdie primaire n’est donc pas une cible transposable automatiquement. Une fT4 proche de la borne basse fait rechercher un sous-traitement ; une fT4 élevée s’interprète avec l’horaire de prise et les signes cliniques.</p>'''+ref('S102')+s[end:];p.write_text(s)
# Source provenance for inherited statements actually reread today: nine abstracts, one title-only record.
j=json.loads((D/'recherche_E00/downloads/inherited-abstracts.json').read_text());read=[]
for a in j['resultList']['result']:
 read.append({'pmid':a['id'],'title':a['title'],'url':'https://pubmed.ncbi.nlm.nih.gov/'+a['id']+'/','read_level':'abstract' if a.get('abstractText') else 'title_and_metadata_only','actual_abstract_excerpt':re.sub('<[^>]+>',' ',a.get('abstractText',''))[:1100],'read_at':'2026-11-02','limits':'Le titre seul ne soutient pas une description de mécanisme ni une prescription.' if not a.get('abstractText') else 'Résumé seul ; ni détails du texte intégral ni extrapolation normative suisse inventés.'})
(D/'recherche_E00/inherited-recheck.json').write_text(json.dumps({'batch_sha256':hashlib.sha256((D/'recherche_E00/downloads/inherited-abstracts.json').read_bytes()).hexdigest(),'records':read},ensure_ascii=False,indent=2)+'\n')
# Rebuild source popup from current ledger, then mention abstract-only recheck.
p=P/'E00_pop2.html';s=p.read_text();body='<p>Lectures ciblées du2novembre2026, distinctes du dossier historique. La reprise reste soumise à revue indépendante et ne constitue pas une validation médicale humaine.</p><ul>'+''.join('<li><b>['+a['id']+']</b> <a href="'+html.escape(a['url'],quote=True)+'" target="_blank" rel="noopener">'+html.escape(a['titre'])+'</a> — '+html.escape(a['version_annee'])+'. '+html.escape(a['section_page'])+'. <b>Portée :</b> '+html.escape(a['population'])+'. <b>Limites :</b> '+html.escape(a['limites'])+'</li>' for a in sources['sources'])+'</ul><p>Les résumés hérités sur l’histoire suisse, la surveillance de2005, l’allaitement, le thiocyanate, les effets de la correction populationnelle et l’essai de supplémentation de2017 ont été relus séparément. Pour Dumont1994 sur le sélénium, seul le titre est disponible : aucune description détaillée ni intervention n’en est déduite.</p>'
s,n=re.subn(r'(<template data-pop="e00-sources-2026"[^>]*>).*?</template>',lambda m:m.group(1)+body+'</template>',s,flags=re.S);assert n==1
# Preserve uncertainty and denominators of the iodine trial.
s=s.replace('environ 313 enfants','313 enfants évalués pour le QI (315 pour les fonctions exécutives), après inclusion initiale de832femmes')
p.write_text(s)
p=P/'E00_b.html';s=p.read_text().replace('dans un essai randomisé d’environ 313 enfants','dans un essai ayant inclus832femmes, dont313enfants ont été évalués pour le quotient intellectuel et315pour les fonctions exécutives ; cette attrition limite l’interprétation');p.write_text(s)
# Typographic repair restricted to text nodes; never attributes/code/URLs/gene names.
for p in P.glob('*.html'):
 parts=re.split(r'(<[^>]*>)',p.read_text())
 for i in range(0,len(parts),2):
  v=parts[i]
  v=re.sub(r'\b([A-Za-zÀ-ÖØ-öø-ÿ]{2,})(\d+)\b',lambda m:m.group(0) if m.group(1) in {'fT','SLC','TBG'} else m.group(1)+' '+m.group(2),v)
  v=re.sub(r'(?<=\d)(?=(?:enfants|femmes|patients|sujets|scanners|pour|Java|µg|mg|kg|pmol|mUI|mU|semaines?|jours?|mois|ans|heures?|novembre|juin|février|%|°C))',' ',v)
  v=re.sub(r'\b(à|À|de|en)(?=\d|µg)',r'\1 ',v)
  parts[i]=v
 p.write_text(''.join(parts))
print('Cohérence FI, seuils, suivi central, sources héritées et typographie corrigées.')
