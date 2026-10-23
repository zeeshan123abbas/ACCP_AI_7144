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
