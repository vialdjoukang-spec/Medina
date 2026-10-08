> **Protocole remplacé pour les travaux nouveaux, 8 octobre 2026.** Lire [le protocole par fragment](PROTOCOLE_FRAGMENTS_2026-10-08.md) et [COORDINATION.md](../../COORDINATION.md). Fragment entier achevé et auto-revu avant audit croisé unique ; l’autre IA corrige puis injecte, INJECTÉ immuable, HTML clair. Les dispositions incompatibles ci-dessous sont conservées comme historique et ne donnent plus d’ordre d’action. Aucun chapitre isolé ne constitue une remise finale.

# Règle administrative du propriétaire — Espace partagé d'audit

**Elle prime sur toute règle antérieure de progression, d'audit et d'injection. Elle s'impose à Claude et à Codex.**

1. **Aucune IA n'attend l'autre.** Un chapitre terminé est déposé dans l'espace partagé ; son auteur passe immédiatement au chapitre suivant de sa file.
2. **Espaces :**
   - `espace_partage/COURS_CLAUDE_A_AUDITER_PAR_CODEX/<CODE>/` : Claude dépose, Codex audite.
   - `espace_partage/COURS_CODEX_A_AUDITER_PAR_CLAUDE/<CODE>/` : Codex dépose, Claude audite.
3. **Audit sur place.** L'auditeur corrige lui-même dans l'espace ce qui doit l'être, sans renvoyer le chapitre, puis enregistre son verdict. L'auteur est informé par le rapport ; il ne bloque rien.
4. **Injection** dans les sources canoniques **uniquement** par `tools/espace.py injecter <CODE>`, et seulement si l'**autre** IA a rendu un verdict favorable sur les empreintes exactes des fichiers. Aucune IA n'injecte un cours non audité, ni un cours qu'elle a seulement audité elle-même.
5. Toutes les opérations passent par `tools/espace.py` (déposer, ouvrir, auditer, injecter). La vérification `garde-espace` rejette toute modification des sources canoniques sans audit croisé correspondant.
6. Chaque IA traite sa file d'audit dès qu'elle a un moment, sans interrompre sa production plus de nécessaire.
