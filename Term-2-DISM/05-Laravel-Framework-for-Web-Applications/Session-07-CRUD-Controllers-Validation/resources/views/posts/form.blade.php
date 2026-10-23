@extends('layouts.app')
@section('content')
<h2>{{ $post->exists ? 'Edit post' : 'New post' }}</h2>
<form method="POST" action="{{ $post->exists ? route('posts.update', $post) : route('posts.store') }}">
  @csrf
  @if ($post->exists) @method('PUT') @endif
  <div class="mb-3">
    <label class="form-label">Title</label>
    <input name="title" value="{{ old('title', $post->title) }}" class="form-control @error('title') is-invalid @enderror">
    @error('title') <div class="invalid-feedback">{{ $message }}</div> @enderror
  </div>
  <div class="mb-3">
    <label class="form-label">Category</label>
    <select name="category_id" class="form-select">
      <option value="">— none —</option>
      @foreach ($categories as $c)
        <option value="{{ $c->id }}" @selected(old('category_id', $post->category_id) == $c->id)>{{ $c->name }}</option>
      @endforeach
    </select>
  </div>
  <div class="mb-3">
    <label class="form-label">Body</label>
    <textarea name="body" rows="6" class="form-control @error('body') is-invalid @enderror">{{ old('body', $post->body) }}</textarea>
    @error('body') <div class="invalid-feedback">{{ $message }}</div> @enderror
  </div>
  <div class="form-check mb-3">
    <input type="checkbox" name="is_published" value="1" class="form-check-input" id="pub" @checked(old('is_published', $post->is_published))>
    <label for="pub" class="form-check-label">Published</label>
  </div>
  <button class="btn btn-success">Save</button>
  <a href="{{ route('posts.index') }}" class="btn btn-link">Cancel</a>
</form>
@endsection
