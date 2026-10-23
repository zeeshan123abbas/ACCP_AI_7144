# Session 08: Authentication, Middleware and Final Application

> Module: Laravel Framework for Web Applications using PHP · Term 2 (DISM) · ⏱ ~2 hours

## 🎯 Learning Objectives

By the end of this session you will be able to:

- Install authentication scaffolding with Laravel Breeze
- Protect routes with the auth middleware and route groups
- Use the authenticated user in controllers and Blade
- Implement simple role-based access (admin vs user)
- Complete a blog where only logged-in users can manage posts

## 📖 Concepts Explained

### 1. Authentication starter kits

Older tutorials use `php artisan make:auth` (Laravel ≤ 5.8) or `laravel/ui`. In Laravel 11 the official, simplest kit is **Breeze**: login, registration, logout, password reset, email verification and profile pages in Blade.

```bash
composer require laravel/breeze --dev
php artisan breeze:install blade
php artisan migrate
npm install && npm run dev
```

### 2. Middleware

Middleware is a filter that runs before/after a request. `auth` redirects guests to `/login`; `guest` keeps logged-in users away from login pages; `verified` requires a verified email. Write your own with `php artisan make:middleware`.

```php
Route::middleware('auth')->group(function () {
    Route::resource('posts', PostController::class)->except(['index', 'show']);
});
```

### 3. Current user

Controller: `auth()->user()`, `$request->user()`, `auth()->id()`. Blade: `@auth ... @endauth`, `@guest ... @endguest`, `{{ auth()->user()->name }}`.

### 4. Roles

Add a `role` column to `users`, create an `admin` middleware, register its alias in `bootstrap/app.php`, and redirect admins after login. For fine-grained rules use **Gates/Policies** (e.g. "only the author can edit this post").

## 💻 Code Examples

All examples below are also saved as files in this folder, so you can open and run them directly.

### Example 1: Roles and post ownership (`database/migrations/2025_01_04_000000_add_role_and_user_to_tables.php`)

```php
<?php
use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration {
    public function up(): void
    {
        Schema::table('users', fn (Blueprint $t) => $t->string('role')->default('user')->after('email'));
        Schema::table('posts', fn (Blueprint $t) => $t->foreignId('user_id')->nullable()->constrained()->cascadeOnDelete());
    }
    public function down(): void
    {
        Schema::table('posts', fn (Blueprint $t) => $t->dropConstrainedForeignId('user_id'));
        Schema::table('users', fn (Blueprint $t) => $t->dropColumn('role'));
    }
};
```

**How it works:**

Every user gets a role (default `user`) and every post an owner.

### Example 2: Admin middleware (`app/Http/Middleware/EnsureUserIsAdmin.php`)

```php
<?php
// php artisan make:middleware EnsureUserIsAdmin
namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;
use Symfony\Component\HttpFoundation\Response;

class EnsureUserIsAdmin
{
    public function handle(Request $request, Closure $next): Response
    {
        abort_unless($request->user()?->role === 'admin', 403, 'Admins only.');
        return $next($request);
    }
}
```

**How it works:**

Stops non-admins with a 403; otherwise passes the request on.

### Example 3: Registering the middleware alias (Laravel 11) (`bootstrap/app.php`)

```php
<?php
use Illuminate\Foundation\Application;
use Illuminate\Foundation\Configuration\Exceptions;
use Illuminate\Foundation\Configuration\Middleware;

return Application::configure(basePath: dirname(__DIR__))
    ->withRouting(
        web: __DIR__.'/../routes/web.php',
        commands: __DIR__.'/../routes/console.php',
        health: '/up',
    )
    ->withMiddleware(function (Middleware $middleware) {
        $middleware->alias(['admin' => \App\Http\Middleware\EnsureUserIsAdmin::class]);
    })
    ->withExceptions(function (Exceptions $exceptions) {
        //
    })->create();
```

**How it works:**

Laravel 11 registers middleware in `bootstrap/app.php` (there is no `Kernel.php` any more).

### Example 4: Public, authenticated and admin route groups (`routes/web.php`)

```php
<?php
use App\Http\Controllers\PostController;
use App\Http\Controllers\ProfileController;
use Illuminate\Support\Facades\Route;

// Logged-in users manage posts (registered FIRST so /posts/create is not caught by /posts/{post})
Route::middleware('auth')->group(function () {
    Route::resource('posts', PostController::class)->except(['index', 'show']);
    Route::get('/dashboard', fn () => auth()->user()->role === 'admin'
        ? redirect()->route('admin.home')
        : view('dashboard'))->name('dashboard');
    Route::get('/profile', [ProfileController::class, 'edit'])->name('profile.edit');
    Route::patch('/profile', [ProfileController::class, 'update'])->name('profile.update');
    Route::delete('/profile', [ProfileController::class, 'destroy'])->name('profile.destroy');
});

// Guests and users can read
Route::get('/', [PostController::class, 'index'])->name('home');
Route::resource('posts', PostController::class)->only(['index', 'show']);

// Admin area
Route::middleware(['auth', 'admin'])->prefix('admin')->name('admin.')->group(function () {
    Route::get('/', fn () => view('admin.home', [
        'users' => \App\Models\User::withCount('posts')->get(),
    ]))->name('home');
});

require __DIR__.'/auth.php';   // login, register, logout routes from Breeze
```

**How it works:**

Route order matters: the protected routes (including `/posts/create`) are registered before the public `/posts/{post}` route. Reading is public, writing requires `auth`, and `/admin` requires both `auth` and `admin`. Dashboard redirects admins (role-based redirection).

### Example 5: Only the author (or an admin) may edit (`app/Policies/PostPolicy.php`)

```php
<?php
// php artisan make:policy PostPolicy --model=Post
namespace App\Policies;

use App\Models\{Post, User};

class PostPolicy
{
    public function update(User $user, Post $post): bool
    {
        return $user->role === 'admin' || $post->user_id === $user->id;
    }

    public function delete(User $user, Post $post): bool
    {
        return $this->update($user, $post);
    }
}
```

**How it works:**

Laravel discovers this policy automatically. In the controller call `Gate::authorize('update', $post);` (use `Illuminate\Support\Facades\Gate`), and in Blade wrap buttons with `@can('update', $post) ... @endcan`. When creating posts, set the owner: `$request->user()->posts()->create($request->validated())` (add `posts()` hasMany to `User`).

### Example 6: Admin page (`resources/views/admin/home.blade.php`)

```html
@extends('layouts.app')
@section('content')
  <h2>Admin: users</h2>
  <table class="table">
    <tr><th>Name</th><th>Email</th><th>Role</th><th>Posts</th></tr>
    @foreach ($users as $u)
      <tr><td>{{ $u->name }}</td><td>{{ $u->email }}</td><td>{{ $u->role }}</td><td>{{ $u->posts_count }}</td></tr>
    @endforeach
  </table>
@endsection
```

**How it works:**

Needs a `posts()` hasMany relation on the `User` model for `withCount('posts')`; uses the layout from Session 07.

### Example 7: Navbar that knows who is logged in (`resources/views/partials/nav.blade.php`)

```html
<nav class="navbar navbar-expand bg-dark navbar-dark px-3">
  <a class="navbar-brand" href="{{ route('home') }}">Student Blog</a>
  <div class="ms-auto d-flex gap-2 align-items-center">
    @auth
      <span class="text-light">Hi, {{ auth()->user()->name }}</span>
      <a class="btn btn-sm btn-success" href="{{ route('posts.create') }}">Write</a>
      @if (auth()->user()->role === 'admin')
        <a class="btn btn-sm btn-warning" href="{{ route('admin.home') }}">Admin</a>
      @endif
      <form method="POST" action="{{ route('logout') }}">@csrf <button class="btn btn-sm btn-outline-light">Logout</button></form>
    @endauth
    @guest
      <a class="btn btn-sm btn-outline-light" href="{{ route('login') }}">Login</a>
      <a class="btn btn-sm btn-light" href="{{ route('register') }}">Register</a>
    @endguest
  </div>
</nav>
```

**How it works:**

`@auth`/`@guest` show different links; logout is a POST with `@csrf`.

## 🧪 Lab Practice

1. Install Breeze in your blog project, migrate and register a user.
2. Wrap create/edit/delete routes in the `auth` middleware; test as a guest.
3. Add the role column, make yourself admin via Tinker (`User::first()->update(['role'=>'admin'])`) and open `/admin`.
4. Create the PostPolicy and hide Edit/Delete buttons with `@can`.
5. Show 'Posted by NAME' on each post using a `user()` relationship.

## 📝 Assignment

**Final mini project – Student Blog / Info App**: guests view published posts; registered users create and manage their own posts with categories and tags; admins see all users and can delete any post. Include validation, pagination, flash messages, soft deletes and a README with setup steps and screenshots.

## ❓ Quick Quiz

1. Which package is Laravel 11's simple Blade auth kit?
   - a) Passport
   - b) Breeze
   - c) Horizon
   - d) Telescope
2. Which middleware redirects guests to login?
3. Where are middleware aliases registered in Laravel 11?
4. Blade directive for logged-in-only content?
5. What is a Policy?

<details>
<summary>Show answers</summary>

1. b) Breeze
2. `auth`
3. `bootstrap/app.php`
4. `@auth ... @endauth`
5. A class grouping authorization rules for a model (e.g. who may update a post).

</details>

## 💼 Interview Questions

1. **Authentication vs authorization in Laravel?**

   <details><summary>Model answer</summary>

   Authentication (guards, Breeze) identifies the user; authorization (gates, policies, middleware) decides what they may do.

   </details>

2. **What is middleware?**

   <details><summary>Model answer</summary>

   Code that filters HTTP requests entering the app (e.g. auth, CSRF, throttling) and can modify responses.

   </details>

3. **How would you implement role-based redirects after login?**

   <details><summary>Model answer</summary>

   Check the user's role after authentication (in a dashboard route or the login controller's redirect) and send admins to the admin area and others to the user dashboard.

   </details>

## ✅ Summary

- Breeze adds complete authentication in minutes.
- The auth middleware and route groups protect pages.
- auth()->user(), @auth and @guest expose the current user.
- Custom middleware and policies implement roles and ownership.

---

[⬅ Previous](../Session-07-CRUD-Controllers-Validation/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../../06-Build-and-Manage-Websites-with-CMS/README.md)

<sub>Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad</sub>
