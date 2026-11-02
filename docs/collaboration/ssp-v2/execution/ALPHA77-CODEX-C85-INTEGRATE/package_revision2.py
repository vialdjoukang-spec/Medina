#!/usr/bin/env python3
"""Package this specific author review only after real successful verification.

No new medical judgment is generated here. Source changes after verification
abort packaging. No push, registry release, clinical certification or PR.
"""
from pathlib import Path
import datetime,hashlib,json
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[4];PACK=OUT/'review-package'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def main():
    verify=json.loads((OUT/'verification.json').read_text());assert verify.get('ok') and len(verify['checks'])==6
    assert all(x['exit_code']==0 for x in verify['checks'])
    for path,digest in verify['final_sources'].items():assert sha(ROOT/path)==digest,path
    assert sha(OUT/'C85-apercu-autonome.html')==verify['preview_sha256']
    at=datetime.datetime.now(datetime.timezone.utc).isoformat()
    old=json.loads((PACK/'self-review.json').read_text());old['reviewed_at']=at
    old['source_sha256']=verify['final_sources'];old['preview_sha256']=verify['preview_sha256']
    old.pop('full_lesson_complete',None);old['coverage_complete_for_project']=True
    old['completion_gate']='Separate complete command required after packaging; this record is an attributed self-review.'
    old['medical']['scope']='Auto-revue de la couverture complète du plan monographique, des vingt rubriques et des corrections, selon les passages effectivement lus. Pas de validation médicale humaine.'
    old['medical']['blocking_findings']=[]
    old['medical']['corrections'] += [
      'Lugano : rate, stadeIII, E limité, A/B ; bulk historique et seuilEHA2025 distingués ; IPI et fréquences avec populations.',
      'Corticoïdes prébiopsie : séries pédiatriques médiastinales et DLBCLadultes séparées ; préparation anesthésique collective, pas règle universelle.',
      'DixFI exactes consultées ; doses/réductions distinguées du protocole complet ; unitéEndoxan et borneDoxorubicine non corrigées par supposition.',
      'LS, exceptions71a–d, LiMA, causalitéLAA9 et conduite exactes selonproduit ajoutées.',
      'PROFILES2017 / exigencesMEBEKO2026 / version2023 et examen2028 séparés ; collisionG2glossaire rénal prévenue localement.',
      'Urgence thérapeutique liée à compression vitale, pas tout syndrome cave ; signalementsCAR-T et débutsJ1–12 non transformés en incidence ni fin de surveillance.',
      'Infiltration70–80 % ne désigne pas seulement plèvre/péricarde ; survieIPI pas prédiction personnelle ; IELSG37 non-inférioritéPFS distincte de survieglobale observée.'
    ]
    old['medical']['limitations']=json.loads((OUT/'limitations.json').read_text())
    old['language']['scope']='Relecture des titres, tableaux, fenêtres, synthèses et correspondances ; conservation des termes natifs et clarification des conditions, unités, populations et temporalité.'
    old['language']['remaining']='Pas de certification d’absence absolue d’erreur ; profondeur de chaque source explicitée, historique conservé.'
    old['visual']['observations']='Aperçu natif final testé en1440/390 : sixsciences, neufsections, quatreoccurrencesoriginales décodées, livre24px, navigation et fenêtres. G2ouvre la ficheadénopathie après normalisation des césures dans le test. Captures finales mobilehistologie et bureaulivre24 réellement affichées et inspectées ; repèresA–F et légende visibles.'
    write(PACK/'self-review.json',old)
    source=json.loads((OUT/'recherche_C85/sources.json').read_text())
    manifest=json.loads((PACK/'lesson-manifest.json').read_text())
    manifest['sources']=[{'id':s['id'],'url':s['url'],'publisher':s['editeur'],'read_at':s['date_consultation'],'section':s['section_page'],'passage':s['passage_paraphrase'],'population':s['population'],'limits':s['limites'],'reading_depth':s['niveau_lecture']} for s in source['sources']]
    extra={1:['S119'],2:['S121'],4:['S122','S138','S139','S140'],5:['S120'],6:['S122'],8:['S119','S136'],9:['S120','S121'],10:['S122','S123','S124'],11:['S130','S131','S132','S133','S134'],12:['S126','S127','S128','S129'],13:['S120','S121'],14:['S122','S125','S138','S139','S140']}
    for row in manifest['monograph']:
        row['status']='covered';row['sources']=list(dict.fromkeys(row['sources']+extra.get(row['point'],[])))
        if row['point']==11:row['coverage_explanation']='Les options européennes et dixFI suisses exactes sont distinguées selon produit, indication, population et fonctiond’organe ; les données douteuses ne deviennent pas des doses et les limites sont explicites.'
        if row['point']==13:row['coverage_explanation']='Les nombres structurants de fréquence, stadification, réponse, survie, dose et signalement ont été recoupés aux passages déclarés ; leur population, temporalité et portée sont précisées dans les synthèses et fenêtres.'
    manifest['blocking_findings']=[];manifest['limitations']=old['medical']['limitations']
    manifest['matrix20']=json.loads((OUT/'matrix-20.json').read_text())['rubrics']
    manifest['closure_status']='ready_for_project_completion_gate_and_user_review'
    for review in manifest['reviews'].values():review['sha256']=sha(PACK/'self-review.json')
    (PACK/'content.html').write_text('\n'.join(p.read_text() for p in sorted((ROOT/'chapters/C85').glob('*.html'))))
    write(PACK/'lesson-manifest.json',manifest)
    for figure in manifest['images']:figure['path']='review-package/'+figure['path'];figure['medical_review']='review-package/self-review.json'
    for review in manifest['reviews'].values():review['path']='review-package/'+review['path']
    manifest['matrix20_reference']='matrix-20.json';write(OUT/'lesson-manifest.json',manifest)
    write(OUT/'monograph-14.json',{'code':'C85','reviewed_at':at,'mode':'self_review','points':manifest['monograph'],'clinical_certification':False})
    binding={'code':'C85','verified_at':verify['finished_at'],'preview':'C85-apercu-autonome.html','preview_sha256':verify['preview_sha256'],'final_sources':verify['final_sources'],'checks':['verification.json','sciences-final.json','browser-report-autonomous.json','verite-verification.log'],'clinical_certification':False}
    write(OUT/'source-binding.json',binding)
    (OUT/'README.md').write_text('''# C85 — version révisée du 2 novembre 2026

Ouvrir `C85-apercu-autonome.html` : leçon native avec deux images originales CC BY 4.0, quatre occurrences et légendes françaises reliées aux repères du scanner et aux panneaux histologiques. Aucun pixel original modifié.

Le plan monographique à 14 points et les 20 rubriques ont une auto-revue attribuée, avec quarante lectures ciblées documentées. Six disciplines scientifiques, neuf sections de sémiologie, 56 fenêtres et cinq quiz. Les limites L1–L6 restent explicites ; aucune validation médicale humaine n’est revendiquée.

`verification.json` et `source-binding.json` rattachent les six étapes réelles (statique, sciences, Betta, construction, assemblage autonome, navigateur) aux octets des sources et de l’aperçu. Les captures finales ont été inspectées. Le test G2 distingue le repère pédagogique de la catégorie rénale du glossaire ; les césures visuelles sont normalisées dans l’assertion, sans retirer ce contrôle.

`reserves.json` garde les sept réserves de la première version et leur résolution documentée. `limitations.json` conserve notamment l’unité hépatique Endoxan inutilisable, la borne doxorubicine, l’absence d’incidence suisse isolée et la portée du codage 2024. Aucun nombre douteux n’est transformé en règle posologique.

## Reproduction

Exécuter `verify_c85.py` depuis ce worktree avec les dépendances de construction Medina, Playwright et Chromium. Dans cet environnement, les dépendances isolées disponibles sont `/tmp/medina-n29-pydeps` (via PYTHONPATH). Le script utilise le moteur natif et le constructeur autonome du harness. Il ne modifie pas les sources médicales, ne pousse pas de branche et ne ferme pas de mission.

Les scripts de migration et d’enregistrement décrivent les décisions de cette reprise. Ne pas rejouer une ancienne migration ou `record_evidence.py` sur une version plus récente : ils ne remplacent pas les sources canoniques ni une nouvelle relecture. `package_revision2.py` vérifie les empreintes avant d’assembler cette revue précise ; il ne génère pas un avis médical.

## Revue et publication

La branche demeure une version de travail pour présentation à Vial. Aucune PR, fusion ou écriture sur main n’a été effectuée. Le reçu `harness-completion.json`, lorsqu’il existe, décrit l’achèvement de projet ; il ne vaut ni publication sur main ni certification clinique. Les compteurs et bandeaux historiques du frontend natif restent ceux de la base et ne remplacent pas l’état du harness.
''')
    print(json.dumps({'packaged':True,'sources':len(source['sources']),'preview_sha256':verify['preview_sha256'],'clinical_certification':False}))
if __name__=='__main__':main()
