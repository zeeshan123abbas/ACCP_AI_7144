# Session 05: Conditions, Loops and Arrays

> Module: Navigating Dynamic Web Development with PHP · Term 2 (DISM) · ⏱ ~2 hours

## 🎯 Learning Objectives

By the end of this session you will be able to:

- Use if, elseif, else, switch and match
- Use while, do-while, for and foreach loops with break and continue
- Create indexed, associative and multidimensional arrays
- Use common array functions
- Sort arrays in different ways

## 📖 Concepts Explained

### 1. Decisions

```php
if ($marks >= 50) { ... } elseif ($marks >= 40) { ... } else { ... }
switch ($day) { case "Sat": case "Sun": echo "Weekend"; break; default: echo "Weekday"; }
$label = match ($code) { 1, 2 => "low", 3 => "mid", default => "high" };
```

`switch` uses loose comparison and needs `break`; `match` is strict and returns a value.

### 2. Loops

| Loop | Use when |
|---|---|
| `for ($i=0; $i<10; $i++)` | you know how many times |
| `while (cond)` | repeat while a condition is true (may run 0 times) |
| `do { } while (cond);` | must run at least once |
| `foreach ($arr as $key => $value)` | walk through arrays |

`break` exits the loop; `continue` skips to the next iteration.

### 3. Arrays

| Kind | Example |
|---|---|
| Indexed | `$cities = ["Karachi", "Lahore"];` |
| Associative | `$student = ["name" => "Ali", "marks" => 80];` |
| Multidimensional | `$class = [["name"=>"Ali","marks"=>80], ["name"=>"Sara","marks"=>91]];` |

Useful functions: `count`, `array_push`, `array_pop`, `array_shift`, `in_array`, `array_search`, `array_keys`, `array_values`, `array_merge`, `array_slice`, `array_sum`, `array_map`, `array_filter`, `array_column`, `array_key_exists`.

### 4. Sorting

| Function | Sorts by | Keeps keys? |
|---|---|---|
| `sort` / `rsort` | value asc/desc | no |
| `asort` / `arsort` | value asc/desc | yes |
| `ksort` / `krsort` | key asc/desc | yes |
| `usort` | your own comparison | no |

## 💻 Code Examples

All examples below are also saved as files in this folder, so you can open and run them directly.

### Example 1: Student marks analyzer (`marks-analyzer.php`)

```php
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
```

**How it works:**

- `foreach ($students as &$s)` uses a **reference** so the new keys are saved into the original array; `unset($s)` breaks the reference afterwards.
- `usort` with the spaceship operator sorts by average descending.
- `array_filter` + `array_column` produce the list of failed students.

## 🧪 Lab Practice

1. Print the multiplication table of 7 using `for`.
2. Print a 5x5 HTML table where even rows have a grey background.
3. Store 5 cities and their populations in an associative array; sort by population with `arsort`.
4. Use `do-while` to roll a dice (`random_int(1,6)`) until you get a 6, counting the rolls.
5. Use `switch` to convert a day number (1–7) to a day name.

## 📝 Assignment

Write `result-sheet.php` that stores 8 students with marks in 5 subjects and outputs a Bootstrap table with total, percentage, grade and position; highlight failing rows in red.

## ❓ Quick Quiz

1. Which loop always runs at least once?
   - a) for
   - b) while
   - c) do-while
   - d) foreach
2. Which sort keeps key associations and sorts by value?
3. What does `continue` do?
4. How do you get one column from a list of rows?
5. Main difference between switch and match?

<details>
<summary>Show answers</summary>

1. c) do-while
2. `asort()` (or `arsort()` for descending)
3. Skips the rest of the current iteration and moves to the next.
4. `array_column($rows, 'key')`
5. match is strict, returns a value and needs no break.

</details>

## 💼 Interview Questions

1. **Indexed vs associative arrays?**

   <details><summary>Model answer</summary>

   Indexed arrays use numeric keys starting at 0; associative arrays use named string keys. PHP arrays are ordered maps, so both are the same underlying type.

   </details>

2. **Why unset the reference after `foreach` by reference?**

   <details><summary>Model answer</summary>

   The variable stays a reference to the last element; a later loop using the same name can overwrite that element.

   </details>

3. **array_map vs array_filter?**

   <details><summary>Model answer</summary>

   array_map transforms every element and returns the same count; array_filter keeps only elements for which the callback returns true.

   </details>

## ✅ Summary

- if/elseif/else, switch and match make decisions.
- for, while, do-while and foreach repeat work; break and continue control loops.
- Arrays can be indexed, associative or multidimensional.
- Use built-in array and sort functions instead of writing your own.

---

[⬅ Previous](../Session-04-Variables-Scope-Operators-RegEx/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-06-Form-Handling-and-Validation/README.md)

<sub>Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad</sub>
