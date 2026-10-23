<?php
// index.php - dashboard
require __DIR__ . '/includes/auth.php';
require_admin();
$pageTitle = 'Dashboard';

$total    = $pdo->query("SELECT COUNT(*) FROM students")->fetchColumn();
$month    = $pdo->query("SELECT COUNT(*) FROM students WHERE created_at >= DATE_FORMAT(CURDATE(), '%Y-%m-01')")->fetchColumn();
$byCourse = $pdo->query("SELECT course, COUNT(*) AS n FROM students GROUP BY course ORDER BY n DESC")->fetchAll();
$latest   = $pdo->query("SELECT name, course, created_at FROM students ORDER BY created_at DESC LIMIT 5")->fetchAll();

require __DIR__ . '/includes/header.php';
?>
<h3 class="mb-4">Dashboard</h3>
<div class="row g-3 mb-4">
  <div class="col-md-4"><div class="card text-bg-primary"><div class="card-body"><h6>Total students</h6><h2><?= $total ?></h2></div></div></div>
  <div class="col-md-4"><div class="card text-bg-success"><div class="card-body"><h6>Joined this month</h6><h2><?= $month ?></h2></div></div></div>
  <div class="col-md-4"><div class="card text-bg-warning"><div class="card-body"><h6>Courses running</h6><h2><?= count($byCourse) ?></h2></div></div></div>
</div>
<div class="row">
  <div class="col-md-6"><h5>Students per course</h5>
    <ul class="list-group"><?php foreach ($byCourse as $c): ?>
      <li class="list-group-item d-flex justify-content-between"><?= e($c['course']) ?><span class="badge bg-secondary"><?= $c['n'] ?></span></li>
    <?php endforeach; ?></ul></div>
  <div class="col-md-6"><h5>Latest registrations</h5>
    <table class="table table-sm"><?php foreach ($latest as $l): ?>
      <tr><td><?= e($l['name']) ?></td><td><?= e($l['course']) ?></td><td><?= date('d M', strtotime($l['created_at'])) ?></td></tr>
    <?php endforeach; ?></table></div>
</div>
<?php require __DIR__ . '/includes/footer.php'; ?>
