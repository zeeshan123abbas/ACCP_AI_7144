@extends('layouts.app')
@section('content')
  <h2>Admin: users</h2>
  <table class="table">
    <tr><th>Name</th><th>Email</th><th>Role</th><th>Posts</th></tr>
    @foreach ($users as $u)
      <tr><td>{{ $u->name }}</td><td>{{ $u->email }}</td><td>{{ $u->role }}</td><td>{{ $u->posts_count }}</td></tr>
    @endforeach
  </table>
@endsection
