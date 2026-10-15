# I64 — Accident vasculaire cérébral, non précisé comme étant hémorragique ou par infarctus (N-05-Neurologie)

Dossier de recherche, cycle Betta 31, agent C31-A1-NEUR (Opus 5.5), 14.10.2026.
Chaque fait est suivi de sa source (S1–S19, voir `sources.json`). Rien n'est écrit de mémoire. Ce qui n'a pas été trouvé figure dans les **lacunes**.

---

## 0. Question clinique et angle pédagogique

I64 est le code d'un AVC dont la nature (hémorragie ou infarctus) **n'a pas été établie**. Pour le clinicien, c'est la situation des premières minutes. Le patient a un déficit neurologique brutal, et aucune imagerie n'a encore tranché. Toute la conduite consiste à transformer cet AVC « indifférencié » en diagnostic précis, le plus vite possible. Les deux traitements urgents sont en effet opposés : thrombolyse pour l'infarctus, contrôle tensionnel et correction de l'hémostase pour l'hémorragie.

Fil conducteur proposé : reconnaître → ne pas nuire avant l'imagerie → imager → orienter vers I63 (infarctus) ou I61/I62/I60 (hémorragies).

## 1. Définition et classification (CIM-10-GM)

- **I64** : « Schlaganfall, nicht als Blutung oder Infarkt bezeichnet ». Inclusion : « Zerebrovaskulärer Insult o.n.A. » (AVC sans autre précision). Exclusion : les séquelles d'un tel AVC se codent **I69.4** (« Folgen eines Schlaganfalls, nicht als Blutung oder Infarkt bezeichnet »). [S1]
- Bloc I60–I69 (maladies cérébrovasculaires) : une hypertension associée se code en plus. Sont exclus du bloc l'hémorragie intracrânienne traumatique (S06.-), la démence vasculaire (F01.-) et l'ischémie cérébrale transitoire (G45.-). [S1]
- **Sous-codes couverts** : I64 n'a pas de sous-code dans la CIM-10-GM 2024 (catégorie terminale). Le registre de nosologie MEDINA (`nosology/fragments/S08.json`) liste bien `codes: ["I64"]`. [S1]
- Les codes voisins, à orienter après imagerie : I60 (hémorragie sous-arachnoïdienne), I61 (hémorragie intracérébrale), I62 (autres hémorragies intracrâniennes non traumatiques), I63 (infarctus cérébral). L'étude épidémiologique suisse définit l'« AVC aigu » par ces codes I60–I64 et exclut I65–I69. [S2]

## 2. Épidémiologie (Suisse d'abord)

Source principale : Hänsel et al., 2025, d'après les données OFS de 2017 (statistique médicale des hôpitaux, HOST ; statistique des causes de décès, CoD). [S2]

| Indicateur (Suisse, 2017) | Valeur | Source |
|---|---|---|
| Sorties d'hôpital pour AVC (I60–I64) | 26 032 (45 % de femmes) ; 13 996 en 2004 | S2 |
| Événements AVC estimés | 26 879 ; taux standardisé 325,0/100 000 | S2 |
| Décès par AVC | 2816 (59 % de femmes) ; 3568 en 2004 | S2 |
| Taux de mortalité brut | femmes 38,5/100 000 (77,5 en 2004) ; hommes 27,2/100 000 (56,1 en 2004) | S2 |
| Taux de mortalité standardisé (population européenne) | 33,7/100 000 | S2 |
| Létalité globale | 10,5 % (22,7 % en 2004) ; femmes 13,4 %, hommes 8,0 % | S2 |
| Létalité hospitalière / extrahospitalière | 7,3 % / 3,2 % (extrahospitalière 11,0 % en 2004) | S2 |
| Part des décès survenus hors de l'hôpital | 30,1 % (48,7 % en 2004) | S2 |

- Les taux de sortie augmentent avec l'âge ; ils sont plus élevés chez l'homme entre 35 et 85 ans et au-delà. Au-delà de 85 ans, la mortalité est plus élevée chez la femme (715,8 contre 661,4/100 000). [S2]
- Interprétation des auteurs : la hausse des diagnostics s'explique surtout par un codage plus systématique depuis SwissDRG (2012), une meilleure connaissance des symptômes et un meilleur accès au diagnostic. Une augmentation réelle de l'incidence n'est pas exclue (hypertension, obésité, hypercholestérolémie en hausse de 2007 à 2017). [S2]
- Les auteurs attribuent la baisse de mortalité, entre autres facteurs, aux stroke units certifiées, aux réseaux de télé-AVC et à la standardisation de la chaîne de soins. [S2]
- Limite essentielle : les bases HOST et CoD ne peuvent pas être reliées, si bien que l'incidence vraie et la distinction premier AVC / récidive sont impossibles. [S2]
- Part de l'hémorragie intracérébrale : 28,8 % de tous les AVC dans le monde en 2019 (3,41 millions de cas). [S6]

## 3. Mécanismes : du normal au pathologique

- **Pourquoi la nature de l'AVC compte** : la différenciation entre infarctus et hémorragie est « la première étape la plus importante », car la prise en charge des deux affections diffère profondément. [S7]
- **Infarctus — dépendance au temps** : dans un AVC ischémique typique d'un gros vaisseau supratentoriel (volume final moyen 54 ml, constitution en environ 10 h), le cerveau perd environ 1,9 million de neurones, 14 milliards de synapses et 12 km de fibres myélinisées **par minute** sans traitement. Cela correspond à 120 millions de neurones par heure, soit un vieillissement cérébral de 3,6 ans par heure. [S15] Conséquence pratique : le bénéfice de la thrombolyse diminue avec le délai. [S13]
- **Pénombre / « mismatch »** : la sélection au-delà de 4,5 h ou au réveil repose sur un décalage entre le cœur de l'infarctus et le tissu hypoperfusé (perfusion CT ou IRM). Elle peut aussi reposer sur une discordance DWI-FLAIR à l'IRM. [S3] Lacune : aucune source primaire de physiopathologie de la pénombre n'a été lue (voir lacunes).
- **Hémorragie — expansion de l'hématome** : l'expansion de l'hématome est associée à un pronostic fonctionnel plus mauvais et à la mort. [S6] Une baisse tensionnelle précoce (< 6 h) est associée à moins d'expansion (OR 0,76, faible certitude). [S6]
- **Pourquoi l'imagerie précède tout traitement spécifique** : un même geste a des effets opposés selon la nature de l'AVC. En préhospitalier, la baisse tensionnelle intensive (INTERACT4, urapidil, cible PAS 130–140 mmHg, n = 2303) n'a pas d'effet global (OR commun 1,00). Elle montre un bénéfice possible dans l'hémorragie et un **préjudice possible dans l'infarctus** (OR commun 1,30). Avec la trinitrine transdermique (RIGHT-2), l'expansion de l'hématome augmentait dans l'hémorragie (46 % contre 27 %). [S5]

## 4. Causes et terrain

- I64 n'est pas une cause : c'est une **étiquette d'incertitude** sur la nature de l'AVC. Les causes appartiennent aux catégories précisées, I61/I62 et I63. [S1]
- Facteurs de risque dont la prévalence a augmenté en Suisse de 2007 à 2017 : hypertension, obésité, hypercholestérolémie, troubles du sommeil. [S2]
- Lacune : aucun registre suisse lu ne quantifie la part réelle des AVC restés codés I64 (ni sa diminution avec l'accès à l'imagerie).

## 5. Anamnèse

- Heure de début ou **dernier moment connu sans symptômes** : les deux AMM suisses en font le point de départ de la fenêtre de 4,5 h. [S13, S14]
- Réveil avec déficit ou heure inconnue : la thrombolyse reste possible avec une sélection par imagerie (voir § 9). [S3]
- Médicaments : anticoagulant oral (AVK et INR ; AOD et heure de la dernière prise), héparine dans les 48 h, antiagrégants. [S3, S13, S14]
- Antécédents qui contre-indiquent la thrombolyse ou la rendent délicate : hémorragie intracrânienne, traumatisme crânien ou chirurgie intracrânienne ou rachidienne récents, chirurgie majeure < 10 jours, accouchement < 10 jours, ulcère actif, AVC antérieur. Une convulsion au début de l'AVC est aussi à rechercher. [S13, S14, S3]
- Symptômes d'alerte grand public en Suisse : il faut appeler le **144** sans délai. [S19]

## 6. Examen clinique

- Le score NIHSS (National Institutes of Health Stroke Scale) quantifie la sévérité. L'IP Actilyse cite un NIHSS > 25 comme exemple d'AVC « sévère » contre-indiquant l'altéplase. Les recommandations européennes ne retiennent **aucune limite supérieure de NIHSS** pour la thrombectomie. [S13, S4]
- Pression artérielle et glycémie capillaire : elles conditionnent l'éligibilité à la thrombolyse (seuil < 185/110 mmHg ; glycémie, voir § 9). [S3, S5]
- **Les scores cliniques ne remplacent pas l'imagerie** pour séparer hémorragie et infarctus :
  - à Glasgow (1059 patients), le score de Guy's Hospital (13 variables) atteint une sensibilité de 70 % et une spécificité de 64 % pour l'hémorragie. Le score de Siriraj (5 variables) atteint 68 % et 64 %, pour une précision globale de 64 % dans les deux cas. Aucun des deux ne suffit pour exclure une hémorragie avant un anticoagulant ou de l'aspirine. [S7]
  - dans une étude indienne de 91 patients, les scores d'Allen, de Siriraj et grec manquent tous de précision pour guider la prise en charge. [S8]

## 7. Diagnostic : l'imagerie qui fait sortir de I64

- Consensus ESO–ESMINT : tout patient suspect d'AVC doit avoir une **imagerie cérébrale en urgence, y compris vasculaire**. [S4]
- La thrombolyse exige d'**exclure une hémorragie intracrânienne** par une imagerie adéquate. [S13, S14]
- Dans les 6 premières heures, l'imagerie avancée n'est pas nécessaire pour sélectionner la thrombectomie (recommandation faible). Au-delà de 6 h, elle est nécessaire (forte). [S4]
- Un scanner sans contraste peut être normal très tôt après un AVC ischémique ; un CT multimodal ou une IRM aident à confirmer l'infarctus et à écarter un simulateur. [S20]
- Biologie avant thrombolyse : plaquettes, INR (AVK), activité anti-Xa ou temps de thrombine (AOD), glycémie (seuils, § 9). [S3, S13]
- Norme organisationnelle suisse (critères Swiss Stroke Society 2012) : CT ou IRM cérébrale dans les **25 minutes** après l'arrivée en stroke unit. [S11]

## 8. Diagnostic différentiel : simulateurs d'AVC (« stroke mimics »)

- À Essen (2167 AVC suspectés amenés par les secours, 2017–2021), **35,2 %** étaient des simulateurs. Leur origine était neurologique dans 51,6 % des cas et non neurologique dans 48,4 %. Les diagnostics les plus fréquents étaient les crises épileptiques (23,2 %) et les infections (14,7 %). [S16]
- Une insuffisance rénale ou hépatique chronique prédit un simulateur ; une fibrillation atriale ou une hypertension rendent un vrai AVC plus probable. [S16]
- Sécurité : chez 392 simulateurs thrombolysés (méta-analyse de 9 études), l'hémorragie intracérébrale symptomatique était de 0,5 % et l'œdème orolingual de 0,3 %. [S17] D'où la règle de ne pas retarder la thrombolyse pour exclure un simulateur peu probable.
- Les adolescents de 16 ans ou plus ne sont traités qu'après confirmation de l'AVC (exclusion des « stroke mimics »). [S13]
- Une convulsion au début de l'AVC, sans simulateur suspecté ni traumatisme crânien, n'empêche pas l'altéplase (suggestion faible). [S3]

## 9. Urgences et prise en charge suisse

### 9.1 Préhospitalier
- Il faut appeler le 144. [S19]
- **Ne pas baisser la pression artérielle de routine en préhospitalier** devant un AVC suspecté, donc encore indifférencié (certitude modérée). [S5]
- Les unités mobiles d'AVC (ambulance avec scanner, laboratoire délocalisé et télémédecine) sont suggérées par l'ESO. Elles améliorent le pronostic à 90 jours dans l'infarctus, raccourcissent le délai jusqu'au traitement et orientent plus d'hémorragies vers un centre tertiaire. [S10] En 2025, elles se sont révélées coût-efficaces dans les systèmes à haut volume. [S9]
- Aucune échelle préhospitalière de détection d'occlusion n'est recommandée (qualité très basse). Le choix entre transfert direct au centre (« mothership ») et transfert secondaire (« drip-and-ship ») dépend de l'organisation locale. [S4]

### 9.2 Organisation suisse
- Il existe deux niveaux, la **Stroke Unit (SU)** et le **Stroke Center (SC)**. Le SC ajoute à la SU des prestations neuroradiologiques et neurochirurgicales spécialisées. [S11]
- Critères de la Swiss Stroke Society (2012) :
  - neurologue présent 10 h par jour ;
  - thrombolyse disponible 24 h sur 24 ;
  - transfert vers neurochirurgie ou neuroradiologie interventionnelle en moins de 60 min ;
  - au moins 6 lits, dont 3 monitorés ;
  - au moins 200 admissions et 20 traitements de recanalisation par an ;
  - registre des AVC. [S11]
- La certification est coordonnée par la SFCNS sous mandat IVHSM. Des critères Stroke Center datés du 18.11.2021 sont en vigueur. [S12]
- Il est fortement recommandé de traiter l'HIC en unité cérébrovasculaire organisée (RR de décès ou dépendance 0,79 dans le sous-groupe HIC). [S6]

### 9.3 Une fois l'imagerie faite : branche infarctus (→ I63)
- **Altéplase IV < 4,5 h** : recommandation forte, qualité élevée. Dose 0,9 mg/kg (maximum 90 mg), dont 10 % en bolus puis le reste en 60 min. La dose standard est préférée à la dose réduite (forte). [S3, S13]
- **Ténectéplase** : en Suisse, Metalyse 5000 U est autorisé dans l'AVC ischémique < 4,5 h, en dose unique ajustée au poids (maximum 25 mg ; par exemple 15 mg si < 60 kg). [S14] Dans l'essai AcT, la ténectéplase 0,25 mg/kg était non inférieure à l'altéplase (mRS 0–1 : 36,9 % contre 34,8 %). [S14] L'ESO suggérait en 2021 la ténectéplase 0,25 mg/kg plutôt que l'altéplase avant thrombectomie. [S3] La synthèse ESO 2025 renforce la ténectéplase comme thrombolyse de pont avant thrombectomie. [S9]
- Fenêtre 4,5–9 h : thrombolyse si mismatch cœur/perfusion (forte, faible qualité). Pas de thrombolyse avec un scanner sans contraste seul (forte). [S3]
- Réveil ou heure inconnue : thrombolyse si mismatch DWI-FLAIR (forte, qualité élevée), ou si mismatch de perfusion dans les 9 h après le milieu du sommeil. [S3]
- Âge > 80 ans : thrombolyse recommandée ; l'âge seul n'est pas une limite. [S3] IP : évolution favorable 18 % contre 13 % (OR 1,56) ; hémorragie symptomatique 8,9 % contre 2 %. [S13]
- AVC mineur : thrombolyse s'il est invalidant (forte) ; pas de thrombolyse s'il n'est pas invalidant (faible). [S3] L'IP Metalyse contre-indique l'AVC sans déficit invalidant. [S14]
- Seuils :
  - PA < 185/110 mmHg avant le bolus, puis < 180/105 mmHg pendant et 24 h après la thrombolyse ou la thrombectomie [S5, S3] ;
  - pas de baisse de la PAS < 140 mmHg dans les 24 h après une thrombectomie réussie (certitude élevée) [S5] ;
  - glycémie > 22,2 mmol/l : thrombolyse suggérée (très basse qualité) [S3] ;
  - plaquettes < 100 × 10⁹/l : pas de thrombolyse ; plaquettes non connues sans raison de les suspecter anormales : débuter sans attendre [S3, S13] ;
  - microsaignements > 10 : pas de thrombolyse suggérée ; pas de dépistage IRM systématique des microsaignements [S3].
- Anticoagulants :
  - AVK : INR ≤ 1,7 → thrombolyse selon l'ESO ; INR > 1,7 ou inconnu → pas de thrombolyse [S3]. **Divergence** : les deux IP suisses contre-indiquent la thrombolyse sous AVK avec un INR > 1,3 [S13, S14] (contentieux à présenter, le texte d'AMM suisse faisant foi pour l'usage autorisé) ;
  - AOD < 48 h sans dosage spécifique → pas de thrombolyse. Avec anti-Xa < 0,5 U/ml ou temps de thrombine < 60 s → thrombolyse possible par consensus. Dabigatran : idarucizumab puis thrombolyse (consensus 8/9) [S3].
- Pas d'antithrombotique dans les 24 h suivant la thrombolyse (ESO, forte ; IP). [S3, S13, S14]
- Effets indésirables : hémorragie intracrânienne « très fréquente » dans l'AVC (NINDS 15,4 %, ECASS III 14,1 %, toutes hémorragies confondues). L'angio-œdème est majoré par les IEC. [S13, S14]
- **Thrombectomie** :
  - occlusion d'un gros vaisseau < 6 h → thrombectomie + meilleur traitement médical, y compris thrombolyse si indiquée (forte, qualité élevée) ;
  - 6–24 h selon les critères DAWN/DEFUSE-3 (forte, modérée) ;
  - pas de limite d'âge ni de NIHSS ; ASPECTS ≥ 6 ou cœur ≤ 70 ml dans les 6 h ;
  - prise en charge en centre complet. [S4]
  - En 2025, trois essais n'ont montré aucun bénéfice de la thrombectomie dans les occlusions de vaisseaux moyens (MeVO). [S9]
  - Occlusion basilaire : thrombolyse jusqu'à 24 h par consensus ; thrombectomie suggérée si NIHSS ≥ 10. [S18]

### 9.4 Une fois l'imagerie faite : branche hémorragie (→ I61/I62)
- Consensus ESO 2025 : abaisser précocement la PAS sous 140 mmHg en cas d'hématome petit à modéré, pour limiter l'expansion. Le bénéfice clinique net reste incertain. [S5]
- L'acide tranexamique réduit l'expansion à 24 h (OR 0,82), sans effet sur décès ou dépendance à 90 jours. [S6]
- Antagonisation des anticoagulants : voir I61/I62. Lacune ici (recommandations non lues).

## 10. Suivi

- Le suivi relève du code final (I63 ou I61/I62). Les séquelles d'un AVC resté non précisé se codent I69.4. [S1]
- Normes suisses de 2012 : physiothérapie dans les 24 h, ergothérapie et logopédie dans la journée ouvrable, évaluation de la déglutition disponible 24 h sur 24. [S11]
- Lacune : prévention secondaire non traitée ici, car elle dépend du type d'AVC.

## 11. Situations particulières

- Âge avancé : voir § 9.3. [S3, S13]
- Adolescents : altéplase contre-indiquée avant 16 ans ; traitement possible dès 16 ans après exclusion des simulateurs. [S13]
- Antécédent d'AVC ischémique < 3 mois : thrombolyse dans des cas choisis par consensus (petit infarctus, AVC > 1 mois, bonne récupération). [S3]
- Accouchement < 10 jours : contre-indication à l'altéplase. [S13] Lacune : grossesse non lue dans S3.

## 12. Critères formels (pour l'îlot `div.alert`)

1. Déficit neurologique d'apparition brutale, attribué à une cause cérébrovasculaire. Lacune : définition formelle de l'AVC (OMS ou ESO) non lue ; ne pas inventer de libellé.
2. Nature hémorragique ou ischémique **non établie** : pas d'imagerie, ou imagerie indisponible ou non concluante. C'est le critère qui fait coder I64 (« Zerebrovaskulärer Insult o.n.A. »). [S1]
3. Exclusions : traumatisme (S06.-), ischémie transitoire (G45.-), séquelles (I69.4). [S1]
4. Sortie de I64 : imagerie cérébrale en urgence (avec imagerie vasculaire) → I63, ou I60/I61/I62. [S4, S1]

## 13. Paramètres clés (pour `div.key`)

| Paramètre | Valeur | Source |
|---|---|---|
| Neurones perdus par minute d'ischémie non traitée | ≈ 1,9 million | S15 |
| Fenêtre de thrombolyse autorisée (AMM CH) | ≤ 4,5 h après le dernier état asymptomatique | S13, S14 |
| Altéplase | 0,9 mg/kg, max 90 mg, 10 % en bolus, 90 % en 60 min | S13 |
| Ténectéplase | 0,25 mg/kg, max 25 mg, bolus unique | S14 |
| PA avant / après thrombolyse | < 185/110 / < 180/105 mmHg (24 h) | S5 |
| PA préhospitalière | pas de baisse de routine | S5 |
| PAS dans l'HIC petite à modérée | < 140 mmHg (consensus) | S5 |
| Plaquettes | ≥ 100 × 10⁹/l | S3, S13 |
| INR sous AVK | ESO ≤ 1,7 ; IP suisses : contre-indication > 1,3 | S3, S13 |
| Thrombectomie | < 6 h ; 6–24 h si critères DAWN/DEFUSE-3 | S4 |
| Simulateurs parmi les AVC suspectés | ≈ 35 % (Essen) | S16 |
| Précision des scores cliniques (Siriraj, Guy's) | ≈ 64 % | S7 |
| Létalité de l'AVC en Suisse (2017) | 10,5 % | S2 |
| Imagerie en stroke unit (norme CH 2012) | ≤ 25 min | S11 |

## 14. Lacunes explicites

1. **Définition formelle de l'AVC** (OMS/ESO) non lue.
2. **Critères SFCNS en vigueur** (18.11.2021) non lus ; seuls les critères 2012 (S11) le sont. Le nombre actuel de SU/SC en Suisse n'est pas sourcé.
3. **Lignes directrices propres à la Swiss Stroke Society** (au-delà de la certification) : aucune n'a été trouvée.
4. **Physiopathologie de la pénombre** : pas de source primaire lue (S15 donne seulement la quantification du temps).
5. **Proportion suisse** infarctus / hémorragie et part des AVC codés I64 : non trouvées (seul le chiffre mondial de S6 est disponible).
6. ESO ICH 2025 : **antagonisation des anticoagulants** non lue (recommandations en images).
7. Buck et al. 2021 (S20) : résumé seul ; « près de la moitié des admissions » est une estimation de revue narrative, à préférer S16 (35,2 %).
8. Thrombolyse et grossesse ; recommandations ESO 2023 dédiées à la ténectéplase non lues (seule la synthèse 2025 l'a été).
9. Données Swiss Stroke Registry sur les délais (porte-aiguille) : non lues.
