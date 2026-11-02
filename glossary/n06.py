from cardio_1 import a,G
# N06 — ajouts conditionnels, aucun ancien glossaire modifié.
if 'ACR' not in G:
    a('ACR',[('A','Albumine'),('CR','Créatinine')],'Rapport albumine/créatinine urinaire','<p>Quantifie l’albumine rapportée àla créatinine dumême prélèvement ; unitéet conditions visibles. Distinct desprotéinestotales et d’unecollecte24hmesurée.</p>','n06-calcul-ratio')
if 'RPC' not in G:
    a('RPC',[('P','Protéines'),('CR','Créatinine')],'Rapport protéines/créatinine urinaire','<p>Quantifie lesprotéinestotales rapportées àla créatinine ; le contexte distingue cette abréviation de la technique d’amplificationmoléculaire.</p>','n06-exp-8')
