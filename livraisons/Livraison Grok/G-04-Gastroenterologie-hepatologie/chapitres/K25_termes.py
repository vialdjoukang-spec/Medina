# Termes interactifs du cours K25 et fenêtres supplémentaires (règle de précision et d'interactivité, 09.10.2026).
from medina_gen import src, lab as L
from images import credit
def ajouter(C, SSI, S2K, ESGE21, WSES, FI):
    C.termes = [
     (r'musculaire muqueuse', 'k25-musculaire'),
     (r'Helicobacter pylori', 'k25-hp'),
     (r'AINS non sélectifs?', 'k25-ains'), (r'\bAINS\b', 'k25-ains'),
     (r'coxibs?\b|Coxib\b', 'k25-coxib'),
     (r'\bISRS\b', 'k25-isrs'),
     (r'inhibiteurs? de P2Y12', 'k25-p2y12'),
     (r'score de Glasgow-Blatchford', 'k25-gbs'),
     (r'classification de Forrest', 'k25-forrest'),
     (r'scores de Boey, PULP et ASA', 'k25-scores-perforation'),
     (r'hypoalbuminémie', 'k25-scores-perforation'),
     (r'sténose', 'k25-stenose'),
     (r'test respiratoire(?: à l’urée marquée)?', 'k25-test-respiratoire'),
     (r'culture', 'k25-culture'),
     (r'sérologie', 'k25-serologie'),
     (r'Pylera®', 'k25-d-pylera'),
     (r'amoxicilline', 'k25-d-amox'), (r'clarithromycine', 'k25-d-clari'), (r'lévofloxacine', 'k25-d-levo'),
     (r'métronidazole', 'k25-metronidazole'),
     (r'ésoméprazole', 'k25-d-ipp'), (r'\bIPP\b', 'k25-d-ipp'),
     (r'40 mg une fois par jour pendant 4 à 8 semaines', 'k25-d-ipp'),
     (r'cellule pariétale', 'k25-cellule-parietale'),
     (r'gastrine', 'k25-gastrine'),
     (r'ulcères de stress', 'k25-stress'),
     (r'tomodensitométrie', 'k25-tdm'),
     (r'antivitamines? K', 'k25-avk'),
     (r'traitement non opératoire', 'k25-nom'),
     (r'suture simple', 'k25-chirurgie-perforation'),
     (r'trithérapie', 'k25-trithérapie'),
     (r'quadrithérapie bismuthée', 'k25-bqt'),
     (r'CYP3A4', 'k25-d-clari'),
     (r'hypomagnésémie', 'k25-ipp-long-cours'),
     (r'uréase', 'k25-test-respiratoire'),
     (r'ARN ribosomique 23S', 'k25-pcr-resistance'),
     (r'ANRESIS', 'k25-anresis'),
    ]
    C.pop('k25-musculaire', 'Musculaire muqueuse', L(('Définition', 'La musculaire muqueuse est une fine couche de muscle lisse qui sépare la muqueuse de la sous-muqueuse.'), ('Valeur', 'C’est la frontière histologique entre érosion (au-dessus) et ulcère (au-delà).'), ('Conséquence', 'La sous-muqueuse contient les artères de calibre suffisant pour une hémorragie grave.')))
    C.pop('k25-hp', 'Helicobacter pylori', L(('Agent', 'C’est un bacille à Gram négatif, spiralé et microaérophile, qui colonise le mucus gastrique.'), ('Effets', 'Il provoque toujours une gastrite chronique, puis parfois un ulcère gastrique ou duodénal, une atrophie, une métaplasie, un cancer gastrique ou un lymphome du MALT.'), ('Conduite', 'On le recherche chez tout ulcéreux, on le traite selon la résistance et on contrôle la guérison (SSI 2026).')) + src(SSI))
    C.pop('k25-ains', 'AINS non sélectifs', L(('Mécanisme', 'Les AINS inhibent les cyclo-oxygénases 1 et 2 et baissent ainsi les prostaglandines qui protègent la muqueuse.'), ('Risque', 'Ils causent souvent des ulcères et des hémorragies, qui restent fréquemment silencieux jusqu’à la complication (S2k 2023, énoncé 7.1).'), ('Prévention', 'IPP si un facteur de risque supplémentaire est présent (recommandation 7.5) ; IPP au long cours après une complication si l’AINS est poursuivi (7.8).')) + src(S2K))
    C.pop('k25-coxib', 'Coxibs', L(('Définition', 'Les coxibs sont des AINS sélectifs de la cyclo-oxygénase 2, par exemple le célécoxib.'), ('Avantage', 'Ils provoquent moins d’ulcères et d’hémorragies que les AINS non sélectifs, car ils épargnent la cyclo-oxygénase 1 de la muqueuse.'), ('Prophylaxie', 'On ajoute un IPP si un facteur de risque supplémentaire existe, et toujours si une aspirine, un inhibiteur de P2Y12, un anticoagulant ou un ISRS est associé (S2k 2023, recommandation 7.6).')) + src(S2K))
    C.pop('k25-isrs', 'ISRS et risque hémorragique', L(('Mécanisme', 'Les plaquettes ne captent plus la sérotonine ; l’agrégation diminue.'), ('Prophylaxie', 'On donne un IPP en cas d’antécédent d’ulcère ou d’association à un AINS, à un coxib ou à un inhibiteur de P2Y12 ; avec un anticoagulant, il reste discutable (S2k 2023, recommandation 7.13).')) + src(S2K))
    C.pop('k25-p2y12', 'Inhibiteurs de P2Y12', L(('Molécules', 'Ce sont le clopidogrel, le prasugrel et le ticagrélor.'), ('Risque digestif', 'Ils augmentent le risque de complication ulcéreuse (S2k 2023, énoncé 7.4).'), ('Après une hémorragie sous P2Y12 seul', 'Le patient reçoit un IPP au long cours ; un passage à l’aspirine peut être discuté si le cardiologue l’accepte (recommandation 7.11).')) + src(S2K))
    C.pop('k25-gbs', 'Score de Glasgow-Blatchford', L(('Composantes', 'Le score combine l’urée, l’hémoglobine, la pression systolique, la fréquence cardiaque, le méléna, la syncope, l’hépatopathie et l’insuffisance cardiaque.'), ('Seuil', 'Un score ≤ 1 signale un très faible risque et permet une prise en charge ambulatoire (ESGE 2021).'), ('Renvoi', 'Le cours K92 — Hémorragies digestives le détaille.')) + src(ESGE21))
    C.pop('k25-forrest', 'Classification de Forrest', L(('Stades', 'Le stade Ia correspond à un saignement en jet, Ib à un suintement, IIa à un vaisseau visible, IIb à un caillot adhérent, IIc à une tache pigmentée et III à un fond propre.'), ('Conduite', 'Les stades Ia, Ib et IIa reçoivent une hémostase endoscopique, car ils resaignent souvent ; au stade IIb, on envisage de retirer le caillot ; les stades IIc et III n’en reçoivent pas (ESGE 2021).')) + src(ESGE21))
    C.pop('k25-scores-perforation', 'Scores de risque de l’ulcère perforé', L(('Boey', 'Le score de Boey compte trois items : comorbidité grave, choc à l’admission et délai de plus de 24 heures ; il est le plus utilisé, mais sa précision varie.'), ('PULP et ASA', 'Les scores PULP et ASA prédisent la mortalité aussi bien l’un que l’autre et mieux que le score de Boey.'), ('Meilleur facteur isolé', 'L’hypoalbuminémie est le meilleur facteur isolé (WSES 2020), car elle reflète la dénutrition et la gravité.')) + src(WSES))
    C.pop('k25-stenose', 'Sténose ulcéreuse', L(('Mécanisme', 'Un œdème inflammatoire, puis une fibrose cicatricielle rétrécissent la région pyloroduodénale.'), ('Clinique', 'Le patient présente des vomissements alimentaires tardifs, un clapotage à jeun et un amaigrissement.'), ('Démarche', 'On fait une endoscopie avec biopsies pour exclure un cancer, puis on traite la cause et on donne un IPP ; si la sténose persiste, on la dilate ou on opère.')) + src(S2K) + C.img('k25_ulcere_pylorique_macro.gif', 'Pièce opératoire : estomac dilaté en amont d’une sténose pylorique ulcéreuse.', 'L’estomac se dilate en amont du pylore rétréci par la fibrose ; c’est pourquoi le patient vomit des aliments ingérés plusieurs heures auparavant.', credit({'auteur': 'Narraburra', 'licence': 'CC0', 'url': 'https://commons.wikimedia.org/wiki/File:Gross_stomach_enlargement,_pyloric_obstruction,_chronic_pyloric_ulcer.jpg'})))
    C.pop('k25-test-respiratoire', 'Test respiratoire à l’urée marquée', L(('Principe', 'L’uréase bactérienne scinde l’urée marquée au carbone 13 ; le CO₂ marqué est mesuré dans l’air expiré.'), ('Performance', 'Sa sensibilité et sa spécificité sont de 90 à 95 % (SSI).'), ('Statut en Suisse', 'La SSI 2026 ne le recommande pas en routine, car il exige un personnel formé et un laboratoire équipé et ne donne aucune information sur la résistance.')) + src(SSI))
    C.pop('k25-culture', 'Culture de Helicobacter pylori', L(('Prélèvement', 'On cultive des biopsies gastriques prises pendant l’endoscopie.'), ('Valeur', 'La culture est la référence de l’antibiogramme, y compris pour le métronidazole.'), ('Limite', 'Sa sensibilité varie de 75 à 91 % selon l’expérience du laboratoire (SSI).')) + src(SSI))
    C.pop('k25-serologie', 'Sérologie de Helicobacter pylori', L(('Principe', 'La sérologie recherche des anticorps IgG.'), ('Limite', 'Elle ne distingue pas une infection active d’une infection guérie, car les anticorps persistent ; elle est donc inutile pour contrôler l’éradication.'), ('Statut', 'La SSI 2026 ne la recommande pas.')) + src(SSI))
    C.pop('k25-metronidazole', 'Métronidazole', L(('Place', 'Il fait partie de Pylera® ; en trithérapie, on ne l’utilise que si la souche est sensible.'), ('Résistance', 'La résistance est élevée : 44 % dans les données suisses ANRESIS citées par la SSI.'), ('Précautions', 'Il provoque un effet antabuse, donc le patient évite l’alcool jusqu’à 24 heures après la fin ; il potentialise aussi les antivitamines K (information professionnelle Pylera®).')) + src(SSI, FI('Pylera®')))
    C.pop('k25-cellule-parietale', 'Cellule pariétale', L(('Siège', 'Elle siège dans les glandes du fundus et du corps gastrique.'), ('Fonction', 'Elle sécrète l’acide chlorhydrique par la pompe H⁺/K⁺-ATPase et le facteur intrinsèque.'), ('Régulation', 'L’histamine (récepteur H2), la gastrine et l’acétylcholine la stimulent, alors que la somatostatine la freine.')))
    C.pop('k25-gastrine', 'Gastrine', L(('Origine', 'Elle est produite par les cellules G de l’antre gastrique.'), ('Effet', 'Elle stimule la sécrétion acide directement et par la libération d’histamine.'), ('Pathologie', 'Elle est élevée dans la gastrite antrale à Helicobacter pylori et, très fortement, dans le gastrinome.')))
    C.pop('k25-stress', 'Ulcères de stress', L(('Mécanisme', 'La muqueuse est mal perfusée au cours des maladies graves ; elle perd donc sa défense.'), ('Facteurs indépendants', 'Les troubles de la coagulation et une ventilation mécanique de plus de 48 heures sont les facteurs de risque indépendants.'), ('Prévention', 'Le patient de soins intensifs à haut risque reçoit un IPP (S2k 2023, recommandation 7.18).')) + src(S2K))
    C.pop('k25-tdm', 'Tomodensitométrie de l’ulcère perforé', L(('Signes', 'La tomodensitométrie montre un pneumopéritoine, du liquide intrapéritonéal, un épaississement pariétal, une infiltration de la graisse ou une fuite de contraste hydrosoluble.'), ('Valeur', 'Elle est plus sensible que la radiographie, situe la perforation et écarte d’autres causes.'), ('Limite', 'Jusqu’à 12 % des perforations ont un examen normal (WSES 2020).')) + src(WSES))
    C.pop('k25-avk', 'Antivitamines K et éradication', L(('Interaction', 'Le métronidazole et l’oméprazole potentialisent l’acénocoumarol et la phenprocoumone.'), ('Conduite', 'Contrôler le temps de prothrombine pendant le traitement et adapter la dose (information professionnelle Pylera®).')) + src(FI('Pylera®')))
    C.pop('k25-nom', 'Traitement non opératoire de l’ulcère perforé', L(('Conditions', 'Le patient doit être stable, sans péritonite ni sepsis, et la perforation doit être colmatée sur l’étude au contraste hydrosoluble.'), ('Risque', 'Environ 28 % des patients échouent à 12 heures dans l’essai randomisé cité par la WSES, et la réponse est moins bonne après 70 ans.'), ('Statut', 'La WSES 2020 ne le recommande pas en routine.')) + src(WSES))
    C.pop('k25-ipp-long-cours', 'IPP au long cours : effets indésirables', L(('Hypomagnésémie', 'Elle survient après au moins 3 mois, le plus souvent après un an, et peut entraîner une hypocalcémie et une hypokaliémie.'), ('Fractures', 'Le risque augmente modérément (hanche, poignet, rachis) après plus d’un an à dose élevée.'), ('Infections', 'Les infections digestives sont un peu plus fréquentes, car l’acide ne détruit plus les germes ingérés.'), ('Conduite', 'On réévalue l’indication et l’on arrête l’IPP si elle n’existe plus.')) + src(FI('Nexium®')))
    C.pop('k25-anresis', 'ANRESIS', L(('Définition', 'ANRESIS est le centre suisse de surveillance de la résistance aux antibiotiques.'), ('Données Helicobacter pylori', 'La résistance atteint 28 % pour la clarithromycine, 18 % pour la lévofloxacine, 44 % pour le métronidazole, 3 % pour l’amoxicilline et 4 % pour la tétracycline, surtout après un échec thérapeutique (SSI 2026).')) + src(SSI))
