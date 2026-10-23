# Session 04: Forms, Configuration and Migrations

> Module: Laravel Framework for Web Applications using PHP · Term 2 (DISM) · ⏱ ~2 hours

## 🎯 Learning Objectives

By the end of this session you will be able to:

- Configure the .env file for MySQL
- Create and run migrations with Artisan
- Build forms with CSRF protection and Blade helpers
- Submit a form to a controller and validate input
- Style pages with Bootstrap (or Tailwind via Vite)

## 📖 Concepts Explained

### 1. Database configuration

Edit `.env`:

```
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=student_portal
DB_USERNAME=root
DB_PASSWORD=
```

Create the empty database in phpMyAdmin first. Run `php artisan config:clear` if changes do not apply.

### 2. Migrations = version control for your schema

A migration is a PHP class with `up()` (apply) and `down()` (undo). The whole team runs the same migrations and gets identical tables.

| Command | Effect |
|---|---|
| `php artisan make:migration create_messages_table` | new migration file |
| `php artisan migrate` | run pending migrations |
| `php artisan migrate:rollback` | undo last batch |
| `php artisan migrate:fresh --seed` | drop all, re-run, seed |
| `php artisan migrate:status` | what has run |

Common column types: `id()`, `string()`, `text()`, `integer()`, `decimal()`, `boolean()`, `date()`, `foreignId()->constrained()`, `timestamps()`, `softDeletes()`. Modifiers: `nullable()`, `default()`, `unique()`.

### 3. Forms in Blade

- Every POST form needs `@csrf` (a hidden token) or Laravel returns **419 Page Expired**.
- `@method('PUT')` / `@method('DELETE')` spoof other HTTP verbs.
- `old('field')` refills fields after validation errors; `@error('field')` shows messages.

## 💻 Code Examples

All examples below are also saved as files in this folder, so you can open and run them directly.

### Example 1: Migration (`database/migrations/2025_01_01_000000_create_messages_table.php`)

```php
<?php
// php artisan make:migration create_messages_table
use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('messages', function (Blueprint $table) {
            $table->id();
            $table->string('name', 100);
            $table->string('email');
            $table->string('subject')->nullable();
            $table->text('message');
            $table->boolean('is_read')->default(false);
            $table->timestamps();
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('messages');
    }
};
```

**How it works:**

`up()` creates the table; `down()` removes it on rollback. `timestamps()` adds `created_at` and `updated_at`.

### Example 2: Controller with validation (`app/Http/Controllers/ContactController.php`)

```php
<?php
// php artisan make:controller ContactController
namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class ContactController extends Controller
{
    public function create()
    {
        return view('contact');
    }

    public function store(Request $request)
    {
        $data = $request->validate([
            'name'    => 'required|string|min:3|max:100',
            'email'   => 'required|email',
            'subject' => 'nullable|string|max:150',
            'message' => 'required|string|min:10',
        ]);

        DB::table('messages')->insert($data + ['created_at' => now(), 'updated_at' => now()]);

        return redirect()->route('contact.create')->with('success', 'Thanks! We will reply soon.');
    }
}
```

**How it works:**

`validate()` automatically redirects back with errors and old input if a rule fails. On success we insert with the query builder (Eloquent comes next session) and flash a message.

### Example 3: Form routes (`routes/web.php`)

```php
<?php
use App\Http\Controllers\ContactController;
use Illuminate\Support\Facades\Route;

Route::get('/contact', [ContactController::class, 'create'])->name('contact.create');
Route::post('/contact', [ContactController::class, 'store'])->name('contact.store');
```

**How it works:**

GET shows the form; POST handles the submission.

### Example 4: Contact form view (`resources/views/contact.blade.php`)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"><title>Contact</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="container py-4" style="max-width:600px">
  <h2>Contact us</h2>
  @if (session('success'))
    <div class="alert alert-success">{{ session('success') }}</div>
  @endif
  <form method="POST" action="{{ route('contact.store') }}">
    @csrf
    <div class="mb-3">
      <label class="form-label">Name</label>
      <input name="name" value="{{ old('name') }}" class="form-control @error('name') is-invalid @enderror">
      @error('name') <div class="invalid-feedback">{{ $message }}</div> @enderror
    </div>
    <div class="mb-3">
      <label class="form-label">Email</label>
      <input name="email" type="email" value="{{ old('email') }}" class="form-control @error('email') is-invalid @enderror">
      @error('email') <div class="invalid-feedback">{{ $message }}</div> @enderror
    </div>
    <div class="mb-3">
      <label class="form-label">Subject</label>
      <input name="subject" value="{{ old('subject') }}" class="form-control">
    </div>
    <div class="mb-3">
      <label class="form-label">Message</label>
      <textarea name="message" rows="4" class="form-control @error('message') is-invalid @enderror">{{ old('message') }}</textarea>
      @error('message') <div class="invalid-feedback">{{ $message }}</div> @enderror
    </div>
    <button class="btn btn-primary">Send</button>
  </form>
</body>
</html>
```

**How it works:**

`@csrf` adds the token, `old()` keeps values, `@error` shows each field's message with Bootstrap styling.

## 🧪 Lab Practice

1. Configure MySQL in `.env`, create `student_portal` and run `php artisan migrate`.
2. Create and run the messages migration; check the table in phpMyAdmin.
3. Submit the form with empty fields, then valid data.
4. Remove `@csrf` and observe the 419 error, then restore it.
5. Add a `phone` column with a new migration (`add_phone_to_messages_table`) and roll it back.

## 📝 Assignment

Create a **Course Enquiry** form (name, email, phone, course select, preferred timing radio) with a migration, controller validation (including a regex for Pakistani mobile numbers) and a success message.

## ❓ Quick Quiz

1. What does @csrf add?
   - a) A captcha
   - b) A hidden token field
   - c) Validation rules
   - d) A cookie banner
2. Which command undoes the last migration batch?
3. What HTTP error appears without a CSRF token?
4. Which helper refills a field after errors?
5. Where do database credentials go?

<details>
<summary>Show answers</summary>

1. b) A hidden token field
2. `php artisan migrate:rollback`
3. 419 Page Expired
4. `old('field')`
5. In the `.env` file.

</details>

## 💼 Interview Questions

1. **What are migrations and why use them?**

   <details><summary>Model answer</summary>

   Version-controlled PHP files that create/modify tables, letting every developer and server reproduce the same schema and roll back changes.

   </details>

2. **How does Laravel validation work in a controller?**

   <details><summary>Model answer</summary>

   $request->validate() checks rules; on failure it redirects back with errors and old input; on success it returns the validated data.

   </details>

3. **Why should .env not be committed?**

   <details><summary>Model answer</summary>

   It contains secrets such as DB passwords and APP_KEY that differ per environment.

   </details>

## ✅ Summary

- Configure the database in `.env`.
- Migrations define and version your schema.
- Every POST form needs @csrf; use old() and @error for good UX.
- Validate in the controller before saving.

---

[⬅ Previous](../Session-03-Routing-Views-Blade/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-05-Eloquent-ORM-Basics/README.md)

<sub>Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad</sub>
