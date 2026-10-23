<?php // includes/header.php  - expects $pageTitle ?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
  <title><?= e($pageTitle ?? 'Admin') ?> · Admin Panel</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<nav class="navbar navbar-dark bg-dark px-3">
  <span class="navbar-brand">Institute Admin</span>
  <span class="text-light">Hi, <?= e($_SESSION['user']['name'] ?? '') ?> · <a class="link-light" href="logout.php">Logout</a></span>
</nav>
<div class="container-fluid"><div class="row">
  <aside class="col-md-2 bg-light min-vh-100 pt-3">
    <ul class="nav flex-column">
      <li class="nav-item"><a class="nav-link" href="index.php">Dashboard</a></li>
      <li class="nav-item"><a class="nav-link" href="students.php">Students</a></li>
    </ul>
  </aside>
  <main class="col-md-10 p-4">
