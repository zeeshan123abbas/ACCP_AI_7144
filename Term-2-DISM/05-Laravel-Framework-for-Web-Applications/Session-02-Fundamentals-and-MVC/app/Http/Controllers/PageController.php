<?php
// php artisan make:controller PageController
namespace App\Http\Controllers;

class PageController extends Controller
{
    public function about()
    {
        $facts = [
            'framework' => 'Laravel ' . app()->version(),
            'php'       => PHP_VERSION,
            'app_name'  => config('app.name'),
            'today'     => now()->format('l, d M Y'),
            'slug'      => str('Aptech North Nazimabad')->slug(),
        ];
        return view('about', compact('facts'));
    }
}
