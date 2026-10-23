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
