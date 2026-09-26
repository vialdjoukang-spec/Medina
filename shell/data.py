WAVES=[(1,"Cœur et hémodynamique",56),(2,"Poumon, plèvre et ventilation",64),(3,"Rein, eau et électrolytes",27),
(4,"Métabolisme, diabète et nutrition · Glandes endocrines",77),(5,"Tube digestif et péritoine · Foie · Pancréas et voies biliaires",102),
(6,"Système nerveux",120),(7,"Microorganismes, hôte et sites infectieux",155),(8,"Sang, moelle et hémostase · Oncologie",85),
(9,"Vaisseaux · Immunité, allergie et inflammation",31),(10,"Appareil locomoteur",157),(11,"Grossesse, naissance · Organes génitaux féminins · Sein",125),
(12,"Nouveau-né · Développement et génétique",72),(13,"Voies urinaires et génital masculin",52),(14,"Peau et annexes",89),
(15,"Œil · ORL · Bouche et maxillaires",136),(16,"Traumatismes · Toxiques et intoxications · Circonstances externes",153),
(17,"Présentation clinique · Prévention et parcours · Codes additionnels",135)]
PRIO={1,2,3,4,5,6,7,8,9,11,12}
DONE_SYS={1}
RENVOIS={1:[("A43","Nocardiose","traitée en infectiologie (vague 7)"),("I51","Complications et maladies cardiaques mal définies","renvois vers les cours I50, I42, I21"),
("I52","Atteintes cardiaques au cours de maladies classées ailleurs","renvois vers les cours concernés"),("R00","Anomalies du rythme cardiaque (symptôme)","sémiologie, vague 17"),
("R01","Souffles et autres bruits cardiaques","sémiologie, vague 17"),("R02","Gangrène, non classée ailleurs","sémiologie, vague 17"),("R03","Valeur tensionnelle anormale sans diagnostic","sémiologie, vague 17")]}
NOTES={"I00":"19,5/20","I40":"19,25/20"}

# Plan de production par système (ordre du prompt de passation, § 9) — sert au bouton directeur de l'accueil
PLAN={
1:["Insuffisance cardiaque","Syndromes coronariens aigus","Coronaropathie chronique","Fibrillation et flutter auriculaires","Hypertension artérielle","Troubles de conduction","Tachycardies","Arrêt cardiaque","Valvulopathie aortique","Valvulopathies mitrale et tricuspide","Endocardite infectieuse","Péricardites","Myocardites","Cardiomyopathies","Autres arythmies","Cardiopathies congénitales","Rhumatisme articulaire aigu"],
2:["Asthme","BPCO","Pneumonies","Embolie pulmonaire","Grippe et viroses respiratoires","Insuffisance respiratoire aiguë et SDRA","Épanchements pleuraux","Pneumothorax","Tuberculose","Cancer bronchique","Pneumopathies interstitielles","Sarcoïdose","Apnées du sommeil","Hypertension pulmonaire","Bronchectasies et mucoviscidose","Bronchite aiguë et bronchiolite","Pneumoconioses et hypersensibilité"],
7:["Sepsis et choc septique","Infections urinaires","Infections de la peau et des tissus mous","Méningites et encéphalites","VIH","Hépatites virales","Infections sexuellement transmissibles","Fièvre au retour de voyage et paludisme","Infections ostéo-articulaires","Clostridioides difficile","Borréliose et encéphalite à tiques","Fièvre chez l’immunodéprimé","Vaccinations de l’adulte","Antibiothérapie raisonnée"],
5:["Hémorragies digestives","Ulcère et Helicobacter pylori","Reflux","Pancréatites","Lithiase et infections biliaires","Cirrhose","Hépatopathies","Maladies inflammatoires intestinales","Diarrhées","Cancer colorectal","Abdomen aigu et appendicite","Diverticulite","Occlusion","Maladie cœliaque","Intestin irritable"],
6:["AVC et AIT","Épilepsies","Céphalées et hémorragie méningée","Démences","Maladie de Parkinson","Sclérose en plaques","Syndrome confusionnel","Neuropathies et Guillain-Barré","Myasthénie","Compressions médullaires","Vertiges"],
4:["Diabète de type 2","Diabète de type 1","Urgences glycémiques","Dyslipidémies","Obésité","Thyroïde","Ostéoporose","Calcium","Surrénales","Hypophyse","Dénutrition"],
3:["Insuffisance rénale aiguë","Maladie rénale chronique","Dysnatrémies","Dyskaliémies","Troubles acido-basiques","Glomérulopathies","Néphropathies diabétique et hypertensive","Polykystose"],
8:["Anémies","Thromboses et anticoagulation","Troubles de l’hémostase","Leucémies, lymphomes, myélome","Neutropénie fébrile","Thrombopénies","Oncologie générale et soins palliatifs"],
11:["Grossesse normale","Premier trimestre et grossesse extra-utérine","Prééclampsie et HELLP","Diabète gestationnel","Accouchement et post-partum","Contraception","Cycle et aménorrhées","Ménopause","Infections génitales","Endométriose","Cancers gynécologiques","Pathologies du sein"],
12:["Nouveau-né et adaptation","Ictère néonatal","Fièvre du nourrisson","Croissance et développement","Vaccinations de l’enfant","Déshydratation","Infections respiratoires de l’enfant","Convulsions fébriles","Maltraitance","Anomalies chromosomiques","Mort subite du nourrisson"],
9:["Artériopathie des membres inférieurs","Anévrisme et dissection aortique","Vascularites","Anaphylaxie et allergies","Lupus et connectivites","Arthrites inflammatoires","Déficits immunitaires"],
}
