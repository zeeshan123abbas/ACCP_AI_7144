<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"><title>Contact</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="container py-4" style="max-width:600px">
  <h2>Contact us</h2>
  @if (session('success'))
    <div class="alert alert-success">{{ session('success') }}</div>
  @endif
  <form method="POST" action="{{ route('contact.store') }}">
    @csrf
    <div class="mb-3">
      <label class="form-label">Name</label>
      <input name="name" value="{{ old('name') }}" class="form-control @error('name') is-invalid @enderror">
      @error('name') <div class="invalid-feedback">{{ $message }}</div> @enderror
    </div>
    <div class="mb-3">
      <label class="form-label">Email</label>
      <input name="email" type="email" value="{{ old('email') }}" class="form-control @error('email') is-invalid @enderror">
      @error('email') <div class="invalid-feedback">{{ $message }}</div> @enderror
    </div>
    <div class="mb-3">
      <label class="form-label">Subject</label>
      <input name="subject" value="{{ old('subject') }}" class="form-control">
    </div>
    <div class="mb-3">
      <label class="form-label">Message</label>
      <textarea name="message" rows="4" class="form-control @error('message') is-invalid @enderror">{{ old('message') }}</textarea>
      @error('message') <div class="invalid-feedback">{{ $message }}</div> @enderror
    </div>
    <button class="btn btn-primary">Send</button>
  </form>
</body>
</html>
