@extends('layouts.app')
@section('title', 'Courses')
@section('content')
  <h2>Courses ({{ $level }})</h2>
  <ul class="list-group">
    @forelse ($courses as $course)
      <li class="list-group-item">{{ $loop->iteration }}. {{ $course['title'] }}
        @if ($course['level'] === 'advanced') <span class="badge bg-danger">Advanced</span> @endif
      </li>
    @empty
      <li class="list-group-item">No courses at this level.</li>
    @endforelse
  </ul>
@endsection
