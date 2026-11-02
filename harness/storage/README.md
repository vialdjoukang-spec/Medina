# Conservation des preuves et capacité

La veille du harness mesure chaque volume de l’hôte toutes les600secondes et publie les octets disponibles dans status.json/watch/storage_capacity. Alerte sous512Mio ; gate bloquée sous128Mio. Aucun nettoyage automatique. Les mesures ne garantissent pas la taille d’un prochain build. Le runner GitHub lit le snapshot de l’hôte, pas sa propre capacité pour conclure sur cet hôte.

archive_closed_worktree.py est en lecture seule par défaut. Une exécution explicite avec --apply exige une clôture enregistrée, branche propre, tête distante exacte et source-binding intact. Elle applique un sparse-checkout réversible au seul ancien worktree et compare tous les fichiers protégés avant/après. Aucun objet Git, cache documentaire, cours, figure ou preuve propre n’est supprimé. Les worktrees actifs sont refusés. Restauration par git sparse-checkout disable quand l’espace suffit. Les reçus déjà émis ne sont jamais écrasés.

D63 a servi de vérification fonctionnelle réelle :110fichiers protégés inchangés,526540800octets disponibles supplémentaires au moment de la mesure. Le test de capacité critique a d’abord échoué sur une fixture sans état ; le journal initial est conservé. Après correction de cette fixture,55tests passent.
