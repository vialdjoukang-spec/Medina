# Contrelecture du delta — I83 — Varices des membres inférieurs (C-01-Cardiologie)

**Décision au SHA `20c67c011e57eccd25b105b15f465becf7df7f2e` : avis favorable à l’injection sélective dans le périmètre Pharmacologie relu. PH-01 reste résolue ; PH-02 est résolue ; la procédure intra-artérielle est fidèle aux extraits suisses nouvellement fournis. Aucun bloqueur médical prouvé ne reste dans ce périmètre.** Cette décision ne remplace ni les autres audits du chapitre ni les contrôles techniques indépendants. Ce poste n’effectue aucune injection.

Date : 8 octobre 2026. Base de comparaison : `20bee19a6329f0a62126e9180bfc909207055e38`. Les preuves et constats historiques de [l’audit initial](AUDIT_PHARMACOLOGIE.md) sont conservés ; le présent rapport donne l’état ultérieur.

## Périmètre effectivement contrevérifié

Lecture réelle du diff Git entre les deux SHA, des passages de cohérence et des **26 lignes intégrales** de la nouvelle preuve `injection_intra_arterielle_extraits.md`. Le delta des sources comporte exactement trois lignes changées : `chapters/I83/I83_d.html:61`, `chapters/I83/I83_d.html:82` et `chapters/I83/I83_pop4.html:67`. Les journaux techniques du producteur ne sont pas exécutés et ne servent pas de preuve médicale.

La lecture intégrale antérieure de l’onglet et de ses fenêtres est documentée dans l’audit initial. La présente contrelecture traite les changements ; elle ne prétend pas avoir retéléchargé ni relu extérieurement toutes les monographies et recommandations.

| Objet exact au SHA reçu | Blob Git | SHA-256 recalculé |
| --- | --- | --- |
| `chapters/I83/I83_d.html` | `e006eace6f7eac73897d0d5418ae9b495067f6cf` | `d6a339fea23ae2ffb8aa16268972ec0e9708b997fbd44403b3a2478387bbc88f` |
| `chapters/I83/I83_pop4.html` | `4d1f3fe2ed5c8e2d11da3783ac22faac1d351b79` | `04ef2f3e5d1985dc9a338f60c4a921a908b9d16c630b28cbb52fec3b05f18574` |
| `preuves/injection_intra_arterielle_extraits.md` | `3ff96ae7f11e017be24febabd711bf24396ef31e` | `fce2515bdf985f5ecf22f56fd7dbbab116058974b992707a4ef196fefb205f25` |

Les chemins `preuves/…` sont relatifs à `livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I83/`. Les lignes du cours désignent le SHA reçu.

## PH-02 — résolue

**Ancienne gravité : modérée, correction clinique nécessaire. Nouvelle localisation : `I83_d.html:82`.**

L’ancienne attribution au médicament « jusqu’à preuve du contraire » est remplacée par une **suspicion**. La nouvelle phrase demande de confronter la chronologie à l’examen, aux causes cardiaques, rénales, hépatiques ou thrombotiques selon le contexte, et à l’évolution après adaptation du traitement. Elle exclut également l’arrêt automatique sur la seule chronologie.

La correction répond précisément au défaut identifié : un indice temporel n’est plus une preuve causale et les causes concomitantes restent évaluées. Aucun nouveau seuil ou arrêt systématique n’est introduit. **PH-02 est fermée.**

## Injection intra-artérielle — réserve documentaire ciblée fermée

**Ancienne gravité potentielle : majeure ; aucune erreur de dose n’avait été prouvée. Résultat actuel : concordance documentaire vérifiée avec les extraits reçus.**

La nouvelle preuve apporte les passages exacts auparavant demandés, et pas seulement des références générales ou des extraits sur la compression :

| Référence déclarée dans la preuve | Lignes du fichier reçu | Passages sources reproduits et résultat |
| --- | --- | --- |
| Aethoxysklerol, information professionnelle suisse française, Swissmedic 33273, novembre 2022 | 7, 10–12 | Sources 47, **71**, 73 : risque de nécrose/amputation, appel immédiat au chirurgien vasculaire ; même aiguille, **5–10 mL de lidocaïne à 1 ou 2 %, ou mépivacaïne, et 500 UI d’héparine** ; ouate, jambe basse, hospitalisation vasculaire ; prudence à la cheville. |
| Sclerovein, information professionnelle suisse française, mai 2022 | 17, 20–24 | Sources 53, 56, 65, **66**, 69 : interdiction de l’injection artérielle du sclérosant, risque de gangrène et prise en charge spécialisée ; **5–10 mL de lidocaïne ou mépivacaïne à 1–2 % et 500 UI d’héparine**, même aiguille ; coton, jambe abaissée, hospitalisation vasculaire. |

`I83_d.html:61` ajoute la mépivacaïne et les deux références datées sans modifier la dose d’héparine. Son libellé suit celui d’Aethoxysklerol ; Sclerovein précise explicitement la concentration des deux anesthésiques. **Les 500 UI sont bien présentes dans les deux extraits : aucune correction à une autre dose n’est justifiée par ces preuves.**

Le corps du cours conserve les 5–10 mL, les concentrations de lidocaïne, la même aiguille, l’ouate, la position basse et l’hospitalisation en chirurgie vasculaire comme conduite immédiate. Le Pareto à `I83_pop4.html:67` ajoute lui aussi la mépivacaïne et conserve les 500 UI, la même aiguille, la position basse et l’hospitalisation spécialisée. Il résume le passage détaillé ; il n’introduit ni une dose concurrente ni une prise en charge ambulatoire. Le passage n’assimile pas ici l’anesthésique à la préparation adrénalinée de tumescence.

**La réserve de passage primaire manquant est levée.** La lecture établit la fidélité de la procédure aux extraits livrés ; elle ne certifie pas par un téléchargement indépendant la transcription à partir des pages officielles.

## PH-01 — correction conservée

`I83_pop4.html:50` est **identique octet pour octet** à cette ligne au SHA `20bee19`. Le delta de ce fichier ne touche que le Pareto, ligne 67. La distinction entre recette ESVS, flacon multidose Rapidocain avec conservateurs, restriction des blocages >15 mL, usage de tumescence hors information et préparation suivant le protocole de pharmacie hospitalière est donc conservée. **PH-01 reste fermée**, dans la portée précisément définie par la contrelecture précédente.

La preuve Rapidocain reste le blob `5106966c1976119e88615c7e84fad423309a4e82`, SHA-256 `262383bd90e0767c846f163b8fe31c67a5bc6f190a07d43d616ce92243bd6308` ; aucune restauration de l’ancienne équivalence pratique n’est constatée.

## Limites restantes et décision d’intégration

Les copies complètes `travail/production/I83/src/fi_aethoxysklerol.txt` et `fi_sclerovein.txt` ne figurent pas dans l’arbre Git au SHA reçu. Leurs SHA-256 annoncés dans la preuve, respectivement `7a8ad4fa77d5975471deb758624dbb9cc55101f090828da1c63acc7ac6f9dd4a` et `5b2451dd8e92eeca8ab33aa6e0f515b69c4150446ea258f40d3a1ff2a4c25dce`, sont **des déclarations du producteur**, distinctes de l’empreinte recalculée du fichier d’extraits réellement livré. Aucun téléchargement officiel indépendant n’est effectué dans cette contrelecture. Les refus réseau déjà consignés ne constituent pas une preuve d’erreur et ne sont pas réintroduits comme veto après réception des passages demandés.

Les autres limites de certification primaire de l’audit initial demeurent déclarées : monographies complètes non relues extérieurement, références européennes non retéléchargées et absence de preuve exhaustive indépendante pour certaines affirmations négatives de disponibilité suisse. Les remarques éditoriales sur le cas d’œdème et l’harmonisation EHIT du glossaire étaient non bloquantes et le restent. Aucun de ces points n’est transformé en erreur médicale démontrée par le nouveau delta.

**Reste bloquant médical prouvé sur le périmètre Pharmacologie : aucun.** L’avis de ce poste permet l’injection sélective de la remise figée, sous la décision du coordinateur appuyée sur les autres audits et contrôles techniques. Il ne certifie pas seul l’ensemble de I83 — Varices des membres inférieurs (C-01-Cardiologie), une préparation pharmaceutique locale particulière ou la complétude du fragment.

Méthode : objets Git figés lus en lecture seule ; comparaison textuelle et calcul d’empreintes par outils propres à l’auditeur ; aucun code entrant exécuté, aucun fichier canonique, index, référence ou commit modifié par ce poste. Seul ce nouveau rapport est écrit.
