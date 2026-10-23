<?php
// students.php - uses db.php and schema.sql from this folder
require __DIR__ . '/db.php';

$action = $_POST['action'] ?? '';
if ($action === 'delete') {
    $pdo->prepare("DELETE FROM students WHERE id = ?")->execute([(int) $_POST['id']]);
    header("Location: students.php?msg=deleted"); exit;
}
if ($action === 'save') {
    $data = [':n' => trim($_POST['name']), ':e' => trim($_POST['email']), ':c' => trim($_POST['course']), ':ci' => trim($_POST['city'])];
    if (!empty($_POST['id'])) {
        $data[':id'] = (int) $_POST['id'];
        $pdo->prepare("UPDATE students SET name=:n, email=:e, course=:c, city=:ci WHERE id=:id")->execute($data);
        $msg = "updated";
    } else {
        $pdo->prepare("INSERT INTO students (name, email, course, city) VALUES (:n, :e, :c, :ci)")->execute($data);
        $msg = "added";
    }
    header("Location: students.php?msg=$msg"); exit;
}

// Edit mode: load one record
$edit = ['id' => '', 'name' => '', 'email' => '', 'course' => '', 'city' => 'Karachi'];
if (isset($_GET['edit'])) {
    $stmt = $pdo->prepare("SELECT * FROM students WHERE id = ?");
    $stmt->execute([(int) $_GET['edit']]);
    $edit = $stmt->fetch() ?: $edit;
}

// Search, sort, paginate
$q = trim($_GET['q'] ?? '');
$sortable = ['name', 'course', 'city', 'created_at'];
$sort = in_array($_GET['sort'] ?? '', $sortable, true) ? $_GET['sort'] : 'name';
$perPage = 5; $page = max(1, (int) ($_GET['page'] ?? 1)); $offset = ($page - 1) * $perPage;

$where = $q !== '' ? "WHERE name LIKE :q OR email LIKE :q2 OR course LIKE :q3" : "";
$params = $q !== '' ? [':q' => "%$q%", ':q2' => "%$q%", ':q3' => "%$q%"] : [];

$count = $pdo->prepare("SELECT COUNT(*) FROM students $where");
$count->execute($params);
$pages = max(1, (int) ceil($count->fetchColumn() / $perPage));

$stmt = $pdo->prepare("SELECT * FROM students $where ORDER BY $sort LIMIT :lim OFFSET :off");
foreach ($params as $k => $v) $stmt->bindValue($k, $v);
$stmt->bindValue(':lim', $perPage, PDO::PARAM_INT);
$stmt->bindValue(':off', $offset, PDO::PARAM_INT);
$stmt->execute();
$rows = $stmt->fetchAll();
?>
<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Students CRUD</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"></head>
<body class="container py-4">
<h2>Students</h2>
<?php if (isset($_GET['msg'])): ?><div class="alert alert-info">Record <?= e($_GET['msg']) ?>.</div><?php endif; ?>

<form method="post" class="row g-2 mb-3 p-3 bg-light rounded">
  <input type="hidden" name="action" value="save"><input type="hidden" name="id" value="<?= e((string) $edit['id']) ?>">
  <div class="col-md-3"><input name="name" required class="form-control" placeholder="Name" value="<?= e($edit['name']) ?>"></div>
  <div class="col-md-3"><input name="email" type="email" required class="form-control" placeholder="Email" value="<?= e($edit['email']) ?>"></div>
  <div class="col-md-2"><input name="course" required class="form-control" placeholder="Course" value="<?= e($edit['course']) ?>"></div>
  <div class="col-md-2"><input name="city" class="form-control" value="<?= e($edit['city']) ?>"></div>
  <div class="col-md-2"><button class="btn btn-<?= $edit['id'] ? 'warning' : 'primary' ?> w-100"><?= $edit['id'] ? 'Update' : 'Add' ?></button></div>
</form>

<form class="d-flex gap-2 mb-2">
  <input name="q" class="form-control" placeholder="Search name, email or course" value="<?= e($q) ?>">
  <select name="sort" class="form-select w-auto"><?php foreach ($sortable as $s): ?><option <?= $s === $sort ? 'selected' : '' ?>><?= $s ?></option><?php endforeach; ?></select>
  <button class="btn btn-outline-secondary">Go</button>
</form>

<table class="table table-hover">
<tr><th>Name</th><th>Email</th><th>Course</th><th>City</th><th></th></tr>
<?php foreach ($rows as $r): ?>
<tr><td><?= e($r['name']) ?></td><td><?= e($r['email']) ?></td><td><?= e($r['course']) ?></td><td><?= e($r['city']) ?></td>
  <td class="text-end">
    <a class="btn btn-sm btn-outline-primary" href="?edit=<?= $r['id'] ?>">Edit</a>
    <form method="post" class="d-inline" onsubmit="return confirm('Delete <?= e($r['name']) ?>?')">
      <input type="hidden" name="action" value="delete"><input type="hidden" name="id" value="<?= $r['id'] ?>">
      <button class="btn btn-sm btn-outline-danger">Delete</button>
    </form>
  </td></tr>
<?php endforeach; ?>
</table>
<nav><ul class="pagination">
<?php for ($i = 1; $i <= $pages; $i++): ?>
  <li class="page-item <?= $i === $page ? 'active' : '' ?>"><a class="page-link" href="?<?= http_build_query(['q' => $q, 'sort' => $sort, 'page' => $i]) ?>"><?= $i ?></a></li>
<?php endfor; ?>
</ul></nav>
</body></html>
