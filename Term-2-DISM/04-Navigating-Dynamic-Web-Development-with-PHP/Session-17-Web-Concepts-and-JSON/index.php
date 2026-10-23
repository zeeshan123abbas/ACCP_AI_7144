<?php
// index.php
function detectBrowser(string $ua): string {
    return match (true) {
        str_contains($ua, 'Edg/')     => 'Microsoft Edge',
        str_contains($ua, 'OPR/')     => 'Opera',
        str_contains($ua, 'Chrome/')  => 'Google Chrome',
        str_contains($ua, 'Firefox/') => 'Mozilla Firefox',
        str_contains($ua, 'Safari/')  => 'Safari',
        default                       => 'Unknown browser',
    };
}
function detectPlatform(string $ua): string {
    foreach (['Windows' => 'Windows', 'Android' => 'Android', 'iPhone' => 'iOS', 'Mac OS' => 'macOS', 'Linux' => 'Linux'] as $k => $v) {
        if (str_contains($ua, $k)) return $v;
    }
    return 'Unknown OS';
}
$ua = $_SERVER['HTTP_USER_AGENT'] ?? '';
$images = glob(__DIR__ . '/images/*.{jpg,jpeg,png,webp}', GLOB_BRACE) ?: [];
$randomImage = $images ? 'images/' . basename($images[array_rand($images)]) : null;
?>
<!DOCTYPE html><html><head><title>Web concepts</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"></head>
<body class="container py-4" style="max-width:640px">
  <p class="text-muted">You are using <b><?= detectBrowser($ua) ?></b> on <b><?= detectPlatform($ua) ?></b>.</p>
  <?php if ($randomImage): ?><img src="<?= $randomImage ?>" class="img-fluid rounded mb-3" alt="random"><?php endif; ?>
  <blockquote class="blockquote p-4 bg-light rounded"><p id="q">Loading…</p><footer class="blockquote-footer" id="a"></footer></blockquote>
  <button class="btn btn-primary" onclick="loadQuote()">New quote</button>
  <a class="btn btn-outline-secondary" href="download.php?file=quotes.json">Download all quotes</a>
<script>
async function loadQuote() {
  const res = await fetch('api.php');
  const q = await res.json();
  document.getElementById('q').textContent = q.text;
  document.getElementById('a').textContent = q.author;
}
loadQuote();
</script>
</body></html>
