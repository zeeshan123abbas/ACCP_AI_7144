<?php
// register.php
require __DIR__ . '/db.php';
$errors = []; $old = ['name' => '', 'email' => '', 'course' => 'PHP', 'city' => 'Karachi'];
$courses = ['PHP', 'MySQL', 'Laravel', 'JavaScript', 'WordPress'];

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $old = array_map('trim', array_intersect_key($_POST, $old)) + $old;
    if (mb_strlen($old['name']) < 3) $errors[] = "Name must be at least 3 characters.";
    if (!filter_var($old['email'], FILTER_VALIDATE_EMAIL)) $errors[] = "Valid email required.";
    if (!in_array($old['course'], $courses, true)) $errors[] = "Choose a course.";

    if (!$errors) {
        try {
            $stmt = $pdo->prepare("INSERT INTO students (name, email, course, city) VALUES (:n, :e, :c, :ci)");
            $stmt->execute([':n' => $old['name'], ':e' => $old['email'], ':c' => $old['course'], ':ci' => $old['city']]);
            header("Location: register.php?added=" . $pdo->lastInsertId());
            exit;
        } catch (PDOException $ex) {
            $errors[] = $ex->errorInfo[1] === 1062 ? "This email is already registered." : "Could not save.";
        }
    }
}
$students = $pdo->query("SELECT id, name, email, course, city, created_at FROM students ORDER BY id DESC")->fetchAll();
$total = $pdo->query("SELECT COUNT(*) FROM students")->fetchColumn();
?>
<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Register</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"></head>
<body class="container py-4">
<h2>Student Registration</h2>
<?php if (isset($_GET['added'])): ?><div class="alert alert-success">Student #<?= (int) $_GET['added'] ?> added.</div><?php endif; ?>
<?php foreach ($errors as $err): ?><div class="alert alert-danger py-2"><?= e($err) ?></div><?php endforeach; ?>
<form method="post" class="row g-2 mb-4">
  <div class="col-md-3"><input name="name" class="form-control" placeholder="Full name" value="<?= e($old['name']) ?>"></div>
  <div class="col-md-3"><input name="email" class="form-control" placeholder="Email" value="<?= e($old['email']) ?>"></div>
  <div class="col-md-2"><select name="course" class="form-select">
    <?php foreach ($courses as $c): ?><option <?= $c === $old['course'] ? 'selected' : '' ?>><?= $c ?></option><?php endforeach; ?>
  </select></div>
  <div class="col-md-2"><input name="city" class="form-control" value="<?= e($old['city']) ?>"></div>
  <div class="col-md-2"><button class="btn btn-primary w-100">Register</button></div>
</form>
<h5>All students (<?= $total ?>)</h5>
<table class="table table-striped">
  <tr><th>#</th><th>Name</th><th>Email</th><th>Course</th><th>City</th><th>Joined</th></tr>
  <?php foreach ($students as $s): ?>
  <tr><td><?= $s['id'] ?></td><td><?= e($s['name']) ?></td><td><?= e($s['email']) ?></td>
      <td><?= e($s['course']) ?></td><td><?= e($s['city']) ?></td><td><?= date('d M Y', strtotime($s['created_at'])) ?></td></tr>
  <?php endforeach; ?>
</table>
</body></html>
