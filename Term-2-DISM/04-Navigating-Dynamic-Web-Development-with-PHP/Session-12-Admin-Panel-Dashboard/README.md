# Session 12: Admin Panel and Dashboard

> Module: Navigating Dynamic Web Development with PHP · Term 2 (DISM) · ⏱ ~2 hours

## 🎯 Learning Objectives

By the end of this session you will be able to:

- Structure a multi-page admin area with includes
- Build a Bootstrap 5 dashboard layout with sidebar and cards
- Protect admin pages behind a login check
- Show statistics from the database
- Organise reusable header, sidebar and footer partials

## 📖 Concepts Explained

### 1. Folder structure

```
admin/
├── includes/
│   ├── db.php          # PDO connection
│   ├── auth.php        # session + require_admin()
│   ├── header.php      # <head>, top navbar
│   └── footer.php
├── login.php
├── index.php           # dashboard with stats
├── students.php        # CRUD (from Session 11)
└── logout.php
```

`require` stops with a fatal error if the file is missing (use for essentials); `include` only warns. `require_once` prevents loading the same file twice.

### 2. Dashboard ideas

| Card | Query |
|---|---|
| Total students | `SELECT COUNT(*) FROM students` |
| New this month | `WHERE created_at >= DATE_FORMAT(CURDATE(), '%Y-%m-01')` |
| Students per course | `GROUP BY course` |
| Latest registrations | `ORDER BY created_at DESC LIMIT 5` |

### 3. Creating the first admin

Passwords are stored as hashes. Generate one in a terminal: `php -r "echo password_hash('Admin@123', PASSWORD_DEFAULT);"` and insert it into `users` with `role = 'admin'` (see `create-admin.php`).

## 💻 Code Examples

All examples below are also saved as files in this folder, so you can open and run them directly.

### Example 1: Login guard (`includes/auth.php`)

```php
<?php
// includes/auth.php
session_start();
require_once __DIR__ . '/db.php';

function require_admin(): void {
    if (($_SESSION['user']['role'] ?? '') !== 'admin') {
        header('Location: login.php');
        exit;
    }
}
```

**How it works:**

Every protected page starts with `require 'includes/auth.php'; require_admin();`. If the session does not contain an admin user, the visitor is sent to the login page.

### Example 2: Shared header and sidebar (`includes/header.php`)

```php
<?php // includes/header.php  - expects $pageTitle ?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
  <title><?= e($pageTitle ?? 'Admin') ?> · Admin Panel</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<nav class="navbar navbar-dark bg-dark px-3">
  <span class="navbar-brand">Institute Admin</span>
  <span class="text-light">Hi, <?= e($_SESSION['user']['name'] ?? '') ?> · <a class="link-light" href="logout.php">Logout</a></span>
</nav>
<div class="container-fluid"><div class="row">
  <aside class="col-md-2 bg-light min-vh-100 pt-3">
    <ul class="nav flex-column">
      <li class="nav-item"><a class="nav-link" href="index.php">Dashboard</a></li>
      <li class="nav-item"><a class="nav-link" href="students.php">Students</a></li>
    </ul>
  </aside>
  <main class="col-md-10 p-4">
```

**How it works:**

The header opens the layout and the sidebar; `footer.php` closes the tags. Change the menu once and every page updates.

### Example 3: Shared footer (`includes/footer.php`)

```php
<?php // includes/footer.php ?>
  </main>
</div></div>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

**How it works:**

Closes the layout opened in `header.php` and loads Bootstrap's JavaScript.

### Example 4: Admin login (`login.php`)

```php
<?php
// login.php
require __DIR__ . '/includes/auth.php';
$error = '';
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $stmt = $pdo->prepare("SELECT id, name, email, password, role FROM users WHERE email = ?");
    $stmt->execute([trim($_POST['email'] ?? '')]);
    $user = $stmt->fetch();
    if ($user && password_verify($_POST['password'] ?? '', $user['password']) && $user['role'] === 'admin') {
        session_regenerate_id(true);
        unset($user['password']);
        $_SESSION['user'] = $user;
        header('Location: index.php'); exit;
    }
    $error = 'Invalid admin credentials.';
}
?>
<!DOCTYPE html><html><head><title>Admin Login</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"></head>
<body class="bg-light d-flex align-items-center min-vh-100">
<form method="post" class="card p-4 mx-auto shadow-sm" style="width:340px">
  <h4 class="mb-3">Admin Login</h4>
  <?php if ($error): ?><div class="alert alert-danger py-2"><?= $error ?></div><?php endif; ?>
  <input name="email" type="email" class="form-control mb-2" placeholder="Email" required>
  <input name="password" type="password" class="form-control mb-3" placeholder="Password" required>
  <button class="btn btn-dark w-100">Sign in</button>
</form>
</body></html>
```

**How it works:**

The user is fetched by email with a prepared statement; `password_verify` checks the hash and only `admin` roles are accepted. The hash is removed before storing the user in the session.

### Example 5: Dashboard with statistics (`index.php`)

```php
<?php
// index.php - dashboard
require __DIR__ . '/includes/auth.php';
require_admin();
$pageTitle = 'Dashboard';

$total    = $pdo->query("SELECT COUNT(*) FROM students")->fetchColumn();
$month    = $pdo->query("SELECT COUNT(*) FROM students WHERE created_at >= DATE_FORMAT(CURDATE(), '%Y-%m-01')")->fetchColumn();
$byCourse = $pdo->query("SELECT course, COUNT(*) AS n FROM students GROUP BY course ORDER BY n DESC")->fetchAll();
$latest   = $pdo->query("SELECT name, course, created_at FROM students ORDER BY created_at DESC LIMIT 5")->fetchAll();

require __DIR__ . '/includes/header.php';
?>
<h3 class="mb-4">Dashboard</h3>
<div class="row g-3 mb-4">
  <div class="col-md-4"><div class="card text-bg-primary"><div class="card-body"><h6>Total students</h6><h2><?= $total ?></h2></div></div></div>
  <div class="col-md-4"><div class="card text-bg-success"><div class="card-body"><h6>Joined this month</h6><h2><?= $month ?></h2></div></div></div>
  <div class="col-md-4"><div class="card text-bg-warning"><div class="card-body"><h6>Courses running</h6><h2><?= count($byCourse) ?></h2></div></div></div>
</div>
<div class="row">
  <div class="col-md-6"><h5>Students per course</h5>
    <ul class="list-group"><?php foreach ($byCourse as $c): ?>
      <li class="list-group-item d-flex justify-content-between"><?= e($c['course']) ?><span class="badge bg-secondary"><?= $c['n'] ?></span></li>
    <?php endforeach; ?></ul></div>
  <div class="col-md-6"><h5>Latest registrations</h5>
    <table class="table table-sm"><?php foreach ($latest as $l): ?>
      <tr><td><?= e($l['name']) ?></td><td><?= e($l['course']) ?></td><td><?= date('d M', strtotime($l['created_at'])) ?></td></tr>
    <?php endforeach; ?></table></div>
</div>
<?php require __DIR__ . '/includes/footer.php'; ?>
```

**How it works:**

Statistics come from simple aggregate queries; the page reuses header and footer partials, keeping each page short.

### Example 6: Logout (`logout.php`)

```php
<?php
// logout.php
session_start();
$_SESSION = [];
session_destroy();
header('Location: login.php');
exit;
```

**How it works:**

Clears and destroys the session, then returns to the login page.

### Example 7: One-time admin creator (CLI) (`create-admin.php`)

```php
<?php
// create-admin.php - run once from terminal:  php create-admin.php
require __DIR__ . '/includes/db.php';
$stmt = $pdo->prepare("INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, 'admin')");
$stmt->execute(['Site Admin', 'admin@demo.pk', password_hash('Admin@123', PASSWORD_DEFAULT)]);
echo "Admin created: admin@demo.pk / Admin@123 (change it!)\n";
```

**How it works:**

Creates the first admin with a hashed password. Delete this file afterwards.

### Example 8: Connection (`includes/db.php`)

```php
<?php
// db.php - one shared PDO connection (edit credentials for your setup)
$host = '127.0.0.1'; $db = 'php_course'; $user = 'root'; $pass = '';
$dsn = "mysql:host=$host;dbname=$db;charset=utf8mb4";
try {
    $pdo = new PDO($dsn, $user, $pass, [
        PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        PDO::ATTR_EMULATE_PREPARES   => false,
    ]);
} catch (PDOException $e) {
    http_response_code(500);
    exit('Database connection failed. Check db.php settings.');
}
function e(?string $v): string { return htmlspecialchars((string) $v, ENT_QUOTES, 'UTF-8'); }
```

**How it works:**

Same PDO connection as Session 10, placed in `includes/`.

### Example 9: Schema (`schema.sql`)

```sql
-- schema.sql : run once in phpMyAdmin or MySQL Workbench
CREATE DATABASE IF NOT EXISTS php_course CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE php_course;

CREATE TABLE IF NOT EXISTS students (
  id         INT AUTO_INCREMENT PRIMARY KEY,
  name       VARCHAR(100) NOT NULL,
  email      VARCHAR(120) NOT NULL UNIQUE,
  course     VARCHAR(60)  NOT NULL,
  city       VARCHAR(50)  NOT NULL DEFAULT 'Karachi',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS users (
  id         INT AUTO_INCREMENT PRIMARY KEY,
  name       VARCHAR(100) NOT NULL,
  email      VARCHAR(120) NOT NULL UNIQUE,
  password   VARCHAR(255) NOT NULL,          -- password_hash() output
  role       ENUM('admin','user') NOT NULL DEFAULT 'user',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT IGNORE INTO students (name, email, course, city) VALUES
 ('Ayesha Khan','ayesha@mail.com','PHP','Karachi'),
 ('Bilal Ahmed','bilal@mail.com','MySQL','Hyderabad'),
 ('Sana Javed','sana@mail.com','Laravel','Karachi'),
 ('Usman Ali','usman@mail.com','JavaScript','Lahore');
```

**How it works:**

Run once to create the tables.

## 🧪 Lab Practice

1. Run `schema.sql`, then `php create-admin.php`, then log in at `login.php`.
2. Copy `students.php` from Session 11 into this folder, add `require 'includes/auth.php'; require_admin();` and wrap it with the header/footer.
3. Add a dashboard card for the number of distinct cities.
4. Highlight the active sidebar link using `basename($_SERVER['PHP_SELF'])`.
5. Add a 'Users' page listing all registered users (no passwords!).

## 📝 Assignment

Create an admin panel for a **Products** catalogue: login, dashboard (total products, out-of-stock count, total stock value), and products CRUD with image upload (reuse Session 09).

## ❓ Quick Quiz

1. Difference between include and require?
2. Why use require_once for db.php?
3. Which function checks a password against its hash?
4. Where should the auth check go on a protected page?
   - a) At the bottom
   - b) Before any output
   - c) In the footer
   - d) Only in JS
5. Why remove the password hash before storing the user in the session?

<details>
<summary>Show answers</summary>

1. require stops with a fatal error if the file is missing; include only warns.
2. To avoid creating the connection or redeclaring functions twice.
3. `password_verify()`
4. b) Before any output
5. The session does not need it; less sensitive data stored means less risk.

</details>

## 💼 Interview Questions

1. **How do you structure a PHP project without a framework?**

   <details><summary>Model answer</summary>

   Separate config, includes/partials, public pages and assets; centralise DB connection and auth; reuse header/footer; keep logic before output.

   </details>

2. **How do you protect admin pages?**

   <details><summary>Model answer</summary>

   Start the session, check the user's role on every admin request server-side, redirect if not authorised, and regenerate the session id at login.

   </details>

3. **Why should you never store plain passwords?**

   <details><summary>Model answer</summary>

   A database leak would expose every user's password, often reused elsewhere. Hashing with password_hash (bcrypt/argon2) makes them very hard to recover.

   </details>

## ✅ Summary

- Split pages into reusable partials with require/include.
- Guard every admin page with a server-side role check.
- Dashboards are aggregate SQL queries shown as cards and tables.
- Store only password hashes.

---

[⬅ Previous](../Session-11-PHP-MySQL-Update-Delete-Search/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-13-Emailing-with-PHPMailer/README.md)

<sub>Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad</sub>
