#!/usr/bin/env python3
"""Idempotent, reviewed C85 additions from passages read on 2 November 2026.

Only the C85 author's reserved files are modified. This does not renew any
review, verification receipt or completion; run verify_c85.py after editing.
"""
from pathlib import Path

ROOT=Path(__file__).resolve().parents[5]
def insert_section(source,anchor,marker,content):
    if marker in source:return source
    start=source.index('id="'+anchor+'"');end=source.index('</section>',start)
    return source[:end]+content+'\n'+source[end:]

def main():
    for name in ('C85_b.html','C85_c.html'):
        p=ROOT/'chapters/C85'/name;s=p.read_text()
        s=s.replace('La TEP à 6 semaines montre un score Deauville 3',
          'La TEP de fin de traitement, réalisée six à huit semaines après la dernière cure, montre un score Deauville 3')
        p.write_text(s)
    p=ROOT/'chapters/C85/C85_c.html';s=p.read_text()
    s=s.replace('Pour le DLBCL, aucun seuil de masse volumineuse n’est validé : on note le plus grand diamètre. En Allemagne, le seuil est de 7,5 cm ou plus',
      'Le diamètre maximal de la masse doit être documenté. Le texte de Lugano de 2014 discutait l’absence d’un seuil universel validé pour le DLBCL ; les recommandations EHA 2025 indiquent désormais que le seuil de 7,5 cm ou plus est largement utilisé. Onkopedia retient aussi ce seuil en Allemagne et signale que certains pays utilisent 10 cm')
    if 'c85-bulk-eha-reference' not in s:
        needle='<p>L’<button class="w" data-k="c85-ipi">'
        s=s.replace(needle,'<p class="src" id="c85-bulk-eha-reference"><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC12456099/" target="_blank" rel="noopener">EHA 2025, Management of first-line LBCL</a>. Le seuil descriptif ne remplace ni la stadification ni l’appréciation de la compression.</p>\n'+needle)
    p.write_text(s)
    p=ROOT/'chapters/C85/C85_a.html';s=p.read_text()
    content='''<h3 id="c85-profiles2023">Lien avec les situations de départ de PROFILES 2023</h3>
<p>PROFILES organise le raisonnement initial du jeune médecin autour de situations cliniques. Pour ce chapitre, les liens pédagogiques retenus sont les suivants ; ils ne constituent pas une liste officielle de maladies « C85 » ni une prédiction des questions d’examen.</p>
<table><tr><th>Situation</th><th>Application dans cette leçon</th></tr>
<tr><td>G2</td><td>Masse ou adénopathie : localiser, caractériser, puis obtenir le diagnostic tissulaire.</td></tr>
<tr><td>G6 et G16</td><td>Fièvre et amaigrissement : rechercher les symptômes généraux et leurs autres causes.</td></tr>
<tr><td>S1.21</td><td>Gonflement cervicofacial : examiner la distribution des signes veineux.</td></tr>
<tr><td>S2.6, S2.7 et S2.9</td><td>Toux, dyspnée et dysphagie : rechercher un retentissement thoracique et son urgence.</td></tr></table>
<p class="src"><a href="https://smifk-cims.ch/profiles-2023/ssps" target="_blank" rel="noopener">SMIFK-CIMS, PROFILES 2023, Situations as Starting Points</a>, introduction et rubriques citées ; traduction et mise en relation pédagogiques.</p>'''
    s=insert_section(s,'c85-0','id="c85-profiles2023"',content);p.write_text(s)
    p=ROOT/'chapters/C85/C85_b.html';s=p.read_text()
    content='''<h3 id="c85-suisse-acces">Accès aux soins et situation professionnelle en Suisse</h3>
<table><tr><th>Question pratique</th><th>Ce qu’il faut distinguer</th></tr>
<tr><td>Indication et remboursement</td><td>L’autorisation Swissmedic et la prise en charge par l’assurance sont deux vérifications différentes. La liste des spécialités (LS) précise les préparations remboursées et leurs limitations ; une indication dans la FI ne suffit pas à garantir le remboursement de chaque situation clinique.</td></tr>
<tr><td>Utilisation hors indication ou hors limitation</td><td>Les articles 71a à 71d OAMal prévoient des exceptions sous conditions. Une demande complète de garantie est examinée par l’assureur après avis de son médecin-conseil ; l’accord doit être obtenu avant de considérer la prise en charge comme acquise. Il ne découle pas automatiquement de la gravité du cancer.</td></tr>
<tr><td>Matériel de soins</td><td>La LiMA concerne les moyens et appareils utilisés notamment à domicile ou en EMS. Elle ne remplace pas la LS des médicaments : le besoin concret en matériel et sa position doivent être vérifiés séparément.</td></tr>
<tr><td>Suspicion d’origine professionnelle</td><td>Rechercher et documenter les expositions professionnelles pertinentes. Une maladie doit remplir les critères de l’article 9 LAA pour être reconnue comme professionnelle ; le seul diagnostic de lymphome ne démontre ni ce lien ni une prise en charge par la Suva.</td></tr></table>
<p class="src">OFSP : <a href="https://www.bag.admin.ch/fr/medicaments" target="_blank" rel="noopener">médicaments et LS</a>, <a href="https://www.bag.admin.ch/fr/prise-en-charge-de-medicaments-dans-des-cas-particuliers" target="_blank" rel="noopener">cas particuliers et garantie de prise en charge</a>, <a href="https://www.bag.admin.ch/fr/liste-des-moyens-et-appareils-lima" target="_blank" rel="noopener">LiMA</a>. Suva : <a href="https://www.suva.ch/fr-ch/prevention/arbeitsmedizin/connaitre-et-reconnaitre-les-maladies-professionnelles" target="_blank" rel="noopener">définition des maladies professionnelles</a>. Les limitations actuelles de chaque médicament doivent être consultées au moment de la prescription.</p>
<h3 id="c85-conduite-fi">Conduite automobile : raisonner selon le produit et les effets neurologiques</h3>
<table><tr><th>Produit exact</th><th>Consigne de la FI suisse consultée</th></tr>
<tr><td>Yescarta, août 2026</td><td>Ne pas conduire ni utiliser de machines lourdes ou dangereuses pendant au moins deux semaines après la perfusion, et prolonger cette abstention jusqu’à disparition complète des effets neurologiques éventuels.</td></tr>
<tr><td>Breyanzi, février 2026</td><td>Pas de conduite ni de machines lourdes ou dangereuses pendant au moins deux semaines après administration, en raison du risque d’événements neurologiques, dont troubles mentaux et convulsions.</td></tr>
<tr><td>Keytruda, août 2026</td><td>Prudence tant que le patient n’est pas certain de l’absence d’effet sur ses capacités, notamment en cas de fatigue.</td></tr></table>
<p>Le délai minimal d’une FI ne permet pas, à lui seul, de déclarer une personne apte si des symptômes persistent. Il faut également prendre en compte les autres médicaments et l’état clinique ; les durées ne sont pas transposées automatiquement à tous les CAR-T.</p>
<p class="src">Rubrique « Effet sur l’aptitude à la conduite et l’utilisation de machines » des FI exactes : <a href="https://amiko.oddb.org/fr/fi?gtin=7680669860011" target="_blank" rel="noopener">Yescarta</a>, <a href="https://amiko.oddb.org/fr/fi?gtin=7680674690016" target="_blank" rel="noopener">Breyanzi</a>, <a href="https://amiko.oddb.org/fr/fi?gtin=7680662310025" target="_blank" rel="noopener">Keytruda</a>.</p>'''
    s=insert_section(s,'c85-13','id="c85-suisse-acces"',content);p.write_text(s)
    print('C85: timing, bulk, Swiss access and PROFILES revised; verification receipts remain unchanged.')
if __name__=='__main__':main()
