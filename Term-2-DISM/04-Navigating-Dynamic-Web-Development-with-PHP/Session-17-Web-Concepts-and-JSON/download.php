<?php
// download.php?file=quotes.json
$allowed = ['quotes.json' => 'application/json'];
$name = basename($_GET['file'] ?? '');            // strips ../ paths
if (!isset($allowed[$name]) || !is_file(__DIR__ . "/$name")) {
    http_response_code(404);
    exit('File not found');
}
header('Content-Type: ' . $allowed[$name]);
header('Content-Disposition: attachment; filename="' . $name . '"');
header('Content-Length: ' . filesize(__DIR__ . "/$name"));
readfile(__DIR__ . "/$name");
exit;
