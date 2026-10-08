# Tests unitaires de la copie de réception I83

**118 tests exécutés, tous réussis, code de sortie0.**

Chapitre : I83 — Varices des membres inférieurs (C-01-Cardiologie).
Base : `ea105ace0046c71492cc6a69ff4c61698ef2ce34`. Remise : `0974d854db292ae0311e435b3daea5fbed187e25`.
Copie : `/workspace/medina-env/reprise-i83/candidate`, préparation sélective des huit HTML, deux glossaires et seule entrée I83 de catalogue.

Commande effectivement exécutée le8octobre2026 depuis cette copie :

```text
python3 -m unittest discover -s tests -p 'test_*.py' > /workspace/medina-env/reprise-i83/unit-tests.log 2>&1
```

Résultat du runner : `Ran118 tests in4.532s`, `OK`. Les118 tests portent sur les outils canoniques de livraison, les banques de justifications, l’organisation et la veille ; ils ne constituent pas un audit médical. La correction20bee19 ne change ensuite que le texte d’une fenêtre HTML, aucun outil ni glossaire ni registre ; cette suite n’est pas répétée pour ce delta.

SHA-256 du journal : `8e8ba16e5e251987bfeaaab76ac0b4fb4b8776872c025d5292fca0b743fb7848`.

```text
......................................................................................................................
----------------------------------------------------------------------
Ran 118 tests in 4.532s

OK
1 têtes repérées ; rapports : /tmp/tmpgy1z47x1/out
```
