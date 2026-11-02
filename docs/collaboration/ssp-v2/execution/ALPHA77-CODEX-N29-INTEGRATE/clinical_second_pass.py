"""Deuxième lecture : remplace des paragraphes dont les liens interrompaient les chaînes textuelles."""
from pathlib import Path
from html import unescape
import re
ROOT=Path(__file__).resolve().parents[5]
def plain(s):return unescape(re.sub('<[^>]*>','',s))
for p in (ROOT/'chapters/N29').glob('*.html'):
 t=p.read_text()
 def paragraph(m):
  h=m[0];s=plain(h)
  if 'La chirurgie est recommandée chez plus de 50 %' in s:
   return '<p>Un obstacle menaçant la fonction rénale demande un drainage sans attendre l’effet des antibiotiques. Les séries citées par l’EAU rapportent un recours chirurgical chez plus de 50 % des patients, mais ce chiffre descriptif ne constitue pas une indication automatique. Le siège, le dommage et la réponse médicale guident le geste ; les délais proposés de chirurgie reconstructrice vont de deux à six semaines à plusieurs mois, sans règle universelle validée. Source : EAU, §3.16.4.</p>'
  if 'La première intention est la benzathine' in s:
   return '<p>La première intention chez l’adulte atteint de syphilis tardive, sans atteinte neurologique, oculaire ou otique, est la <button class="w" data-k="n29-extencilline">benzathine benzylpénicilline</button> : Extencilline® 2,4 millions d’unités par voie intramusculaire profonde une fois par semaine pendant trois semaines. L’IUSTI 2020 mentionne la pénicilline procaïne 600 000 unités par jour pendant 17 à 21 jours comme alternative historique ; aucun produit suisse correspondant n’a été vérifié ici. La HAS 2025 propose une autre voie en cas d’indisponibilité : doxycycline pendant 28 jours, hors grossesse et atteinte neurologique. Chez l’adulte non enceinte allergique à la pénicilline, la FI suisse Doxycyclin-Mepha® prévoit 100 mg par voie orale deux fois par jour pendant quatre semaines. Certains contextes demandent une désensibilisation spécialisée. L’azithromycine est exclue par l’IUSTI.</p>'
  if 'Le traitement spécifique est la cystéamine' in s:
   return '<p>Le traitement spécifique est la <button class="w" data-k="n29-procysbi">cystéamine</button> : Procysbi® à libération retardée, dose d’entretien de 1,3 g/m²/jour en deux prises espacées de douze heures, maximum 1,95 g/m²/jour. Commencer à un sixième à un quart de la dose cible, puis augmenter toutes les quatre à six semaines, ou toutes les deux semaines entre un et six ans selon la FI. Pour les leucocytes mixtes, la cible est inférieure à 1 nmol d’hémicystine/mg de protéine, avec prélèvement 30 minutes après la dose du matin, soit 12,5 heures après celle du soir. Le laboratoire précise la cible de toute autre méthode. <button class="w" data-k="n29-cystadrops">Cystadrops®</button>, une goutte par œil quatre fois par jour chez l’enfant de plus de six mois et chez l’adulte, traite les dépôts cornéens ; la cystéamine orale ne suffit pas pour l’œil.</p>'
  if 'Le traitement de soutien comprend' in s:
   return '<p>Le soutien comprend nutrition adaptée, accès libre à l’eau et compensation individualisée des pertes hydriques, électrolytiques et de bicarbonate. Les recommandations 2026 discutent l’indométacine chez certains jeunes enfants dont le Fanconi reste incontrôlé ; l’arrêter si les pertes sont maîtrisées ou si la fonction rénale baisse, et ne pas l’associer aux inhibiteurs de l’enzyme de conversion ou antagonistes de l’angiotensine II. Ces derniers ne constituent pas une néphroprotection systématique dans la cystinose ; leur indication dépend notamment de l’hypertension ou d’une protéinurie glomérulaire. La prise en charge spécialisée de la croissance et de l’os peut associer hormone de croissance, phosphate, vitamine D active, correction de l’acidose et physiothérapie. La transplantation est le traitement de choix au stade terminal, sans supprimer le besoin de cystéamine systémique.</p>'
  if 'Le praziquantel 40 mg/kg est le traitement recommandé' in s:
   return '<p>Pour la schistosomiase à <i>S. haematobium</i>, la revue suisse RMS 2018 propose du <button class="w" data-k="n29-praziquantel">praziquantel</button>, 40 mg/kg par voie orale en prise unique, répétée après quatre semaines. Le RCP français Biltricide® décrit cette dose unique pour cette espèce, avec prise pendant ou après un repas ; les doses diffèrent pour certaines autres espèces. Une exposition très récente ou un syndrome de Katayama exige une discussion spécialisée, car les formes immatures sont peu sensibles au médicament. Les lésions inflammatoires peuvent régresser ; une fibrose fixée ne doit pas être considérée comme réversible par le seul traitement antiparasitaire. Les gestes urologiques se discutent selon l’obstacle persistant et son retentissement.</p>'
  if 'Le choix suit la recommandation européenne 2020 ;' in s:
   return '<p>Le choix confronte la FI du produit suisse exact à la HAS 2025 et à l’IUSTI 2020 ; les formulations de pénicilline ne sont pas interchangeables. En cas de grossesse, de signes neurologiques, oculaires ou auditifs, demander un avis spécialisé plutôt que transposer cette alternative orale.</p>'
  return h
 t=re.sub(r'<p(?:\s[^>]*)?>.*?</p>',paragraph,t,flags=re.S)
 # Discrete cells and captions, including residual inherited summary statements.
 for old,new in {
 'En Europe, la microscopie urinaire n’est positive que dans 11,5 % des cas ; la sérologie ne distingue pas infection active et ancienne':'Dans la cohorte de Barcelone : 96/831 cas testés positifs, sans estimation indépendante de sensibilité ; la sérologie ne prouve pas l’activité',
 'Contexte, manifestations tertiaires':'Histoire de l’infection, sérologie et recherche de manifestations ; la forme tardive peut être latente',
 'Diagnostic de syphilis (infection de plus d’un an ou de durée inconnue) puis évaluation de l’organe':'Diagnostic sérologique, datation (au moins un an ou durée inconnue pour la forme tardive), puis évaluation de la lésion et du lien causal',
 'Corticothérapie préventive si atteinte cardiovasculaire ou neurologique':'Prophylaxie à discuter dans les formes à risque ; surveillance hospitalière, preuve limitée',
 'et qu’elles se préviennent par la surveillance et non par le renoncement au traitement.':'La surveillance permet de repérer leur survenue et d’adapter la prise en charge ; elle ne garantit pas leur prévention.',
 'Le schéma individuel suisse ou européen n’a pas été lu : le cours enseigne la recommandation de l’Organisation mondiale de la santé et la pratique observée à Barcelone, sans la présenter comme une recommandation suisse.':'La revue suisse RMS 2018 et le RCP français Biltricide® ont été relus dans cette reprise. La pharmacie doit confirmer le produit et les modalités d’accès ; l’absence de résultat dans une base ne prouve pas l’indisponibilité.',
 'Aucun protocole suisse lu':'Suivi de cohorte descriptif ; conduite clinique suisse RMS 2018 détaillée ci-dessous',
 'Consensus 2014 ; recommandations 2026 lues en résumé':'Recommandations 2026, sections complètes relues ; FI suisse Procysbi® pour méthode et horaire',
 'Les recommandations 2026 sur la cystinose ont été lues en résumé seulement.':'Les sections diagnostiques et thérapeutiques pertinentes du texte intégral 2026 ont été relues dans cette reprise.',
 'aucune recommandation suisse ou européenne propre à la tuberculose urogénitale n’a été lue ; les données sur l’urine proviennent d’une revue non systématique.':'le guide suisse général 2024 est complété ici par la section urogénitale 3.16 de l’EAU, effectivement relue ; les valeurs de la revue 2021 restent attribuées et leurs divergences sont exposées.',
 '(résumé lu)':'(texte intégral, sections pertinentes relues en novembre 2026)',
 'infection de plus d’un an avec manifestation tertiaire':'syphilis documentée et lésion d’organe caractérisée sans confondre forme tardive et forme tertiaire',
 'Aucune entrée N29 ne comporte d’inclusion ni d’exclusion supplémentaire.':'La catégorie N29 n’ajoute pas de note générale ; N29.1 inclut explicitement tuberculose et schistosomiase, et N29.8 la thésaurismose cystinique. Ces inclusions ont été vérifiées dans le fichier OFS CIM-10-GM 2024.',
 'les lésions urétérales sont limitées à la moitié inférieure des uretères':'les lésions urétérales siègent typiquement dans leur moitié inférieure',
 'l’uretère inférieur seulement':'l’uretère surtout inférieur',
 'Infection non traitée de plus d’un an':'Infection non traitée d’au moins un an ou de durée inconnue',
 'Le praziquantel est considéré comme sûr pendant la grossesse selon l’Organisation mondiale de la santé.':'Le RCP français Biltricide® autorise le praziquantel pendant la grossesse si cela est cliniquement justifié ; il demande, pour un traitement court, d’interrompre l’allaitement le jour du traitement et durant les 24 heures suivantes. Confirmer le produit effectivement disponible en Suisse.',
 'l’éthambutol et le pyrazinamide passent à trois prises par semaine':'le guide suisse propose l’éthambutol et le pyrazinamide trois fois par semaine ; cette proposition doit être confrontée aux FI, notamment à la contre-indication de Pyrazinamide Labatec® sous 50 mL/min et de Rifater® sous 30 mL/min',
 'Cible &lt; 1 nmol':'Cible sur leucocytes mixtes avec Procysbi®, 30 min après la dose matinale : &lt; 1 nmol',
 '17p 13.2':'17p13.2','iv 87-94':'iv87-94','jours 1,8 et 15':'jours 1, 8 et 15',
 }.items():t=t.replace(old,new)
 t=re.sub(r'(, chaque semaine si insuffisance rénale){2,}',r'\1',t)
 p.write_text(t)
print('Deuxième lecture des paragraphes liés et résumés : corrections propagées.')
