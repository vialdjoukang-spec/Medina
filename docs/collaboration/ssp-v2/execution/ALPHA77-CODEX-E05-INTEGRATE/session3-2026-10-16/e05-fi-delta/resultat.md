# E05 — delta ciblé FI des quatre options secondaires, 16 octobre 2026

Lecture seule du candidat `721b86af6bde93f751d8e785e1506b1836841b32`, branche `codex/alpha77/e05-integrate-g1`, S05/E05. Aucun acquire/START, réservation, branche, reçu ou fichier source/MED/SEMIO modifié. Le candidat est resté propre. Aucune validation humaine ni clôture médicale globale.

## Constat de périmètre

Les sept core ont été parcourus pour les noms des immunomodulateurs. **Ciclosporine, azathioprine, rituximab et tocilizumab sont chacun cités une seule fois**, `chapters/E05/E05_b.html`, paragraphe sous `e05-a10-partie-3`, ligne41. Cette phrase décrit la deuxième ligne EUGOGO2021 ; elle n'enseigne aucune dose, voie ni produit exact pour ces quatre molécules. Elle associe correctement ciclosporine/azathioprine à un corticoïde oral. Son fond européen est déjà établi par `final-claim-mapping.json#FINAL-EUGOGO`, passage réel conservé, sans nouvelle lecture EUGOGO revendiquée.

Myfortic et Tepezza sont déjà documentés (`FINAL-MYFORTIC`, `FINAL-TEPEZZA`, `DELTA-MYFORTIC-FI` et S6/S29 du dossier de recherche). Ils n'ont pas été relus sur le réseau. Aucun médicament absent ajouté au périmètre. Pas de réaudit BWPS, hydrocortisone, JTA, EUGOGO, OFS ou Manuel2026.

## Sources primaires réellement lues

Les quatre pages Compendium ont été ouvertes dans Chromium réel via le proxy hérité, TLS vérifié, sans accès professionnel ni contournement. Elles indiquent « Information professionnelle approuvée par Swissmedic ». Les pages AmiKo ont d'abord servi à identifier les présentations, puis les **rubriques Compendium** ont été lues et conservées. Les références sont des produits de référence choisis pour les molécules citées ; ils ne sont pas des produits déjà prescrits dans le cours.

| Molécule → produit exact | FI / numéro Swissmedic | Indications complètes lues et conclusion limitée |
|---|---|---|
| Ciclosporine → [Sandimmun Neoral oral, capsules25mg](https://compendium.ch/fr/product/37688-sandimmun-neoral-caps-25-mg/mpro), GTIN7680526560283 | Janvier2026 ;52656 (capsules),52657 (solution) ; référence affichée4865/03.03.2026 | Transplantation d'organes/moelle et GvHD ; uvéites définies, psoriasis sévère, dermatite atopique sévère, polyarthrite chronique sévère, syndrome néphrotique défini. Pas d'orbitopathie dans cette liste. |
| Azathioprine → [Imurek oral, comprimés25mg](https://compendium.ch/fr/product/1304567-imurek-cpr-pell-25-mg/mpro), GTIN7680318870460 | Avril2026 ;31887 ; DOC-26-06-2026 et21027/10.07.2026 | Prévention du rejet de greffe et huit maladies explicitement nommées : PR sévère, lupus viscéral, dermatomyosite/polymyosite, hépatite auto-immune, pemphigus, périartérite noueuse, anémie hémolytique auto-immune, PTI chronique réfractaire. «Dans les maladies suivantes» ne constitue pas une catégorie ouverte de toute maladie auto-immune. Pas d'orbitopathie listée. |
| Rituximab → [MabThera concentré pour perfusion IV100mg/10ml](https://compendium.ch/fr/product/1098021-mabthera-conc-perf-100-mg-10ml/mpro), GTIN7680543780176 | Décembre2025 ;54378 ; référence7715/31.03.2026 | Indications hémato-oncologiques détaillées, PR dans les conditions nommées, GPA/PAM et pemphigus vulgaire. Pas d'orbitopathie listée. FI IV, produit distinct de MabThera sous-cutané. |
| Tocilizumab → [Actemra concentré pour perfusion IV80mg/4ml](https://compendium.ch/fr/product/1110447-actemra-conc-perf-80-mg-4ml/mpro), GTIN7680588680011 | Septembre2026 ;58868 pour IV ; FI groupée cite aussi63166/66931 pour SC ; référence20040/05.10.2026 | PR, ACG (SC), AJI polyarticulaire/systémique avec limites d'âge/voie explicites, syndrome de relargage cytokinique induit par CAR-T (IV). Pas d'orbitopathie listée. Les formes IV/SC ne sont pas interchangeables. |

Le mois de FI, la référence éditoriale Compendium et le numéro Swissmedic sont trois informations distinctes. **Aucune date initiale d'autorisation n'a été établie ici.** Les indications détaillées, populations, citations intégrales, sections et lignes sont dans `source-readings.json` et les quatre fichiers `*-primary.txt`.

La lecture complète des rubriques d'indications montre des listes circonscrites sans orbitopathie ; elle ne justifie pas de prétendre que toute maladie auto-immune serait autorisée. L'emploi orbitaire de ces produits doit donc être distingué des indications listées dans leur FI et examiné dans le cadre hors AMM. Ceci ne constitue pas une expertise réglementaire de toutes les spécialités/génériques/biosimilaires ni une décision de remboursement. La recommandation de deuxième ligne vient de l'EUGOGO, pas de ces FI.

## Posologie et sécurité : portée de la vérification

Aucune dose orbitaire n'est proposée pour ces quatre molécules dans les sept core. Les introductions de posologie confirment la voie orale de Sandimmun Neoral et Imurek, la perfusion IV de MabThera, et la séparation IV/SC d'Actemra. **Les doses de greffe, rhumatologie ou oncologie ne doivent pas être transférées à l'orbite.** Aucun schéma EUGOGO secondaire n'est certifié par ce delta.

Les rubriques complètes «Contre-indications» ont été lues. Points à conserver si une fenêtre pharmacologique est ultérieurement ajoutée :

- Sandimmun Neoral : hypersensibilité ; hors transplantation, insuffisance rénale avec exception néphrotique strictement définie, HTA insuffisamment contrôlée, infections insuffisamment contrôlées et malignité avec exception cutanée après traitement curatif. La surveillance rénale/hépatique et de la pression artérielle est décrite dans les mises en garde.
- Imurek : hypersensibilité à l'azathioprine,6-mercaptopurine ou excipients. La surveillance hématologique et les risques TPMT/NUDT15 sont dans les **mises en garde**, pas des contre-indications génériques inventées. La FI exige une formule sanguine hebdomadaire pendant les8premières semaines puis au moins tous les3mois ; ce repère n'est pas injecté dans le cours.
- MabThera IV : hypersensibilité, insuffisance cardiaque NYHAIV ; contre-indication grossesse/allaitement de l'association rituximab avec chimiothérapie, y compris MTX, formulée dans ce contexte exact. Les infections virales sévères et l'hépatite B active excluent le traitement selon les **mises en garde** ; dépistage VHB avant traitement (au moins HBsAg et anti-HBc). La structure suisse est préservée sans copier une liste européenne.
- Actemra : hypersensibilité ; association avec anti-TNF simultanément et jusqu'à1mois après anticorps anti-TNF. Infection active déconseillée et tuberculose latente à rechercher/traiter dans les **mises en garde** ; risques hépatiques et de perforation diverticulaire. L'inhibition IL-6 peut atténuer CRP et réponse inflammatoire, ce qui limite leur interprétation devant une infection.

Ces points de sécurité expliquent les limites d'une simple énumération ; leur revue n'est pas une monographie exhaustive, notamment pour interactions, grossesse, monitoring complet ou cumul de traitements.

## Correction concrète proposée, non appliquée

La phrase actuelle n'est pas démontrée fausse sur la place EUGOGO. Le manque précis est l'absence de lien explicite avec les FI suisses de ces quatre options. Ajouter après l'énumération, avant la phrase sur Tepezza, un paragraphe court :

> La place de la ciclosporine, de l'azathioprine, du rituximab et du tocilizumab en deuxième ligne vient de l'EUGOGO. L'orbitopathie ne figure pas parmi les indications énumérées par les FI suisses consultées de Sandimmun Neoral, Imurek, MabThera intraveineux et Actemra. Ces FI ne fournissent donc pas une posologie orbitaire ; leurs doses d'autres indications ne doivent pas être transposées. L'emploi de ces produits dans ce cadre demande une décision du centre spécialisé intégrant le cadre hors AMM et la sécurité propre au produit.

Accompagner ce texte des quatre liens Compendium ci-dessus, avec consultation16octobre2026 et mois de FI distincts. Ne pas ajouter de dose ou d'affirmation de remboursement ; ne pas promouvoir ces quatre produits de référence au rang de prescription imposée. Le coordinateur décidera de l'application sous son mandat source.

## Sous-point établi et réserve restante

**Établi : les quatre FI de produits de référence correspondant exactement aux quatre molécules secondaires réellement nommées ont maintenant été obtenues et lues dans les rubriques ciblées, avec preuves traçables.** La réserve «FI exactes secondaires non exhaustives» peut être précisée à ce périmètre documentaire ; aucun avis médical favorable global ne s'en déduit.

Restent ouverts : décision/source finale à intégrer et relecture sur ses nouvelles empreintes ; choix du produit réellement prescrit, éventuel protocole spécialisé orbitaire et sécurité complète de cette prescription, disponibilité et remboursement applicables. Toutes les autres réserves REMAINING-PROOF restent indépendantes et inchangées. Les preuves/reçus0001 et le travail Claude sont préservés.

Fichiers probants : `source-readings.json`, `claim-mapping.json`, `integrity.json`, `compendium-fi-access.json`, les HTML/textes primaires et les extraits intégraux d'indications/contre-indications. Le hash SHA256 des preuves et des7core figure dans `integrity.json`.
