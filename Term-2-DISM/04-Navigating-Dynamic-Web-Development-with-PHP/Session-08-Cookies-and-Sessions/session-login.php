<?php
// session-login.php - demo users kept in an array (Session 14 uses a database)
session_start();

$users = [
    "admin@demo.pk"   => ["name" => "Admin",  "hash" => password_hash("admin123", PASSWORD_DEFAULT)],
    "student@demo.pk" => ["name" => "Ayesha", "hash" => password_hash("student123", PASSWORD_DEFAULT)],
];

if (isset($_GET['logout'])) {
    $_SESSION = [];
    session_destroy();
    setcookie(session_name(), '', time() - 3600, '/');
    header("Location: session-login.php");
    exit;
}

$error = "";
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $email = strtolower(trim($_POST['email'] ?? ''));
    $pass  = $_POST['password'] ?? '';
    if (isset($users[$email]) && password_verify($pass, $users[$email]['hash'])) {
        session_regenerate_id(true);
        $_SESSION['user'] = ["email" => $email, "name" => $users[$email]['name']];
        $_SESSION['login_time'] = time();
        if (!empty($_POST['remember'])) {
            setcookie("last_email", $email, ["expires" => time() + 86400 * 30, "path" => "/",
                      "httponly" => true, "samesite" => "Lax"]);
        }
        header("Location: session-login.php");
        exit;
    }
    $error = "Invalid credentials";
}
$_SESSION['views'] = ($_SESSION['views'] ?? 0) + 1;
?>
<!DOCTYPE html><html><body style="font-family:sans-serif;max-width:420px;margin:40px auto">
<?php if (isset($_SESSION['user'])): ?>
  <h2>Hello, <?= htmlspecialchars($_SESSION['user']['name']) ?></h2>
  <p>Logged in <?= time() - $_SESSION['login_time'] ?> seconds ago. Page views this session: <?= $_SESSION['views'] ?></p>
  <a href="?logout=1">Logout</a>
<?php else: ?>
  <h2>Login</h2>
  <p style="color:red"><?= $error ?></p>
  <form method="post">
    <input name="email" placeholder="Email" value="<?= htmlspecialchars($_COOKIE['last_email'] ?? '') ?>"><br><br>
    <input name="password" type="password" placeholder="Password"><br><br>
    <label><input type="checkbox" name="remember" value="1"> Remember my email</label><br><br>
    <button>Login</button>
  </form>
  <small>Try student@demo.pk / student123</small>
<?php endif; ?>
</body></html>
