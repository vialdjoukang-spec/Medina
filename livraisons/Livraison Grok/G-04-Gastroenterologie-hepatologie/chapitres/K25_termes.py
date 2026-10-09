# Termes interactifs du cours K25 et fenêtres supplémentaires (règle de précision et d'interactivité, 09.10.2026).
from medina_gen import src, lab as L
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
    C.pop('k25-musculaire', 'Musculaire muqueuse', L(('Définition', 'Fine couche de muscle lisse qui sépare la muqueuse de la sous-muqueuse.'), ('Valeur', 'C’est la frontière histologique entre érosion (au-dessus) et ulcère (au-delà).'), ('Conséquence', 'La sous-muqueuse contient les artères de calibre suffisant pour une hémorragie grave.')))
    C.pop('k25-hp', 'Helicobacter pylori', L(('Agent', 'Bacille à Gram négatif, spiralé, microaérophile, qui colonise le mucus gastrique.'), ('Effets', 'Gastrite chronique constante ; ulcère gastrique ou duodénal ; atrophie, métaplasie, cancer gastrique ; lymphome du MALT.'), ('Conduite', 'Recherche chez tout ulcéreux ; traitement guidé par la résistance ; contrôle de la guérison (SSI 2026).')) + src(SSI))
    C.pop('k25-ains', 'AINS non sélectifs', L(('Mécanisme', 'Inhibition des cyclo-oxygénases 1 et 2 ; baisse des prostaglandines protectrices de la muqueuse.'), ('Risque', 'Cause fréquente d’ulcère et d’hémorragie, souvent silencieuse jusqu’à la complication (S2k 2023, énoncé 7.1).'), ('Prévention', 'IPP si un facteur de risque supplémentaire est présent (recommandation 7.5) ; IPP au long cours après une complication si l’AINS est poursuivi (7.8).')) + src(S2K))
    C.pop('k25-coxib', 'Coxibs', L(('Définition', 'AINS sélectifs de la cyclo-oxygénase 2, par exemple le célécoxib.'), ('Avantage', 'Moins d’ulcères et d’hémorragies que les AINS non sélectifs.'), ('Prophylaxie', 'IPP si un facteur de risque supplémentaire ; toujours si aspirine, inhibiteur de P2Y12, anticoagulant ou ISRS associé (S2k 2023, recommandation 7.6).')) + src(S2K))
    C.pop('k25-isrs', 'ISRS et risque hémorragique', L(('Mécanisme', 'Les plaquettes ne captent plus la sérotonine ; l’agrégation diminue.'), ('Prophylaxie', 'IPP si antécédent d’ulcère ou association à un AINS, un coxib ou un inhibiteur de P2Y12 ; discutable avec un anticoagulant (S2k 2023, recommandation 7.13).')) + src(S2K))
    C.pop('k25-p2y12', 'Inhibiteurs de P2Y12', L(('Molécules', 'Clopidogrel, prasugrel, ticagrélor.'), ('Risque digestif', 'Facteur de risque de complication ulcéreuse (S2k 2023, énoncé 7.4).'), ('Après une hémorragie sous P2Y12 seul', 'IPP au long cours ; un passage à l’aspirine peut être discuté si le cardiologue l’accepte (recommandation 7.11).')) + src(S2K))
    C.pop('k25-gbs', 'Score de Glasgow-Blatchford', L(('Composantes', 'Urée, hémoglobine, pression systolique, fréquence cardiaque, méléna, syncope, hépatopathie, insuffisance cardiaque.'), ('Seuil', '≤ 1 : très faible risque, prise en charge ambulatoire possible (ESGE 2021).'), ('Renvoi', 'Détail dans le cours K92 — Hémorragies digestives.')) + src(ESGE21))
    C.pop('k25-forrest', 'Classification de Forrest', L(('Stades', 'Ia jet ; Ib suintement ; IIa vaisseau visible ; IIb caillot adhérent ; IIc tache pigmentée ; III fond propre.'), ('Conduite', 'Ia, Ib, IIa : hémostase endoscopique ; IIb : retrait du caillot envisagé ; IIc et III : pas d’hémostase (ESGE 2021).')) + src(ESGE21))
    C.pop('k25-scores-perforation', 'Scores de risque de l’ulcère perforé', L(('Boey', 'Trois items : comorbidité grave, choc à l’admission, délai de plus de 24 heures ; le plus utilisé, mais de précision variable.'), ('PULP et ASA', 'Prédisent la mortalité aussi bien l’un que l’autre et mieux que le score de Boey.'), ('Meilleur facteur isolé', 'L’hypoalbuminémie (WSES 2020).')) + src(WSES))
    C.pop('k25-stenose', 'Sténose ulcéreuse', L(('Mécanisme', 'Œdème inflammatoire puis fibrose cicatricielle de la région pyloroduodénale.'), ('Clinique', 'Vomissements alimentaires tardifs, clapotage à jeun, amaigrissement.'), ('Démarche', 'Endoscopie avec biopsies pour exclure un cancer ; traitement de la cause et IPP ; dilatation ou chirurgie si la sténose persiste.')) + src(S2K))
    C.pop('k25-test-respiratoire', 'Test respiratoire à l’urée marquée', L(('Principe', 'L’uréase bactérienne scinde l’urée marquée au carbone 13 ; le CO₂ marqué est mesuré dans l’air expiré.'), ('Performance', 'Sensibilité et spécificité de 90 à 95 % (SSI).'), ('Statut en Suisse', 'Non recommandé en routine par la SSI 2026 : personnel formé et laboratoire équipé nécessaires, aucune information sur la résistance.')) + src(SSI))
    C.pop('k25-culture', 'Culture de Helicobacter pylori', L(('Prélèvement', 'Biopsies gastriques prises pendant l’endoscopie.'), ('Valeur', 'Référence de l’antibiogramme, y compris pour le métronidazole.'), ('Limite', 'Sensibilité de 75 à 91 % selon l’expérience du laboratoire (SSI).')) + src(SSI))
    C.pop('k25-serologie', 'Sérologie de Helicobacter pylori', L(('Principe', 'Recherche d’anticorps IgG.'), ('Limite', 'Ne distingue pas une infection active d’une infection guérie ; inutile pour contrôler l’éradication.'), ('Statut', 'Non recommandée par la SSI 2026.')) + src(SSI))
    C.pop('k25-metronidazole', 'Métronidazole', L(('Place', 'Composant de Pylera® ; trithérapie possible seulement si la souche est sensible.'), ('Résistance', 'Élevée : 44 % dans les données suisses ANRESIS citées par la SSI.'), ('Précautions', 'Effet antabuse (pas d’alcool jusqu’à 24 heures après la fin) ; potentialisation des antivitamines K (information professionnelle Pylera®).')) + src(SSI, FI('Pylera®')))
    C.pop('k25-cellule-parietale', 'Cellule pariétale', L(('Siège', 'Glandes du fundus et du corps gastrique.'), ('Fonction', 'Sécrétion d’acide chlorhydrique par la pompe H⁺/K⁺-ATPase et de facteur intrinsèque.'), ('Régulation', 'Stimulée par l’histamine (récepteur H2), la gastrine et l’acétylcholine ; freinée par la somatostatine.')))
    C.pop('k25-gastrine', 'Gastrine', L(('Origine', 'Cellules G de l’antre gastrique.'), ('Effet', 'Stimule la sécrétion acide, directement et par la libération d’histamine.'), ('Pathologie', 'Élevée dans la gastrite antrale à Helicobacter pylori et, très fortement, dans le gastrinome.')))
    C.pop('k25-stress', 'Ulcères de stress', L(('Mécanisme', 'Défaut de perfusion de la muqueuse au cours des maladies graves.'), ('Facteurs indépendants', 'Troubles de la coagulation et ventilation mécanique de plus de 48 heures.'), ('Prévention', 'IPP chez le patient de soins intensifs à haut risque (S2k 2023, recommandation 7.18).')) + src(S2K))
    C.pop('k25-tdm', 'Tomodensitométrie de l’ulcère perforé', L(('Signes', 'Pneumopéritoine, liquide intrapéritonéal, épaississement pariétal, infiltration de la graisse, fuite de contraste hydrosoluble.'), ('Valeur', 'Plus sensible que la radiographie ; situe la perforation et écarte d’autres causes.'), ('Limite', 'Jusqu’à 12 % des perforations ont un examen normal (WSES 2020).')) + src(WSES))
    C.pop('k25-avk', 'Antivitamines K et éradication', L(('Interaction', 'Le métronidazole et l’oméprazole potentialisent l’acénocoumarol et la phenprocoumone.'), ('Conduite', 'Contrôler le temps de prothrombine pendant le traitement et adapter la dose (information professionnelle Pylera®).')) + src(FI('Pylera®')))
    C.pop('k25-nom', 'Traitement non opératoire de l’ulcère perforé', L(('Conditions', 'Patient stable, sans péritonite ni sepsis, perforation colmatée sur l’étude au contraste hydrosoluble.'), ('Risque', 'Environ 28 % d’échecs à 12 heures dans l’essai randomisé cité par la WSES ; moins bonne réponse après 70 ans.'), ('Statut', 'Non recommandé de routine (WSES 2020).')) + src(WSES))
    C.pop('k25-ipp-long-cours', 'IPP au long cours : effets indésirables', L(('Hypomagnésémie', 'Après au moins 3 mois, le plus souvent après un an ; peut entraîner hypocalcémie et hypokaliémie.'), ('Fractures', 'Risque modérément accru (hanche, poignet, rachis) après plus d’un an à dose élevée.'), ('Infections', 'Infections digestives un peu plus fréquentes.'), ('Conduite', 'Réévaluer l’indication ; arrêter si elle n’existe plus.')) + src(FI('Nexium®')))
    C.pop('k25-anresis', 'ANRESIS', L(('Définition', 'Centre suisse de surveillance de la résistance aux antibiotiques.'), ('Données Helicobacter pylori', 'Clarithromycine 28 %, lévofloxacine 18 %, métronidazole 44 %, amoxicilline 3 %, tétracycline 4 %, surtout après échec thérapeutique (SSI 2026).')) + src(SSI))
