# Session 09: File Uploading and File Handling

> Module: Navigating Dynamic Web Development with PHP · Term 2 (DISM) · ⏱ ~2 hours

## 🎯 Learning Objectives

By the end of this session you will be able to:

- Read and write files with file_get_contents, fopen, fwrite and fgets
- Work with directories and file information
- Build a secure file upload form
- Validate upload errors, size and real MIME type
- Handle errors with exceptions (try/catch/finally)

## 📖 Concepts Explained

### 1. Reading and writing files

| Task | Function |
|---|---|
| Read whole file | `file_get_contents($path)`, `readfile($path)` (outputs directly), `file($path)` (array of lines) |
| Write whole file | `file_put_contents($path, $data, FILE_APPEND)` |
| Stream line by line | `fopen`, `fgets`, `fwrite`, `fclose` |
| CSV | `fgetcsv`, `fputcsv` |
| Info | `file_exists`, `is_file`, `is_dir`, `filesize`, `filemtime`, `pathinfo` |
| Folders | `mkdir`, `scandir`, `glob`, `unlink`, `rename` |

`fopen` modes: `r` read, `w` write (truncate), `a` append, `x` create new only, `r+` read/write.

### 2. File upload flow

1. Form must use `method="post"` and `enctype="multipart/form-data"`.
2. PHP stores the file temporarily; details are in `$_FILES['field']` (`name`, `type`, `tmp_name`, `error`, `size`).
3. Check `error === UPLOAD_ERR_OK`, size, extension **and** real MIME (`finfo`).
4. Generate a new safe file name and call `move_uploaded_file()`.

Limits come from `php.ini`: `upload_max_filesize`, `post_max_size`.

**Never trust** the original file name or the browser-sent `type`. Store uploads outside the code folder or block script execution in the uploads folder.

### 3. Exception handling

```php
try {
    risky();
} catch (RuntimeException $e) {
    echo "Problem: " . $e->getMessage();
} finally {
    // always runs: close files, log
}
```

You can `throw new InvalidArgumentException("...")` and create custom exception classes.

## 💻 Code Examples

All examples below are also saved as files in this folder, so you can open and run them directly.

### Example 1: Secure profile picture upload (`upload-profile.php`)

```php
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
```

**How it works:**

- Every failure throws a `RuntimeException`; the `catch` block turns it into a friendly message.
- `finfo` reads the file's actual bytes to detect its type; the browser's `type` could be faked.
- A random name prevents overwriting and blocks names like `shell.php.jpg` tricks.
- Each upload is appended to a log with `FILE_APPEND`.

### Example 2: Reading and writing text and CSV (`notes-file.php`)

```php
<?php
// notes-file.php  (run: php notes-file.php)
$file = __DIR__ . '/students.csv';

$h = fopen($file, 'w');
fputcsv($h, ['id', 'name', 'city']);
foreach ([[1, 'Ayesha', 'Karachi'], [2, 'Bilal', 'Hyderabad'], [3, 'Sana', 'Karachi']] as $row) fputcsv($h, $row);
fclose($h);

$h = fopen($file, 'r');
$header = fgetcsv($h);
while (($row = fgetcsv($h)) !== false) {
    $rec = array_combine($header, $row);
    echo "{$rec['id']}: {$rec['name']} from {$rec['city']}" . PHP_EOL;
}
fclose($h);

echo "Size: " . filesize($file) . " bytes, modified " . date('d-m-Y H:i', filemtime($file)) . PHP_EOL;

try {
    $data = @file_get_contents(__DIR__ . '/missing.txt');
    if ($data === false) throw new Exception("missing.txt not found");
} catch (Exception $e) {
    echo "Handled: " . $e->getMessage() . PHP_EOL;
} finally {
    echo "Done." . PHP_EOL;
}
```

**How it works:**

- `fputcsv`/`fgetcsv` handle commas and quotes correctly, unlike `explode(',')`.
- `array_combine` turns the header and each row into an associative array.
- `finally` runs whether or not an exception happened.

## 🧪 Lab Practice

1. Upload a `.txt` renamed to `.jpg` and confirm it is rejected.
2. Show a gallery of all files in `uploads/` using `glob('uploads/*.{jpg,png,webp}', GLOB_BRACE)`.
3. Allow deleting an uploaded image with `unlink` (confirm first).
4. Write a guestbook that appends messages to `guestbook.txt` and lists them newest first.
5. Create a custom `FileTooLargeException` class and throw it.

## 📝 Assignment

Build `assignments-upload.php` where a student enters roll number and uploads a PDF (max 5 MB). Save as `ROLLNO_timestamp.pdf`, log uploads to a CSV and show a table of previous submissions with download links.

## ❓ Quick Quiz

1. Which form attribute is required for uploads?
   - a) action
   - b) enctype="multipart/form-data"
   - c) novalidate
   - d) target
2. Which function moves the uploaded temp file?
3. Why not trust `$_FILES['x']['type']`?
4. Which fopen mode appends?
5. Which block always runs in try/catch?

<details>
<summary>Show answers</summary>

1. b) enctype="multipart/form-data"
2. `move_uploaded_file()`
3. It is sent by the browser and can be faked; detect MIME with finfo.
4. `a`
5. `finally`

</details>

## 💼 Interview Questions

1. **How do you make file uploads secure?**

   <details><summary>Model answer</summary>

   Check error and size, verify real MIME, whitelist extensions, rename with random names, store outside web root or disable script execution there, and limit sizes in php.ini.

   </details>

2. **Difference between file_get_contents and fopen/fgets?**

   <details><summary>Model answer</summary>

   file_get_contents loads the whole file into memory; fopen/fgets streams it line by line, better for large files.

   </details>

3. **What is the purpose of exceptions?**

   <details><summary>Model answer</summary>

   To separate error handling from normal logic and let errors propagate to a place that can handle them meaningfully.

   </details>

## ✅ Summary

- PHP reads/writes files with simple helpers or streams.
- Uploads need multipart forms and careful validation.
- Rename files and check real MIME types.
- Use try/catch/finally and throw meaningful exceptions.

---

[⬅ Previous](../Session-08-Cookies-and-Sessions/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-10-PHP-MySQL-Create-Read/README.md)

<sub>Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad</sub>
