<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>@yield('title', 'Student Portal')</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
  <nav class="navbar navbar-expand bg-dark navbar-dark px-3">
    <a class="navbar-brand" href="{{ route('home') }}">Student Portal</a>
    <div class="navbar-nav">
      <a class="nav-link {{ request()->routeIs('about') ? 'active' : '' }}" href="{{ route('about') }}">About</a>
      <a class="nav-link {{ request()->routeIs('courses') ? 'active' : '' }}" href="{{ route('courses') }}">Courses</a>
      <a class="nav-link {{ request()->routeIs('contact') ? 'active' : '' }}" href="{{ route('contact') }}">Contact</a>
    </div>
  </nav>
  <main class="container py-4">
    @yield('content')
  </main>
  <footer class="text-center text-muted py-3">&copy; {{ date('Y') }} Student Portal</footer>
</body>
</html>
