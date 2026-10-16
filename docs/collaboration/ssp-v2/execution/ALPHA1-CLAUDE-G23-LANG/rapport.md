# Audit linguistique agressif — G23, Autres maladies dégénératives des noyaux gris centraux (S08)

Mission ALPHA1-CLAUDE-G23-LANG, tour 1, génération 1. Base 32416a20, branche `claude/alpha1/g23-lang-g1`. Audit IA : revue distincte d’une validation médicale humaine ; aucune source canonique modifiée.

## Synthèse pour Vial

La leçon est globalement bien écrite : aucune faute d’orthographe courante, aucun guillemet ou apostrophe droit, aucun double espace, et tous les sigles possèdent une clé de glossaire. Les défauts sont d’un autre ordre : des phrases nominales dans les épilogues « À retenir » et les cellules, un méta-discours de plan, quelques ambiguïtés de rattachement, une terminologie flottante (« dossier », « chapitre », « fiche ») et deux renvois internes imprécis ou faux.

| Indicateur | Valeur |
|---|---|
| Propositions locales (`ancien` -> `nouveau`) | 63 |
| Renvois médicaux (non reformulés) | 16 |
| Fichiers concernés | 6 sur 6 (le glossaire n’appelle aucune proposition) |
| Empreintes SHA-256 des 7 fichiers | conformes au manifeste |
| Unicité de chaque `ancien`, absence de chevauchement | vérifiées par script, 79 sur 79 |
| Nombres et balises après application simulée | inchangés, sauf le renvoi interne 9.6 -> 9.5 et l’ajout de « 9.4 » |

## Constats par catégorie

1. **Phrases nominales et infinitifs injonctifs (17)** : épilogues « À retenir » (sections 4, 6, 7, 9, e-1, e-2, p-1), cellules de la section 5, fenêtre `g23-ho`, Pareto. Le guide de rédaction exige des phrases complètes.
2. **Ambiguïtés (9)** : la phrase sur les corps de Lewy (section 1.1), « spécifique de la maladie » (section 5.3), « pourcentages de Richardson », « principale cause d’AMS prise pour une PSP », « PKAN de 4 ans ou plus », « rattachement de code ».
3. **Élision (9 occurrences)** : le libellé de source « critères de Armstrong » doit s’écrire « critères d’Armstrong », comme le corps du texte le fait déjà.
4. **Terminologie (7)** : « dossier » désigne tantôt l’ensemble des sources, tantôt le dossier du patient (« le consigner au dossier ») ; « chapitre » et « fiche » flottent là où le texte dit « cours » et « section ».
5. **Registre (7)** : « gold standard » (3 occurrences, remplacé par « référence diagnostique »), infinitifs injonctifs, ellipses.
6. **Lourdeurs et tautologies (4)** : « Molécule précise non précisée », « urgences lentes », personnification du diagnostic.
7. **Grammaire (4)** : identification impropre entre un syndrome et une maladie, article manquant, « reste de la recherche ».
8. **Renvois internes (2)** : la section 8.2 renvoie à la section 9.6 alors que l’hypotension orthostatique est traitée en 9.5 ; la fenêtre `g23-oculomoteur` renvoie « au chapitre de prise en charge ».
9. **Intitulés (2)** : « Évaluation autonome » (lu comme « indépendante ») et « Diagnostics × associations d’examens ».
10. **Méta-discours (1)** : « Le cours poursuit quatre objectifs. Il apprend à… », proscrit par le guide.
11. **Ponctuation (1)** : deux propositions juxtaposées par une virgule dans `g23-preganglionnaire`.

## Renvois médicaux (16)

Ces formulations créent ou supposent une causalité, une fréquence ou une chronologie que la source citée n’établit peut-être pas. Elles ne sont pas corrigées. Aucune source n’a été relue dans cette mission : leur statut reste à trancher par un relecteur médical.

- Causalité : « ce qui justifie la limite d’âge », « explique pourquoi le pronostic et les soins palliatifs sont abordés dès le diagnostic », « La topographie explique le tableau », « d’où l’imagerie dopaminergique », « qui réduit la polyurie… », « à cause des chutes », « ce qui suppose d’avoir envisagé ces causes », « donc évocateur d’une synucléinopathie », « donc attendue, mais pas exclue ».
- Fréquence et chronologie : « précède souvent le syndrome moteur », « survie… après le diagnostic » (point de départ de la survie), « dont l’atteinte corticale est plus fréquente » (comparatif sans second terme, dans G23_a et dans la fenêtre `g23-dcb`).
- Autres : la phrase sur la droxidopa, sans source ni statut suisse ; l’incohérence sur l’amantadine, traitée en 9.2 comme antiparkinsonien mais décrite en p-1 comme répondant à une complication ; la causalité générale « Deux physiologies expliquent les échecs thérapeutiques… ».

## Constats hors périmètre linguistique, transmis à l'audit MED

- **MAJEUR, sémiologie** : `G23_c.html` compte 5 boutons `data-s` (anatomie, neuropathologie, physiologie, biochimie, génétique). Le sous-onglet « Sémiologie fondamentale et analytique » est absent, alors qu'AGENTS.md l'exige pour tout audit S08.
- **Réserve ORIGINE_INCONNUE, figure 4** (neurone, oligodendrocyte, astrocyte) : figure anatomique dessinée, origine non documentée ; vérification de provenance transmise à l'audit MED, sans jugement sur le fond.
- **Réserve ORIGINE_INCONNUE, figure 5** (arc autonome, ganglion) : même réserve.
- Figures 1, 2, 3, 6 et 7 : schémas non anatomiques, classement provisoire. Mon contrôle a porté sur le texte des figures, pas sur leur provenance.

## Choix différés, non appliqués

- Espaces insécables globales avant « ; : ! ? » et dans les nombres : aucun espace insécable dans les six fichiers, correction globale différée.
- « Fibrillation atriale » ou « auriculaire » : terme absent de G23.

## Observations non proposées

- « 1000 mg » et « 1400 pg/mL » sont écrits sans espace, « 100 000 » avec : à traiter avec la décision globale sur les espaces.
- Les variantes « dopa-sensible » et « peu sensible à la lévodopa », « pression couchée et assise » et « couchée puis debout » reprennent les libellés des sources ; elles ne sont pas harmonisées par prudence.

## Lacunes

- Aucune source médicale relue : les renvois sont conditionnels.
- Rendu navigateur et lisibilité à 390 px non contrôlés ; contrôle des figures limité à leur texte, non à leur provenance.
- Propositions non appliquées ni compilées : leur intégration relève d’une mission d’intégration.

## Tableau de bord

| Fichier | Propositions | dont renvois médicaux |
|---|---|---|
| G23_a.html | 10 | 6 |
| G23_b.html | 16 | 3 |
| G23_c.html | 15 | 3 |
| G23_d.html | 3 | 1 |
| G23_pop1.html | 7 | 3 |
| G23_pop2.html | 12 | 0 |
| **Total** | **63** | **16** |
