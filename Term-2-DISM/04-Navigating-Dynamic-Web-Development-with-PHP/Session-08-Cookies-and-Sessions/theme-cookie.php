<?php
// theme-cookie.php
$allowed = ["light", "dark"];
if (isset($_GET['theme']) && in_array($_GET['theme'], $allowed, true)) {
    setcookie("theme", $_GET['theme'], ["expires" => time() + 86400 * 365, "path" => "/", "samesite" => "Lax"]);
    header("Location: theme-cookie.php");   // reload so $_COOKIE has the new value
    exit;
}
$theme = $_COOKIE['theme'] ?? "light";
$bg = $theme === "dark" ? "#222; color:#eee" : "#fff; color:#222";
?>
<body style="background:<?= $bg ?>;font-family:sans-serif;padding:30px">
  <h2>Current theme: <?= $theme ?></h2>
  <a href="?theme=light">Light</a> | <a href="?theme=dark">Dark</a>
</body>
