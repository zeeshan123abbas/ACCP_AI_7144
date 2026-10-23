<?php
// auth.php - include at the top of every page
session_start();
require_once __DIR__ . '/db.php';

function current_user(): ?array { return $_SESSION['user'] ?? null; }

function require_login(): void {
    if (!current_user()) { header('Location: login.php'); exit; }
}

function require_role(string $role): void {
    require_login();
    if (current_user()['role'] !== $role) {
        http_response_code(403);
        exit('<h2>403 Forbidden</h2><p>You do not have permission to view this page.</p><a href="dashboard.php">Back</a>');
    }
}

function csrf_token(): string {
    return $_SESSION['csrf'] ??= bin2hex(random_bytes(32));
}
function csrf_field(): string {
    return '<input type="hidden" name="csrf" value="' . csrf_token() . '">';
}
function verify_csrf(): void {
    if (!hash_equals($_SESSION['csrf'] ?? '', $_POST['csrf'] ?? '')) {
        http_response_code(419); exit('Invalid form token. Please reload the page.');
    }
}
