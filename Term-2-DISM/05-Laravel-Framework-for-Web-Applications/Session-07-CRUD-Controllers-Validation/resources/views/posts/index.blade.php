@extends('layouts.app')
@section('content')
<div class="d-flex justify-content-between align-items-center mb-3">
  <h2>Posts</h2>
  <a href="{{ route('posts.create') }}" class="btn btn-primary">New post</a>
</div>
@if (session('success')) <div class="alert alert-success">{{ session('success') }}</div> @endif
<form class="mb-3"><input name="q" value="{{ request('q') }}" class="form-control" placeholder="Search titles..."></form>
<table class="table">
  <tr><th>Title</th><th>Category</th><th>Status</th><th></th></tr>
  @forelse ($posts as $post)
  <tr>
    <td><a href="{{ route('posts.show', $post) }}">{{ $post->title }}</a></td>
    <td>{{ $post->category?->name ?? '—' }}</td>
    <td>{!! $post->is_published ? '<span class="badge bg-success">Published</span>' : '<span class="badge bg-secondary">Draft</span>' !!}</td>
    <td class="text-end">
      <a href="{{ route('posts.edit', $post) }}" class="btn btn-sm btn-outline-primary">Edit</a>
      <form action="{{ route('posts.destroy', $post) }}" method="POST" class="d-inline" onsubmit="return confirm('Delete?')">
        @csrf @method('DELETE')
        <button class="btn btn-sm btn-outline-danger">Delete</button>
      </form>
    </td>
  </tr>
  @empty
  <tr><td colspan="4">No posts found.</td></tr>
  @endforelse
</table>
{{ $posts->links() }}
@endsection
