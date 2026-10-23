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
