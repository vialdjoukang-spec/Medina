# Termes interactifs du cours K92 et fenêtres supplémentaires (règle de précision et d'interactivité, 09.10.2026).
from medina_gen import src, lab as L
def ajouter(C, ESGE21, ESGE22, BAV7, BSG19, EASL18, FI):
    C.termes = [
     (r'hématochézie', 'k92-hematochezie'),
     (r'score de Glasgow-Blatchford|Glasgow-Blatchford', 'k92-gbs'),
     (r'score d’Oakland|Oakland', 'k92-oakland'),
     (r'classification de Forrest|Forrest (?:Ia|IIa)', 'k92-forrest'),
     (r'Child-Pugh', 'k92-child'), (r'\bMELD\b', 'k92-child'),
     (r'indice de choc', 'k92-hemodynamique'),
     (r'terlipressine', 'k92-d-terli'), (r'octréotide', 'k92-d-octreo'),
     (r'ceftriaxone', 'k92-antibioprophylaxie'),
     (r'érythromycine', 'k92-erythromycine'),
     (r'IPP', 'k92-d-ipp'), (r'pantoprazole', 'k92-d-ipp'),
     (r'ligature', 'k92-ligature'), (r'\bTIPS\b', 'k92-tips'),
     (r'angio-tomodensitométrie', 'k92-angiotdm'),
     (r'vidéocapsule', 'k92-capsule'),
     (r'Helicobacter pylori', 'k92-hp'),
     (r'syndrome de Mallory-Weiss', 'k92-mallory'),
     (r'lésion de Dieulafoy', 'k92-dieulafoy'),
     (r'angiodysplasie', 'k92-angiodysplasie'),
     (r'saignement diverticulaire|Diverticule', 'k92-diverticule'),
     (r'fistule aorto-digestive', 'k92-fistule'),
     (r'acide tranexamique', 'k92-tranexamique'),
     (r'plasma frais congelé', 'k92-pfc'),
     (r'adrénaline', 'k92-adrenaline'),
     (r'clip monté sur capuchon', 'k92-otsc'),
     (r'embolisation', 'k92-embolisation'),
     (r'colle tissulaire \(cyanoacrylate\)|cyanoacrylate', 'k92-cyanoacrylate'),
     (r'ballon de tamponnement', 'k92-tamponnement'),
     (r'lactulose', 'k92-lactulose'),
     (r'bêtabloquant non sélectif', 'k92-bbns'),
     (r'gradient de pression veineuse hépatique', 'k92-gpvh'),
     (r'anticoagulants? oraux directs', 'k92-aod'),
     (r'Baveno VII', 'k92-baveno'),
    ]
    C.pop('k92-hematochezie', 'Hématochézie', L(('Définition', 'L’hématochézie est l’émission par l’anus de sang rouge ou foncé, pur ou mêlé aux selles.'), ('Valeur', 'Elle oriente vers une source basse ; avec un choc, elle peut révéler une source haute à débit massif.'), ('Chiffre', 'Selon la BSG 2019, 11 à 15 % des hémorragies crues basses ont une source haute.')) + src(BSG19))
    C.pop('k92-mallory', 'Syndrome de Mallory-Weiss', L(('Lésion', 'Il s’agit d’une déchirure longitudinale de la muqueuse de la jonction œsogastrique.'), ('Contexte', 'Elle survient après des efforts de vomissement répétés, souvent après une prise d’alcool.'), ('Évolution', 'Elle guérit le plus souvent spontanément ; une hémostase endoscopique n’est nécessaire qu’en cas de saignement actif.')) + src(ESGE21))
    C.pop('k92-dieulafoy', 'Lésion de Dieulafoy', L(('Lésion', 'Il s’agit d’une artère sous-muqueuse de gros calibre qui affleure à travers une petite perte de substance, sans ulcère autour.'), ('Siège', 'Elle siège le plus souvent dans l’estomac proximal.'), ('Piège', 'Elle peut passer inaperçue entre deux épisodes de saignement.')) + src(ESGE21))
    C.pop('k92-angiodysplasie', 'Angiodysplasie', L(('Lésion', 'C’est une malformation vasculaire acquise de la muqueuse, faite de capillaires et de veinules dilatés.'), ('Terrain', 'Elle touche le sujet âgé et saigne de façon indolore, souvent récidivante.'), ('Siège', 'Elle siège dans le côlon droit et le grêle, où elle cause souvent des saignements.')) + src(BSG19))
    C.pop('k92-diverticule', 'Saignement diverticulaire', L(('Mécanisme', 'Une artériole se rompt au collet d’un diverticule colique.'), ('Fréquence', 'C’est la première cause d’hémorragie basse au Royaume-Uni (BSG 2019).'), ('Évolution', 'Le saignement s’arrête le plus souvent spontanément, mais il peut récidiver.')) + src(BSG19))
    C.pop('k92-fistule', 'Fistule aorto-digestive', L(('Contexte', 'Elle survient chez un patient porteur d’une prothèse aortique ou d’un anévrisme de l’aorte.'), ('Tableau', 'Un petit saignement « sentinelle » précède une hémorragie massive.'), ('Conduite', 'Une angio-tomodensitométrie et un avis chirurgical vasculaire s’imposent immédiatement ; c’est l’une des rares indications de chirurgie sans localisation préalable (BSG 2019).')) + src(BSG19))
    C.pop('k92-tranexamique', 'Acide tranexamique', L(('Recommandation', 'Il n’est pas recommandé dans l’hémorragie haute non variqueuse (ESGE 2021, énoncé 9), ni dans l’hémorragie variqueuse (Baveno VII).'), ('Preuve', 'Dans l’essai HALT-IT, la mortalité par hémorragie à 5 jours était de 4 % sous acide tranexamique comme sous placebo (RR 0,99), alors que les événements thromboemboliques veineux étaient plus nombreux.')) + src(ESGE21, BAV7))
    C.pop('k92-pfc', 'Plasma frais congelé', L(('Dans la cirrhose', 'Il est déconseillé dans l’hémorragie variqueuse, car il ne corrige pas l’hémostase et augmente la volémie et la pression portale (Baveno VII, énoncés 6.35 et 6.36).'), ('Piège', 'L’INR du cirrhotique ne mesure pas son risque hémorragique.')) + src(BAV7))
    C.pop('k92-adrenaline', 'Injection d’adrénaline', L(('Technique', 'L’endoscopiste injecte de l’adrénaline diluée dans la sous-muqueuse autour du point de saignement.'), ('Mécanisme', 'Elle agit par vasoconstriction et par compression locale, mais son effet est transitoire.'), ('Règle', 'Elle ne s’utilise jamais seule pour un saignement actif ; elle s’associe toujours à une méthode thermique de contact ou mécanique (ESGE 2021).')) + src(ESGE21))
    C.pop('k92-otsc', 'Clip monté sur capuchon', L(('Principe', 'Un grand clip monté sur un capuchon à l’extrémité de l’endoscope saisit une large épaisseur de paroi.'), ('Indications', 'On peut l’envisager en première intention pour les ulcères à haut risque, et il sert en cas de saignement persistant ou de récidive après hémostase (ESGE 2021, énoncés 17 et 6).')) + src(ESGE21))
    C.pop('k92-embolisation', 'Embolisation artérielle', L(('Principe', 'Le radiologue occlut par voie endovasculaire l’artère qui saigne, repérée par angiographie.'), ('Place haute', 'Elle se discute après l’échec d’une seconde hémostase endoscopique, avant la chirurgie (ESGE 2021).'), ('Place basse', 'Elle suit une angio-tomodensitométrie positive, dans les 60 minutes dans un centre équipé (BSG 2019).')) + src(ESGE21, BSG19))
    C.pop('k92-cyanoacrylate', 'Colle tissulaire (cyanoacrylate)', L(('Principe', 'On injecte du N-butyl-cyanoacrylate, qui polymérise au contact du sang et obture la varice.'), ('Indication', 'Elle traite les varices gastriques isolées et les varices œsogastriques de type 2 (Baveno VII, énoncé 6.22).'), ('Risque', 'Une embolie de colle peut survenir, mais elle est rare.')) + src(BAV7, ESGE22))
    C.pop('k92-tamponnement', 'Ballon de tamponnement et prothèse œsophagienne', L(('Principe', 'Un ballon ou une prothèse métallique couverte comprime mécaniquement les varices.'), ('Place', 'Ils servent de pont temporaire vers un TIPS de sauvetage en cas d’hémorragie réfractaire (Baveno VII).'), ('Limite', 'Le ballon donne des complications fréquentes, et sa durée d’utilisation est limitée.')) + src(BAV7))
    C.pop('k92-lactulose', 'Lactulose', L(('Mécanisme', 'Disaccharide non absorbé ; accélère le transit et acidifie le côlon, ce qui réduit l’absorption d’ammoniac.'), ('Place', 'Évacuer le sang digestif et prévenir l’encéphalopathie après une hémorragie variqueuse (Baveno VII, énoncé 6.33).')) + src(BAV7))
    C.pop('k92-bbns', 'Bêtabloquants non sélectifs', L(('Molécules', 'Les molécules sont le propranolol, le nadolol et le carvédilol.'), ('Mécanisme', 'Ils baissent le débit cardiaque et provoquent une vasoconstriction splanchnique ; ainsi, la pression portale diminue.'), ('Place', 'Ils s’associent aux ligatures en prophylaxie secondaire après une hémorragie variqueuse (ESGE 2022, Baveno VII).')) + src(BAV7, ESGE22))
    C.pop('k92-gpvh', 'Gradient de pression veineuse hépatique', L(('Définition', 'Le gradient est la différence entre la pression sus-hépatique bloquée et la pression sus-hépatique libre ; il reflète la pression portale.'), ('Seuils', 'Au-delà de 10 mmHg, il définit une hypertension portale cliniquement significative ; au-delà de 20 mmHg pendant une hémorragie, il constitue un critère de TIPS préemptif (Baveno VII).')) + src(BAV7))
    C.pop('k92-aod', 'Anticoagulants oraux directs', L(('Molécules', 'L’apixaban, l’édoxaban et le rivaroxaban inhibent le facteur Xa, alors que le dabigatran inhibe la thrombine.'), ('Pendant l’hémorragie', 'On les suspend, et l’on discute une antagonisation spécifique en cas d’hémorragie menaçante.'), ('Reprise', 'Ils reprennent vers 7 jours selon le risque thromboembolique, en tenant compte de leur action rapide (ESGE 2021, BSG 2019).')) + src(ESGE21, BSG19))
    C.pop('k92-baveno', 'Consensus de Baveno VII', L(('Nature', 'Il s’agit d’une conférence de consensus européenne sur l’hypertension portale, publiée en 2022.'), ('Contenu', 'Il définit les termes, stratifie le risque et fixe la prophylaxie et le traitement de l’hémorragie variqueuse aiguë (énoncés 6.1 à 6.38).')) + src(BAV7))
