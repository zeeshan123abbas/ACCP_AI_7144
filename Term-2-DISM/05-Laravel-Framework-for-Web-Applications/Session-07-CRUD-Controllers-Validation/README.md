# Session 07: CRUD with Resource Controllers and Validation

> Module: Laravel Framework for Web Applications using PHP · Term 2 (DISM) · ⏱ ~2 hours

## 🎯 Learning Objectives

By the end of this session you will be able to:

- Create resource routes and controllers
- Describe the Laravel request/response lifecycle
- Validate with Form Request classes
- Use route model binding, flash messages and pagination
- Build a complete Post CRUD

## 📖 Concepts Explained

### 1. Resource routes

`Route::resource('posts', PostController::class);` creates seven routes:

| Verb | URI | Action | Name |
|---|---|---|---|
| GET | /posts | index | posts.index |
| GET | /posts/create | create | posts.create |
| POST | /posts | store | posts.store |
| GET | /posts/{post} | show | posts.show |
| GET | /posts/{post}/edit | edit | posts.edit |
| PUT/PATCH | /posts/{post} | update | posts.update |
| DELETE | /posts/{post} | destroy | posts.destroy |

Generate with `php artisan make:controller PostController --resource --model=Post`.

### 2. Request lifecycle

`public/index.php` → app bootstrapped (`bootstrap/app.php`) → HTTP kernel & **middleware** (sessions, CSRF) → **router** → controller → response passes back through middleware → browser.

### 3. Route model binding

Type-hint `Post $post` and Laravel loads the record from `{post}` automatically (404 if missing).

### 4. Form Requests

`php artisan make:request StorePostRequest` moves validation rules out of the controller. The controller receives already-validated data with `$request->validated()`.

### 5. Flash & pagination

`return redirect()->route('posts.index')->with('success', '...')` stores a one-time message. `Post::latest()->paginate(10)` plus `{{ $posts->links() }}` gives pagination (call `Paginator::useBootstrapFive()` in `AppServiceProvider::boot()` for Bootstrap styling).

## 💻 Code Examples

All examples below are also saved as files in this folder, so you can open and run them directly.

### Example 1: Resource controller (`app/Http/Controllers/PostController.php`)

```php
<?php
namespace App\Http\Controllers;

use App\Http\Requests\StorePostRequest;
use App\Models\{Category, Post};
use Illuminate\Http\Request;

class PostController extends Controller
{
    public function index(Request $request)
    {
        $posts = Post::with('category')
            ->search($request->query('q'))
            ->latest()
            ->paginate(10)
            ->withQueryString();
        return view('posts.index', compact('posts'));
    }

    public function create()
    {
        return view('posts.form', ['post' => new Post(), 'categories' => Category::orderBy('name')->get()]);
    }

    public function store(StorePostRequest $request)
    {
        Post::create($request->validated());
        return redirect()->route('posts.index')->with('success', 'Post created.');
    }

    public function show(Post $post)
    {
        return view('posts.show', compact('post'));
    }

    public function edit(Post $post)
    {
        return view('posts.form', ['post' => $post, 'categories' => Category::orderBy('name')->get()]);
    }

    public function update(StorePostRequest $request, Post $post)
    {
        $post->update($request->validated());
        return redirect()->route('posts.index')->with('success', 'Post updated.');
    }

    public function destroy(Post $post)
    {
        $post->delete();
        return back()->with('success', 'Post deleted.');
    }
}
```

**How it works:**

Each action is tiny thanks to route model binding, Form Requests and Eloquent. `withQueryString()` keeps `?q=` on pagination links.

### Example 2: Form Request validation (`app/Http/Requests/StorePostRequest.php`)

```php
<?php
namespace App\Http\Requests;

use Illuminate\Foundation\Http\FormRequest;

class StorePostRequest extends FormRequest
{
    public function authorize(): bool
    {
        return true;   // Session 08 restricts this to logged-in users
    }

    public function rules(): array
    {
        return [
            'title'        => ['required', 'string', 'min:5', 'max:150'],
            'body'         => ['required', 'string', 'min:20'],
            'category_id'  => ['nullable', 'exists:categories,id'],
            'is_published' => ['boolean'],
        ];
    }

    protected function prepareForValidation(): void
    {
        $this->merge(['is_published' => $this->boolean('is_published')]);
    }

    public function messages(): array
    {
        return ['body.min' => 'Please write at least 20 characters.'];
    }
}
```

**How it works:**

`exists:categories,id` makes sure the chosen category is real. An unchecked checkbox sends nothing, so `prepareForValidation` converts it to false.

### Example 3: Resource route (`routes/web.php`)

```php
<?php
use App\Http\Controllers\PostController;
use Illuminate\Support\Facades\Route;

Route::redirect('/', '/posts');
Route::resource('posts', PostController::class);
```

**How it works:**

One line registers all seven CRUD routes.

### Example 4: List with search, pagination and delete (`resources/views/posts/index.blade.php`)

```html
@extends('layouts.app')
@section('content')
<div class="d-flex justify-content-between align-items-center mb-3">
  <h2>Posts</h2>
  <a href="{{ route('posts.create') }}" class="btn btn-primary">New post</a>
</div>
@if (session('success')) <div class="alert alert-success">{{ session('success') }}</div> @endif
<form class="mb-3"><input name="q" value="{{ request('q') }}" class="form-control" placeholder="Search titles..."></form>
<table class="table">
  <tr><th>Title</th><th>Category</th><th>Status</th><th></th></tr>
  @forelse ($posts as $post)
  <tr>
    <td><a href="{{ route('posts.show', $post) }}">{{ $post->title }}</a></td>
    <td>{{ $post->category?->name ?? '—' }}</td>
    <td>{!! $post->is_published ? '<span class="badge bg-success">Published</span>' : '<span class="badge bg-secondary">Draft</span>' !!}</td>
    <td class="text-end">
      <a href="{{ route('posts.edit', $post) }}" class="btn btn-sm btn-outline-primary">Edit</a>
      <form action="{{ route('posts.destroy', $post) }}" method="POST" class="d-inline" onsubmit="return confirm('Delete?')">
        @csrf @method('DELETE')
        <button class="btn btn-sm btn-outline-danger">Delete</button>
      </form>
    </td>
  </tr>
  @empty
  <tr><td colspan="4">No posts found.</td></tr>
  @endforelse
</table>
{{ $posts->links() }}
@endsection
```

**How it works:**

`@method('DELETE')` turns the POST form into a DELETE request; `$posts->links()` renders pagination.

### Example 5: One form for create and edit (`resources/views/posts/form.blade.php`)

```html
@extends('layouts.app')
@section('content')
<h2>{{ $post->exists ? 'Edit post' : 'New post' }}</h2>
<form method="POST" action="{{ $post->exists ? route('posts.update', $post) : route('posts.store') }}">
  @csrf
  @if ($post->exists) @method('PUT') @endif
  <div class="mb-3">
    <label class="form-label">Title</label>
    <input name="title" value="{{ old('title', $post->title) }}" class="form-control @error('title') is-invalid @enderror">
    @error('title') <div class="invalid-feedback">{{ $message }}</div> @enderror
  </div>
  <div class="mb-3">
    <label class="form-label">Category</label>
    <select name="category_id" class="form-select">
      <option value="">— none —</option>
      @foreach ($categories as $c)
        <option value="{{ $c->id }}" @selected(old('category_id', $post->category_id) == $c->id)>{{ $c->name }}</option>
      @endforeach
    </select>
  </div>
  <div class="mb-3">
    <label class="form-label">Body</label>
    <textarea name="body" rows="6" class="form-control @error('body') is-invalid @enderror">{{ old('body', $post->body) }}</textarea>
    @error('body') <div class="invalid-feedback">{{ $message }}</div> @enderror
  </div>
  <div class="form-check mb-3">
    <input type="checkbox" name="is_published" value="1" class="form-check-input" id="pub" @checked(old('is_published', $post->is_published))>
    <label for="pub" class="form-check-label">Published</label>
  </div>
  <button class="btn btn-success">Save</button>
  <a href="{{ route('posts.index') }}" class="btn btn-link">Cancel</a>
</form>
@endsection
```

**How it works:**

`$post->exists` switches between create and edit; `old('title', $post->title)` prefers the user's last input.

### Example 6: Single post (`resources/views/posts/show.blade.php`)

```html
@extends('layouts.app')
@section('content')
  <h2>{{ $post->title }}</h2>
  <p class="text-muted">{{ $post->category?->name }} · {{ $post->created_at->diffForHumans() }}</p>
  <div>{!! nl2br(e($post->body)) !!}</div>
  <a href="{{ route('posts.index') }}">&larr; Back</a>
@endsection
```

**How it works:**

`e()` escapes the body first, then `nl2br` keeps line breaks.

### Example 7: Layout (`resources/views/layouts/app.blade.php`)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"><title>Blog</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body><main class="container py-4">@yield('content')</main></body>
</html>
```

**How it works:**

Minimal Bootstrap layout used by the post views.

## 🧪 Lab Practice

1. Generate the controller with `--resource --model=Post` and the Form Request.
2. Run `php artisan route:list --name=posts`.
3. Create, edit and delete posts; trigger every validation error.
4. Enable Bootstrap pagination in `AppServiceProvider` and seed 50 posts to test it.
5. Add a category filter dropdown to the index page.

## 📝 Assignment

Build a complete **Student Information CRUD** in Laravel (`students`: name, roll_no unique, email unique, course, city, photo optional) with a resource controller, Form Request (unique rules that ignore the current record on update: `Rule::unique('students')->ignore($student)`), search, pagination and flash messages.

## ❓ Quick Quiz

1. How many routes does Route::resource create?
   - a) 4
   - b) 5
   - c) 7
   - d) 9
2. How does an HTML form send a DELETE request?
3. What is route model binding?
4. Command to create a Form Request?
5. Which method renders pagination links?

<details>
<summary>Show answers</summary>

1. c) 7
2. POST with `@method('DELETE')`.
3. Laravel automatically loads the model matching the route parameter, or returns 404.
4. `php artisan make:request StorePostRequest`
5. `$posts->links()`

</details>

## 💼 Interview Questions

1. **Describe the Laravel request lifecycle.**

   <details><summary>Model answer</summary>

   Request enters public/index.php, the application boots, global and route middleware run, the router dispatches to a controller, which returns a response that travels back through middleware to the client.

   </details>

2. **Why use Form Requests?**

   <details><summary>Model answer</summary>

   They keep controllers thin, centralise validation and authorization, and are reusable for store and update.

   </details>

3. **What are flash messages?**

   <details><summary>Model answer</summary>

   Session data that survives exactly one subsequent request, ideal for success/error notices after redirects.

   </details>

## ✅ Summary

- Route::resource maps seven CRUD routes to a controller.
- Route model binding loads records automatically.
- Form Requests hold validation rules.
- Flash messages and paginate() complete a polished CRUD.

---

[⬅ Previous](../Session-06-Eloquent-Relationships/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-08-Authentication-and-Final-App/README.md)

<sub>Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad</sub>
