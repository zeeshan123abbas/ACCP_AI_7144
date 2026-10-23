<?php
namespace App\Models;

use Illuminate\Database\Eloquent\Builder;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\{BelongsTo, BelongsToMany};
use Illuminate\Database\Eloquent\SoftDeletes;
use Illuminate\Support\Str;

class Post extends Model
{
    use HasFactory, SoftDeletes;

    protected $fillable = ['title', 'body', 'is_published', 'category_id'];
    protected function casts(): array { return ['is_published' => 'boolean']; }

    public function category(): BelongsTo { return $this->belongsTo(Category::class); }
    public function tags(): BelongsToMany { return $this->belongsToMany(Tag::class); }

    public function scopePublished(Builder $q): void { $q->where('is_published', true); }
    public function scopeSearch(Builder $q, ?string $term): void
    {
        $q->when($term, fn ($q) => $q->where('title', 'like', "%{$term}%"));
    }

    protected static function booted(): void
    {
        static::creating(function (Post $post) {
            $post->slug = Str::slug($post->title) . '-' . Str::random(5);
        });
    }
}
