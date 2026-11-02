#!/usr/bin/env python3
"""Record the author's completed coverage review; never certify clinical safety.

This records a specific manual review, not a generic automatic review engine.
verify_c85.py must run afterwards; binding and final package are separate.
"""
from pathlib import Path
import datetime,json
OUT=Path(__file__).resolve().parent
ROWS=[
('Question clinique et examen fédéral','S101,S102,S138,S139,S140','c85-profiles2017','La vignette mène à localisation, urgence et prélèvement ; SSP2017 identifiés, évolution2023/examen2028 explicitée sans prédiction des questions.'),
('Définition et périmètre CIM-10-GM','S113,S119','c85-1','C85.1/C85.9 non précisés ; C85.7 autre type précisé ; exclusions et diagnostic intégré distingués du codage.'),
('Classifications et stades','S101,S103,S119,S120','c85-e-4','Lugano tableaux2/3 et notes relus : rate, suffixeE limité, A/B Hodgkin ; diamètre et seuils historiques/actuels distingués ; IPI du DLBCL non prédiction individuelle PMBCL.'),
('Épidémiologie suisse et européenne','S114,S101,S102,S121','c85-2','Chiffres suisses agrégés2013–2017 et périmètreC82–C86,C96 ; populations des proportions européennes distinctes ; incidenceC85isolée non inventée.'),
('Normal vers pathologique','S104,S105,S106,S107','c85-s-semio','Six sciences, neuf analyses sémiologiques ; retour veineux, voies aériennes et histologie reliés aux signes, examens, limites et conséquences.'),
('Étiologies et facteurs de risque','S102,S106','c85-4','Mécanismes biologiques distingués des associations et des causes ; absence de facteur modifiable spécifique et pas de causalité professionnelle présumée.'),
('Anamnèse et symptômes','S101,S102,S120','c85-5','Compression, évolution et symptômesB ; fièvreOnkopedia>38°C distinguée du38,3°C historiqueLugano dans la fenêtre explicative.'),
('Examen clinique','S101,S102,S122','c85-6','Territoiresveineux, voiesrespiratoires, airesganglionnaires et position ; absence de symptôme ne garantit pas absence de risque anesthésique.'),
('Drapeaux rouges et urgences','S108,S109,S110,S122,S123,S124,S135','c85-biopsie-securite','Compression vitale et plan collectif ; anesthésie locale si faisable ; balance corticoïdes/prélèvement sans dogme ni dose inventée, populations adultes/pédiatriques séparées.'),
('Examens complémentaires','S101,S103,S120,S121','c85-7','Prélèvement suffisant, expertise, limitesTEP et calendriers5–6/6–8semaines explicités ; normales du laboratoire ; images liées à leurs repères.'),
('Diagnostic différentiel','S104,S105,S119,S136','c85-8','Masse antérieure : thymome, germinale, thyroïde, lymphomes ; morphologie/phénotype intégrés ; limites de la zone grise et expertise étayées.'),
('Prise en charge suisse et FI','S108,S109,S110,S111,S112,S130,S131,S132,S133,S134','c85-10','DixFI exactes et leurs indications ; schémas/réductions d’organe distingués ; unitéEndoxan et borneDoxorubicine neutralisées ; vincristine jamais intrathécale.'),
('Complications et pronostic','S101,S110,S115,S118','c85-12','Survie observationnelle, non-infériorité randomisée et taux de signalement distingués ; débutJ1–12 n’est pas fin de surveillanceCAR-T.'),
('Suivi, prévention, dépistage','S101,S116,S120','c85-13','Suivi clinique, effets tardifs, dépistage indiqué et registre suisse ; pas imagerie systématique après rémission ni extrapolation d’incidence.'),
('Situations particulières','S101,S108,S112,S117,S130,S131,S132,S133,S134,S137','c85-cytotoxiques-fi','Grossesse/fertilité selonOnkopedia séparées ducas ; âgé/fragile et organes ; pédiatrie selon indications/protocoles, aucun traitement adulte divisé arbitrairement.'),
('Spécificités administratives suisses','S116,S126,S127,S128,S129,S108,S110,S111','c85-suisse-acces','LS et indication distinctes, exceptions71a–d, LiMA matériel, causalitéLAA9 et conduite selonFI exacte ; pas garantie individuelle de remboursement.'),
('Diagnostic formel','S103,S102,S113,S119','c85-15','Synthèse intégrée ; aucun marqueur isolé ou liste de marqueurs tousobligatoires ; codage aprèsdiagnostic.'),
('Paramètres clés chiffrés','S101,S102,S104,S108,S110,S114,S115,S118,S120,S121,S130,S131,S132,S133,S135','c85-15','Relecture des nombres structurants : populationsOFS, proportionsPMBCL, immunophénotype, IPI, TEP, IELSG37/Cook, dosesFI etcas. Correction infiltration70–80 % et taux de signalement ; limites conservées.'),
('Sous-codes couverts','S113,S119','c85-1','C85.1,C85.2,C85.7,C85.9 explicités ; rubrique résiduelle non substitut au traitement de l’entité histologique.'),
('Points d’examen fédéral','S138,S139,S140,S125','c85-profiles2017','SSP2017numérotées et correspondances2023G/S différenciées ; cinqquizpédagogiques. G2local ne renvoie plus à la catégorie rénale du glossaire global.'),
]
RESOLUTIONS=[
('C85-R1','Classification et stades','S119,S120,S121','Lugano tables et WHO réellement lus ; rate/E/A/B et populationsIPI précisés.'),
('C85-R2','Compression, anesthésie et corticothérapie','S122,S123,S124,S135','Revue européenne avec Berne ; risque et stratégie collective ; deux séries avec populations/limites distinctes, urgence limitée à menace vitale.'),
('C85-R3','Composants cytotoxiques','S130,S131,S132,S133,S134','CinqFI supplémentaires réellement lues ; adaptations propres aux préparations. Seuil hépatiqueEndoxan incohérent exclu plutôt que corrigé par supposition.'),
('C85-R4','Pédiatrie et situations particulières','S101,S108,S112,S117,S130,S131,S132,S133,S134,S137','Cadre spécialisé et indications exactes ; pastranspositionadultes/enfants ; grossessefertilitéguidelines distinguées d’uncas.'),
('C85-R5','Administration suisse','S126,S127,S128,S129,S108,S110,S111','LS/limites,71a–d,LiMA,LAA9 et conduite consultés et intégrés sans garantie de cas individuel.'),
('C85-R6','Paramètres chiffrés','S101,S102,S104,S108,S110,S114,S115,S118,S120,S121,S130,S131,S132,S133,S135','Nombres structurants recoupés ; sensdénominatueur, unités, durée et population explicités ; effetsobservés nonchangés en preuvescausales.'),
('C85-R7','Objectifs fédéraux','S125,S138,S139,S140','PDF2017retrouvé, SSPpertinenteslues ; MEBEKO2026 et annonce2028 distinguées du mapping pédagogique2023.'),
]
LIMITS=[
 {'id':'C85-L1','text':'Aucune incidence suisse propre àC85/PMBCL trouvée ; chiffresagrégés datés uniquement.','blocking':False},
 {'id':'C85-L2','text':'CodageCIM-10-GM2024 consulté ; aucune revalidationCIM2026 prétendue.','blocking':False},
 {'id':'C85-L3','text':'Unité hépatiqueEndoxan incohérente dans copieFI ; seuil neutralisé, contrôleofficiel/pharmacie exigé avant administration.','blocking':False},
 {'id':'C85-L4','text':'Borne51µmol/l dansFIDoxorubicine nonclarifiée par supposition ; pas d’algorithme chiffré àcetteborne.','blocking':False},
 {'id':'C85-L5','text':'LesFI composant parcomposant ne constituent pas une ordonnance complète du protocole ; pédiatrie spécialisée, indicationsdistinctes.','blocking':False},
 {'id':'C85-L6','text':'Lectures ciblées et résumés nommés ; pas lectureintégrale globale ni validationhumaine revendiquée.','blocking':False},
]

def main():
    at=datetime.datetime.now(datetime.timezone.utc).isoformat()
    matrix=[{'point':i,'title':t,'status':'covered','sources':ids.split(','),'anchor':a,'evidence':note} for i,(t,ids,a,note) in enumerate(ROWS,1)]
    (OUT/'matrix-20.json').write_text(json.dumps({'code':'C85','reviewed_at':at,'mode':'self_review','rubrics':matrix,'meaning':'Couverture pédagogique revue, pas score médical ni certification.'},ensure_ascii=False,indent=2)+'\n')
    md='# C85 — recherche et couverture revue\n\nQuarante sources avec profondeur de lecture, populations et limites explicites. Auto-revue attribuée ; pas de certification médicale humaine ni relecture intégrale prétendue de tous les articles.\n\n## Matrice de complétude\n\n| Rubrique | Statut | Sources | Ancre | Preuve et limite |\n|---|---|---|---|---|\n'
    for r in matrix:md+=f"| {r['point']}. {r['title']} | ✔ | "+', '.join('['+x+']' for x in r['sources'])+f" | `{r['anchor']}` | {r['evidence']} |\n"
    md+='\n## Sous-codes\n\nC85.1, C85.2, C85.7 et C85.9 ; C83.3/C83.8 comme exclusions pertinentes.\n\n## Limites explicites\n\n'+'\n'.join('- '+x['id']+' : '+x['text'] for x in LIMITS)+'\n\n## Iconographie\n\nDeuxoriginauxCCBY4.0conservés, scannerA/B et histologieA–F ; légendesfrançaises liées aux repèresoriginaux ; aucun pixel ni anatomieIA créé.\n'
    (OUT/'recherche_C85/recherche.md').write_text(md)
    (OUT/'reserves.json').write_text(json.dumps([{'id':i,'subject':t,'status':'resolved_in_content_with_documented_limits','sources':ids.split(','),'resolution':note,'reviewed_at':at,'clinical_certification':False} for i,t,ids,note in RESOLUTIONS],ensure_ascii=False,indent=2)+'\n')
    (OUT/'limitations.json').write_text(json.dumps(LIMITS,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'matrix20':len(matrix),'reserves_documented':len(RESOLUTIONS),'final_tests_pending':True}))
if __name__=='__main__':main()
