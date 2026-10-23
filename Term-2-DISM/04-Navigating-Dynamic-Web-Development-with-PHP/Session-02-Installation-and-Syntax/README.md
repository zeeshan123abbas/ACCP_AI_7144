# Session 02: Installing PHP and Basic Syntax

> Module: Navigating Dynamic Web Development with PHP · Term 2 (DISM) · ⏱ ~2 hours

## 🎯 Learning Objectives

By the end of this session you will be able to:

- Install XAMPP or Laragon and start Apache and MySQL
- Know where to save PHP files (htdocs/www) and how to open them
- Embed PHP inside HTML
- Use PHP opening/closing tags, statements and comments
- Use echo, print and variables to display output

## 📖 Concepts Explained

### 1. System requirements

A modern Windows 10/11, macOS or Linux PC, 4 GB RAM (8 GB recommended), a code editor (VS Code) and a browser.

### 2. Installing XAMPP (Windows)

1. Download XAMPP with PHP 8.2+ from https://www.apachefriends.org/.
2. Install to `C:\xampp` (avoid `Program Files` to prevent permission issues).
3. Open **XAMPP Control Panel** → click **Start** for **Apache** and **MySQL**.
4. Visit `http://localhost` – the XAMPP dashboard appears.
5. Create the folder `C:\xampp\htdocs\php-course` and put your files there. Open `http://localhost/php-course/file.php`.

**Laragon** (https://laragon.org/) is a lighter alternative: files go in `C:\laragon\www` and every folder gets a pretty URL like `http://php-course.test`.

If Apache will not start, port 80 is usually used by another program (Skype, IIS). Change `Listen 80` to `Listen 8080` in `httpd.conf` and use `http://localhost:8080`.

### 3. PHP tags and statements

| Syntax | Meaning |
|---|---|
| `<?php ... ?>` | standard PHP block |
| `<?= expr ?>` | short echo |
| `;` | ends every statement |
| file with only PHP | omit the closing `?>` to avoid stray whitespace |

### 4. Comments

```php
// single-line comment
#  also single-line
/* multi-line
   comment */
/** DocBlock used by editors and documentation tools */
```

### 5. echo vs print

`echo` can output several comma-separated values and returns nothing; `print` outputs one value and returns 1. In practice, use `echo`.

### 6. Variables

Variables start with `$`, are case-sensitive and need no type declaration: `$city = "Karachi";`. Use double quotes for interpolation (`"Hi $name"`), single quotes for plain text.

## 💻 Code Examples

All examples below are also saved as files in this folder, so you can open and run them directly.

### Example 1: PHP mixed with HTML (`index.php`)

```php
<?php
// index.php
$title   = "My First PHP Page";
$courses = ["XML & JSON", "JavaScript", "MySQL", "PHP"];
$hour    = (int) date("G");
$greeting = $hour < 12 ? "Good morning" : ($hour < 17 ? "Good afternoon" : "Good evening");
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title><?= $title ?></title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="container py-4">
  <h1><?= $greeting ?>!</h1>
  <p class="lead">Term 2 modules:</p>
  <ul class="list-group w-50">
    <?php foreach ($courses as $i => $course): ?>
      <li class="list-group-item"><?= ($i + 1) . ". " . htmlspecialchars($course) ?></li>
    <?php endforeach; ?>
  </ul>
  <?php
    /* print returns 1, echo returns nothing */
    echo "<p class='mt-3'>Generated at ", date("h:i:s A"), "</p>";
    print "<p>Server software: " . $_SERVER['SERVER_SOFTWARE'] . "</p>";
  ?>
</body>
</html>
```

**How it works:**

- PHP and HTML alternate freely; the `foreach ... : endforeach;` form is easy to read inside HTML.
- `.` joins strings; `echo` accepts several comma-separated values.
- `$_SERVER` is a built-in array with information about the request and server.

### Example 2: Checking your installation (`phpinfo.php`)

```php
<?php
// phpinfo.php - shows full PHP configuration. Delete this file on a live server!
phpinfo();
```

**How it works:**

Open it in the browser to see the PHP version, loaded extensions (look for `pdo_mysql`, `mbstring`, `openssl`) and the path of `php.ini`.

## 🧪 Lab Practice

1. Install XAMPP or Laragon and start Apache and MySQL.
2. Create `php-course` in htdocs and run `index.php`.
3. Open `phpinfo.php` and find the `php.ini` location and `upload_max_filesize`.
4. Add a comment of each style to `index.php`.
5. Print a table of 5 rows with `echo` inside a `for` loop.

## 📝 Assignment

Build `profile.php`: a Bootstrap card showing your name, photo (any image), city and a list of hobbies stored in a PHP array. Use at least three variables and comments.

## ❓ Quick Quiz

1. Default folder for web files in XAMPP?
   - a) www
   - b) public
   - c) htdocs
   - d) root
2. Which character starts a PHP variable?
3. Why omit the closing `?>` in pure PHP files?
4. Difference between echo and print?
5. Apache will not start. Most common cause?

<details>
<summary>Show answers</summary>

1. c) htdocs
2. `$`
3. To avoid accidental whitespace being sent to the browser (headers already sent errors).
4. echo can take multiple arguments and returns nothing; print takes one and returns 1.
5. Port 80 (or 443) is already used by another program.

</details>

## 💼 Interview Questions

1. **What is a WAMP/XAMPP stack?**

   <details><summary>Model answer</summary>

   A bundle of Apache web server, MySQL/MariaDB and PHP (plus Perl) for running PHP sites locally.

   </details>

2. **Single vs double quotes in PHP?**

   <details><summary>Model answer</summary>

   Double quotes parse variables and escape sequences like \n; single quotes output text literally and are slightly simpler.

   </details>

3. **What is php.ini?**

   <details><summary>Model answer</summary>

   PHP's main configuration file: memory limits, upload sizes, error display, extensions, timezone.

   </details>

## ✅ Summary

- XAMPP/Laragon gives you Apache + MySQL + PHP locally.
- Save files in htdocs (or www) and open them through http://localhost.
- PHP blocks live inside HTML; statements end with semicolons.
- Use comments generously and echo for output.

---

[⬅ Previous](../Session-01-Introduction-to-PHP/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-03-Data-Types-Strings-Constants/README.md)

<sub>Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad</sub>
