#!/usr/bin/env bash
# Ancienne reconstruction de main depuis des arbres historiques : désactivée.
# Aucun appel Git et aucune écriture ; conserve l'historique et le travail courant.
set -eu
printf '%s\n' \
  'Commande historique désactivée : elle pouvait écraser des contributions récentes.' \
  'Consulter python3 tools/medina_resume.py, puis réconcilier la branche réelle sans remplacer main par un ancien arbre.' >&2
exit 2
