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
    C.pop('k92-hematochezie', 'Hématochézie', L(('Définition', 'Émission par l’anus de sang rouge ou foncé, pur ou mêlé aux selles.'), ('Valeur', 'Elle oriente vers une source basse ; avec un choc, elle peut révéler une source haute à débit massif.'), ('Chiffre', '11 à 15 % des hémorragies crues basses ont une source haute (BSG 2019).')) + src(BSG19))
    C.pop('k92-mallory', 'Syndrome de Mallory-Weiss', L(('Lésion', 'Déchirure longitudinale de la muqueuse de la jonction œsogastrique.'), ('Contexte', 'Efforts de vomissement répétés, souvent après une prise d’alcool.'), ('Évolution', 'Le plus souvent spontanément favorable ; hémostase endoscopique si saignement actif.')) + src(ESGE21))
    C.pop('k92-dieulafoy', 'Lésion de Dieulafoy', L(('Lésion', 'Artère sous-muqueuse de gros calibre qui affleure à travers une petite perte de substance, sans ulcère autour.'), ('Siège', 'Le plus souvent dans l’estomac proximal.'), ('Piège', 'Elle peut passer inaperçue entre deux épisodes de saignement.')) + src(ESGE21))
    C.pop('k92-angiodysplasie', 'Angiodysplasie', L(('Lésion', 'Malformation vasculaire acquise de la muqueuse, faite de capillaires et de veinules dilatés.'), ('Terrain', 'Sujet âgé ; saignement indolore, souvent récidivant.'), ('Siège', 'Côlon droit et grêle ; cause fréquente de saignement du grêle.')) + src(BSG19))
    C.pop('k92-diverticule', 'Saignement diverticulaire', L(('Mécanisme', 'Rupture d’une artériole au collet d’un diverticule colique.'), ('Fréquence', 'Première cause d’hémorragie basse au Royaume-Uni (BSG 2019).'), ('Évolution', 'Arrêt spontané le plus souvent ; récidive possible.')) + src(BSG19))
    C.pop('k92-fistule', 'Fistule aorto-digestive', L(('Contexte', 'Prothèse aortique ou anévrisme de l’aorte.'), ('Tableau', 'Petit saignement « sentinelle » suivi d’une hémorragie massive.'), ('Conduite', 'Angio-tomodensitométrie et avis chirurgical vasculaire immédiat ; une des rares indications de chirurgie sans localisation préalable (BSG 2019).')) + src(BSG19))
    C.pop('k92-tranexamique', 'Acide tranexamique', L(('Recommandation', 'Non recommandé dans l’hémorragie haute non variqueuse (ESGE 2021, énoncé 9) ni dans l’hémorragie variqueuse (Baveno VII).'), ('Preuve', 'Essai HALT-IT : mortalité par hémorragie à 5 jours de 4 % sous acide tranexamique comme sous placebo (RR 0,99) ; davantage d’événements thromboemboliques veineux.')) + src(ESGE21, BAV7))
    C.pop('k92-pfc', 'Plasma frais congelé', L(('Dans la cirrhose', 'Déconseillé dans l’hémorragie variqueuse : il ne corrige pas l’hémostase et augmente la volémie et la pression portale (Baveno VII, énoncés 6.35 et 6.36).'), ('Piège', 'L’INR du cirrhotique ne mesure pas son risque hémorragique.')) + src(BAV7))
    C.pop('k92-adrenaline', 'Injection d’adrénaline', L(('Technique', 'Injection sous-muqueuse d’adrénaline diluée autour du point de saignement.'), ('Mécanisme', 'Vasoconstriction et compression locale, effet transitoire.'), ('Règle', 'Jamais seule pour un saignement actif : toujours associée à une méthode thermique de contact ou mécanique (ESGE 2021).')) + src(ESGE21))
    C.pop('k92-otsc', 'Clip monté sur capuchon', L(('Principe', 'Grand clip monté sur un capuchon à l’extrémité de l’endoscope, qui prend une large épaisseur de paroi.'), ('Indications', 'Première intention à envisager pour les ulcères à haut risque ; saignement persistant ; récidive après hémostase (ESGE 2021, énoncés 17 et 6).')) + src(ESGE21))
    C.pop('k92-embolisation', 'Embolisation artérielle', L(('Principe', 'Occlusion par voie endovasculaire de l’artère qui saigne, repérée par angiographie.'), ('Place haute', 'Après échec d’une seconde hémostase endoscopique, avant la chirurgie (ESGE 2021).'), ('Place basse', 'Après une angio-tomodensitométrie positive, dans les 60 minutes dans un centre équipé (BSG 2019).')) + src(ESGE21, BSG19))
    C.pop('k92-cyanoacrylate', 'Colle tissulaire (cyanoacrylate)', L(('Principe', 'Injection de N-butyl-cyanoacrylate qui polymérise au contact du sang et obture la varice.'), ('Indication', 'Varices gastriques isolées et varices œsogastriques de type 2 (Baveno VII, énoncé 6.22).'), ('Risque', 'Embolie de colle, rare.')) + src(BAV7, ESGE22))
    C.pop('k92-tamponnement', 'Ballon de tamponnement et prothèse œsophagienne', L(('Principe', 'Compression mécanique des varices par un ballon ou une prothèse métallique couverte.'), ('Place', 'Pont temporaire vers un TIPS de sauvetage en cas d’hémorragie réfractaire (Baveno VII).'), ('Limite', 'Ballon : complications fréquentes, durée limitée.')) + src(BAV7))
    C.pop('k92-lactulose', 'Lactulose', L(('Mécanisme', 'Disaccharide non absorbé ; accélère le transit et acidifie le côlon, ce qui réduit l’absorption d’ammoniac.'), ('Place', 'Évacuer le sang digestif et prévenir l’encéphalopathie après une hémorragie variqueuse (Baveno VII, énoncé 6.33).')) + src(BAV7))
    C.pop('k92-bbns', 'Bêtabloquants non sélectifs', L(('Molécules', 'Propranolol, nadolol, carvédilol.'), ('Mécanisme', 'Baisse du débit cardiaque et vasoconstriction splanchnique : la pression portale diminue.'), ('Place', 'Prophylaxie secondaire avec les ligatures après une hémorragie variqueuse (ESGE 2022, Baveno VII).')) + src(BAV7, ESGE22))
    C.pop('k92-gpvh', 'Gradient de pression veineuse hépatique', L(('Définition', 'Différence entre pression sus-hépatique bloquée et pression sus-hépatique libre ; reflet de la pression portale.'), ('Seuils', 'Au-delà de 10 mmHg : hypertension portale cliniquement significative ; au-delà de 20 mmHg pendant une hémorragie : critère de TIPS préemptif (Baveno VII).')) + src(BAV7))
    C.pop('k92-aod', 'Anticoagulants oraux directs', L(('Molécules', 'Apixaban, édoxaban, rivaroxaban (anti-Xa) ; dabigatran (antithrombine).'), ('Pendant l’hémorragie', 'Suspension ; antagonisation spécifique discutée en cas d’hémorragie menaçante.'), ('Reprise', 'Vers 7 jours selon le risque thromboembolique ; leur action est rapide (ESGE 2021, BSG 2019).')) + src(ESGE21, BSG19))
    C.pop('k92-baveno', 'Consensus de Baveno VII', L(('Nature', 'Conférence de consensus européenne sur l’hypertension portale (2022).'), ('Contenu', 'Définitions, stratification du risque, prophylaxie et traitement de l’hémorragie variqueuse aiguë (énoncés 6.1 à 6.38).')) + src(BAV7))
