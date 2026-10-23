# Session 02: Setting Up the WordPress Environment

> Module: Build and Manage Websites with CMS · Term 2 (DISM) · ⏱ ~2 hours

## 🎯 Learning Objectives

By the end of this session you will be able to:

- List WordPress system requirements
- Install a local server (XAMPP or LocalWP)
- Create a MySQL database and user in phpMyAdmin
- Install WordPress manually and configure wp-config.php
- Configure General, Reading and Permalink settings

## 📖 Concepts Explained

### 1. Requirements (WordPress 6.5+)

PHP 7.4+ (8.1+ recommended), MySQL 5.7+ or MariaDB 10.4+, HTTPS support, Apache or Nginx with `mod_rewrite` for pretty permalinks.

### 2. Two local options

| XAMPP (manual install) | LocalWP (one-click) |
|---|---|
| teaches you every step | creates sites in a click |
| files in `C:\xampp\htdocs\mysite` | managed folders, SSL, Mailpit |

### 3. Manual installation steps

1. Start **Apache** and **MySQL** in XAMPP.
2. Download WordPress from https://wordpress.org/download/ and unzip into `C:\xampp\htdocs\mysite`.
3. Open `http://localhost/phpmyadmin` → **Databases** → create `wp_mysite` with collation `utf8mb4_unicode_ci`.
4. (Recommended) **User accounts** → add user `wp_user` with a strong password and privileges only on `wp_mysite`.
5. Visit `http://localhost/mysite` → choose language → enter database name, user, password, host `localhost`, table prefix (change `wp_` to something like `ms24_`).
6. WordPress writes `wp-config.php` (or you copy `wp-config-sample.php` and edit it yourself).
7. Enter **Site Title**, admin username (not "admin"), strong password, email → **Install WordPress**.

### 4. First settings

| Screen | What to set |
|---|---|
| Settings → General | Site title, tagline, timezone (Karachi), date format |
| Settings → Reading | static homepage vs latest posts; "Discourage search engines" ON while developing |
| Settings → Permalinks | **Post name** (`/%postname%/`) for clean URLs |
| Settings → Discussion | comment moderation |
| Users → Profile | display name, strong password |

### 5. Folder anatomy

`wp-admin/` (dashboard), `wp-includes/` (core), `wp-content/` (**your** themes, plugins, uploads — the only folder you back up besides the database), `wp-config.php` (settings and secrets).

## 💻 Code Examples

All examples below are also saved as files in this folder, so you can open and run them directly.

### Example 1: Key wp-config.php settings (`wp-config-snippet.php`)

```php
<?php
// Important parts of wp-config.php (not the whole file)

// ** Database settings ** //
define( 'DB_NAME', 'wp_mysite' );
define( 'DB_USER', 'wp_user' );
define( 'DB_PASSWORD', 'Use-A-Strong-Password-Here' );
define( 'DB_HOST', 'localhost' );
define( 'DB_CHARSET', 'utf8mb4' );
define( 'DB_COLLATE', '' );

// Unique keys and salts: generate at https://api.wordpress.org/secret-key/1.1/salt/
define( 'AUTH_KEY',  'paste-unique-phrase-here' );
// ... (7 more keys and salts)

// Table prefix: changing the default makes automated attacks a little harder
$table_prefix = 'ms24_';

// Development helpers (turn OFF on a live site)
define( 'WP_DEBUG', true );
define( 'WP_DEBUG_LOG', true );       // writes to wp-content/debug.log
define( 'WP_DEBUG_DISPLAY', false );

// Hardening
define( 'DISALLOW_FILE_EDIT', true ); // removes the theme/plugin code editor from the dashboard
define( 'WP_POST_REVISIONS', 10 );    // keep at most 10 revisions per post

/* That's all, stop editing! */
if ( ! defined( 'ABSPATH' ) ) {
    define( 'ABSPATH', __DIR__ . '/' );
}
require_once ABSPATH . 'wp-settings.php';
```

**How it works:**

- The four `DB_*` constants connect WordPress to the database you created.
- Keys and salts secure login cookies — always generate unique ones.
- `WP_DEBUG_LOG` records errors to a file without showing them to visitors.
- `DISALLOW_FILE_EDIT` prevents editing PHP from the dashboard if an admin account is compromised.

## 🧪 Lab Practice

1. Install XAMPP (or LocalWP) and create the database `wp_mysite` and user `wp_user`.
2. Install WordPress manually and log in at `/wp-admin`.
3. Set site title, tagline, timezone (UTC+5 / Karachi) and Post name permalinks.
4. Enable 'Discourage search engines' while developing.
5. Open `wp-config.php` and add `DISALLOW_FILE_EDIT`; confirm the editor disappears.

## 📝 Assignment

Install a second site with LocalWP, then write `install-report.md` comparing manual (XAMPP) vs one-click installation: steps, time taken, problems and screenshots of the dashboard and permalink settings.

## ❓ Quick Quiz

1. Which file stores database credentials?
   - a) functions.php
   - b) wp-config.php
   - c) .htaccess
   - d) index.php
2. Which permalink setting is best for SEO?
3. Which folder holds themes, plugins and uploads?
4. Why avoid the username 'admin'?
5. Which constant enables debug mode?

<details>
<summary>Show answers</summary>

1. b) wp-config.php
2. Post name (`/%postname%/`).
3. `wp-content`
4. It is the first guess in brute-force attacks.
5. `WP_DEBUG`

</details>

## 💼 Interview Questions

1. **Walk through a manual WordPress install.**

   <details><summary>Model answer</summary>

   Create database and user, upload/unzip files, configure wp-config.php (or run the setup wizard), then run the installer to create the admin account and site title.

   </details>

2. **What should you back up for a WordPress site?**

   <details><summary>Model answer</summary>

   The database and the wp-content folder (plus wp-config.php).

   </details>

3. **What do keys and salts do?**

   <details><summary>Model answer</summary>

   They add randomness to cookie and nonce hashing, making stolen cookies harder to forge.

   </details>

## ✅ Summary

- WordPress needs PHP, MySQL/MariaDB and a web server.
- Create a dedicated DB user, then run the installer.
- Configure timezone, reading and Post-name permalinks first.
- wp-config.php holds credentials, salts and debug/hardening settings.

---

[⬅ Previous](../Session-01-Introduction-to-CMS-and-WordPress/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-03-WordPress-Themes/README.md)

<sub>Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad</sub>
