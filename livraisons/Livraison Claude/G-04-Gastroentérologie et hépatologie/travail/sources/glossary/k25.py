from cardio_1 import a, G
from cardio_2 import t
# K25 — Ulcère gastroduodénal (G-04-Gastroentérologie et hépatologie) : clés propres au cours, absentes des glossaires canoniques au 08.10.2026.
# Collision possible : IPP peut aussi être défini par d'autres cours G-04 (K21, K29, K30, K92) ; garder une seule définition à l'intégration.
a('IPP',[('I','Inhibiteur de la'),('P','Pompe à'),('P','Protons')],'Inhibiteur de la pompe à protons','<p>Médicament qui bloque de façon irréversible la pompe à protons de la cellule pariétale gastrique, étape finale commune de la sécrétion acide (pantoprazole, ésoméprazole, oméprazole, lansoprazole, rabéprazole).</p>','k25-d-ipp')
a('COX-1',[('COX','CycloOXygénase'),('1','isoforme 1 (constitutive)')],'Cyclo-oxygénase de type 1','<p>Enzyme exprimée en permanence dans l’estomac, le rein et les plaquettes ; elle produit les prostaglandines de protection gastrique et le thromboxane plaquettaire. Les AINS et l’aspirine l’inhibent.</p>','k25-cox')
a('ECL',[('E','Entéro-'),('C','Chromaffin-'),('L','Like (de type entérochromaffine)')],'Cellules de type entérochromaffine','<p>Cellules endocrines du corps gastrique qui libèrent l’histamine sous l’effet de la gastrine et de l’acétylcholine.</p>','k25-ecl')
a('CagA',[('Cag','Cytotoxin-associated gene (gène associé à la cytotoxine)'),('A','protéine A')],'Protéine CagA d’Helicobacter pylori','<p>Protéine de virulence injectée dans la cellule épithéliale par un système de sécrétion de type IV ; associée à une inflammation plus intense, à l’ulcère et au cancer gastrique.</p>','k25-caga')
a('VacA',[('Vac','Vacuolating (vacuolisante)'),('A','cytotoxine A')],'Cytotoxine vacuolisante VacA d’Helicobacter pylori','<p>Toxine qui forme des canaux membranaires, crée des vacuoles dans les cellules épithéliales et freine les lymphocytes T.</p>','k25-caga')
a('MALT',[('M','Mucosa-'),('A','Associated'),('L','Lymphoid'),('T','Tissue')],'Tissu lymphoïde associé aux muqueuses','<p>Tissu lymphoïde des muqueuses ; dans l’estomac, il apparaît sous l’effet de l’infection à Helicobacter pylori et peut donner un lymphome de la zone marginale.</p>','k25-malt')
a('MEN1',[('MEN','Multiple Endocrine Neoplasia (néoplasie endocrinienne multiple)'),('1','type 1')],'Gène et syndrome de néoplasie endocrinienne multiple de type 1','<p>Gène suppresseur de tumeur dont la mutation germinale provoque la néoplasie endocrinienne multiple de type 1 (hyperparathyroïdie, tumeurs neuroendocrines duodéno-pancréatiques, adénomes hypophysaires).</p>','k25-nem1')
a('WSES',[('W','World'),('S','Society of'),('E','Emergency'),('S','Surgery')],'World Society of Emergency Surgery (Société mondiale de chirurgie d’urgence)','<p>Société savante qui a publié en 2020 les recommandations sur l’ulcère perforé et hémorragique (Tarasconi et al., World Journal of Emergency Surgery 2020;15:3).</p>','k25-tdm-perf')
a('ASGE',[('A','American'),('S','Society for'),('G','Gastrointestinal'),('E','Endoscopy')],'American Society for Gastrointestinal Endoscopy (Société américaine d’endoscopie digestive)','<p>Société savante auteure de la recommandation de 2010 sur le rôle de l’endoscopie dans la maladie ulcéreuse (Gastrointestinal Endoscopy 2010;71:663–668).</p>')
a('CONCERN',[('CONCERN','nom de l’essai, non développable lettre à lettre dans la publication')],'Essai CONCERN (célécoxib contre naproxène après ulcère hémorragique sous aspirine)','<p>Essai randomisé en double aveugle de Hong Kong (Chan et al., Lancet 2017;389:2375–2382).</p>','k25-concern')
a('G-04-Gastroentérologie',[('G','Gastroentérologie (initiale de la spécialité)'),('04','quatrième fragment dans l’ordre de production'),('Gastroentérologie','nom littéral du fragment, complété par « et hépatologie »')],'Fragment G-04-Gastroentérologie et hépatologie de MEDINA','<p>Quatrième fragment de production de MEDINA, qui réunit les cours de gastroentérologie et d’hépatologie (organisation/fragments.json).</p>')
a('Zollinger-Ellison',[('Zollinger-Ellison','noms propres de Robert Zollinger et Edwin Ellison, chirurgiens qui ont décrit le syndrome en 1955')],'Syndrome de Zollinger-Ellison (gastrinome)','<p>Hypersécrétion acide permanente due à un gastrinome duodénal ou pancréatique ; ulcères multiples, distaux ou réfractaires et diarrhée.</p>','k25-zes')
a('NSAID',[('N','Non-'),('S','Steroidal'),('A','Anti-inflammatory'),('D','Drug')],'Anti-inflammatoire non stéroïdien (sigle anglais)','<p>Équivalent anglais du sigle AINS, conservé dans les titres de publications.</p>','k25-ains')
a('NSAIDs',[('NSAID','Non-Steroidal Anti-inflammatory Drug'),('s','pluriel anglais')],'Anti-inflammatoires non stéroïdiens (sigle anglais au pluriel)','<p>Équivalent anglais du sigle AINS au pluriel, conservé dans les titres de publications.</p>','k25-ains')
a('Amoxi-Mepha',[('Amoxi','Amoxicilline'),('Mepha','nom du fabricant suisse Mepha')],'Amoxi-Mepha (amoxicilline, produit suisse)','<p>Spécialité suisse d’amoxicilline ; information professionnelle d’août 2024 consultée le 08.10.2026.</p>','k25-d-amox')
a('gyrA',[('gyr','gyrase (ADN gyrase)'),('A','sous-unité A')],'Gène gyrA codant la sous-unité A de l’ADN gyrase','<p>Ses mutations rendent Helicobacter pylori résistant à la lévofloxacine.</p>','k25-mutations')
a('IIc',[('II','stade II de Forrest (stigmate de saignement récent)'),('c','sous-type c : tache pigmentée plane')],'Stade IIc de la classification de Forrest','<p>Ulcère portant une tache pigmentée plane, à faible risque de récidive hémorragique.</p>','k25-forrest')
for code, lib in [
    ('K25.0','Ulcère de l’estomac, aigu, avec hémorragie'),
    ('K25.4','Ulcère de l’estomac, chronique ou non précisé, avec hémorragie'),
    ('K25.7','Ulcère de l’estomac, chronique, sans hémorragie ni perforation'),
    ('K26.1','Ulcère du duodénum, aigu, avec perforation'),
    ('K26.4','Ulcère du duodénum, chronique ou non précisé, avec hémorragie'),
    ('K26.5','Ulcère du duodénum, chronique ou non précisé, avec perforation'),
    ('K26.7','Ulcère du duodénum, chronique, sans hémorragie ni perforation'),
    ('K26.9','Ulcère du duodénum, non précisé comme aigu ou chronique, sans hémorragie ni perforation'),
    ('K27.9','Ulcère digestif de siège non précisé, non précisé comme aigu ou chronique, sans hémorragie ni perforation'),
    ('K28.7','Ulcère gastro-jéjunal, chronique, sans hémorragie ni perforation'),
    ('K63.3','Ulcère de l’intestin'),
    ('P78.8','Autres affections périnatales précisées de l’appareil digestif (dont l’ulcère gastroduodénal du nouveau-né)'),
    ('E16.4','Anomalies de la sécrétion de gastrine (dont le syndrome de Zollinger-Ellison)'),
]:
    a(code,[(code,'code CIM-10-GM 2024 : '+lib)],lib,'<p>Code de la CIM-10-GM 2024 (BfArM, bloc correspondant, consulté le 08.10.2026).</p>','k25-codes')
