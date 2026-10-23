<?php
// age-calculator.php
date_default_timezone_set("Asia/Karachi");

function ageDetails(string $dob): ?array {
    $birth = DateTimeImmutable::createFromFormat('Y-m-d', $dob);
    if (!$birth || $birth > new DateTimeImmutable()) return null;
    $diff = $birth->diff(new DateTimeImmutable());
    $next = $birth->setDate((int) date('Y'), (int) $birth->format('m'), (int) $birth->format('d'));
    if ($next < new DateTimeImmutable('today')) $next = $next->modify('+1 year');
    return ['y' => $diff->y, 'm' => $diff->m, 'd' => $diff->d,
            'days_to_birthday' => (new DateTimeImmutable('today'))->diff($next)->days];
}

$dob = $_POST['dob'] ?? '';
$info = $dob ? ageDetails($dob) : null;
?>
<form method="post">
  <label>Date of birth <input type="date" name="dob" value="<?= htmlspecialchars($dob) ?>" required></label>
  <button>Calculate</button>
</form>
<?php if ($dob && !$info): ?>
  <p style="color:red">Please enter a valid past date.</p>
<?php elseif ($info): ?>
  <p>You are <b><?= $info['y'] ?></b> years, <?= $info['m'] ?> months and <?= $info['d'] ?> days old.</p>
  <p><?= $info['days_to_birthday'] ?> day(s) until your next birthday.</p>
<?php endif; ?>
