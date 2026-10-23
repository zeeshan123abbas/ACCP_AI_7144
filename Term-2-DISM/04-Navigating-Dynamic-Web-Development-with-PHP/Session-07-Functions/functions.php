<?php
// functions.php
declare(strict_types=1);
date_default_timezone_set("Asia/Karachi");

function feeWithTax(float $fee, float $rate = 0.16): float {
    return round($fee * (1 + $rate), 2);
}
echo feeWithTax(42000), PHP_EOL;              // default rate
echo feeWithTax(rate: 0.05, fee: 30000), PHP_EOL;  // named arguments, any order

function average(int|float ...$nums): float {
    return $nums ? array_sum($nums) / count($nums) : 0.0;
}
echo average(70, 85, 90), PHP_EOL;

function addBonus(array &$marks, int $bonus): void {
    foreach ($marks as &$m) { $m = min(100, $m + $bonus); }
}
$marks = [45, 98, 70];
addBonus($marks, 5);
print_r($marks);                                 // original changed

$rate = 0.10;
$discount = fn(float $p): float => $p - $p * $rate;   // arrow function captures $rate
echo $discount(1000), PHP_EOL;

$ops = ["strtoupper", "strrev", "ucfirst"];
foreach ($ops as $fn) { echo $fn("aptech"), " "; }  // dynamic calls
echo PHP_EOL, date("l, d M Y h:i A"), " | timestamp: ", time(), PHP_EOL;
