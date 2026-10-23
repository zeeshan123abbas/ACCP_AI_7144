# Session 03: Routing, Views and Blade

> Module: Laravel Framework for Web Applications using PHP · Term 2 (DISM) · ⏱ ~2 hours

## 🎯 Learning Objectives

By the end of this session you will be able to:

- Plan an application's pages and routes
- Write static and dynamic routes with parameters and constraints
- Name routes and generate URLs
- Pass data from routes/controllers to Blade views
- Use Blade directives and master layouts

## 📖 Concepts Explained

### 1. Routes

```php
Route::get('/contact', ...);                    // static
Route::get('/user/{name}', ...);                // required parameter
Route::get('/posts/{id?}', ...);                // optional parameter (give a default)
Route::get('/student/{id}', ...)->whereNumber('id');
Route::view('/terms', 'pages.terms');           // view only
Route::redirect('/home', '/');
```

HTTP verbs: `get`, `post`, `put`, `patch`, `delete`, `match`, `any`. Group shared settings with `Route::prefix('admin')->name('admin.')->group(...)`.

### 2. Blade essentials

| Syntax | Purpose |
|---|---|
| `{{ $x }}` | echo escaped |
| `{!! $html !!}` | echo raw (trusted HTML only) |
| `@if / @elseif / @else / @endif` | conditions |
| `@foreach / @forelse / @empty` | loops (`$loop->iteration`) |
| `@extends('layouts.app')` | use a layout |
| `@section('content') ... @endsection` | fill a section |
| `@yield('content')` | placeholder in the layout |
| `@include('partials.nav')` | include a partial |
| `{{-- comment --}}` | Blade comment |

Views live in `resources/views`; dots separate folders (`pages.home` = `pages/home.blade.php`).

## 💻 Code Examples

All examples below are also saved as files in this folder, so you can open and run them directly.

### Example 1: Routes for a small site (`routes/web.php`)

```php
<?php
use Illuminate\Support\Facades\Route;

Route::view('/', 'pages.home')->name('home');
Route::view('/about', 'pages.about')->name('about');
Route::view('/contact', 'pages.contact')->name('contact');

Route::get('/user/{name}', function (string $name) {
    return view('pages.user', ['name' => ucfirst($name)]);
})->where('name', '[A-Za-z]+')->name('user.show');

Route::get('/courses/{level?}', function (string $level = 'all') {
    $courses = [
        ['title' => 'PHP', 'level' => 'beginner'],
        ['title' => 'Laravel', 'level' => 'intermediate'],
        ['title' => 'System Design', 'level' => 'advanced'],
    ];
    if ($level !== 'all') {
        $courses = array_filter($courses, fn ($c) => $c['level'] === $level);
    }
    return view('pages.courses', compact('courses', 'level'));
})->name('courses');
```

**How it works:**

Dynamic segments become function parameters; `where` adds a regex constraint; `?` makes `level` optional with default `all`.

### Example 2: Master layout (`resources/views/layouts/app.blade.php`)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>@yield('title', 'Student Portal')</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
  <nav class="navbar navbar-expand bg-dark navbar-dark px-3">
    <a class="navbar-brand" href="{{ route('home') }}">Student Portal</a>
    <div class="navbar-nav">
      <a class="nav-link {{ request()->routeIs('about') ? 'active' : '' }}" href="{{ route('about') }}">About</a>
      <a class="nav-link {{ request()->routeIs('courses') ? 'active' : '' }}" href="{{ route('courses') }}">Courses</a>
      <a class="nav-link {{ request()->routeIs('contact') ? 'active' : '' }}" href="{{ route('contact') }}">Contact</a>
    </div>
  </nav>
  <main class="container py-4">
    @yield('content')
  </main>
  <footer class="text-center text-muted py-3">&copy; {{ date('Y') }} Student Portal</footer>
</body>
</html>
```

**How it works:**

Pages extend this file; `@yield` marks where their content goes and `request()->routeIs()` highlights the active link.

### Example 3: Home page (`resources/views/pages/home.blade.php`)

```html
@extends('layouts.app')
@section('title', 'Home')
@section('content')
  <h1>Welcome!</h1>
  <p>Try <a href="{{ route('user.show', 'ayesha') }}">/user/ayesha</a> or
     <a href="{{ route('courses', 'beginner') }}">beginner courses</a>.</p>
@endsection
```

**How it works:**

`route('user.show', 'ayesha')` generates `/user/ayesha` from the route name.

### Example 4: Loop with @forelse (`resources/views/pages/courses.blade.php`)

```html
@extends('layouts.app')
@section('title', 'Courses')
@section('content')
  <h2>Courses ({{ $level }})</h2>
  <ul class="list-group">
    @forelse ($courses as $course)
      <li class="list-group-item">{{ $loop->iteration }}. {{ $course['title'] }}
        @if ($course['level'] === 'advanced') <span class="badge bg-danger">Advanced</span> @endif
      </li>
    @empty
      <li class="list-group-item">No courses at this level.</li>
    @endforelse
  </ul>
@endsection
```

**How it works:**

`@forelse` shows the `@empty` block when the list is empty; `$loop->iteration` counts from 1.

### Example 5: Dynamic route view (`resources/views/pages/user.blade.php`)

```html
@extends('layouts.app')
@section('title', 'User')
@section('content')
  <h2>Hello, {{ $name }}!</h2>
@endsection
```

**How it works:**

Displays the name captured from the URL.

### Example 6: About page (`resources/views/pages/about.blade.php`)

```html
@extends('layouts.app')
@section('title', 'About')
@section('content')
  <h2>About us</h2>
  <p>A Laravel practice project for Term 2 students.</p>
@endsection
```

**How it works:**

A simple static page.

### Example 7: Contact page (`resources/views/pages/contact.blade.php`)

```html
@extends('layouts.app')
@section('title', 'Contact')
@section('content')
  <h2>Contact</h2>
  <p>Email: info@example.com</p>
@endsection
```

**How it works:**

The form is added in Session 04.

## 🧪 Lab Practice

1. Create the layout and the Home, About, Contact pages.
2. Visit `/user/123` and see the 404 caused by the constraint.
3. Add a `partials/footer.blade.php` and `@include` it.
4. Group three admin routes under `/admin` with names `admin.*`.
5. Use `$loop->first` and `$loop->last` to style the first and last list items.

## 📝 Assignment

Build a **Portfolio** with a master layout and pages: Home, Projects (list from an array with `@forelse`), Project detail (`/projects/{slug}`), and Contact. All links must use named routes.

## ❓ Quick Quiz

1. Which directive inserts a section into a layout?
   - a) @include
   - b) @yield
   - c) @extends
   - d) @php
2. How do you make a route parameter optional?
3. Which Blade syntax escapes output?
4. How do you generate a URL from a named route?
5. What does @forelse add over @foreach?

<details>
<summary>Show answers</summary>

1. b) @yield
2. Add `?` (e.g. `{level?}`) and give the function parameter a default.
3. `{{ }}`
4. `route('name', $params)`
5. An `@empty` block for empty collections.

</details>

## 💼 Interview Questions

1. **Why use named routes?**

   <details><summary>Model answer</summary>

   URLs can change in one place without breaking links; code is clearer.

   </details>

2. **Difference between {{ }} and {!! !!}?**

   <details><summary>Model answer</summary>

   {{ }} escapes HTML to prevent XSS; {!! !!} outputs raw HTML and should be used only for trusted content.

   </details>

3. **What are Blade layouts?**

   <details><summary>Model answer</summary>

   A master template with @yield placeholders that child views fill using @extends and @section, avoiding repeated HTML.

   </details>

## ✅ Summary

- Routes map URLs to closures, views or controllers.
- Parameters, constraints and names make routes flexible.
- Blade adds safe echo, control structures and layouts.
- Use @extends/@section/@yield and @include to avoid repetition.

---

[⬅ Previous](../Session-02-Fundamentals-and-MVC/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-04-Forms-and-Migrations/README.md)

<sub>Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad</sub>
