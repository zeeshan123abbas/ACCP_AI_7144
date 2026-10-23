import { useState } from "react";

export default function ClickDemo() {
  const [message, setMessage] = useState("Nothing yet");
  const [hover, setHover] = useState(false);

  function greet(name) {
    setMessage(`Hello ${name}! Clicked at ${new Date().toLocaleTimeString()}`);
  }

  return (
    <section>
      <h2>Mouse events</h2>
      <button onClick={() => greet("Ahmed")}>Greet Ahmed</button>
      <button onDoubleClick={() => setMessage("Double click detected")}>Double-click me</button>
      <div
        onMouseEnter={() => setHover(true)}
        onMouseLeave={() => setHover(false)}
        style={{ marginTop: 12, padding: 20, background: hover ? "#ffe08a" : "#eee" }}
      >
        {hover ? "Mouse is over me" : "Hover over this box"}
      </div>
      <p>{message}</p>
    </section>
  );
}
