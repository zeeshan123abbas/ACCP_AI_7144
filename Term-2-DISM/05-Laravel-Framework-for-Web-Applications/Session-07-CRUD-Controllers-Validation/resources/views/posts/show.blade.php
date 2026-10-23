@extends('layouts.app')
@section('content')
  <h2>{{ $post->title }}</h2>
  <p class="text-muted">{{ $post->category?->name }} · {{ $post->created_at->diffForHumans() }}</p>
  <div>{!! nl2br(e($post->body)) !!}</div>
  <a href="{{ route('posts.index') }}">&larr; Back</a>
@endsection
