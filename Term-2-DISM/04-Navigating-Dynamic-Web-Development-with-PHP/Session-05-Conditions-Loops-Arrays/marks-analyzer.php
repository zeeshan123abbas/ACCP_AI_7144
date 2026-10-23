<?php
// marks-analyzer.php
$students = [
    ["name" => "Ayesha", "marks" => [88, 91, 79]],
    ["name" => "Bilal",  "marks" => [64, 58, 72]],
    ["name" => "Sana",   "marks" => [45, 39, 50]],
    ["name" => "Usman",  "marks" => [95, 87, 90]],
];

function grade(float $avg): string {
    return match (true) {
        $avg >= 85 => "A+", $avg >= 75 => "A", $avg >= 60 => "B",
        $avg >= 50 => "C", default => "F",
    };
}

foreach ($students as &$s) {                       // & lets us modify each row
    $s["avg"]   = round(array_sum($s["marks"]) / count($s["marks"]), 1);
    $s["grade"] = grade($s["avg"]);
}
unset($s);

usort($students, fn($a, $b) => $b["avg"] <=> $a["avg"]);   // highest first

echo str_pad("Name", 10) . str_pad("Avg", 8) . "Grade" . PHP_EOL;
foreach ($students as $pos => $s) {
    echo str_pad(($pos + 1) . ". " . $s["name"], 10) . str_pad($s["avg"], 8) . $s["grade"] . PHP_EOL;
}

$failed = array_filter($students, fn($s) => $s["grade"] === "F");
echo "Failed: " . (count($failed) ? implode(", ", array_column($failed, "name")) : "none") . PHP_EOL;
echo "Class average: " . round(array_sum(array_column($students, "avg")) / count($students), 1) . PHP_EOL;

// while + continue + break
$n = 0;
while (true) {
    $n++;
    if ($n % 2 === 0) continue;   // skip even
    if ($n > 9) break;            // stop after 9
    echo $n . " ";
}
echo PHP_EOL;
