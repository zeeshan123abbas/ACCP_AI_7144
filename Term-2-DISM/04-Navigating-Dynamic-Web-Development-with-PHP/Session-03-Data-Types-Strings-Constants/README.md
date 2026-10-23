# Session 03: Data Types, Strings and Constants

> Module: Navigating Dynamic Web Development with PHP · Term 2 (DISM) · ⏱ ~2 hours

## 🎯 Learning Objectives

By the end of this session you will be able to:

- List PHP's scalar, compound and special data types
- Inspect values with var_dump and gettype
- Use common string functions
- Use numbers and math functions
- Define constants with define() and const
- Build a simple calculator

## 📖 Concepts Explained

### 1. Data types

| Category | Types | Example |
|---|---|---|
| Scalar | `int`, `float`, `string`, `bool` | `42`, `3.14`, `"PHP"`, `true` |
| Compound | `array`, `object`, `callable`, `iterable` | `[1,2]`, `new DateTime()` |
| Special | `null`, `resource` | `null`, a file handle |

PHP is **dynamically typed**: the type comes from the value. `var_dump($x)` prints type and value; `gettype($x)` returns the type name. Type juggling converts automatically (`"5" + 3` gives `8`), which is why we prefer `===` (value **and** type) over `==`.

### 2. Strings

Strings can use single quotes, double quotes, **heredoc** (`<<<EOT`, interpolates) or **nowdoc** (`<<<'EOT'`, literal).

| Function | Purpose | Example result |
|---|---|---|
| `strlen("Karachi")` | length in bytes | 7 |
| `mb_strlen("کراچی")` | length in characters (Unicode) | 5 |
| `strtoupper`, `strtolower`, `ucwords` | change case | |
| `str_contains`, `str_starts_with` (PHP 8) | search | `true/false` |
| `strpos($s, "a")` | position of first match | int or `false` |
| `substr($s, 0, 3)` | part of string | |
| `str_replace("a","b",$s)` | replace | |
| `trim`, `explode`, `implode` | clean, split, join | |
| `sprintf("%05.2f", 3.1)` / `number_format(1234567)` | format | `03.10` / `1,234,567` |

### 3. Numbers and math

`intdiv(7,2)` → 3, `7 % 2` → 1, `round(2.567, 2)`, `ceil`, `floor`, `abs`, `max`, `min`, `sqrt`, `pow` or `**`, `random_int(1,6)` (cryptographically secure), `is_numeric()`.

### 4. Constants

Constants hold values that never change. Names are usually UPPER_CASE and have no `$`.

```php
define("SITE_NAME", "Aptech North");   // runtime, can be used in conditions
const TAX_RATE = 0.16;                 // compile-time, also used inside classes
```

Magic constants: `__FILE__`, `__LINE__`, `__DIR__`, `PHP_VERSION`, `PHP_EOL`.

## 💻 Code Examples

All examples below are also saved as files in this folder, so you can open and run them directly.

### Example 1: Types and strings (`types-strings.php`)

```php
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
```

**How it works:**

- `var_dump` is your best friend for checking types while learning.
- `trim` removes spaces, `ucwords` capitalises each word.
- The initials line splits words, takes the first letter of each with an arrow function, and joins them.
- Inside heredoc, `{$active}` prints `1` because `true` converts to the string "1".

### Example 2: Calculator with operators (`calculator.php`)

```php
<?php
// calculator.php - open in browser
$result = null; $error = "";
$a = $_GET['a'] ?? ""; $b = $_GET['b'] ?? ""; $op = $_GET['op'] ?? "+";

if ($a !== "" && $b !== "") {
    if (!is_numeric($a) || !is_numeric($b)) {
        $error = "Please enter valid numbers.";
    } else {
        $a = (float) $a; $b = (float) $b;
        $result = match ($op) {
            "+" => $a + $b,
            "-" => $a - $b,
            "*" => $a * $b,
            "/" => $b == 0 ? null : $a / $b,
            "%" => $b == 0 ? null : fmod($a, $b),
            "**" => $a ** $b,
            default => null,
        };
        if ($result === null) $error = "Cannot divide by zero.";
    }
}
?>
<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><title>Calculator</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"></head>
<body class="container py-4" style="max-width:480px">
<h2>PHP Calculator</h2>
<form method="get" class="d-flex gap-2">
  <input name="a" class="form-control" value="<?= htmlspecialchars((string)$a) ?>" placeholder="a">
  <select name="op" class="form-select w-auto">
    <?php foreach (["+","-","*","/","%","**"] as $o): ?>
      <option <?= $o === $op ? "selected" : "" ?>><?= $o ?></option>
    <?php endforeach; ?>
  </select>
  <input name="b" class="form-control" value="<?= htmlspecialchars((string)$b) ?>" placeholder="b">
  <button class="btn btn-primary">=</button>
</form>
<?php if ($error): ?><div class="alert alert-danger mt-3"><?= $error ?></div>
<?php elseif ($result !== null): ?><div class="alert alert-success mt-3">Result: <?= round($result, 4) ?></div><?php endif; ?>
</body></html>
```

**How it works:**

- `$_GET['a'] ?? ""` reads the query string safely (null coalescing).
- `is_numeric` validates input before casting to `float`.
- `match` picks the operation; division by zero is handled explicitly.

## 🧪 Lab Practice

1. Use `var_dump` on 8 different values including an array and `null`.
2. Write a script that prints a name reversed, in upper case and with its vowel count.
3. Format the number 1234567.891 as `1,234,567.89`.
4. Add a square-root button to the calculator.
5. Define a constant for your institute name and print it in a footer.

## 📝 Assignment

Create `fee-slip.php` that stores a student name, course and fee in variables and prints a formatted fee slip (heredoc) including 16% tax and a total, using constants for tax rate and institute name.

## ❓ Quick Quiz

1. Which operator checks value and type?
   - a) ==
   - b) =
   - c) ===
   - d) !=
2. Which function counts Unicode characters correctly?
3. How do you define a constant?
4. What does `intdiv(17, 5)` return?
5. Heredoc vs nowdoc?

<details>
<summary>Show answers</summary>

1. c) ===
2. `mb_strlen()`
3. `define('NAME', value)` or `const NAME = value;`
4. 3
5. Heredoc interpolates variables; nowdoc does not.

</details>

## 💼 Interview Questions

1. **Explain type juggling in PHP.**

   <details><summary>Model answer</summary>

   PHP converts values automatically between types depending on context, e.g. `'10' + 5` is 15. It is convenient but can cause bugs, so use strict comparison and `declare(strict_types=1)`.

   </details>

2. **When would you use a constant instead of a variable?**

   <details><summary>Model answer</summary>

   For values that must not change during execution, like configuration, tax rates or app names.

   </details>

3. **What does `strpos` return if the text is not found and why must you use `===`?**

   <details><summary>Model answer</summary>

   It returns `false`; because position 0 is also falsy you must compare with `=== false`.

   </details>

## ✅ Summary

- PHP has scalar, compound and special data types.
- Use `===` to avoid type juggling surprises.
- Many built-in string and math functions save time.
- Constants (`define`, `const`) hold fixed values.

---

[⬅ Previous](../Session-02-Installation-and-Syntax/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-04-Variables-Scope-Operators-RegEx/README.md)

<sub>Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad</sub>
