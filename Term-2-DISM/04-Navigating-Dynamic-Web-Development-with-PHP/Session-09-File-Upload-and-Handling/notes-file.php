<?php
// notes-file.php  (run: php notes-file.php)
$file = __DIR__ . '/students.csv';

$h = fopen($file, 'w');
fputcsv($h, ['id', 'name', 'city']);
foreach ([[1, 'Ayesha', 'Karachi'], [2, 'Bilal', 'Hyderabad'], [3, 'Sana', 'Karachi']] as $row) fputcsv($h, $row);
fclose($h);

$h = fopen($file, 'r');
$header = fgetcsv($h);
while (($row = fgetcsv($h)) !== false) {
    $rec = array_combine($header, $row);
    echo "{$rec['id']}: {$rec['name']} from {$rec['city']}" . PHP_EOL;
}
fclose($h);

echo "Size: " . filesize($file) . " bytes, modified " . date('d-m-Y H:i', filemtime($file)) . PHP_EOL;

try {
    $data = @file_get_contents(__DIR__ . '/missing.txt');
    if ($data === false) throw new Exception("missing.txt not found");
} catch (Exception $e) {
    echo "Handled: " . $e->getMessage() . PHP_EOL;
} finally {
    echo "Done." . PHP_EOL;
}
