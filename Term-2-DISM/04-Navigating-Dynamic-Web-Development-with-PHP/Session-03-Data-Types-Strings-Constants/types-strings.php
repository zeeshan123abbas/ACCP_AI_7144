<?php
// types-strings.php  (run: php types-strings.php)
$age = 21; $gpa = 3.6; $name = "  ayesha khan  "; $active = true; $nothing = null;
var_dump($age, $gpa, $active, $nothing);
echo gettype($name), PHP_EOL;

var_dump("5" == 5);   // true  (loose)
var_dump("5" === 5);  // false (strict)

$clean = ucwords(trim($name));
echo "Clean name: $clean", PHP_EOL;
echo "Length: ", strlen($clean), PHP_EOL;
echo "Has 'Khan'? ", str_contains($clean, "Khan") ? "yes" : "no", PHP_EOL;
echo "Initials: ", implode("", array_map(fn($w) => $w[0], explode(" ", $clean))), PHP_EOL;

$fee = 42000;
printf("Fee: Rs %s | Monthly: Rs %.2f%s", number_format($fee), $fee / 9, PHP_EOL);

$card = <<<TXT
Student: $clean
Status : {$active}
TXT;
echo $card, PHP_EOL;

define("SITE_NAME", "Aptech North Nazimabad");
const TAX_RATE = 0.16;
echo SITE_NAME, " tax on fee: ", $fee * TAX_RATE, PHP_EOL;
echo "This line is ", __LINE__, " of ", basename(__FILE__), PHP_EOL;
