# Session 07: Functions in PHP

> Module: Navigating Dynamic Web Development with PHP · Term 2 (DISM) · ⏱ ~2 hours

## 🎯 Learning Objectives

By the end of this session you will be able to:

- Use built-in functions including date and time functions
- Write user-defined functions with parameters and return types
- Use default values, named arguments and variadic parameters
- Pass arguments by value and by reference
- Use anonymous functions, arrow functions and dynamic calls

## 📖 Concepts Explained

### 1. Why functions?

A function is a named, reusable block of code. It avoids repetition, makes code testable and gives a name to an idea (`calculateAge()`).

### 2. Anatomy

```php
function fullName(string $first, string $last = "", bool $upper = false): string {
    $name = trim("$first $last");
    return $upper ? strtoupper($name) : $name;
}
```

- **Type declarations** (`string`, `int`, `?float`, `int|string`) and **return types** (`: string`, `: void`) catch bugs early; add `declare(strict_types=1);` at the top of the file to disable silent conversions.
- **Default values** make parameters optional.
- **Named arguments** (PHP 8): `fullName(first: "Ali", upper: true)` — skip optional ones and make calls self-explanatory.
- **Variadic** `...$numbers` collects any number of arguments into an array.

### 3. By value vs by reference

| By value (default) | By reference (`&$x`) |
|---|---|
| function gets a copy | function works on the original |
| original unchanged | original changes |

### 4. Functions as values

- **Anonymous function (closure)**: `$tax = function($x) use ($rate) { return $x * $rate; };`
- **Arrow function**: `fn($x) => $x * $rate` (captures outer variables automatically)
- **Dynamic call**: `$fn = "strtoupper"; echo $fn("hi");` or `call_user_func($fn, "hi")`.

### 5. Date and time

`date("d-m-Y H:i")`, `time()` (Unix timestamp), `mktime()`, `strtotime("+1 week")`, and the object-oriented `DateTime` / `DateTimeImmutable` with `diff()` for accurate differences. Set your zone: `date_default_timezone_set("Asia/Karachi");`.

## 💻 Code Examples

All examples below are also saved as files in this folder, so you can open and run them directly.

### Example 1: Function features (`functions.php`)

```php
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
```

**How it works:**

- Named arguments let you pass `rate` before `fee`.
- `...$nums` accepts any count of numbers.
- `&$marks` modifies the caller's array; `min(100, ...)` caps marks at 100.
- Each string in `$ops` is called as a function.

### Example 2: Age calculator form (`age-calculator.php`)

```php
<?php
// age-calculator.php
date_default_timezone_set("Asia/Karachi");

function ageDetails(string $dob): ?array {
    $birth = DateTimeImmutable::createFromFormat('Y-m-d', $dob);
    if (!$birth || $birth > new DateTimeImmutable()) return null;
    $diff = $birth->diff(new DateTimeImmutable());
    $next = $birth->setDate((int) date('Y'), (int) $birth->format('m'), (int) $birth->format('d'));
    if ($next < new DateTimeImmutable('today')) $next = $next->modify('+1 year');
    return ['y' => $diff->y, 'm' => $diff->m, 'd' => $diff->d,
            'days_to_birthday' => (new DateTimeImmutable('today'))->diff($next)->days];
}

$dob = $_POST['dob'] ?? '';
$info = $dob ? ageDetails($dob) : null;
?>
<form method="post">
  <label>Date of birth <input type="date" name="dob" value="<?= htmlspecialchars($dob) ?>" required></label>
  <button>Calculate</button>
</form>
<?php if ($dob && !$info): ?>
  <p style="color:red">Please enter a valid past date.</p>
<?php elseif ($info): ?>
  <p>You are <b><?= $info['y'] ?></b> years, <?= $info['m'] ?> months and <?= $info['d'] ?> days old.</p>
  <p><?= $info['days_to_birthday'] ?> day(s) until your next birthday.</p>
<?php endif; ?>
```

**How it works:**

- `DateTimeImmutable::diff()` returns a `DateInterval` with exact years, months and days.
- The function returns `null` for invalid or future dates (`?array` return type).
- The next birthday is this year's date, or next year's if it has already passed.

## 🧪 Lab Practice

1. Write `isEven(int $n): bool` and `factorial(int $n): int` (recursive).
2. Write `formatPKR(float $amount, bool $withSymbol = true)` and call it with named arguments.
3. Write `swap(&$a, &$b)` and prove it works.
4. Use `array_map` with an arrow function to add 10% to a list of fees.
5. Print how many days are left until 31 December using `DateTime::diff`.

## 📝 Assignment

Create `utils.php` containing at least six reusable functions (e.g. `e()`, `formatPKR()`, `grade()`, `slugify()`, `ageFromDob()`, `isValidCnic()`), and `test-utils.php` that `require`s it and demonstrates each one.

## ❓ Quick Quiz

1. How do you make a parameter optional?
   - a) Use &
   - b) Give it a default value
   - c) Use static
   - d) Use global
2. What symbol passes an argument by reference?
3. What does `...$args` do?
4. Arrow function syntax?
5. Which function returns the current Unix timestamp?

<details>
<summary>Show answers</summary>

1. b) Give it a default value
2. `&`
3. Collects a variable number of arguments into an array (variadic).
4. `fn($x) => expression`
5. `time()`

</details>

## 💼 Interview Questions

1. **What are named arguments and why are they useful?**

   <details><summary>Model answer</summary>

   PHP 8 feature allowing arguments to be passed by parameter name; it improves readability and lets you skip optional parameters.

   </details>

2. **Closure vs arrow function?**

   <details><summary>Model answer</summary>

   A closure needs `use` to capture outer variables and can have multiple statements; an arrow function captures by value automatically and contains a single expression.

   </details>

3. **What does declare(strict_types=1) change?**

   <details><summary>Model answer</summary>

   Scalar type declarations become strict: passing '5' to an int parameter throws a TypeError instead of being converted.

   </details>

## ✅ Summary

- Functions package reusable logic with typed parameters and return values.
- Defaults, named arguments and variadics make calls flexible.
- By-reference parameters change the caller's variable.
- Closures and arrow functions treat functions as values.
- Use DateTime classes for reliable date maths.

---

[⬅ Previous](../Session-06-Form-Handling-and-Validation/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-08-Cookies-and-Sessions/README.md)

<sub>Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad</sub>
