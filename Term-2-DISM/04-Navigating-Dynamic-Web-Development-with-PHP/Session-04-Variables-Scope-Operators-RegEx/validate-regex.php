<?php
// validate-regex.php
$inputs = [
    ["email",  "zoya@example.com"],
    ["email",  "zoya@@example"],
    ["mobile", "0301-2345678"],
    ["mobile", "+923012345678"],
    ["mobile", "12345"],
    ["cnic",   "42101-1234567-1"],
    ["cnic",   "4210112345671"],
];

function validate(string $type, string $value): bool {
    return match ($type) {
        "email"  => filter_var($value, FILTER_VALIDATE_EMAIL) !== false,
        "mobile" => preg_match('/^(\+92|0)3\d{2}-?\d{7}$/', $value) === 1,
        "cnic"   => preg_match('/^\d{5}-\d{7}-\d$/', $value) === 1,
        default  => false,
    };
}

foreach ($inputs as [$type, $value]) {
    printf("%-7s %-18s %s%s", $type, $value, validate($type, $value) ? "VALID" : "invalid", PHP_EOL);
}

// Extract all numbers from text, and mask a phone number
preg_match_all('/\d+/', "Room 12, Floor 3, Batch 2507", $m);
echo "Numbers: " . implode(", ", $m[0]) . PHP_EOL;
echo preg_replace('/(\d{4})-?(\d{3})(\d{4})/', '$1-***$3', "0301-2345678") . PHP_EOL;
