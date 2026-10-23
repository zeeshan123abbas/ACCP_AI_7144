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
