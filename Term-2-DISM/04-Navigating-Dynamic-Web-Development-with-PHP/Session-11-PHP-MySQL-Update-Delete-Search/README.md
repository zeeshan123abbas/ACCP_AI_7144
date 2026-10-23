# Session 11: PHP and MySQL: Update, Delete and Search

> Module: Navigating Dynamic Web Development with PHP · Term 2 (DISM) · ⏱ ~2 hours

## 🎯 Learning Objectives

By the end of this session you will be able to:

- Load a record into an edit form and update it
- Delete records safely with POST and confirmation
- Build a search form with LIKE and prepared statements
- Use ORDER BY and LIMIT for sorting and pagination
- Assemble a complete student CRUD

## 📖 Concepts Explained

### 1. CRUD map

| Operation | SQL | HTTP |
|---|---|---|
| Create | INSERT | POST |
| Read | SELECT | GET |
| Update | UPDATE ... WHERE id = :id | POST (form) |
| Delete | DELETE ... WHERE id = :id | POST (never a plain GET link) |

Deleting with a GET link is dangerous: search engines, link previews or a malicious image tag could trigger it. Use a small POST form with a JavaScript `confirm()`.

### 2. Search with LIKE

```php
$stmt = $pdo->prepare("SELECT * FROM students WHERE name LIKE :q OR email LIKE :q2");
$stmt->execute([':q' => "%$q%", ':q2' => "%$q%"]);
```

The `%` wildcards go into the **value**, not the SQL string.

### 3. Sorting and pagination

Column names cannot be placeholders, so sort columns must be **whitelisted**. Pagination: `LIMIT :limit OFFSET :offset`, where `offset = (page - 1) * perPage` (bind as integers).

## 💻 Code Examples

All examples below are also saved as files in this folder, so you can open and run them directly.

### Example 1: Complete CRUD in one file (`students.php`)

```php
<?php
// students.php - uses db.php and schema.sql from this folder
require __DIR__ . '/db.php';

$action = $_POST['action'] ?? '';
if ($action === 'delete') {
    $pdo->prepare("DELETE FROM students WHERE id = ?")->execute([(int) $_POST['id']]);
    header("Location: students.php?msg=deleted"); exit;
}
if ($action === 'save') {
    $data = [':n' => trim($_POST['name']), ':e' => trim($_POST['email']), ':c' => trim($_POST['course']), ':ci' => trim($_POST['city'])];
    if (!empty($_POST['id'])) {
        $data[':id'] = (int) $_POST['id'];
        $pdo->prepare("UPDATE students SET name=:n, email=:e, course=:c, city=:ci WHERE id=:id")->execute($data);
        $msg = "updated";
    } else {
        $pdo->prepare("INSERT INTO students (name, email, course, city) VALUES (:n, :e, :c, :ci)")->execute($data);
        $msg = "added";
    }
    header("Location: students.php?msg=$msg"); exit;
}

// Edit mode: load one record
$edit = ['id' => '', 'name' => '', 'email' => '', 'course' => '', 'city' => 'Karachi'];
if (isset($_GET['edit'])) {
    $stmt = $pdo->prepare("SELECT * FROM students WHERE id = ?");
    $stmt->execute([(int) $_GET['edit']]);
    $edit = $stmt->fetch() ?: $edit;
}

// Search, sort, paginate
$q = trim($_GET['q'] ?? '');
$sortable = ['name', 'course', 'city', 'created_at'];
$sort = in_array($_GET['sort'] ?? '', $sortable, true) ? $_GET['sort'] : 'name';
$perPage = 5; $page = max(1, (int) ($_GET['page'] ?? 1)); $offset = ($page - 1) * $perPage;

$where = $q !== '' ? "WHERE name LIKE :q OR email LIKE :q2 OR course LIKE :q3" : "";
$params = $q !== '' ? [':q' => "%$q%", ':q2' => "%$q%", ':q3' => "%$q%"] : [];

$count = $pdo->prepare("SELECT COUNT(*) FROM students $where");
$count->execute($params);
$pages = max(1, (int) ceil($count->fetchColumn() / $perPage));

$stmt = $pdo->prepare("SELECT * FROM students $where ORDER BY $sort LIMIT :lim OFFSET :off");
foreach ($params as $k => $v) $stmt->bindValue($k, $v);
$stmt->bindValue(':lim', $perPage, PDO::PARAM_INT);
$stmt->bindValue(':off', $offset, PDO::PARAM_INT);
$stmt->execute();
$rows = $stmt->fetchAll();
?>
<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Students CRUD</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"></head>
<body class="container py-4">
<h2>Students</h2>
<?php if (isset($_GET['msg'])): ?><div class="alert alert-info">Record <?= e($_GET['msg']) ?>.</div><?php endif; ?>

<form method="post" class="row g-2 mb-3 p-3 bg-light rounded">
  <input type="hidden" name="action" value="save"><input type="hidden" name="id" value="<?= e((string) $edit['id']) ?>">
  <div class="col-md-3"><input name="name" required class="form-control" placeholder="Name" value="<?= e($edit['name']) ?>"></div>
  <div class="col-md-3"><input name="email" type="email" required class="form-control" placeholder="Email" value="<?= e($edit['email']) ?>"></div>
  <div class="col-md-2"><input name="course" required class="form-control" placeholder="Course" value="<?= e($edit['course']) ?>"></div>
  <div class="col-md-2"><input name="city" class="form-control" value="<?= e($edit['city']) ?>"></div>
  <div class="col-md-2"><button class="btn btn-<?= $edit['id'] ? 'warning' : 'primary' ?> w-100"><?= $edit['id'] ? 'Update' : 'Add' ?></button></div>
</form>

<form class="d-flex gap-2 mb-2">
  <input name="q" class="form-control" placeholder="Search name, email or course" value="<?= e($q) ?>">
  <select name="sort" class="form-select w-auto"><?php foreach ($sortable as $s): ?><option <?= $s === $sort ? 'selected' : '' ?>><?= $s ?></option><?php endforeach; ?></select>
  <button class="btn btn-outline-secondary">Go</button>
</form>

<table class="table table-hover">
<tr><th>Name</th><th>Email</th><th>Course</th><th>City</th><th></th></tr>
<?php foreach ($rows as $r): ?>
<tr><td><?= e($r['name']) ?></td><td><?= e($r['email']) ?></td><td><?= e($r['course']) ?></td><td><?= e($r['city']) ?></td>
  <td class="text-end">
    <a class="btn btn-sm btn-outline-primary" href="?edit=<?= $r['id'] ?>">Edit</a>
    <form method="post" class="d-inline" onsubmit="return confirm('Delete <?= e($r['name']) ?>?')">
      <input type="hidden" name="action" value="delete"><input type="hidden" name="id" value="<?= $r['id'] ?>">
      <button class="btn btn-sm btn-outline-danger">Delete</button>
    </form>
  </td></tr>
<?php endforeach; ?>
</table>
<nav><ul class="pagination">
<?php for ($i = 1; $i <= $pages; $i++): ?>
  <li class="page-item <?= $i === $page ? 'active' : '' ?>"><a class="page-link" href="?<?= http_build_query(['q' => $q, 'sort' => $sort, 'page' => $i]) ?>"><?= $i ?></a></li>
<?php endfor; ?>
</ul></nav>
</body></html>
```

**How it works:**

- One file handles add, edit, delete, search, sort and pagination.
- A hidden `id` decides between INSERT and UPDATE.
- Delete is a POST form with `confirm()`, not a link.
- `$sort` comes from a whitelist, so it is safe to place in the SQL; everything else is bound.
- `LIMIT`/`OFFSET` are bound as integers with `PDO::PARAM_INT`.

### Example 2: Connection (same as Session 10) (`db.php`)

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

Copied here so the folder runs on its own.

### Example 3: Schema (same as Session 10) (`schema.sql`)

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

Run once if you have not already.

## 🧪 Lab Practice

1. Add server-side validation (as in Session 10) to the save action.
2. Add a 'city' filter dropdown next to the search box.
3. Show 'Showing 6–10 of 23' above the table.
4. Add a 'Delete selected' feature with checkboxes and `WHERE id IN (...)` (build placeholders dynamically).
5. Export the current search result to CSV.

## 📝 Assignment

Build a complete **Book Library CRUD** (`books`: title, author, isbn unique, category, price, stock) with add, edit, delete, search by title/author and pagination of 10 per page.

## ❓ Quick Quiz

1. Why should delete use POST instead of a GET link?
2. Where do the % wildcards go in a prepared LIKE query?
3. Can ORDER BY column names be placeholders?
   - a) Yes
   - b) No
4. Formula for OFFSET?
5. Which PDO constant binds an integer?

<details>
<summary>Show answers</summary>

1. GET requests can be triggered by crawlers, previews or other sites; state changes must use POST (with CSRF protection).
2. In the bound value, e.g. `"%$q%"`.
3. b) No – whitelist them.
4. (page − 1) × perPage
5. `PDO::PARAM_INT`

</details>

## 💼 Interview Questions

1. **How do you implement pagination?**

   <details><summary>Model answer</summary>

   Count total rows, compute pages = ceil(total / perPage), and fetch with LIMIT perPage OFFSET (page-1)*perPage; for very large tables use keyset pagination.

   </details>

2. **What happens if you forget WHERE in UPDATE?**

   <details><summary>Model answer</summary>

   Every row is updated. Always include WHERE and test with SELECT first; enable safe update mode in tools.

   </details>

3. **How do you safely use dynamic sort columns?**

   <details><summary>Model answer</summary>

   Map user choices to a fixed whitelist of column names and fall back to a default.

   </details>

## ✅ Summary

- CRUD = INSERT, SELECT, UPDATE, DELETE.
- Load a record into the form to edit it; use a hidden id.
- Delete with POST and confirmation.
- Search with LIKE via bound values; whitelist sort columns; paginate with LIMIT/OFFSET.

---

[⬅ Previous](../Session-10-PHP-MySQL-Create-Read/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-12-Admin-Panel-Dashboard/README.md)

<sub>Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad</sub>
