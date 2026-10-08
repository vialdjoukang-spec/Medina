# Lot ESC 2026 — I35 — Valvulopathies aortiques (C-01-Cardiologie)

**Responsable :** Claude, avec un producteur, un vérificateur indépendant et un agent de levée des réserves de Codex. **Date :** 8 octobre 2026. **Branche :** `claude/loving-shannon-spwrhc`. **Base canonique :** `main` `315280ccc26e4a07b9bb6e36922cb579dd930f0e`. Le SHA livré est celui du commit qui publie ce rapport.

## Objet

Il s'agit de comparer le cours aux recommandations ESC publiées le 28.08.2026 : insuffisance cardiaque, réadaptation, maladie cardiovasculaire et maladie rénale chronique, cinquième définition universelle de l'infarctus. La comparaison prend la forme d'une fenêtre dédiée, complétée par des parenthèses dans le texte lorsqu'une phrase est devenue inexacte. Chaque classe et chaque niveau cités viennent d'un tableau de recommandations.

## Preuves (réserve MED-01)

- `travail/esc2026/I35/PREUVES.md` : pour chaque changement, la ligne exacte du tableau, citée en anglais, avec section, numéro de tableau, population, classe, niveau, notes et ligne antérieure comparée.
- `travail/esc2026/PROVENANCE.md` : titre, DOI, date, fichier lu et empreinte SHA-256 de chaque document.

## Fichiers

| Cible | Opération | SHA-256 d'origine | SHA-256 proposé |
| --- | --- | --- | --- |
| `chapters/I35/I35_b.html` | remplacement | `f91418163c5cc090` | `ef4620fab01f0587` |
| `chapters/I35/I35_d.html` | remplacement | `bbd637dfdf656362` | `39e59a6c89f5c807` |
| `chapters/I35/I35_pop_esc_comparison.html` | add | `—` | `064b0b86fea75c8f` |

## Vérification indépendante

Verdict : corrigée.

Erreurs corrigées :
- « Les troubles phosphocalciques accélèrent la calcification » : l’ESC 2026 présente cet effet comme théorique (le cinacalcet n’a pas réduit les événements) ; retiré de la fenêtre.
- Durabilité des bioprothèses généralisée au patient « plus jeune » : le texte la limite au patient jeune atteint de maladie rénale sévère, sans essai pour guider le choix ; reformulé.

Réserves :
- Hors ESC 2026, non corrigé : I35_d, furosémide intraveineux « 20–40 mg chez le patient naïf » (ESC 2021) ; l’ESC 2026 (section 7.5.3) indique 40 mg chez le patient naïf et deux fois la dose orale habituelle chez le patient déjà traité.
- DapaTAVI non repris (texte sans recommandation).

## Levée des réserves de l'audit croisé de Codex

- **MED-01 (preuves reproductibles)** : statut global « levée côté producteur : chaque changement ESC 2026 est rattaché à une ligne de tableau citée (document, DOI, date, section, tableau, population, ligne, classe et niveau, notes, ligne antérieure comparée, provenance du fichier lu). Contrelecture indépendante de Codex à refaire au commit de remise. » ; accès primaire : Textes intégraux 2026 lus sur les extractions pdftotext locales des PDF de l’éditeur (tampon « by guest on 07 October 2026 », empreintes SHA-256 dans PROVENANCE.md), non versionnés. Accès automatisé à academic.oup.com refusé depuis cet environnement (HTTP 403, vérification anti-robot) ; ESC 2021 sur la stimulation relu sur PubMed Central (PMC13179788) ; ESC 2024 sur la fibrillation auriculaire relu sur le jeu de diapositives officiel de l’ESC.. Pour I35 : {"preuves": "livraisons/Livraison Claude/C-01-Cardiologie/travail/esc2026/I35/PREUVES.md", "changements_retires": []}.
- **Vigilance I35 (furosémide)** : la ligne du tableau donne désormais en premier la dose ESC 2026 (section 7.5.3) : 40 mg IV chez le patient naïf de diurétique, deux fois la dose orale habituelle chez le patient déjà traité par un diurétique de l’anse. La ligne ajoute aussi la note a de la figure 15 : dose initiale plus élevée en cas de maladie rénale chronique (réception Codex `95836fe`). La dose de 20–40 mg de l’ESC 2021 n’est citée que comme antérieure (réception Codex `fa8fe70`). Texte source : « Patients naïve to diuretics usually respond well to 40 mg of i.v. furosemide or equivalent, whereas i.v. doses of two times the patient’s usual oral diuretic dose should be considered for patients who have been on loop diuretics as outpatients. »

## Contrôles exécutés sur `main` `960586ec0f6ddf76911a966f1bbd4a2bdcbc29b1`

Les contrôles ont été menés dans un arbre de travail distinct, avec les sources du lot appliquées sur le canonique :

```
python3 test_v7.py --static I35             # OK
verifier_sigles.py I35 chapters/I35/*.html   # {}
build_front.py ; build_front.py --all-fragments ; tests/audit_fragments.py   # 22 fragments, JavaScript valide, build reproductible
python3 test_v7.py I35                      # OK
node tests/verify_course_native.cjs I35      # 3269 contrôles, 0 échec (ordinateur 1 360 px, mobile 390 px)
python3 tools/livraison.py check-claude --root <checkout de main> <ce dossier>   # empreintes et chemins conformes (la racine doit être main : les empreintes d’origine sont celles de main)
```

Journal : `controles/i35_native_main.json`.

## Réserves générales

- Une comparaison ESC 2026 vérifiée ne valide pas le reste du cours. Le cours reste en `pending_exhaustive_review`.
- Couverture CIM-11 non établie.

## Demande à Codex

Je demande l'audit croisé de ce lot au commit de remise, puis `python3 tools/livraison.py apply-claude "<ce dossier>"`.
