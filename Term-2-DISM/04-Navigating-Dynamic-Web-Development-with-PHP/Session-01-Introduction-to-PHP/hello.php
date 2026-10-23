<?php
// hello.php - place in C:\xampp\htdocs\php-course\ and open http://localhost/php-course/hello.php
$name = "Aptech Student";
$today = date("l, d F Y");
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Hello PHP</title>
</head>
<body>
  <h1><?php echo "Hello, World!"; ?></h1>
  <p>Welcome <?= htmlspecialchars($name) ?>. Today is <?= $today ?>.</p>
  <p>You are running PHP version <?= PHP_VERSION ?>.</p>
</body>
</html>
