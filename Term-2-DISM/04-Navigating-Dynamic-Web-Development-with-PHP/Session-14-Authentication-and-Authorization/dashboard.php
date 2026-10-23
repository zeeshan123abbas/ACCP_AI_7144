<?php
// dashboard.php
require __DIR__ . '/auth.php';
require_login();
$u = current_user();
?>
<h2>Welcome, <?= e($u['name']) ?></h2>
<p>Your role: <b><?= e($u['role']) ?></b></p>
<?php if ($u['role'] === 'admin'): ?><p><a href="admin.php">Go to admin area</a></p><?php endif; ?>
<form method="post" action="logout.php"><?= csrf_field() ?><button>Logout</button></form>
