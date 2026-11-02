#!/usr/bin/env python3
"""Fix observed ICD semantics and distinguish supportive signs from formal rules."""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[5]
ONKO='https://www.onkopedia.com/de/onkopedia/guidelines/diffuses-grosszelliges-b-zell-lymphom/@@guideline/html/index.html'
KEY='https://amiko.oddb.org/fr/fi?gtin=7680662310025'
POL='https://amiko.oddb.org/fr/fi?gtin=7680671650020'
def a(url,label):return f'<a href="{url}" target="_blank" rel="noopener">{label}</a>'
changes={
 'diagnostics incomplets (C85.1, C85.7, C85.9) traités comme démarche à compléter':'diagnostics non précisés (C85.1, C85.9) à compléter ; C85.7 réservé aux autres types précisés',
 'Les autres codes signalent une précision insuffisante, donc une étape diagnostique manquante.':'C85.1 et C85.9 indiquent une absence de précision ; C85.7 signifie au contraire « autres types précisés » et ne doit pas leur être assimilé.',
 'et exclut explicitement C83.3 (lymphome diffus à grandes cellules B) et C83.8 (autres lymphomes non folliculaires)':' ; les rubriques C83.3 (lymphome diffus à grandes cellules B) et C83.8 (autres lymphomes non folliculaires) excluent explicitement le lymphome médiastinal codé C85.2',
 'C85.2 nomme une maladie, alors que C85.1, C85.7 et C85.9 décrivent un état d’information.':'C85.2 nomme l’entité médiastinale ; C85.1 et C85.9 expriment une absence de précision. C85.7 désigne d’autres types précisés : le caractère résiduel de la rubrique ne signifie pas que le diagnostic tissulaire est incomplet.',
 'le code C85.2 exclut C83.3':'la rubrique C83.3 exclut explicitement le lymphome médiastinal C85.2',
 'Les codes C85.1, C85.7 et C85.9 ne désignent aucune maladie précise.':'Les codes C85.1 et C85.9 indiquent une absence de précision. C85.7 regroupe d’autres types précisés ; ce libellé ne permet pas de conclure à une biopsie insuffisante.',
 'C85.1, C85.7 et C85.9 signalent une précision insuffisante.':'C85.1 et C85.9 signalent une absence de précision ; C85.7 regroupe d’autres types précisés.',
 'et exclut C83.3 et C83.8. Les codes C85.1 (lymphome à cellules B sans précision), C85.7 (autres types précisés) et C85.9 (non précisé) décrivent un état d’information.':' ; C83.3 et C83.8 excluent explicitement cette entité. C85.1 (lymphome à cellules B sans précision) et C85.9 (non précisé) ne doivent pas être confondus avec C85.7, qui signifie « autres types précisés ».',
 'C85.2 exclut C83.3 et C83.8.':'Les rubriques C83.3 et C83.8 excluent le lymphome médiastinal codé C85.2.',
 'biopsie tissulaire suffisante</button> avant tout traitement.':'biopsie tissulaire suffisante</button> pour qualifier la maladie. En présence d’une compression menaçante, l’équipe spécialisée coordonne la sécurité immédiate, le prélèvement et le traitement ; cet enchaînement pédagogique ne doit pas devenir un retard à la prise en charge de l’urgence.',
 'Critères formels du diagnostic de lymphome médiastinal primitif à grandes cellules B (C85.2).':'Diagnostic formel : synthèse anatomoclinique et hématopathologique. Les éléments ci-dessous guident cette synthèse ; ils ne constituent pas un score validé ni une règle imposant la positivité simultanée de chaque marqueur.',
 '(3) Phénotype compatible : immunoglobuline de surface négative, CD23 positif, CD30 faible, MAL positif, CD15 négatif':'(3) Phénotype compatible, interprété en panel : absence habituelle d’immunoglobuline de surface, expression fréquente de CD23, expression souvent faible de CD30, expression possible de MAL, CD15 généralement négatif. Les fréquences rapportées dans les sources montrent que ces marqueurs ne sont pas tous obligatoirement positifs chez chaque patient',
 '(5) Codage :':'Le codage suit le diagnostic, sans constituer un critère biologique supplémentaire :',
 'Critères formels : biopsie tissulaire, masse médiastinale antérieure, phénotype compatible, exclusion du Hodgkin et de la zone grise, codage C85.2 ou diagnostic à compléter.':'Diagnostic formel : intégration de la biopsie, de la présentation médiastinale et d’un panel phénotypique ; aucun marqueur de soutien isolé ne suffit. Le codage vient ensuite ; C85.7 signifie « autre type précisé ».',
 'insuffisance cardiaque après anthracyclines (surtout avant 55 ans)':'risque d’insuffisance cardiaque accru par rapport à la population générale après anthracyclines, particulièrement lorsque l’exposition a eu lieu avant 55 ans',
 'width="1181" height="1153"':'width="787" height="768"',
}
for p in [*(ROOT/'chapters/C85').glob('*.html'),ROOT/'glossary/c85.py']:
 t=p.read_text()
 for old,new in changes.items():
  # Protect an already-corrected phrase to make reruns idempotent.
  token='__MEDINA_ALREADY_CORRECTED__';t=t.replace(new,token).replace(old,new).replace(token,new)
 p.write_text(t)

p=ROOT/'chapters/C85/C85_b.html';t=p.read_text()
if 'c85-organes-fi-2026' not in t:
 old='<b>Insuffisance rénale ou hépatique.</b> Aucune source lue ne traite l’adaptation des doses ; le chapitre ne propose pas de conduite chiffrée.'
 new=f'''<b>Insuffisance rénale ou hépatique.</b> Les recommandations dépendent du produit, pas du seul diagnostic. <span id="c85-organes-fi-2026">La FI suisse Keytruda (août 2026) ne demande pas d’adaptation en insuffisance rénale légère à modérée ; l’insuffisance rénale sévère n’a pas été étudiée. Pour le foie, aucune adaptation n’est demandée dans les formes légères ou modérées, avec données limitées pour les formes modérées ; les formes sévères n’ont pas été étudiées.</span> La FI Polivy (novembre 2025) ne demande pas d’adaptation pour une clairance de la créatinine d’au moins 30 ml/min ; aucune recommandation posologique n’est disponible en dessous de ce seuil. Elle demande d’éviter le produit si la bilirubine totale dépasse 1,5 fois la limite supérieure de la normale. Ces limites concernent ces préparations ; les autres composants des associations exigent leur propre FI. {a(KEY,'FI suisse Keytruda, insuffisances d’organe')} ; {a(POL,'FI suisse Polivy, instructions posologiques particulières')}.'''
 if old not in t:raise ValueError('Organ impairment paragraph missing')
 t=t.replace(old,new)
t=t.replace('Onkopedia traite la grossesse au § 5.2.8, mais cette section n’a pas été lue en détail : lacune.',f'''La section 5.2.8 d’Onkopedia a été relue : elle distingue les risques selon le trimestre et souligne le risque de la chimiothérapie pendant l’organogenèse ainsi que les conséquences de la prématurité. Ces recommandations sur les lymphomes agressifs exigent une discussion hématologique et obstétricale individualisée ; elles ne sont pas un protocole spécifique de lymphome médiastinal déduit de ce rapport de cas. {a(ONKO,'Onkopedia, grossesse et fertilité')}.''')
t=t.replace('La préservation de la fertilité se discute avant le traitement ; la cryoconservation du sperme est proposée en cas de désir d’enfant','La préservation de la fertilité se discute avant le traitement. Onkopedia relie notamment le risque aux alkylants et à l’irradiation pelvienne, décrit une possible réduction de la réserve ovarienne, et recommande une conservation du sperme avant chimiothérapie en cas de désir d’enfant')
p.write_text(t)
print('C85 : codage C85.7, sens des exclusions, diagnostic intégré et FI des insuffisances d’organe corrigés.')
