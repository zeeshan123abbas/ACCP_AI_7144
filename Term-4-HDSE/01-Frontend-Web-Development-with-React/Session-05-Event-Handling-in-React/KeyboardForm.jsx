import { useState } from "react";

export default function KeyboardForm() {
  const [text, setText] = useState("");
  const [todos, setTodos] = useState([]);
  const [focused, setFocused] = useState(false);

  function addTodo() {
    if (!text.trim()) return;
    setTodos((prev) => [...prev, { id: Date.now(), text: text.trim() }]);
    setText("");
  }

  function handleKeyDown(e) {
    if (e.key === "Enter") addTodo();
    if (e.key === "Escape") setText("");
  }

  function handleSubmit(e) {
    e.preventDefault(); // stop the page from reloading
    addTodo();
  }

  return (
    <form onSubmit={handleSubmit}>
      <h2>Keyboard & form events</h2>
      <input
        value={text}
        onChange={(e) => setText(e.target.value)}
        onKeyDown={handleKeyDown}
        onFocus={() => setFocused(true)}
        onBlur={() => setFocused(false)}
        placeholder="Type a task and press Enter"
        style={{ outline: focused ? "2px solid #0d6efd" : "none" }}
      />
      <button type="submit">Add</button>
      <small> {text.length}/50 characters</small>
      <ul>{todos.map((t) => <li key={t.id}>{t.text}</li>)}</ul>
    </form>
  );
}
