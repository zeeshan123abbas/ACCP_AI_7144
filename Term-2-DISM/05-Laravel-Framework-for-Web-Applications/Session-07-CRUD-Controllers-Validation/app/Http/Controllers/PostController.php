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
