<?php
// register.php
require __DIR__ . '/auth.php';
$errors = [];
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    verify_csrf();
    $name = trim($_POST['name'] ?? ''); $email = strtolower(trim($_POST['email'] ?? '')); $pass = $_POST['password'] ?? '';
    if (mb_strlen($name) < 3) $errors[] = 'Name too short';
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) $errors[] = 'Invalid email';
    if (!preg_match('/^(?=.*[A-Z])(?=.*\d).{8,}$/', $pass)) $errors[] = 'Password: 8+ chars, 1 capital, 1 digit';
    if ($pass !== ($_POST['confirm'] ?? '')) $errors[] = 'Passwords do not match';
    if (!$errors) {
        try {
            $pdo->prepare("INSERT INTO users (name, email, password) VALUES (?, ?, ?)")
                ->execute([$name, $email, password_hash($pass, PASSWORD_DEFAULT)]);
            header('Location: login.php?registered=1'); exit;
        } catch (PDOException $e) { $errors[] = 'Email already registered'; }
    }
}
?>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
<form method="post" class="card p-4 mx-auto mt-5" style="width:380px">
  <h4>Create account</h4>
  <?php foreach ($errors as $er): ?><div class="text-danger small"><?= $er ?></div><?php endforeach; ?>
  <?= csrf_field() ?>
  <input name="name" class="form-control my-1" placeholder="Name">
  <input name="email" class="form-control my-1" placeholder="Email">
  <input name="password" type="password" class="form-control my-1" placeholder="Password">
  <input name="confirm" type="password" class="form-control my-1" placeholder="Confirm password">
  <button class="btn btn-primary mt-2">Register</button>
  <a href="login.php" class="small mt-2">Already have an account?</a>
</form>
