from pathlib import Path
import re,json,datetime
R=Path.cwd();P=R/'chapters/E07';changes=[]
replacements={
'une thyréostimuline supérieure à 20 mU/l justifie le traitement même si la thyroxine libre est normale':'une thyréostimuline supérieure à 20 mU/l à la confirmation, vers la deuxième semaine de vie, justifie le traitement même si la thyroxine libre est normale (seuil d’avis expert du consensus)',
'd’où des glucocorticoïdes à dose de stress':'à rechercher et prendre en charge selon le protocole hospitalier avant la substitution',
'<b>Critères formels.</b>':'<b>Arguments diagnostiques et limites.</b>',
'calcitonine stimulée au calcium au-dessus de 79 pg/ml (femme) et 466 pg/ml (homme)':'seuils stimulés de 79 pg/ml (femme) et 466 pg/ml (homme) issus d’une étude avec Immulite 2000, non universels',
'hypothyroïdie congénitale primaire (thyroxine libre basse, thyréostimuline élevée) avec glande en place ou goitre ; test au perchlorate positif au-delà de 10 % de décharge ; thyroglobuline orientant le gène ; confirmation génétique':'profil typique d’hypothyroïdie primaire avec glande en place ou goitre ; perchlorate et thyroglobuline orientent le mécanisme, puis la génétique peut confirmer. Le perchlorate peut rester négatif, notamment pour IYD ; aucun test génétique ne doit retarder le traitement indiqué',
'surdité neurosensorielle, aqueduc vestibulaire élargi, goitre avec ou sans défaut d’organification ; variants biallèliques de SLC26A4':'surdité neurosensorielle et variants biallèliques pathogènes de SLC26A4 ; anomalies vestibulaires et atteinte thyroïdienne variables, parfois tardives ; distinguer Pendred et surdité SLC26A4 sans atteinte thyroïdienne',
'maladie aiguë ou critique, sans maladie thyroïdienne intrinsèque':'maladie aiguë ou critique compatible, avec recherche d’une maladie thyroïdienne coexistante et des effets médicamenteux',
'Procalcitonine normale inférieure à 0,05 ng/ml ; au-delà de 0,1 à 0,2 ng/ml, un cancer médullaire est évoqué hors infection.':'Procalcitonine : référence et seuil dépendants de l’essai ; les seuils de 0,1–0,2 ng/ml étudiés pour le cancer médullaire ne sont pas diagnostiques à eux seuls.',
'dans une série de 104 cancers médullaires sporadiques opérés à Pise, elle n’était diagnostique que dans 45,9 % des cas':'dans une série de 104 cancers médullaires sporadiques opérés à Pise, elle n’était diagnostique que chez 45,9 % des 85 patients ponctionnés',
'Dans une série de 104 cancers médullaires sporadiques (Pise), la cytoponction n’était diagnostique que dans 45,9 % des cas':'Dans une série de 104 cancers médullaires sporadiques (Pise), la cytoponction n’était diagnostique que chez 45,9 % des 85 patients ponctionnés',
'Le premier contrôle a lieu une à deux semaines après le début du traitement, puis':'Le premier contrôle a lieu une à deux semaines après le début du traitement (au plus tard une semaine si la dose initiale atteint 50 µg/j ou davantage), puis',
'Contrôle 1 à 2 semaines après le début, puis':'Contrôle 1 à 2 semaines après le début (au plus tard une semaine si la dose initiale atteint 50 µg/j ou davantage), puis',
'contrôlée 1 à 2 semaines après le début, puis':'contrôlée 1 à 2 semaines après le début (au plus tard une semaine à partir de 50 µg/j initiaux), puis',
'<td style="min-width:10em">Ne pas traiter</td>':'<td style="min-width:10em">Pas de substitution pour l’anomalie isolée ; traiter une hypothyroïdie coexistante</td>',
'<td style="min-width:10em">Pas de substitution ; poursuivre la lévothyroxine chez l’hypothyroïdien connu</td>':'<td style="min-width:10em">Pas de substitution systématique du profil NTIS ; traiter l’hypothyroïdie authentique</td>',
'Normale en dessous de 0,05 ng/ml. En l’absence d’infection, une valeur supérieure à 0,1 à 0,2 ng/ml évoque un cancer médullaire ; une procalcitonine indétectable a une forte valeur prédictive négative.':'Les références et seuils dépendent de l’essai. Des études utilisent 0,1–0,2 ng/ml pour explorer un cancer médullaire ; une valeur indétectable peut être rassurante dans la population étudiée, mais ne suffit pas à exclure toute tumeur. Infection, inflammation systémique, traumatisme et insuffisance rénale doivent être considérés.',
'Études de cancers connus, résumés seuls pour deux sources ; la procalcitonine s’élève dans l’infection, ce qui impose une interprétation hors infection.':'Méta-analyse et cohorte chirurgicale sélectionnée, résumés seuls pour ces deux sources : la validation prospective portait sur 335 patients néerlandais et 61 suisses, dont 44 cancers médullaires. Les performances ne sont pas celles d’un dépistage universel ; une élévation ne se réduit pas au couple infection/cancer.'
}
for f in P.glob('*.html'):
 s=f.read_text()
 for a,b in replacements.items():
  n=s.count(a)
  if n:s=s.replace(a,b);changes.append({'file':f.name,'before':a,'after':b,'count':n})
 if f.name=='E07_c.html':s=re.sub(r'<h3 data-semiology="([^"]+)"',lambda m:f'<h3 id="e07-semio-{m[1]}" data-semiology="{m[1]}"',s)
 f.write_text(s)
D=R/'docs/collaboration/ssp-v2/execution/ALPHA77-CODEX-E07-INTEGRATE'
(D/'corrections-relecture-finale.json').write_text(json.dumps({'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'changes':changes},ensure_ascii=False,indent=2)+'\n')
print(len(changes),'corrections appliquées')
