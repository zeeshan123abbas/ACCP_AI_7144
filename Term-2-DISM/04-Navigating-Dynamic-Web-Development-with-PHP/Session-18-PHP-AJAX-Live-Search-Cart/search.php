<?php
// search.php?q=ay            -> JSON
// search.php?q=ay&format=xml -> XML
require __DIR__ . '/db.php';
$q = trim($_GET['q'] ?? '');
$rows = [];
if (mb_strlen($q) >= 1) {
    $stmt = $pdo->prepare("SELECT id, name, course, city FROM students WHERE name LIKE ? OR course LIKE ? ORDER BY name LIMIT 10");
    $stmt->execute(["%$q%", "%$q%"]);
    $rows = $stmt->fetchAll();
}

if (($_GET['format'] ?? '') === 'xml') {
    header('Content-Type: application/xml; charset=utf-8');
    $xml = new SimpleXMLElement('<students/>');
    foreach ($rows as $r) {
        $s = $xml->addChild('student');
        foreach ($r as $k => $v) $s->addChild($k, htmlspecialchars((string) $v));
    }
    echo $xml->asXML();
} else {
    header('Content-Type: application/json; charset=utf-8');
    echo json_encode(['query' => $q, 'count' => count($rows), 'results' => $rows]);
}
