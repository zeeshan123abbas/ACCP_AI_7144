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
