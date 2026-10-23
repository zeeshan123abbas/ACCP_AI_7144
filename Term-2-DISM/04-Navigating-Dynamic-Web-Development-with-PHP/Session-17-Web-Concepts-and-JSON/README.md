# Session 17: PHP Web Concepts and JSON

> Module: Navigating Dynamic Web Development with PHP · Term 2 (DISM) · ⏱ ~2 hours

## 🎯 Learning Objectives

By the end of this session you will be able to:

- Redirect browsers with header() and send correct status codes
- Display a random image and random content
- Force a file download dialog safely
- Detect browser and platform from the User-Agent
- Encode and decode JSON and build a simple JSON API

## 📖 Concepts Explained

### 1. Headers and redirection

HTTP headers travel before the page body, so `header()` must run before any output.

```php
header('Location: thank-you.php', true, 302);  // temporary redirect
exit;                                           // always stop the script
```

Common status codes: 200 OK, 201 Created, 301 Moved Permanently, 302 Found, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 422 Unprocessable, 500 Server Error. Use `http_response_code(404)`.

### 2. File download

Send `Content-Type`, `Content-Disposition: attachment; filename="..."` and `Content-Length`, then `readfile()`. Only allow files from a whitelist or a fixed folder (use `basename()`), otherwise users could download `../db.php` (**path traversal**).

### 3. Browser and platform detection

`$_SERVER['HTTP_USER_AGENT']` contains a string such as `Mozilla/5.0 (Windows NT 10.0; Win64; x64) ... Chrome/126...`. Simple `preg_match` checks can guess the browser/OS for statistics. It can be faked, so never use it for security; for layout prefer responsive CSS.

### 4. JSON in PHP

| Function | Purpose |
|---|---|
| `json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE)` | PHP → JSON text |
| `json_decode($json, true)` | JSON → associative array (`false` gives objects) |
| `JSON_THROW_ON_ERROR` | throw exceptions on invalid JSON |

A JSON API sets `header('Content-Type: application/json')` and echoes `json_encode(...)`.

## 💻 Code Examples

All examples below are also saved as files in this folder, so you can open and run them directly.

### Example 1: Data file (`quotes.json`)

```json
[
  {"text": "Code is like humour. When you have to explain it, it is bad.", "author": "Cory House"},
  {"text": "First, solve the problem. Then, write the code.", "author": "John Johnson"},
  {"text": "Simplicity is the soul of efficiency.", "author": "Austin Freeman"},
  {"text": "Make it work, make it right, make it fast.", "author": "Kent Beck"},
  {"text": "The best error message is the one that never shows up.", "author": "Thomas Fuchs"}
]
```

**How it works:**

A small JSON array of quote objects used by the API.

### Example 2: Random quote JSON API (`api.php`)

```php
<?php
// api.php  - GET api.php            -> one random quote
//            GET api.php?all=1      -> all quotes
//            POST api.php (JSON body {"text":"..","author":".."}) -> add a quote
header('Content-Type: application/json; charset=utf-8');
$file = __DIR__ . '/quotes.json';

try {
    $quotes = json_decode(file_get_contents($file), true, flags: JSON_THROW_ON_ERROR);

    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        $in = json_decode(file_get_contents('php://input'), true, flags: JSON_THROW_ON_ERROR);
        if (empty($in['text']) || empty($in['author'])) {
            http_response_code(422);
            echo json_encode(['error' => 'text and author are required']);
            exit;
        }
        $quotes[] = ['text' => trim($in['text']), 'author' => trim($in['author'])];
        file_put_contents($file, json_encode($quotes, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE), LOCK_EX);
        http_response_code(201);
        echo json_encode(['message' => 'Quote added', 'count' => count($quotes)]);
        exit;
    }

    echo isset($_GET['all'])
        ? json_encode($quotes, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE)
        : json_encode($quotes[array_rand($quotes)], JSON_UNESCAPED_UNICODE);
} catch (JsonException $e) {
    http_response_code(400);
    echo json_encode(['error' => 'Invalid JSON: ' . $e->getMessage()]);
}
```

**How it works:**

- `php://input` reads the raw request body for JSON POSTs.
- Status codes tell clients what happened: 201 created, 422 validation error, 400 bad JSON.
- `LOCK_EX` prevents two requests writing the file at the same time.

### Example 3: Quote page, random image, download and browser info (`index.php`)

```php
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
```

**How it works:**

- Put some pictures in an `images/` folder to see a different one on every refresh.
- The quote is loaded from `api.php` with `fetch`, so the button changes it without reloading.
- Browser/OS detection uses simple `str_contains` checks on the User-Agent; Edge is checked before Chrome because its UA also contains "Chrome".

### Example 4: Safe download dialog (`download.php`)

```php
<?php
// download.php?file=quotes.json
$allowed = ['quotes.json' => 'application/json'];
$name = basename($_GET['file'] ?? '');            // strips ../ paths
if (!isset($allowed[$name]) || !is_file(__DIR__ . "/$name")) {
    http_response_code(404);
    exit('File not found');
}
header('Content-Type: ' . $allowed[$name]);
header('Content-Disposition: attachment; filename="' . $name . '"');
header('Content-Length: ' . filesize(__DIR__ . "/$name"));
readfile(__DIR__ . "/$name");
exit;
```

**How it works:**

`basename` and a whitelist block path traversal; `Content-Disposition: attachment` makes the browser show the save dialog.

### Example 5: Redirect examples (`redirect.php`)

```php
<?php
// redirect.php?to=home|docs|old
$targets = ['home' => 'index.php', 'docs' => 'https://www.php.net/manual/en/', 'old' => 'index.php'];
$to = $_GET['to'] ?? 'home';
if (!isset($targets[$to])) { http_response_code(400); exit('Unknown target'); }
$code = $to === 'old' ? 301 : 302;        // 301 = moved permanently
header('Location: ' . $targets[$to], true, $code);
exit;
```

**How it works:**

Redirect targets are whitelisted to avoid **open redirects**, which attackers abuse for phishing.

## 🧪 Lab Practice

1. Call `api.php` and `api.php?all=1` in the browser and in Postman.
2. POST a new quote with Postman (Body → raw → JSON) and check `quotes.json`.
3. Add a `?author=` filter to the API.
4. Log each visitor's browser and platform to a CSV and show counts.
5. Create a download page for three PDF notes using a whitelist.

## 📝 Assignment

Build a **Random Quote Generator** site: a JSON file with 20 quotes in categories, an API supporting `?category=`, a page with a category dropdown that loads quotes via fetch, and a "Download as JSON" button.

## ❓ Quick Quiz

1. Which header performs a redirect?
   - a) Content-Type
   - b) Location
   - c) Refresh-Now
   - d) Accept
2. Which function converts JSON to an associative array?
3. Which header triggers a download dialog?
4. Why call exit after header('Location: ...')?
5. Status code for 'resource created'?

<details>
<summary>Show answers</summary>

1. b) Location
2. `json_decode($json, true)`
3. `Content-Disposition: attachment; filename=...`
4. To stop the script so no further code runs or output is sent.
5. 201

</details>

## 💼 Interview Questions

1. **What is path traversal and how do you prevent it in downloads?**

   <details><summary>Model answer</summary>

   Using ../ in file parameters to read files outside the intended folder; prevent with basename(), whitelists and realpath checks.

   </details>

2. **How do you build a JSON API endpoint in plain PHP?**

   <details><summary>Model answer</summary>

   Set Content-Type: application/json, read input from $_GET or php://input, validate, set the status code and echo json_encode() of the response.

   </details>

3. **Why is User-Agent detection unreliable?**

   <details><summary>Model answer</summary>

   The header is supplied by the client and can be changed or spoofed; use it only for analytics, not security.

   </details>

## ✅ Summary

- header() sends redirects, content types and status codes before output.
- Downloads need Content-Disposition plus whitelisting.
- The User-Agent hints at browser and OS but can be faked.
- json_encode / json_decode power simple APIs.

---

[⬅ Previous](../Session-16-OOP-Inheritance-Interfaces/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-18-PHP-AJAX-Live-Search-Cart/README.md)

<sub>Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad</sub>
