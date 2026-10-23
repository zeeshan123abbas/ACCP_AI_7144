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
