<?php
// calculator.php - open in browser
$result = null; $error = "";
$a = $_GET['a'] ?? ""; $b = $_GET['b'] ?? ""; $op = $_GET['op'] ?? "+";

if ($a !== "" && $b !== "") {
    if (!is_numeric($a) || !is_numeric($b)) {
        $error = "Please enter valid numbers.";
    } else {
        $a = (float) $a; $b = (float) $b;
        $result = match ($op) {
            "+" => $a + $b,
            "-" => $a - $b,
            "*" => $a * $b,
            "/" => $b == 0 ? null : $a / $b,
            "%" => $b == 0 ? null : fmod($a, $b),
            "**" => $a ** $b,
            default => null,
        };
        if ($result === null) $error = "Cannot divide by zero.";
    }
}
?>
<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><title>Calculator</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"></head>
<body class="container py-4" style="max-width:480px">
<h2>PHP Calculator</h2>
<form method="get" class="d-flex gap-2">
  <input name="a" class="form-control" value="<?= htmlspecialchars((string)$a) ?>" placeholder="a">
  <select name="op" class="form-select w-auto">
    <?php foreach (["+","-","*","/","%","**"] as $o): ?>
      <option <?= $o === $op ? "selected" : "" ?>><?= $o ?></option>
    <?php endforeach; ?>
  </select>
  <input name="b" class="form-control" value="<?= htmlspecialchars((string)$b) ?>" placeholder="b">
  <button class="btn btn-primary">=</button>
</form>
<?php if ($error): ?><div class="alert alert-danger mt-3"><?= $error ?></div>
<?php elseif ($result !== null): ?><div class="alert alert-success mt-3">Result: <?= round($result, 4) ?></div><?php endif; ?>
</body></html>
