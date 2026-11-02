#!/usr/bin/env python3
"""Corrections de périmètre établies par lecture des FI suisses exactes."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[5]
replacements={
 'Il faut une hydratation suffisante et un uricostatique dès 48 heures avant la première perfusion de rituximab':'La FI demande d’envisager une prophylaxie appropriée chez les patients à risque de lyse sous rituximab. Son délai de 48 heures figure dans la sous-section leucémie lymphatique chronique et ne constitue pas une règle chiffrée propre au lymphome médiastinal',
 'Hydratation suffisante et uricostatique dès 48 heures avant la première perfusion de rituximab':'Prophylaxie de la lyse adaptée au risque avant rituximab ; ne pas extrapoler au lymphome médiastinal le délai de 48 heures décrit dans la FI pour la leucémie lymphatique chronique',
 'Hydratation suffisante et uricostatique dès 48 heures avant la première perfusion (syndrome de lyse tumorale).':'Envisager une prophylaxie appropriée de la lyse selon le risque. Le délai de 48 heures mentionné dans la FI concerne sa sous-section leucémie lymphatique chronique ; il ne définit pas un protocole universel pour ce lymphome.',
 'La destruction rapide de cellules tumorales libère de l’acide urique, d’où l’uricostatique anticipé de 48 heures.':'La lyse rapide des cellules peut entraîner hyperuricémie, hyperkaliémie, hyperphosphatémie, hypocalcémie et insuffisance rénale aiguë. La FI demande une prophylaxie adaptée au risque et une surveillance étroite, particulièrement en cas de forte charge tumorale.',
 'uricostatique 48 heures avant le rituximab':'prophylaxie de la lyse adaptée au risque avant rituximab',
 'uricostatique dès 48 heures':'prophylaxie de la lyse adaptée au risque',
 'L’œdème cérébral est plus fréquent dans le lymphome médiastinal : 1,6 % au total, dont 0,8 % mortel, contre 0,7 % dans le DLBCL':'La FI Yescarta rapporte, dans les données après autorisation, un taux de signalement d’œdème cérébral de 1,6 % dans le lymphome médiastinal (0,8 % de cas fatals), contre 0,7 % dans le DLBCL et les autres indications (0,2 % de cas fatals). Ces taux de signalement concernent ce produit et ne sont pas une incidence comparative de tous les CAR-T',
 'L’œdème cérébral après CAR-T est plus fréquent dans le lymphome médiastinal (1,6 %, dont 0,8 % mortel)':'Après Yescarta, la FI rapporte un taux de signalement d’œdème cérébral de 1,6 % dans le lymphome médiastinal (0,8 % de cas fatals) ; il s’agit de données après autorisation propres au produit',
 'œdème cérébral, plus fréquent dans le lymphome médiastinal (1,6 %, dont 0,8 % mortel) que dans le DLBCL (0,7 %)':'œdème cérébral signalé après Yescarta à un taux de 1,6 % dans le lymphome médiastinal (0,8 % de cas fatals), contre 0,7 % dans le DLBCL et les autres indications (0,2 % de cas fatals)',
 'Œdème cérébral : 1,6 % dans le lymphome médiastinal, dont 0,8 % mortel, contre 0,7 % dans le DLBCL':'Œdème cérébral après autorisation de Yescarta : taux de signalement de 1,6 % dans le lymphome médiastinal (0,8 % de cas fatals), contre 0,7 % dans le DLBCL et les autres indications (0,2 % de cas fatals)',
 'entre J1 et J12':'entre J1 et J12 dans ZUMA-1 et ZUMA-7',
 'du jour 1 au jour 12':'du jour 1 au jour 12 dans ZUMA-1 et ZUMA-7',
 'le syndrome de libération de cytokines dans les 12 premiers jours après CAR-T':'le syndrome de libération de cytokines précocement après thérapie cellulaire (jours 1 à 12 dans ZUMA-1 et ZUMA-7 ; ce délai ne constitue pas une limite de surveillance)',
 'cytokines dans les 12 jours après CAR-T':'cytokines précocement après thérapie cellulaire, sans arrêter la vigilance au douzième jour',
 'Insuffisance cardiaque tardive, surtout avant 55 ans':'Risque d’insuffisance cardiaque accru par rapport à la population générale, particulièrement si l’exposition a eu lieu avant 55 ans',
 'contre-indication relative':'limite d’indication',
 'Contre-indication relative':'Limite d’indication',
}
for p in (ROOT/'chapters/C85').glob('*.html'):
 t=p.read_text()
 for old,new in replacements.items():t=t.replace(old,new)
 p.write_text(t)
print('FI : périmètre LLC/lyse, pharmacovigilance Yescarta, temporalité et indication clarifiés.')
