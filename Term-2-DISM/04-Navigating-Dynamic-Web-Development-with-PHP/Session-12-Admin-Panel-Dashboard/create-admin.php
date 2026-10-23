<?php
// create-admin.php - run once from terminal:  php create-admin.php
require __DIR__ . '/includes/db.php';
$stmt = $pdo->prepare("INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, 'admin')");
$stmt->execute(['Site Admin', 'admin@demo.pk', password_hash('Admin@123', PASSWORD_DEFAULT)]);
echo "Admin created: admin@demo.pk / Admin@123 (change it!)\n";
