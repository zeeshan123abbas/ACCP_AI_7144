<?php
// admin.php
require __DIR__ . '/auth.php';
require_role('admin');
$users = $pdo->query("SELECT name, email, role, created_at FROM users ORDER BY created_at DESC")->fetchAll();
?>
<h2>Admin area</h2>
<table border="1" cellpadding="6">
<tr><th>Name</th><th>Email</th><th>Role</th><th>Joined</th></tr>
<?php foreach ($users as $x): ?>
<tr><td><?= e($x['name']) ?></td><td><?= e($x['email']) ?></td><td><?= $x['role'] ?></td><td><?= $x['created_at'] ?></td></tr>
<?php endforeach; ?>
</table>
<p><a href="dashboard.php">Dashboard</a></p>
