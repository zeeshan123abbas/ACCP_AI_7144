<?php
// redirect.php?to=home|docs|old
$targets = ['home' => 'index.php', 'docs' => 'https://www.php.net/manual/en/', 'old' => 'index.php'];
$to = $_GET['to'] ?? 'home';
if (!isset($targets[$to])) { http_response_code(400); exit('Unknown target'); }
$code = $to === 'old' ? 301 : 302;        // 301 = moved permanently
header('Location: ' . $targets[$to], true, $code);
exit;
