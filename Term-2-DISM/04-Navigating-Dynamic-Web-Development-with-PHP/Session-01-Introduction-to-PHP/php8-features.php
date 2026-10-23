<?php
// php8-features.php - run with:  php php8-features.php
declare(strict_types=1);

// Named arguments
echo str_pad(string: "7", length: 3, pad_string: "0", pad_type: STR_PAD_LEFT), PHP_EOL; // 007

// match expression
$marks = 78;
$grade = match (true) {
    $marks >= 85 => "A+",
    $marks >= 75 => "A",
    $marks >= 60 => "B",
    default      => "C or below",
};
echo "Grade: $grade", PHP_EOL;

// Union types + nullsafe operator
function half(int|float $n): float { return $n / 2; }
echo half(9), PHP_EOL;

$student = null;
echo $student?->name ?? "No student loaded", PHP_EOL;

// Enum (PHP 8.1)
enum Status: string { case Active = 'active'; case Left = 'left'; }
echo Status::Active->value, PHP_EOL;
