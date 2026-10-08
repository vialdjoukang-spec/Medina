from cardio_1 import a, G
from cardio_2 import t
# K57 — Diverticulose et diverticulite (G-04-Gastroentérologie et hépatologie) : clés propres au cours, absentes des glossaires canoniques au 08.10.2026.
# Dépendances : les clés WSES et G-04-Gastroentérologie sont déjà définies dans glossary/k25.py (même zone de travail) ; elles ne sont pas redéfinies ici.
# Collision possible : ESCP, ACG, AGA, ASCRS peuvent aussi être définies par d'autres cours G-04 (K35, K65, K92) ; garder une seule définition à l'intégration.

a('ESCP',[('E','European'),('S','Society of'),('C','Coloproctology'),('P','(Proctologie)')],'European Society of Coloproctology (Société européenne de coloproctologie)','<p>Société savante européenne de chirurgie colorectale ; elle a publié en 2020 les recommandations sur la maladie diverticulaire du côlon (Schultz et al., Colorectal Disease 2020, 38 énoncés).</p>','k57-abces')
a('ACG',[('A','American'),('C','College of'),('G','Gastroenterology')],'American College of Gastroenterology (Collège américain de gastroentérologie)','<p>Société savante nord-américaine ; recommandation clinique sur la diverticulite colique publiée en juillet 2026 (Peery et al., American Journal of Gastroenterology).</p>','k57-sansab')
a('AGA',[('A','American'),('G','Gastroenterological'),('A','Association')],'American Gastroenterological Association (Association américaine de gastroentérologie)','<p>Société savante nord-américaine ; mise au point de pratique clinique sur le traitement médical de la diverticulite (Peery, Shaukat et Strate, Gastroenterology 2021).</p>')
a('ASCRS',[('A','American'),('S','Society of'),('C','Colon and'),('R','Rectal'),('S','Surgeons')],'American Society of Colon and Rectal Surgeons (Société américaine des chirurgiens du côlon et du rectum)','<p>Société savante nord-américaine ; recommandations 2020 sur la diverticulite du côlon gauche (Hall et al., Diseases of the Colon and Rectum).</p>','k57-abces')
a('CDD',[('C','Classification of'),('D','Diverticular'),('D','Disease')],'Classification of Diverticular Disease (classification de la maladie diverticulaire)','<p>Classification en types 0 à 4 employée par la recommandation allemande de 2021 sur la maladie diverticulaire.</p>','k57-cdd')
a('DGVS',[('D','Deutsche'),('G','Gesellschaft für'),('V','Verdauungs- und'),('S','Stoffwechselkrankheiten')],'Société allemande des maladies digestives et métaboliques','<p>Société savante allemande de gastroentérologie, coéditrice de la recommandation de 2021 sur la maladie diverticulaire (registre AWMF 021-020).</p>','k57-cdd')
a('DGAV',[('D','Deutsche'),('G','Gesellschaft für'),('A','Allgemein- und'),('V','Viszeralchirurgie')],'Société allemande de chirurgie générale et viscérale','<p>Société savante allemande de chirurgie viscérale, coéditrice de la recommandation de 2021 sur la maladie diverticulaire.</p>','k57-cdd')

t('AVOD',[('AVOD','nom d’essai suédois (antibiotiques dans la diverticulite non compliquée) ; développement officiel lettre à lettre non retrouvé dans les sources consultées')],'Essai AVOD (2012)','<p>Essai randomisé suédois et islandais de 623 patients : l’antibiotique n’a ni accéléré la guérison ni prévenu les complications de la diverticulite non compliquée (Chabok et al., British Journal of Surgery 2012).</p>','k57-avod')
t('DIABOLO',[('DIABOLO','nom d’essai arrangé à partir de « DIverticulitis: AntiBiotics Or cLose Observation », non strictement lettre à lettre')],'Essai DIABOLO (2017)','<p>Essai randomisé néerlandais de 528 patients : l’observation sans antibiotique n’a pas prolongé la guérison d’un premier épisode de diverticulite non compliquée (Daniels et al., British Journal of Surgery 2017).</p>','k57-diabolo')
t('DINAMO',[('DINAMO','nom d’essai espagnol (diverticulite légère traitée en ambulatoire sans antibiotique) ; développement officiel lettre à lettre non retrouvé dans les sources consultées')],'Essai DINAMO (2021)','<p>Essai randomisé espagnol de 480 patients : le traitement ambulatoire sans antibiotique de la diverticulite légère n’a pas été inférieur au traitement par amoxicilline-acide clavulanique (Mora López et al., Annals of Surgery 2021).</p>','k57-dinamo')
t('LADIES',[('LADIES','nom d’essai arrangé à partir de « LAparoscopic peritoneal lavage or resection for generalised peritonitis for DIvErticulitiS », non strictement lettre à lettre')],'Essai LADIES (2019)','<p>Essai randomisé : dans la péritonite diverticulaire Hinchey III ou IV du patient stable, l’anastomose primaire a donné une meilleure survie sans stomie que l’intervention de Hartmann (Lambrichts et al., Lancet Gastroenterology and Hepatology 2019).</p>','k57-hartmann')
t('SCANDIV',[('SCAN','SCANdinavian (scandinave)'),('DIV','DIVerticulitis trial (essai sur la diverticulite)')],'Essai SCANDIV (Scandinavian Diverticulitis trial)','<p>Essai randomisé suédois et norvégien comparant lavage laparoscopique et résection dans la diverticulite perforée purulente ; résultats à cinq ans publiés en 2021 (Azhar et al., JAMA Surgery).</p>','k57-lavage')
t('LASER',[('LA','LAparoscopic (laparoscopique)'),('S','Sigmoid (du sigmoïde)'),('E','Elective (élective)'),('R','Resection following diverticulitis (résection après diverticulite)')],'Essai LASER (Laparoscopic Elective Sigmoid Resection following diverticulitis)','<p>Essai randomisé finlandais de 90 patients comparant sigmoïdectomie laparoscopique élective et traitement conservateur ; résultats publiés en 2021, 2023 et 2025 (Santos et al., JAMA Surgery).</p>','k57-laser')
t('PREVENT1',[('PREVENT','nom d’essai (prévenir la récidive de diverticulite), non développable lettre à lettre'),('1','premier des deux essais jumeaux')],'Essai PREVENT1 (2014)','<p>Essai de phase 3 de 590 patients : la mésalazine n’a pas prévenu la récidive de diverticulite par rapport au placebo (Raskin et al., Gastroenterology 2014).</p>','k57-prevent')
t('PREVENT2',[('PREVENT','nom d’essai (prévenir la récidive de diverticulite), non développable lettre à lettre'),('2','second des deux essais jumeaux')],'Essai PREVENT2 (2014)','<p>Essai de phase 3 de 592 patients, jumeau de PREVENT1 : la mésalazine n’a pas fait mieux que le placebo (Raskin et al., Gastroenterology 2014).</p>','k57-prevent')
t('STOP-IT',[('STOP','Study to Optimize Peritoneal infection'),('IT','Therapy (essai d’optimisation du traitement des infections péritonéales), nom arrangé, non strictement lettre à lettre')],'Essai STOP-IT (2015)','<p>Essai randomisé : après contrôle de la source d’une infection intra-abdominale compliquée, environ quatre jours d’antibiotique n’ont pas été inférieurs à une durée plus longue (Sawyer et al., New England Journal of Medicine 2015).</p>','k57-stopit')

# Codes CIM-10-GM 2024 à décimale (vérifiés sur klassifikationen.bfarm.de, bloc K55–K64, le 08.10.2026)
_K57 = {
 'K57.0':'Maladie diverticulaire de l’intestin grêle avec perforation et abcès',
 'K57.1':'Maladie diverticulaire de l’intestin grêle sans perforation ni abcès',
 'K57.2':'Maladie diverticulaire du côlon avec perforation et abcès',
 'K57.3':'Maladie diverticulaire du côlon sans perforation ni abcès',
 'K57.4':'Maladie diverticulaire de l’intestin grêle et du côlon avec perforation et abcès',
 'K57.5':'Maladie diverticulaire de l’intestin grêle et du côlon sans perforation ni abcès',
 'K57.8':'Maladie diverticulaire de l’intestin, siège non précisé, avec perforation et abcès',
 'K57.9':'Maladie diverticulaire de l’intestin, siège non précisé, sans perforation ni abcès',
 'K57.22':'Diverticulite du côlon avec perforation et abcès, sans indication de saignement',
 'K57.30':'Diverticulose du côlon sans perforation ni abcès, sans indication de saignement',
 'K57.31':'Diverticulose du côlon sans perforation ni abcès, avec saignement',
 'K57.32':'Diverticulite du côlon sans perforation ni abcès, sans indication de saignement',
 'K38.2':'Diverticule de l’appendice (exclu de K57)',
 'Q43.0':'Diverticule de Meckel (exclu de K57)',
 'Q43.8':'Autres malformations congénitales précisées de l’intestin, dont le diverticule congénital (exclu de K57)',
}
for _c, _l in _K57.items():
    a(_c, [(_c, 'code de la CIM-10-GM 2024')], _c + ' — ' + _l, '<p>' + _l + ' (CIM-10-GM 2024, BfArM).</p>', 'k57-cim')
