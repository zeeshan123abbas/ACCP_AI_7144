{{-- resources/views/about.blade.php --}}
<!DOCTYPE html>
<html>
<head><title>About</title></head>
<body style="font-family:sans-serif">
  <h1>About this app</h1>
  <ul>
    @foreach ($facts as $key => $value)
      <li><strong>{{ $key }}</strong>: {{ $value }}</li>
    @endforeach
  </ul>
  <a href="{{ url('/') }}">Home</a>
</body>
</html>
