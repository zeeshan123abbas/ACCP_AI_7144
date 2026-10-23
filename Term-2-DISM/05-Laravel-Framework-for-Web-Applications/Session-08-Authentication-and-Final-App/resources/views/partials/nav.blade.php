<nav class="navbar navbar-expand bg-dark navbar-dark px-3">
  <a class="navbar-brand" href="{{ route('home') }}">Student Blog</a>
  <div class="ms-auto d-flex gap-2 align-items-center">
    @auth
      <span class="text-light">Hi, {{ auth()->user()->name }}</span>
      <a class="btn btn-sm btn-success" href="{{ route('posts.create') }}">Write</a>
      @if (auth()->user()->role === 'admin')
        <a class="btn btn-sm btn-warning" href="{{ route('admin.home') }}">Admin</a>
      @endif
      <form method="POST" action="{{ route('logout') }}">@csrf <button class="btn btn-sm btn-outline-light">Logout</button></form>
    @endauth
    @guest
      <a class="btn btn-sm btn-outline-light" href="{{ route('login') }}">Login</a>
      <a class="btn btn-sm btn-light" href="{{ route('register') }}">Register</a>
    @endguest
  </div>
</nav>
