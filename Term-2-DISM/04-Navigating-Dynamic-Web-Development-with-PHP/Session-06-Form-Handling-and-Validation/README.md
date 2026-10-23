# Session 06: HTML Forms and Validation

> Module: Navigating Dynamic Web Development with PHP · Term 2 (DISM) · ⏱ ~2 hours

## 🎯 Learning Objectives

By the end of this session you will be able to:

- Create HTML forms that submit to PHP
- Explain GET vs POST and when to use each
- Read input with $_GET, $_POST and $_REQUEST
- Validate required fields, formats and lengths on the server
- Keep entered values (sticky form) and prevent XSS

## 📖 Concepts Explained

### 1. How a form reaches PHP

The `action` attribute says which file receives the data; `method` says how. Each input's `name` becomes a key in `$_GET` or `$_POST`.

| GET | POST |
|---|---|
| data in the URL (`?q=php`) | data in the request body |
| bookmarkable, cached | not shown in URL |
| ~2,000 character practical limit | large data, files |
| searches, filters | login, registration, anything that changes data |

`$_REQUEST` merges GET, POST and cookies — convenient but ambiguous, so prefer the specific array.

### 2. Server-side validation is mandatory

HTML5 `required` and `type="email"` help users, but anyone can bypass the browser. Always validate again in PHP:

1. Check the request method: `$_SERVER['REQUEST_METHOD'] === 'POST'`.
2. Trim input; check required fields are not empty.
3. Check formats (`filter_var`, `preg_match`) and lengths.
4. Collect errors in an array; process only if it is empty.
5. Escape output with `htmlspecialchars()` to prevent **XSS** (cross-site scripting).

### 3. Post/Redirect/Get

After a successful POST, redirect (`header('Location: success.php')`) so refreshing the page does not resubmit the form.

## 💻 Code Examples

All examples below are also saved as files in this folder, so you can open and run them directly.

### Example 1: Login form with validation (`login-form.php`)

```php
<?php
// login-form.php - sticky form with server-side validation (no database yet)
$errors = []; $email = ""; $success = false;

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $email    = trim($_POST['email'] ?? '');
    $password = $_POST['password'] ?? '';
    $remember = isset($_POST['remember']);

    if ($email === '') {
        $errors['email'] = "Email is required.";
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors['email'] = "Enter a valid email address.";
    }
    if ($password === '') {
        $errors['password'] = "Password is required.";
    } elseif (strlen($password) < 8) {
        $errors['password'] = "Password must be at least 8 characters.";
    }

    if (!$errors) {
        // Demo credentials only - Session 10 will check a real database
        $success = ($email === 'admin@demo.pk' && $password === 'secret123');
        if (!$success) $errors['form'] = "Wrong email or password.";
    }
}
function e(string $v): string { return htmlspecialchars($v, ENT_QUOTES, 'UTF-8'); }
?>
<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><title>Login</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"></head>
<body class="container py-5" style="max-width:420px">
<h2 class="mb-3">Student Login</h2>
<?php if ($success): ?>
  <div class="alert alert-success">Welcome back, <?= e($email) ?>!</div>
<?php else: ?>
  <?php if (isset($errors['form'])): ?><div class="alert alert-danger"><?= $errors['form'] ?></div><?php endif; ?>
  <form method="post" novalidate>
    <div class="mb-3">
      <label class="form-label">Email</label>
      <input type="email" name="email" value="<?= e($email) ?>"
             class="form-control <?= isset($errors['email']) ? 'is-invalid' : '' ?>" required>
      <div class="invalid-feedback"><?= $errors['email'] ?? '' ?></div>
    </div>
    <div class="mb-3">
      <label class="form-label">Password</label>
      <input type="password" name="password"
             class="form-control <?= isset($errors['password']) ? 'is-invalid' : '' ?>" required>
      <div class="invalid-feedback"><?= $errors['password'] ?? '' ?></div>
    </div>
    <div class="form-check mb-3">
      <input class="form-check-input" type="checkbox" name="remember" id="remember">
      <label class="form-check-label" for="remember">Remember me</label>
    </div>
    <button class="btn btn-primary w-100">Login</button>
  </form>
<?php endif; ?>
</body></html>
```

**How it works:**

- The page posts to itself (no `action`), checks the method, and collects errors per field.
- `novalidate` disables browser checks so you can see the PHP validation working.
- Bootstrap's `is-invalid` class shows the red message under each field.
- The email field keeps its value after errors (sticky form); the password is never echoed back.

### Example 2: GET search form (`search-get.php`)

```php
<?php
// search-get.php - GET is right for searches (shareable URL)
$courses = ["XML and JSON", "JavaScript", "MySQL", "PHP", "Laravel", "WordPress CMS"];
$q = trim($_GET['q'] ?? '');
$found = $q === '' ? $courses : array_filter($courses, fn($c) => stripos($c, $q) !== false);
?>
<form method="get">
  <input name="q" value="<?= htmlspecialchars($q) ?>" placeholder="Search courses">
  <button>Search</button>
</form>
<p><?= count($found) ?> result(s)<?= $q ? " for <b>" . htmlspecialchars($q) . "</b>" : "" ?></p>
<ul><?php foreach ($found as $c): ?><li><?= $c ?></li><?php endforeach; ?></ul>
```

**How it works:**

Submit a search and look at the address bar: `?q=java`. You can bookmark or share that URL. `stripos` does a case-insensitive search.

## 🧪 Lab Practice

1. Run `login-form.php` and trigger each error message.
2. Add a 'Full name' field (required, letters and spaces only, 3–50 chars).
3. Print `$_GET`, `$_POST` and `$_REQUEST` with `print_r` after submitting each form.
4. Type `<script>alert(1)</script>` in the search box and confirm it is shown as text, not executed.
5. Implement Post/Redirect/Get on successful login.

## 📝 Assignment

Build `admission-form.php` with name, father's name, email, mobile, date of birth, gender (radio), course (select) and terms checkbox. Validate everything server-side, keep values on error and show a confirmation summary on success.

## ❓ Quick Quiz

1. Which method should a login form use?
   - a) GET
   - b) POST
   - c) PUT
   - d) HEAD
2. Which superglobal holds both GET and POST data?
3. Why is browser validation not enough?
4. What does `htmlspecialchars` protect against?
5. How do you detect a form submission?

<details>
<summary>Show answers</summary>

1. b) POST
2. `$_REQUEST`
3. Users or tools can bypass it; only server-side checks can be trusted.
4. Cross-site scripting (XSS).
5. Check `$_SERVER['REQUEST_METHOD'] === 'POST'`.

</details>

## 💼 Interview Questions

1. **Explain the GET vs POST difference.**

   <details><summary>Model answer</summary>

   GET sends data in the URL, is idempotent and bookmarkable, used for reading/searching. POST sends data in the body, used for actions that change state or carry sensitive or large data.

   </details>

2. **What is XSS and how do you prevent it in PHP?**

   <details><summary>Model answer</summary>

   Injecting scripts into pages viewed by others. Escape all output with htmlspecialchars, validate input and use a Content Security Policy.

   </details>

3. **What is the Post/Redirect/Get pattern?**

   <details><summary>Model answer</summary>

   After processing a POST, redirect to a GET page so refreshes do not resubmit the form.

   </details>

## ✅ Summary

- Forms send data to PHP via GET or POST.
- Always validate on the server and collect errors per field.
- Sticky forms keep user input; escape all output.
- Use POST for changes, GET for searches.

---

[⬅ Previous](../Session-05-Conditions-Loops-Arrays/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-07-Functions/README.md)

<sub>Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad</sub>
