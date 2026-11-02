from cardio_1 import a, G
# N00 — Syndrome néphritique aigu ; définitions locales sans écraser le glossaire commun.
def local(k, literal, title, body, ref=None):
    if k not in G:
        a(k, [(k, literal)], title, '<p>' + body + '</p>', ref)
local('N00', 'catégorie de la CIM-10-GM', 'Syndrome néphritique aigu', 'Code syndromique ; la cause et la morphologie restent à documenter.', 'n00-nephritique-nephrotique')
for suffix, title in [('0','Anomalies glomérulaires mineures'),('1','Lésions glomérulaires segmentaires et focales'),('2','Glomérulonéphrite membraneuse diffuse'),('3','Glomérulonéphrite mésangio-proliférative diffuse'),('4','Glomérulonéphrite proliférative endocapillaire diffuse'),('5','Glomérulonéphrite mésangiocapillaire diffuse'),('6','Maladie à dépôt dense'),('7','Glomérulonéphrite diffuse en croissant'),('8','Autres modifications morphologiques'),('9','Type de modification morphologique non précisé')]:
    local('N00.'+suffix,'code de la CIM-10-GM 2024, subdivision morphologique',title,'Le suffixe décrit une morphologie ; les subdivisions .0 à .8 supposent normalement une identification histologique précise. Ce code ne définit pas une étiologie ni une prescription.','n00-biopsie')
local('MEBEKO','Medizinalberufekommission','Commission fédérale des professions médicales','Les exigences2026 définissent le cadre de l’examen fédéral ; les exercices du cours restent pédagogiques et non officiels.')
local('CIMS','Commission interfacultés médicales suisse','Commission interfacultés médicales suisse','Émetteur suisse associé au catalogue PROFILES ; la numérotation de l’édition2017 est explicitement distinguée des autres éditions.')
local('NC1','non-collagenous domain 1','Domaine non collagénique1 du collagèneIV','Le domaine NC1 de la chaîne alpha3 du collagèneIV est la cible décrite dans la maladie anti-membrane basale.','n00-immunofluorescence')

local('CUEN','Collège universitaire des enseignants de néphrologie','Collège universitaire des enseignants de néphrologie','Le manuel français de néphrologie2025 complète les sources suisses ; il ne remplace pas les informations professionnelles des produits suisses.')
local('GN','glomérulonéphrite','Glomérulonéphrite','Lésion inflammatoire du glomérule dont la cause et le profil histologique doivent être précisés.','n00-biopsie')
local('GTIN','Global Trade Item Number','Identifiant international de présentation commerciale','L’identifiant permet de rattacher la lecture à une présentation exacte de médicament ; il ne constitue pas une recommandation thérapeutique.')
