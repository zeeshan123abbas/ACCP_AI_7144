<?php
// php artisan make:controller ContactController
namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class ContactController extends Controller
{
    public function create()
    {
        return view('contact');
    }

    public function store(Request $request)
    {
        $data = $request->validate([
            'name'    => 'required|string|min:3|max:100',
            'email'   => 'required|email',
            'subject' => 'nullable|string|max:150',
            'message' => 'required|string|min:10',
        ]);

        DB::table('messages')->insert($data + ['created_at' => now(), 'updated_at' => now()]);

        return redirect()->route('contact.create')->with('success', 'Thanks! We will reply soon.');
    }
}
