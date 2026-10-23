<?php
// search-get.php - GET is right for searches (shareable URL)
$courses = ["XML and JSON", "JavaScript", "MySQL", "PHP", "Laravel", "WordPress CMS"];
$q = trim($_GET['q'] ?? '');
$found = $q === '' ? $courses : array_filter($courses, fn($c) => stripos($c, $q) !== false);
?>
<form method="get">
  <input name="q" value="<?= htmlspecialchars($q) ?>" placeholder="Search courses">
  <button>Search</button>
</form>
<p><?= count($found) ?> result(s)<?= $q ? " for <b>" . htmlspecialchars($q) . "</b>" : "" ?></p>
<ul><?php foreach ($found as $c): ?><li><?= $c ?></li><?php endforeach; ?></ul>
