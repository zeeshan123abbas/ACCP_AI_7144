```php
$tech = Category::create(['name' => 'Technology']);
$post = $tech->posts()->create(['title' => 'Why Laravel?', 'body' => '...', 'is_published' => true]);
$post->category->name;                       // "Technology"
$php = Tag::create(['name' => 'php']); $web = Tag::create(['name' => 'web']);
$post->tags()->attach([$php->id, $web->id]);
$post->tags->pluck('name');                  // ["php","web"]
$post->tags()->sync([$php->id]);             // keep only php

Post::with('category', 'tags')->published()->get();          // eager loading
Category::withCount('posts')->get()->pluck('posts_count', 'name');
Post::published()->get()->groupBy('category_id')->map->count();

$post->delete();                 // soft delete
Post::count();                   // excludes it
Post::withTrashed()->count();    // includes it
Post::onlyTrashed()->first()->restore();
```
