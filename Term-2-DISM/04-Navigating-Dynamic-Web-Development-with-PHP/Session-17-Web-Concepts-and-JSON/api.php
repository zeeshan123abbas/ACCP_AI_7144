<?php
// api.php  - GET api.php            -> one random quote
//            GET api.php?all=1      -> all quotes
//            POST api.php (JSON body {"text":"..","author":".."}) -> add a quote
header('Content-Type: application/json; charset=utf-8');
$file = __DIR__ . '/quotes.json';

try {
    $quotes = json_decode(file_get_contents($file), true, flags: JSON_THROW_ON_ERROR);

    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        $in = json_decode(file_get_contents('php://input'), true, flags: JSON_THROW_ON_ERROR);
        if (empty($in['text']) || empty($in['author'])) {
            http_response_code(422);
            echo json_encode(['error' => 'text and author are required']);
            exit;
        }
        $quotes[] = ['text' => trim($in['text']), 'author' => trim($in['author'])];
        file_put_contents($file, json_encode($quotes, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE), LOCK_EX);
        http_response_code(201);
        echo json_encode(['message' => 'Quote added', 'count' => count($quotes)]);
        exit;
    }

    echo isset($_GET['all'])
        ? json_encode($quotes, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE)
        : json_encode($quotes[array_rand($quotes)], JSON_UNESCAPED_UNICODE);
} catch (JsonException $e) {
    http_response_code(400);
    echo json_encode(['error' => 'Invalid JSON: ' . $e->getMessage()]);
}
