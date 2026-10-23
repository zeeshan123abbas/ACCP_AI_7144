# Session 05: Eloquent ORM Essentials

> Module: Laravel Framework for Web Applications using PHP · Term 2 (DISM) · ⏱ ~2 hours

## 🎯 Learning Objectives

By the end of this session you will be able to:

- Explain what an ORM is
- Generate models with migrations, factories and seeders
- Follow Eloquent naming conventions
- Create, read, update and delete records with Eloquent
- Experiment with queries in Tinker

## 📖 Concepts Explained

### 1. What is an ORM?

An **Object-Relational Mapper** lets you work with database rows as PHP objects. Instead of `SELECT * FROM posts WHERE id = 5` you write `Post::find(5)`. Eloquent builds safe SQL (prepared statements) for you.

### 2. Conventions

| Model | Table | Primary key | Timestamps |
|---|---|---|---|
| `Post` | `posts` | `id` | `created_at`, `updated_at` |
| `Category` | `categories` | `id` | yes |

Override when needed: `protected $table = 'blog_posts';`, `public $timestamps = false;`.

### 3. Mass assignment

`Post::create($request->all())` is only allowed for columns listed in `$fillable` (or not in `$guarded`). This stops attackers from submitting fields like `is_admin=1`.

### 4. Core methods

| Task | Code |
|---|---|
| all rows | `Post::all()` |
| by id | `Post::find(1)`, `Post::findOrFail(1)` (404 if missing) |
| filter | `Post::where('status', 'published')->orderByDesc('id')->get()` |
| first match | `->first()` |
| count | `Post::count()` |
| insert | `Post::create([...])` or `new Post; ...; $post->save()` |
| update | `$post->update([...])` |
| delete | `$post->delete()` or `Post::destroy([1,2])` |

### 5. Tinker

`php artisan tinker` opens a REPL connected to your app — perfect to test queries.

## 💻 Code Examples

All examples below are also saved as files in this folder, so you can open and run them directly.

### Example 1: Post model (`app/Models/Post.php`)

```php
<?php
// php artisan make:model Post -mfs   (model + migration + factory + seeder)
namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Post extends Model
{
    use HasFactory;

    protected $fillable = ['title', 'body', 'is_published'];

    protected function casts(): array
    {
        return ['is_published' => 'boolean'];
    }
}
```

**How it works:**

`$fillable` whitelists columns for mass assignment; `casts()` turns 0/1 into true/false.

### Example 2: Posts migration (`database/migrations/2025_01_02_000000_create_posts_table.php`)

```php
<?php
use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration {
    public function up(): void
    {
        Schema::create('posts', function (Blueprint $table) {
            $table->id();
            $table->string('title');
            $table->text('body');
            $table->boolean('is_published')->default(false);
            $table->timestamps();
        });
    }
    public function down(): void { Schema::dropIfExists('posts'); }
};
```

**How it works:**

Defines the `posts` table expected by the `Post` model.

### Example 3: Factory for fake data (`database/factories/PostFactory.php`)

```php
<?php
namespace Database\Factories;

use Illuminate\Database\Eloquent\Factories\Factory;

class PostFactory extends Factory
{
    public function definition(): array
    {
        return [
            'title'        => fake()->sentence(6),
            'body'         => fake()->paragraphs(3, true),
            'is_published' => fake()->boolean(70),
        ];
    }
}
```

**How it works:**

Generates realistic test posts; 70% will be published.

### Example 4: Seeder (`database/seeders/DatabaseSeeder.php`)

```php
<?php
namespace Database\Seeders;

use App\Models\Post;
use Illuminate\Database\Seeder;

class DatabaseSeeder extends Seeder
{
    public function run(): void
    {
        Post::factory()->count(20)->create();
    }
}
```

**How it works:**

`php artisan db:seed` (or `migrate:fresh --seed`) inserts 20 posts.

### Example 5: Eloquent in Tinker (`tinker-practice.md`)

```markdown
# php artisan tinker

```php
Post::count();
Post::create(['title' => 'Hello Eloquent', 'body' => 'My first post', 'is_published' => true]);
$p = Post::find(1);
$p->title;
$p->update(['title' => 'Updated title']);
Post::where('is_published', true)->latest()->take(5)->pluck('title');
Post::where('title', 'like', '%Eloquent%')->first();
$p->delete();
Post::findOrFail(9999);   // throws ModelNotFoundException
```
```

**How it works:**

Paste each line into Tinker and watch the results; `pluck` returns just one column.

## 🧪 Lab Practice

1. Run `php artisan make:model Post -mfs`, paste the code and `php artisan migrate:fresh --seed`.
2. In Tinker, create, read, update and delete posts.
3. Try `Post::create(['title'=>'x','body'=>'y','id'=>999])` and observe that `id` is ignored.
4. Write a route `/posts` that lists published post titles with Eloquent.
5. Use `Post::query()->toSql()` to see the generated SQL.

## 📝 Assignment

Create a `Student` model (name, email unique, roll_no unique, city, gpa decimal) with migration, factory (50 students) and seeder. Add a `/students` page that shows the top 10 students by GPA and the count per city.

## ❓ Quick Quiz

1. Default table name for model `Category`?
   - a) category
   - b) categorys
   - c) categories
   - d) Category
2. What does $fillable protect against?
3. Difference between find() and findOrFail()?
4. Command for an interactive Eloquent shell?
5. What does `-mfs` add to make:model?

<details>
<summary>Show answers</summary>

1. c) categories
2. Mass assignment of unexpected fields.
3. find returns null if missing; findOrFail throws an exception that becomes a 404.
4. `php artisan tinker`
5. A migration, a factory and a seeder.

</details>

## 💼 Interview Questions

1. **What is an ORM and its pros/cons?**

   <details><summary>Model answer</summary>

   Maps tables to classes and rows to objects. Pros: productivity, readable code, built-in safety. Cons: can hide inefficient queries (N+1) and is slower for complex reporting than hand-written SQL.

   </details>

2. **What is mass assignment vulnerability?**

   <details><summary>Model answer</summary>

   Passing all request input to create/update lets attackers set protected columns; Laravel prevents it with $fillable/$guarded.

   </details>

3. **What are factories and seeders?**

   <details><summary>Model answer</summary>

   Factories define how to generate fake model data; seeders use them (or fixed data) to fill the database for development and testing.

   </details>

## ✅ Summary

- Eloquent maps tables to models using conventions.
- Use $fillable for safe mass assignment.
- all, find, where, create, update, delete cover CRUD.
- Factories, seeders and Tinker speed up development.

---

[⬅ Previous](../Session-04-Forms-and-Migrations/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-06-Eloquent-Relationships/README.md)

<sub>Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad</sub>
