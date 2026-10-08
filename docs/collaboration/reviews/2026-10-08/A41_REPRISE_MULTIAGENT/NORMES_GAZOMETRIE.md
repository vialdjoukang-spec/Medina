# Normes suisses réellement reçues — gazométrie

**Recherche partiellement débloquée pour A41 — Sepsis et choc septique de l’adulte (I-03-Infectiologie).** Le catalogue officiel de l’USZ fournit deux plages lisibles et cohérentes, avec leurs matrices. Il ne fournit pas le jeu complet de normes artérielles demandé par `audit_examens_sciences_pharmacologie-03` ; cette observation reste ouverte sur ce volet. Aucun intervalle n’est complété de mémoire.

| Paramètre effectivement lu | Valeur et unité d’origine | Matrice/méthode | Date |
| --- | --- | --- | --- |
| [Lactate USZ, fiche 161](https://vademecum.usz.ch/Analysis/?entryID=161) | 0,5–2,2 mmol/L | Plasma Na-fluorure ; test enzymatique lactate-oxydase/peroxydase, Institut für Klinische Chemie | Consultation 08.10.2026 ; aucune date de version affichée |
| [Bicarbonate USZ, fiche 35](https://vademecum.usz.ch/Analysis/?entryID=35) | 22–29 mmol/L | Plasma hépariné ; test enzymatique, tarif « Bikarbonat, venös » | Consultation 08.10.2026 ; aucune date de version affichée |

Ces deux plages peuvent être citées **avec cette matrice, cette méthode et cette limite de datation**. Elles ne sont pas les valeurs de tout laboratoire suisse et ne doivent pas être présentées comme celles du bicarbonate actuel/standard calculé sur les gaz du sang. L’intervalle sain du lactate et le seuil opérationnel de choc septique sont deux objets distincts. Le JSON conserve les textes effectivement reçus, URL finale, horodatage, taille et SHA256, pas seulement les annonces du producteur.

Extraits de contrôle USZ : « Einheit mmol/l … Referenzbereich … Alle 0.5 2.2 … Probe Na-Fluorid Plasma … Enzymatischer Farbtest (Lactatoxidase/Peroxidase) » ; bicarbonate « Einheit mmol/l … Referenzbereich … Alle 22 29 … Probe Heparin-Plasma … Enzymatischer Test ». La fiche lactate mentionne les faux résultats possibles selon stase, délai et traitements ; le laboratoire local reste la référence d’un résultat individuel.

La [fiche CHUV artérielle 00717](https://catalogue.chuv.ch/analyses-examens/laboratoires/fiche/DLA_INV_01_00717/gazometrie-arterielle), V16 du 16.07.2024, est réellement lue : température/FiO2, pH/pO2/pCO2 corrigés à la température, bicarbonates calculés et préanalytique, **sans intervalles normaux publiés sur cette page**. Son existence ne permet pas d’attribuer une plage inventée au CHUV.

Les [fiches HUG 3807 artérielle](https://rpa.hug.ch/lvert/rpa/inf/fiches/FICHE_3807_.html) et [3935 veineuse](https://rpa.hug.ch/lvert/rpa/inf/fiches/FICHE_3935_.html), mises en production le 03.09.2025, affichent littéralement « 0.4 - 1.9 umol/l ». L’incohérence d’unité est conservée ; aucune conversion silencieuse de cette source vers mmol/L n’est faite. Une source alternative cohérente comme USZ peut être citée, sans prétendre corriger les HUG.

Le document [TRIBU CHUV lactate](https://tribu.chuv.ch/docs?UniqueId=d3a3ad4a-9399-4cb0-a903-80c9d279842d) répond HTTP 200 mais redirige vers « Accès refusé — Les documents TRIBU sont accessibles uniquement depuis l’intérieur du réseau informatique du CHUV. » Son contenu clinique n’a pas été reçu. Les fiches PCT 3940/CRP 3877 déjà lues par review_plan ne sont pas redemandées et leur preuve est distincte du problème gazométrique.

Restent non documentés par un primaire suisse effectivement lu : pH artériel, PaCO₂, PaO₂, bicarbonate calculé et trou anionique. Le trou anionique exige en outre préciser inclusion du potassium, méthode et albumine ; la compensation de Winter dans Jung 2019 est une règle d’interprétation, pas un intervalle sain de laboratoire suisse. Les valeurs générales pourraient être sourcées ailleurs avec attribution transparente, mais ne satisferaient pas à elles seules la demande d’un jeu suisse daté de version.

Recherche complémentaire réelle : catalogue USZ accessible (lactate/bicarbonate trouvés ; Blutgas/pCO/Sauerstoff/Anion sans résultat), HUG recherche publique (atelier SAUP sans texte de normes), Insel HTTP 503, guide laboratoire/Bâle HTTP 403, Unilabs page de configuration sans plage obtenue. Les pages de recherche générales avec CAPTCHA ou résultats hors sujet ont été écartées. Aucune tentative de contournement d’accès ni norme déduite d’un extrait de moteur de recherche.

Aucun canonique/Git modifié, aucun code entrant exécuté. Cet état est communiqué à review_plan et au coordinateur avant l’écriture d’une table candidate.

Lecture arrêtée à 2026-10-08T12:05:30.267433+00:00 UTC.
