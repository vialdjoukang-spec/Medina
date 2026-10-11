# I63 — ajout conditionnel ; ne remplace aucune clé partagée.
from cardio_1 import a, G
def _a(k,lit,full,d='',ref=None):
    if k not in G:
        a(k,lit,full,d,ref)
_a('AVC',[('A', 'Accident'), ('V', 'Vasculaire'), ('C', 'Cérébral')],'Accident vasculaire cérébral','<p>Déficit neurologique aigu d’origine vasculaire ; l’imagerie distingue infarctus et hémorragie.</p>','i63-imagerie')
_a('AIT',[('A', 'Accident'), ('I', 'Ischémique'), ('T', 'Transitoire')],'Accident ischémique transitoire','<p>Déficit focal transitoire sans lésion en diffusion selon la définition tissulaire bernoise 2026 ; évaluation urgente.</p>','i63-ait')
_a('NIHSS',[('N', 'National'), ('I', 'Institutes of'), ('H', 'Health'), ('S', 'Stroke'), ('S', 'Scale')],'National Institutes of Health Stroke Scale','<p>Instrument standardisé décrivant le déficit neurologique ; le total ne remplace pas le caractère invalidant ni la localisation.</p>','i63-nihss')
_a('FLAIR',[('FL', 'FLuid (liquide)'), ('A', 'Attenuated (atténué)'), ('I', 'Inversion'), ('R', 'Recovery (récupération)')],'Fluid-attenuated inversion recovery','<p>Séquence de résonance magnétique dont la comparaison à la diffusion contribue à certaines sélections de début inconnu.</p>','i63-imagerie')
_a('NOTCH3',[('NOTCH', 'nom de la famille de récepteurs Notch, non acronyme lettre par lettre'), ('3', 'membre 3')],'Notch receptor 3','<p>Symbole de gène ; la maladie monogénique correspondante se recherche sur un profil clinique et radiologique ciblé.</p>','i63-etiologie')
_a('GLA',[('GLA', 'symbole officiel du gène de la galactosidase alpha ; non développement littéral des trois lettres')],'Galactosidase alpha','<p>Gène associé à la maladie de Fabry ; la sélection clinique du bilan est spécialisée.</p>','i63-etiologie')
_a('AcT',[('A', 'Alteplase'), ('c', 'Compared to'), ('T', 'Tenecteplase')],'Alteplase Compared to Tenecteplase','<p>Nom de l’essai décrit par la FI suisse de Metalyse ; population éligible à la thrombolyse dans les 4,5 heures.</p>','i63-metalyse')
_a('ECASS-III',[('E', 'European'), ('C', 'Cooperative'), ('A', 'Acute'), ('S', 'Stroke'), ('S', 'Study'), ('III', 'troisième étude')],'European Cooperative Acute Stroke Study III','<p>Essai européen décrit dans la FI Actilyse ; sélection et résultats figurent dans la fenêtre.</p>','i63-actilyse')
_a('SPARCL',[('S', 'Stroke'), ('P', 'Prevention by'), ('A', 'Aggressive'), ('R', 'Reduction in'), ('C', 'Cholesterol'), ('L', 'Levels')],'Stroke Prevention by Aggressive Reduction in Cholesterol Levels','<p>Essai décrit dans la FI Sortis ; bénéfice préventif et analyses hémorragiques sont distingués.</p>','i63-sortis')
