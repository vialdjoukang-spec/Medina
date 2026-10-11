from pathlib import Path
from datetime import datetime, timezone
import json, hashlib, re

D=Path('/workspace/work/medina-cycle1/livraisons/Livraison Codex/E-06-Endocrinologie et métabolisme/travail/CYCLE_01_E11')
C=D/'chapters/E11'; log=[]
def sub(file,old,new,source,why):
 p=C/file; t=p.read_text(); n=t.count(old)
 assert n>0,(file,old)
 p.write_text(t.replace(old,new))
 log.append({'file':file,'before':old,'after':new,'occurrences':n,'source_ids':source,'reason':why})
def f(file,old,new):sub(file,old,new,[],'Phrase complète, précision rédactionnelle ou correction de répétition ; faits et renvois conservés.')

sub('E11_b.html','Le tableau se lit de haut en bas : la première ligne qui s’applique l’emporte, et plusieurs lignes peuvent se cumuler.','Avant de choisir une protection à long terme, le médecin recherche et traite une carence insulinique ou une urgence métabolique. Les autres situations du tableau peuvent se cumuler ; elles orientent ensuite les traitements protecteurs selon les organes atteints.',['SSED','Crises'],'La ligne d’urgence insulinique doit précéder les choix de protection ; le classement visuel ne définit aucune priorité clinique.')
sub('E11_c.html','Dans le réticulum endoplasmique, elle devient proinsuline, puis l’appareil de Golgi la clive en insuline et en peptide C, stockés ensemble dans des granules.','Dans le réticulum endoplasmique, elle devient proinsuline. Celle-ci passe ensuite par l’appareil de Golgi, entre dans des vésicules sécrétoires immatures et y est clivée en insuline et en peptide C ; l’insuline mature est stockée dans les granules.',['Mécanismes'],'PMC7503727 : distinction entre transit par le Golgi et clivage dans les vésicules immatures.')
f('E11_c.html','son métabolisme couple l’apport de glucose à la réponse sécrétoire. Son métabolisme élève le rapport ATP/ADP','son métabolisme couple l’apport de glucose à la réponse sécrétoire en élevant le rapport ATP/ADP')
f('E11_c.html','via transporteurs du glucose','entrée cellulaire')
sub('E11_c.html','Chez le sujet non diabétique, l’HbA1c reste inférieure à 5,7 %.','Dans la classification de la SSED 2011, une HbA1c inférieure à 5,7 % se situe sous la zone du prédiabète.',['HbA1c'],'Une personne avec prédiabète reste non diabétique ; le seuil ne décrit pas tous les non-diabétiques.')
sub('E11_c.html','l’effet incrétine, s’est effondrée','l’effet incrétine, est diminuée',['Incrétines'],'Éviter une disparition universelle de cet effet.')
sub('E11_a.html','</button> s’effondre, et le glucagon','</button> diminue, et le glucagon',['Incrétines'],'Éviter une disparition universelle de cet effet.')
sub('E11_c.html','son effet glycémique disparaît quand le DFG baisse','son effet glycémique s’affaiblit quand le DFG baisse',['FI-Jardiance','FI-Forxiga'],'Le degré d’affaiblissement dépend du DFG et du produit ; pas disparition à toute baisse.')
sub('E11_pop2.html','hématurie macroscopique inexpliquée','hématurie inexpliquée',['FI-Actos'],'La contre-indication suisse ne se limite pas à une hématurie macroscopique.')
sub('E11_pop1.html','Le guide suisse classe le pied en trois niveaux.','Devant une plaie du pied, le guide suisse organise la prise en charge en trois niveaux.',['Pied'],'Distinguer triage de plaie et stratification générale du pied sans plaie.')
sub('E11_pop1.html','deux pouls pédieux perçus','deux pouls du pied palpables',['Pied'],'Ne pas confondre deux pouls du même pied et deux artères pédieuses bilatérales.')
for file in ['E11_pop1.html','E11_pop2.html']:
 sub(file,'SSED, document d’alternatives aux insulines, état août 2025</a>','SSED–SGRM, diabète et conduite, édition août 2025</a>',['Conduite'],'Le lien Handout_Richtlinien_Diabetes renvoie aux règles de conduite.')
sub('E11_pop2.html','>SSED 2026</a>','>SSED, alternatives aux insulines, état août 2025</a>',['InsulinesSSED'],'La version dans le document prime sur 2026 dans le nom du fichier.')
sub('E11_pop2.html','(SSED 2026).','(SSED, alternatives aux insulines, état août 2025).',['InsulinesSSED'],'La version dans le document prime sur 2026 dans le nom du fichier.')
sub('E11_pop2.html','quatre textes comparés','trois textes comparés',['SSED','ESC','EASD'],'La fenêtre comporte exactement trois référentiels.')
sub('E11_pop2.html','≤ 6,5 % sans médicament hypoglycémiant ou si début avant 40 ans','≤ 6,5 % avec mode de vie seul ou médicament sans risque hypoglycémique, ou si début avant 40 ans',['EASD'],'Le texte n’exclut pas tout médicament réduisant la glycémie, seulement ceux exposant à l’hypoglycémie.')
sub('E11_pop2.html','Le temps passé entre 3,9 et 10 mmol/L doit dépasser 70 % chez le patient équipé d’un capteur.','Le consensus propose comme cible générale un temps supérieur à 70 % entre 3,9 et 10 mmol/L chez les adultes suivis par capteur ; une cible moins stricte peut convenir en cas de fragilité, de complications avancées ou d’espérance de vie limitée.',['EASD'],'La cible générale n’est pas une obligation identique pour toutes les populations.')
sub('E11_b.html','L’âge, la fonction rénale, la grossesse et la conduite modifient la cible et le choix des molécules, rarement l’indication des classes protectrices.','L’âge, la fonction rénale, la grossesse et la conduite modifient la cible et le choix des molécules. Chaque prescription respecte les restrictions de la FI suisse exacte, notamment pendant la grossesse et l’allaitement.',['FI-Glucophage','FI-Jardiance','FI-Ozempic','FI-Mounjaro'],'Une grossesse peut empêcher la prescription d’une classe protectrice ; aucune exception générale n’est affirmée.')
f('E11_b.html','Le diagnostic repose sur une mesure de laboratoire, sur une glycémie plasmatique de laboratoire plutôt que sur un lecteur capillaire, utilisé pour la surveillance.','Le diagnostic repose sur des mesures de laboratoire. La glycémie plasmatique, plutôt que celle d’un lecteur capillaire destiné à la surveillance, permet d’appliquer les seuils diagnostiques.')
f('E11_b.html','à longue durée d’action et à métabolites actifs, à durée prolongée et métabolites actifs','à longue durée d’action et à métabolites actifs')
f('E11_d.html','Plus recommandé par la SSED ; exceptions','N’est plus recommandé par la SSED ; exceptions')
f('E11_d.html','Ne jamais doubler une classe, ne jamais associer agoniste du GLP-1 et inhibiteur de la DPP-4, éviter l’association insuline et sulfonylurée.','Le prescripteur évite les doublons de classe et n’associe pas un agoniste du GLP-1 à un inhibiteur de la DPP-4. Il évite autant que possible l’association d’insuline à une sulfonylurée.')
sub('E11_b.html','pieds chaque année, ophtalmologie tous les 2 ans.','pieds chaque année, ophtalmologie au diagnostic puis tous les 2 ans si l’examen est normal.',['Qualité'],'Rappeler la condition clinique de l’intervalle ophtalmologique.')

# Les consignes deviennent des phrases avec un sujet, sans faits supplémentaires.
replacements={
'E11_pop1.html':[
('Demander un avis diabétologique et génétique','Le médecin demande un avis diabétologique et génétique'),
('Si le résultat est normal, programmer le contrôle','Si le résultat est normal, le médecin programme le contrôle'),
('Sous metformine, vérifier notamment une carence','Sous metformine, le médecin recherche notamment une carence'),
('Montrer d’abord la sensation sur la main du patient ; il ne regarde pas les sites testés. Tester trois sites sur chaque pied. Poser le filament perpendiculairement jusqu’à sa courbure','L’examinateur montre d’abord la sensation sur la main du patient ; celui-ci ne regarde pas les sites testés. L’examinateur teste trois sites sur chaque pied et pose le filament perpendiculairement jusqu’à sa courbure'),
('Éviter ulcère, callosité, cicatrice et nécrose ; ne pas faire glisser le filament.','Il évite ulcère, callosité, cicatrice et nécrose ; il ne fait pas glisser le filament.'),
('Répéter deux contacts au même site en les alternant','L’examinateur répète deux contacts au même site en les alternant'),
('Une perte de protection fait craindre une plaie non perçue : adapter chaussage, inspection et suivi.','Une perte de protection fait craindre une plaie non perçue : l’équipe adapte le chaussage, l’inspection et le suivi.'),
('Employer un filament en bon état et le protocole complet choisi, sans additionner les scores de méthodes différentes.','L’examinateur emploie un filament en bon état et suit le protocole complet choisi, sans additionner les scores de méthodes différentes.'),
('Avec un diapason de 128 Hz, montrer d’abord la vibration au poignet.','L’examinateur montre d’abord la vibration au poignet avec un diapason de 128 Hz.'),
('Poser le diapason perpendiculairement','Il pose le diapason perpendiculairement'),
('Faire deux applications vibrantes et une simulée','Il fait deux applications vibrantes et une simulée'),
('Si elle est absente à l’orteil, répéter plus proximalement.','Si elle est absente à l’orteil, il répète le test plus proximalement.'),
('sont deux méthodes : conserver la méthode et sa règle d’interprétation. Intégrer monofilament, peau, déformations, pouls et antécédent d’ulcère avant de classer le risque.','sont deux méthodes : l’examinateur conserve la méthode et sa règle d’interprétation. Il intègre monofilament, peau, déformations, pouls et antécédent d’ulcère avant de classer le risque.'),
('Après une hyperglycémie de stress, recontrôler à distance','Après une hyperglycémie de stress, le médecin recontrôle la glycémie à distance'),
('Prévenir les secours, surveiller le patient et ne rien faire avaler tant qu’il ne peut pas déglutir en sécurité.','L’entourage prévient les secours, surveille le patient et ne lui fait rien avaler tant qu’il ne peut pas déglutir en sécurité.'),
('Quand il a récupéré et peut avaler, donner des glucides par voie orale','Quand le patient a récupéré et peut avaler, son entourage lui donne des glucides par voie orale'),
('appliquer le protocole hospitalier avec surveillance rapprochée','l’équipe applique le protocole hospitalier avec surveillance rapprochée'),
('sous ce traitement, mesurer les cétones et le gaz du sang quelle que soit la glycémie. Arrêter le produit et organiser une évaluation hospitalière immédiate.','sous ce traitement, le médecin mesure les cétones et le gaz du sang quelle que soit la glycémie. Il arrête le produit et organise une évaluation hospitalière immédiate.'),
('Liquides, insuline, correction et surveillance des électrolytes, puis traitement de la cause.','Le traitement associe liquides et insuline, avec correction et surveillance des électrolytes, puis traitement de la cause.'),
('n’est pas automatique : vérifier le facteur déclenchant et le bénéfice–risque.','n’est pas automatique : le médecin vérifie le facteur déclenchant et le bénéfice–risque.'),
('Classer ensemble la cause, le DFG et l’albuminurie ; répéter un résultat inhabituel.','Le médecin classe ensemble la cause, le DFG et l’albuminurie ; il contrôle de nouveau un résultat inhabituel.'),
('Ajouter un inhibiteur du SGLT2 adapté','Le médecin ajoute un inhibiteur du SGLT2 adapté'),
('Hématurie persistante, sédiment actif, chute rapide et durable du DFG, albuminurie A3 en progression, syndrome néphrotique ou histoire familiale suggérant une autre cause.','Le médecin adresse le patient en cas d’hématurie persistante, de sédiment actif, de chute rapide et durable du DFG, d’albuminurie A3 en progression, de syndrome néphrotique ou d’histoire familiale suggérant une autre cause.'),
('Pour l’état hyperosmolaire, calculer l’osmolalité efficace','Pour l’état hyperosmolaire, le médecin calcule l’osmolalité efficace')],
'E11_pop2.html':[
('prescrire la classe dont le bénéfice est démontré','le médecin prescrit la classe dont le bénéfice est démontré'),
('ajouter ou garder la metformine','il ajoute ou garde la metformine'),
('Enseigner la technique, la surveillance, la conduite et le traitement de l’hypoglycémie ; réévaluer les sécrétagogues.','L’équipe enseigne la technique, la surveillance, la conduite et le traitement de l’hypoglycémie ; le médecin réévalue les sécrétagogues.'),
('Après optimisation de la basale, vérifier les glycémies postprandiales, l’observance et la technique.','Après optimisation de la basale, le médecin vérifie les glycémies postprandiales, l’observance et la technique.'),
('gliclazide seulement, à titre exceptionnel, éviter l’association à l’insuline autant que possible','le gliclazide reste une option exceptionnelle et son association à l’insuline est évitée autant que possible'),
('ne jamais interrompre toute insuline chez un patient insulinodéficient sans encadrement médical.','le patient insulinodéficient ne supprime jamais toute son insuline sans encadrement médical.'),
('sans capteur, mesurer avant le trajet et au moins toutes les deux heures pendant un long trajet.','sans capteur, le patient mesure sa glycémie avant le trajet et au moins toutes les deux heures pendant un long trajet.'),
('Sous 4 mmol/L : arrêter, prendre des glucides rapides et attendre au moins 45 minutes avant de repartir ; entre 4 et 5, prendre 10 à 20 g de glucides.','Sous 4 mmol/L, il s’arrête, prend des glucides rapides et attend au moins 45 minutes avant de repartir ; entre 4 et 5, il prend 10 à 20 g de glucides.'),
('Vérifier le permis exact, les hypoglycémies, les complications visuelles/neurologiques et l’usage du capteur.','Le médecin vérifie le permis exact, les hypoglycémies, les complications visuelles/neurologiques et l’usage du capteur.'),
('Hypersensibilité ; vérifier aussi les intolérances héréditaires aux excipients décrites par la FI.','L’hypersensibilité est une contre-indication ; le médecin vérifie aussi les intolérances héréditaires aux excipients décrites par la FI.'),
('Risques de mycose génitale, déplétion volémique et aggravation d’une déshydratation','Ces médicaments exposent à une mycose génitale, à une déplétion volémique et à l’aggravation d’une déshydratation'),
('avec fièvre ou malaise, rechercher une gangrène de Fournier et arrêter le produit.','avec fièvre ou malaise, le médecin recherche une gangrène de Fournier et arrête le produit.'),
('Contrôler le rein et la volémie ; réduire éventuellement l’insuline ou le sécrétagogue associé.','Il contrôle le rein et la volémie ; il réduit éventuellement l’insuline ou le sécrétagogue associé.'),
('Suspendre lors de jeûne prolongé, maladie aiguë avec déshydratation ou suspicion d’acidocétose.','Le traitement est suspendu lors de jeûne prolongé, de maladie aiguë avec déshydratation ou de suspicion d’acidocétose.'),
('Jardiance® et Forxiga® : interruption au moins trois jours avant chirurgie majeure ou acte avec jeûne prolongé, selon leurs FI. Reprendre lorsque l’état clinique est stable et l’alimentation rétablie.','Jardiance® et Forxiga® sont interrompus au moins trois jours avant une chirurgie majeure ou un acte avec jeûne prolongé, selon leurs FI. La reprise attend que l’état clinique soit stable et l’alimentation rétablie.'),
('pour ces produits, appliquer l’intervalle de leur FI suisse.','pour ces produits, le prescripteur applique l’intervalle de leur FI suisse.'),
('nécessité absolue ; interrompre l’allaitement sous traitement.','nécessité absolue ; l’allaitement est interrompu sous traitement.'),
('Hypersensibilité au produit. Pancréatite suspectée : arrêt et évaluation ; pancréatite confirmée : ne pas réintroduire. Éviter les formes sévères de gastroparésie selon le produit ; informer l’anesthésiste avant une procédure en raison du risque d’aspiration. Réduire si nécessaire l’insuline/sulfonylurée associée.','L’hypersensibilité au produit est une contre-indication. Une suspicion de pancréatite conduit à l’arrêt et à une évaluation ; une pancréatite confirmée empêche la réintroduction. Le médecin évite les formes sévères de gastroparésie selon le produit et informe l’anesthésiste avant une procédure en raison du risque d’aspiration. Il réduit si nécessaire l’insuline ou la sulfonylurée associée.'),
('Enseigner cette prudence spécialisée plutôt que la transformer silencieusement en contre-indication suisse formelle.','Le cours enseigne cette prudence spécialisée sans la transformer en contre-indication suisse formelle.'),
('Hypersensibilité. Pancréatite suspectée : arrêter et évaluer ; si confirmée, ne pas réintroduire.','L’hypersensibilité est une contre-indication. Le médecin arrête le traitement et évalue une pancréatite suspectée ; si elle est confirmée, il ne réintroduit pas le produit.'),
('Surveiller la nutrition, la rétinopathie et les symptômes psychiques selon les antécédents. Réduire éventuellement l’insuline ou le sécrétagogue associé.','Il surveille la nutrition, la rétinopathie et les symptômes psychiques selon les antécédents. Il réduit éventuellement l’insuline ou le sécrétagogue associé.'),
('Hypersensibilité. Rechercher une pancréatite devant une douleur abdominale persistante ; arrêter si suspectée.','L’hypersensibilité est une contre-indication. Le médecin recherche une pancréatite devant une douleur abdominale persistante et arrête le traitement si elle est suspectée.'),
('diminuent l’exposition : envisager un autre traitement.','diminuent l’exposition : le médecin envisage un autre traitement.'),
('Éviter pendant la grossesse ; ne pas utiliser pendant l’allaitement selon les FI. Ne pas associer à un agoniste du GLP-1 ou au tirzépatide','Ces produits sont évités pendant la grossesse et ne sont pas utilisés pendant l’allaitement, selon leurs FI. Ils ne sont pas associés à un agoniste du GLP-1 ou au tirzépatide'),
('peut diminuer les besoins : intensifier le contrôle et ajuster individuellement, sans tableau de réduction automatique. Hypersensibilité au produit ;','peut diminuer les besoins : le médecin intensifie le contrôle et ajuste individuellement, sans tableau de réduction automatique. L’hypersensibilité au produit est une contre-indication ;'),
('Risques communs : hypoglycémie, prise de poids, lipodystrophie et amyloïdose cutanée aux sites. Faire tourner les sites, vérifier le produit et la concentration avant chaque injection, enseigner le secours et la conduite.','Ces produits exposent à l’hypoglycémie, à la prise de poids, à la lipodystrophie et à l’amyloïdose cutanée aux sites. Le patient alterne les sites et vérifie le produit et la concentration avant chaque injection ; l’équipe enseigne le secours et la conduite.')],
'E11_c.html':[
('Interpréter le prélèvement avec la situation clinique et contrôler un résultat inhabituel.','Le médecin interprète le prélèvement avec la situation clinique et contrôle un résultat inhabituel.')],
'E11_d.html':[
('Les effets indésirables se gèrent plutôt qu’ils ne font arrêter.','La conduite devant un effet indésirable dépend de sa gravité : la tolérance peut parfois s’améliorer avec une adaptation, alors qu’un signal de danger impose l’arrêt et une évaluation.')]
}
for file,pairs in replacements.items():
 for old,new in pairs:f(file,old,new)

# Les sept résumés Pareto conservent leurs quatre parties et leurs fenêtres réelles.
for file,pairs in {
'E11_pop2.html':[
('</button> dès 35 ans dans le consensus conjoint 2026,','</button> est proposé dès 35 ans dans le consensus conjoint 2026,'),
('Examen : poids, pression artérielle, signes d’insuffisance cardiaque, pouls et','L’examen apprécie le poids, la pression artérielle, les signes d’insuffisance cardiaque, les pouls et'),
('Sans symptômes, deux résultats concordants au laboratoire ; si discordants, répéter le test anormal. Tenir compte des limites de l’HbA1c.','Sans symptômes, le diagnostic exige deux résultats concordants au laboratoire ; si les tests sont discordants, le médecin répète le test anormal et tient compte des limites de l’HbA1c.'),
('>Hypoglycémie</button> est','>L’hypoglycémie</button> est'),
('>État hyperosmolaire</button> : les quatre critères réunis — glycémie ≥ 33,3 mmol/L ; osmolalité efficace &gt; 300 ou totale &gt; 320 ; β-hydroxybutyrate &lt; 3 ou cétonurie &lt; 2+ ; pH ≥ 7,3 et bicarbonates ≥ 15.','>L’état hyperosmolaire</button> exige quatre critères réunis : glycémie ≥ 33,3 mmol/L ; osmolalité efficace &gt; 300 ou totale &gt; 320 mOsm/kg ; β-hydroxybutyrate &lt; 3 mmol/L ou cétonurie &lt; 2+ ; pH ≥ 7,3 et bicarbonates ≥ 15 mmol/L.'),
('>Acidocétose</button> : diabète connu ou glucose ≥ 11,1 ; β-hydroxybutyrate ≥ 3 ou cétonurie ≥ 2+ ; pH &lt; 7,3 et/ou bicarbonates &lt; 18. Une glycémie basse ne l’exclut pas. Urgence hospitalière.','>L’acidocétose</button> exige trois critères réunis : diabète connu ou glucose ≥ 11,1 mmol/L ; β-hydroxybutyrate ≥ 3 mmol/L ou cétonurie ≥ 2+ ; pH &lt; 7,3 et/ou bicarbonates &lt; 18 mmol/L. Une glycémie basse ne l’exclut pas ; elle exige une prise en charge hospitalière urgente.'),
('>Cible d’HbA1c</button> autour de 7 %,','>La cible d’HbA1c</button> se situe autour de 7 %,'),
('Traitement multifactoriel : tabac, pression artérielle, LDL, poids et activité.','Le traitement agit sur plusieurs facteurs : tabac, pression artérielle, LDL, poids et activité.'),
('Choisir les <button','Le médecin choisit les <button'),
('SSED 2023 : metformine combinée d’emblée à une classe protectrice, puis trithérapie ;','La SSED 2023 recommande la metformine combinée d’emblée à une classe protectrice, puis la trithérapie ; elle recommande une'),
('Sulfonylurées non recommandées en première intention par la SSED ;','Les sulfonylurées ne sont pas recommandées en première intention par la SSED ; le'),
('</button> réservé à certaines situations','</button> est réservé à certaines situations'),
('>Repères suisses de suivi</button> : trois visites et deux HbA1c annuelles dans la grille de qualité de patientèle ; adapter le suivi individuel.','>Les repères suisses de suivi</button> comportent trois visites et deux HbA1c annuelles dans la grille de qualité de patientèle ; le suivi individuel reste adapté au patient.'),
('>Jours de maladie</button> : plan écrit, hydratation, surveillance, arrêt temporaire des produits à risque selon la situation ; ne pas supprimer seul l’insuline nécessaire.','>Les jours de maladie</button> exigent un plan écrit, une hydratation, une surveillance et un arrêt temporaire des produits à risque selon la situation ; le patient ne supprime pas seul l’insuline nécessaire.'),
('>Glucophage®</button> contre-indiqué si DFG &lt; 30 ;','>Glucophage®</button> est contre-indiqué si le DFG est &lt; 30 mL/min/1,73 m² ; les'),
('>inhibiteurs du SGLT2</button> : seuils d’initiation/poursuite propres au produit et à l’indication.','>inhibiteurs du SGLT2</button> ont des seuils d’initiation et de poursuite propres au produit et à l’indication.'),
('>Grossesse/allaitement</button> : restrictions de la FI exacte ; sémaglutide exclu, arrêt deux mois avant projet. Tirzépatide : contraception supplémentaire après début et chaque augmentation.','>La grossesse et l’allaitement</button> imposent les restrictions de la FI exacte ; le sémaglutide est exclu et s’arrête deux mois avant un projet. Le tirzépatide exige une contraception supplémentaire après le début et chaque augmentation.'),
('>Conduite</button> : risque iatrogène, complications et catégorie de permis ;','>La conduite</button> dépend du risque iatrogène, des complications et de la catégorie de permis ; une'),
('>Périopératoire</button> : metformine 48 heures avant anesthésie générale/locorégionale ; Jardiance®/Forxiga® au moins trois jours avant intervention majeure selon leurs FI.','>La période périopératoire</button> impose l’arrêt de la metformine 48 heures avant une anesthésie générale ou locorégionale ; Jardiance® et Forxiga® s’arrêtent au moins trois jours avant une intervention majeure, selon leurs FI.'),
('Albuminurie : A1 &lt; 3, A2 de 3 à &lt; 30, A3 ≥ 30 mg/mmol ;','L’albuminurie se classe en A1 &lt; 3, A2 de 3 à &lt; 30 et A3 ≥ 30 mg/mmol ; sa'),
('</button> au moins trois mois et confirmation du stade.','</button> exige au moins trois mois et une confirmation du stade.'),
('>NT-proBNP</button> chez le diabétique asymptomatique :','>Le NT-proBNP</button> s’interprète selon le contexte chez le diabétique asymptomatique :'),
('; interpréter selon contexte.','.'),
('>β-hydroxybutyrate</button> ≥ 3 mmol/L ne suffit pas seul à diagnostiquer une acidocétose ; examiner pH/bicarbonates et diabète/hyperglycémie.','>Un β-hydroxybutyrate</button> ≥ 3 mmol/L ne suffit pas seul à diagnostiquer une acidocétose ; le médecin examine le pH et les bicarbonates ainsi que le diabète ou l’hyperglycémie.'),
('Osmolalité efficace = 2 × Na⁺ + glucose ; totale = 2 × Na⁺ + glucose + urée, en mmol/L.','L’osmolalité efficace se calcule par 2 × Na⁺ + glucose ; la totale ajoute l’urée, toutes ces concentrations étant en mmol/L et le résultat en mOsm/kg.'),
('Glycémie élevée avec HbA1c normale : évoquer','Une glycémie élevée avec HbA1c normale fait évoquer une'),
('; confirmer à distance.','; le médecin confirme la situation à distance.'),
('>Basales sous-cutanées</button> ont','>Les basales sous-cutanées</button> ont'),
('>Incrétines</button> : GIP/GLP-1 amplifient','>Les incrétines</button> GIP et GLP-1 amplifient'),
('>Signal insulinique</button> : récepteur → IRS-1/IRS-2 → PI3K → AKT ; GLUT4 vers la membrane musculaire/adipocytaire, FOXO1 freiné dans le foie.','>Le signal insulinique</button> suit la voie récepteur → IRS-1/IRS-2 → PI3K → AKT ; il conduit GLUT4 vers la membrane musculaire ou adipocytaire et freine FOXO1 dans le foie.'),
('Stress oxydant et','Le stress oxydant et la'),
('; anomalies de durée de vie des hématies','; les anomalies de durée de vie des hématies'),
('>SGLT2</button> : glucose et sodium réabsorbés au tubule proximal ; inhibition entraîne glycosurie et probablement rétrocontrôle tubulo-glomérulaire protecteur, avec effets glycémiques et rénaux distincts.','>SGLT2</button> réabsorbe le glucose et le sodium au tubule proximal ; son inhibition entraîne une glycosurie et probablement un rétrocontrôle tubulo-glomérulaire protecteur, avec des effets glycémiques et rénaux distincts.')]
}.items():
 for old,new in pairs:f(file,old,new)

# Les icônes de la barre Sciences sont décoratives et ne portent aucune affirmation médicale.
p=C/'E11_c.html'; t=p.read_text()
icons=['<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="3"/>','<path d="M2 12h4l3-7 4 14 3-7h6"/>','<circle cx="6" cy="6" r="3"/><circle cx="18" cy="6" r="3"/><circle cx="12" cy="18" r="3"/><path d="m8 8 3 7m5-7-3 7M9 6h6"/>','<path d="M9 3C2 3 2 21 9 21c5 0 3-7 0-9 3-2 5-9 0-9Zm6 9h6"/>']
for i,m in reversed(list(enumerate(re.finditer(r'(<button\b[^>]*\bdata-s=[^>]*>)',t)))):
 assert i<4
 svg='<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8">'+icons[i]+'</svg>'
 t=t[:m.end()]+svg+t[m.end():]
assert t.count('<svg viewBox="0 0 24 24" aria-hidden="true"')==4
p.write_text(t); log.append({'file':'E11_c.html','before':'Quatre boutons Sciences sans icône','after':'Quatre icônes SVG décoratives accessibles','source_ids':[],'reason':'Forme de la barre de sélection Sciences requise par le modèle et le contrat.'})

out={'actor':'C01-R-ENDO','code':'E11','corrected_at':datetime.now(timezone.utc).isoformat(),'entry_record':'conformite_entree_reprise2.json','purpose':'Écarts réels détectés par relecture intégrale postérieure à la nouvelle entrée ; pas corrections de schéma de convenance.','dose_rechecks_unchanged':['Diamicron MR : paliers d’au moins deux semaines dans la FI suisse, contrairement à une règle étrangère différente.','Trulicity : dose adulte recommandée 0,75 mg/semaine puis 1,5 si insuffisant et toléré ; pas règle étrangère imposant 1,5 en association.'],'changes':log}
(D/'preuves/corrections_reprise2.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(len(log),'corrections réelles et rédactionnelles tracées.')
