<?php
// index.php
$title   = "My First PHP Page";
$courses = ["XML & JSON", "JavaScript", "MySQL", "PHP"];
$hour    = (int) date("G");
$greeting = $hour < 12 ? "Good morning" : ($hour < 17 ? "Good afternoon" : "Good evening");
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title><?= $title ?></title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="container py-4">
  <h1><?= $greeting ?>!</h1>
  <p class="lead">Term 2 modules:</p>
  <ul class="list-group w-50">
    <?php foreach ($courses as $i => $course): ?>
      <li class="list-group-item"><?= ($i + 1) . ". " . htmlspecialchars($course) ?></li>
    <?php endforeach; ?>
  </ul>
  <?php
    /* print returns 1, echo returns nothing */
    echo "<p class='mt-3'>Generated at ", date("h:i:s A"), "</p>";
    print "<p>Server software: " . $_SERVER['SERVER_SOFTWARE'] . "</p>";
  ?>
</body>
</html>
