<?php
// login.php
require __DIR__ . '/auth.php';
$error = '';
$_SESSION['fails'] ??= 0;
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    verify_csrf();
    if ($_SESSION['fails'] >= 5) {
        $error = 'Too many attempts. Try again later.';
    } else {
        $stmt = $pdo->prepare("SELECT id, name, email, password, role FROM users WHERE email = ?");
        $stmt->execute([strtolower(trim($_POST['email'] ?? ''))]);
        $u = $stmt->fetch();
        if ($u && password_verify($_POST['password'] ?? '', $u['password'])) {
            session_regenerate_id(true);
            unset($u['password']);
            $_SESSION['user'] = $u; $_SESSION['fails'] = 0;
            header('Location: ' . ($u['role'] === 'admin' ? 'admin.php' : 'dashboard.php')); exit;
        }
        $_SESSION['fails']++;
        $error = 'Email or password is incorrect.';
    }
}
?>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
<form method="post" class="card p-4 mx-auto mt-5" style="width:360px">
  <h4>Login</h4>
  <?php if (isset($_GET['registered'])): ?><div class="text-success small">Account created. Please log in.</div><?php endif; ?>
  <div class="text-danger small"><?= $error ?></div>
  <?= csrf_field() ?>
  <input name="email" class="form-control my-1" placeholder="Email">
  <input name="password" type="password" class="form-control my-1" placeholder="Password">
  <button class="btn btn-success mt-2">Login</button>
  <a href="register.php" class="small mt-2">Create account</a>
</form>
