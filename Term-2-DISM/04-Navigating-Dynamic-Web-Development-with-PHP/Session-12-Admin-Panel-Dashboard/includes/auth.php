<?php
// includes/auth.php
session_start();
require_once __DIR__ . '/db.php';

function require_admin(): void {
    if (($_SESSION['user']['role'] ?? '') !== 'admin') {
        header('Location: login.php');
        exit;
    }
}
