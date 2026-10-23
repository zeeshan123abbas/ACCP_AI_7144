# Session 01: Setting up the Laravel Environment

> Module: Laravel Framework for Web Applications using PHP · Term 2 (DISM) · ⏱ ~2 hours

## 🎯 Learning Objectives

By the end of this session you will be able to:

- List the tools needed for Laravel development
- Install PHP 8.2+, Composer, Node.js and Git
- Create a Laravel 11 project with Composer or the Laravel installer
- Run the app with php artisan serve
- Describe Homestead, Sail, Herd and Laragon as environment options

## 📖 Concepts Explained

### 1. What you need

| Tool | Why | Check |
|---|---|---|
| PHP 8.2+ (with `pdo_mysql`, `mbstring`, `openssl`, `fileinfo`, `zip`) | Laravel 11 requires it | `php -v` |
| Composer 2 | installs Laravel and packages | `composer -V` |
| Node.js 20 + npm | builds CSS/JS with Vite | `node -v` |
| Git / Git Bash | version control, nicer terminal on Windows | `git --version` |
| MySQL 8 (XAMPP/Laragon) | database | |
| VS Code + "Laravel" & "PHP Intelephense" extensions | editing | |

### 2. Environment options

| Option | Notes |
|---|---|
| **XAMPP / Laragon** + Composer | simplest on Windows; Laragon has one-click Laravel |
| **Laravel Herd** | native PHP + nginx for Windows/macOS, very fast |
| **Laravel Sail** | Docker-based; same environment for the whole team |
| **Homestead** | official Vagrant + VirtualBox box with everything pre-installed (heavier, legacy but still documented) |

### 3. Creating a project

```bash
composer create-project laravel/laravel student-portal
# or: composer global require laravel/installer  then  laravel new student-portal
cd student-portal
php artisan serve          # http://127.0.0.1:8000
```

Laravel 11 uses **SQLite** by default; switch to MySQL in `.env` (Session 04). Run `npm install && npm run dev` when you start using Vite assets.

### 4. Homestead in brief

1. Install VirtualBox and Vagrant.
2. `vagrant box add laravel/homestead`.
3. Clone the Homestead repo, run `init.bat`, edit `Homestead.yaml` (folders, sites, databases).
4. `vagrant up`, add `192.168.56.56 student-portal.test` to your hosts file.

## 💻 Code Examples

All examples below are also saved as files in this folder, so you can open and run them directly.

### Example 1: Complete setup checklist (`setup-commands.md`)

```markdown
# Laravel setup checklist (Windows)

1. Install XAMPP 8.2+ and add `C:\xampp\php` to the PATH  ->  `php -v`
2. In `C:\xampp\php\php.ini` enable: `extension=zip`, `extension=fileinfo`, `extension=pdo_mysql`
3. Install Composer (https://getcomposer.org/Composer-Setup.exe)  ->  `composer -V`
4. Install Node.js 20 LTS  ->  `node -v` and `npm -v`
5. Install Git for Windows  ->  `git --version`
6. Create the project:
       composer create-project laravel/laravel student-portal
       cd student-portal
       php artisan --version
       php artisan serve
7. Open http://127.0.0.1:8000 - you should see the Laravel welcome page
8. Open the folder in VS Code: `code .`
9. Initialise Git:
       git init && git add . && git commit -m "Fresh Laravel 11 install"
```

**How it works:**

Follow the list top to bottom; each step has a command to verify it worked.

### Example 2: Your first change (`routes/web.php`)

```php
<?php
// routes/web.php
use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});

Route::get('/hello', function () {
    return 'Hello from Laravel ' . app()->version() . ' on PHP ' . PHP_VERSION;
});
```

**How it works:**

Add the `/hello` route, save, and visit `http://127.0.0.1:8000/hello` — no server restart needed.

## 🧪 Lab Practice

1. Install all tools and verify each with its version command.
2. Create `student-portal` and run it with `php artisan serve`.
3. Change the port: `php artisan serve --port=8080`.
4. Add the `/hello` route.
5. Commit the fresh project to Git.

## 📝 Assignment

Write a one-page `SETUP.md` in your project documenting your exact versions (PHP, Composer, Node, Laravel), the commands you ran, and any errors you solved.

## ❓ Quick Quiz

1. Which tool installs Laravel?
   - a) npm
   - b) pip
   - c) Composer
   - d) NuGet
2. Which command starts the development server?
3. Minimum PHP version for Laravel 11?
4. What is Homestead?
5. Default database in a fresh Laravel 11 app?

<details>
<summary>Show answers</summary>

1. c) Composer
2. `php artisan serve`
3. PHP 8.2
4. An official Vagrant box (virtual machine) with a complete Laravel environment.
5. SQLite

</details>

## 💼 Interview Questions

1. **What is Composer and how does Laravel use it?**

   <details><summary>Model answer</summary>

   PHP's dependency manager; it downloads Laravel and its packages into vendor/ and provides autoloading.

   </details>

2. **Sail vs Homestead?**

   <details><summary>Model answer</summary>

   Sail uses Docker containers defined per project; Homestead uses a Vagrant virtual machine shared across projects.

   </details>

3. **Why commit right after installing?**

   <details><summary>Model answer</summary>

   It gives a clean baseline to compare or roll back to.

   </details>

## ✅ Summary

- Laravel needs PHP 8.2+, Composer, Node and a database.
- Create projects with `composer create-project laravel/laravel`.
- `php artisan serve` runs a local server.
- Homestead, Sail, Herd and Laragon are alternative environments.

---

[⬅ Previous](../README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-02-Fundamentals-and-MVC/README.md)

<sub>Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad</sub>
