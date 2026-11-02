"""Targeted corrections supported by passages actually read on 2026-11-02."""
from pathlib import Path
import subprocess
ROOT=Path(__file__).resolve().parents[5]
CH=ROOT/'chapters/N04'
BASE='8a512893acbab9caa0dcfdd0e8682a44ea72fda6'

a=(CH/'N04_a.html').read_text();b=(CH/'N04_b.html').read_text();c=(CH/'N04_c.html').read_text()
d=subprocess.check_output(['git','show',f'{BASE}:chapters/N04/N04_d.html'],cwd=ROOT,text=True)
pop2=subprocess.check_output(['git','show',f'{BASE}:chapters/N04/N04_pop2.html'],cwd=ROOT,text=True)
pop1=(CH/'N04_pop1.html').read_text()

# Move the full inherited coding content after the clinical conclusion, without loss.
start=a.index('<h3 id="n04-a02-partie-4">');end=a.index('<div class="key">',start)
coding=a[start:end]
coding=coding.replace('4. Le codage CIM-10-GM 2024 : un syndrome et dix sous-codes','CIM-10-GM 2024 : un syndrome et dix sous-codes')
coding=coding.replace('Glomérulonéphrite mésangioproliférative diffuse','Glomérulonéphrite mésangio-proliférative diffuse').replace('Maladie à dépôts denses','Maladie à dépôt dense').replace('<td>Type non précisé</td>','<td>Type de modification morphologique non précisé</td>')
a=a[:start]+'<p>Le diagnostic clinique précède le codage. La table complète N04.0–N04.9 est conservée dans l’annexe nosologique, après la conclusion clinique.</p>'+a[end:]
annex='<section class="ilot" id="n04-annexe-cim"><h2><span class="n">Annexe</span> Correspondance nosologique suisse</h2>'+coding+'<p class="src">Source : Office fédéral de la statistique, CIM-10-GM 2024 française, nomenclature du 31 octobre 2024 ; catégorie N04 et table commune des sous-codes N00–N07 relues le 2 novembre 2026. La nomenclature décrit les lésions et ne remplace pas la démarche clinique.</p></section>'
idx=b.rindex('</section>')+len('</section>');b=b[:idx]+annex+b[idx:]

# Exact product information must not be mistaken for a disease-specific protocol.
d=d.replace('80 à 120 mg/jour pour le traitement à dose élevée du syndrome néphrotique','80 à 120 mg/jour pour le traitement à dose élevée du syndrome néphrotique ; la FI limite habituellement ce traitement à dose élevée à 48–72 heures, jusqu’à stabilisation')
d=d.replace('Les doses pédiatriques en mg/m² de KDIGO 2025 priment pour l’indication','Cette plage de la FI ne définit pas le protocole néphrologique prolongé. Les schémas pédiatriques en mg/m² de KDIGO 2025 sont distincts et relèvent de la décision spécialisée')
d=d.replace('; dose maximale 1500 mg/jour','; maximum intraveineux 1500 mg/jour, réservé dans la FI aux situations de fonction rénale fortement diminuée')
d=d.replace('Créatinine &lt; 200 µmol/L (adulte) ou &lt; 140 µmol/L (enfant) ; arrêt si aucun effet après 3 mois','Si la créatinine initiale est anormale : maximum initial 2,5 mg/kg/jour, sous surveillance étroite, dans l’exception néphrotique de la FI ; seuils de créatinine 200 µmol/L (adulte) et 140 µmol/L (enfant). Arrêt si aucun effet après 3 mois')
d=d.replace('voie intraveineuse continue 3 à 6 mg/kg/jour, intermittente 10 à 15 mg/kg tous les 2 à 5 jours','voie orale : 50 à 200 mg/jour (1 à 4 dragées), le matin, sans fractionner les dragées ; voie intraveineuse continue : 3 à 6 mg/kg/jour, intermittente : 10 à 15 mg/kg tous les 2 à 5 jours. Ces plages générales de la FI ne remplacent pas les protocoles néphrologiques spécifiques')
d=d.replace('Prophylaxie du syndrome néphrotique : position d’experts (ÖGN)','Prophylaxie propre au syndrome néphrotique : position d’experts (ÖGN), distincte des indications médicales aiguës et chirurgicales de la FI')
d=d.replace('thrombose veineuse : 1 mg/kg toutes les 12 h','thrombose veineuse : 1 mg/kg toutes les 12 h ; si clairance &lt; 30 mL/min, 1 mg/kg une fois par jour selon la FI')
d=d.replace('Clairance &lt; 15 mL/min','Clairance &lt; 15 mL/min')
b=b.replace('Demi-dose selon l’ÖGN ; contre-indiqué si clairance &lt; 15 mL/min selon la FI','La FI prévoit une demi-dose pour une clairance de 15 à 30 mL/min ; ne pas utiliser si clairance &lt; 15 mL/min. Ne pas assimiler sans vérification clairance en mL/min et DFGe indexé')
b=b.replace('son DFGe de 85 permet de se passer de biopsie','son DFGe de 85 mL/min/1,73 m² permet d’envisager l’absence de biopsie si les anticorps sont nettement positifs avec la méthode considérée et si les autres causes ont été exclues')

pop2=pop2.replace('Induction 5 mg/kg/jour (adulte) ou 6 mg/kg/jour (enfant) en 2 prises ;','Induction 5 mg/kg/jour (adulte) ou 6 mg/kg/jour (enfant) en 2 prises si la fonction rénale le permet ; si la créatinine initiale est anormale dans l’exception néphrotique de la FI, maximum initial 2,5 mg/kg/jour avec surveillance étroite ;')
pop1=pop1.replace('Traitement de la thrombose veineuse : 1 mg/kg toutes les 12 heures.','Traitement de la thrombose veineuse : 1 mg/kg toutes les 12 heures ; si la clairance de la créatinine est inférieure à 30 mL/min, la FI prévoit 1 mg/kg une fois par jour.')
pop1=pop1.replace('Patient de DFGe 25 mL/min : 20 mg par jour','Patient dont la clairance de la créatinine est de 25 mL/min, en prophylaxie : 20 mg par jour').replace('Patient de 85 kg en traitement d’une thrombose : 85 mg toutes les 12 heures (1 mg/kg).','Patient de 85 kg, sans insuffisance rénale sévère, en traitement d’une thrombose : 85 mg toutes les 12 heures (1 mg/kg). Le DFGe indexé en mL/min/1,73 m² ne doit pas être substitué sans examen à une clairance en mL/min pour l’adaptation du produit.')
c=c.replace('Les podocytes sont post-mitotiques : ils ne se renouvellent pas, de sorte qu’une perte podocytaire n’est pas compensée par une division cellulaire','Les podocytes matures sont post-mitotiques : leur prolifération ne compense pas efficacement leur perte. Le consensus autrichien décrit toutefois une réserve limitée de précurseurs épithéliaux pariétaux. Une perte podocytaire persistante dépasse cette réparation limitée')
# Clarify inherited statements across clinical and prescribing surfaces.
a=a.replace('Une hyalinose sans syndrome néphrotique complet est secondaire jusqu’à preuve du contraire et ne reçoit pas d’immunosuppression.','Une hyalinose sans syndrome néphrotique complet fait rechercher une cause secondaire ou génétique et ne justifie pas d’emblée une immunosuppression.')
a=a.replace('doit faire rechercher une cause secondaire et ne justifie pas d’immunosuppression.','doit faire rechercher une cause secondaire ou génétique et ne justifie pas d’emblée une immunosuppression.')
b=b.replace('La statine est de première ligne si la dyslipidémie persiste (dès 8 ans selon le contexte familial et des LDL ou Lp(a) très élevés).','La statine est de première ligne si la dyslipidémie persiste. La mention internationale d’un traitement dès 8 ans, selon le contexte familial et des LDL ou Lp(a) très élevés, ne vaut pas autorisation de tout produit suisse : la FI de Sortis ne l’autorise pas chez l’enfant ou l’adolescent. Le choix pédiatrique dépend du produit, de son indication et de l’avis spécialisé.')
b=b.replace('Le tableau gradue la conduite selon l’albumine.','Les schémas de prévention ne sont pas uniformisés : la figure 11 de KDIGO emploie une anticoagulation à dose pleine à envisager dans certains profils à haut risque, tandis que l’ÖGN souligne l’absence d’essais contrôlés et de frontière posologique uniforme entre prévention et traitement. Les doses prophylactiques et curatives de la FI ne doivent donc pas être interchangées automatiquement ; le choix relève d’une appréciation spécialisée du bénéfice et du risque. Le tableau gradue la conduite selon l’albumine.')
d=d.replace('Prescrite pour la dyslipidémie persistante ; contre-indiquée pendant la grossesse','Prescrite pour la dyslipidémie persistante ; Sortis n’est pas autorisé chez l’enfant ou l’adolescent ; contre-indiquée pendant la grossesse')
pop2=pop2.replace('avec ciclosporine, au plus 10 mg/jour','avec ciclosporine, au plus 10 mg/jour')
if 'data-pop="n04-mono-atorvastatine"' in pop2:
    start=pop2.index('data-pop="n04-mono-atorvastatine"');end=pop2.index('</template>',start)
    pop2=pop2[:end]+'<p>Population : la FI suisse de Sortis n’autorise pas son utilisation chez l’enfant ou l’adolescent. Une recommandation internationale sur la classe des statines ne constitue pas une autorisation pédiatrique de ce produit.</p>'+pop2[end:]
b=b.replace('<td>Énoxaparine</td><td>Clairance', '<td>Énoxaparine — prophylaxie</td><td>Clairance')
# A final rubric review identified an internal duration discrepancy in the consulted KDIGO PDF.
b=b.replace('La décroissance commence 2 semaines après la rémission complète et dure au moins 24 semaines.', 'La décroissance commence 2 semaines après la rémission complète. La durée doit être individualisée : le texte de KDIGO décrit environ 24 semaines d’exposition totale, tandis que sa figure 45 mentionne une décroissance d’au moins 24 semaines. Le consensus européen ÖGN vise au plus 24 semaines de traitement total ; ces durées ne doivent pas être additionnées ni transformées en minimum universel de décroissance (voir la fenêtre de discussion ci-dessous).')
pop2=pop2.replace('KDIGO : décroissance sur au moins 24 semaines après rémission. ÖGN : durée totale d’au plus 24 semaines. Aucune recommandation suisse.', 'Dans le PDF KDIGO 2021 consulté, la figure 45 (page 155 du supplément) mentionne une décroissance sur au moins 24 semaines, mais le texte voisin (page 156 du supplément) décrit une exposition totale d’environ 24 semaines et constate l’absence de comparaison entre décroissance rapide et lente chez l’adulte. L’ÖGN 2023 retient une durée totale d’au plus 24 semaines, reconnaît l’absence de schéma uniforme et évoque une réduction de 5 à 10 mg par semaine après rémission. La figure et le texte KDIGO ne permettent donc pas d’enseigner un minimum universel de 24 semaines de décroissance. Le cadre européen et la situation individuelle guident la discussion spécialisée ; aucune recommandation suisse précisant cette durée n’a été trouvée dans les sources consultées.')
pop2=pop2.replace('Spiricort® cite 80 à 120 mg/jour pour le syndrome néphrotique.', 'Spiricort® cite 80 à 120 mg/jour pour un traitement à dose élevée, habituellement limité à 48–72 heures jusqu’à stabilisation ; ce passage ne définit pas un protocole néphrologique prolongé.')
pop2=pop2.replace('Présenter 1 mg/kg avec les deux plafonds ; la FI suisse autorise ces doses. La durée reste une incertitude à discuter avec le centre spécialisé.', 'Présenter les schémas spécialisés de 1 mg/kg avec leurs plafonds respectifs, en les distinguant des plages générales et des durées décrites dans les FI suisses. Ne pas présenter les FI comme une autorisation globale de tous les schémas prolongés. La durée et la décroissance restent à individualiser avec le centre spécialisé, en explicitant la discordance des sources.')
for part,content in [('a',a),('b',b),('c',c),('d',d),('pop1',pop1),('pop2',pop2)]:
    (CH/f'N04_{part}.html').write_text(content)
print('N04: coding annex preserved; targeted Swiss-product/renal-dose and diagnostic corrections applied.')
