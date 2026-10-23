# Session 04: Variables, Scope, Operators and Regular Expressions

> Module: Navigating Dynamic Web Development with PHP · Term 2 (DISM) · ⏱ ~2 hours

## 🎯 Learning Objectives

By the end of this session you will be able to:

- Explain local, global and static variable scope
- Use superglobals
- Apply arithmetic, assignment, comparison, logical, string and null-coalescing operators
- Explain operator precedence
- Validate input with preg_match and other PCRE functions

## 📖 Concepts Explained

### 1. Variable scope

| Scope | Where it lives | Notes |
|---|---|---|
| Local | inside a function | disappears when the function returns |
| Global | outside functions | not visible inside functions unless `global $x;` or `$GLOBALS['x']` |
| Static | inside a function, declared `static` | keeps its value between calls |
| Superglobal | everywhere | `$_GET`, `$_POST`, `$_SERVER`, `$_SESSION`, `$_COOKIE`, `$_FILES`, `$_ENV`, `$_REQUEST`, `$GLOBALS` |

Best practice: pass values in as parameters instead of using `global`.

### 2. Operators

| Type | Operators |
|---|---|
| Arithmetic | `+ - * / % **` |
| Assignment | `= += -= *= /= .= ??=` |
| Comparison | `== === != !== < > <= >= <=>` (spaceship) |
| Logical | `&& || ! and or xor` |
| String | `.` concatenation, `.=` append |
| Increment | `++$i`, `$i++` |
| Null coalescing | `$a ?? $b` |
| Ternary | `cond ? x : y`, short `x ?: y` |

**Precedence**: `*` before `+`, `&&` before `||`; use brackets when in doubt. Beware: `and`/`or` have lower precedence than `=`.

### 3. Regular expressions (PCRE)

A **regex** is a pattern for matching text. PHP uses `preg_*` functions with delimiters like `/.../`.

| Token | Meaning |
|---|---|
| `^` `$` | start / end of string |
| `\d` `\w` `\s` | digit / word char / whitespace |
| `[A-Z]` | a range |
| `+ * ? {n,m}` | quantifiers |
| `( )` | group / capture |
| `i` flag | case-insensitive |

Functions: `preg_match`, `preg_match_all`, `preg_replace`, `preg_split`. For emails prefer `filter_var($email, FILTER_VALIDATE_EMAIL)` — it is more reliable than a hand-written regex.

## 💻 Code Examples

All examples below are also saved as files in this folder, so you can open and run them directly.

### Example 1: Scope and operators (`scope-operators.php`)

```php
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
```

**How it works:**

- Functions cannot see global variables directly; `$GLOBALS` (or a parameter) is required.
- `static $count` is initialised once and then remembered.
- `<=>` returns -1, 0 or 1 — handy for sorting.

### Example 2: Validating email, mobile and CNIC (`validate-regex.php`)

```php
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
```

**How it works:**

- The mobile pattern accepts Pakistani numbers starting with `03` or `+923`, with an optional dash.
- CNIC format is 5 digits, 7 digits, 1 digit separated by dashes.
- `preg_match_all` returns all matches in `$m[0]`; `preg_replace` uses captured groups `$1`, `$3` to mask digits.

## 🧪 Lab Practice

1. Write a function using `static` that returns a new invoice number on every call (INV-001, INV-002...).
2. Predict, then check, the output of five tricky precedence expressions.
3. Write a regex for a strong password (8+ chars, upper, lower, digit, symbol).
4. Validate a postal code (5 digits) and a URL (`FILTER_VALIDATE_URL`).
5. Use `preg_split` to split a sentence on any punctuation or space.

## 📝 Assignment

Build `register-check.php`: a form with email, mobile, CNIC and password fields. On submit, validate each with regex/filter_var and show green ticks or red error messages next to each field.

## ❓ Quick Quiz

1. Which keyword keeps a function variable's value between calls?
   - a) global
   - b) static
   - c) const
   - d) var
2. What does `$a ?? $b` return?
3. Which function returns 1 when a regex matches?
4. Value of `10 <=> 10`?
5. Best built-in way to validate an email?

<details>
<summary>Show answers</summary>

1. b) static
2. `$a` if it is set and not null, otherwise `$b`.
3. `preg_match()`
4. 0
5. `filter_var($email, FILTER_VALIDATE_EMAIL)`

</details>

## 💼 Interview Questions

1. **Explain superglobals.**

   <details><summary>Model answer</summary>

   Built-in arrays available in every scope, such as $_GET, $_POST, $_SESSION, $_SERVER, $_FILES and $_COOKIE, carrying request and environment data.

   </details>

2. **Why avoid the `global` keyword?**

   <details><summary>Model answer</summary>

   It creates hidden dependencies, makes code hard to test and reason about; passing parameters is clearer.

   </details>

3. **What is the difference between `??` and `?:`?**

   <details><summary>Model answer</summary>

   `??` checks for null/unset only; `?:` checks for any falsy value like 0, '' or false.

   </details>

## ✅ Summary

- Variables have local, global, static or superglobal scope.
- PHP has a rich set of operators including `??`, `<=>` and `?:`.
- Use brackets to make precedence clear.
- preg_* functions and filter_var validate user input.

---

[⬅ Previous](../Session-03-Data-Types-Strings-Constants/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-05-Conditions-Loops-Arrays/README.md)

<sub>Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad</sub>
