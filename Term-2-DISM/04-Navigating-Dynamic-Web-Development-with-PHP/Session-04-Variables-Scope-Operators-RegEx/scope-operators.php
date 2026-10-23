<?php
// scope-operators.php
$campus = "North Nazimabad";          // global

function showCampus(): void {
    // echo $campus;                   // would be undefined here
    echo "Campus: " . $GLOBALS['campus'] . PHP_EOL;
}
showCampus();

function visitCounter(): int {
    static $count = 0;                 // keeps value between calls
    return ++$count;
}
visitCounter(); visitCounter();
echo "Visits: " . visitCounter() . PHP_EOL;   // 3

$a = 10; $b = 3;
echo "$a / $b = " . round($a / $b, 2) . ", remainder " . ($a % $b) . ", power " . ($a ** 2) . PHP_EOL;
echo "Spaceship: " . (5 <=> 9) . PHP_EOL;     // -1
$username = $_GET['user'] ?? "guest";
$nick = "" ?: "anonymous";
echo "User: $username, nick: $nick" . PHP_EOL;
$x = 2 + 3 * 4;      // 14 not 20
$ok = true && false || true; // (true && false) || true = true
var_dump($x, $ok);
