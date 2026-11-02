# D62 — Anémie posthémorragique aiguë

État rédigé le 2026-11-02T16:13:08.195472+00:00. Auteur : parent Codex Hématologie. Cette version est destinée à la revue de Vial ; aucune certification médicale indépendante, PR ou publication sur main.

[Aperçu autonome](D62-apercu-autonome.html) · [Matrice monographique](coverage-final.md) · [Recherches attribuées](recherche_D62/recherche.md) · [Images et droits](images-provenance.json).

## Périmètre et preuves

- 14 points monographiques et 20 rubriques traitées. « covered » signifie rubrique abordée, y compris lacune documentée ; ce n’est pas une note médicale.
- 27 entrées de sources, avec lectures ciblées et réemplois attribués ; quatre informations professionnelles suisses. Les textes complets mis en cache restent hors Git.
- Six sciences, neuf unités de sémiologie, deux originaux photographiques du normal en trois occurrences et douze repères de légende ; cinq schémas causaux non anatomiques.
- 34 fenêtres et quatre quiz parcourus à chacune des deux largeurs, 1440 et 390 pixels. Quinze captures effectivement inspectées ; cinq captures modifiées revues après le dernier passage. Pas d’affirmation de lecture visuelle de chaque ligne.
- Quatre volets de relecture explicitement self_review par le même auteur : médical, linguistique, ordinateur, mobile.

## Validation et liaison finale

Les six contrôles de verification.json et le contrôle natif strict de sémiologie ont passé. Fin de vérification : 2026-11-02T16:04:19.287631+00:00. Relecture finale : 2026-11-02T16:12:24.217288+00:00.

- SHA256 aperçu : `44225bf5a0a4c594cdb11efc14a73661b366357a69c0737501d834af39cda1ce`.
- SHA256 manifeste : `4fb29682fb351f655683c0368a7bb924d0c7f485a5029294f64687a2c76b1080`.
- SHA256 source-binding : `4c6e464f053c5972fc46a6510fd7d28a8d8938251d0356c8ee7a8d6722bdc9bc`.
- Onze fichiers de contenu liés ; catalogue contrôlé séparément : `fe6e4d345d7efdd5dcf0b1b9beebf0fe9e148b03ba9729058b530c3ddff94a1e`.

## Réserves et incidents conservés

Les limites détaillées figurent dans lesson-manifest.json : populations, données suisses absentes, divergences TXA/ESGE, recommandations obstétricales distinctes, procédures locales, auto-relecture et attentes utilisateur. Aucun coût, token ou gain financier mesuré disponible. Les échecs de structure sémiologique, correction d’unités et omission initiale du contenu brut dans le dossier de revue restent dans verification-attempts. Un KeyError label/title du script de manifeste a été corrigé avant émission du premier reçu.

Le moteur hérité n’assure pas la navigation par flèches. Tab/Entrée sont vérifiés. Livre24 : corps de fenêtre 24,004 px, légendes 16,944 px. Les barres fixes peuvent recouvrir le bas d’une capture longue. Les compteurs globaux de la plateforme ne sont pas les compteurs de cette campagne.

## Scripts et veille

Les scripts de génération, verify_d62.py et browser_probe.py restent disponibles pour vérification explicite. record_final_review.py refuse toute exécution dès qu’un source-binding existe. La veille du harness observe toutes les 600 secondes ; elle ne crée aucune relecture, aucun achèvement ni activité d’auteur. Toute modification clinique future exige une nouvelle version et des contrôles adaptés, sans réécrire ce reçu.

L’achèvement projet n’est acquis qu’au reçu de medina_harness complete ; le simple indicateur d’assemblage production.json ne vaut pas achèvement clinique ou approbation utilisateur.
