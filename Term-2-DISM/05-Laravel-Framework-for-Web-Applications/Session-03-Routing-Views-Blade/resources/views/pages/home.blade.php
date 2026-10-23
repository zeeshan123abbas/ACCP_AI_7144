@extends('layouts.app')
@section('title', 'Home')
@section('content')
  <h1>Welcome!</h1>
  <p>Try <a href="{{ route('user.show', 'ayesha') }}">/user/ayesha</a> or
     <a href="{{ route('courses', 'beginner') }}">beginner courses</a>.</p>
@endsection
