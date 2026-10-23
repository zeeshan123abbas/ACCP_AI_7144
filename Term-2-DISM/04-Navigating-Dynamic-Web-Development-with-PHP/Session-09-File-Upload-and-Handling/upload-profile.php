<?php
// upload-profile.php - create a writable "uploads" folder next to this file
const MAX_BYTES = 2 * 1024 * 1024;               // 2 MB
const ALLOWED = ['image/jpeg' => 'jpg', 'image/png' => 'png', 'image/webp' => 'webp'];
$message = ""; $saved = null;

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        $f = $_FILES['photo'] ?? null;
        if (!$f || $f['error'] === UPLOAD_ERR_NO_FILE) throw new RuntimeException("Please choose a file.");
        if ($f['error'] !== UPLOAD_ERR_OK) throw new RuntimeException("Upload failed (code {$f['error']}).");
        if ($f['size'] > MAX_BYTES) throw new RuntimeException("File is larger than 2 MB.");

        $mime = (new finfo(FILEINFO_MIME_TYPE))->file($f['tmp_name']);   // real type from content
        if (!isset(ALLOWED[$mime])) throw new RuntimeException("Only JPG, PNG or WEBP images are allowed.");

        $dir = __DIR__ . '/uploads';
        if (!is_dir($dir)) mkdir($dir, 0755, true);
        $newName = bin2hex(random_bytes(8)) . '.' . ALLOWED[$mime];     // never reuse user's name
        if (!move_uploaded_file($f['tmp_name'], "$dir/$newName")) throw new RuntimeException("Could not save file.");

        file_put_contents("$dir/upload-log.txt", date('c') . " $newName {$f['size']} bytes" . PHP_EOL, FILE_APPEND);
        $saved = "uploads/$newName";
        $message = "Uploaded successfully!";
    } catch (RuntimeException $e) {
        $message = $e->getMessage();
    }
}
?>
<!DOCTYPE html><html><body style="font-family:sans-serif;max-width:480px;margin:40px auto">
<h2>Upload profile picture</h2>
<form method="post" enctype="multipart/form-data">
  <input type="file" name="photo" accept="image/*">
  <button>Upload</button>
</form>
<p><?= htmlspecialchars($message) ?></p>
<?php if ($saved): ?><img src="<?= $saved ?>" width="160" style="border-radius:50%"><?php endif; ?>
</body></html>
