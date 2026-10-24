// web/main.dart
// Dart code that runs in the browser using package:web.
//
// Build it:  dart compile js web/main.dart -o web/main.dart.js
// Then open web/index.html with a local server (see the session notes).

import 'package:web/web.dart';

void main() {
  setupCounter();
  setupForm();
  showTopics();
}

// ---------- Example 1: Click counter ----------
void setupCounter() {
  // Find the elements by their id. "as" tells Dart the exact element type.
  final countSpan = document.querySelector('#count') as HTMLSpanElement;
  final plusButton = document.querySelector('#plus-btn') as HTMLButtonElement;
  final resetButton = document.querySelector('#reset-btn') as HTMLButtonElement;

  int count = 0;

  // onClick is a Stream of click events. listen() runs our code on each click.
  plusButton.onClick.listen((event) {
    count++;
    countSpan.textContent = '$count';
  });

  resetButton.onClick.listen((event) {
    count = 0;
    countSpan.textContent = '0';
  });
}

// ---------- Example 2: Form handling ----------
void setupForm() {
  final form = document.querySelector('#register-form') as HTMLFormElement;
  final nameInput = document.querySelector('#name-input') as HTMLInputElement;
  final ageInput = document.querySelector('#age-input') as HTMLInputElement;
  final courseSelect = document.querySelector('#course-select') as HTMLSelectElement;
  final message = document.querySelector('#form-message') as HTMLParagraphElement;

  form.onSubmit.listen((event) {
    // Stop the browser from reloading the page.
    event.preventDefault();

    // Read the values the user typed.
    String name = nameInput.value.trim();
    int? age = int.tryParse(ageInput.value); // null if not a number
    String course = courseSelect.value;

    // Validate step by step and show a helpful message.
    if (name.isEmpty) {
      showMessage(message, 'Please enter your name.', isError: true);
      return;
    }
    if (age == null || age < 15) {
      showMessage(message, 'Please enter a valid age (15 or above).', isError: true);
      return;
    }

    showMessage(message, 'Thank you $name! You are registered for $course.');
    form.reset(); // clear the form
  });
}

// Writes a message and switches its CSS class for colour.
void showMessage(HTMLParagraphElement element, String text, {bool isError = false}) {
  element.textContent = text;
  element.className = isError ? 'error' : 'success';
}

// ---------- Example 3: Build HTML from Dart data ----------
void showTopics() {
  final list = document.querySelector('#topic-list') as HTMLUListElement;
  List<String> topics = ['Null safety', 'Classes', 'Async', 'Packages', 'AI'];

  for (String topic in topics) {
    // Create a new <li> element and add it to the list.
    final item = document.createElement('li') as HTMLLIElement;
    item.textContent = topic;
    list.appendChild(item);
  }
}
