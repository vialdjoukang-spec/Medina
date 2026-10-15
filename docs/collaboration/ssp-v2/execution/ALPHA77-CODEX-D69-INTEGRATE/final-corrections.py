from pathlib import Path
import json
out=Path(__file__).parent;root=out.resolve().parents[4]
changes={
'chapters/D69/D69_a.html':[
('Le cours ne fournit pas d’intervalle de référence plaquettaire suisse : cet intervalle dépend du laboratoire et figure sur son compte rendu.','Les HUG publient un repère illustratif de 150–350 G/L ; l’intervalle individuel reste celui du laboratoire et figure sur son compte rendu.'),
('L’hémogramme seul élimine formellement un purpura thrombopénique.','La numération recherche une thrombopénie ; le frottis et le contexte orientent sa cause.'),
('un hémogramme normal confirme que les plaquettes ne sont pas en cause.','une numération normale ne documente pas de thrombopénie ; le diagnostic causal reste à établir.'),
('La photographie suivante montre un purpura pétéchial cutané. Elle sert à reconnaître la lésion élémentaire : de petites taches rouges punctiformes, non saillantes, parfois confluentes.','La photographie suivante illustre des lésions cutanées rouges punctiformes, parfois confluentes. Elle permet d’en observer la répartition ; leur relief et leur comportement à la vitropression doivent être évalués par l’examen clinique.'),
("Purpura pétéchial cutané : taches rouges punctiformes qui ne s'effacent pas à la vitropression.",'Photographie de purpura : lésions rouges punctiformes ou confluentes ; relief et vitropression non évaluables sur cette image.'),
('La lecture commence par le relief : les taches sont plates, donc non infiltrées. Elle se poursuit par la répartition, qui oriente le médecin vers la recherche d’un déficit en plaquettes.','La lecture décrit les lésions visibles et leur répartition. Le médecin recherche ensuite leur relief et réalise la vitropression lors de l’examen ; ni une thrombopénie ni son absence ne sont établies par la photographie.'),
('mais seul l’hémogramme élimine un purpura thrombopénique.','tandis que la numération vérifie le nombre de plaquettes et que le frottis et le contexte complètent le diagnostic.'),
('La catégorie D69 de la CIM-10-GM 2024 réunit des maladies dont le point commun est un saignement cutané ou muqueux sans trouble de la coagulation plasmatique.','La catégorie D69 de la CIM-10-GM 2024 réunit des purpuras et d’autres diathèses hémorragiques. Le code ne prouve pas à lui seul un mécanisme ni la normalité du bilan de coagulation.')],
'chapters/D69/D69_d.html':[
('La dose minimale efficace est utilisée ; des doses élevées sont sans risque à court terme (10 jours au plus), puis réduites rapidement ; un traitement de plus de quelques jours s’arrête progressivement.','La dose minimale efficace est recherchée, et une dose initiale élevée est réduite rapidement. La FI demande un arrêt progressif d’un traitement dépassant quelques jours ; elle comporte aussi des mises en garde et une surveillance qui excluent de présenter les corticoïdes comme dépourvus de risque.'),
('les agonistes du récepteur de la TPO (cible 50 à 150 G/L)','les agonistes du récepteur de la TPO (objectif et titration propres à chaque produit, sans normaliser la numération)')]
}
log=[]
for name,pairs in changes.items():
 p=root/name;s=p.read_text()
 for before,after in pairs:
  assert s.count(before)==1,(name,before,s.count(before));s=s.replace(before,after);log.append(dict(file=name,before=before,after=after))
 p.write_text(s)
(out/'final-corrections.json').write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n')
print(len(log),'targeted corrections')
